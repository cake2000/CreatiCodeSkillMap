# T12 – Organizing Programs: K–8 Skill List (Draft v1)

Topic reference: `T12 Organizing Programs` in `domains_topics_overview.md`
Domain: Programming (D2) · CSTA focus: PRO‑PM (Project Management)

Each skill below has:

- a stable **ID** (`T12.G<grade>.<nn>`),
- an IXL‑style **short name**,
- a **description** (what understanding/behavior it targets),
- a **challenge format** (the typical problem type to assess it).

Where relevant, a primary **CSTA code** is noted.

**Role and scope in v3:** T12 focuses on **organizing programs and projects** once students are coding: naming things clearly, structuring scripts, documenting intent, and maintaining consistent style so teams (and future selves) can understand and extend code. K–2 planning, grouping everyday steps, and assigning jobs are handled by T01/T03/T05; T12 assumes that conceptual planning foundation and begins in **Grade 1** with unplugged, picture‑based organization of routines, then transitions in Grades 3–8 to CreatiCode projects (comments, script headers, grouping related code, refactoring for readability). T11 covers procedural abstraction (custom blocks/functions); T03 covers project decomposition; T12 is specifically about *how the code and documentation are laid out for clarity and collaboration*.

---

---

## Grade 1

Grade 1 extends organizing everyday instructions by naming sections, noticing the “main plan” versus smaller tasks, and explaining who does what, all without needing a computer.

### T12.G1.01 – Find the main set of instructions

- **Short name:** Spot the main plan
- **Description:** Students look at 2–3 short sets of picture‑based instructions (e.g., "how to set up the game," "how to decorate," "how to clean up") and decide which one tells everyone what to do overall for an activity. This builds the idea that some instructions are the main plan and others are side tasks.
- **Challenge format:** Concept, multiple choice. Show several picture strips; students choose which strip is the main plan for the activity. Auto‑grading checks that the main, overall routine is selected.
- **CSTA:** E1‑PRO‑PM‑04 (Explain the function of a step in a process).

### T12.G1.02 – Give a clear title to a set of steps

- **Short name:** Name a set of steps
- **Description:** Students practice giving each group of picture steps a clear title that tells what it is for (e.g., "Getting Ready," "Playing the Game," "Clean‑Up Time") instead of vague titles like "Stuff" or "Things to Do."
- **Challenge format:** Concept, matching or choice. Show a set of picture steps plus several possible titles. Students choose the title that best matches the set. Auto‑grading checks for a clear, accurate title.
- **CSTA:** E1‑PRO‑PM‑04.

### T12.G1.03 – Explain what each group of steps does

- **Short name:** Say what each group does
- **Description:** Students see 2–3 groups of picture instructions for a class routine and match each group to a simple description (e.g., "These steps get the classroom ready," "These steps are for playing," "These steps are for cleaning up"). This strengthens the habit of explaining the role of each part of a plan.
- **Challenge format:** Concept, matching. Provide groups of steps and short descriptions; students connect each group to its description. Auto‑grading checks correct matches.
- **CSTA:** E1‑PRO‑PM‑04.

### T12.G1.04 – Split a long list of steps into two lists

- **Short name:** Put different jobs in different lists
- **Description:** Students are given a long mixed list of picture steps for a class event and asked to split them into two shorter lists (e.g., "Before the event" and "During the event," or "Adult jobs" and "Student jobs"). This mirrors splitting one big routine into smaller, organized parts.
- **Challenge format:** Concept, sorting activity. Provide one long list of step cards and two labeled areas. Students drag or place each card into the list where it belongs. Auto‑grading checks that steps are grouped into sensible lists.
- **CSTA:** E1‑PRO‑PM‑05 (Collaborate with a partner to develop a plan).

---

## Grade 2

Grade 2 introduces simple notes and labels for parts of a plan and encourages students to group related steps under clear headings, still at a fully conceptual, picture‑based level.

### T12.G2.01 – Add a note to explain a section of a plan

- **Short name:** Write a note for a section
- **Description:** Students add a short note near a group of steps to explain why that section is there (e.g., "These steps are to get ready," "These steps are to clean up"). This is an unplugged analogue of commenting and documenting parts of a project.
- **Challenge format:** Concept, matching or fill‑in. Show a routine divided into 2–3 visual sections and several possible sticky‑note style explanations. Students choose or place the note that best explains each section. Auto‑grading checks note–section matches.
- **CSTA:** E2‑PRO‑PM‑04 (Document the steps taken during a process).

### T12.G2.02 – Fix confusing labels on a plan

- **Short name:** Rename to make a plan clearer
- **Description:** Students see a simple plan with section titles that are vague or unclear (e.g., "Stuff," "More things") and replace them with clearer titles that match the steps underneath (e.g., "Set up chairs," "Decorate the room"). This mirrors renaming confusing identifiers but stays at the level of everyday language.
- **Challenge format:** Concept, editing titles. Provide sections with poor labels and a list of better labels; students choose the best label for each section. Auto‑grading checks that clearer, specific labels are chosen.
- **CSTA:** E2‑PRO‑PM‑04.

### T12.G2.03 – Use the same style for section titles

- **Short name:** Make titles match in style
- **Description:** Students review several section titles for one plan (e.g., "Set up," "Playing the game," "Clean up time!") and adjust or choose options so they all follow a similar style (for example, all starting with action words). This builds awareness of consistent naming without introducing code vocabulary.
- **Challenge format:** Concept, choose‑and‑edit. Show multiple headings; students pick the version of each that follows a chosen style (all verb phrases, all starting with a capital letter, etc.). Auto‑grading checks that the selected titles follow one consistent style.
- **CSTA:** E2‑PRO‑PM‑04.

### T12.G2.04 – Group related steps under a heading

- **Short name:** Put steps under the right heading
- **Description:** Students see 2–3 headings (e.g., "Before class," "During class," "After class") and a mixed set of picture steps, then group each step under the heading where it belongs. This extends the Grade 1 idea of splitting lists into clearly labeled sections.
- **Challenge format:** Concept, drag‑and‑drop grouping. Provide headings and step cards; students drag each step to its heading. Auto‑grading checks that steps are grouped under reasonable headings.
- **CSTA:** E2‑PRO‑PM‑04.

---

## Grade 3

Grade 3 deepens documentation practices and introduces the concept of refactoring for readability. Students articulate code structure and improve projects for others to understand.

### T12.G3.01 – Write a comment explaining a complex block

- **Short name:** Document a complex block
- **Description:** Students add a comment to a block or small sequence that is less obvious in purpose (e.g., a `repeat until <touching goal>` loop) to clarify the intent ("Loop until the sprite reaches the flag"). Comments explain the "why" and "what" of non-obvious code.
- **Challenge format:** Coding, starter project. Provided: a script with a complex block or sequence (e.g., a condition with multiple parts). Prompt: "Add a comment above this block explaining what it does and why it's needed." Auto‑grading checks that a comment exists and uses key terms from the code.
- **CSTA:** E3‑PRO‑PM‑05 (Articulate the function of a specific aspect of a program).

### T12.G3.02 – Create a header comment for a script

- **Short name:** Summarize a script at the top
- **Description:** Students add a comment block at the very top of a script that summarizes its purpose, triggering event, and role in the larger program (e.g., "# When the green flag is clicked, initialize the game: set lives to 3, reset score, show the start screen"). This is a first step toward external documentation.
- **Challenge format:** Coding, starter project. Provided: a script without a header comment. Prompt: "Add a comment at the top of this script explaining what it does and when it runs." Auto‑grading checks for a comment at the top (first block) with at least 10 words covering event and purpose.
- **CSTA:** E3‑PRO‑PM‑05.

### T12.G3.03 – Refactor nested or repeated blocks for readability

- **Short name:** Simplify code to make it clearer
- **Description:** Students take a project with deeply nested conditionals or repeated patterns and refactor it—either by using custom blocks, better variable names, or breaking into multiple scripts—to make the logic easier to follow.
- **Challenge format:** Coding, refactor starter. Provided: a script with 2–3 levels of nesting or repeated similar blocks. Prompt: "Reorganize this code to make it easier to read. You can create custom blocks or split into separate scripts if it helps." Auto‑grading checks that nesting depth is reduced or logic is broken into clearer sections, and that behavior is unchanged.
- **CSTA:** E3‑PRO‑PM‑05, PRO‑TR (testing and refining).

### T12.G3.04 – Explain the structure of a multi-script project

- **Short name:** Describe how scripts work together
- **Description:** Students write or select explanations for how the scripts in a project interact and fit together (e.g., "The green-flag script sets up the game, and the key-press scripts let the player control the character"). This develops understanding of overall code organization.
- **Challenge format:** Concept, open-ended explanation or selection. A project with 3–4 scripts is shown. Students write or choose from prompts a summary of the project structure ("There are ___ scripts: one for ___, one for ___, and one for ___"). Auto‑grading uses keyword matching or rubric-based scoring.
- **CSTA:** E3‑PRO‑PM‑05.

---

## Grade 4

Grade 4 emphasizes comprehensive documentation (comments and external notes), refactoring for clarity, and understanding how code organization affects collaboration.

### T12.G4.01 – Document a program with embedded comments

- **Short name:** Add comments throughout a program
- **Description:** Students add comments to multiple scripts, blocks, and sections in a complete project, explaining what each part does and how it contributes to the whole. This is the first experience with systematic documentation.
- **Challenge format:** Coding, starter project. Provided: a complete game or interactive project with no comments. Prompt: "Add comments to at least 5 different parts of your program, explaining what each does." Auto‑grading checks for comment count, placement (at least one per script or logical section), and relevance (comments describe code, not just restate syntax).
- **CSTA:** E4‑PRO‑PM‑05 (Document a program using embedded comments).

### T12.G4.02 – Choose descriptive names for custom blocks

- **Short name:** Name a custom block clearly
- **Description:** Students create custom blocks with clear, verb-based names (e.g., "move forward", "draw star", "check collision") so that anyone using the block understands its purpose without looking inside.
- **Challenge format:** Coding, starter project. Provided: a project with a custom block that has a vague name (e.g., "do_thing" or "block1"). Prompt: "Rename your custom block to describe exactly what it does." Auto‑grading checks that the custom block name is a verb or verb phrase (starts with a verb like "move," "draw," "check") and is at least 2 words.
- **CSTA:** E4‑PRO‑PM‑05.

### T12.G4.03 – Refactor repeated blocks into a custom block for clarity

- **Short name:** Use custom blocks to reduce duplication
- **Description:** Students identify repeated code segments (within or across scripts) and extract them into a new custom block with a clear name. This reduces clutter and makes the main code easier to read.
- **Challenge format:** Coding, refactor starter. Provided: a project with a sequence of blocks (e.g., "say 'Ready?', wait 1 sec, say 'Set!', wait 1 sec") repeated 2–3 times. Prompt: "Create a custom block called 'say_countdown' and use it to replace the repeated code." Auto‑grading checks that the custom block exists, is used at least twice, and that the original repeated blocks are removed.
- **CSTA:** E4‑PRO‑PM‑05, PRO‑TR.

### T12.G4.04 – Analyze and improve variable scope and naming

- **Short name:** Use meaningful variable names and scopes
- **Description:** Students examine a project and ensure that variables have clear names and that their scope (where they can be used) is understood. They may rename variables or add comments to clarify scope (e.g., "global variable used by all sprites").
- **Challenge format:** Coding, code-review starter. Provided: a project with several variables. Students review and identify which are global vs local, rename any unclear ones, and optionally add comments explaining scope. Auto‑grading checks that variable names are descriptive and that any new comments mention scope or usage correctly.
- **CSTA:** E4‑PRO‑PM‑05.

---

## Grade 5

Grade 5 encourages students to view documentation and organization as collaborative tools. They create external guides and improve projects for others to understand and extend.

### T12.G5.01 – Create external documentation for a project

- **Short name:** Write a guide for your project
- **Description:** Students write or create a simple external document (text block within CreatiCode or a linked file) that explains the project: what it does, how to use it, what each script does, and what variables track. This is the first experience with formal external documentation.
- **Challenge format:** Concept and coding hybrid. Provided: a completed project. Prompt: "Create a simple guide that explains your project. Include: (1) What the project does, (2) How to use it, (3) What each script does." Auto‑grading checks that the document exists, is at least 100 words, and covers all three required sections with specific references to scripts/variables.
- **CSTA:** E5‑PRO‑PM‑05 (Create embedded or external documentation).

### T12.G5.02 – Document code functionality and choices

- **Short name:** Explain why you coded it that way
- **Description:** Students add comments explaining not just what code does, but why they chose that approach (e.g., "I use a repeat loop here instead of separate move blocks because it's shorter and easier to change the distance"). This introduces meta-cognition about code organization.
- **Challenge format:** Coding, reflection starter. Provided: a script with a highlighted block or sequence. Prompt: "Add a comment explaining why you chose this approach. What makes it better than an alternative?" Auto‑grading checks for comments that explain reasoning (uses words like "because," "instead of," "this way," "advantage").
- **CSTA:** E5‑PRO‑PM‑05.

### T12.G5.03 – Organize a multi-feature project with sections

- **Short name:** Organize code into clear sections
- **Description:** Students structure a larger project into clearly marked sections (using comments and script organization) such as "Initialization," "Player Controls," "Collision Detection," "Score Display," etc. This introduces larger-scale code organization.
- **Challenge format:** Coding, starter project with multiple features. Prompt: "Reorganize your project so each major feature has its own script or section with a clear header comment. For example, 'Initialization,' 'Player Controls,' 'Enemy AI,' 'Scoring.'" Auto‑grading checks that at least 4 sections are identified, each with a header comment, and that related code is grouped together.
- **CSTA:** E5‑PRO‑PM‑05.

### T12.G5.04 – Review and improve another student's code organization

- **Short name:** Give feedback on code clarity
- **Description:** Students review a peer's project and provide constructive feedback on its organization, naming, and documentation (e.g., "The variable names are clear, but some scripts are very long and could be split up"). This develops critical reading skills and introduces collaboration norms.
- **Challenge format:** Concept, peer review activity. Students are given a project (provided or from a peer) with moderate organization. Prompt: "Review the code and identify: (1) One thing that is clear and well-organized, (2) One thing that could be improved for clarity." Auto‑grading (if used) checks that feedback is specific and actionable; teacher or peer scoring is typical.
- **CSTA:** E5‑PRO‑PM‑06 (Collaborate with peers to design and review a project).

---

## Grade 6

In middle school, students apply organization and documentation to more complex projects and understand their importance for team collaboration and code maintenance.

### T12.G6.01 – Analyze a program's organization and suggest improvements

- **Short name:** Evaluate and improve code structure
- **Description:** Students read a multi-script program and critique its organization (e.g., "The collision checks are mixed with the movement code; they should be separate for clarity") and propose refactoring steps that improve readability without changing behavior.
- **Challenge format:** Concept and coding hybrid. Provided: a program (2–4 scripts) with suboptimal organization. Prompt: "Explain what could be clearer about this program's organization, and propose one refactoring (e.g., create a custom block, split a script, add comments) to improve it." Auto‑grading uses rubric-based scoring (clarity of critique, feasibility of suggestion).
- **CSTA:** MS‑PRO‑PM‑16 (Document a program using comments, descriptive names, and structured guides).

### T12.G6.02 – Use comments to explain algorithm logic

- **Short name:** Document an algorithm with comments
- **Description:** Students add comments to a section of code that implements a recognizable algorithm or pattern (e.g., a loop that finds the maximum, or a conditional that checks collisions) to explain the logic in plain English.
- **Challenge format:** Coding, starter project with algorithmic code. Prompt: "This section of code checks if the player is touching an enemy. Add comments explaining how it works step by step." Auto‑grading checks that comments correspond to code lines and accurately describe the logic.
- **CSTA:** MS‑PRO‑PM‑16.

### T12.G6.03 – Create a style guide for variable and block naming

- **Short name:** Establish a naming convention
- **Description:** Students define a naming convention (camelCase, snake_case, verb-based for custom blocks, noun-based for variables) and apply it consistently across a project, or write a short guide for others to follow.
- **Challenge format:** Coding and concept hybrid. Prompt: "Choose a naming style for variables (camelCase or snake_case) and custom blocks (verb phrases). Apply your style to your project consistently. Write a one-sentence description of your style choice." Auto‑grading checks consistency in the project and the presence of a style description.
- **CSTA:** MS‑PRO‑PM‑16.

### T12.G6.04 – Document code for collaborative maintenance

- **Short name:** Write docs for someone else to work on
- **Description:** Students add comments, external documentation, and clear structure to a project specifically to enable a peer or future self to modify it. They explain key variables, the role of each script, and any design decisions that might not be obvious.
- **Challenge format:** Coding, handoff activity. Prompt: "Imagine someone else will modify your code next week. Add comments and documentation so they can understand and change it easily." Auto‑grading (often peer or teacher review) checks for clarity, completeness (all scripts mentioned), and whether a newcomer could navigate the code.
- **CSTA:** MS‑PRO‑PM‑16.

---

## Grade 7

Grade 7 deepens the connection between code organization and maintainability. Students analyze trade-offs in organization choices and work on larger projects with many features.

### T12.G7.01 – Refactor long scripts into smaller, named subroutines

- **Short name:** Break a long script into smaller blocks
- **Description:** Students identify a script with many statements and refactor it by extracting logical groups into separate custom blocks, each with a clear name. This reduces script complexity and improves readability.
- **Challenge format:** Coding, refactor challenge. Provided: a script with 20+ blocks covering multiple behaviors (e.g., movement, collision, scoring). Prompt: "Refactor this script by creating custom blocks for each major behavior (e.g., 'handle_input', 'update_position', 'check_collisions'). Keep the main script short." Auto‑grading checks that custom blocks are created, used in the main script, and that the main script is substantially shorter.
- **CSTA:** MS‑PRO‑PM‑16, PRO‑TR.

### T12.G7.02 – Analyze readability vs performance trade-offs

- **Short name:** Compare readability and efficiency
- **Description:** Students examine two solutions to the same problem—one more readable but longer, and one more compact but harder to understand—and discuss the trade-off, learning when to prioritize clarity.
- **Challenge format:** Concept, analysis and explanation. Provided: two equivalent code snippets (e.g., a loop with intermediate variables vs a single complex expression). Prompt: "Which is more readable? Why might a programmer choose the longer version?" Auto‑grading uses rubric-based scoring (mentions clarity, ease of debugging, collaboration).
- **CSTA:** MS‑PRO‑PM‑16, MS‑ALG‑AF.

### T12.G7.03 – Create a code review checklist for clarity

- **Short name:** Make a checklist for code review
- **Description:** Students create a checklist of items to look for when reviewing code for clarity and organization (e.g., "Are all variables named clearly?" "Are comments present for complex blocks?" "Is code grouped logically?") and use it to evaluate a peer's or sample project.
- **Challenge format:** Concept and coding. Prompt: "Create a checklist of 5–7 items that help you review code for clarity. Then use it to review a sample project." Auto‑grading checks that the checklist is specific and usable, and that the review identifies real issues in the sample project.
- **CSTA:** MS‑PRO‑PM‑16.

### T12.G7.04 – Document design decisions in code

- **Short name:** Explain why you designed it this way
- **Description:** Students add "design comments" to their code explaining major architectural choices (e.g., "I use a table to store enemy positions so it's easy to add new enemies" or "I use a state variable instead of multiple forever loops to avoid conflicts").
- **Challenge format:** Coding, reflective starter. Provided: a multi-feature project. Prompt: "Add a comment at the top or in a header explaining 2–3 major design choices you made (e.g., how you organized data, why you split scripts the way you did)." Auto‑grading checks that comments exist, reference specific code structures, and explain reasoning.
- **CSTA:** MS‑PRO‑PM‑16.

---

## Grade 8

Grade 8 treats code organization as a professional practice. Students apply industry-like standards for documentation, structure, and readability to more sophisticated projects.

### T12.G8.01 – Apply consistent style across a large project

- **Short name:** Keep style consistent everywhere
- **Description:** Students work on a larger project (5+ scripts, many variables) and ensure consistent naming conventions, comment styles, script organization, and indentation throughout, demonstrating professional code hygiene.
- **Challenge format:** Coding, style audit. Provided or created: a larger project. Prompt: "Review your entire project and ensure: (1) All variables follow the same naming style (camelCase or snake_case), (2) All custom block names use verb phrases, (3) All scripts have header comments, (4) Related code is grouped together." Auto‑grading checks consistency metrics (% of variables following style, presence of comments, script organization).
- **CSTA:** MS‑PRO‑PM‑16.

### T12.G8.02 – Create comprehensive documentation for a complex project

- **Short name:** Write full documentation
- **Description:** Students create a formal documentation guide for a multi-feature project, including: overview, user instructions, code architecture (script purposes and interactions), variable reference, and custom block specifications.
- **Challenge format:** Coding and writing hybrid. Prompt: "Create documentation for your project with these sections: (1) Overview (what the project does), (2) How to use it, (3) Code overview (scripts and their roles), (4) Variables (list and explain key ones), (5) Custom blocks (name and purpose)." Auto‑grading checks section completeness, accuracy (documentation matches code), and clarity. Typically 500+ words.
- **CSTA:** MS‑PRO‑PM‑16.

### T12.G8.03 – Refactor for maintainability in a team context

- **Short name:** Refactor so a team can work on it
- **Description:** Students refactor a project to be modular and well-documented so that team members can work on different features independently, with clear boundaries (separate scripts, well-named custom blocks, commented responsibilities).
- **Challenge format:** Coding and collaboration scenario. Prompt: "Imagine three team members will each work on different features of your game. Refactor your code and documentation so each person can work independently without interfering with others' code. Create a brief task list showing who works on what." Auto‑grading checks modularity (scripts are independent), documentation clarity, and feasibility of parallel work.
- **CSTA:** MS‑PRO‑PM‑16.

### T12.G8.04 – Evaluate and improve code for accessibility and inclusion

- **Short name:** Make code clear for diverse learners
- **Description:** Students examine their code and documentation with an eye toward accessibility and clarity for diverse learners: simple language, explanations of non-obvious choices, alternatives documented, no jargon assumed known.
- **Challenge format:** Concept and coding hybrid. Prompt: "Review your code and documentation. Identify any parts that might confuse someone new to coding or that assume too much prior knowledge. Rewrite or add explanations for clarity." Auto‑grading (often peer or teacher review) assesses whether explanations are genuinely clearer and whether jargon is minimized.
- **CSTA:** MS‑PRO‑PM‑16 (enable collaboration and explain complex logic).
