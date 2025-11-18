# Creative Skills: Detailed Specifications

**Created:** 2025-11-17
**Purpose:** Complete specifications for 3 new creative skills addressing creativity gaps in CreatiCode K-8 Skill Map

---

## Overview

These 3 skills were created to enhance creative/artistic coverage in the curriculum based on the WEEK2_CREATIVITY_ANALYSIS findings:

1. **T20.G7.05** - Design a Visual Theme for Your Project (HIGH PRIORITY)
2. **T16.G7.06** - Add Delightful Details to Your Interface (HIGH PRIORITY)
3. **T05.G6.07** - Brainstorm Creative Solutions with Ideation Techniques (MEDIUM PRIORITY)

All three skills are production-ready with complete auto-grading rules, accessibility features, and detailed activity specifications.

---

## Skill 1: T20.G7.05 - Design a Visual Theme for Your Project

### Why This Skill Was Created

**Gap Identified:** Despite strong creative coverage, there was no explicit skill teaching aesthetic design principles - color theory, typography, and visual consistency.

**Current State:** T16.G7.05 (High-Fidelity Mockups) touches on visual design but doesn't explicitly teach color theory, typography principles, or aesthetic decision-making.

**Solution:** This skill explicitly teaches students to make intentional aesthetic choices based on emotion/mood, learn basic color theory, and create cohesive visual language.

---

### Learning Objectives

Students will be able to:
1. Choose a 3-5 color palette intentionally based on desired mood/emotion
2. Apply basic color theory concepts (complementary, analogous, warm/cool)
3. Select typography that matches project personality (playful, serious, modern, retro)
4. Create a style guide documenting design decisions
5. Apply visual theme consistently across all project elements
6. Explain the rationale behind color and typography choices

---

### Activity Design

**Duration:** 45 minutes

**Activity Flow:**

#### Phase 1: Learn Color Theory Basics (10 minutes)
Students review provided resources:
- **Color Wheel:** Understanding primary, secondary, tertiary colors
- **Color Relationships:**
  - Complementary colors (opposite on wheel - high contrast, energetic)
  - Analogous colors (next to each other - harmonious, calm)
  - Warm colors (red, orange, yellow - energetic, passionate)
  - Cool colors (blue, green, purple - calm, professional)
- **Color Psychology:**
  - Red: excitement, urgency, passion
  - Blue: trust, calm, professional
  - Yellow: happiness, optimism, warmth
  - Green: growth, nature, balance
  - Purple: creativity, luxury, mystery
  - Orange: friendly, energetic, playful

#### Phase 2: Define Project Mood (5 minutes)
Students answer:
- What emotion do I want my project to convey?
- Who is my audience?
- What similar apps/games have the feel I want?

Examples:
- Educational math game for kids → Playful, colorful, energetic
- Meditation app → Calm, minimal, soothing
- Mystery adventure game → Mysterious, dramatic, intriguing

#### Phase 3: Choose Color Palette (10 minutes)
Students select 3-5 colors:
1. **Primary color** (main brand color, used most)
2. **Secondary color** (supports primary, creates variety)
3. **Accent color** (used sparingly for important elements, creates pop)
4. **Optional:** Background color, text color

Tools:
- Color picker in CreatiCode
- Inspiration from provided palette examples
- Accessibility checker (sufficient contrast for text readability)

#### Phase 4: Select Typography (5 minutes)
Students choose fonts that match personality:
- **Playful:** Rounded, bouncy fonts (kids' games)
- **Serious:** Sans-serif, clean fonts (educational apps)
- **Modern:** Geometric, minimal fonts (tech apps)
- **Retro:** Pixel fonts or vintage-style (nostalgic games)

Best practices:
- Use 2 fonts max (one for headings, one for body)
- Ensure readability (avoid overly decorative fonts for body text)
- Consider font weight variety (bold for headings, regular for text)

#### Phase 5: Create Style Guide (10 minutes)
Students document in a text sprite or separate document:
```
PROJECT: [Name]
MOOD: [e.g., "Energetic and playful"]

COLORS:
- Primary: #FF6B6B (Coral Red)
- Secondary: #4ECDC4 (Turquoise)
- Accent: #FFE66D (Sunny Yellow)
- Background: #F7FFF7 (Off-white)

TYPOGRAPHY:
- Headings: "Fredoka" (Rounded, playful)
- Body Text: "Nunito" (Clean, readable)

USAGE RULES:
- Use primary color for main characters/buttons
- Use accent color sparingly for stars/rewards
- All backgrounds use color palette
- All text uses selected fonts
```

#### Phase 6: Apply Theme to Project (15 minutes)
Students systematically apply their theme:
- Change sprite colors to use palette
- Update background colors
- Change text fonts and colors
- Ensure consistency across all screens

---

### Auto-Grading Implementation

**Type:** Design Rubric with Automated Checks

**Automated Checks:**

1. **Color Palette Analysis** (25 points)
   - Detect distinct colors used in project
   - Check if 3-5 colors are consistently used
   - Implementation: Scan sprite costumes and backgrounds for color distribution

2. **Color Consistency Check** (20 points)
   - Verify selected colors appear on multiple sprites/backgrounds
   - Calculate color repetition score
   - Implementation: Check if each palette color appears in at least 3 different sprites/backgrounds

3. **Font Variety Detection** (20 points)
   - Detect if text elements use intentional font choices
   - Check for more than just default font
   - Implementation: Scan all text blocks for font properties

4. **Style Guide Submission** (20 points)
   - Check for uploaded/created style guide document
   - Verify it includes color codes and font names
   - Implementation: Look for sprite/document with "style guide" or specific format

5. **Design Rationale** (15 points)
   - Written reflection explaining choices
   - Check for thoughtful explanation
   - Implementation: Submission of reflection text (teacher-reviewed or keyword detection)

**Feedback Messages:**

- **Excellent (90-100%):** "Beautiful visual theme! Your color and typography choices create a cohesive, intentional design that matches your project's mood perfectly!"
- **Good (70-89%):** "Nice visual theme! Your project has consistent colors and fonts. Consider adding more variety in your typography or refining your color palette for even stronger visual impact."
- **Needs Improvement (<70%):** "Your project needs more visual consistency. Make sure you're using the same color palette throughout and that your fonts match your theme's personality."

---

### Accessibility Considerations

- Color blind safe: Style guide must include color names, not just visual swatches
- High contrast mode: Teach students to check text contrast against backgrounds
- Screen reader compatible: Style guide should be text-based, not just images
- Resources provided in both visual and text formats

---

### Dependencies

- **T16.G6.05** (Wireframes) - Students understand UI layout before styling
- **T20.G6.01** (Basic algorithmic art) - Students have experience with visual elements

---

### Standards Alignment

**CSTA:** 2-DA-09 (Refine computational models based on the data they have generated)
- Students use visual data (colors, fonts) to refine their design

**Competition Tags:** Games for Change, Congressional App Challenge
- Visual design is critical for competition projects

---

### Teacher Notes

**Common Misconceptions:**
- "Any colors work together" → Teach that intentional palettes create professional look
- "More colors = better" → Teach that restraint and consistency look more polished
- "Fonts don't matter" → Show examples of how font choice changes perception

**Extension Activities:**
- Analyze professional apps/games for color palette and typography
- Create multiple style guides for different moods
- A/B test: Show project to users with different color palettes

**Differentiation:**
- **Struggling students:** Provide pre-made palette options to choose from
- **Advanced students:** Challenge to create monochromatic palette or learn about color triads

---

## Skill 2: T16.G7.06 - Add Delightful Details to Your Interface

### Why This Skill Was Created

**Gap Identified:** No explicit skills about adding user delight and microinteractions to interfaces.

**Current State:** UI skills focus on functionality (buttons work, forms collect data) but not on polish and personality.

**Solution:** This skill teaches students to add microinteractions, easter eggs, and playful microcopy that make interfaces feel alive and joyful.

---

### Learning Objectives

Students will be able to:
1. Implement at least 2 microinteractions (button animations, transitions, hover effects)
2. Create at least 1 easter egg or surprise element
3. Replace generic UI text with playful, personality-filled microcopy
4. Understand that great design includes small, thoughtful details
5. Make interfaces that users smile while using

---

### Activity Design

**Duration:** 40 minutes

**Activity Flow:**

#### Phase 1: What Makes Apps Delightful? (5 minutes)
Discussion/reflection:
- Think of an app you love using. What makes it fun?
- Often it's the small details: smooth animations, fun sounds, playful language
- Show examples:
  - Button that bounces when clicked
  - Loading screen with encouraging messages
  - Hidden animation when clicking logo
  - Error message that's funny instead of scary

#### Phase 2: Add Microinteractions (15 minutes)
Students implement at least 2 of these:

**Button Click Animations:**
```
When button clicked:
- Grow button size to 110% for 0.1 seconds
- Shrink back to 100%
- (Creates satisfying bounce effect)
```

**Hover Effects:**
```
When mouse hovers over button:
- Change color slightly (lighter or darker)
- Show glow effect
- (Provides feedback that button is interactive)
```

**Screen Transitions:**
```
When changing screens:
- Fade out current screen over 0.3 seconds
- Fade in new screen over 0.3 seconds
- (Smooth transition feels professional)
```

**Element Appear Animations:**
```
When showing new element:
- Start at 0% size
- Grow to 100% size over 0.3 seconds
- Add slight rotation or bounce
- (Elements feel like they're "popping in")
```

#### Phase 3: Hide an Easter Egg (10 minutes)
Students create at least 1 surprise:

**Multi-Click Secret:**
```
Variable: logo_click_count
When logo clicked:
- Increment logo_click_count
- If logo_click_count = 3:
  - Show hidden animation/message
  - Play fun sound
  - Reset counter
```

**Hidden Sprite Interaction:**
```
Place tiny invisible sprite in corner
When clicked:
- Show confetti animation
- Play secret sound
- Display fun message
```

**Secret Code Entry:**
```
If user types specific word in text input:
- Unlock special theme/character
- Show achievement message
```

**Surprise Animation Trigger:**
```
When user achieves high score:
- Character does victory dance
- Fireworks animation
- Confetti falls
```

#### Phase 4: Write Playful Microcopy (10 minutes)
Students replace boring text with personality:

**BEFORE → AFTER:**
- "Click here" → "Let's go!" or "Start the adventure!"
- "Submit" → "Send it!" or "Make it happen!"
- "Error" → "Oops, that didn't work!" or "Hmm, let's try again"
- "Loading" → "Getting things ready..." or "Hang tight!"
- "Delete" → "Say goodbye to this?" (with confirmation)
- "Cancel" → "Never mind" or "Go back"

**Principles:**
- Use contractions (it's, let's, we're) - sounds conversational
- Address user directly (you, your, we)
- Add encouragement ("You got this!", "Almost there!")
- Make errors less scary ("No worries, let's fix this")

---

### Auto-Grading Implementation

**Type:** Interaction Pattern Detection

**Automated Checks:**

1. **Microinteractions Detection** (40 points)
   - Minimum: 2 microinteractions
   - Detection method: Scan for animation blocks on button/UI sprites
   - Accepted types:
     - Button click animation (size/color change)
     - Hover effect (change appearance when sensing mouse)
     - Screen transition (fade/slide effects between backdrops)
     - Element appear animation (size/position change when showing)

2. **Easter Egg Detection** (30 points)
   - Minimum: 1 easter egg
   - Detection method: Look for hidden interactions
   - Accepted types:
     - Multi-click counter (variable that tracks clicks, triggers at threshold)
     - Hidden sprite interaction (sprite with low visibility/size that triggers something)
     - Secret code entry (conditional checking for specific text input)
     - Surprise animation trigger (special animation on unusual condition)

3. **Playful Microcopy Detection** (30 points)
   - Minimum: 3 instances of playful text
   - Detection method: Scan all text blocks for personality
   - Flag generic text: "Click here", "Error", "OK", "Submit", "Cancel"
   - Reward creative text: exclamation points, questions, conversational language

**Feedback Messages:**

- **Excellent (90-100%):** "Your interface is delightful! The microinteractions, easter eggs, and playful text make it feel alive and fun to use. Great attention to detail!"
- **Partial (60-89%):** "Good start on adding personality! You have some nice details, but try adding more microinteractions or making your text even more playful."
- **Incomplete (<60%):** "Your interface could use more delightful details! Add some animations, hide a fun surprise, and make your text more playful."

---

### Example Activities

**Example 1: Button Bounce Animation**
```
When "Start Game" button clicked:
  change size to 110% (0.1 seconds)
  change size to 100% (0.1 seconds)
  play sound "pop"
  start game
```

**Example 2: Loading Screen with Personality**
```
When loading:
  show sprite "Loading Animation"
  randomly choose message from list:
    - "Waking up the hamsters..."
    - "Sprinkling magic dust..."
    - "Charging the lasers..."
    - "Almost there!"
  display message
  when loaded: hide loading sprite
```

**Example 3: Secret Code Easter Egg**
```
When user types in text box:
  if text = "unicorn":
    show sprite "Rainbow Unicorn"
    play sound "magical"
    say "You found the secret!" for 2 seconds
```

---

### Dependencies

- **T16.G7.05** (High-Fidelity Mockups) - Students have designed UI before adding polish
- **T16.G6.01** (Basic widgets) - Students know how to create UI elements

---

### Standards Alignment

**CSTA:** 2-AP-16 (Incorporate existing code, media, and libraries into original programs, and give attribution)
- Students use animation libraries and interaction patterns

**Competition Tags:** Games for Change, Congressional App Challenge
- Polish and user experience are important for competition success

---

### Teacher Notes

**Why This Matters:**
Apps that feel delightful get used more. Small details make users smile and want to keep using your app. This is about caring about the full user experience, not just functionality.

**Common Pitfalls:**
- **Too many animations:** Animations should enhance, not distract. Teach restraint.
- **Slow animations:** Keep animations fast (0.1-0.3 seconds). Slow animations frustrate users.
- **Inconsistent personality:** If your app is professional, don't add silly easter eggs. Match tone.

**Extension Activities:**
- User test: Does someone smile while using your app?
- Find 5 delightful details in professional apps you use
- Create a "delight checklist" for your project

**Differentiation:**
- **Struggling students:** Start with just 1 button animation and 1 playful text change
- **Advanced students:** Create complex animation sequences or sound design

---

## Skill 3: T05.G6.07 - Brainstorm Creative Solutions with Ideation Techniques

### Why This Skill Was Created

**Gap Identified:** Students often jump to the first idea without exploring alternatives. No explicit skill teaching structured ideation techniques.

**Current State:** Students expected to come up with ideas but not taught how to brainstorm effectively.

**Solution:** This skill teaches industry-standard ideation techniques (Crazy 8s, SCAMPER, mind mapping) and "Yes, and..." thinking.

---

### Learning Objectives

Students will be able to:
1. Use structured ideation techniques (Crazy 8s, SCAMPER, mind mapping)
2. Generate at least 10 distinct ideas before selecting one
3. Practice divergent thinking (many ideas, no judgment) then convergent thinking (select best)
4. Apply "Yes, and..." thinking to build on ideas
5. Document idea evolution from initial thought to refined concept
6. Understand that creativity is a skill that can be practiced

---

### Activity Design

**Duration:** 30 minutes

**Activity Flow:**

#### Phase 1: Introduction to Ideation (5 minutes)
Teacher explains:
- **Problem:** Students often use first idea without exploring alternatives
- **Solution:** Professional designers generate dozens of ideas before choosing
- **Process:** Divergent (generate many) → Convergent (select best)
- **Key rule:** During brainstorming, quantity beats quality! Wild ideas welcome!

#### Phase 2: Choose and Use Ideation Technique (15 minutes)

**OPTION A: Crazy 8s (Recommended for Speed)**

Setup:
1. Fold paper into 8 sections (or use template)
2. Set timer for 8 minutes
3. Goal: Sketch a different idea in each section

Process:
- 1 minute per idea
- Draw rough sketches (stick figures OK!)
- Don't overthink - speed prevents perfectionism
- Fill all 8 sections before time runs out

Benefits:
- Forces quantity over quality
- Prevents attachment to first idea
- Fun and energetic

---

**OPTION B: SCAMPER (Recommended for Remixing)**

Start with existing idea or problem, then ask:

- **S - Substitute:** What can I replace? (Different character? Different setting?)
- **C - Combine:** What can I merge? (Two game genres? Two features?)
- **A - Adapt:** What can I borrow from something else? (How do other apps solve this?)
- **M - Modify:** What can I change? (Make it bigger? Faster? Sillier?)
- **P - Put to other use:** What if it had a different purpose? (Educational game → art tool?)
- **E - Eliminate:** What can I remove? (Simplify? Minimize?)
- **R - Reverse:** What if I did the opposite? (Bad guys are heroes? Player doesn't move?)

Process:
1. Write initial idea
2. Go through each SCAMPER letter
3. Generate 2-3 variations for each
4. Review all variations and select favorites

Benefits:
- Systematic exploration
- Creates unexpected combinations
- Good for improving existing ideas

---

**OPTION C: Mind Mapping (Recommended for Complex Problems)**

Setup:
1. Write main problem/topic in center circle
2. Draw branches for major categories
3. Draw sub-branches for specific ideas
4. Keep expanding outward

Example - "Design a Game":
```
          [Characters]─── Animals
         /              └─ Robots
        /
[GAME]─────[Setting]─── Space
        \              └─ Underwater
         \
          [Goal]──── Rescue mission
                   └─ Collect items
```

Process:
- Start broad (categories)
- Get specific (ideas within categories)
- Look for connections between branches
- Circle most interesting ideas

Benefits:
- Visualizes thinking
- Shows connections
- Good for exploring complex problems

---

#### Phase 3: Generate Additional Ideas (5 minutes)
If technique didn't generate 10 ideas yet:
- Use "What if...?" prompts
- Combine ideas from different techniques
- Practice "Yes, and..." (build on existing ideas)

Example "Yes, and...":
- Idea: "A game about planting trees"
- Yes, and... "What if the trees fight pollution monsters?"
- Yes, and... "What if each tree has special powers?"
- Yes, and... "What if it's multiplayer and you build a forest together?"

---

#### Phase 4: Select and Refine (5 minutes)

Selection criteria:
- **Feasibility:** Can I actually build this with my skills?
- **Impact:** Will this solve the problem or delight users?
- **Originality:** Is this different from what already exists?
- **Excitement:** Am I genuinely excited to build this?

Document:
- Which idea did you choose?
- Why did you choose it over others?
- How did it evolve from initial brainstorm?

---

### Auto-Grading Implementation

**Type:** Submission Portfolio with Rubric

**Required Submissions:**

1. **Ideation Worksheet** (Image or Text)
   - Submit sketches/notes showing 10+ ideas
   - Can be photos of paper sketches or digital document

2. **Variety Check** (Automated)
   - AI analysis of idea descriptions
   - Flag if all ideas are minor variations
   - Reward diverse approaches

3. **Evolution Documentation**
   - Before/after comparison showing refinement
   - Could be: "Initial idea: [X] → Refined to: [Y] because [reason]"

4. **Selection Rationale**
   - Written explanation (3-5 sentences)
   - Why this idea? What makes it strong?

**Rubric:**

| Criterion | Points | Excellent | Good | Needs Improvement |
|-----------|--------|-----------|------|-------------------|
| Quantity | 25 | 10+ distinct ideas | 7-9 ideas | < 7 ideas |
| Variety | 25 | Ideas explore different approaches | Some variety | All similar variations |
| Evolution | 20 | Clear refinement documented | Some evolution shown | No evolution |
| Technique | 20 | Effectively used ideation technique | Attempted technique | Didn't follow technique |
| Rationale | 10 | Thoughtful explanation | Basic explanation | No rationale |

**Feedback Messages:**

- **Excellent (90-100%):** "Outstanding ideation! You generated diverse, creative ideas and clearly documented your thinking process. This brainstorming will lead to a stronger final project!"
- **Good (70-89%):** "Good brainstorming! You generated multiple ideas. To improve, try pushing for even more variety - what's a completely different approach?"
- **Needs Improvement (<70%):** "You need more ideas! Set a timer and try Crazy 8s - sketch 8 different ideas without stopping to judge them."

---

### Ideation Technique Quick Reference

**When to Use What:**

| Technique | Best For | Time Needed | Output |
|-----------|----------|-------------|--------|
| **Crazy 8s** | Quick idea generation, visual projects | 8 minutes | 8 sketch ideas |
| **SCAMPER** | Remixing existing ideas, systematic exploration | 15 minutes | 10-20 variations |
| **Mind Mapping** | Complex problems, exploring connections | 10-15 minutes | Visual idea tree |
| **Yes, and...** | Group brainstorming, building momentum | 5-10 minutes | Collaborative ideas |

---

### Example Ideation: "Design a Math Learning Game"

**Crazy 8s Sketches (8 minutes):**
1. Pizza fractions - divide pizzas to serve customers
2. Math race - solve problems to move forward
3. Number garden - plant flowers by solving equations
4. Time travel - fix historical events with math
5. Math wizard - cast spells using formulas
6. Space mission - calculate trajectory to planets
7. Cooking show - measure ingredients for recipes
8. City builder - use math to plan city layout

**SCAMPER Variations:**
- **Substitute:** Replace numbers with shapes? Musical notes?
- **Combine:** Mix math + art (create patterns)? Math + storytelling?
- **Adapt:** Borrow from cooking games? Racing games?
- **Modify:** Make it multiplayer? Add power-ups?
- **Put to other use:** Not a game - an interactive toy?
- **Eliminate:** Remove scoring? Remove time pressure?
- **Reverse:** Student teaches instead of being taught?

**Selection:**
- **Chose:** "Number Garden" - plant flowers by solving equations
- **Why:** Combines calming visuals with math practice. Different difficulty flowers for different math levels. Satisfying to watch garden grow.
- **Evolution:** Initial idea was just "solve math problems". SCAMPER added gardening theme. Crazy 8s showed visual appeal matters.

---

### Dependencies

**None** - This is a foundational creative skill that can be taught early

---

### Standards Alignment

**CSTA:** 1B-AP-15 (Test and debug a program or algorithm to ensure it runs as intended)
- Ideation is part of the design process before testing

**Competition Tags:** Games for Change, Congressional App Challenge
- Strong brainstorming leads to better competition projects

---

### Teacher Notes

**Creating a Safe Brainstorming Environment:**
- Emphasize "no bad ideas during brainstorming"
- Model wild/silly ideas yourself
- Celebrate quantity ("Wow, 15 ideas!")
- Separate divergent (generate) from convergent (judge) phases

**Common Student Reactions:**
- "My first idea is the best!" → Show examples where later ideas were chosen
- "I can't think of anything!" → Use prompts: "What if it was underwater? In space? Tiny? Giant?"
- "This is silly!" → Explain that silly ideas often lead to breakthroughs

**Extension Activities:**
- Group brainstorming (4 students do Crazy 8s together, share ideas)
- Reverse brainstorming ("How could we make this as BAD as possible?" then reverse)
- Forced connections ("Combine your idea with [random word]")

**Differentiation:**
- **Struggling students:** Start with SCAMPER on existing idea (easier than blank slate)
- **Advanced students:** Try multiple techniques, generate 20+ ideas, explore idea combinations

---

## Integration with Existing Curriculum

### How These Skills Fit

**T05.G6.07 (Ideation)** → Foundational creative skill
- Used BEFORE starting any project
- Feeds into all design and project skills

**T20.G7.05 (Visual Theme)** → Mid-project design skill
- Used AFTER planning, BEFORE/DURING implementation
- Feeds into: T16.G7.05 (Mockups), T36.G7.05 (Demo Video)

**T16.G7.06 (Delightful Details)** → Polish/refinement skill
- Used AFTER core functionality complete
- Final step before: T13.G7.05 (Beta Testing), T36.G7.05 (Demo Video)

---

### Recommended Project Flow

```
1. T05.G6.07 - Brainstorm ideas (choose project concept)
2. T05.G6.06 - Write user stories (define features)
3. T16.G6.05 - Create wireframes (plan layout)
4. T20.G7.05 - Design visual theme (choose aesthetics)
5. T16.G7.05 - Create mockups (detailed design)
6. [Build core functionality - various programming skills]
7. T16.G7.06 - Add delightful details (polish)
8. T13.G7.05 - Beta test (gather feedback)
9. T36.G7.05 - Create demo video (showcase)
```

---

## Assessment Guidelines

### Formative Assessment (During Activity)

**T20.G7.05 (Visual Theme):**
- Walk around and ask: "Why did you choose these colors?"
- Check: Are students using color theory concepts?
- Look for: Consistency across sprites/backgrounds

**T16.G7.06 (Delightful Details):**
- Ask: "What makes someone smile when using your app?"
- Test: Do interactions feel smooth and satisfying?
- Look for: Personality in text and animations

**T05.G6.07 (Ideation):**
- Check: Are students generating quantity or judging too early?
- Ask: "How is this idea different from the previous one?"
- Look for: Variety and willingness to explore wild ideas

---

### Summative Assessment (Final Submission)

All skills include detailed auto-grading rubrics. Teachers can also:

**Portfolio Review:**
- Collect style guides, ideation worksheets, and screenshots
- Display excellent examples for class to learn from
- Create gallery of visual themes

**Peer Review:**
- Students test each other's projects for delightful details
- Students critique each other's visual themes
- Students share brainstorming techniques that worked

**Reflection Questions:**
- "How did your ideation process change your final project?"
- "What did you learn about color/typography that surprised you?"
- "What delightful detail are you most proud of?"

---

## Resources Needed

### For T20.G7.05 (Visual Theme):
- Color wheel reference chart
- Color psychology guide
- Typography personality guide
- Example style guides from professional apps/games
- Color contrast checker (for accessibility)
- Hex code picker tool

### For T16.G7.06 (Delightful Details):
- Animation examples from popular apps
- Microinteraction video demonstrations
- List of generic vs. playful microcopy examples
- Sound effects library (for easter eggs)

### For T05.G6.07 (Ideation):
- Crazy 8s template (paper folded into 8 sections)
- SCAMPER prompt cards
- Mind mapping template
- Timer for Crazy 8s activity
- Example ideation worksheets

All resources should be provided in both digital and printable formats for accessibility.

---

## Success Metrics

**How to measure if these skills are effective:**

1. **Student Engagement:**
   - Do students spend more time on visual design?
   - Do students voluntarily add details beyond requirements?
   - Do students show excitement about their aesthetic choices?

2. **Project Quality:**
   - Do final projects have more visual consistency?
   - Do projects have more personality and polish?
   - Do projects show evidence of exploring multiple ideas?

3. **Student Reflection:**
   - Can students articulate their design decisions?
   - Do students understand color theory and typography basics?
   - Do students recognize ideation as a skill to practice?

4. **Competition Success:**
   - Do projects submitted to competitions show stronger design?
   - Do judges comment on visual appeal and polish?

---

## Conclusion

These 3 creative skills address specific gaps in the curriculum:

1. **T20.G7.05** fills the gap in explicit aesthetic design instruction
2. **T16.G7.06** fills the gap in user delight and microinteractions
3. **T05.G6.07** fills the gap in structured ideation techniques

All three skills are:
- ✅ **Production-ready** with complete specifications
- ✅ **Auto-gradable** with detailed rubrics and detection methods
- ✅ **Accessible** with full accessibility support
- ✅ **Standards-aligned** with CSTA codes
- ✅ **Competition-relevant** tagged for Games for Change and Congressional App Challenge
- ✅ **Age-appropriate** for their grade levels (G6-G7)

These skills enhance the creative/artistic balance of the curriculum while maintaining the practical, project-based approach that makes CreatiCode effective.
