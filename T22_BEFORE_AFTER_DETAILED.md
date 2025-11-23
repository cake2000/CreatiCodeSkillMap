# T22 Before/After Detailed Comparison

## Overview
This document shows the exact changes made to T22 skills, highlighting the differences.

---

## CHANGE 1: T22.G5.1.5 → T22.G5.04

### BEFORE (Invalid ID Format)
```
ID: T22.G5.1.5
Topic: T22 – Chatbots & Prompting
Skill: Use a chatbot block to get AI responses
Description: Students use the basic `OpenAI ChatGPT: request [PROMPT] result [VARIABLE]`
block to send a simple message to ChatGPT and store the response in a variable. They build
a minimal project that displays the AI's answer on the stage, learning the fundamental
mechanics of making an AI request before exploring advanced features.

Dependencies:
* T09.G4.01: Build a simple string variable for name entry
* T22.G5.01: Flag risky vs safe chatbot prompts
* T22.G5.03: Experiment with prompt phrasing to improve responses
```

### AFTER (Fixed ID, Proper Position)
```
ID: T22.G5.04
Topic: T22 – Chatbots & Prompting
Skill: Use a chatbot block to get AI responses
Description: Students use the basic `OpenAI ChatGPT: request [PROMPT] result [VARIABLE]`
block to send a simple message to ChatGPT and store the response in a variable. They build
a minimal project that displays the AI's answer on the stage, learning the fundamental
mechanics of making an AI request before exploring advanced features.

Dependencies:
* T09.G4.01: Build a simple string variable for name entry
* T22.G5.01: Flag risky vs safe chatbot prompts
* T22.G5.03: Experiment with prompt phrasing to improve responses
```

**Changes**:
- ✅ ID: T22.G5.1.5 → T22.G5.04 (fixed invalid format)
- ✅ Position: Moved from end of G5 to 4th position (logical)
- ⚪ Description: Unchanged (already well-written)
- ⚪ Dependencies: Unchanged (correct)

**Reason**: The ID "T22.G5.1.5" used dot notation which violates the standard format. Additionally, this is a foundational skill that should come before the parameter observation skill.

---

## CHANGE 2: T22.G5.04 → T22.G5.05

### BEFORE
```
ID: T22.G5.04
Topic: T22 – Chatbots & Prompting
Skill: Identify ChatGPT block parameters in starter code
Description: Students examine a simple CreatiCode project using the ChatGPT block and
identify what each parameter does (mode, temperature, max length, session). They don't
modify the code yet, but label screenshots showing where each parameter is and predict
what happens if values change. This prepares them for tracing more complex scripts in G6.

Dependencies:
* T22.G5.1.5: Use a chatbot block to get AI responses
* T22.G5.02: Observe chatbot strengths and weaknesses through testing
```

### AFTER
```
ID: T22.G5.05
Topic: T22 – Chatbots & Prompting
Skill: Identify ChatGPT block parameters in starter code
Description: Students examine a simple CreatiCode project using the ChatGPT block and
identify what each parameter does (mode, temperature, max length, session). They don't
modify the code yet, but label screenshots showing where each parameter is and predict
what happens if values change. This prepares them for tracing more complex scripts in G6.

Dependencies:
* T22.G5.02: Observe chatbot strengths and weaknesses through testing
* T22.G5.04: Use a chatbot block to get AI responses
```

**Changes**:
- ✅ ID: T22.G5.04 → T22.G5.05 (renumbered)
- ⚪ Description: Unchanged (already well-written)
- ✅ Dependencies: Updated T22.G5.1.5 → T22.G5.04, reordered for clarity

**Reason**: Renumbered to make room for the foundational chatbot block skill (now G5.04). Fixed dependency reference from invalid ID.

---

## CHANGE 3: T22.G6.05.5 → T22.G6.05

### BEFORE (Invalid ID, Conceptual)
```
ID: T22.G6.05.5
Topic: T22 – Chatbots & Prompting
Skill: Understand chatbot session types
Description: Students learn the difference between single-turn requests (independent
questions) and multi-turn conversations (maintaining context across exchanges). They
identify when to use the basic request block versus when to manage sessions with the
session parameter, understanding how context affects chatbot responses.

Dependencies:
* T22.G6.01: Trace how a chatbot script processes each turn
* T22.G6.02: Adjust temperature for response creativity
* T22.G6.03: Handle streaming mode and long requests
```

### AFTER (Fixed ID, Hands-On Implementation)
```
ID: T22.G6.05
Topic: T22 – Chatbots & Prompting
Skill: Implement session management for multi-turn conversations
Description: Students compare single-turn requests (independent questions) to multi-turn
conversations (maintaining context across exchanges). They use the session parameter to
maintain conversation context and build a project that demonstrates when context helps
vs. when it causes confusion. They implement a "New Chat" button to clear session history.

Dependencies:
* T22.G6.01: Trace how a chatbot script processes each turn
* T22.G6.02: Adjust temperature for response creativity
* T22.G6.03: Handle streaming mode and long requests
```

**Changes**:
- ✅ ID: T22.G6.05.5 → T22.G6.05 (fixed invalid format)
- ✅ Title: "Understand chatbot session types" → "Implement session management for multi-turn conversations"
- ✅ Description: Enhanced from passive observation to active implementation
- ⚪ Dependencies: Unchanged (correct)

**Detailed Description Changes**:

| Aspect | Before | After |
|--------|--------|-------|
| Action Verbs | "learn", "identify", "understanding" | "compare", "use", "build", "implement" |
| Deliverable | Implied understanding | Explicit: "build a project", "implement 'New Chat' button" |
| Focus | Conceptual (what are sessions) | Practical (how to use sessions) |
| Grade Level | Too passive for G6 | Appropriate hands-on for G6 |

**Reason**: The ID violated standard format. The skill was too conceptual for Grade 6 - students should be implementing, not just understanding. Enhanced to include specific deliverables.

---

## DEPENDENCY UPDATE 1: T22.G6.01

### BEFORE
```
Dependencies:
* T06.G4.01: Program multiple events to run independently
* T08.G4.01: Use nested conditions or multi-branch selection
* T09.G4.01: Build a simple string variable for name entry
* T09.G4.04: Trace multi-step expressions with parentheses
* T22.G5.01: Flag risky vs safe chatbot prompts
* T22.G5.04: Identify ChatGPT block parameters in starter code
```

### AFTER
```
Dependencies:
* T06.G4.01: Program multiple events to run independently
* T08.G4.01: Use nested conditions or multi-branch selection
* T09.G4.01: Build a simple string variable for name entry
* T09.G4.04: Trace multi-step expressions with parentheses
* T22.G5.01: Flag risky vs safe chatbot prompts
* T22.G5.05: Identify ChatGPT block parameters in starter code
```

**Change**: T22.G5.04 → T22.G5.05 (updated reference to renumbered skill)

---

## DEPENDENCY UPDATE 2: T22.G6.04.01

### BEFORE
```
Dependencies:
* T16.G3.01: Add a button widget to the stage
* T16.G3.05: Add a textbox widget for user input
* T22.G5.1.5: Use a chatbot block to get AI responses
```

### AFTER
```
Dependencies:
* T16.G3.01: Add a button widget to the stage
* T16.G3.05: Add a textbox widget for user input
* T22.G5.04: Use a chatbot block to get AI responses
```

**Change**: T22.G5.1.5 → T22.G5.04 (updated reference to corrected ID)

---

## SKILLS THAT DID NOT CHANGE (35 skills)

All other skills remained exactly as they were:

### Kindergarten (2 skills)
- T22.GK.01: Recognize a talking helper vs a silent toy
- T22.GK.02: Practice asking a picture helper a friendly question

### Grade 1 (2 skills)
- T22.G1.01: Sort good questions from confusing questions
- T22.G1.02: Identify what a chatbot might not know

### Grade 2 (2 skills)
- T22.G2.01: Role-play asking a helper for information
- T22.G2.02: Decide which questions are okay to ask a helper

### Grade 3 (1 skill)
- T22.G3.01: Identify chatbot behavior from fixed button replies

### Grade 4 (1 skill)
- T22.G4.01: Write clear, polite questions for a helper bot

### Grade 5 (2 skills unchanged)
- T22.G5.01: Flag risky vs safe chatbot prompts
- T22.G5.02: Observe chatbot strengths and weaknesses through testing
- T22.G5.03: Experiment with prompt phrasing to improve responses

### Grade 6 (8 skills unchanged)
- T22.G6.02: Adjust temperature for response creativity
- T22.G6.03: Handle streaming mode and long requests
- T22.G6.04.02: Build a conversation log with dynamic updates
- T22.G6.06.01: Create and configure a pre-built chat window
- T22.G6.06.02: Manage chat messages with append and update blocks
- T22.G6.06.03: Display streaming responses in real-time
- T22.G6.07: Debug off-topic responses by rewriting prompts
- T22.G6.08: Use multiple chatbot sessions with the select chatbot block

### Grade 7 (9 skills)
- T22.G7.01: Use system messages to set bot behavior
- T22.G7.02: Author a persona using system messages and few-shot turns
- T22.G7.03: Manage chat history and reset logic
- T22.G7.04: Capture data from UI widgets and inject into prompts
- T22.G7.05: Add moderation guardrails and escalation paths
- T22.G7.06: Attach images and files to chatbot conversations
- T22.G7.07: Use image moderation to filter visual content
- T22.G7.08: Compare different LLM models using the generic LLM block
- T22.G7.09: User-test the chatbot for inclusivity and clarity

### Grade 8 (5 skills)
- T22.G8.01: Add retrieval-augmented generation (RAG) to a chatbot
- T22.G8.02: Coordinate multi-agent conversations and summaries
- T22.G8.03: Parse structured chatbot outputs to trigger tools
- T22.G8.04: Create an automated chatbot testing and reporting system
- T22.G8.05: Integrate web search into chatbot responses

---

## VISUAL SUMMARY

### Grade 5 Skill Order

**BEFORE**:
```
G5.01 ──┐
G5.02 ──┤ Good concepts
G5.03 ──┘
G5.04 ── Observe parameters (depends on G5.1.5 - FORWARD REF!)
G5.1.5 ─ Use chatbot block (INVALID ID)
```

**AFTER**:
```
G5.01 ──┐
G5.02 ──┤ Good concepts
G5.03 ──┘
G5.04 ── Use chatbot block (FOUNDATIONAL)
G5.05 ── Observe parameters (depends on G5.04 - VALID)
```

### Grade 6 ID Fix

**BEFORE**: T22.G6.05.5 (INVALID dot notation)
**AFTER**: T22.G6.05 (VALID standard format)

---

## IMPACT SUMMARY

### Files Affected
- **allskills.md**: 3 skill IDs changed, 1 description enhanced, 3 dependency references updated

### External References to Update
If you have external materials referencing:
- T22.G5.1.5 → Update to T22.G5.04
- T22.G5.04 → Update to T22.G5.05
- T22.G6.05.5 → Update to T22.G6.05

### Code/Project References
If CreatiCode projects reference skill IDs in metadata:
- Update the 3 changed IDs
- Verify any projects tagged with these skills

### Assessment Materials
- Update rubrics referencing G5.04 or G5.1.5
- Update learning objectives for G6.05/G6.05.5
- Update skill progression charts

---

## VALIDATION CHECKLIST

After applying changes, verify:

✅ **ID Format**:
- No skills use dot notation (like G5.1.5 or G6.05.5)
- All IDs follow T22.GX.XX or T22.GX.XX.XX

✅ **Dependency Flow**:
- No forward references within T22
- T22.G5.05 depends on T22.G5.04 (not G5.1.5)
- T22.G6.01 depends on T22.G5.05 (not G5.04)
- T22.G6.04.01 depends on T22.G5.04 (not G5.1.5)

✅ **Skill Content**:
- All 38 skills present
- No skills deleted
- No skills added
- T22.G6.05 has enhanced hands-on description

✅ **Cross-Topic Dependencies**:
- All T06, T08, T09, T16, T21, T03 references preserved
- No changes to cross-topic dependency list

---

## CONCLUSION

**Total Changes**:
- 3 skill IDs renumbered/reformatted
- 1 skill description enhanced
- 3 dependency references updated
- 0 skills deleted
- 0 skills added

**Impact**: Minimal changes, maximum benefit. All critical issues resolved while preserving all skill content.

**Result**: T22 now has consistent ID formatting, logical skill progression, and valid dependency chains.
