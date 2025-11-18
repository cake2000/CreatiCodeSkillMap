# Implementation Guide: Using the CreatiCode Skill Map

**For platform developers, curriculum designers, and technical implementers**

---

## Overview

This guide explains how to use the skill map data in practice. Whether you're building an LMS, creating a curriculum, designing an assessment system, or analyzing learning outcomes, this guide has you covered.

---

## Part 1: Understanding the Data Structure

### The Skill Object

Each skill in `skills_enriched.json` has this structure:

```json
{
  "id": "T07.G3.01",
  "title": "Use a repeat loop to move a character or object repeatedly",
  "short_name": "Use a loop for repetition",
  "topic_id": "T07",
  "topic_name": "Loops & Repetition",
  "grade": 3,
  "description": "Students use a repeat/for loop to make a character or object repeat an action (e.g., 'repeat 5 times, move forward'). They understand that loops reduce code duplication and can be parameterized.",
  "csta_code": "",
  "domain": null,
  "domain_id": "Unknown",
  "domain_name": "Unknown"
}
```

**Key fields:**
- `id`: Unique identifier (T = Topic, G = Grade, 01 = sequence)
- `title`: Complete skill name
- `short_name`: 5-10 word version for UI display
- `topic_id`: Which of 36 topics this belongs to
- `grade`: Specific grade (1-8)
- `description`: What students should be able to do
- `domain_id` & `domain_name`: Broader category (Algorithms, Programming, Data, Systems, Society)

### Understanding Skill IDs

Format: `T[##].G[#].[##]`

Example: `T07.G3.01`
- `T07` = Topic 7 (Loops & Repetition)
- `G3` = Grade 3
- `.01` = First skill in this topic for this grade

All skills for a topic appear in every grade (K-8), but with increasing complexity.

### The Dependency Files

Five files map all prerequisite relationships:
- `dependencies_T01_T05.json` (Algorithms)
- `dependencies_T06_T13.json` (Programming foundations)
- `dependencies_T14_T24.json` (Programming applications)
- `dependencies_T25_T29.json` (Data & Analysis)
- `dependencies_T30_T36.json` (Systems & Society)

Each file is a JSON array of skill objects with a `dependencies` field:

```json
[
  {
    "id": "T07.G3.01",
    "title": "Use a repeat loop...",
    "topic": "T07",
    "grade": 3,
    "dependencies": [
      "T06.G2.03",
      "T01.G2.01"
    ],
    "notes": "...",
    "grade_level_ok": true,
    "quality_issues": []
  }
]
```

The `dependencies` array lists all skills that must be mastered first.

### The Domain Mapping

`domain_mapping.json` maps topics to domains:

```json
{
  "T07": {
    "domain_id": "D2",
    "domain_name": "Programming"
  }
}
```

Use this to organize topics into broader categories.

---

## Part 2: Building a Skill Browser

### Scenario: You're building a web app where teachers select skills to teach.

### Step 1: Load the Data

```python
import json

with open('skills_enriched.json') as f:
    skills = json.load(f)

with open('domain_mapping.json') as f:
    domains = json.load(f)

# skills is a list of 1,155 skill objects
# domains is a dict mapping topic_id -> {domain_id, domain_name}
```

### Step 2: Index by Topic and Grade

```python
from collections import defaultdict

by_topic_grade = defaultdict(list)
for skill in skills:
    key = (skill['topic_id'], skill['grade'])
    by_topic_grade[key].append(skill)

# Now: by_topic_grade[('T07', 3)] gives all Grade 3 Loops skills
```

### Step 3: Create Filter UI

```
┌─────────────────────────────────────┐
│ Filter Skills                        │
├─────────────────────────────────────┤
│ Domain: [All ▼]                     │
│ Topic:  [All ▼]                     │
│ Grade:  [All ▼]                     │
│                         [Search]    │
├─────────────────────────────────────┤
│ Results (147 skills):               │
│                                     │
│ ☐ T07.G3.01 - Use a repeat loop... │
│ ☐ T07.G3.02 - Create a loop with...│
│ ☐ T07.G4.01 - Loop with a condition│
│    [View Details] [Teach This]      │
│                                     │
└─────────────────────────────────────┘
```

### Step 4: Show Skill Details

```
Title: Use a repeat loop to move a character repeatedly
ID: T07.G3.01
Grade: 3
Topic: Loops & Repetition
Domain: Programming

Description:
Students use a repeat/for loop to make a character or object
repeat an action (e.g., 'repeat 5 times, move forward'). They
understand that loops reduce code duplication...

Prerequisites: (click to load)
  - T06.G2.03: Create a simple sequence with events
  - T01.G2.01: Write an algorithm with "if/then" choice

Dependent Skills: (will be unlocked after this)
  - T10.G3.01: Use lists to store multiple values
  - T14.G3.02: Create a game with repeated actions

Status: [Not Started] [In Progress] [Mastered]
```

---

## Part 3: Implementing Prerequisites

### Scenario: Assign a skill to a student; block it if prerequisites aren't met.

### Step 1: Load Dependencies

```python
dep_data = {}
for filename in ['dependencies_T01_T05.json', 'dependencies_T06_T13.json', ...]:
    with open(filename) as f:
        skills_with_deps = json.load(f)
        for skill in skills_with_deps:
            dep_data[skill['id']] = skill['dependencies']

# Now: dep_data['T07.G3.01'] = ['T06.G2.03', 'T01.G2.01']
```

### Step 2: Check Prerequisites Before Assignment

```python
def can_attempt_skill(student_id, skill_id, mastered_skills):
    """
    Check if a student can attempt a skill.

    Args:
        student_id: Student identifier
        skill_id: Skill to check (e.g., 'T07.G3.01')
        mastered_skills: Set of skills student has already mastered

    Returns:
        (can_attempt: bool, missing_prerequisites: list)
    """

    if skill_id not in dep_data:
        return True, []  # No dependencies recorded

    prerequisites = dep_data[skill_id]
    missing = [dep for dep in prerequisites if dep not in mastered_skills]

    return len(missing) == 0, missing

# Usage:
student_mastery = {'T06.G2.03', 'T01.G2.01', 'T06.G1.01'}
can_teach, missing = can_attempt_skill('student123', 'T07.G3.01', student_mastery)

if can_teach:
    print("Student is ready! Assign the skill.")
else:
    print(f"Prerequisites missing: {missing}")
    print("Recommend these skills first:")
    for prereq in missing:
        print(f"  - {prereq}: {skill_dict[prereq]['title']}")
```

### Step 3: Block/Warn in UI

```
Attempting skill: T07.G3.01 - Use a repeat loop

⚠️ WARNING: Student is missing 1 prerequisite

Missing:
  [!] T06.G2.03: Create a simple sequence with events

Recommendation: Have student complete this skill first.

[Teach Prerequisite] [Assign Anyway (Admin Override)]
```

---

## Part 4: Sequencing and Pathways

### Scenario: Create a Grade 3 curriculum. Use the skill map to suggest sequencing.

### Step 1: Identify Grade-Level Skills

```python
def get_skills_for_grade(grade_num, topic_id=None):
    """Get all skills for a grade, optionally filtered by topic."""
    results = []
    for skill in skills:
        if skill['grade'] != grade_num:
            continue
        if topic_id and skill['topic_id'] != topic_id:
            continue
        results.append(skill)
    return results

grade_3_skills = get_skills_for_grade(3)
print(f"Grade 3 has {len(grade_3_skills)} total skills")

grade_3_loops = get_skills_for_grade(3, 'T07')
print(f"Grade 3 Loops has {len(grade_3_loops)} skills")
```

### Step 2: Topological Sort (Teach Prerequisites First)

```python
from collections import defaultdict, deque

def topological_sort_skills(topic_id, grade):
    """Return skills in teaching order (prerequisites first)."""

    # Get all skills for this grade/topic combo
    topic_skills = get_skills_for_grade(grade, topic_id)
    skill_ids = {s['id'] for s in topic_skills}

    # Build dependency graph
    in_degree = {sid: 0 for sid in skill_ids}
    graph = defaultdict(list)

    for skill_id in skill_ids:
        deps = dep_data.get(skill_id, [])
        # Count dependencies that are within this topic/grade
        for dep in deps:
            if dep in skill_ids:
                graph[dep].append(skill_id)
                in_degree[skill_id] += 1

    # Topological sort (Kahn's algorithm)
    queue = deque([s for s in skill_ids if in_degree[s] == 0])
    sorted_skills = []

    while queue:
        current = queue.popleft()
        sorted_skills.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_skills

# Usage:
sequence = topological_sort_skills('T07', 3)
for i, skill_id in enumerate(sequence, 1):
    skill = skill_dict[skill_id]
    print(f"{i}. {skill_id} - {skill['title']}")
```

### Step 3: Create a Learning Path

```
Grade 3 Loops & Repetition - Suggested Teaching Order

Week 1-2:
  □ T06.G2.03 - Create a simple sequence with events [PREREQUISITE]
  □ T07.G2.01 - Use a simple repeat/loop for a basic action

Week 3-4:
  □ T07.G3.01 - Use a repeat loop to move repeatedly
  □ T07.G3.02 - Create a loop with a condition (repeat until)

Week 5-6:
  □ T07.G3.03 - Trace nested loops to understand timing
  □ T07.G3.04 - Use loops with variables for animation

Week 7-8:
  □ INTEGRATED PROJECT: Create an animated scene with loops

Each skill: 1-2 lessons (15-30 min each) + practice
Practice: Do 2-3 mini-projects per skill
Project: 1 major project integrating 5-6 skills
```

---

## Part 5: Creating Auto-Grading Specs

### Scenario: Create an auto-grader that checks if a student has mastered T07.G3.01

### Step 1: Define Mastery Criteria

For each skill, create an assessment spec:

```json
{
  "skill_id": "T07.G3.01",
  "skill_title": "Use a repeat loop to move a character repeatedly",
  "assessment_type": "auto_grade",
  "success_criteria": [
    {
      "criterion": "Code contains at least one loop structure",
      "check": "regex: (repeat|for|while)\\s*\\(",
      "weight": 0.25
    },
    {
      "criterion": "Loop executes 3+ times",
      "check": "static_analysis: loop_iterations >= 3",
      "weight": 0.25
    },
    {
      "criterion": "Movement happens inside the loop",
      "check": "dynamic: runtime_moves > 0 AND moves_occur_in_loop",
      "weight": 0.25
    },
    {
      "criterion": "No logic errors; program completes",
      "check": "dynamic: runtime_errors == 0 AND completion == true",
      "weight": 0.25
    }
  ],
  "min_score": 0.75,
  "common_mistakes": [
    "Using repeat but without actual movement inside",
    "Loop only runs once due to logic error",
    "Movement happens outside the loop instead of inside"
  ]
}
```

### Step 2: Implement Auto-Grader

```python
class SkillGrader:
    def __init__(self, skill_id, spec):
        self.skill_id = skill_id
        self.spec = spec

    def grade(self, student_code, runtime_data):
        """
        Grade a student's submission.

        Args:
            student_code: String of student's code
            runtime_data: Dict with execution info (moves, errors, etc.)

        Returns:
            {'score': 0.0-1.0, 'feedback': str, 'mastered': bool}
        """

        results = {}
        total_weight = 0
        weighted_score = 0

        for criterion in self.spec['success_criteria']:
            passed = self._check_criterion(criterion, student_code, runtime_data)
            weight = criterion['weight']
            results[criterion['criterion']] = {'passed': passed, 'weight': weight}

            if passed:
                weighted_score += weight
            total_weight += weight

        score = weighted_score / total_weight if total_weight > 0 else 0
        mastered = score >= self.spec['min_score']

        feedback = self._generate_feedback(results, mastered)

        return {
            'score': score,
            'feedback': feedback,
            'mastered': mastered,
            'details': results
        }

    def _check_criterion(self, criterion, code, runtime_data):
        """Check a single criterion."""
        check_type = criterion['check'].split(':')[0]
        check_value = criterion['check'].split(':', 1)[1].strip()

        if check_type == 'regex':
            import re
            return bool(re.search(check_value, code))
        elif check_type == 'static_analysis':
            return self._static_check(check_value, code)
        elif check_type == 'dynamic':
            return self._dynamic_check(check_value, runtime_data)
        return False

    def _generate_feedback(self, results, mastered):
        """Create human-readable feedback."""
        if mastered:
            return f"Excellent! You've mastered {self.spec['skill_title']}"

        passed = [c for c, r in results.items() if r['passed']]
        failed = [c for c, r in results.items() if not r['passed']]

        feedback = f"Good progress! You've achieved {len(passed)}/{len(results)} criteria.\n\n"

        if failed:
            feedback += "Next steps:\n"
            for criterion in failed:
                feedback += f"  - {criterion}\n"

        return feedback

# Usage:
spec = load_spec('T07.G3.01')
grader = SkillGrader('T07.G3.01', spec)
result = grader.grade(student_code, runtime_data)

print(f"Score: {result['score']:.1%}")
print(f"Mastered: {result['mastered']}")
print(f"Feedback: {result['feedback']}")
```

---

## Part 6: Student Progress Tracking

### Scenario: Show a student their skill mastery and next recommendations.

### Step 1: Create a Mastery Record

```python
class StudentSkillProgress:
    def __init__(self, student_id):
        self.student_id = student_id
        self.mastery = {}  # skill_id -> {'score': 0-1, 'mastered': bool, 'date': datetime}

    def record_attempt(self, skill_id, score, mastered):
        """Record a skill attempt."""
        self.mastery[skill_id] = {
            'score': score,
            'mastered': mastered,
            'date': datetime.now()
        }

    def get_mastery_percent(self, topic_id=None, grade=None):
        """Get percentage of skills mastered."""
        relevant = []
        for skill in skills:
            if topic_id and skill['topic_id'] != topic_id:
                continue
            if grade and skill['grade'] != grade:
                continue
            relevant.append(skill['id'])

        if not relevant:
            return 0

        mastered = sum(1 for sid in relevant if self.mastery.get(sid, {}).get('mastered'))
        return mastered / len(relevant)

    def recommend_next_skills(self, num_recommendations=5):
        """Recommend the next 5 skills to attempt."""
        recommendations = []

        for skill in skills:
            # Only consider skills not yet attempted
            if skill['id'] in self.mastery:
                continue

            # Check if prerequisites are met
            prerequisites = dep_data.get(skill['id'], [])
            all_mastered = all(
                self.mastery.get(p, {}).get('mastered') for p in prerequisites
            )

            if all_mastered:
                recommendations.append(skill)

        # Prioritize:
        # 1. Current grade level
        # 2. Topics with started work
        # 3. Hub skills

        return recommendations[:num_recommendations]
```

### Step 2: Create a Dashboard View

```
╔════════════════════════════════════════════════════════════╗
║ Student Skill Progress - Alex Chen (Grade 3)               ║
╠════════════════════════════════════════════════════════════╣
║                                                             ║
║ Overall Progress: 24/143 skills mastered (16.8%)           ║
║ ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   ║
║                                                             ║
║ By Domain:                                                  ║
║  • Algorithms & Design:    12/18 mastered ███░░░░░░ 66%   ║
║  • Programming:            10/45 mastered ██░░░░░░░░ 22%   ║
║  • Data & Analysis:         2/8 mastered  ██░░░░░░░░ 25%   ║
║  • Systems & Security:      0/3 mastered  ░░░░░░░░░░  0%   ║
║  • Computing & Society:     0/2 mastered  ░░░░░░░░░░  0%   ║
║                                                             ║
║ Recommended Next Skills:                                    ║
║                                                             ║
║  1. [In Progress] T07.G3.01 - Use a repeat loop           ║
║     Prerequisites: ✓ Complete  Due: 2024-11-24             ║
║                                                             ║
║  2. [Recommended] T08.G2.01 - Use if/then in a sequence   ║
║     Prerequisites: ✓ Complete                              ║
║                                                             ║
║  3. [Ready] T09.G2.01 - Assign a value to a variable      ║
║     Prerequisites: ✓ Complete                              ║
║                                                             ║
║  4. [Upcoming] T10.G3.01 - Use lists to store values       ║
║     Prerequisites: ⏳ T09.G3.01 (in progress)               ║
║                                                             ║
║  5. [Future] T14.G4.01 - Create a simple game level        ║
║     Prerequisites: ⏳ T08.G3.01, T09.G4.01 (in progress)   ║
║                                                             ║
╚════════════════════════════════════════════════════════════╝
```

---

## Part 7: Analytics and Insights

### Scenario: Identify which skills are hard for students and which are taught well.

### Step 1: Calculate Skill Difficulty

```python
def analyze_skill_difficulty(skill_id, class_attempts):
    """
    Analyze a skill across a class.

    Args:
        skill_id: Skill to analyze
        class_attempts: List of {'student_id': s, 'score': 0-1, 'time_mins': int}

    Returns:
        {'avg_score': 0-1, 'mastery_rate': 0-1, 'avg_time': minutes, 'difficulty': 'easy'/'medium'/'hard'}
    """

    if not class_attempts:
        return None

    scores = [a['score'] for a in class_attempts]
    avg_score = sum(scores) / len(scores)
    mastery_rate = sum(1 for s in scores if s >= 0.75) / len(scores)
    avg_time = sum(a.get('time_mins', 0) for a in class_attempts) / len(class_attempts)

    # Difficulty heuristic: low mastery + high time = hard
    if mastery_rate < 0.5:
        difficulty = 'hard'
    elif mastery_rate >= 0.8:
        difficulty = 'easy'
    else:
        difficulty = 'medium'

    return {
        'avg_score': avg_score,
        'mastery_rate': mastery_rate,
        'avg_time_mins': avg_time,
        'difficulty': difficulty,
        'num_students': len(class_attempts)
    }

# Usage:
attempts = [
    {'student_id': 'alex', 'score': 0.9, 'time_mins': 20},
    {'student_id': 'blake', 'score': 0.75, 'time_mins': 45},
    {'student_id': 'casey', 'score': 0.6, 'time_mins': 60},
]
analysis = analyze_skill_difficulty('T07.G3.01', attempts)

print(f"Mastery rate: {analysis['mastery_rate']:.0%}")
if analysis['mastery_rate'] < 0.75:
    print("⚠️ This skill may need more instruction time")
```

### Step 2: Identify Struggling Topics

```python
def find_struggling_topics(class_progress):
    """Find topics where students are struggling."""

    topic_analyses = {}

    for topic_id in set(s['topic_id'] for s in skills):
        topic_skills = [s['id'] for s in skills if s['topic_id'] == topic_id]

        # Gather all attempts for this topic
        attempts_by_skill = defaultdict(list)
        for student_id, mastery in class_progress.items():
            for skill_id, record in mastery.items():
                if skill_id in topic_skills:
                    attempts_by_skill[skill_id].append(record)

        # Analyze topic
        if attempts_by_skill:
            avg_mastery = sum(
                sum(1 for r in attempts if r.get('mastered'))
                for attempts in attempts_by_skill.values()
            ) / len(attempts_by_skill)

            topic_analyses[topic_id] = {
                'avg_mastery': avg_mastery,
                'num_skills_attempted': len(attempts_by_skill)
            }

    # Return struggling topics (mastery < 60%)
    struggling = sorted(
        [(t, a) for t, a in topic_analyses.items() if a['avg_mastery'] < 0.6],
        key=lambda x: x[1]['avg_mastery']
    )

    return struggling

# Usage:
struggling = find_struggling_topics(class_progress_data)
print("Topics needing more instruction time:")
for topic_id, analysis in struggling[:3]:
    topic_name = [s['topic_name'] for s in skills if s['topic_id'] == topic_id][0]
    print(f"  • {topic_name}: {analysis['avg_mastery']:.0%} mastery")
```

---

## Part 8: Adapting the Skill Map

### How to Customize for Your Context

#### Option 1: Add Custom Skills

```json
{
  "id": "T14_CUSTOM.01",
  "title": "Create a Scratch game with a local storyline",
  "short_name": "Scratch game with local story",
  "topic_id": "T14",
  "grade": 4,
  "description": "Students create a 2D game in Scratch that uses local landmarks or characters...",
  "dependencies": ["T14.G4.01", "T06.G3.03"]
}
```

Add to your database with a custom prefix (e.g., `T14_CUSTOM`) to distinguish from official skills.

#### Option 2: Adjust Grade Levels

If you want to teach a skill at a different grade:

1. Check its prerequisites (ensure your grade has taught them)
2. Adjust the grade field in your database
3. Re-run dependency validation (ensure no Grade N skill requires Grade N+1)

```python
# Example: Teach T08.G4.01 (nested if/else) in Grade 3 instead of Grade 4
skill_to_adjust = next(s for s in skills if s['id'] == 'T08.G4.01')
prerequisite_skills = dep_data['T08.G4.01']

# Check that all prerequisites are available in Grade 3
grade_3_skills = {s['id'] for s in skills if s['grade'] <= 3}
all_available = all(p in grade_3_skills for p in prerequisite_skills)

if all_available:
    # Safe to teach in Grade 3
    skill_to_adjust['grade'] = 3
else:
    print(f"Cannot move to Grade 3; missing prerequisites: {prerequisite_skills - grade_3_skills}")
```

#### Option 3: Create Topic Clusters

Group multiple topics for thematic units:

```python
def create_thematic_unit(unit_name, topic_ids, grade):
    """Create a thematic unit combining multiple topics."""

    unit_skills = []
    for skill in skills:
        if skill['topic_id'] in topic_ids and skill['grade'] == grade:
            unit_skills.append(skill)

    # Sort by dependency to suggest teaching order
    sorted_skills = topological_sort_skills_multi(unit_skills)

    return {
        'name': unit_name,
        'topics': topic_ids,
        'grade': grade,
        'skills': sorted_skills,
        'estimated_duration_hours': len(sorted_skills) * 1.5
    }

# Example: "Interactive Storytelling" unit for Grade 4
storytelling_unit = create_thematic_unit(
    "Interactive Storytelling",
    ['T15', 'T14', 'T06', 'T09'],  # Animation, Games, Events, Variables
    grade=4
)
```

---

## Part 9: Integration Patterns

### Pattern 1: LMS Integration

```python
# Pseudocode for connecting to Canvas, Blackboard, etc.

def sync_skills_to_lms(lms_api, skills_data):
    """Push skills to LMS as learning standards."""

    for skill in skills_data:
        lms_api.create_learning_objective({
            'code': skill['id'],
            'title': skill['title'],
            'description': skill['description'],
            'grade_level': skill['grade'],
            'subject': domains[skill['topic_id']]['domain_name'],
            'tags': [skill['topic_id']]
        })

def track_completion_from_lms(lms_api, student_id):
    """Pull student mastery from LMS."""

    submissions = lms_api.get_student_submissions(student_id)
    mastered_skills = set()

    for submission in submissions:
        if submission['score'] >= 0.75:
            mastered_skills.add(submission['learning_objective_code'])

    return mastered_skills
```

### Pattern 2: Platform Integration

```javascript
// JavaScript for CreatiCode platform

class SkillTracker {
  constructor(apiEndpoint) {
    this.api = apiEndpoint;
    this.skills = [];
    this.dependencies = {};
  }

  async loadSkillMap() {
    const response = await fetch(`${this.api}/skills/all.json`);
    this.skills = await response.json();

    const depResponse = await fetch(`${this.api}/dependencies/all.json`);
    this.dependencies = await depResponse.json();
  }

  canAttemptSkill(studentId, skillId, masteredSkills) {
    const prerequisites = this.dependencies[skillId] || [];
    const missing = prerequisites.filter(p => !masteredSkills.has(p));
    return {
      canAttempt: missing.length === 0,
      missingPrerequisites: missing
    };
  }

  recordMastery(studentId, skillId, score) {
    return fetch(`${this.api}/students/${studentId}/mastery`, {
      method: 'POST',
      body: JSON.stringify({ skillId, score })
    });
  }

  getRecommendations(studentId, numRecommendations = 5) {
    const mastery = this.getMasteredSkills(studentId);
    const recommendations = [];

    for (const skill of this.skills) {
      if (mastery.has(skill.id)) continue;
      const { canAttempt } = this.canAttemptSkill(studentId, skill.id, mastery);
      if (canAttempt) recommendations.push(skill);
    }

    return recommendations.slice(0, numRecommendations);
  }
}

// Usage:
const tracker = new SkillTracker('https://api.creaticode.com');
await tracker.loadSkillMap();

const canTeach = tracker.canAttemptSkill('student123', 'T07.G3.01', new Set(['T06.G2.03']));
if (canTeach.canAttempt) {
  // Assign the skill
} else {
  // Show prerequisites
  console.log(`Missing: ${canTeach.missingPrerequisites.join(', ')}`);
}
```

### Pattern 3: Analytics Integration

```python
# Connect to analytics platform (e.g., Amplitude, Mixpanel)

class SkillAnalytics:
    def __init__(self, analytics_api):
        self.analytics = analytics_api

    def track_skill_attempt(self, student_id, skill_id, score, time_seconds):
        """Log a skill attempt."""

        skill = next((s for s in skills if s['id'] == skill_id), None)

        self.analytics.track('skill_attempt', {
            'user_id': student_id,
            'skill_id': skill_id,
            'topic_id': skill['topic_id'] if skill else None,
            'grade': skill['grade'] if skill else None,
            'score': score,
            'time_seconds': time_seconds,
            'mastered': score >= 0.75
        })

    def get_skill_analytics(self, skill_id):
        """Get aggregated analytics for a skill."""

        return self.analytics.query(f"""
            SELECT
                COUNT(*) as attempts,
                AVG(score) as avg_score,
                SUM(CASE WHEN mastered THEN 1 ELSE 0 END) / COUNT(*) as mastery_rate,
                AVG(time_seconds) as avg_time
            WHERE skill_id = '{skill_id}'
        """)
```

---

## Part 10: Troubleshooting

### Problem: "Students can't move forward - too many missing prerequisites"

**Solution:** Check if prerequisites are appropriate for your context. Options:
1. Adjust grade levels (teach prerequisites earlier)
2. Provide more scaffolding for missing skills
3. Create prerequisite catch-up mini-lessons
4. Consider if the skill actually needs all listed prerequisites

### Problem: "Some dependencies don't make sense for our curriculum"

**Solution:** Review dependencies and adjust:

```python
# Check a dependency
skill = dep_data['T14.G4.02']
print(skill['notes'])  # May explain the reasoning
print(skill['quality_issues'])  # Any concerns flagged

# Modify if needed (but keep a record)
# skill['dependencies'].remove('T09.G5.01')
# Add comment: "Removed - our students don't need this for this skill"
```

### Problem: "Grade 8 skills are too hard for our students"

**Solution:** Either:
1. Adjust prerequisites (add more foundational work earlier)
2. Move Grade 8 skills to Grade 9 (if you have it)
3. Create scaffolded versions of Grade 8 skills for Grade 7

### Problem: "We want to teach topics in a different order"

**Solution:** OK! As long as you respect dependencies:

```python
# Check if T20 (Algorithmic Art) can be taught before T19 (Multiplayer)
t20_deps = set(dep for skill_data in dep_data.values()
               if skill_data['topic'] == 'T20'
               for dep in skill_data['dependencies'])
t19_skills = {s['id'] for s in skills if s['topic_id'] == 'T19'}

if t20_deps & t19_skills:
    print("Warning: T20 depends on T19. Can't teach T20 first.")
else:
    print("OK: T20 can be taught independently of T19")
```

---

## Summary: Quick Implementation Checklist

- [ ] Load `skills_enriched.json` into your database
- [ ] Load dependency files into your database
- [ ] Create skill browser UI (filter, search, details)
- [ ] Implement prerequisite checking
- [ ] Add skill assignment to student accounts
- [ ] Create auto-grading specs for 10 pilot skills
- [ ] Implement skill mastery tracking
- [ ] Create student progress dashboard
- [ ] Create teacher analytics views
- [ ] Test with real teachers and students
- [ ] Gather feedback and iterate

---

**Document Version:** 1.0
**For:** Platform developers, curriculum designers, technical leads
**Next Step:** Load the data and start building!
