#!/usr/bin/env node
/**
 * Export all skills from the specified skills folder into allskills.md
 *
 * Usage:
 *   node tools/export_all_skills.js [skills_folder]
 *
 * Example:
 *   node tools/export_all_skills.js skillsv4
 */

const fs = require("fs/promises");
const path = require("path");

const HEADING_REGEX = /^#{2,5}\s+(T\d{2}\.G(?:K|\d)\.\d{2})\s+–\s+(.*)$/;
const BOLD_LINE_REGEX = /^\*\*(T\d{2}\.G(?:K|\d)\.\d{2})\s+–\s+(.*?)\*\*\s*$/;
const DESCRIPTION_LINE_REGEX = /^-?\s*\*\*Description:\*\*\s*(.*)$/i;
const TOPIC_NAME_REGEX = /^#\s+(.*?)\s*$/;

async function main() {
  const folder = process.argv[2] || "skillsv4";
  const skillsDir = path.resolve(process.cwd(), folder);
  const outputPath = path.join(skillsDir, "allskills.md");

  let entries;
  try {
    entries = await fs.readdir(skillsDir, { withFileTypes: true });
  } catch (err) {
    console.error(`Failed to read folder "${skillsDir}": ${err.message}`);
    process.exit(1);
  }

  const skillFiles = entries
    .filter((entry) => entry.isFile() && entry.name.startsWith("skills_") && entry.name.endsWith(".md"))
    .map((entry) => entry.name)
    .sort();

  const outputLines = [];

  for (const fileName of skillFiles) {
    const filePath = path.join(skillsDir, fileName);
    const content = await fs.readFile(filePath, "utf8");
    const lines = content.split(/\r?\n/);

    let topicName = "";
    let simpleTopicName = path.basename(fileName, ".md");
    for (const line of lines) {
      const topicMatch = line.match(TOPIC_NAME_REGEX);
      if (topicMatch) {
        topicName = topicMatch[1].trim();
        // Strip trailing "Skill List ..." or "Skill List (..)" suffixes for cleaner topic names.
        let cleaned = topicName.replace(/:?\s*-?\s*K–?8\s+Skill\s+List.*$/i, "");
        cleaned = cleaned.replace(/\s*\(.*?\)\s*$/, "");
        const prefixMatch = cleaned.match(/^(T\d{2}\s+–\s+.+?)(?:\s*$|\s+\()/);
        simpleTopicName = prefixMatch ? prefixMatch[1] : cleaned || topicName;
        break;
      }
    }

    for (let i = 0; i < lines.length; i++) {
      let skillMatch = lines[i].match(HEADING_REGEX);
      let skillId, skillTitle;
      if (skillMatch) {
        [, skillId, skillTitle] = skillMatch;
      } else {
        const boldMatch = lines[i].match(BOLD_LINE_REGEX);
        if (boldMatch) {
          [, skillId, skillTitle] = boldMatch;
        } else {
          continue;
        }
      }
      let descriptionText = "";

      // Find the description line(s) after this skill heading/bold line.
      for (let j = i + 1; j < lines.length; j++) {
        const descMatch = lines[j].match(DESCRIPTION_LINE_REGEX);
        if (descMatch) {
          descriptionText = descMatch[1].trim();
          // Include continuation lines that are indented (until blank line or new bullet/heading).
          for (let k = j + 1; k < lines.length; k++) {
            const nextLine = lines[k];
            if (!nextLine.trim()) {
              break;
            }
            if (/^\s*-\s+\*\*/.test(nextLine) || /^#{1,6}\s+/.test(nextLine)) {
              break;
            }
            descriptionText += " " + nextLine.trim();
          }
          break;
        }
        const trimmed = lines[j].trim();
        if (!trimmed) {
          if (descriptionText) {
            break;
          }
          continue;
        }
        if (/^#{1,6}\s+/.test(trimmed) || /^\*\*(T\d{2}\.G[A-Z]?\d\.\d{2})\s+–/.test(trimmed)) {
          break;
        }
        if (/^_?Format/i.test(trimmed) || /^-?\s*\*\*Format/i.test(trimmed)) {
          if (descriptionText) {
            break;
          }
          continue;
        }
        if (!descriptionText) {
          descriptionText = trimmed;
        } else {
          descriptionText += " " + trimmed;
        }
      }

      outputLines.push(`ID: ${skillId}`);
      outputLines.push(`Topic: ${simpleTopicName}`);
      outputLines.push(`Skill: ${skillTitle}`);
      outputLines.push(`Description: ${descriptionText}`);
      outputLines.push(""); // blank line between skills
    }
  }

  await fs.writeFile(outputPath, outputLines.join("\n"), "utf8");
  console.log(`Exported ${outputLines.filter((line) => line.startsWith("ID:")).length} skills to ${outputPath}`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
