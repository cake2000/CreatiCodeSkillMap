# CreatiCode Track System: Implementation & Migration Plan

## Executive Summary

This document provides a step-by-step plan for implementing the three-track system (Standard, Enrichment, Competition) in the CreatiCode K-8 platform, with focus on Grades 7-8 where differentiation is most critical.

**Timeline:** 6-8 weeks for full implementation
**Priority:** HIGH for 3 skills, MEDIUM for 11 skills, LOW for remaining
**Impact:** Ensures age-appropriate curriculum while supporting advanced learners and competition preparation

---

## Phase 1: Data Model Updates (Week 1)

### 1.1 Add Track Metadata to Skill Schema

**Current Skill Schema:**
```json
{
  "id": "T10.G8.02",
  "title": "Implement a sorting algorithm",
  "short_name": "Write a sorting algorithm",
  "topic_id": "T10",
  "grade": 8,
  "description": "...",
  "dependencies": [...],
  ...
}
```

**NEW: Add Track Fields:**
```json
{
  "id": "T10.G8.02",
  "title": "Implement a sorting algorithm",
  "short_name": "Write a sorting algorithm",
  "topic_id": "T10",
  "grade": 8,
  "description": "...",
  "dependencies": [...],

  // NEW FIELDS
  "difficulty_track": "competition",
  "track_metadata": {
    "reason": "AP CS A content, requires formal reasoning",
    "competitions": ["ACSL Junior", "Lanqiao Senior", "NOC Junior"],
    "alternative_standard_id": "T10.G8.02-STD",
    "scaffolding_required": false,
    "terminology_revision": null,
    "priority": "HIGH"
  }
}
```

**Field Definitions:**

| Field | Type | Required | Values | Description |
|-------|------|----------|--------|-------------|
| `difficulty_track` | string | YES | "standard", "enrichment", "competition" | Primary track assignment |
| `track_metadata.reason` | string | NO | freeform | Why this track was assigned |
| `track_metadata.competitions` | array | NO | Competition names | Relevant competitions |
| `track_metadata.alternative_standard_id` | string | NO | Skill ID | ID of standard-track alternative |
| `track_metadata.scaffolding_required` | boolean | NO | true/false | Does skill need special scaffolding? |
| `track_metadata.terminology_revision` | object | NO | see below | If terminology needs updating |
| `track_metadata.priority` | string | NO | "HIGH", "MEDIUM", "LOW" | Implementation priority |

**Terminology Revision Object:**
```json
"terminology_revision": {
  "old_title": "Implement a Monte Carlo simulation",
  "new_title": "Run many trials to estimate a probability",
  "old_terms": ["Monte Carlo", "stochastic"],
  "new_terms": ["repeated trials", "probability estimation"],
  "reason": "Make terminology accessible to 7th graders"
}
```

### 1.2 Database Migration Script

**Action Items:**
1. Add columns to skills table
2. Create `skill_track_metadata` table for complex metadata
3. Add indexes for efficient track filtering
4. Create view for "standard-only" skill trees

**SQL Migration (PostgreSQL example):**
```sql
-- Add track column to skills table
ALTER TABLE skills
ADD COLUMN difficulty_track VARCHAR(20) DEFAULT 'standard';

-- Create enum constraint
ALTER TABLE skills
ADD CONSTRAINT difficulty_track_check
CHECK (difficulty_track IN ('standard', 'enrichment', 'competition'));

-- Add metadata JSON column
ALTER TABLE skills
ADD COLUMN track_metadata JSONB;

-- Create index for filtering
CREATE INDEX idx_skills_difficulty_track ON skills(difficulty_track);
CREATE INDEX idx_skills_grade_track ON skills(grade, difficulty_track);

-- Create view for standard-only progression
CREATE VIEW standard_skills AS
SELECT * FROM skills WHERE difficulty_track = 'standard';
```

### 1.3 Initial Data Population

**Process:**
1. Import track assignments from `SKILL_TRACK_CATEGORIZATION.json`
2. Mark all non-flagged skills as "standard" (default)
3. Apply specific assignments to 31 flagged Grade 7-8 skills
4. Validate dependencies don't violate track rules

**Validation Query:**
```sql
-- Find standard skills that depend on enrichment/competition
SELECT s.id, s.title, s.difficulty_track, d.dependency_id, ds.difficulty_track
FROM skills s
JOIN skill_dependencies sd ON s.id = sd.skill_id
JOIN skills ds ON sd.dependency_id = ds.id
WHERE s.difficulty_track = 'standard'
  AND ds.difficulty_track IN ('enrichment', 'competition');
```

**Expected Result:** Zero violations (if found, reassign or fix dependencies)

---

## Phase 2: High-Priority Skill Revisions (Week 2)

### 2.1 T10.G8.02 - Sorting Algorithm

**Priority:** HIGH

**Current State:**
- Title: "Implement a sorting algorithm (bubble sort or selection sort)"
- Track: Should be Competition
- Issue: AP CS A content, too advanced for standard 8th grade

**Actions Required:**

**Step 1: Create Competition Version (keep existing)**
```json
{
  "id": "T10.G8.02",
  "title": "Implement a sorting algorithm (bubble sort or selection sort)",
  "short_name": "Write a sorting algorithm",
  "difficulty_track": "competition",
  "track_metadata": {
    "reason": "AP CS A content, requires formal reasoning about algorithm correctness",
    "competitions": ["ACSL Junior", "Lanqiao Senior", "NOC Junior"],
    "alternative_standard_id": "T10.G8.02-STD",
    "priority": "HIGH"
  }
}
```

**Step 2: Create Standard Alternative**
```json
{
  "id": "T10.G8.02-STD",
  "title": "Use sort blocks to organize data by criteria",
  "short_name": "Sort data using built-in tools",
  "topic_id": "T10",
  "grade": 8,
  "difficulty_track": "standard",
  "description": "Students use CreatiCode's built-in sort blocks to organize lists and tables by different attributes (alphabetical, numerical, by property). They understand WHAT sorting accomplishes and WHEN to use it, without implementing the algorithm from scratch.",
  "student_prompt": "Use sort blocks to organize your data in different ways: alphabetically, by number, by custom properties. Explain when each type of sorting is useful.",
  "activity_type": "coding_project",
  "auto_grade_rules": {
    "type": "code_analysis",
    "checks": [
      "Uses sort block at least twice",
      "Sorts by different criteria (e.g., alphabetical and numerical)",
      "Data is correctly organized after sorting"
    ]
  },
  "dependencies": ["T10.G7.01", "T01.G1.01", "T09.G3.01", "T07.G3.01"],
  "csta_code": "2-AP-14",
  "track_metadata": {
    "replaces_competition_skill": "T10.G8.02",
    "priority": "HIGH"
  }
}
```

**Step 3: Update Skill Tree UI**
- Main path shows T10.G8.02-STD (standard)
- Optional branch shows T10.G8.02 with 🏆 Competition badge
- Tooltip explains difference

**Step 4: Communication**
- Email to teachers explaining the change
- Add note to teacher guide for Topic T10
- Update curriculum maps

---

### 2.2 T27.G8.02 - Causal Relationships → Variable Relationships

**Priority:** HIGH

**Current State:**
- Title: "Analyze two variables for potential causal relationships"
- Issue: Causal inference is college-level statistics

**Actions Required:**

**Step 1: Revise Existing Skill**
```json
{
  "id": "T27.G8.02",
  "title": "Explore whether two variables are related",
  "short_name": "Investigate variable relationships",
  "topic_id": "T27",
  "grade": 8,
  "difficulty_track": "enrichment",
  "description": "Students explore whether two variables seem to be related (when one is high, is the other high too?) and discuss possible reasons. They learn that sometimes both variables are affected by a third factor (e.g., ice cream sales and drowning both increase in summer because of heat). No formal causal analysis or hypothesis testing required.",
  "student_prompt": "Pick two variables from your data. Do they seem related? When one goes up, does the other go up? Or down? What might explain this pattern? Could something else be causing both to change?",
  "activity_type": "data_analysis",
  "learning_objectives": [
    "Identify when variables appear to be related",
    "Distinguish between 'related' and 'one causes the other'",
    "Recognize that correlation doesn't prove causation",
    "Discuss alternative explanations (third variables)"
  ],
  "track_metadata": {
    "terminology_revision": {
      "old_title": "Analyze two variables for potential causal relationships",
      "new_title": "Explore whether two variables are related",
      "old_terms": ["causal relationships", "causation"],
      "new_terms": ["related", "relationship", "pattern"],
      "reason": "Causal inference is beyond 8th grade; correlation exploration is appropriate"
    },
    "scaffolding_required": true,
    "priority": "HIGH"
  }
}
```

**Step 2: Create Teaching Resources**
- Example: "Ice cream sales & drowning rates" (both caused by summer heat)
- Example: "Study time & test scores" (likely related AND causal)
- Example: "Shoe size & reading ability" (both caused by age, not causal)
- Discussion guide: "Related vs. one causes the other"

**Step 3: Update Assessments**
- OLD: "Prove causation using experimental design"
- NEW: "Identify if variables are related and discuss possible explanations"

---

### 2.3 T35.G7.01 - Systemic Impacts → Pros and Cons

**Priority:** HIGH

**Current State:**
- Title: "Analyze unintended systemic impacts of a technology"
- Issue: Systems thinking and second-order effects too advanced

**Actions Required:**

**Step 1: Revise Existing Skill**
```json
{
  "id": "T35.G7.01",
  "title": "Identify pros and cons of a technology",
  "short_name": "List technology trade-offs",
  "topic_id": "T35",
  "grade": 7,
  "difficulty_track": "enrichment",
  "description": "Students identify and list 3-5 positive effects and 3-5 negative effects of a technology (e.g., smartphones, social media, AI assistants). They discuss who benefits, who is harmed, and whether the technology is 'worth it' overall.",
  "student_prompt": "Choose a technology that affects your life. List at least 3 good things about it and 3 bad things about it. Who benefits most? Who is harmed? Is it worth it overall?",
  "activity_type": "discussion_and_writing",
  "learning_objectives": [
    "Identify multiple positive effects of a technology",
    "Identify multiple negative effects of a technology",
    "Recognize that technologies have trade-offs",
    "Consider who is affected differently by technology"
  ],
  "track_metadata": {
    "terminology_revision": {
      "old_title": "Analyze unintended systemic impacts of a technology",
      "new_title": "Identify pros and cons of a technology",
      "old_terms": ["systemic impacts", "ripple effects", "second-order effects"],
      "new_terms": ["pros and cons", "good things and bad things", "trade-offs"],
      "reason": "Systems thinking is too advanced for 7th grade; pros/cons listing is appropriate"
    },
    "priority": "HIGH"
  }
}
```

**Step 2: Create Activity Template**
```
Technology: _______________________

GOOD THINGS:
1. _______________________________________________
2. _______________________________________________
3. _______________________________________________
4. _______________________________________________
5. _______________________________________________

BAD THINGS:
1. _______________________________________________
2. _______________________________________________
3. _______________________________________________
4. _______________________________________________
5. _______________________________________________

WHO BENEFITS MOST? _____________________________

WHO IS HARMED MOST? _____________________________

IS IT WORTH IT? WHY OR WHY NOT?
_________________________________________________
_________________________________________________
_________________________________________________
```

**Step 3: Update Rubric**
- OLD: "Analyzes system-level ripple effects and unintended consequences"
- NEW: "Identifies multiple positive and negative effects with specific examples"

---

## Phase 3: Medium-Priority Terminology Fixes (Week 3)

### 3.1 Monte Carlo → Repeated Trials (2 skills)

**Skills to Update:**
1. T28.G7.02: "Implement a Monte Carlo simulation to estimate a probability"
2. T07.G8.01: "Monte Carlo simulations with loops"

**Changes:**

**T28.G7.02:**
```json
{
  "id": "T28.G7.02",
  "title": "Run many trials to estimate a probability",
  "short_name": "Estimate probability through repeated trials",
  "difficulty_track": "standard",
  "track_metadata": {
    "terminology_revision": {
      "old_title": "Implement a Monte Carlo simulation to estimate a probability",
      "new_title": "Run many trials to estimate a probability",
      "old_terms": ["Monte Carlo", "stochastic"],
      "new_terms": ["many trials", "repeated trials", "probability estimation"],
      "reason": "Monte Carlo is intimidating jargon; concept is age-appropriate"
    },
    "priority": "MEDIUM"
  }
}
```

**T07.G8.01:**
```json
{
  "id": "T07.G8.01",
  "title": "Use loops for repeated simulation trials",
  "short_name": "Repeated trial simulations with loops",
  "difficulty_track": "standard",
  "track_metadata": {
    "terminology_revision": {
      "old_title": "Monte Carlo simulations with loops",
      "new_title": "Use loops for repeated simulation trials",
      "reason": "Simplify terminology while keeping content"
    }
  }
}
```

**Implementation:**
- Update titles in database
- Update all references in curriculum materials
- Teachers can mention "also called Monte Carlo" for advanced students
- No activity content changes needed

---

### 3.2 Distributions → Averages and Ranges

**Skill:** T27.G7.04

**Change:**
```json
{
  "id": "T27.G7.04",
  "title": "Compare datasets using averages and ranges",
  "short_name": "Compare data with mean and range",
  "difficulty_track": "standard",
  "description": "Students compare two datasets by calculating their means (averages) and ranges (min to max), identifying which dataset tends higher or has more spread. They use simple statistics, not formal distribution analysis.",
  "track_metadata": {
    "terminology_revision": {
      "old_title": "Compare distributions of data",
      "new_title": "Compare datasets using averages and ranges",
      "old_terms": ["distributions", "spread", "shape"],
      "new_terms": ["averages", "ranges", "which is higher"],
      "reason": "Distribution suggests formal statistics (skew, variance); mean and range are appropriate"
    },
    "priority": "MEDIUM"
  }
}
```

**Assessment Updates:**
- OLD: "Compare the shape and spread of distributions"
- NEW: "Calculate and compare means and ranges; identify which dataset is higher/lower or more/less spread out"
- Avoid: skew, variance, standard deviation, normal distribution

---

### 3.3 Pseudocode with Templates (2 skills)

**Skills:** T01.G7.03, T02.G8.01

**Change:** Add scaffolding, keep terminology

```json
{
  "id": "T01.G7.03",
  "title": "Represent an algorithm in pseudocode or text code",
  "short_name": "Plan an algorithm using words and steps",
  "difficulty_track": "standard",
  "track_metadata": {
    "scaffolding_required": true,
    "scaffolding_details": {
      "provide_templates": true,
      "use_fill_in_blank": true,
      "translate_from_scratch": true,
      "examples_before_practice": true
    },
    "priority": "MEDIUM"
  }
}
```

**Create Template Library:**

**Template 1: Search Algorithm**
```
Algorithm to find [item] in [list]:

Step 1: Start at the beginning of [list]
Step 2: For each item in [list]:
  - If item equals [target], then FOUND
  - Otherwise, continue to next item
Step 3: If reached end, NOT FOUND
```

**Template 2: Accumulation**
```
Algorithm to calculate [result]:

Step 1: Start with [variable] = 0
Step 2: Repeat for each [item]:
  - Add [value] to [variable]
Step 3: Return [variable]
```

**Template 3: Conditional Processing**
```
Algorithm to [goal]:

Step 1: Get input [data]
Step 2: For each [item] in [data]:
  - If [condition] is true:
    - Do [action A]
  - Otherwise:
    - Do [action B]
Step 3: Done
```

---

## Phase 4: UI and UX Updates (Week 4-5)

### 4.1 Skill Tree Visualization

**Standard Skills (no badge):**
```
📘 T10.G7.01 - Design tables for real data
└─ ✅ Mastered
```

**Enrichment Skills (star badge):**
```
⭐ T01.G7.04 - Analyze algorithm edge cases
└─ 🔓 Unlocked (optional challenge)
```

**Competition Skills (trophy badge):**
```
🏆 T10.G8.02 - Implement sorting algorithm
└─ 🔒 Competition Track (ACSL, Lanqiao)
   └─ Alternative: T10.G8.02-STD (Use sort blocks)
```

### 4.2 Filtering and Display Options

**Teacher Dashboard:**
- [ ] Show only Standard track (default for curriculum planning)
- [ ] Show Standard + Enrichment (for advanced classes)
- [ ] Show All tracks (for competition prep)

**Student Dashboard:**
- Standard skills always visible
- Enrichment skills visible after prerequisites + "Try a challenge!"
- Competition skills in separate "Competition Prep" section

### 4.3 Progress Tracking Updates

**New Metrics:**

**Student View:**
```
Grade 8 Progress

Core Skills (Standard): 42/48 (88%)
├─ Algorithms: 8/10
├─ Data Structures: 10/12
├─ Data Analysis: 12/15
└─ Ethics & Society: 12/11

Challenge Skills (Enrichment): 5/12 (42%)
⭐ You're excelling at advanced challenges!

Competition Skills: 1/3 (33%)
🏆 Keep practicing for ACSL!
```

**Teacher View:**
```
Class Progress - Grade 8

Standard Track: 85% average mastery
Enrichment Track: 34% participation
Competition Track: 12% participation

Students ready for enrichment: 18/25
Students ready for competition: 4/25

Recommended actions:
- Introduce enrichment challenges to high performers
- Form competition prep study group (4 interested students)
```

### 4.4 Skill Detail Page Updates

**Add Track Information:**

```
┌─────────────────────────────────────────────┐
│ T10.G8.02-STD                               │
│ Use sort blocks to organize data            │
│                                             │
│ Track: 📘 Standard                          │
│ Grade: 8                                    │
│                                             │
│ [Description...]                            │
│                                             │
│ 💡 Looking for more challenge?             │
│    Try: 🏆 T10.G8.02 (Competition)         │
│    Implement sorting algorithm from scratch │
└─────────────────────────────────────────────┘
```

For competition skills:
```
┌─────────────────────────────────────────────┐
│ T10.G8.02                                   │
│ Implement sorting algorithm                 │
│                                             │
│ Track: 🏆 Competition                       │
│ Relevant for: ACSL Junior, Lanqiao Senior  │
│                                             │
│ ⚠️ This is advanced content typically      │
│    taught in high school AP CS courses.     │
│                                             │
│ [Description...]                            │
│                                             │
│ Alternative for standard track:            │
│    📘 T10.G8.02-STD - Use sort blocks      │
└─────────────────────────────────────────────┘
```

---

## Phase 5: Content Updates (Week 5-6)

### 5.1 Activity Updates for Revised Skills

**For each revised skill, update:**
1. Student prompts
2. Example problems
3. Auto-grading rubrics
4. Teacher guides
5. Video tutorials (if exist)

**Example: T27.G8.02 Activity Update**

**OLD Activity:**
- Prompt: "Analyze whether study time causes higher test scores"
- Requires: Formal hypothesis testing, control for confounds
- Rubric: "Proves or disproves causation using experimental design"

**NEW Activity:**
- Prompt: "Explore whether study time and test scores are related"
- Requires: Plot data, observe patterns, discuss possible explanations
- Rubric: "Identifies relationship and discusses at least 2 possible explanations"

**NEW Auto-Grade:**
```json
{
  "type": "written_response",
  "required_elements": [
    "Describes whether variables appear related (yes/no/somewhat)",
    "Provides at least one example from data",
    "Discusses at least one alternative explanation (e.g., 'both affected by...')",
    "Does NOT claim proof of causation without acknowledging limitations"
  ],
  "ai_assisted_grading": true,
  "teacher_review_required": false
}
```

### 5.2 New Scaffolding Materials

**Create for Each Scaffolded Skill:**

**Recursion (T01.G8.02):**
- Video: "Recursion in Nature" (fractals, spirals, branching)
- Interactive: Russian dolls animation
- Worksheet: Identify recursive patterns
- DO NOT: Require writing recursive code

**AI Bias (T28.G8.03, T21.G7.02, T23.G8.04):**
- Case study library (real examples of AI bias)
- Testing protocol (try AI with diverse inputs)
- Discussion guides (who is harmed? why did this happen?)
- DO NOT: Require understanding ML architecture

**Pseudocode (T01.G7.03, T02.G8.01):**
- Template library (6-8 common algorithm patterns)
- Scratch-to-pseudocode translator
- Fill-in-the-blank exercises
- Worked examples

### 5.3 Teacher Professional Development

**Create Training Module:**

**Module 1: Understanding the Track System (30 min)**
- Why three tracks?
- How to use each track
- Dependency rules
- When to offer enrichment/competition

**Module 2: Teaching Revised Skills (45 min)**
- What changed and why
- New scaffolding materials
- Updated assessments
- Addressing parent questions

**Module 3: Differentiation Strategies (30 min)**
- Using enrichment for advanced students
- Supporting struggling students in standard track
- Running competition prep programs
- Mixed-ability classroom management

---

## Phase 6: Documentation and Communication (Week 6-7)

### 6.1 Updated Documentation

**Create/Update:**

1. **Curriculum Overview** (external-facing)
   - Mention three-track system
   - Explain how it serves all learners
   - List competition pathways

2. **Teacher Guide** (for each topic)
   - Which skills are standard/enrichment/competition
   - How to teach revised skills
   - Scaffolding materials locations

3. **Parent Communication Template**
   ```
   Dear Parents,

   We're excited to share that CreatiCode now offers three learning tracks:

   📘 Standard Track: Core skills for all students
   ⭐ Enrichment Track: Optional challenges for deeper learning
   🏆 Competition Track: Preparation for coding competitions

   Your child will primarily work in the Standard Track, with opportunities
   to explore Enrichment challenges. If your child is interested in coding
   competitions (ACSL, Scratch Olympiad, etc.), please let us know!

   [Read more: link to track system overview]
   ```

4. **Competition Prep Guide** (new document)
   - Which competitions exist
   - What skills are needed
   - How to prepare
   - Timeline for each competition
   - How to register

### 6.2 FAQ Document

**Create comprehensive FAQ:**

**For Teachers:**
- Q: Can I skip standard skills? A: No, they're foundational
- Q: How do I grade enrichment? A: Extra credit or honors distinction
- Q: What if a student wants competition skills but isn't ready? A: ...

**For Students:**
- Q: Do I have to do enrichment skills? A: No, but they're fun challenges!
- Q: What's the difference between enrichment and competition? A: ...
- Q: Can I try competition skills if I'm in 6th grade? A: Yes, if ready!

**For Parents:**
- Q: Is my child falling behind if they only do standard? A: No! Standard is complete curriculum
- Q: How do I know if my child should try competition? A: ...
- Q: What's ACSL? A: ...

### 6.3 Communication Timeline

**Week 6:**
- Announce track system to teachers (email + webinar)
- Provide preview of changes
- Invite feedback

**Week 7:**
- Release updated platform with track system
- Send parent communication
- Update website and marketing materials
- Publish blog post explaining rationale

**Week 8:**
- Gather initial feedback
- Host Q&A session for teachers
- Monitor usage analytics
- Prepare for adjustments if needed

---

## Phase 7: Testing and Validation (Week 7-8)

### 7.1 Pilot Testing

**Recruit Pilot Teachers:**
- 5-10 teachers across different contexts
- Mix of: urban/rural, advanced/mixed-ability, competition-focused/general
- Provide early access to updated system

**Pilot Focus Areas:**
1. Are track assignments intuitive?
2. Is UI clear and helpful?
3. Are revised skills age-appropriate?
4. Is scaffolding sufficient?
5. How do students respond to enrichment?

### 7.2 Data Validation

**Run Automated Checks:**

**Check 1: Dependency Violations**
```sql
-- Should return 0 rows
SELECT s.id, s.difficulty_track, d.dependency_id, ds.difficulty_track
FROM skills s
JOIN skill_dependencies sd ON s.id = sd.skill_id
JOIN skills ds ON sd.dependency_id = ds.id
WHERE s.difficulty_track = 'standard'
  AND ds.difficulty_track IN ('enrichment', 'competition');
```

**Check 2: Orphaned Competition Skills**
```sql
-- Skills marked competition but no competitions listed
SELECT id, title
FROM skills
WHERE difficulty_track = 'competition'
  AND (track_metadata->>'competitions') IS NULL;
```

**Check 3: Missing Alternatives**
```sql
-- Competition skills without standard alternative
SELECT id, title
FROM skills
WHERE difficulty_track = 'competition'
  AND grade IN (7, 8)
  AND (track_metadata->>'alternative_standard_id') IS NULL;
```

### 7.3 Content Review

**Have curriculum team review:**
- [ ] All HIGH priority revisions complete and accurate
- [ ] Scaffolding materials created for flagged skills
- [ ] New activities align with revised learning objectives
- [ ] Terminology is consistently updated across all materials
- [ ] Teacher guides reflect changes

### 7.4 Accessibility Check

**Ensure track system doesn't create barriers:**
- Screen reader compatibility for track badges
- Color-blind safe color coding
- Clear text labels (not icon-only)
- Keyboard navigation works for all tracks
- Mobile view displays tracks clearly

---

## Phase 8: Launch and Monitor (Week 8+)

### 8.1 Staged Rollout

**Option A: All at once**
- Pros: Simpler, consistent experience
- Cons: Higher risk if issues found

**Option B: Gradual (recommended)**
- Week 8: Launch to existing pilot teachers
- Week 9: Open to all teachers (opt-in)
- Week 10: Make default for all new users
- Week 11: Migrate remaining users

### 8.2 Success Metrics

**Track These Metrics:**

**Adoption:**
- % of teachers using track filters
- % of students attempting enrichment
- % of students in competition track
- Number of competition prep programs started

**Engagement:**
- Time spent on enrichment vs standard
- Completion rates by track
- Student satisfaction ratings by track

**Outcomes:**
- Standard skill mastery rates (should remain high)
- Enrichment participation rates (target: 30-40%)
- Competition participation (track students who compete)

**Quality:**
- Teacher satisfaction with track system
- Parent feedback (positive/negative)
- Student feedback on difficulty appropriateness

### 8.3 Feedback Collection

**Week 9-12: Active Feedback Gathering**

**From Teachers:**
- Survey: "Is the track system helping you differentiate?"
- Interview: 5-10 teachers for deep insights
- Office hours: Weekly drop-in Q&A

**From Students:**
- Survey: "How do you feel about challenge skills?"
- Analytics: Are students trying enrichment?
- Focus groups: Small groups of advanced students

**From Parents:**
- Survey: "Do you understand the track system?"
- Feedback form: Open-ended questions
- Monitor support tickets for concerns

### 8.4 Iteration Plan

**Based on feedback, prepare to adjust:**

**If enrichment participation is too low (<20%):**
- Make enrichment more visible
- Add more incentives (badges, certificates)
- Reduce perceived difficulty
- Add more scaffolding

**If standard skills feel too easy:**
- Review if too much moved to enrichment
- Consider moving some enrichment back to standard
- Ensure adequate challenge in standard

**If competition track is confusing:**
- Clarify communication about competitions
- Add more resources about each competition
- Create competition prep pathways

---

## Risk Mitigation

### Risk 1: Teachers confused by track system

**Mitigation:**
- Comprehensive training materials
- Clear documentation
- Responsive support team
- FAQ document

**Fallback:**
- Option to hide tracks and see "all skills"
- Traditional view available

### Risk 2: Students feel discouraged by enrichment/competition labels

**Mitigation:**
- Positive framing ("challenge" not "advanced")
- Emphasize that standard is complete and sufficient
- Celebrate all achievement types
- Avoid language suggesting enrichment is "better"

**Fallback:**
- Allow customizing track names
- Option to hide track labels from students

### Risk 3: Parents misunderstand and think standard is "basic"

**Mitigation:**
- Clear communication that standard = full curriculum
- Emphasize "IXL for coding" quality
- Show standard skills are rigorous and complete
- Avoid language suggesting standard is lesser

**Fallback:**
- Rename tracks if "standard" causes issues
- Alternative names: "Core" / "Extended" / "Competition"

### Risk 4: Competition track too small/underutilized

**Mitigation:**
- Clear connection to real competitions
- Resources about competition opportunities
- Success stories from competition students
- Partnership with competition organizers

**Fallback:**
- Merge competition into enrichment if too small
- Keep metadata but simplify UI to two tracks

### Risk 5: Enrichment dependencies create accessibility issues

**Mitigation:**
- Careful dependency mapping
- Ensure no hidden prerequisites
- Regular dependency audits
- Student testing with diverse backgrounds

**Fallback:**
- Break dependencies if needed
- Add prerequisite lessons within enrichment skills

---

## Resource Requirements

### Engineering (4-6 weeks)

**Week 1: Database**
- Database schema updates: 16 hours
- Migration scripts: 8 hours
- Testing: 8 hours
- **Total: 32 hours**

**Week 2-3: Backend**
- API updates for track filtering: 16 hours
- Dependency validation: 8 hours
- Track assignment logic: 8 hours
- Testing: 16 hours
- **Total: 48 hours**

**Week 4-5: Frontend**
- UI components for tracks: 24 hours
- Skill tree visualization: 16 hours
- Dashboard updates: 16 hours
- Mobile responsive: 8 hours
- Testing: 16 hours
- **Total: 80 hours**

**Total Engineering: 160 hours (~4 weeks for 1 engineer)**

### Content Team (3-4 weeks)

**Week 2: HIGH Priority**
- Revise 3 skills completely: 24 hours
- Create alternatives: 16 hours
- Testing: 8 hours
- **Total: 48 hours**

**Week 3: MEDIUM Priority**
- Terminology updates (5 skills): 10 hours
- Scaffolding materials: 20 hours
- Activity updates: 10 hours
- **Total: 40 hours**

**Week 5-6: Documentation**
- Teacher guides: 16 hours
- Parent communications: 8 hours
- FAQ document: 8 hours
- Training modules: 16 hours
- **Total: 48 hours**

**Total Content: 136 hours (~3-4 weeks for 1 content creator)**

### Design (1-2 weeks)

- Track badge designs: 8 hours
- UI mockups: 16 hours
- Teacher dashboard designs: 8 hours
- Marketing materials: 8 hours
- **Total: 40 hours (~1 week for 1 designer)**

### Project Management

- Coordination: 2 hours/week × 8 weeks = 16 hours
- Testing coordination: 8 hours
- Stakeholder communication: 8 hours
- **Total: 32 hours**

### TOTAL RESOURCE ESTIMATE
- **Engineering:** 160 hours
- **Content:** 136 hours
- **Design:** 40 hours
- **PM:** 32 hours
- **TOTAL:** 368 hours (~9-10 person-weeks)

---

## Success Criteria

The track system implementation will be considered successful when:

### Technical Success
- ✅ All 31 flagged skills have track assignments
- ✅ Zero dependency violations (standard depending on enrichment/competition)
- ✅ UI clearly displays all three tracks
- ✅ Filtering by track works correctly
- ✅ Performance impact is minimal (<100ms query time)

### Content Success
- ✅ All HIGH priority revisions complete (3 skills)
- ✅ All MEDIUM priority revisions complete (11 skills)
- ✅ Scaffolding materials created for flagged skills
- ✅ Teacher guides updated
- ✅ Student activities revised to match new objectives

### Adoption Success
- ✅ 80%+ of teachers understand track system (survey)
- ✅ 30%+ of advanced students try enrichment (analytics)
- ✅ 5%+ of students explore competition track (analytics)
- ✅ 90%+ teacher satisfaction with track system (survey)

### Outcome Success
- ✅ Standard skill mastery rates remain high (85%+)
- ✅ No increase in student frustration (survey)
- ✅ Positive parent feedback (>80% positive sentiment)
- ✅ At least 3 teachers start competition prep programs

---

## Timeline Summary

| Week | Phase | Key Activities | Deliverables |
|------|-------|----------------|--------------|
| 1 | Data Model | Schema updates, migration | Database ready |
| 2 | HIGH Priority | Revise 3 critical skills | Updated skills, alternatives |
| 3 | MEDIUM Priority | Terminology fixes | 11 skills updated |
| 4-5 | UI/UX | Build track interfaces | Working UI |
| 5-6 | Content | Activities, scaffolding | Teaching materials |
| 6-7 | Documentation | Guides, communications | All docs ready |
| 7-8 | Testing | Pilot, validation | Tested system |
| 8+ | Launch | Rollout, monitoring | Live system |

---

## Appendix A: Quick Reference - Priority Matrix

### HIGH Priority (Do First - Week 2)
| Skill ID | Action | Estimated Hours |
|----------|--------|-----------------|
| T10.G8.02 | Create competition + standard versions | 16 |
| T27.G8.02 | Revise to "explore relationships" | 8 |
| T35.G7.01 | Revise to "pros and cons" | 8 |

### MEDIUM Priority (Week 3)
| Skill ID | Action | Estimated Hours |
|----------|--------|-----------------|
| T28.G7.02 | Rename "Monte Carlo" | 2 |
| T07.G8.01 | Rename "Monte Carlo" | 2 |
| T27.G7.04 | Rename "distributions" | 3 |
| T01.G7.03 | Add scaffolding | 5 |
| T02.G8.01 | Add scaffolding | 5 |

### LOW Priority (Week 5, if time)
| Skill ID | Action | Estimated Hours |
|----------|--------|-----------------|
| T01.G8.02 | Ensure visual recursion only | 4 |
| T28.G8.03 | Create AI bias examples | 4 |
| T21.G7.02 | Create AI bias examples | 4 |

---

## Appendix B: Communication Templates

### Template 1: Teacher Announcement Email

**Subject:** Introducing Three Learning Tracks for Grades 7-8

Dear CreatiCode Teachers,

We're excited to introduce a new feature that will help you better serve all your students: **Three Learning Tracks**.

**📘 Standard Track** - Core skills for all students (no change to existing curriculum)
**⭐ Enrichment Track** - Optional challenges for students seeking deeper learning
**🏆 Competition Track** - Preparation for coding competitions (ACSL, Scratch Olympiad, etc.)

**What's changing?**
- We've refined 14 Grade 7-8 skills to ensure age-appropriateness
- 3 advanced skills now have easier alternatives for standard track
- Competition skills are clearly marked for students pursuing contests
- New filtering options in your teacher dashboard

**What's NOT changing?**
- The standard curriculum remains complete and rigorous
- All students can succeed with standard track alone
- Existing lesson plans still work

**Learn more:** [link to documentation]
**Questions?** Join our webinar on [date] or email support@creaticode.com

Happy coding!
The CreatiCode Team

---

### Template 2: Parent Communication

**Subject:** New Learning Options in CreatiCode

Dear Parents,

Your child's coding education just got even better! We've introduced three learning tracks to meet students where they are:

**📘 Core Skills** - Everything your child needs for excellent computer science education
**⭐ Challenge Skills** - Optional advanced activities for students who want more
**🏆 Competition Prep** - For students interested in coding competitions

**What this means for your child:**
- The core curriculum is complete and comprehensive
- Students can explore challenges at their own pace
- Competition opportunities are available for interested students

**Nothing is required beyond core skills.** Challenge and competition tracks are completely optional.

Questions? Visit [FAQ link] or contact your child's teacher.

Best regards,
CreatiCode

---

## Document Version

- **Version:** 1.0
- **Date:** 2025-11-17
- **Author:** CreatiCode Curriculum Team
- **Next Review:** After Week 12 (post-implementation feedback)

---

## Conclusion

This migration plan provides a clear path to implementing the three-track system while minimizing disruption and ensuring quality. By prioritizing the 3 HIGH-priority skills first and taking a phased approach, we can deliver immediate value while building toward the complete vision.

**Next Step:** Review and approve this plan, then begin Phase 1 (Data Model Updates).
