const fs = require('fs');
const data = JSON.parse(fs.readFileSync('/media/binyu/USB2/dev/CreatiCodeSkillMap/t32_analysis.json', 'utf-8'));

console.log('=== SKILL QUALITY ANALYSIS ===\n');

// Check verb usage
const activeVerbs = ['create', 'build', 'design', 'analyze', 'evaluate', 'implement', 'test', 'develop', 'compare', 'apply', 'identify', 'explain'];
const weakVerbs = ['describe', 'list', 'name', 'match', 'sort', 'point', 'circle'];
const vagueVerbs = ['understand', 'know', 'learn', 'explore', 'appreciate'];

console.log('VERB USAGE ANALYSIS:\n');

const skillsByVerb = { active: [], weak: [], vague: [], other: [] };

data.allSkills.forEach(s => {
  const verb = s.skill.split(' ')[0].toLowerCase();

  if (activeVerbs.some(v => verb.startsWith(v))) {
    skillsByVerb.active.push(s);
  } else if (weakVerbs.some(v => verb.startsWith(v))) {
    skillsByVerb.weak.push(s);
  } else if (vagueVerbs.some(v => verb.startsWith(v))) {
    skillsByVerb.vague.push(s);
  } else {
    skillsByVerb.other.push(s);
  }
});

console.log(`Active verbs (${skillsByVerb.active.length} skills): ${activeVerbs.join(', ')}`);
console.log(`Weak verbs (${skillsByVerb.weak.length} skills): ${weakVerbs.join(', ')}`);
console.log(`Vague verbs (${skillsByVerb.vague.length} skills): ${vagueVerbs.join(', ')}`);
console.log(`Other verbs (${skillsByVerb.other.length} skills)\n`);

// Show K-2 weak verb examples
console.log('K-2 skills with weak verbs (may be acceptable for early grades):');
skillsByVerb.weak.filter(s => ['K', '1', '2'].includes(s.grade)).forEach(s => {
  console.log(`  ${s.id}: ${s.skill}`);
});
console.log('');

// Show G3+ weak verb examples (these should potentially be stronger)
console.log('G3+ skills with weak verbs (consider strengthening):');
skillsByVerb.weak.filter(s => !['K', '1', '2'].includes(s.grade)).forEach(s => {
  console.log(`  ${s.id}: ${s.skill}`);
});
console.log('');

// Check for skills that are too similar
console.log('=== SIMILARITY ANALYSIS ===\n');

const similarGroups = [];

// Check AI testing skills for overlap
const aiTestSkills = [
  data.allSkills.find(s => s.id === 'T32.G6.01'),
  data.allSkills.find(s => s.id === 'T32.G6.02'),
  data.allSkills.find(s => s.id === 'T32.G6.03'),
  data.allSkills.find(s => s.id === 'T32.G7.01'),
  data.allSkills.find(s => s.id === 'T32.G7.07')
].filter(Boolean);

console.log('AI Testing Skills (potential overlap):');
aiTestSkills.forEach(s => {
  console.log(`\n${s.id}: ${s.skill}`);
  console.log(`  Description: ${s.description.substring(0, 150)}...`);
});
console.log('');

// Check ethics lens skills
const ethicsLensSkills = [
  data.allSkills.find(s => s.id === 'T32.G6.04'),
  data.allSkills.find(s => s.id === 'T32.G6.05'),
  data.allSkills.find(s => s.id === 'T32.G6.06'),
  data.allSkills.find(s => s.id === 'T32.G6.07')
].filter(Boolean);

console.log('Ethics Lens Skills (G6.04-07 could potentially be 1-2 skills):');
ethicsLensSkills.forEach(s => {
  console.log(`\n${s.id}: ${s.skill}`);
  console.log(`  Description: ${s.description.substring(0, 150)}...`);
});
console.log('');

// Check career identification skills
const careerIdSkills = [
  data.allSkills.find(s => s.id === 'T32.G6.14'),
  data.allSkills.find(s => s.id === 'T32.G6.15'),
  data.allSkills.find(s => s.id === 'T32.G6.16'),
  data.allSkills.find(s => s.id === 'T32.G6.17')
].filter(Boolean);

console.log('Career Cluster Skills (G6.14-17 are repetitive - could be 1 skill):');
careerIdSkills.forEach(s => {
  console.log(`\n${s.id}: ${s.skill}`);
});
console.log('');

// Check AI displacement skills
const displacementSkills = [
  data.allSkills.find(s => s.id === 'T32.G8.17'),
  data.allSkills.find(s => s.id === 'T32.G8.18'),
  data.allSkills.find(s => s.id === 'T32.G8.19')
].filter(Boolean);

console.log('AI Displacement Skills (G8.17-19 could be consolidated):');
displacementSkills.forEach(s => {
  console.log(`\n${s.id}: ${s.skill}`);
  console.log(`  Description: ${s.description.substring(0, 120)}...`);
});
console.log('');

// Identify skills that could be merged
console.log('=== CONSOLIDATION RECOMMENDATIONS ===\n');

const consolidationOpportunities = [
  {
    name: 'Ethics Lens Application (G6)',
    current: ['T32.G6.04', 'T32.G6.05', 'T32.G6.06'],
    proposed: 'T32.G6.04: Apply ethics lenses (beneficence, fairness, autonomy) to evaluate projects',
    rationale: 'Teaching three lenses separately is pedagogically sound, but each could be a sub-skill of one assessment skill',
    savings: '2 skills'
  },
  {
    name: 'Career Cluster Identification (G6)',
    current: ['T32.G6.14', 'T32.G6.15', 'T32.G6.16', 'T32.G6.17'],
    proposed: 'T32.G6.14: Identify and compare computing career clusters (software, hardware, data, AI/ML)',
    rationale: 'These are identical in structure, just different domains. Could be one skill with 4 examples.',
    savings: '3 skills'
  },
  {
    name: 'AI Displacement Analysis (G8)',
    current: ['T32.G8.17', 'T32.G8.18', 'T32.G8.19'],
    proposed: 'T32.G8.17: Analyze AI impacts on jobs (displacement vs augmentation patterns)',
    rationale: 'These form one coherent analysis - identifying both displacement and augmentation should happen together',
    savings: '2 skills'
  },
  {
    name: 'Workshop Design & Delivery (G7-G8)',
    current: ['T32.G7.24', 'T32.G7.25', 'T32.G8.04.01', 'T32.G8.04.02', 'T32.G8.04.03'],
    proposed: 'G7: Plan and deliver lesson to younger coders; G8: Design and deliver interactive workshop on responsible tech',
    rationale: 'G7.24-25 already form a plan-deliver pair. G8.04.01-03 duplicate this pattern with more complexity.',
    savings: '2-3 skills'
  },
  {
    name: 'Build Testing Tools (G6-G7)',
    current: ['T32.G6.01', 'T32.G6.02', 'T32.G6.03', 'T32.G7.01', 'T32.G7.07'],
    proposed: 'Keep G6.03 (dashboard) and G7.01 (systematic framework), but G6.01-02 could be sub-components',
    rationale: 'Too granular - testing image AI and chat AI separately, then combining, is excessive',
    savings: '1-2 skills'
  },
  {
    name: 'Team Meeting Skills (G6-G7)',
    current: ['T32.G5.12', 'T32.G6.21', 'T32.G6.23', 'T32.G8.22', 'T32.G8.23'],
    proposed: 'G5: Lead team check-ins; G6: Conduct agile ceremonies (stand-ups, sprint reviews); G8: Facilitate retrospectives',
    rationale: 'Teaching specific agile ceremonies is great, but could be consolidated into agile collaboration skills',
    savings: '1-2 skills'
  }
];

consolidationOpportunities.forEach((opp, i) => {
  console.log(`${i + 1}. ${opp.name}`);
  console.log(`   Current (${opp.current.length} skills): ${opp.current.join(', ')}`);
  console.log(`   Proposed: ${opp.proposed}`);
  console.log(`   Rationale: ${opp.rationale}`);
  console.log(`   Potential savings: ${opp.savings}`);
  console.log('');
});

const totalSavings = consolidationOpportunities.reduce((sum, opp) => {
  const savings = parseInt(opp.savings.split('-')[0]);
  return sum + savings;
}, 0);

console.log(`Total potential consolidation: ~${totalSavings}-${totalSavings + 5} skills\n`);

// Check skill description quality
console.log('=== DESCRIPTION QUALITY ISSUES ===\n');

const descriptionIssues = [];

data.allSkills.forEach(s => {
  const desc = s.description;

  // Check for overly long descriptions
  if (desc.length > 600) {
    descriptionIssues.push({
      id: s.id,
      issue: 'Very long description (>600 chars)',
      length: desc.length
    });
  }

  // Check for descriptions that are just lists without context
  if ((desc.match(/\(/g) || []).length > 5) {
    descriptionIssues.push({
      id: s.id,
      issue: 'Many parenthetical examples - may be too complex'
    });
  }
});

console.log(`Found ${descriptionIssues.length} description quality issues:\n`);
descriptionIssues.forEach(issue => {
  console.log(`${issue.id}: ${issue.issue}${issue.length ? ` (${issue.length} chars)` : ''}`);
});
console.log('');

// Save analysis
const output = {
  verbAnalysis: {
    active: skillsByVerb.active.length,
    weak: skillsByVerb.weak.length,
    vague: skillsByVerb.vague.length,
    other: skillsByVerb.other.length
  },
  consolidationOpportunities,
  totalPotentialSavings: `${totalSavings}-${totalSavings + 5} skills`,
  descriptionIssues
};

fs.writeFileSync('/media/binyu/USB2/dev/CreatiCodeSkillMap/t32_quality_analysis.json', JSON.stringify(output, null, 2));
console.log('Quality analysis saved to t32_quality_analysis.json');
