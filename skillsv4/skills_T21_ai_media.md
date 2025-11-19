# T21 – AI Media: G6–8 Skill List (Draft v2)

Topic reference: `T21 AI Media` in `domains_topics_overview.md`
Domain: CreatiCode-specific AI & Creative Computing · CSTA focus: MS-PRO-PF, MS-PRO-DH, MS-CAS-ET (with links to MS-ALG-HD, MS-CAS-HC)

Each skill below has:

- a stable **ID** (`T21.G<grade>.<nn>`),
- an IXL-style **short name**,
- a **description** (what understanding/behavior it targets),
- a **challenge format** (the typical problem type to assess it).

Where relevant, a primary **CSTA code** is noted.

**Role and scope in v3:** T21 now includes **concept-only Grade 3–5** skills plus **applied Grade 6–8** workflows.  
- G3–5: Picture-/UI-only microsteps that show AI media as a helper, compare AI vs non-AI outputs, and practice safe prompts without touching parameters.  
- G6–8: Applying generative tools in CreatiCode apps: planning asset kits, writing layered prompts, wiring prompt inputs to the DALL-E blocks, iterating when results fail, shipping polished experiences, and documenting ethical guardrails. Theory about diffusion stays elsewhere—T21 is “IXL for shipping AI-powered media workflows.”  
- _AI4K12:_ Humans & AI; Machine Learning (media); Ethical AI Design.

---

## Grade 3–5 (concept-only, no coding)

### T21.G3.01 – Tell whether media was AI-generated or recorded

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.01: Use a counted repeat loop
  * T20.G3.01: Translate art recipe cards into blocks


- **Short name:** Spot AI vs real photos/sounds  
- **Description:** Students compare pairs of images or short sounds (one AI-generated, one recorded) and pick which seems AI-made, explaining clues (odd shadows, repeated textures, robotic voice tone).  
- **Challenge format:** Picture/audio MCQ with short justification; auto-graded.  
- **AI4K12:** A1 Humans & AI; C1 Representation.

### T21.G4.01 – Choose safe and specific prompts for images

_Dependency:_
  * T08.G3.01: Use a simple if in a script
  * T09.G3.04: Trace code with variables to predict outcomes
  * T10.G3.03: Add and remove items from a list
  * T21.G3.01: Tell whether media was AI-generated or recorded


- **Short name:** Improve a vague art request  
- **Description:** Given a vague or risky image request (“make a person” or “draw my house address”), students rewrite it to be specific, safe, and privacy-friendly (e.g., “Draw a friendly robot in a park, daytime”).  
- **Challenge format:** Prompt rewrite + checklist; auto-graded for safety and specificity.  
- **AI4K12:** D1 Ethical AI Design; A3 Human role.

### T21.G5.01 – Plan which assets should be AI-made vs hand-made

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.04: Trace code with variables to predict outcomes
  * T10.G3.03: Add and remove items from a list


- **Short name:** Pick AI vs handmade for a project kit  
- **Description:** Students see a simple app pitch (storybook, quiz) and choose which assets to request from AI (e.g., varied backdrops) and which to make by hand (e.g., main character for consistent look), noting one reason for each choice.  
- **Challenge format:** Drag to AI vs Hand bins + short rationale; auto-graded.  
- **AI4K12:** A2 Capabilities & Limits; E1 Societal Impacts.

---

## Grade 6

Grade 6 students move from “AI makes pretty pictures” to “AI supplies assets that satisfy a design brief.” They plan which sprites or UI panels benefit from AI, write layered prompts, and build small interfaces that test multiple results before committing one to a project.

### T21.G6.01 – Plan a mixed-source asset kit for a project

_Dependency:_
  * T08.G3.01: Use a simple if in a script
  * T09.G3.04: Trace code with variables to predict outcomes
  * T10.G3.03: Add and remove items from a list
  * T21.G4.01: Choose safe and specific prompts for images
  * T21.G5.01: Plan which assets should be AI-made vs hand-made


- **Short name:** Decide which assets should be AI-generated
- **Description:** Students map every sprite costume, backdrop, UI panel, and audio clip in a planned game/app, categorize each as “AI-generated,” “hand-created,” or “remix/library,” and justify their choice (e.g., “AI for backgrounds because we need ten fast variants, but we’ll draw the mascot so it matches the story”). This reinforces the human role in directing AI.
- **Challenge format:** Concept, structured design brief. Learners complete a planning grid with at least 8 assets, tagging source, required style, and responsible teammate. Auto-grading checks that all major screens are covered and every AI asset has a rationale.
- **CSTA:** MS-ALG-HD-03, MS-PRO-PM-03.

### T21.G6.02 – Write layered prompts that lock in a visual style

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.04: Trace code with variables to predict outcomes
  * T10.G3.03: Add and remove items from a list
  * T21.G5.01: Plan which assets should be AI-made vs hand-made


- **Short name:** Add subject, style, color, and camera details to prompts
- **Description:** Students turn vague prompt starters (e.g., “dragon in a cave”) into structured prompts that include subject, action, camera angle, palette, and mood so the resulting art matches UI expectations. They learn to reuse the same structure for multiple assets to keep scenes consistent.
- **Challenge format:** Concept + applied writing. For three creative briefs, students rewrite simple prompts into detailed ones, highlighting each component (subject, action, medium, palette) and explaining why it matters. Auto-grading checks for the required components and logical alignment with the brief.
- **CSTA:** MS-PRO-PF-02, MS-ALG-HD-04.

### T21.G6.03 – Build a prompt test bench inside CreatiCode

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.04: Trace code with variables to predict outcomes
  * T10.G3.03: Add and remove items from a list
  * T21.G5.01: Plan which assets should be AI-made vs hand-made


- **Short name:** Create a UI to try and capture AI art
- **Description:** Students design a screen with a text input, dropdown style selector, and gallery of preview sprites. Pressing a “Generate” button triggers the `OpenAI DALL-E: generate costume image` block, loads three variations, and logs each prompt + URL in a table so the designer can choose a winner.
- **Challenge format:** Coding, guided build. Starter project contains the widgets; students implement the logic to (1) read the prompt, (2) request three images at different resolutions, (3) label thumbnails with the prompt text, and (4) let the user click “Use this one” to copy the costume into the final sprite. Auto-grading simulates prompt entries and checks that data logging and selection work.
- **CSTA:** MS-PRO-PF-01, MS-PRO-DH-04.

### T21.G6.04 – Iterate when an AI output fails requirements

_Dependency:_
  * T07.G3.01: Use a counted repeat loop
  * T08.G3.01: Use a simple if in a script
  * T09.G3.04: Trace code with variables to predict outcomes
  * T10.G3.03: Add and remove items from a list
  * T21.G5.01: Plan which assets should be AI-made vs hand-made


- **Short name:** Diagnose why the image missed the brief and fix it
- **Description:** Students practice reading a failed generation (wrong colors, missing character, awkward proportions), identifying the cause (prompt missing detail, wrong style, conflicting terms), and rewriting the prompt to address the issue. They compare “before/after” versions to show how iteration improves fit.
- **Challenge format:** Coding + debugging task. Given a CreatiCode project with three flawed AI backdrops and original prompts, students annotate each issue, craft a revised prompt, regenerate, and explain why the fix worked. Auto-grading checks that revisions address the named problems and that regenerated assets meet constraints (e.g., contains tagged colors).
- **CSTA:** MS-PRO-TR-11.

---

## Grade 7

Grade 7 students orchestrate entire AI media pipelines: they capture art direction in data structures, call both ChatGPT and DALL-E blocks, test for bias, and blend AI imagery with manual edits and narration so it fits polished experiences.

### T21.G7.01 – Create a reusable prompt template library

_Dependency:_
  * T07.G3.01: Use a counted repeat loop
  * T09.G3.04: Trace code with variables to predict outcomes
  * T10.G3.03: Add and remove items from a list
  * T21.G6.03: Build a prompt test bench inside CreatiCode
  * T21.G6.04: Iterate when an AI output fails requirements


- **Short name:** Store style rules in a table and auto-generate assets
- **Description:** Students build a CreatiCode table with columns such as `subject`, `palette`, `camera`, `lighting`, and `tone`. A loop reads each row, assembles the prompt using placeholders, calls DALL-E, and records the returned costume name + URL. This ensures a whole level or comic chapter shares the same art direction.
- **Challenge format:** Coding, data-driven project. Provided starter code loads a half-filled table. Students finish the prompt-assembly block, loop through all rows, and push finished metadata (prompt, costume, approval flag) back into the table. Auto-grading confirms that every row yields an asset and that prompts follow the template exactly.
- **CSTA:** MS-PRO-DH-04, MS-PRO-PD-08.

### T21.G7.02 – Use ChatGPT to expand briefs before generating art

_Dependency:_
  * T08.G3.01: Use a simple if in a script
  * T09.G3.04: Trace code with variables to predict outcomes
  * T10.G3.03: Add and remove items from a list
  * T21.G6.03: Build a prompt test bench inside CreatiCode
  * T21.G6.04: Iterate when an AI output fails requirements


- **Short name:** Chain a text prompt designer with the image block
- **Description:** Students combine the ChatGPT block (system message + role prompt) with DALL-E. ChatGPT converts a story outline into a set of polished prompts (e.g., “Scene 3: aerial view of neon market, magenta lighting”), then each prompt feeds the image block. Students compare raw vs. AI-enhanced prompts to see the quality jump.
- **Challenge format:** Coding, multi-block pipeline. Learners build a “Generate storyboard” button that (1) sends the story synopsis to ChatGPT, (2) parses the returned list into individual prompts, and (3) loops through them to produce costumes for each screen. Auto-grading checks that ChatGPT output is stored, parsed, and that every prompt leads to an imported costume.
- **CSTA:** MS-PRO-PF-02, MS-ALG-HD-04.

### T21.G7.03 – Audit AI imagery for representation and bias

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.01: Use a counted repeat loop
  * T08.G3.01: Use a simple if in a script
  * T09.G3.04: Trace code with variables to predict outcomes
  * T10.G3.03: Add and remove items from a list
  * T21.G6.03: Build a prompt test bench inside CreatiCode
  * T21.G6.04: Iterate when an AI output fails requirements


- **Short name:** Check whether prompts return diverse characters
- **Description:** Students design experiments (e.g., run “a scientist giving a talk” 10 times) and log characteristics (perceived gender, culture, age) into a table. They graph the distribution, identify gaps, and adjust prompts (adding descriptors, requesting diversity) to reach targeted representation goals, highlighting AI4K12’s focus on societal impact.
- **Challenge format:** Concept + coding investigation. Provided logging code writes metadata into a table; students add their measurement categories, run at least 20 generations, then visualize results using charts or reporter blocks. They submit a short reflection describing changes made to close gaps. Auto-grading checks that data collection exceeds the threshold and that revised prompts shift the distribution.
- **CSTA:** MS-CAS-ET-05, MS-PRO-TR-13.

### T21.G7.04 – Blend AI frames with manual touch-ups for animation

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T08.G3.01: Use a simple if in a script
  * T09.G3.04: Trace code with variables to predict outcomes
  * T10.G3.03: Add and remove items from a list
  * T21.G6.04: Iterate when an AI output fails requirements


- **Short name:** Combine AI images and hand edits into smooth motion
- **Description:** Students import AI-generated poses for a character, then fix artifacts (hands, faces, edges) using the costume editor or vector tools. They align all frames with equal sizing and anchor points, then script a timed animation that matches UI state (buttons, HUD cues) from T16.
- **Challenge format:** Coding + art workflow. Learners receive four raw AI frames; they must clean them, tag them in order, and code a `broadcast`-based animation that plays when a UI button is pressed. Auto-grading inspects costume names, checks for consistent sizes, and verifies animation speed/events.
- **CSTA:** MS-PRO-PF-02, MS-PRO-TR-12.

### T21.G7.05 – Pair AI visuals with AI narration for immersive scenes

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.04: Trace code with variables to predict outcomes
  * T10.G3.03: Add and remove items from a list
  * T21.G6.04: Iterate when an AI output fails requirements


- **Short name:** Generate images and matching voiceovers from one brief
- **Description:** Students start with a lore snippet, feed it to ChatGPT to craft narration, use `OpenAI DALL-E` for visuals, and convert the narration to speech via `say [TEXT] in [LANGUAGE]` AI block. They align cues so that the voiceover references what is on screen, reinforcing cross-modal coherence.
- **Challenge format:** Coding, multimedia build. Starter sprites hold placeholder art. Students write scripts that (1) produce the narration, (2) trigger image generation, (3) preload the audio clip, and (4) play them in sync when the user taps a widget. Auto-grading checks for synchronized timing and that prompts/audio trace back to the same brief stored in variables.
- **CSTA:** MS-PRO-PF-02, MS-CAS-ET-07.

---

## Grade 8

Grade 8 students deliver production-ready AI media systems. They let end users request art safely, maintain approval pipelines, coordinate multi-modal kits (visuals, narration, UI skins), and articulate ethical guardrails for their studio or class.

### T21.G8.01 – Build a user-facing generative art widget with guardrails

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T08.G3.01: Use a simple if in a script
  * T09.G3.04: Trace code with variables to predict outcomes
  * T10.G3.03: Add and remove items from a list
  * T21.G7.04: Blend AI frames with manual touch-ups for animation


- **Short name:** Let players request new scenes safely
- **Description:** Students design an in-app panel (text field, preset buttons, preview box) where users can request a fresh background. The script moderates the prompt with `get moderation result`, applies house style presets, runs DALL-E, and falls back to curated art if moderation fails. Users can save approved scenes to a gallery.
- **Challenge format:** Coding, full-stack feature. Prompt sanitization, asynchronous image loading, and gallery storage must all work. Auto-grading sends multiple prompts (clean + disallowed) and verifies that unsafe prompts are blocked, safe prompts generate art, and saved scenes persist in a list/table for later use.
- **CSTA:** MS-PRO-PF-02, MS-PRO-TR-12.

### T21.G8.02 – Implement an approval pipeline for AI assets

_Dependency:_
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.04: Trace code with variables to predict outcomes
  * T10.G3.03: Add and remove items from a list
  * T21.G7.04: Blend AI frames with manual touch-ups for animation


- **Short name:** Track prompts, moderation, reviewers, and publish state
- **Description:** Students build a dashboard that lists each generated asset with metadata: prompt, author, moderation result, reviewer notes, and publish toggle. Only assets with “Approved” checked become visible in the live scene. This mirrors professional workflows and enforces accountability.
- **Challenge format:** Coding + data management. Starter data table contains sample rows; students wire the UI (checkboxes, dropdowns) to update the table, display statuses, and block unapproved art from loading. Auto-grading manipulates entries to ensure that only approved assets render and that metadata updates persist.
- **CSTA:** MS-PRO-DH-04, MS-PRO-PM-03.

### T21.G8.03 – Produce a multi-modal media kit from one creative brief

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T09.G3.04: Trace code with variables to predict outcomes
  * T10.G3.03: Add and remove items from a list
  * T21.G7.04: Blend AI frames with manual touch-ups for animation
  * T21.G7.05: Pair AI visuals with AI narration for immersive scenes


- **Short name:** Keep story, art, and narration aligned
- **Description:** Students receive a short creative brief (setting, emotional arc). They instruct ChatGPT to output scene-by-scene descriptions, DALL-E to produce matching art, and AI TTS to narrate each beat. They integrate everything into a multi-screen experience where UI widgets trigger synchronized visuals + audio.
- **Challenge format:** Coding, capstone sequence. Students implement arrays/lists to keep each scene’s text, image, and audio in lockstep, and prove that clicking “Next” advances all assets together. Auto-grading steps through the scenes to confirm synchronization and data integrity.
- **CSTA:** MS-PRO-PF-02, MS-ALG-HD-04.

### T21.G8.04 – Develop ethical guidelines for AI media use in a studio

_Dependency:_
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.04: Trace code with variables to predict outcomes
  * T10.G3.03: Add and remove items from a list
  * T21.G7.04: Blend AI frames with manual touch-ups for animation


- **Short name:** Write and defend an AI art policy
- **Description:** Students research a real example (e.g., a game studio using AI concept art), identify stakeholder concerns (artists, players, communities referenced), and draft a policy describing disclosure, credit, data sourcing, and escalation paths. They tie recommendations to in-class workflows (moderation logs, approvals) to show accountability.
- **Challenge format:** Concept, policy memo + presentation. Learners submit a short document plus a slide or video pitch summarizing their guardrails, referencing evidence from their own project logs. Auto-grading (rubric) looks for stakeholder analysis, concrete rules, and alignment with AI4K12 priorities about societal impact and human oversight.
- **CSTA:** MS-CAS-ET-06, MS-CAS-HC-02.

---
