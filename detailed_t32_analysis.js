const fs = require('fs');
const data = JSON.parse(fs.readFileSync('/media/binyu/USB2/dev/CreatiCodeSkillMap/t32_analysis.json', 'utf-8'));

console.log('=== DETAILED T32 ISSUE ANALYSIS ===\n');

// Group skills by theme
const themes = {
  'Digital Safety & Well-being': [],
  'AI Ethics': [],
  'Accessibility': [],
  'Tech Careers': [],
  'Collaboration': [],
  'Online Citizenship': [],
  'Critical Thinking': [],
  'Privacy & Data': [],
  'Other': []
};

data.allSkills.forEach(s => {
  const text = (s.skill + ' ' + s.description).toLowerCase();

  if (text.includes('safety') || text.includes('well-being') || text.includes('screen time') || text.includes('balance')) {
    themes['Digital Safety & Well-being'].push(s);
  } else if (text.includes('ai') && (text.includes('ethics') || text.includes('bias') || text.includes('fairness'))) {
    themes['AI Ethics'].push(s);
  } else if (text.includes('accessibility') || text.includes('accessible') || text.includes('inclusive')) {
    themes['Accessibility'].push(s);
  } else if (text.includes('career') || text.includes('job') || text.includes('professional')) {
    themes['Tech Careers'].push(s);
  } else if (text.includes('team') || text.includes('collaboration') || text.includes('group')) {
    themes['Collaboration'].push(s);
  } else if (text.includes('online') || text.includes('digital citizen') || text.includes('kindness')) {
    themes['Online Citizenship'].push(s);
  } else if (text.includes('critical') || text.includes('evaluate') || text.includes('analyze') || text.includes('credibility')) {
    themes['Critical Thinking'].push(s);
  } else if (text.includes('privacy') || text.includes('data') || text.includes('consent')) {
    themes['Privacy & Data'].push(s);
  } else {
    themes['Other'].push(s);
  }
});

console.log('THEME DISTRIBUTION:');
Object.entries(themes).forEach(([theme, skills]) => {
  console.log(`${theme}: ${skills.length} skills`);
});
console.log('');

// Identify specific issues by grade
console.log('=== SPECIFIC ISSUES BY GRADE ===\n');

// K-2 Analysis
console.log('KINDERGARTEN (8 skills):');
const kSkills = data.allSkills.filter(s => s.grade === 'K');
kSkills.forEach(s => {
  console.log(`${s.id}: ${s.skill}`);
});

const kIssues = [];
// Check if all are picture-based
kSkills.forEach(s => {
  const desc = s.description.toLowerCase();
  if (!desc.includes('picture') && !desc.includes('card') && !desc.includes('draw') && !desc.includes('role-play')) {
    kIssues.push(`${s.id}: May not be sufficiently visual/concrete`);
  }
});

if (kIssues.length > 0) {
  console.log('\nIssues:');
  kIssues.forEach(i => console.log(`  - ${i}`));
}
console.log('');

console.log('GRADE 1 (8 skills):');
const g1Skills = data.allSkills.filter(s => s.grade === '1');
g1Skills.forEach(s => {
  console.log(`${s.id}: ${s.skill}`);
});
console.log('');

console.log('GRADE 2 (9 skills):');
const g2Skills = data.allSkills.filter(s => s.grade === '2');
g2Skills.forEach(s => {
  console.log(`${s.id}: ${s.skill}`);
});
console.log('');

// Check for redundancy in higher grades
console.log('=== REDUNDANCY ANALYSIS (G6-G8) ===\n');

const highGradeSkills = data.allSkills.filter(s => ['6', '7', '8'].includes(s.grade));

// Check AI ethics skills
const aiEthicsSkills = highGradeSkills.filter(s => {
  const text = (s.skill + ' ' + s.description).toLowerCase();
  return (text.includes('ai') || text.includes('chatbot') || text.includes('image generation'))
    && (text.includes('bias') || text.includes('test') || text.includes('ethics') || text.includes('audit'));
});

console.log(`AI Ethics/Testing skills (${aiEthicsSkills.length}):`);
aiEthicsSkills.forEach(s => {
  console.log(`${s.id} (G${s.grade}): ${s.skill}`);
});
console.log('');

// Career skills
const careerSkills = data.allSkills.filter(s => {
  const text = (s.skill + ' ' + s.description).toLowerCase();
  return text.includes('career') || text.includes('job') || (text.includes('tech') && text.includes('professional'));
});

console.log(`Career-related skills (${careerSkills.length}):`);
careerSkills.forEach(s => {
  console.log(`${s.id} (G${s.grade}): ${s.skill}`);
});
console.log('');

// Check for skills that could be consolidated
console.log('=== CONSOLIDATION OPPORTUNITIES ===\n');

// Ethics lens skills (G6)
const ethicsLensSkills = data.allSkills.filter(s => s.id.includes('G6') && s.skill.toLowerCase().includes('lens'));
console.log(`Ethics lens skills (could be consolidated?):`);
ethicsLensSkills.forEach(s => {
  console.log(`${s.id}: ${s.skill}`);
});
console.log('');

// AI testing skills (spread across G6-G7)
const aiTestingSkills = data.allSkills.filter(s => {
  const text = (s.skill + ' ' + s.description).toLowerCase();
  return text.includes('test') && text.includes('ai');
});
console.log(`AI testing skills (could be consolidated?):`);
aiTestingSkills.forEach(s => {
  console.log(`${s.id} (G${s.grade}): ${s.skill}`);
});
console.log('');

// Workshop/teaching skills
const workshopSkills = data.allSkills.filter(s => {
  const text = s.skill.toLowerCase();
  return text.includes('workshop') || text.includes('teach') || text.includes('lesson');
});
console.log(`Workshop/Teaching skills:`);
workshopSkills.forEach(s => {
  console.log(`${s.id} (G${s.grade}): ${s.skill}`);
});
console.log('');

// Missing topics
console.log('=== MISSING/UNDERREPRESENTED MODERN TOPICS ===\n');

const missingTopics = [
  'Deepfake detection (only 1 skill: T32.G7.17)',
  'AI content attribution (0 skills)',
  'Algorithmic literacy/transparency (0 skills with "algorithmic")',
  'Digital footprint management (only 1 skill: T32.G3.01)',
  'Disinformation vs misinformation (0 skills with "disinformation")',
  'AI-generated content disclosure (minimal coverage)',
  'Data ownership & right to be forgotten (minimal coverage)',
  'Filter bubbles & echo chambers (0 skills)',
  'Social media algorithms & recommendation systems (minimal, only G3.02)',
  'Cryptocurrency/blockchain ethics (0 skills)',
  'IoT privacy concerns (0 skills)',
  'Biometric data ethics (0 skills)',
  'AI creativity vs human creativity (touched in G7 art skills)',
  'Gaming addiction & dark patterns (minimal)',
  'Online radicalization & extremism (0 skills)'
];

console.log('Topics that could be added or expanded:');
missingTopics.forEach(t => console.log(`  - ${t}`));
console.log('');

// Check progression coherence
console.log('=== PROGRESSION GAPS ===\n');

// Digital footprint: K -> G3 is a big jump
console.log('Digital Footprint progression:');
const footprintSkills = data.allSkills.filter(s => {
  const text = (s.skill + ' ' + s.description).toLowerCase();
  return text.includes('footprint') || text.includes('private information') || text.includes('personal information');
});
footprintSkills.forEach(s => console.log(`  G${s.grade}: ${s.id} - ${s.skill}`));
console.log('  GAP: K-2 have basic privacy, but G3.01 jumps to digital footprints with coding. Missing G3 unplugged intro?\n');

// AI ethics: jumps from G4-G5 intro to G6 comprehensive
console.log('AI Ethics progression:');
const aiEthicsProgression = data.allSkills.filter(s => {
  const text = (s.skill + ' ' + s.description).toLowerCase();
  return text.includes('ai') && (text.includes('ethics') || text.includes('bias') || text.includes('fairness'));
});
aiEthicsProgression.forEach(s => console.log(`  G${s.grade}: ${s.id} - ${s.skill}`));
console.log('');

// Collaboration: check if progression is smooth
console.log('Collaboration progression:');
const collabSkills = data.allSkills.filter(s => {
  const text = (s.skill + ' ' + s.description).toLowerCase();
  return text.includes('team') || text.includes('collaboration') || text.includes('group');
});
collabSkills.forEach(s => console.log(`  G${s.grade}: ${s.id} - ${s.skill}`));
console.log('');

// G6-G8 imbalance
console.log('=== GRADE DISTRIBUTION IMBALANCE ===\n');
console.log('Grade distribution shows heavy concentration in G6-G7:');
console.log('  K-2: 25 skills (8+8+9)');
console.log('  3-5: 34 skills (9+12+13)');
console.log('  6-8: 76 skills (27+27+22)');
console.log('  G6 and G7 each have 27 skills - likely too many!');
console.log('  Could some G6-G7 skills be redistributed or consolidated?\n');

// Save detailed report
const report = {
  themes,
  issues: {
    kIssues,
    missingTopics,
    redundantSkills: {
      aiTesting: aiTestingSkills.map(s => s.id),
      careers: careerSkills.map(s => s.id),
      workshops: workshopSkills.map(s => s.id)
    }
  }
};

fs.writeFileSync('/media/binyu/USB2/dev/CreatiCodeSkillMap/t32_detailed_report.json', JSON.stringify(report, null, 2));
console.log('Detailed report saved to t32_detailed_report.json');
