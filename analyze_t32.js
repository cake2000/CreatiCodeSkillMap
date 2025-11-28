const fs = require('fs');

// Read the allskills.md file
const content = fs.readFileSync('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv5/allskills.md', 'utf-8');

// Parse T32 skills
const skillRegex = /ID: (T32\.[^\n]+)\nTopic: ([^\n]+)\nSkill: ([^\n]+)\nDescription: ([^\n]+?)(?:\n\nDependencies:\n([\s\S]*?))?\n\n\n/g;

const skills = [];
let match;

while ((match = skillRegex.exec(content)) !== null) {
  const [, id, topic, skill, description, depsRaw] = match;

  const dependencies = [];
  if (depsRaw) {
    const depMatches = depsRaw.matchAll(/\* ([T\d\.GK]+): ([^\n]+)/g);
    for (const depMatch of depMatches) {
      dependencies.push({
        id: depMatch[1],
        description: depMatch[2]
      });
    }
  }

  skills.push({
    id,
    topic,
    skill,
    description,
    dependencies,
    grade: id.match(/\.G(\d|K)\./)?.[1] || id.match(/\.G(K)/)?.[1]
  });
}

console.log(`Total T32 skills found: ${skills.length}\n`);

// Count by grade
const gradeCount = {};
skills.forEach(s => {
  const grade = s.grade;
  gradeCount[grade] = (gradeCount[grade] || 0) + 1;
});

console.log('Skills by grade:');
Object.keys(gradeCount).sort().forEach(grade => {
  console.log(`  G${grade}: ${gradeCount[grade]} skills`);
});
console.log('');

// 1. Check for vague verbs
const vagueVerbs = ['understand', 'know', 'learn', 'explore', 'appreciate', 'become familiar'];
const vagueSkills = skills.filter(s => {
  const lower = s.skill.toLowerCase();
  return vagueVerbs.some(v => lower.startsWith(v) || lower.includes(' ' + v + ' '));
});

console.log('=== 1. VAGUE VERBS ===');
console.log(`Found ${vagueSkills.length} skills with vague verbs:\n`);
vagueSkills.forEach(s => {
  console.log(`${s.id}: ${s.skill}`);
});
console.log('');

// 2. Check X-2 rule violations
console.log('=== 2. X-2 RULE VIOLATIONS ===');
const gradeOrder = ['K', '1', '2', '3', '4', '5', '6', '7', '8'];
const violations = [];

skills.forEach(skill => {
  const skillGradeIndex = gradeOrder.indexOf(skill.grade);

  skill.dependencies.forEach(dep => {
    const depGrade = dep.id.match(/\.G(\d|K)\./)?.[1];
    if (!depGrade) return;

    const depGradeIndex = gradeOrder.indexOf(depGrade);

    if (depGradeIndex !== -1 && skillGradeIndex !== -1) {
      const diff = skillGradeIndex - depGradeIndex;
      if (diff > 2) {
        violations.push({
          skill: skill.id,
          skillGrade: skill.grade,
          dep: dep.id,
          depGrade: depGrade,
          diff: diff
        });
      }
    }
  });
});

console.log(`Found ${violations.length} X-2 rule violations:\n`);
violations.forEach(v => {
  console.log(`${v.skill} (G${v.skillGrade}) depends on ${v.dep} (G${v.depGrade}) - gap of ${v.diff} grades`);
});
console.log('');

// 3. Check K-2 for non-visual activities
console.log('=== 3. K-2 VISUAL/UNPLUGGED CHECK ===');
const k2Skills = skills.filter(s => ['K', '1', '2'].includes(s.grade));
const nonVisualKeywords = ['code', 'coding', 'blocks', 'script', 'program', 'algorithm'];
const visualKeywords = ['picture', 'card', 'sort', 'match', 'point', 'draw', 'role-play', 'scenario'];

const k2Issues = k2Skills.filter(s => {
  const desc = s.description.toLowerCase();
  const skill = s.skill.toLowerCase();
  const hasNonVisual = nonVisualKeywords.some(kw => desc.includes(kw) || skill.includes(kw));
  const hasVisual = visualKeywords.some(kw => desc.includes(kw) || skill.includes(kw));
  return hasNonVisual && !hasVisual;
});

console.log(`Found ${k2Issues.length} K-2 skills that may not be sufficiently visual/unplugged:\n`);
k2Issues.forEach(s => {
  console.log(`${s.id}: ${s.skill}`);
  console.log(`  Description: ${s.description.substring(0, 100)}...`);
});
console.log('');

// 4. Find duplicate/overlapping skills
console.log('=== 4. POTENTIAL DUPLICATES/OVERLAPS ===');
const skillsByTheme = {};
skills.forEach(s => {
  const words = s.skill.toLowerCase().split(' ');
  const key = words.slice(0, 3).join(' ');
  if (!skillsByTheme[key]) skillsByTheme[key] = [];
  skillsByTheme[key].push(s);
});

const duplicates = Object.entries(skillsByTheme).filter(([key, skills]) => skills.length > 1);
console.log(`Found ${duplicates.length} potential duplicate themes:\n`);
duplicates.slice(0, 10).forEach(([key, skills]) => {
  console.log(`Theme: "${key}"`);
  skills.forEach(s => console.log(`  ${s.id} (G${s.grade}): ${s.skill}`));
  console.log('');
});

// 5. Skills that are too broad
console.log('=== 5. OVERLY BROAD SKILLS ===');
const broadKeywords = ['various', 'multiple', 'comprehensive', 'general', 'overall', 'different'];
const broadSkills = skills.filter(s => {
  const text = (s.skill + ' ' + s.description).toLowerCase();
  return broadKeywords.some(kw => text.includes(kw));
});

console.log(`Found ${broadSkills.length} potentially broad skills:\n`);
broadSkills.slice(0, 15).forEach(s => {
  console.log(`${s.id}: ${s.skill}`);
});
console.log('');

// 6. Missing modern topics
console.log('=== 6. COVERAGE OF MODERN TOPICS ===');
const modernTopics = {
  'deepfake': 0,
  'synthetic media': 0,
  'algorithmic': 0,
  'digital footprint': 0,
  'AI bias': 0,
  'AI ethics': 0,
  'misinformation': 0,
  'disinformation': 0,
  'content attribution': 0,
  'AI-generated': 0
};

skills.forEach(s => {
  const text = (s.skill + ' ' + s.description).toLowerCase();
  Object.keys(modernTopics).forEach(topic => {
    if (text.includes(topic)) modernTopics[topic]++;
  });
});

console.log('Modern topic coverage:');
Object.entries(modernTopics).forEach(([topic, count]) => {
  console.log(`  ${topic}: ${count} skills`);
});
console.log('');

// 7. Analyze progression gaps
console.log('=== 7. PROGRESSION ANALYSIS ===');
const themesByGrade = {};
skills.forEach(s => {
  if (!themesByGrade[s.grade]) themesByGrade[s.grade] = [];

  // Extract main theme from skill
  const theme = s.skill.split(/(?:and|using|with|for|to|in|by)/)[0].trim().toLowerCase();
  themesByGrade[s.grade].push(theme);
});

console.log('Themes by grade (first 5 per grade):');
gradeOrder.forEach(grade => {
  if (themesByGrade[grade]) {
    console.log(`G${grade}: ${themesByGrade[grade].slice(0, 5).join(', ')}`);
  }
});
console.log('');

// 8. CreatiCode AI/Widget integration
console.log('=== 8. CREATICODE FEATURE INTEGRATION ===');
const ccFeatures = {
  'widget': 0,
  'ChatGPT': 0,
  'AI ': 0,
  'DALL-E': 0,
  'image generation': 0,
  'perception': 0,
  'hand tracking': 0,
  'body tracking': 0,
  'voice': 0,
  'text-to-speech': 0
};

skills.forEach(s => {
  const text = s.skill + ' ' + s.description;
  Object.keys(ccFeatures).forEach(feature => {
    if (text.includes(feature)) ccFeatures[feature]++;
  });
});

console.log('CreatiCode feature integration:');
Object.entries(ccFeatures).forEach(([feature, count]) => {
  console.log(`  ${feature}: ${count} skills`);
});
console.log('');

// 9. Save detailed output
const output = {
  totalSkills: skills.length,
  gradeCount,
  vagueSkills: vagueSkills.map(s => ({ id: s.id, skill: s.skill })),
  x2Violations: violations,
  k2Issues: k2Issues.map(s => ({ id: s.id, skill: s.skill, description: s.description })),
  modernTopicCoverage: modernTopics,
  ccFeatureIntegration: ccFeatures,
  allSkills: skills
};

fs.writeFileSync('/media/binyu/USB2/dev/CreatiCodeSkillMap/t32_analysis.json', JSON.stringify(output, null, 2));
console.log('Detailed analysis saved to t32_analysis.json');
