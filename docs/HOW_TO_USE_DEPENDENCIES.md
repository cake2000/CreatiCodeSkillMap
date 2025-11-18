# How to Use the T01-T05 Dependency Data

This guide explains how to use the dependency analysis files for Topics T01-T05.

## Files Overview

### 1. dependencies_T01_T05.json (Primary Data)
**Size**: 45 KB
**Format**: JSON array with 156 skill objects
**Use for**: Platform integration, programmatic access

**Structure**:
```json
{
  "id": "T01.G3.04",
  "title": "Describe an algorithm in words after running code",
  "topic": "T01",
  "grade": 3,
  "dependencies": ["T01.G2.01", "T02.G3.01"],
  "notes": "Applies algorithms in block coding context (cross-topic with T02)",
  "grade_level_ok": true,
  "quality_issues": []
}
```

### 2. dependencies_T01_T05_summary.json (Statistics)
**Size**: 449 bytes
**Format**: JSON object with aggregate data
**Use for**: Quick stats, dashboard displays

### 3. DEPENDENCIES_T01_T05_REPORT.md (Full Analysis)
**Size**: 11 KB
**Format**: Markdown report
**Use for**: Understanding methodology, detailed findings

### 4. DEPENDENCIES_T01_T05_SUMMARY.md (Quick Reference)
**Size**: 6 KB
**Format**: Markdown summary
**Use for**: Quick lookups, executive overview

### 5. DEPENDENCY_MAP_T01_T05.md (Visual Map)
**Size**: 24 KB
**Format**: Markdown with hierarchical view
**Use for**: Human-readable dependency chains

---

## Common Use Cases

### Use Case 1: Check Prerequisites Before Teaching

**Question**: What do students need to know before learning T01.G4.02?

**Solution**:
```python
import json

with open('dependencies_T01_T05.json') as f:
    skills = json.load(f)

# Find the skill
skill = next(s for s in skills if s['id'] == 'T01.G4.02')

print(f"Skill: {skill['title']}")
print(f"Prerequisites: {skill['dependencies']}")

# Output:
# Skill: Optimize an algorithm (fewer steps or faster)
# Prerequisites: ['T01.G4.01']
```

### Use Case 2: Build Learning Paths

**Question**: What's the complete path from T01.G1.01 to T01.G4.02?

**Solution**:
```python
def get_dependency_chain(skill_id, skills_dict, visited=None):
    if visited is None:
        visited = set()

    if skill_id in visited:
        return []

    visited.add(skill_id)
    skill = skills_dict.get(skill_id)

    if not skill:
        return []

    chain = [skill_id]
    for dep in skill['dependencies']:
        chain.extend(get_dependency_chain(dep, skills_dict, visited))

    return chain

# Load skills
with open('dependencies_T01_T05.json') as f:
    skills = json.load(f)

skills_dict = {s['id']: s for s in skills}

# Get chain
chain = get_dependency_chain('T01.G4.02', skills_dict)
print("Learning path (reverse order):")
for skill_id in reversed(list(dict.fromkeys(chain))):
    print(f"  → {skill_id}: {skills_dict[skill_id]['title']}")

# Output:
# Learning path (reverse order):
#   → T01.G1.01: Write or draw steps for a simple task
#   → T01.G1.02: Trace and predict the outcome of a simple algorithm
#   → T01.G2.01: Write an algorithm with "if/then" choice
#   → T01.G2.02: Write an algorithm with a repeat statement
#   → T01.G3.01: Create a simple algorithm in code (sequence and events)
#   → T01.G3.03: Use a loop in code for repetition
#   → T01.G4.01: Create an algorithm to solve a simple problem
#   → T01.G4.02: Optimize an algorithm (fewer steps or faster)
```

### Use Case 3: Identify Cross-Topic Skills

**Question**: Which skills connect T01 (Algorithms) to other topics?

**Solution**:
```python
import json

with open('dependencies_T01_T05.json') as f:
    skills = json.load(f)

# Find T01 skills with cross-topic dependencies
cross_topic = []
for skill in skills:
    if skill['topic'] == 'T01':
        cross_deps = [d for d in skill['dependencies'] if not d.startswith('T01')]
        if cross_deps:
            cross_topic.append({
                'id': skill['id'],
                'title': skill['title'],
                'cross_deps': cross_deps
            })

print(f"T01 skills with cross-topic dependencies: {len(cross_topic)}")
for skill in cross_topic:
    print(f"\n{skill['id']}: {skill['title']}")
    print(f"  Depends on: {', '.join(skill['cross_deps'])}")

# Output shows 6 T01 skills that integrate with other topics
```

### Use Case 4: Validate Student Readiness

**Question**: Has a student completed all prerequisites for T05.G6.02?

**Solution**:
```python
import json

def check_prerequisites(skill_id, completed_skills, skills_dict):
    skill = skills_dict.get(skill_id)
    if not skill:
        return False, ["Skill not found"]

    missing = []
    for dep in skill['dependencies']:
        if dep not in completed_skills:
            missing.append(dep)

    return len(missing) == 0, missing

# Load skills
with open('dependencies_T01_T05.json') as f:
    skills = json.load(f)

skills_dict = {s['id']: s for s in skills}

# Example: Student's completed skills
completed = ['T05.G1.01', 'T05.G2.01', 'T05.G3.01', 'T05.G4.01',
             'T05.G5.01', 'T05.G5.02', 'T05.G6.01']

# Check readiness for T05.G6.02
ready, missing = check_prerequisites('T05.G6.02', completed, skills_dict)

if ready:
    print(f"✓ Student is ready for {skills_dict['T05.G6.02']['title']}")
else:
    print(f"✗ Missing prerequisites:")
    for dep_id in missing:
        print(f"  - {dep_id}: {skills_dict[dep_id]['title']}")

# Output:
# ✓ Student is ready for Applies UX design to interfaces
```

### Use Case 5: Generate Recommended Next Skills

**Question**: What skills can a student attempt next?

**Solution**:
```python
import json

def get_available_skills(completed_skills, all_skills):
    available = []

    for skill in all_skills:
        # Skip if already completed
        if skill['id'] in completed_skills:
            continue

        # Check if all prerequisites are met
        prereqs_met = all(dep in completed_skills for dep in skill['dependencies'])

        if prereqs_met:
            available.append(skill)

    return available

# Load skills
with open('dependencies_T01_T05.json') as f:
    skills = json.load(f)

# Example: Student has completed all Grade 1 and some Grade 2
completed = ['T01.G1.01', 'T01.G1.02', 'T01.G1.03', 'T01.G1.04', 'T01.G2.01']

# Find what's available next
available = get_available_skills(completed, skills)

print("Recommended next skills:")
for skill in available[:5]:  # Show top 5
    print(f"  {skill['id']}: {skill['title']}")
    if skill['dependencies']:
        print(f"    (builds on: {', '.join(skill['dependencies'])})")

# Output shows skills the student is ready to learn
```

---

## Integration Examples

### Example 1: React Learning Path Component

```javascript
import dependenciesData from './dependencies_T01_T05.json';

function LearningPath({ targetSkillId }) {
  const skillsMap = new Map(dependenciesData.map(s => [s.id, s]));

  function buildPath(skillId, visited = new Set()) {
    if (visited.has(skillId)) return [];
    visited.add(skillId);

    const skill = skillsMap.get(skillId);
    if (!skill) return [];

    const path = [skill];
    for (const dep of skill.dependencies) {
      path.push(...buildPath(dep, visited));
    }
    return path;
  }

  const path = buildPath(targetSkillId);
  const uniquePath = Array.from(new Set(path.map(s => s.id)))
    .map(id => skillsMap.get(id))
    .sort((a, b) => a.grade - b.grade);

  return (
    <div>
      <h3>Learning Path to {skillsMap.get(targetSkillId)?.title}</h3>
      <ol>
        {uniquePath.map(skill => (
          <li key={skill.id}>
            <strong>{skill.id}</strong>: {skill.title}
            <span className="grade">Grade {skill.grade}</span>
          </li>
        ))}
      </ol>
    </div>
  );
}
```

### Example 2: Python Skill Graph Analysis

```python
import json
import networkx as nx
import matplotlib.pyplot as plt

# Load dependencies
with open('dependencies_T01_T05.json') as f:
    skills = json.load(f)

# Build graph
G = nx.DiGraph()

for skill in skills:
    G.add_node(skill['id'],
               title=skill['title'],
               topic=skill['topic'],
               grade=skill['grade'])

    for dep in skill['dependencies']:
        G.add_edge(dep, skill['id'])

# Analyze
print(f"Total skills: {G.number_of_nodes()}")
print(f"Dependencies: {G.number_of_edges()}")
print(f"Average out-degree: {sum(dict(G.out_degree()).values()) / G.number_of_nodes():.2f}")

# Find foundational skills (no incoming edges)
foundational = [node for node in G.nodes() if G.in_degree(node) == 0]
print(f"\nFoundational skills: {len(foundational)}")
for skill_id in foundational:
    print(f"  {skill_id}: {G.nodes[skill_id]['title']}")

# Find terminal skills (no outgoing edges)
terminal = [node for node in G.nodes() if G.out_degree(node) == 0]
print(f"\nTerminal (capstone) skills: {len(terminal)}")

# Visualize (for smaller subsets)
topic_subgraph = [n for n in G.nodes() if G.nodes[n]['topic'] == 'T01']
H = G.subgraph(topic_subgraph)
pos = nx.spring_layout(H)
nx.draw(H, pos, with_labels=True, node_size=500, font_size=8)
plt.savefig('t01_dependency_graph.png')
```

---

## Tips for Effective Use

1. **Start with Foundational Skills**: Always begin learning paths with skills that have no dependencies
2. **Respect Grade Levels**: While dependencies show prerequisites, grade levels indicate cognitive appropriateness
3. **Consider Cross-Topic Links**: When planning curriculum, note when skills from different topics connect
4. **Use for Assessment**: Check prerequisites before assessing students on advanced skills
5. **Support Remediation**: Use dependency chains to identify where students need additional support

---

## API Design Suggestions

If implementing a platform API:

```javascript
// Get skill details with prerequisites
GET /api/skills/:skillId
Response: {
  id, title, description, topic, grade,
  prerequisites: [{id, title, topic, grade}, ...],
  enables: [{id, title, topic, grade}, ...]  // Skills that depend on this one
}

// Get recommended skills for a student
POST /api/skills/recommendations
Body: { completedSkillIds: [...] }
Response: [
  {id, title, grade, reason: "All prerequisites met"},
  ...
]

// Validate readiness
POST /api/skills/:skillId/check-readiness
Body: { completedSkillIds: [...] }
Response: {
  ready: true/false,
  missing: [{id, title}, ...],
  completed: [{id, title}, ...]
}

// Get learning path
GET /api/skills/:skillId/path
Response: {
  target: {id, title, grade},
  path: [{id, title, grade, completed: true/false}, ...],
  estimatedSteps: 8
}
```

---

## Questions?

For more details on methodology and findings:
- See **DEPENDENCIES_T01_T05_REPORT.md** for comprehensive analysis
- See **DEPENDENCIES_T01_T05_SUMMARY.md** for quick reference
- See **DEPENDENCY_MAP_T01_T05.md** for visual dependency chains

The dependency framework is designed to be flexible - use it as a guide for sequencing while allowing for different instructional approaches and student needs.
