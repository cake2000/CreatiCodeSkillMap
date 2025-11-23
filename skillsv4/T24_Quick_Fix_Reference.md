# T24 Quick Fix Reference
**Fast navigation for Phase 1 fixes**

---

## AUTO-FIXABLE ISSUES (5 total - Start here!)

### FIX #1: T24.G5.07 - Add Streaming Mode Details
**Line:** 14315-14323
**Current:** Incomplete ChatGPT block syntax
**Action:** Replace description with full parameter details

```markdown
OLD DESCRIPTION:
"Students use the `ChatGPT request [PROMPT] result [VARIABLE]` block to send prompts programmatically and store responses in variables. They build simple projects where AI responses drive sprite behavior or display text. They learn the difference between `session: new chat` (fresh conversation) and `session: continue` (maintains context). They learn to use 'session: new' for independent queries and 'session: continue' to maintain conversation context across multiple XO requests, enabling more sophisticated multi-turn assistance."

NEW DESCRIPTION:
"Students use the `ChatGPT request [PROMPT] result [VARIABLE] mode [streaming/waiting] length [MAXLENGTH] temperature [TEMPERATURE] session [new chat/continue]` block to send prompts programmatically. They learn: (1) Mode - streaming (updates variable with partial responses, ends with ✅) vs waiting (waits for complete response), (2) Length - maximum tokens (100 tokens ≈ 75 words), (3) Temperature - 0-1 scale controlling creativity (0=focused, 1=creative), (4) Session - 'new chat' for independent queries vs 'continue' to maintain context. They build projects comparing streaming UI feedback vs waiting mode."
```

---

### FIX #2: T24.G3.02 - Complete Block Syntax
**Line:** 14152-14160
**Current:** Incomplete block reference
**Action:** Add TYPE parameter to block syntax

```markdown
OLD (line 14155):
"They use the `search for AI image` block to test prompts"

NEW:
"They use the `search for AI image of [TYPE] with query [QUERY]` block to test prompts, selecting appropriate TYPE (Object/Character/Backdrop)"
```

---

### FIX #3: T24.G2.01 - Convert to Demo-Based
**Line:** 14102-14110
**Current:** Block-based coding in Grade 2 (violates K-2 guideline)
**Action:** Convert to teacher demonstration

```markdown
OLD DESCRIPTION:
"Students type short sentences and use the `say [TEXT] in [LANGUAGE]` text-to-speech block to make the computer read their story aloud. They experiment with different sentences to create a mini-narrative, introducing block-based coding with AI features."

NEW DESCRIPTION:
"Students watch a teacher demonstration of the `say [TEXT] in [LANGUAGE]` text-to-speech block reading a story aloud. They suggest sentences to add and observe how the computer speaks them. They compare different voices and languages through guided demonstration. This bridges listening to AI (G1) with coding speech features (G3) through observation rather than hands-on coding."
```

**Also update dependencies:**
- Remove T24.G2.01 as prerequisite from T24.G3.01 (keep T24.G2.04)
- T24.G3.01 can mention "building on G2 demonstration"

---

### FIX #4: Add Table Structure Clarifications
**Affected Skills:** T24.G5.06, G6.05, G7.01, G7.02, G7.03, G7.04, G8.01, G8.02, G8.03, G8.04

**Action #4A: T24.G5.06 (line 14302-14311)**
```markdown
ADD TO END OF DESCRIPTION:
"The analyze sentence block automatically writes results to a CreatiCode table with 7 columns. Students learn to read this structured data by accessing table rows and columns using table blocks to extract specific grammatical information."
```

**Action #4B: T24.G6.05 (line 14396-14407)**
```markdown
MODIFY TABLE DESCRIPTION (line 14399):
OLD: "The table structure includes columns for: timestamp, AI tool used, prompt text, result quality (1-5 rating), and action taken (used/modified/rejected)."

NEW: "Students create a tracking table using CreatiCode table blocks with columns for: timestamp, AI tool used, prompt text, result quality (1-5 rating), and action taken (used/modified/rejected). They use `add row to table` and `set value at row () column () to ()` blocks to maintain structured logs."
```

**Action #4C: Apply similar clarification to G7.01, G7.02, G7.03, G7.04, G8.01, G8.02, G8.03, G8.04**
Add phrase: "Students create [X] table using CreatiCode table blocks" before listing column structure.

---

### FIX #5: Remove X-2 Violations
**Affected Skills:** T24.G7.02, T24.G7.04

**Action #5A: T24.G7.02 (line 14477-14488)**
```markdown
OLD DEPENDENCIES:
* T06.G5.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G5.01: Use if‑else to handle two cases
* T09.G5.04: Use arithmetic and comparison operators with variables
* T24.G6.06: Label risky prompts and rewrite them safely
* T24.G7.01: Create reusable XO prompt templates in lists

NEW DEPENDENCIES:
* T06.G5.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G5.01: Use if‑else to handle two cases
* T09.G5.04: Use arithmetic and comparison operators with variables
* T24.G5.05: Reject unsafe or off-spec XO suggestions
* T24.G7.01: Create reusable XO prompt templates in lists
```
REASON: Skip T24.G6.06, depend directly on T24.G5.05 (same concept, shorter chain)

**Action #5B: T24.G7.04 (line 14503-14514)**
```markdown
OLD DEPENDENCIES:
* T08.G5.01: Use if‑else to handle two cases
* T10.G5.03: Add and remove items from a list
* T24.G6.05: Maintain a prompt/response lab notebook using lists
* T24.G6.06: Label risky prompts and rewrite them safely
* T24.G7.01: Create reusable XO prompt templates in lists

NEW DEPENDENCIES:
* T08.G5.01: Use if‑else to handle two cases
* T10.G5.03: Add and remove items from a list
* T24.G6.05: Maintain a prompt/response lab notebook using lists
* T24.G5.05: Reject unsafe or off-spec XO suggestions
* T24.G7.01: Create reusable XO prompt templates in lists
```
REASON: Skip T24.G6.06, depend directly on T24.G5.05

---

## AUTO-FIX PRIORITY ORDER

1. **Fix #2** (T24.G3.02) - Simple syntax fix
2. **Fix #1** (T24.G5.07) - Important feature clarification
3. **Fix #3** (T24.G2.01) - Grade compliance
4. **Fix #5** (X-2 violations) - Dependency cleanup
5. **Fix #4** (Table clarifications) - Multiple skills

**Total Edits:** ~13 description edits + 2 dependency updates

---

## CRITICAL NEW SKILLS NEEDED (28 total)

### Computer Vision (7 skills)
- **G5.09**: Explore face detection interface
- **G5.10**: Use face position to control sprites
- **G6.10**: Detect hand gestures for game controls
- **G6.11**: Use 2D body tracking for interactive projects
- **G7.07**: Build gesture recognition systems
- **G7.08**: Create full-body pose games with 3D detection
- **G8.06**: Multi-modal AI (vision + ChatGPT)

### Machine Learning (6 skills)
- **G6.12**: Understand classification concepts
- **G7.09**: Create KNN classifiers
- **G7.10**: Build KNN prediction projects
- **G8.07**: Neural network concepts
- **G8.08**: Create NN models
- **G8.09**: Train/validate neural networks (Capstone)

### Semantic Search (3 skills)
- **G7.11**: Semantic search concepts
- **G8.10**: Create semantic databases
- **G8.11**: Semantic search projects (Capstone)

### Web Search (3 skills)
- **G6.13**: Use web search blocks
- **G7.12**: Combine web search + ChatGPT
- **G8.12**: Build research assistant (Capstone)

### Advanced Features (4 skills)
- **G6.14**: ChatGPT vision with costume attachment
- **G7.13**: Attach local files to ChatGPT
- **G8.13**: Google Drive integration
- **G3.00**: Basic speech recognition (scaffolding)

---

## VERIFICATION CHECKLIST

After fixes, verify:
- [ ] All auto-fixable edits completed (5 fixes)
- [ ] T24.G2.01 dependencies updated in G3 skills
- [ ] X-2 rule violations resolved (max 2 grades back)
- [ ] All skill descriptions reference correct block syntax
- [ ] Table structure clarifications added to 10 skills
- [ ] Grade appropriateness (K-2 picture-based, G3+ coding)

---

## MISSING BLOCKS REFERENCE

**Covered:** 27/43 blocks (63%)
**Missing:** 16/43 blocks (37%)

### Missing Categories:
1. **Computer Vision** (16 blocks) - Face, body, hand detection
2. **Machine Learning** (8 blocks) - KNN, neural networks
3. **Semantic Search** (3 blocks) - Vector database, embeddings
4. **Web Search** (1 block) - Real-time information retrieval
5. **File Attachments** (2 blocks) - Local files, Google Drive
6. **Vision Features** (partial) - ChatGPT image analysis

See full analysis in: `T24_Phase1_Analysis_Report.md`

