#!/usr/bin/env node

/**
 * Dependency Analysis Agent for T14-T24 (Applications Domain)
 * Analyzes 346 application skills and maps dependencies to programming core (T06-T13)
 */

const fs = require('fs');
const path = require('path');

// Load input data
console.log('Loading skill data...');
const skillsT14T24 = JSON.parse(fs.readFileSync('skills_T14_T24_extracted.json', 'utf8'));
const depsT01T05 = JSON.parse(fs.readFileSync('dependencies_T01_T05.json', 'utf8'));
const depsT06T13 = JSON.parse(fs.readFileSync('dependencies_T06_T13.json', 'utf8'));

console.log(`Loaded ${skillsT14T24.length} application skills`);
console.log(`Loaded ${depsT01T05.length} T01-T05 dependencies`);
console.log(`Loaded ${depsT06T13.length} T06-T13 dependencies`);

// Create lookup maps
const skillMap = {};
skillsT14T24.forEach(skill => {
  skillMap[skill.id] = skill;
});

// Create grade lookup for validation
const gradeMap = {};
[...skillsT14T24, ...depsT01T05, ...depsT06T13].forEach(item => {
  if (item.id) {
    const match = item.id.match(/\.G(\d+)\./);
    if (match) {
      gradeMap[item.id] = parseInt(match[1]);
    }
  }
});

// Dependency pattern rules by topic
const dependencyPatterns = {
  // T14: 2D Games
  T14: {
    keywords: ['game', 'sprite', 'move', 'collision', 'score', 'level', 'player', 'enemy'],
    coreDeps: {
      movement: ['T06.G3.01', 'T07.G3.01', 'T09.G3.01'], // events, loops, variables
      collision: ['T08.G3.01', 'T09.G3.01'], // conditionals, variables
      scoring: ['T09.G3.01', 'T08.G3.01'], // variables, conditionals
      states: ['T08.G3.01', 'T11.G3.01'], // conditionals, functions
      multiLevel: ['T12.G3.01', 'T10.G3.01'] // organization, lists
    }
  },
  // T15: Stories/Animation
  T15: {
    keywords: ['story', 'scene', 'animation', 'character', 'dialogue', 'narrative', 'media'],
    coreDeps: {
      sceneControl: ['T06.G3.01', 'T12.G3.01'], // events, organization
      animation: ['T07.G3.01', 'T09.G3.01'], // loops, variables
      branching: ['T08.G3.01'], // conditionals
      dialogue: ['T09.G3.01', 'T10.G3.01'], // variables, lists
      behaviors: ['T11.G3.01'] // functions
    }
  },
  // T16: UI/Widgets
  T16: {
    keywords: ['ui', 'widget', 'button', 'input', 'form', 'menu', 'interface', 'control'],
    coreDeps: {
      interactive: ['T06.G3.01'], // events
      input: ['T09.G3.01', 'T08.G3.01'], // variables, validation
      forms: ['T10.G3.01', 'T08.G3.01'], // lists, conditionals
      library: ['T11.G3.01', 'T12.G3.01'] // functions, organization
    }
  },
  // T17: Physics
  T17: {
    keywords: ['physics', 'motion', 'gravity', 'force', 'velocity', 'acceleration', 'simulation'],
    coreDeps: {
      motion: ['T07.G3.01', 'T09.G3.01'], // loops, variables
      forces: ['T08.G3.01', 'T09.G3.01'], // conditionals, variables
      collision: ['T08.G3.01', 'T09.G3.01'] // conditionals, variables
    },
    crossAppDeps: ['T14'] // builds on 2D games
  },
  // T18: 3D Worlds
  T18: {
    keywords: ['3d', 'world', 'camera', 'perspective', 'coordinate', 'depth'],
    coreDeps: {
      movement3d: ['T06.G3.01', 'T09.G3.01'], // events, variables (x/y/z)
      camera: ['T09.G3.01', 'T08.G3.01'], // variables, conditionals
      collision3d: ['T08.G3.01'] // conditionals
    },
    crossAppDeps: ['T14'] // 2D game patterns in 3D
  },
  // T19: Multiplayer
  T19: {
    keywords: ['multiplayer', 'player', 'turn', 'network', 'sync', 'connected'],
    coreDeps: {
      playerData: ['T10.G4.01', 'T09.G4.01'], // lists, variables
      sync: ['T08.G4.01', 'T11.G4.01'], // conditionals, functions
      turnBased: ['T08.G4.01', 'T09.G4.01'] // conditionals, state
    },
    crossAppDeps: ['T14', 'T18'] // builds on games
  },
  // T20: Algorithmic Art
  T20: {
    keywords: ['art', 'pattern', 'generative', 'parametric', 'design', 'aesthetic'],
    coreDeps: {
      patterns: ['T07.G3.01', 'T09.G3.01'], // loops, parameters
      generative: ['T04.G3.01', 'T11.G3.01'], // patterns, functions
      parametric: ['T09.G3.01', 'T07.G3.01'] // variables, loops
    }
  },
  // T21: AI Media
  T21: {
    keywords: ['ai', 'media', 'image', 'audio', 'generate', 'api', 'model'],
    coreDeps: {
      apiCalls: ['T06.G4.01', 'T09.G4.01'], // events, variables
      generation: ['T10.G4.01', 'T08.G4.01'], // lists, conditionals
    },
    crossAppDeps: ['T15', 'T16'], // media + UI
    designDeps: ['T05.G4.01'] // HCD for AI
  },
  // T22: AI Chatbots
  T22: {
    keywords: ['chatbot', 'conversation', 'dialogue', 'chat', 'ai', 'nlp', 'response'],
    coreDeps: {
      conversation: ['T08.G4.01', 'T10.G4.01'], // conditionals, lists
      input: ['T06.G4.01', 'T09.G4.01'], // events, variables
      context: ['T09.G4.01', 'T10.G4.01'] // variables, lists
    },
    crossAppDeps: ['T16'], // UI widgets
    designDeps: ['T05.G4.01'] // HCD for ethics
  },
  // T23: AI Voice/Vision/Gesture
  T23: {
    keywords: ['voice', 'vision', 'gesture', 'sensor', 'recognition', 'input', 'camera', 'microphone'],
    coreDeps: {
      sensor: ['T06.G4.01', 'T09.G4.01'], // events, variables
      recognition: ['T08.G4.01', 'T10.G4.01'], // conditionals, lists
      interaction: ['T06.G4.01'] // events
    },
    crossAppDeps: ['T16'], // UI
    designDeps: ['T05.G4.01'] // HCD for accessibility
  },
  // T24: XO AI Practices (meta-level)
  T24: {
    keywords: ['xo', 'ai', 'assist', 'generate', 'debug', 'plan', 'code'],
    coreDeps: {
      planning: ['T03.G4.01', 'T02.G4.01'], // decomposition, planning
      generation: ['T01.G4.01', 'T11.G4.01'], // algorithms, functions
      debugging: ['T13.G4.01'] // testing
    },
    designDeps: ['T05.G4.01'] // HCD for AI ethics
  }
};

// Analyze dependencies for a skill
function analyzeDependencies(skill) {
  const result = {
    id: skill.id,
    dependencies: [],
    cross_domain_dependencies: [],
    notes: '',
    grade_level_ok: true,
    quality_issues: [],
    gateway_skill: false,
    dependency_count: 0,
    capstone_skill: false
  };

  const topic = skill.topic_id;
  const grade = parseInt(skill.id.match(/\.G(\d+)\./)[1]);
  const title = skill.title.toLowerCase();
  const description = (skill.description || '').toLowerCase();
  const combined = `${title} ${description}`;

  // 1. Within-topic dependencies (same grade or lower)
  const sameTopicSkills = skillsT14T24.filter(s =>
    s.topic_id === topic &&
    parseInt(s.id.match(/\.G(\d+)\./)[1]) < grade
  );

  // Add dependency on immediately previous grade in same topic
  if (grade > 1) {
    const prevGrade = grade - 1;
    const prevSkillId = `${topic}.G${prevGrade}.01`;
    if (skillMap[prevSkillId]) {
      result.dependencies.push(prevSkillId);
    }
  }

  // 2. Cross-domain dependencies (T06-T13 programming core)
  const pattern = dependencyPatterns[topic];
  if (pattern) {
    // Check for keyword matches
    const matchedDeps = new Set();

    Object.entries(pattern.coreDeps).forEach(([category, deps]) => {
      const categoryKeywords = pattern.keywords.concat(category.split(/(?=[A-Z])/));
      const hasKeyword = categoryKeywords.some(kw => combined.includes(kw.toLowerCase()));

      if (hasKeyword) {
        deps.forEach(dep => {
          // Adjust dependency to match or be lower than current grade
          const depGrade = parseInt(dep.match(/\.G(\d+)\./)[1]);
          const depTopic = dep.match(/^(T\d+)\./)[1];

          if (depGrade <= grade) {
            matchedDeps.add(dep);
          } else if (depGrade > grade && grade >= 3) {
            // Use lower grade version of same topic
            const adjustedDep = `${depTopic}.G${grade}.01`;
            matchedDeps.add(adjustedDep);
          }
        });
      }
    });

    // Add core programming dependencies based on grade
    if (grade >= 3) {
      // All application skills need basic events
      matchedDeps.add(`T06.G${Math.min(grade, 8)}.01`);

      // Most need loops and conditionals
      if (combined.includes('loop') || combined.includes('repeat') || combined.includes('animate')) {
        matchedDeps.add(`T07.G${Math.min(grade, 8)}.01`);
      }
      if (combined.includes('if') || combined.includes('condition') || combined.includes('check')) {
        matchedDeps.add(`T08.G${Math.min(grade, 8)}.01`);
      }

      // Variable-related
      if (combined.includes('variable') || combined.includes('score') || combined.includes('data') ||
          combined.includes('track') || combined.includes('store')) {
        matchedDeps.add(`T09.G${Math.min(grade, 8)}.01`);
      }

      // List-related
      if (combined.includes('list') || combined.includes('array') || combined.includes('collection') ||
          combined.includes('multiple') || combined.includes('players')) {
        matchedDeps.add(`T10.G${Math.min(grade, 8)}.01`);
      }

      // Function-related
      if (combined.includes('function') || combined.includes('custom block') || combined.includes('module') ||
          combined.includes('reusable')) {
        matchedDeps.add(`T11.G${Math.min(grade, 8)}.01`);
      }

      // Organization-related
      if (combined.includes('organize') || combined.includes('multi') || combined.includes('scene') ||
          combined.includes('level') || grade >= 6) {
        matchedDeps.add(`T12.G${Math.min(grade, 8)}.01`);
      }

      // Testing-related
      if (combined.includes('test') || combined.includes('debug') || combined.includes('fix') ||
          grade >= 5) {
        matchedDeps.add(`T13.G${Math.min(grade, 8)}.01`);
      }
    }

    result.cross_domain_dependencies = Array.from(matchedDeps).sort();

    // 3. Design dependencies (T01-T05)
    if (pattern.designDeps) {
      pattern.designDeps.forEach(dep => {
        const depGrade = parseInt(dep.match(/\.G(\d+)\./)[1]);
        if (depGrade <= grade) {
          result.cross_domain_dependencies.push(dep);
        }
      });
    }

    // 4. Cross-application dependencies
    if (pattern.crossAppDeps && grade >= 4) {
      pattern.crossAppDeps.forEach(crossTopic => {
        const crossSkillId = `${crossTopic}.G${Math.min(grade - 1, 8)}.01`;
        if (skillMap[crossSkillId]) {
          result.cross_domain_dependencies.push(crossSkillId);
        }
      });
    }
  }

  // Remove duplicates and sort
  result.cross_domain_dependencies = [...new Set(result.cross_domain_dependencies)].sort();
  result.dependency_count = result.dependencies.length + result.cross_domain_dependencies.length;

  // Check for capstone skills (5+ deps from 3+ topics)
  if (result.dependency_count >= 5) {
    const topics = new Set();
    [...result.dependencies, ...result.cross_domain_dependencies].forEach(dep => {
      const depTopic = dep.match(/^(T\d+)\./)?.[1];
      if (depTopic) topics.add(depTopic);
    });
    if (topics.size >= 3) {
      result.capstone_skill = true;
    }
  }

  // Validate grade levels
  [...result.dependencies, ...result.cross_domain_dependencies].forEach(dep => {
    const depGrade = gradeMap[dep];
    if (depGrade && depGrade > grade) {
      result.grade_level_ok = false;
      result.quality_issues.push(`Dependency ${dep} is from grade ${depGrade}, higher than skill grade ${grade}`);
    }
  });

  // Generate notes
  const notesParts = [];
  if (result.capstone_skill) {
    notesParts.push('CAPSTONE: Integrates multiple programming concepts');
  }
  if (pattern) {
    notesParts.push(`${topic} application skill`);
  }
  if (result.cross_domain_dependencies.length > 0) {
    const coreTopics = [...new Set(result.cross_domain_dependencies
      .map(d => d.match(/^(T\d+)\./)?.[1])
      .filter(t => t && t.match(/^T0[6-9]|T1[0-3]$/))
    )];
    if (coreTopics.length > 0) {
      notesParts.push(`Requires core skills: ${coreTopics.join(', ')}`);
    }
  }
  result.notes = notesParts.join('; ');

  return result;
}

// Process all skills
console.log('\nAnalyzing dependencies for 346 application skills...');
const results = [];
let capstoneCount = 0;
let gatewayCount = 0;

skillsT14T24.forEach((skill, index) => {
  if (index % 50 === 0) {
    console.log(`Progress: ${index}/${skillsT14T24.length} skills analyzed`);
  }

  const analysis = analyzeDependencies(skill);
  results.push(analysis);

  if (analysis.capstone_skill) capstoneCount++;
  if (analysis.gateway_skill) gatewayCount++;
});

console.log(`\nAnalysis complete!`);
console.log(`Total skills: ${results.length}`);
console.log(`Capstone skills: ${capstoneCount}`);
console.log(`Gateway skills: ${gatewayCount}`);

// Write output
fs.writeFileSync('dependencies_T14_T24.json', JSON.stringify(results, null, 2));
console.log('\nWrote dependencies_T14_T24.json');

// Generate statistics
const stats = {
  totalSkills: results.length,
  capstoneSkills: capstoneCount,
  gatewaySkills: gatewayCount,
  avgDependencies: (results.reduce((sum, r) => sum + r.dependency_count, 0) / results.length).toFixed(2),
  gradeIssues: results.filter(r => !r.grade_level_ok).length,
  byTopic: {}
};

skillsT14T24.forEach(skill => {
  const topic = skill.topic_id;
  if (!stats.byTopic[topic]) {
    stats.byTopic[topic] = { count: 0, avgDeps: 0 };
  }
  stats.byTopic[topic].count++;
});

Object.keys(stats.byTopic).forEach(topic => {
  const topicResults = results.filter(r => r.id.startsWith(topic));
  stats.byTopic[topic].avgDeps = (topicResults.reduce((sum, r) => sum + r.dependency_count, 0) / topicResults.length).toFixed(2);
  stats.byTopic[topic].capstones = topicResults.filter(r => r.capstone_skill).length;
});

console.log('\nStatistics:');
console.log(JSON.stringify(stats, null, 2));

console.log('\nDone!');
