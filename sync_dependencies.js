#!/usr/bin/env node

/**
 * Sync Dependencies Script
 *
 * This script reads allskills.md from a specified folder and syncs
 * the dependency information to all individual topic files (T##_*.md).
 *
 * Usage: node sync_dependencies.js <folder_name>
 * Example: node sync_dependencies.js skillsv4
 */

const fs = require('fs');
const path = require('path');

// Parse command line arguments
const folderName = process.argv[2];

if (!folderName) {
  console.error('Error: Please provide a folder name');
  console.error('Usage: node sync_dependencies.js <folder_name>');
  console.error('Example: node sync_dependencies.js skillsv4');
  process.exit(1);
}

const folderPath = path.join(__dirname, folderName);
const allSkillsPath = path.join(folderPath, 'allskills.md');

// Validate folder and allskills.md exist
if (!fs.existsSync(folderPath)) {
  console.error(`Error: Folder "${folderName}" does not exist`);
  process.exit(1);
}

if (!fs.existsSync(allSkillsPath)) {
  console.error(`Error: allskills.md not found in "${folderName}"`);
  process.exit(1);
}

console.log(`Reading allskills.md from ${folderName}...`);

/**
 * Parse allskills.md and extract all skills with their dependencies
 */
function parseAllSkills(content) {
  const skills = {};
  const skillBlocks = content.split(/(?=^ID: T\d+\.G)/m);

  for (const block of skillBlocks) {
    if (!block.trim()) continue;

    const idMatch = block.match(/^ID: (T\d+\.G[K\d]\.?\d*)/m);
    if (!idMatch) continue;

    const skillId = idMatch[1];
    const topicMatch = skillId.match(/^(T\d+)\./);
    if (!topicMatch) continue;

    const topicId = topicMatch[1];

    // Extract the dependency section (note: it's "Dependencies:" in allskills.md)
    const dependencyMatch = block.match(/^Dependencies?:\s*\n([\s\S]*?)(?=\n(?:ID:|$))/m);
    const dependencies = [];

    if (dependencyMatch) {
      const depSection = dependencyMatch[1];
      const depLines = depSection.split('\n').filter(line => line.trim().startsWith('*'));

      for (const line of depLines) {
        const cleaned = line.trim().substring(1).trim(); // Remove leading *
        if (cleaned) {
          dependencies.push(cleaned);
        }
      }
    }

    if (!skills[topicId]) {
      skills[topicId] = {};
    }

    skills[topicId][skillId] = dependencies;
  }

  return skills;
}

/**
 * Find the topic file for a given topic ID (e.g., T01)
 */
function findTopicFile(topicId) {
  const files = fs.readdirSync(folderPath);
  const pattern = new RegExp(`^skills_${topicId}_.*\\.md$`);

  for (const file of files) {
    if (pattern.test(file)) {
      return path.join(folderPath, file);
    }
  }

  return null;
}

/**
 * Update a topic file with dependency information
 * Topic files use format: **T##.G#.## – Skill title**
 */
function updateTopicFile(topicId, skillDependencies) {
  const topicFilePath = findTopicFile(topicId);

  if (!topicFilePath) {
    console.log(`  ⚠ Topic file for ${topicId} not found, skipping...`);
    return { updated: 0, notFound: true };
  }

  let content = fs.readFileSync(topicFilePath, 'utf8');
  let updatedCount = 0;

  // Process each skill in this topic
  for (const [skillId, dependencies] of Object.entries(skillDependencies)) {
    // Escape dots in skill ID for regex
    const escapedId = skillId.replace(/\./g, '\\.');

    // Find the skill in the topic file
    // Format can be either:
    //   **T##.G#.## – Skill title**
    //   ### T##.G#.## – Skill title
    // Followed by description paragraphs
    // May or may not have a _Dependency:_ section before the next skill or ---

    // Try both patterns
    let skillRegex = new RegExp(
      `(\\*\\*${escapedId}[^*]*?\\*\\*[\\s\\S]*?)(?=(?:\\n\\*\\*T\\d+\\.G|\\n###\\s*T\\d+\\.G|\\n---|\\n##|$))`,
      'm'
    );

    let match = content.match(skillRegex);

    if (!match) {
      // Try ### pattern
      skillRegex = new RegExp(
        `(###\\s*${escapedId}[^\\n]*[\\s\\S]*?)(?=(?:\\n\\*\\*T\\d+\\.G|\\n###\\s*T\\d+\\.G|\\n---|\\n##(?!#)|$))`,
        'm'
      );
      match = content.match(skillRegex);
    }

    if (!match) {
      console.log(`  ⚠ Skill ${skillId} not found in ${path.basename(topicFilePath)}`);
      continue;
    }

    let skillBlock = match[1];

    // Check if dependency section already exists
    const hasDependency = /_Dependency:_/m.test(skillBlock);

    let newSkillBlock;

    if (dependencies.length === 0) {
      // No dependencies - remove any existing dependency section
      if (hasDependency) {
        newSkillBlock = skillBlock.replace(/\n_Dependency:_[\s\S]*?(?=\n(?:_Format:|$))/m, '');
        updatedCount++;
      } else {
        continue; // Nothing to do
      }
    } else {
      // Has dependencies - format them
      const dependencyText = '\n_Dependency:_\n' +
        dependencies.map(dep => `  * ${dep}`).join('\n') + '\n';

      if (hasDependency) {
        // Replace existing dependency section
        newSkillBlock = skillBlock.replace(
          /_Dependency:_[\s\S]*?(?=\n_Format:|$)/m,
          `_Dependency:_\n${dependencies.map(dep => `  * ${dep}`).join('\n')}\n`
        );
      } else {
        // Add dependency section before _Format:_ line or at the end of description
        const formatMatch = skillBlock.match(/\n(_Format:_)/);
        if (formatMatch) {
          // Insert before _Format:_
          newSkillBlock = skillBlock.replace(
            /\n(_Format:_)/,
            `${dependencyText}$1`
          );
        } else {
          // Add at the end
          newSkillBlock = skillBlock.trimEnd() + '\n' + dependencyText;
        }
      }
      updatedCount++;
    }

    // Replace the skill block in the content
    content = content.replace(skillBlock, newSkillBlock);
  }

  // Write the updated content back to the file
  fs.writeFileSync(topicFilePath, content, 'utf8');

  return { updated: updatedCount, notFound: false };
}

// Main execution
try {
  const allSkillsContent = fs.readFileSync(allSkillsPath, 'utf8');
  const skillsByTopic = parseAllSkills(allSkillsContent);

  console.log(`Parsed ${Object.keys(skillsByTopic).length} topics from allskills.md\n`);

  let totalUpdated = 0;
  let totalTopics = 0;
  let notFoundTopics = 0;

  // Process each topic
  for (let i = 1; i <= 36; i++) {
    const topicId = `T${i.toString().padStart(2, '0')}`;
    const skillDeps = skillsByTopic[topicId] || {};
    const topicFile = findTopicFile(topicId);

    if (topicFile) {
      console.log(`Processing ${path.basename(topicFile)}...`);
    } else {
      console.log(`Processing ${topicId}...`);
    }

    const result = updateTopicFile(topicId, skillDeps);

    if (result.notFound) {
      notFoundTopics++;
    } else {
      totalTopics++;
      totalUpdated += result.updated;
      console.log(`  ✓ Updated ${result.updated} skills`);
    }
  }

  console.log('\n' + '='.repeat(50));
  console.log('Sync Complete!');
  console.log('='.repeat(50));
  console.log(`Topics processed: ${totalTopics}`);
  console.log(`Topics not found: ${notFoundTopics}`);
  console.log(`Total skills updated: ${totalUpdated}`);
  console.log('='.repeat(50));

} catch (error) {
  console.error('Error:', error.message);
  console.error(error.stack);
  process.exit(1);
}
