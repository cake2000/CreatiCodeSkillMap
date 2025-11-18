# CreatiCode Skill Track System: Standard, Enrichment & Competition

## Document Purpose

This document defines the three-track system for CreatiCode K-8 skills, with special focus on Grades 7-8 where skill complexity and student readiness vary significantly. The track system enables:

1. **Differentiated instruction** - Meet all students where they are
2. **Age-appropriate progression** - Ensure core curriculum is accessible to all 12-14 year olds
3. **Competition preparation** - Support students pursuing coding competitions
4. **Clear expectations** - Help teachers, students, and parents understand skill difficulty

---

## The Three Tracks

### 🎯 **Standard Track**

**Definition:** Core skills that ALL students should master as part of the K-8 computer science curriculum.

**Characteristics:**
- Age-appropriate for typical 12-14 year olds (Grades 7-8)
- Aligned with CSTA middle school standards
- Concrete, hands-on learning with real-world applications
- No prerequisites beyond earlier grade levels in CreatiCode
- Accessible terminology and concepts
- Visual and interactive learning activities

**When to Use:**
- Regular classroom instruction
- Required curriculum for all students
- Assessment and grading for core competencies
- Foundation for enrichment and competition work

**Examples (Grade 7-8):**
- T05.G7.04: Design a simulation for a real-world question
- T10.G7.01: Design and populate a table for real-world data
- T26.G7.04: Identify and correct data quality issues
- T07.G7.02: Use nested loops for 2D grids
- T26.G7.02: Conduct a data collection campaign

**Teacher Guidance:**
- These skills should be taught to the whole class
- All students are expected to demonstrate proficiency
- Use for formal assessment and grading
- Provide scaffolding for struggling students
- No student should be exempted from standard track

---

### ⭐ **Enrichment Track**

**Definition:** Advanced but age-appropriate stretch goals for high-achieving students, optional deep dives, or differentiation activities.

**Characteristics:**
- Challenging but within reach of motivated 12-14 year olds
- Requires abstract thinking or meta-cognitive skills
- May use more formal terminology (with support)
- Perfect for differentiation in mixed-ability classrooms
- Optional but valuable for deeper understanding
- Often involves analysis, optimization, or design thinking

**When to Use:**
- Differentiation for advanced students in regular classes
- Optional extension activities
- Challenge problems for students who finish early
- Bridge to competition preparation
- Honors or advanced sections

**Examples (Grade 7-8):**

**Algorithm Analysis (with simplification):**
- T02.G7.03: Analyze algorithm complexity → "Count and compare steps" (NOT Big-O)
- T01.G7.04: Analyze an algorithm for correctness on edge cases
- T01.G8.04: Refactor a complex algorithm for clarity or efficiency

**Conceptual Understanding:**
- T01.G8.02: Understand recursion conceptually → Visual only (fractals, nested patterns)
- T04.G7.04: Explain how pattern recognition leads to better algorithm design
- T02.G8.04: Compare deterministic and probabilistic algorithms

**Advanced Data & AI:**
- T25.G8.03: Use advanced data structures for algorithms
- T23.G8.04: Evaluate and mitigate bias in AI detection systems

**Revised Ethics (from too-advanced):**
- T27.G8.02: Explore whether two variables are related (REVISED from causal analysis)
- T35.G7.01: List pros and cons of a technology (REVISED from systemic impacts)
- T35.G8.02: Discuss whether rules are needed (REVISED from policy analysis)

**Teacher Guidance:**
- Introduce AFTER students master related standard skills
- Use for gifted/talented programs or honors tracks
- Excellent for project-based learning extensions
- Can be offered as optional challenges
- Appropriate for extra credit or bonus activities
- Provide scaffolding and support materials

**Scaffolding Requirements:**
- Heavy visual support for abstract concepts (recursion)
- Templates for formal methods (pseudocode)
- Concrete examples before abstraction
- Step-by-step guided practice

---

### 🏆 **Competition Track**

**Definition:** Skills specifically for competitive programming preparation or requiring AP/college-level knowledge.

**Characteristics:**
- Often beyond standard 8th grade curriculum
- Aligned with competition requirements (ACSL, Scratch Olympiad, etc.)
- Requires formal reasoning or advanced algorithms
- May need significant self-study or specialized instruction
- Optional - not required for regular curriculum completion

**When to Use:**
- Dedicated competition preparation programs
- Coding club or after-school enrichment
- Students targeting ACSL, Scratch Olympiad, NOC, Lanqiao
- Advanced CS electives
- Preparation for high school AP Computer Science

**Competition Mappings:**

**ACSL Junior Division (Grades 6-8):**
- Algorithm complexity and optimization
- Number systems and boolean logic
- Data structures (lists, arrays)
- Graph theory basics
- T10.G8.02: Implement sorting algorithm ⭐ COMPETITION

**Scratch Olympiad Junior (Grades 4-6) & Senior (Grades 7-8):**
- Advanced game mechanics
- Complex interactive stories
- Optimization challenges
- Visual algorithms

**NOC Junior (Grades 6-8) - Chinese Contest:**
- Algorithm design and optimization
- Creative applications of CS
- Advanced game development

**Lanqiao Scratch Senior (Grades 6-8):**
- Timed challenge problems
- Pattern recognition speed
- Efficient code patterns
- Algorithm optimization

**Examples:**
- **T10.G8.02: Implement a sorting algorithm (bubble sort or selection sort)**
  - **Track:** Competition
  - **Why:** AP CS A content (grade 11-12), requires formal reasoning
  - **Alternative for Standard:** "Use built-in sort blocks to organize data"
  - **Competitions:** ACSL Junior, Lanqiao Senior, NOC Junior

**Teacher Guidance:**
- Offer as specialized track, NOT required for all
- Best suited for dedicated competition prep sessions
- Students should have mastered related standard AND enrichment skills
- May require outside resources or specialized curriculum
- Consider forming competition teams or clubs
- Connect with competition organizers for practice problems

---

## Dependency Rules

### What Can Depend on What?

| If a skill is... | Can it depend on Standard? | Can it depend on Enrichment? | Can it depend on Competition? |
|------------------|---------------------------|------------------------------|-------------------------------|
| **Standard** | ✅ YES | ❌ NO | ❌ NO |
| **Enrichment** | ✅ YES | ✅ YES | ❌ NO |
| **Competition** | ✅ YES | ✅ YES | ✅ YES |

**Why These Rules?**

1. **Standard skills must be universally accessible**
   - Cannot require enrichment or competition prerequisites
   - Ensures all students can progress through core curriculum

2. **Enrichment can build on standard or other enrichment**
   - Natural progression from core to advanced
   - Allows for differentiated learning paths

3. **Competition skills can leverage anything**
   - Most advanced track with most prerequisites
   - Students pursuing competition prep have typically mastered standard curriculum

### Checking Dependencies

When reviewing skill dependencies:

```
IF skill is Standard:
  CHECK that ALL dependencies are also Standard
  FLAG any dependencies marked Enrichment or Competition

IF skill is Enrichment:
  ALLOW dependencies that are Standard or Enrichment
  FLAG any dependencies marked Competition

IF skill is Competition:
  ALLOW dependencies from any track
```

---

## Visual Identification System

### UI Badges and Markers

**Standard Track:**
- No special marker (default)
- Always visible in main skill tree
- Regular progression indicators

**Enrichment Track:**
- ⭐ Star icon or sparkle effect
- "Challenge" or "Stretch Goal" badge
- Optional branch markers in skill tree
- Highlighted border (gold/yellow)
- Tooltip: "Advanced optional skill for students seeking deeper understanding"

**Competition Track:**
- 🏆 Trophy icon
- "Competition Prep" badge
- Separate section or clearly marked branch
- Highlighted border (blue/purple)
- Tooltip: "For students preparing for coding competitions (ACSL, Scratch Olympiad)"

### Skill Tree Organization

```
Standard Path (Main trunk):
├── T01.G7.01: Common algorithm patterns
├── T01.G7.03: Pseudocode (with templates) ⚠️ Scaffolding needed
├── T10.G7.01: Design tables for real data
└── T10.G7.02: Basic list operations

Enrichment Branches (Optional):
├── ⭐ T01.G7.02: Why different algorithms are chosen
├── ⭐ T01.G7.04: Analyze edge cases
└── ⭐ T02.G7.03: Count and compare algorithm steps

Competition Branch (Advanced):
└── 🏆 T10.G8.02: Implement bubble or selection sort
    └── Alternative Standard: "Use sort blocks"
```

---

## How Teachers Should Use This System

### For Regular Classroom Teaching

**Focus: Standard Track**

1. **Plan curriculum around standard skills**
   - These are non-negotiable core competencies
   - All students should attempt and master these
   - Use for grading and assessment

2. **Use enrichment for differentiation**
   - Offer to students who finish early
   - Provide as extension activities
   - Create advanced sections or honors tracks
   - Optional homework or project enhancements

3. **Introduce competition skills selectively**
   - Only for dedicated competition prep
   - After-school clubs or electives
   - Not part of regular grading

### For Coding Clubs & Competition Prep

**Focus: Enrichment → Competition**

1. **Start with enrichment skills**
   - Build bridge from standard curriculum
   - Develop deeper analytical thinking
   - Practice with edge cases and optimization

2. **Progress to competition skills**
   - Align with specific competition requirements
   - Use past competition problems for practice
   - Form study groups or teams

3. **Supplement with competition-specific practice**
   - ACSL practice problems
   - Scratch Olympiad project examples
   - Timed challenges

### For Advanced/Gifted Programs

**Focus: All Standard + Most Enrichment**

1. **Complete all standard skills** (foundation)
2. **Integrate enrichment throughout** (not just at end)
3. **Introduce competition concepts** (exposure, not mastery)
4. **Emphasize depth over speed**

---

## Implementation in CreatiCode Platform

### Skill Metadata

Add `difficulty_track` field to each skill:

```json
{
  "id": "T10.G8.02",
  "title": "Implement a sorting algorithm",
  "difficulty_track": "competition",
  "track_metadata": {
    "reason": "AP CS A content, requires formal reasoning",
    "competitions": ["ACSL Junior", "Lanqiao Senior"],
    "alternative_standard": "Use built-in sort blocks",
    "prerequisites_met": true
  }
}
```

### Student Progress Tracking

Track separately:
- **Standard Mastery:** Required for grade-level completion
- **Enrichment Progress:** Optional achievements
- **Competition Skills:** Special achievements/badges

### Parent Communication

**Report Card Format:**

```
Grade 7 Computer Science

Standard Skills: 45/48 (94%) ✅
  - Excellent progress in core curriculum

Enrichment Challenges: 8/15 (53%) ⭐
  - [Student Name] is excelling in advanced challenges
  - Recommended for Honors track in Grade 8

Competition Skills: 2/5 (40%) 🏆
  - [Student Name] is exploring competition-level content
  - Consider coding competition participation
```

---

## Specific Recommendations for Flagged Skills

### HIGH PRIORITY: Move or Drastically Simplify

#### 1. T10.G8.02 - Sorting Algorithm Implementation

**Current:** Implement a sorting algorithm (bubble sort or selection sort)

**Issue:** AP Computer Science A content (typically grade 11-12)

**Track Assignment:** 🏆 Competition

**Actions:**

**For Standard Curriculum:**
- **Replace with:** "Use built-in sort blocks to organize data by criteria"
- **Focus:** Using sort as a tool, understanding what sorting does
- **Description:** "Students use CreatiCode's sort blocks to organize lists and tables by different attributes (alphabetical, numerical, by property). They understand WHAT sorting accomplishes without implementing the algorithm."

**For Competition Track:**
- **Keep original:** Full implementation of bubble or selection sort
- **Target:** ACSL Junior, Lanqiao Senior, NOC Junior
- **Prerequisites:** All standard list operations, nested loops, swap logic
- **Assessment:** Can implement, trace, and debug sorting algorithm

---

#### 2. T27.G8.02 - Causal Relationships

**Current:** Analyze two variables for potential causal relationships

**Issue:** Causal inference is college-level statistics

**Track Assignment:** ⭐ Enrichment (with major simplification)

**Actions:**

**SIMPLIFY to:**
- **New Title:** "Explore whether two variables are related"
- **New Description:** "Students explore whether two variables seem to be related (when one is high, is the other high too?) and discuss possible reasons. They learn that sometimes both variables are affected by a third factor (e.g., ice cream sales and drowning both increase in summer because it's hot). No formal causal analysis required."

**What Students DO:**
- Plot two variables on a graph
- Observe if they tend to move together
- Discuss: "Does one CAUSE the other, or could something else cause both?"
- Give concrete examples (correlation without causation)

**What Students DON'T Do:**
- Formal hypothesis testing
- Control for confounding variables (beyond discussion)
- Experimental design for proving causation
- Statistical significance testing

---

#### 3. T35.G7.01 - Systemic Impacts

**Current:** Analyze unintended systemic impacts of a technology

**Issue:** Systems thinking and second-order effects too advanced for 7th grade

**Track Assignment:** ⭐ Enrichment (with major simplification)

**Actions:**

**SIMPLIFY to:**
- **New Title:** "Identify pros and cons of a technology"
- **New Description:** "Students identify and list 3-5 positive effects and 3-5 negative effects of a technology (e.g., smartphones, social media, AI assistants). They discuss why each effect matters and who is most affected."

**What Students DO:**
- List good things and bad things about a technology
- Give examples of who benefits and who is harmed
- Discuss trade-offs in accessible terms

**What Students DON'T Do:**
- Analyze ripple effects or second-order consequences
- Map system-level interactions
- Predict long-term societal transformations
- Formal systems analysis

**Example Activity:**
```
Technology: Smartphones

Good things:
- Stay connected with family
- Access information quickly
- Emergency calls
- Educational apps
- Camera for memories

Bad things:
- Can be addictive
- Screen time before bed affects sleep
- Less face-to-face conversation
- Expensive
- Privacy concerns with apps

Discussion: Are smartphones worth it? How can we get the good without the bad?
```

---

### MEDIUM PRIORITY: Terminology Fixes

#### T28.G7.02 & T07.G8.01 - "Monte Carlo" Simulations

**Issue:** Term "Monte Carlo" is intimidating and unnecessary jargon

**Track:** Standard (content is perfect, just rename)

**Simple Fix:**
- **OLD:** "Implement a Monte Carlo simulation to estimate a probability"
- **NEW:** "Run many trials to estimate a probability"
- **OR:** "Use repeated simulation to find probability"

**Content stays identical** - just more accessible language.

---

#### T27.G7.04 - "Distributions"

**Issue:** "Distributions" suggests formal statistics (skew, variance, standard deviation)

**Track:** Standard (with simplification)

**Simple Fix:**
- **OLD:** "Compare distributions of data"
- **NEW:** "Compare datasets using averages and ranges"
- **Description:** "Students compare two datasets by calculating their means and ranges, identifying which tends higher or has more spread."

**Avoid:** Shape of distribution, skew, variance, standard deviation
**Use:** Average (mean), range (min to max), spread, which is higher/lower

---

#### T01.G7.03 & T02.G8.01 - "Pseudocode"

**Issue:** Term "pseudocode" can be intimidating

**Track:** Standard (with scaffolding)

**Approach:**
- Keep the term "pseudocode" (it's valuable)
- Provide HEAVY scaffolding:
  - Fill-in-the-blank templates
  - Sentence starters
  - Scratch-to-text translation guides
- Alternative phrasing: "Plan an algorithm using words and steps"

**Template Example:**
```
Algorithm to [describe goal]:

Step 1: Start with [initial state]
Step 2: Repeat [number] times:
  - Do [action]
  - If [condition], then [action]
Step 3: Stop when [end condition]
```

---

### LOW PRIORITY: Add Scaffolding

#### T01.G8.02 - Recursion

**Current Status:** Borderline but acceptable

**Track:** ⭐ Enrichment

**Implementation Requirements:**

**DO:**
- Show recursive patterns visually (fractals, Koch snowflake)
- Use physical analogs (Russian dolls, mirrors reflecting)
- Demonstrate with family trees or folder structures
- "An algorithm that uses itself as a step"

**DON'T:**
- Require students to write recursive functions in code
- Expect understanding of call stack or base cases
- Test on recursive algorithm implementation
- Use formal notation

**Assessment:**
- Can recognize recursive patterns in nature/art
- Can describe what recursion means conceptually
- Can identify base case and recursive case in simple example
- NOT: Can implement recursive function

---

#### AI Bias Skills - Various

**Skills:**
- T28.G8.03: Analyze bias in AI models
- T21.G7.02: Examine bias in AI-generated images
- T23.G8.04: Evaluate bias in AI detection systems

**Track:** Standard (critically important for digital citizenship)

**Scaffolding Required:**

**DO:**
- Use concrete examples (facial recognition, hiring AI, image generation)
- Show real cases of bias (news articles, demonstrations)
- Focus on impacts and recognition
- Test with diverse inputs

**DON'T:**
- Require understanding of ML model architecture
- Expect knowledge of training algorithms
- Test on technical details of bias mitigation
- Use formal ML terminology

**Example Activity:**
```
Facial Recognition Bias Lab:

1. Test facial recognition AI with diverse photos
2. Record which faces are recognized accurately
3. Observe: Does it work better for some groups?
4. Discuss: Why might this happen? (training data)
5. Consider: Who is harmed when AI doesn't work for them?
```

---

## Quality Checklist for New Skills

When adding or revising Grade 7-8 skills, check:

### Standard Track Requirements

- [ ] No college-level content (if in AP CS A/B or college intro CS, it's too advanced)
- [ ] Terminology at 6th-8th grade reading level
- [ ] Concrete examples provided (not just abstract concepts)
- [ ] Visual or hands-on component available
- [ ] Can be learned with age-appropriate scaffolding
- [ ] Aligns with CSTA middle school standards
- [ ] No formal proofs or mathematical notation beyond 8th grade algebra
- [ ] "Analyze" means concrete exploration, not formal analysis

### Enrichment Track Requirements

- [ ] Challenging but within reach of motivated 12-14 year olds
- [ ] Clear educational value (not just "hard for hard's sake")
- [ ] Builds meaningfully on standard skills
- [ ] Appropriate scaffolding can be provided
- [ ] Useful for differentiation or deeper understanding

### Competition Track Requirements

- [ ] Aligned with specific competition(s)
- [ ] Clear which competitions require this skill
- [ ] Prerequisites are achievable by target grade
- [ ] Alternative standard-track version exists or skill is optional
- [ ] Won't disadvantage students who don't pursue competitions

---

## FAQs for Teachers

### Q: Can I skip standard skills for my advanced class?

**A: No.** Standard skills are foundational. Even advanced students should demonstrate mastery of all standard skills. You can move through them faster and add enrichment, but don't skip them.

### Q: Should I teach enrichment skills to everyone?

**A: It depends.** If you have time and students are ready, enrichment skills are valuable for all. However, if you must choose, prioritize mastery of standard skills over breadth of enrichment coverage.

### Q: My student wants to do ACSL. What should they study?

**A: Three-phase approach:**
1. **Master ALL standard skills** in relevant topics (T01-T02, T07-T11, T25-T27)
2. **Complete enrichment skills** in algorithms and data structures
3. **Study competition skills** + use ACSL practice problems
4. Join a competition prep program or coding club

### Q: Can a student skip straight to competition track?

**A: Not recommended.** Competition skills assume mastery of standard curriculum. Students who skip ahead often have gaps that limit their competition performance. Build solid foundation first.

### Q: How do I grade enrichment and competition work?

**Grading Recommendations:**
- **Standard skills:** Traditional grading, required for course completion
- **Enrichment skills:** Extra credit, honors distinction, or separate "advanced mastery" category
- **Competition skills:** Not part of regular grade; track as special achievements or club participation

### Q: Is recursion (T01.G8.02) really appropriate for 8th grade?

**A: Yes, if taught conceptually.** The key is keeping it visual and conceptual. Show fractals, nested dolls, and recursive patterns. Do NOT require students to implement recursive functions in code. That's the competition-level version.

### Q: What if my 6th grader is ready for 8th grade competition skills?

**A: Great!** Tracks are about skill readiness, not age. If a student has mastered prerequisites and is ready for competition content, they can pursue it. Just ensure they're genuinely ready and not skipping foundational concepts.

---

## Conclusion

The three-track system enables CreatiCode to serve all students:

- **Standard Track:** Ensures every student gets age-appropriate, high-quality CS education
- **Enrichment Track:** Provides challenges for advanced students and differentiation options
- **Competition Track:** Supports students pursuing competitive programming

By clearly categorizing skills, we maintain "IXL for coding" quality while supporting diverse learner needs from struggling students to competition champions.

**Core Principle:** *All students deserve excellent CS education. Advanced students deserve additional challenges. Competition students deserve specialized preparation. No student should be left behind OR held back.*

---

## Document Version

- **Version:** 1.0
- **Date:** 2025-11-17
- **Next Review:** After implementation feedback from pilot teachers
- **Maintained by:** CreatiCode Curriculum Team

---

## Appendix: Full List of Track Assignments (Grades 7-8 Flagged Skills)

### Competition Track
1. T10.G8.02 - Implement sorting algorithm 🏆

### Enrichment Track (Advanced but Appropriate)
1. T01.G8.02 - Recursion (conceptual only) ⭐
2. T02.G7.03 - Algorithm complexity (count steps, not Big-O) ⭐
3. T02.G8.04 - Compare deterministic and probabilistic algorithms ⭐
4. T01.G7.02 - Why different algorithms are chosen ⭐
5. T01.G7.04 - Analyze edge cases ⭐
6. T02.G8.03 - Analyze algorithm representation ⭐
7. T04.G7.04 - Pattern recognition → algorithm design ⭐
8. T01.G8.04 - Refactor algorithms ⭐
9. T25.G8.03 - Advanced data structures ⭐

### Enrichment Track (Revised from Too Advanced)
1. T27.G8.02 - Explore variable relationships (REVISED from causal) ⭐
2. T35.G7.01 - List pros/cons (REVISED from systemic impacts) ⭐
3. T35.G8.02 - Discuss rules needed (REVISED from policy analysis) ⭐
4. T23.G8.04 - Evaluate AI bias (with scaffolding) ⭐

### Standard Track with Terminology Fixes
1. T28.G7.02 - Run many trials (was "Monte Carlo")
2. T07.G8.01 - Repeated simulations (was "Monte Carlo")
3. T27.G7.04 - Compare averages/ranges (was "distributions")
4. T01.G7.03 - Pseudocode (with templates)
5. T02.G8.01 - Pseudocode for algorithms (with templates)

### Standard Track with Scaffolding (AI Ethics)
1. T28.G8.03 - Analyze AI bias (concrete examples)
2. T21.G7.02 - Examine bias in AI images (concrete examples)
3. T33.G7.03 - Evaluate algorithmic bias (concrete examples)

### Exemplary Standard Track (No Changes Needed)
1. T05.G7.04 - Design simulation for real question
2. T10.G7.01 - Design tables for real data
3. T26.G7.04 - Identify and correct data quality issues
4. T07.G7.02 - Nested loops for 2D grids
5. T26.G7.02 - Conduct data collection campaign
6. T26.G7.01 - Formulate testable data question
7. T28.G7.01 - Conduct experiment with hypothesis
8. T04.G8.02 - Design modular custom blocks
9. T26.G8.02 - Complete data investigation

**Total Categorized:** 31 flagged skills
**Estimated Remaining Standard Track:** ~270 skills (already appropriate)
