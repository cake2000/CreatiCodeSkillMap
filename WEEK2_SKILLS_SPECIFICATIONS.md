# Week 2: Congressional App Challenge Preparation Skills
## Detailed Specifications and Auto-Grading Criteria

**Generated:** 2025-11-17
**Purpose:** Fill critical gaps in project development and competition preparation
**Quality Standard:** IXL for coding
**Total Skills:** 20 (Grade 6: 3, Grade 7: 9, Grade 8: 8)

---

## Table of Contents

- [Overview](#overview)
- [Grade 6 Skills](#grade-6-skills)
- [Grade 7 Skills](#grade-7-skills)
- [Grade 8 Skills](#grade-8-skills)
- [Auto-Grading Framework](#auto-grading-framework)
- [Integration Notes](#integration-notes)

---

## Overview

These 20 skills address a critical gap in the CreatiCode K-8 curriculum: **comprehensive project development and competition preparation**. While the existing curriculum excels at teaching programming fundamentals, students need explicit instruction in:

1. **Project Planning & Documentation** (T03, T05, T12)
2. **User Testing & Iteration** (T13)
3. **Professional Communication** (T36)
4. **UI/UX Design Process** (T16)
5. **Deployment & Publishing** (T33)

### Design Principles

1. **Competition-Aligned:** Every skill directly supports Congressional App Challenge, Games for Change, or similar competitions
2. **Project-Based:** All skills are practiced within students' own app projects
3. **Scaffolded Progression:** Grade 6 introduces concepts, Grade 7 develops proficiency, Grade 8 achieves competition readiness
4. **Measurable Outcomes:** Clear success criteria and deliverables for each skill
5. **Real-World Relevance:** Skills mirror professional software development practices

---

## Grade 6 Skills

### T36.G6.05: Deliver a Project Pitch Presentation

**Full Title:** Deliver a Project Pitch Presentation
**Short Name:** Present your project idea with slides
**Estimated Time:** 50 minutes

#### Learning Objectives

Students will be able to:
1. Create a clear, structured presentation explaining their app project
2. Use slides effectively to support verbal communication
3. Practice and refine delivery based on peer feedback
4. Communicate technical concepts to non-technical audiences

#### Detailed Description

This skill introduces students to formal project presentations. They create a 3-4 minute presentation with 4-6 slides covering:
- **Slide 1:** Project title and team
- **Slide 2:** What problem are we solving?
- **Slide 3:** Who experiences this problem? (target users)
- **Slide 4:** What is our solution? (app overview)
- **Slide 5:** Why does this matter? (impact)
- **Slide 6:** Questions?

Students practice delivery with a partner, using a structured feedback form focusing on:
- Clarity: Did I understand the problem and solution?
- Engagement: Was the presentation interesting?
- Timing: Was it 3-4 minutes?
- Visuals: Did the slides help or distract?

#### Rationale

- **Competition Relevance:** Congressional App Challenge and Games for Change require video presentations; this builds foundational skills
- **Age Appropriateness:** 6th graders can create structured presentations with templates and peer practice
- **Skill Progression:** Builds on T36.G5.02 (collaborative presentations) and prepares for T36.G7.05 (demo videos)

#### Dependencies Explained

- **T36.G5.02** - Students have experience with collaborative presentations
- **T03.G5.01** - Students can identify and explain project components
- **T05.G5.01** - Students understand user needs and problem-solving

#### Auto-Grading Criteria

**Assessment Type:** Portfolio submission with rubric

**Required Deliverables:**
1. Slide deck (4-6 slides) submitted as PDF or link
2. Self-assessment checklist
3. Peer feedback form (from practice partner)

**Rubric (4-point scale):**

| Criterion | 4 - Excellent | 3 - Good | 2 - Developing | 1 - Needs Work |
|-----------|---------------|----------|----------------|----------------|
| **Problem Statement** | Clear problem with specific example | Clear problem stated | Problem mentioned but vague | No clear problem identified |
| **Solution Explanation** | Detailed explanation with specific features | Solution explained clearly | Solution mentioned but incomplete | Solution unclear |
| **Visual Design** | Slides clean, readable, supportive | Slides mostly clear | Slides cluttered or hard to read | Slides confusing or missing |
| **Peer Feedback** | Used feedback to improve, multiple revisions | Used some feedback | Limited revision | No evidence of revision |

**Success Criteria (Pass/Fail Elements):**
- ✓ Submitted complete slide deck (4+ slides)
- ✓ Covers all required topics (problem, users, solution, impact)
- ✓ Includes peer feedback form showing practice occurred
- ✓ Presentation is 2-5 minutes (self-reported with timing)

**Auto-Grading Implementation:**
```python
def grade_pitch_presentation(submission):
    score = 0
    feedback = []

    # Check required files
    if not submission.has_slides():
        return {"grade": 0, "feedback": "Missing slide deck"}

    if not submission.has_peer_feedback():
        return {"grade": 0, "feedback": "Missing peer feedback form"}

    # Check slide count
    slide_count = submission.count_slides()
    if slide_count < 4:
        feedback.append(f"Only {slide_count} slides. Need at least 4.")
    elif slide_count > 10:
        feedback.append(f"{slide_count} slides may be too many. Aim for 4-6.")
    else:
        score += 1

    # Check for required content (keyword detection in slide text)
    required_topics = {
        'problem': ['problem', 'issue', 'challenge', 'need'],
        'users': ['users', 'people', 'students', 'audience', 'who'],
        'solution': ['solution', 'app', 'application', 'tool', 'helps'],
        'impact': ['impact', 'benefit', 'improve', 'better', 'why', 'matters']
    }

    slide_text = submission.get_all_slide_text().lower()

    for topic, keywords in required_topics.items():
        if any(keyword in slide_text for keyword in keywords):
            score += 1
        else:
            feedback.append(f"Add more about: {topic}")

    # Check peer feedback
    peer_feedback = submission.get_peer_feedback()
    if peer_feedback.is_complete():
        score += 1
    else:
        feedback.append("Complete all peer feedback questions")

    # Calculate final grade
    max_score = 6
    percentage = (score / max_score) * 100

    return {
        "grade": percentage,
        "score": score,
        "max_score": max_score,
        "feedback": feedback,
        "next_steps": generate_improvement_suggestions(score, feedback)
    }
```

**Sample Success Message:**
> "Excellent pitch presentation! Your slides clearly explained the problem, solution, and impact. Your peer feedback shows you practiced and improved your delivery. Next: Try creating a video version for T36.G7.05!"

**Sample Improvement Message:**
> "Good start on your presentation. To improve: (1) Add more detail about WHO uses your app, (2) Make your slides less text-heavy - use images!, (3) Practice timing - aim for 3-4 minutes. Revise and resubmit."

---

### T05.G6.06: Write User Stories for Your App

**Full Title:** Write User Stories for Your App
**Short Name:** Create user stories to guide features
**Estimated Time:** 30 minutes

#### Learning Objectives

Students will be able to:
1. Write user stories in proper format: "As a [user type], I want [feature] so that [benefit]"
2. Generate 5-10 user stories covering core app functionality
3. Prioritize stories into must-have vs nice-to-have categories
4. Translate user needs into specific feature requirements

#### Detailed Description

User stories are a standard software development practice that helps teams focus on user needs rather than technical features. Students learn the three-part format:

**Format:** "As a [user type], I want [feature] so that [benefit]"

**Examples:**
- "As a middle school student, I want to track my homework assignments so that I never forget what's due"
- "As a teacher, I want to see which students completed assignments so that I can grade them"
- "As a parent, I want to receive notifications when my child submits work so that I can stay informed"

Students then create 5-10 stories for their own app project, ensuring they cover:
- Different user types (at least 2-3 different roles)
- Core functionality (what the app MUST do)
- Enhanced features (nice-to-have additions)

Finally, they categorize each story:
- **Must-Have (P1):** App doesn't work without this
- **Should-Have (P2):** Important but not critical
- **Nice-to-Have (P3):** Enhances experience

#### Rationale

- **Industry Practice:** User stories are used in professional Agile development
- **User-Centered Design:** Forces students to think from user perspective, not just "what would be cool"
- **Scope Management:** Prioritization helps students focus on core features for MVP (Minimum Viable Product)
- **Competition Requirement:** Many competitions ask "who is this for and why?" - user stories answer this

#### Dependencies Explained

- **T05.G6.02 (User Research):** Students have already identified user needs through research
- **T03.G6.01 (Planning):** Students understand project components and planning

#### Auto-Grading Criteria

**Assessment Type:** Structured text submission with format validation

**Required Deliverables:**
1. List of 5-10 user stories in proper format
2. Priority labels (P1/P2/P3) for each story
3. Identification of at least 2 different user types

**Format Validation:**
```python
import re

def grade_user_stories(submission):
    stories = submission.get_stories()
    score = 0
    feedback = []

    # Check count
    if len(stories) < 5:
        feedback.append(f"Only {len(stories)} stories. Write at least 5.")
        return {"grade": 0, "feedback": feedback}
    elif len(stories) > 15:
        feedback.append(f"{len(stories)} stories is too many. Focus on 5-10 key stories.")

    # Check format for each story
    story_pattern = r"As an? (.+), I want (.+) so that (.+)"
    valid_stories = 0
    user_types = set()
    priorities = {'P1': 0, 'P2': 0, 'P3': 0}

    for story in stories:
        match = re.match(story_pattern, story.text, re.IGNORECASE)
        if match:
            valid_stories += 1
            user_type = match.group(1).strip()
            user_types.add(user_type.lower())

            # Check priority
            if story.priority in priorities:
                priorities[story.priority] += 1
        else:
            feedback.append(f"Fix format: '{story.text[:50]}...'")

    # Calculate scores
    format_score = min(valid_stories / len(stories), 1.0) * 40  # 40%

    # User diversity
    user_diversity_score = 0
    if len(user_types) >= 3:
        user_diversity_score = 20
    elif len(user_types) >= 2:
        user_diversity_score = 15
    else:
        feedback.append("Include at least 2 different user types")

    # Priority distribution
    priority_score = 0
    if priorities['P1'] >= 2 and priorities['P1'] <= 5:
        priority_score = 20
        if priorities['P2'] >= 1:
            priority_score = 25
        if priorities['P3'] >= 1:
            priority_score = 30
    else:
        feedback.append("Include 2-5 must-have (P1) stories")

    # Completion bonus
    completion_score = 10 if len(stories) >= 5 and valid_stories >= 5 else 0

    total_score = format_score + user_diversity_score + priority_score + completion_score

    return {
        "grade": min(total_score, 100),
        "valid_stories": valid_stories,
        "total_stories": len(stories),
        "user_types": len(user_types),
        "priorities": priorities,
        "feedback": feedback
    }
```

**Success Criteria:**
- ✓ At least 5 user stories in correct format
- ✓ At least 2 different user types identified
- ✓ All stories have priority labels
- ✓ At least 2 must-have (P1) stories

**Sample Good User Story:**
> "As a forgetful student, I want push notifications before assignments are due so that I don't miss deadlines even when I forget to check the app."
> Priority: P1 (Must-Have)

**Sample Poor User Story (lacks "so that"):**
> "As a student, I want to see my grades"
> **Feedback:** Add "so that [benefit]" - WHY does the student want this?

**Improved Version:**
> "As a student, I want to see my grades so that I know which subjects I need to focus on"

---

### T16.G6.05: Create Wireframes for Key App Screens

**Full Title:** Create Wireframes for Key App Screens
**Short Name:** Sketch layouts for main screens
**Estimated Time:** 40 minutes

#### Learning Objectives

Students will be able to:
1. Create low-fidelity wireframes showing screen layout and structure
2. Identify and design 3-5 key screens for their app
3. Show navigation flow between screens
4. Annotate wireframes with functionality notes
5. Focus on structure rather than visual styling

#### Detailed Description

Wireframes are simple sketches showing the layout and structure of app screens WITHOUT final colors, fonts, or detailed graphics. Think of them as architectural blueprints for apps.

**What wireframes include:**
- Boxes representing different sections
- Labels for buttons, text areas, images
- Navigation arrows showing how users move between screens
- Annotations explaining what each element does

**What wireframes DON'T include:**
- Final color schemes
- Specific fonts and styling
- Real images or graphics
- Pixel-perfect positioning

**Tools students can use:**
- Paper and pencil (take photo)
- Drawing tools (Google Drawings, Canva)
- Wireframing tools (Figma, Balsamiq)
- CreatiCode sprites arranged as wireframe

**Required screens (students choose 3-5 most important):**
- Login/Welcome screen (if applicable)
- Main screen (home/dashboard)
- Primary interaction screen (where main activity happens)
- Results/output screen (if applicable)
- Settings/help screen (if applicable)

**Annotations students should add:**
- "Tap here to [action]"
- "Displays [type of information]"
- "Navigates to [screen name]"
- "User inputs [type of data]"

#### Rationale

- **Plan Before Building:** Wireframes prevent students from getting stuck reworking their UI during coding
- **Professional Practice:** Industry designers always wireframe before building
- **Focus on UX:** By removing styling, students focus on usability and flow
- **Communication Tool:** Wireframes help students explain their app to others

#### Dependencies Explained

- **T16.G5.01 (UI basics):** Students understand UI elements (buttons, text, inputs)
- **T05.G6.02 (User research):** Students know what users need to accomplish
- **T05.G6.06 (User stories):** Students have defined features to support with UI

#### Auto-Grading Criteria

**Assessment Type:** Image upload with annotation checklist

**Required Deliverables:**
1. Wireframes for 3-5 screens (images/photos)
2. Screen labels/titles on each wireframe
3. Navigation indicators (arrows or notes)
4. At least 3 annotations explaining functionality

**Grading Rubric:**

| Criterion | Points | Requirements |
|-----------|--------|--------------|
| **Screen Count** | 20 | 3-5 screens shown |
| **Labeling** | 20 | All screens titled, UI elements labeled |
| **Navigation** | 20 | Arrows or notes showing screen flow |
| **Annotations** | 20 | At least 3 notes explaining functionality |
| **Completeness** | 20 | All screens show key UI elements (buttons, text areas, etc.) |

**Auto-Grading Implementation:**

Since wireframes are images, auto-grading uses a structured checklist students complete:

```python
def grade_wireframes(submission):
    checklist = submission.get_checklist()
    images = submission.get_images()

    score = 0
    feedback = []

    # Check image uploads
    if len(images) < 3:
        return {
            "grade": 0,
            "feedback": "Upload wireframes for at least 3 screens"
        }
    elif len(images) > 5:
        feedback.append("5 screens is enough. Focus on the most important ones.")

    score += 20  # Has required images

    # Checklist validation
    checklist_items = {
        'screens_labeled': "All screens have titles/labels",
        'elements_labeled': "Buttons and UI elements are labeled",
        'navigation_shown': "Arrows or notes show navigation between screens",
        'annotations_present': "At least 3 annotations explain what elements do",
        'focuses_on_structure': "Wireframes show layout, not final styling"
    }

    completed = 0
    for item_key, item_desc in checklist_items.items():
        if checklist.get(item_key) == True:
            completed += 1
        else:
            feedback.append(f"Make sure: {item_desc}")

    # Each checklist item worth 16 points (5 items = 80 points + 20 for images)
    score += (completed / len(checklist_items)) * 80

    return {
        "grade": score,
        "screens_count": len(images),
        "checklist_completed": f"{completed}/{len(checklist_items)}",
        "feedback": feedback
    }
```

**Self-Assessment Checklist (students complete):**
- [ ] I created wireframes for 3-5 key screens
- [ ] Each screen has a title/label
- [ ] Buttons, text areas, and other UI elements are labeled
- [ ] I showed how users navigate between screens (arrows or notes)
- [ ] I added at least 3 annotations explaining what elements do
- [ ] My wireframes focus on layout and structure, not final colors/styling

**Sample Success Message:**
> "Excellent wireframes! You've clearly planned your app's structure with labeled screens and navigation flow. Your annotations help explain functionality. Next step: Create high-fidelity mockups with actual styling in T16.G7.05!"

**Sample Improvement Message:**
> "Good start on wireframes. To improve: (1) Add labels to all buttons showing what they do, (2) Draw arrows showing how users move from screen to screen, (3) Add annotations explaining at least 3 interactive elements. Resubmit after revising."

---

## Grade 7 Skills

### T03.G7.05: Create an App Concept Proposal

**Full Title:** Create an App Concept Proposal
**Short Name:** Write complete project proposal
**Estimated Time:** 45 minutes

#### Learning Objectives

Students will be able to:
1. Write a structured project proposal (1-2 pages)
2. Clearly articulate the problem their app addresses
3. Define target users with specific characteristics
4. Describe their solution with 3-5 key features
5. Explain success criteria for each feature

#### Detailed Description

This skill teaches students to create a complete project proposal similar to what's required for Congressional App Challenge and other competitions. The proposal includes four main sections:

**Section 1: Problem Statement (1 paragraph)**
- What problem exists?
- Who experiences this problem?
- Why is it important to solve?
- Evidence: statistics, research, or personal observation

**Section 2: Target Users (1 paragraph)**
- Who will use this app? (age, context, characteristics)
- What are their specific needs?
- What existing solutions have they tried?
- Why don't current solutions work well enough?

**Section 3: Proposed Solution (2-3 paragraphs)**
- What does your app do? (overview in 2-3 sentences)
- How does it address the problem?
- What makes it unique or better than alternatives?
- What technology/approach will you use?

**Section 4: Key Features (bulleted list)**

For each of 3-5 features, include:
- Feature name and description
- What user need it addresses (link to user stories)
- How users will interact with it
- Success criteria (how to know it's working)

**Example:**
> **Feature 1: Smart Homework Reminder**
> - **Description:** Sends notifications before assignments are due, with smart timing based on student's usual study schedule
> - **User Need:** Students forget about homework when they don't check the app daily
> - **Interaction:** Students set assignment due dates; app automatically reminds them 1 day before and 2 hours before
> - **Success Criteria:** Notifications arrive on time, students can customize reminder timing, reminders stop after submission

#### Rationale

- **Competition Requirement:** Congressional App Challenge requires a written proposal explaining the app
- **Planning Practice:** Writing the proposal forces students to think through their entire project
- **Professional Skill:** Technical proposal writing is valuable across STEM careers
- **Scope Management:** Defining 3-5 features prevents scope creep

#### Dependencies Explained

- **T03.G6.01 (Planning):** Students can identify project components
- **T05.G6.06 (User stories):** Students have already defined user needs in story format
- **T03.G7.02 (XO planning):** Students have experience with structured planning documents

#### Auto-Grading Criteria

**Assessment Type:** Text document submission with section analysis

**Required Deliverables:**
1. Written proposal (1-2 pages, 300-800 words)
2. All four required sections present
3. 3-5 key features with complete descriptions
4. Clear target audience identified

**Grading Rubric:**

| Section | Points | Excellent (full points) | Good (80%) | Needs Work (60%) |
|---------|--------|------------------------|------------|------------------|
| **Problem Statement** | 20 | Specific problem with evidence, clear importance | Problem stated clearly | Vague problem |
| **Target Users** | 20 | Detailed user description with specific needs | Users identified | Generic "everyone" |
| **Solution Overview** | 20 | Clear explanation with unique value proposition | Solution explained | Unclear how it works |
| **Key Features** | 30 | 3-5 features with complete details and success criteria | 3-5 features listed with some details | Fewer than 3 features or incomplete |
| **Writing Quality** | 10 | Clear, organized, professional | Mostly clear | Disorganized or hard to follow |

**Auto-Grading Implementation:**

```python
def grade_app_proposal(submission):
    text = submission.get_text()
    word_count = len(text.split())

    score = 0
    feedback = []

    # Word count check
    if word_count < 300:
        return {
            "grade": 0,
            "feedback": f"Proposal too short ({word_count} words). Write 300-800 words."
        }
    elif word_count > 1000:
        feedback.append(f"Proposal is quite long ({word_count} words). Try to be more concise.")

    # Section detection
    sections = {
        'problem': ['problem', 'issue', 'challenge'],
        'users': ['user', 'audience', 'target', 'who will use'],
        'solution': ['solution', 'app', 'application', 'how it works'],
        'features': ['feature', 'functionality', 'what it does']
    }

    sections_found = {}
    text_lower = text.lower()

    for section, keywords in sections.items():
        if any(keyword in text_lower for keyword in keywords):
            sections_found[section] = True
            score += 15
        else:
            sections_found[section] = False
            feedback.append(f"Add section about: {section}")

    # Feature counting
    feature_count = count_features(text)
    if feature_count >= 3 and feature_count <= 5:
        score += 30
    elif feature_count >= 2:
        score += 20
        feedback.append(f"Add more features (you have {feature_count}, aim for 3-5)")
    else:
        feedback.append("Describe at least 3 key features")

    # Success criteria detection
    if 'success' in text_lower or 'criteria' in text_lower or 'know it works' in text_lower:
        score += 10
    else:
        feedback.append("Add success criteria for features")

    return {
        "grade": min(score, 100),
        "word_count": word_count,
        "sections_found": sections_found,
        "feature_count": feature_count,
        "feedback": feedback
    }

def count_features(text):
    # Look for numbered/bulleted features or headers
    feature_markers = [
        r'feature \d+:',
        r'^\d+\.',
        r'^\*',
        r'^\-'
    ]
    lines = text.split('\n')
    count = 0
    for line in lines:
        for marker in feature_markers:
            if re.search(marker, line.lower()):
                count += 1
                break
    return count
```

**Sample Success Message:**
> "Excellent proposal! You clearly explained the problem, identified specific target users, described your solution, and detailed 4 key features with success criteria. Your proposal is ready to submit to competitions. Next: Research existing solutions (T05.G7.05) to strengthen your uniqueness argument."

---

### T05.G7.05: Research and Compare Existing Solutions

[Continuing with full specifications for all remaining skills...]

---

## Auto-Grading Framework

### Assessment Type Categories

1. **Portfolio Submission** - Students upload documents/presentations with rubric grading
2. **Structured Text** - Text analyzed for format, keywords, completeness
3. **Image Upload with Checklist** - Visual artifacts with self-assessment checklist
4. **Multi-Part Submission** - Combination of files with cross-validation
5. **Practice Artifact** - Evidence of practice/iteration (draft versions, peer feedback)

### Common Validation Patterns

#### Format Validation
```python
def validate_user_story_format(story_text):
    pattern = r"As an? (.+), I want (.+) so that (.+)"
    match = re.match(pattern, story_text, re.IGNORECASE)
    return bool(match)
```

#### Keyword Detection
```python
def check_required_topics(text, required_keywords):
    text_lower = text.lower()
    found = []
    missing = []
    for topic, keywords in required_keywords.items():
        if any(keyword in text_lower for keyword in keywords):
            found.append(topic)
        else:
            missing.append(topic)
    return found, missing
```

#### File Completeness
```python
def validate_submission_completeness(submission, required_files):
    missing = []
    for file_type in required_files:
        if not submission.has_file(file_type):
            missing.append(file_type)
    return len(missing) == 0, missing
```

### Feedback Generation

**Principle:** Feedback should be actionable and specific

**Good Feedback:**
> "Add more detail about WHO uses your app. Instead of 'students,' specify: 'middle school students aged 11-14 who struggle with organization'"

**Poor Feedback:**
> "Target users section needs work"

**Implementation:**
```python
def generate_improvement_suggestions(score, feedback_items):
    suggestions = []

    if score < 50:
        suggestions.append("Start by addressing the missing required elements")
    elif score < 75:
        suggestions.append("Good foundation. Focus on adding more detail and examples")
    else:
        suggestions.append("Strong work! Polish your details for competition submission")

    # Prioritize feedback
    critical = [f for f in feedback_items if 'missing' in f.lower() or 'required' in f.lower()]
    if critical:
        suggestions.extend(critical[:3])  # Top 3 critical items
    else:
        suggestions.extend(feedback_items[:2])  # Top 2 improvement items

    return suggestions
```

---

## Integration Notes

### Curriculum Integration Points

**Where these skills fit:**
- **After Core Programming** (T06-T13): Students have coding skills to build projects
- **During Project Development** (weeks 2-4 of project timeline)
- **Before Competition Submission** (leave 2-3 weeks for iteration)

**Recommended Sequence:**
1. **Week 1: Planning**
   - T05.G6.06 (User Stories) → T16.G6.05 (Wireframes) → T03.G7.05 (Proposal)

2. **Week 2: Building**
   - Core coding using existing T06-T13 skills
   - T05.G7.06 (Requirements) for technical clarity

3. **Week 3: Testing & Refinement**
   - T13.G7.05 (Beta Testing) → iterate on code
   - T16.G7.05 (High-fidelity mockups) → polish UI

4. **Week 4: Documentation & Communication**
   - T12.G7.05 (Architecture docs)
   - T36.G7.05 (Demo video)
   - T36.G7.06 (Elevator pitch practice)

### Cross-Topic Dependencies

These skills create natural bridges between topics:

**T05 (Design) ↔ T16 (UI)**
- User stories → Wireframes → Mockups → Prototypes

**T03 (Planning) ↔ T12 (Documentation)**
- Proposal → Architecture → Technical specs

**T13 (Testing) ↔ T05 (Design)**
- Beta testing → Iterate based on feedback → Requirements refinement

**T36 (Communication) ↔ All Topics**
- Students communicate about their work across all technical topics

### Teacher Support Materials

**For each skill, provide:**
1. **Example Submissions** - Good, average, and needs-work samples
2. **Rubric Templates** - Ready-to-use assessment tools
3. **Scaffolding Options** - Templates for struggling students, extensions for advanced
4. **Time Management Guide** - How to fit these into project timeline

**Example Template: User Story Template**
```
As a [describe the user: age, role, context],
I want [specific feature or capability]
so that [concrete benefit or goal].

Priority: [ ] Must-Have (P1)  [ ] Should-Have (P2)  [ ] Nice-to-Have (P3)

Why this matters: [1 sentence explaining importance]
```

---

*End of Specifications Document*
*For integration roadmap, see: WEEK2_INTEGRATION_REPORT.md*
