# T24 – XO & Generative AI Practices: G5–8 Skill List (Draft v2)

Topic reference: `T24 XO & AI Practices` in `domains_topics_overview.md`
Domain: CreatiCode-specific AI enablement · CSTA focus: E5–MS PRO‑PM, PRO‑PF, PRO‑TR, CAS‑ET (with links to DAA‑DF, ALG‑HD)

Each skill below has:

- a stable **ID** (`T24.G<grade>.<nn>`),
- an IXL‑style **short name**,
- a **description** (what understanding/behavior it targets),
- a **challenge format** (the typical problem type to assess it).

Where relevant, a primary **CSTA code** is noted.

**Role and scope in v3:** XO is CreatiCode’s built-in AI teammate and the quickest way for students to brainstorm, plan, debug, and fact-check their own projects. T24 starts in Grade 5, when students can read multi-sentence answers and follow instructions. The topic also covers CreatiCode’s AI image generator/search blocks because planning conversations often flow directly into asset creation. Focus is on *prompt craftsmanship, verification, and ethical guardrails*—students learn how to describe intent clearly, cross-check XO’s suggestions, document prompt/result logs, and decide when to rely on AI versus their own reasoning. Theory about how LLMs or diffusion models work lives elsewhere; here we deliver “IXL-style reps” for using XO and image tools effectively inside real coding workflows.  
- _AI4K12:_ Humans & AI; Ethical AI Design; Societal Impacts.

---

## Grade 5

Grade 5 introduces XO as a reading-heavy helper. Students learn the interface, practice writing concise prompts, follow XO plans, and connect those plans to AI-generated assets.

### T24.G5.01 – Read and interpret XO’s interface cues

- **Short name:** Understand XO panels and buttons
- **Description:** Students explore XO’s chat area, template prompts, code/explanation tabs, and “insert into project” buttons. They learn how to pause, copy, and pin answers for later. This reduces friction before they start asking for help.
- **Challenge format:** Guided walkthrough. Learners receive a screenshot with labels removed and must drag labels (Prompt Box, Code Preview, Regenerate, Library) to the correct UI elements. Auto-grading checks correct placement and a short reflection (“Which button inserts code?”).
- **CSTA:** E5-PRO-PM-01.

### T24.G5.02 – Ask XO for a three-step project plan

- **Short name:** Get XO to list steps for your idea
- **Description:** Students practice writing a structured prompt (goal + constraints + audience) so XO replies with a numbered plan. They verify the plan covers at least three concrete actions (e.g., “draw sprite,” “add `when green flag clicked`,” “show score label”).
- **Challenge format:** Prompt-writing exercise. Learners complete a template: “I’m building __. It should include __. Please give me __ steps.” XO’s reply appears; students highlight the three steps they will follow and explain why one step comes first. Auto-grading checks prompt completeness and that selected steps match the plan.
- **CSTA:** E5-PRO-PM-04, E5-PRO-PM-05.

### T24.G5.03 – Turn an XO suggestion into starter code safely

- **Short name:** Copy XO blocks and check them
- **Description:** Students copy a short script provided by XO (e.g., movement loop) into their project, but before running it they verify variables/events exist and annotate what each block does. This builds the habit of reading AI output before trusting it.
- **Challenge format:** Coding + checklist. XO replies with block code containing placeholders. Students import it into a starter project, replace placeholder names, and complete a two-column checklist (Does the variable exist? Does the event match?). Auto-grading inspects the final script for correct names and requires the completed checklist text.
- **CSTA:** E5-PRO-TR-01, E5-PRO-PF-01.

### T24.G5.04 – Use the AI image library to collect matching assets

- **Short name:** Search/generate sprites with prompts from XO
- **Description:** Students take XO’s narrative description (e.g., “Journey of a Waterdrop” scene) and convert it into AI image search/generation prompts for backdrops and sprites. They compare options and justify why each asset matches the plan.
- **Challenge format:** Coding + curation. Learners paste XO’s text into the “search for AI image” block, generate at least two candidates, screenshot the results, and rate them on a rubric (clarity, transparency, scale). Auto-grading checks that prompts include subject + style descriptors and that chosen assets are tagged with rationale statements.
- **CSTA:** E5-PRO-PM-04, CAS-ET-02.

### T24.G5.05 – Reject unsafe or off-spec XO suggestions

- **Short name:** Spot and refuse risky answers  
- **Description:** Students review an XO reply that includes off-task, private, or non-compliant steps (e.g., “ask a friend for their password,” “skip testing”) and practice declining it. They write a replacement step that follows the rubric/spec and log why the original was rejected.  
- **Challenge format:** Concept + checklist. Provided XO transcript with 2–3 issues. Learners highlight risky lines, write a corrected step, and tick a safety checklist (no private data, follows requirements). Auto-grading checks that flagged issues match the transcript and that a replacement step is provided.  
- **CSTA:** E5-PRO-PM-04, CAS-ET-02.

---

## Grade 6

Grade 6 students use XO for debugging, quizzes, and iteration. They learn to provide context, confirm AI answers independently, and document prompt/result logs for peer review.

### T24.G6.01 – Provide complete context when asking XO to debug

- **Short name:** Give XO the error, code, and goal
- **Description:** Students assemble a “debug packet” with the bug description, relevant script, and what they expected. XO returns a fix; students evaluate whether it addresses the issue and annotate any manual tweaks.
- **Challenge format:** Coding, structured submission. Starter project intentionally misuses a variable. Learners fill a form (What happened? Which blocks?) and send it to XO. After receiving the suggestion, they update the code and complete a checklist (“XO fix applied?” “Extra edits?”). Auto-grading compares before/after scripts and checks that the debug packet fields are filled.
- **CSTA:** MS-PRO-TR-11.

### T24.G6.02 – Verify XO’s explanation against the project

- **Short name:** Fact-check XO before accepting advice
- **Description:** Students ask XO “Explain how this script works,” then compare the explanation to the actual code. They highlight any mismatches (missing variable, wrong loop) and either accept or correct the AI explanation.
- **Challenge format:** Concept + evidence. Learners receive XO’s paragraph plus the real script. They annotate true statements in green and corrections in red, then rewrite a concise summary. Auto-grading checks for at least two validated statements and one correction when XO is wrong.
- **CSTA:** MS-PRO-PF-01, MS-PRO-TR-12.

### T24.G6.03 – Generate and deliver a quiz using XO

- **Short name:** Let XO build practice questions, you review them
- **Description:** Students prompt XO for three multiple-choice questions about a chosen topic (loops, events), then vet each question for clarity and accuracy before sharing it with classmates via widgets.
- **Challenge format:** Coding + UI. Learners ask XO for questions, edit wording if needed, then populate a quiz interface. Auto-grading checks that (1) XO is credited, (2) each question includes an answer key verified by the student, and (3) the quiz UI records scores.
- **CSTA:** MS-PRO-PM-03, MS-PRO-PF-02.

### T24.G6.04 – Iterate AI images using feedback from XO

- **Short name:** Use XO critiques to improve generated art
- **Description:** Students upload an AI-generated backdrop to XO, ask for improvement ideas (e.g., “What should I change to make it look stormy?”), then modify the prompt and regenerate. They compare before/after results and note which prompt edits caused the change.
- **Challenge format:** Coding + reflection. Learners submit original prompt + image, XO feedback, revised prompt, and final image in a table. Auto-grading checks that revisions reflect XO advice and that the final image differs in specified attributes (color palette, mood).
- **CSTA:** MS-CAS-ET-05, MS-PRO-PF-02.

### T24.G6.05 – Maintain a prompt/response lab notebook

- **Short name:** Log XO and image prompts with outcomes
- **Description:** Students keep a table (date, tool, prompt, result quality, action taken). They review the log weekly to spot patterns (e.g., “long prompts give better responses”). This builds metacognitive habits.
- **Challenge format:** Concept + data. Provided template includes 10 rows. Students fill at least five entries, categorize outcome quality, and write one insight. Auto-grading verifies entries have all fields and that the insight references log data.
- **CSTA:** MS-PRO-PM-03, MS-DAA-DF-02.

### T24.G6.06 – Label risky prompts and rewrite them safely

- **Short name:** Fix risky XO requests  
- **Description:** Students examine sample prompts that leak private info, copy code wholesale, or ask XO to skip grading criteria. They classify each as “safe” or “risky,” then rewrite risky ones to remove private data and align to the rubric while keeping the learning goal.  
- **Challenge format:** Concept + rewrite. Learners drag prompts into Safe/Risky bins, then edit the risky prompts inline (e.g., replace “copy the whole answer” with “explain how to start” and remove names). Auto-grading checks bin placement and that rewrites eliminate the risk phrases.  
- **CSTA:** MS-CAS-ET-06, MS-PRO-PM-03.

---

## Grade 7

Grade 7 work centers on orchestrating XO as a teammate: chaining prompts, enforcing ethical guidelines, and combining XO text with AI art across multi-screen apps.

### T24.G7.01 – Create reusable XO prompt macros

- **Short name:** Build prompt templates for recurring tasks
- **Description:** Students design templates (e.g., “Code Review Macro,” “Project Outline Macro”) with placeholders for sprites, variables, and goals. They store these in a CreatiCode list so they can quickly paste the right structure into XO.
- **Challenge format:** Coding + documentation. Learners create at least two macros, document when to use them, and demonstrate each inside XO with a real request. Auto-grading inspects the macro list and the resulting XO transcripts to ensure placeholders were replaced correctly.
- **CSTA:** MS-PRO-PD-08, MS-PRO-PF-02.

### T24.G7.02 – Run an XO-led code review with evidence

- **Short name:** XO finds issues, you confirm them
- **Description:** Students paste a medium script into XO and ask for “3 improvements.” They then inspect each suggestion, either implementing it or rejecting it with justification (performance, readability, game design).
- **Challenge format:** Coding + rubric. Learners submit side-by-side: XO suggestion, decision (accept/reject), evidence (line reference). Auto-grading checks that all three suggestions were addressed and that accepted changes appear in the final code. Rubric scoring rewards well-supported rejections.
- **CSTA:** MS-PRO-TR-12, MS-PRO-PF-02.

### T24.G7.03 – Combine XO storyboards with AI sprite generation

- **Short name:** XO writes the scene list, AI draws it
- **Description:** Students ask XO for a storyboard (scene descriptions + characters) for a themed project, then generate sprites/backdrops for each scene via the AI image blocks. They document alignment between text and visuals.
- **Challenge format:** Coding, multi-screen build. Learners submit a table linking XO scene text, prompt used for generation, final asset, and how it’s used in the project. Auto-grading checks that each scene has a matching asset and that the prompts contain style cues specified by XO (e.g., “misty forest”).
- **CSTA:** MS-PRO-PM-03, MS-CAS-ET-07.

### T24.G7.04 – Enforce responsible-use rules for XO assistance

- **Short name:** Track credits, sources, and human review
- **Description:** Students implement an “AI Help” log inside their project (a hidden list or widget) that records each XO contribution, who reviewed it, and whether it was modified. They also add on-screen indicators telling players when AI-generated art/text appears.
- **Challenge format:** Coding + ethics. Learners add logging scripts and visible disclosures (e.g., “Level art generated with CreatiCode AI”). Auto-grading inspects the log for at least five entries with reviewer initials and ensures the disclosure widget is visible before gameplay starts.
- **CSTA:** MS-CAS-ET-06, MS-PRO-PM-03.

### T24.G7.05 – Use XO to coach peers with rubric-based feedback

- **Short name:** XO drafts feedback, you personalize it
- **Description:** Students feed XO a project summary and ask for constructive feedback. They then edit the response to match a class rubric (naming strengths, next steps) before sending it to a peer. This reinforces human oversight and empathy.
- **Challenge format:** Concept + writing. Learners submit XO’s raw feedback, their edited version, and a checklist showing rubric alignment. Auto-grading checks for meaningful edits (not just copy-paste) and references to the peer’s actual project.
- **CSTA:** MS-CAS-ET-05, MS-PRO-PM-03.

---

## Grade 8

Grade 8 students operationalize XO/image workflows like a studio: they build automation around prompts, integrate testing, and document policies for human-AI collaboration.

### T24.G8.01 – Automate XO requests with data-driven prompt builders

- **Short name:** Generate prompts from tables
- **Description:** Students store project metadata (sprite name, mechanic, constraint) in a table and build scripts that concatenate those fields into structured XO prompts. Pressing a widget button copies the prompt for immediate use.
- **Challenge format:** Coding, data automation. Learners implement a “Prompt Builder” UI: select a row, click “Copy Prompt,” and paste into XO. Auto-grading checks that prompts include all required fields and that the script updates when the table changes.
- **CSTA:** MS-PRO-DH-04, MS-PRO-PD-08.

### T24.G8.02 – Pair XO with automated tests to validate fixes

- **Short name:** Ask XO to fix code, run tests, iterate
- **Description:** Students write a small automated test harness (assertions or monitoring variables). They then prompt XO for a fix, apply it, run the tests, and report whether the fix passed. If not, they loop with refined prompts until the tests succeed.
- **Challenge format:** Coding + QA. Provided tests fail initially. Learners document each iteration: prompt, XO suggestion, test result, next action. Auto-grading checks that at least two iterations occur and that the final code passes all provided tests.
- **CSTA:** MS-PRO-TR-12, MS-PRO-PF-02.

### T24.G8.03 – Compare XO-generated code/image options with human-crafted versions

- **Short name:** Run A/B comparisons of AI vs. you
- **Description:** Students implement two versions of a feature or asset: one produced with XO/AI image tool, one produced manually. They create metrics (lines of code, frame rate, user preference) and analyze tradeoffs.
- **Challenge format:** Concept + data. Learners build a comparison screen showing both versions, run user tests, and log results in a table. Auto-grading verifies that metrics are recorded and that the written analysis cites those metrics.
- **CSTA:** MS-CAS-ET-05, MS-PRO-PM-03.

### T24.G8.04 – Draft a studio policy for XO/image usage

- **Short name:** Formalize how your team uses AI help
- **Description:** Students synthesize experience from logs/tests to write a two-page policy covering: approved use cases, citation requirements, bias monitoring, privacy of prompt logs, and human override procedures. They relate rules to AI4K12 priorities (human role, societal impact).
- **Challenge format:** Concept, policy memo. Learners submit the policy plus a short presentation referencing their own log data or comparisons. Rubric scoring checks for stakeholder analysis, concrete procedures, and explicit ties to class projects.
- **CSTA:** MS-CAS-HC-02, MS-CAS-ET-06.

### T24.G8.05 – Mentor younger students on XO best practices

- **Short name:** Teach Grade 5/6 peers how to prompt responsibly
- **Description:** Students design a mini-workshop (slide deck or interactive demo) that trains younger peers on one XO workflow (planning, debugging, image iteration). They gather questions from the audience and document how they adjusted their guidance.
- **Challenge format:** Concept + facilitation. Learners submit workshop materials, a list of peer questions, and a reflection on what they changed mid-session. Auto-grading checks that materials include screenshots of XO, that questions were actually captured, and that reflections mention at least one improvement.
- **CSTA:** MS-PRO-PM-04, CAS-ET-06.

---
