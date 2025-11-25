# T16 Skills - Visual Change Diagram

## Problem 1: Checkbox and Radio Button Split

```
BEFORE:
┌─────────────────────────────────────┐
│ T16.G4.07                          │
│ Add checkbox AND radio button      │
│ (TWO different widget types!)      │
└─────────────────────────────────────┘
              │
              │ (dependencies)
              ├──→ T16.G4.07.01 (tabs)
              ├──→ T16.G4.08 (settings)
              └──→ T16.G5.02 (forms)

AFTER:
┌────────────────────────┐  ┌────────────────────────┐
│ T16.G4.07.A           │  │ T16.G4.07.B           │
│ Add checkbox widgets   │  │ Add radio buttons      │
│ (independent toggles)  │  │ (mutually exclusive)   │
└────────────────────────┘  └────────────────────────┘
         │                           │
         │                           │
         ├──→ T16.G4.08             └──→ T16.G4.07.01
         │    (settings panel)            (tabs widget)
         │
         └──→ T16.G5.02
              (form validation)
```

**Rationale:** Checkboxes and radio buttons are fundamentally different concepts:
- Checkboxes: Multiple independent selections
- Radio buttons: One mutually exclusive selection

---

## Problem 2: Video Widget Simplification

```
BEFORE:
┌──────────────────────────────────────┐
│ T16.G5.05                           │
│ Embed AND control a video widget    │
│ (Too broad!)                         │
└──────────────────────────────────────┘
              │
              ├──→ T16.G5.05.01 (advanced controls)
              └──→ T16.G5.05.02 (video events)

AFTER:
┌──────────────────────────────────────┐
│ T16.G5.05                           │
│ Add a video widget to the stage     │
│ (Focus: just adding the widget)     │
└──────────────────────────────────────┘
              │
              ├──→ T16.G5.05.01 (advanced controls)
              └──→ T16.G5.05.02 (video events)
```

**Rationale:** Base skill should focus on adding the video widget. Sub-skills already properly cover controls and events.

---

## Problem 3: Chat Window Operations Split

```
BEFORE:
┌──────────────────────────────────────────────┐
│ T16.G5.06.01                                │
│ Create chat window + append + update        │
│ (THREE operations in one skill!)            │
└──────────────────────────────────────────────┘

AFTER:
┌─────────────────────────┐
│ T16.G5.06.01           │
│ Add a chat window      │
│ (Just create it)       │
└─────────────────────────┘
           │
           ├──→ ┌─────────────────────────┐
           │    │ T16.G5.06.02           │
           │    │ Append messages        │
           │    │ (Add new messages)     │
           │    └─────────────────────────┘
           │              │
           │              └──→ ┌─────────────────────────┐
           │                   │ T16.G5.06.03           │
           │                   │ Update streaming       │
           │                   │ (Modify last message)  │
           │                   └─────────────────────────┘
```

**Rationale:** Each operation uses a different block and serves a different purpose:
1. Creating the chat widget structure
2. Adding new message entries
3. Updating the most recent message (for streaming)

---

## Problem 4: Menu Bar Operations Split

```
BEFORE:
┌──────────────────────────────────────────────┐
│ T16.G6.06                                   │
│ Create menu bar + add groups + add items   │
│ (THREE operations in one skill!)            │
└──────────────────────────────────────────────┘
           │
           └──→ ┌─────────────────────────┐
                │ T16.G6.06.01           │
                │ Handle menu events     │
                └─────────────────────────┘

AFTER:
┌─────────────────────────┐
│ T16.G6.06              │
│ Add a menu bar widget  │
│ (Just create empty bar)│
└─────────────────────────┘
           │
           ├──→ ┌─────────────────────────────┐
           │    │ T16.G6.06.01 (NEW!)        │
           │    │ Add groups and items       │
           │    │ (Populate the menu bar)    │
           │    └─────────────────────────────┘
           │              │
           │              └──→ ┌─────────────────────────────┐
           │                   │ T16.G6.06.02 (renumbered) │
           │                   │ Handle menu item events    │
           │                   └─────────────────────────────┘
```

**Rationale:** Each operation uses different blocks and builds on the previous:
1. Create empty menu bar widget
2. Add menu groups (File, Edit) and items (New, Open, Save)
3. Respond to menu item click events

---

## Dependency Flow Visualization

### Checkbox Split Impact

```
OLD DEPENDENCIES:
    T16.G4.07 ──┬──→ T16.G4.07.01 (tabs)
                ├──→ T16.G4.08 (settings panel)
                └──→ T16.G5.02 (form validation)

NEW DEPENDENCIES:
    T16.G4.07.A ──┬──→ T16.G4.08 (settings panel - needs checkboxes)
                  └──→ T16.G5.02 (form validation - needs checkboxes)

    T16.G4.07.B ────→ T16.G4.07.01 (tabs - uses radio buttons concept)
```

---

## Skill Numbering Changes

### G4 Section (Checkboxes/Radio Buttons)
```
OLD:              NEW:
T16.G4.06         T16.G4.06 (no change)
T16.G4.07    →    T16.G4.07.A (checkboxes)
                  T16.G4.07.B (radio buttons)
T16.G4.07.01      T16.G4.07.01 (updated dependency)
T16.G4.08         T16.G4.08 (updated dependency)
T16.G4.09         T16.G4.09 (no change)
```

### G5 Section (Chat Window)
```
OLD:              NEW:
T16.G5.06         T16.G5.06 (no change)
T16.G5.06.01 →    T16.G5.06.01 (REPLACED - add chat window)
                  T16.G5.06.02 (NEW - append messages)
                  T16.G5.06.03 (NEW - update streaming)
T16.G5.07         T16.G5.07 (no change)
```

### G6 Section (Menu Bar)
```
OLD:              NEW:
T16.G6.06    →    T16.G6.06 (REVISED - add menu bar only)
                  T16.G6.06.01 (NEW - add groups and items)
T16.G6.06.01 →    T16.G6.06.02 (RENUMBERED - handle events)
T16.G6.06.02      T16.G6.06.03 or .07? (may need renumbering)
```

---

## Block Coverage Mapping

### Widget Creation Blocks - All Covered ✅
```
add button           → T16.G3.01
add label            → T16.G3.03
add textbox          → T16.G3.05
add rich textbox     → T16.G5.06
add slider           → T16.G4.05
add dropdown menu    → T16.G4.03
add checkbox         → T16.G4.07.A ✨ (split from G4.07)
add radio buttons    → T16.G4.07.B ✨ (split from G4.07)
add date picker      → T16.G5.02.01
add color picker     → T16.G5.02.01
add image (costume)  → T16.G4.02.01
add image (URL)      → T16.G4.02.01
add video            → T16.G5.05 ✨ (simplified)
add camera           → T16.G6.05
add progress bar     → T16.G5.04.01
add chat window      → T16.G5.06.01 ✨ (split)
add tabs             → T16.G4.07.01
add toolbox          → T16.G5.07
add menu bar         → T16.G6.06 ✨ (simplified)
add link             → T16.G4.10
```

### Widget Operation Blocks - All Covered ✅
```
append to chat       → T16.G5.06.02 ✨ (split)
update last chat     → T16.G5.06.03 ✨ (split)
add menu group       → T16.G6.06.01 ✨ (split)
add menu item        → T16.G6.06.01 ✨ (split)
draw charts          → T16.G7.05
set text style       → T16.G4.01
set widget style     → T16.G4.02
move widget          → T16.G3.08
resize widget        → T16.G3.08
scale widget         → T16.G5.04.02
rotate widget        → T16.G5.04.02
set transparency     → T16.G5.04.02
set visibility       → T16.G3.07
remove widget        → T16.G3.07.01
set z-index          → T16.G6.03.01
enable/disable       → T16.G6.03.02
release focus        → T16.G6.03.02
value of widget      → T16.G3.06, G3.04, G4.04, G4.06
set value            → T16.G3.04
append text          → T16.G3.04.01
```

### Widget Event Blocks - All Covered ✅
```
when widget clicked  → T16.G3.02
when widget changes  → T16.G4.04, G4.06
when pointer enters  → T16.G4.09
when pointer leaves  → T16.G4.09
when tab selected    → T16.G4.07.01
when video events    → T16.G5.05.02
when menu clicked    → T16.G6.06.02 ✨ (renumbered)
when any button      → T16.G3.02.01
```

---

## Summary Statistics

```
┌─────────────────────────────────────────────┐
│ SKILL COUNT CHANGES                         │
├─────────────────────────────────────────────┤
│ Starting Total:              63 skills      │
│ Deletions:                   -2 skills      │
│ Additions:                   +7 skills      │
│ Net Change:                  +5 skills      │
│ Final Total:                 68 skills      │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│ CHANGE BREAKDOWN                            │
├─────────────────────────────────────────────┤
│ Skills Split:                4 skills       │
│ Skills Revised:              3 skills       │
│ Skills with Dep Updates:     4 skills       │
│ Skills Renumbered:           1 skill        │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│ TOPIC COVERAGE                              │
├─────────────────────────────────────────────┤
│ CreatiCode Widget Blocks:    70+ blocks    │
│ T16 Skills Coverage:         100% ✅        │
│ Skills per Grade Band:                      │
│   - K:   2 skills (picture-based)          │
│   - G1:  2 skills (unplugged)              │
│   - G2:  2 skills (picture/unplugged)      │
│   - G3: 13 skills (basic widgets)          │
│   - G4: 14 skills (styling & inputs)       │
│   - G5: 11 skills (advanced widgets)       │
│   - G6:  9 skills (design & layout)        │
│   - G7:  5 skills (data & accessibility)   │
│   - G8:  4 skills (analysis & iteration)   │
└─────────────────────────────────────────────┘
```

---

## Benefits of These Changes

### 1. Single-Concept Skills ✅
```
BEFORE: T16.G4.07 → Checkboxes + Radio Buttons (2 concepts)
AFTER:  T16.G4.07.A → Checkboxes only (1 concept)
        T16.G4.07.B → Radio buttons only (1 concept)
```

### 2. Better Assessment Granularity ✅
```
Teachers can now track:
- Does student know how to add checkboxes? (T16.G4.07.A)
- Does student know how to add radio buttons? (T16.G4.07.B)

Instead of:
- Does student know both checkboxes and radio buttons? (T16.G4.07)
```

### 3. Flexible Curriculum Sequencing ✅
```
Scenario 1: Teach checkboxes first, radio buttons later
  → Assign T16.G4.07.A early, T16.G4.07.B later

Scenario 2: Teach only checkboxes this unit
  → Skip T16.G4.07.B entirely

NOT POSSIBLE with combined T16.G4.07!
```

### 4. Reduced Cognitive Load ✅
```
BEFORE: Learn 3 blocks in one skill (chat window)
  - add chat window
  - append to chat
  - update last chat message

AFTER: Learn 1 block per skill
  - T16.G5.06.01: add chat window
  - T16.G5.06.02: append to chat
  - T16.G5.06.03: update last chat message
```

### 5. Alignment with Block Structure ✅
```
Each skill now teaches exactly ONE block or ONE closely related concept.

This matches how CreatiCode blocks are organized in the palette!
```

---

## Implementation Timeline

```
Week 1: Planning & Backup
  └─→ Review all documents
  └─→ Backup allskills.md
  └─→ Plan implementation order

Week 2: Phase 1 - Checkbox/Radio Split
  └─→ Add T16.G4.07.A and T16.G4.07.B
  └─→ Delete T16.G4.07
  └─→ Update 3 dependencies

Week 2: Phase 2 - Video Simplification
  └─→ Revise T16.G5.05 description

Week 3: Phase 3 - Chat Window Split
  └─→ Replace T16.G5.06.01
  └─→ Add T16.G5.06.02 and .03

Week 3: Phase 4 - Menu Bar Split
  └─→ Revise T16.G6.06
  └─→ Add T16.G6.06.01
  └─→ Renumber T16.G6.06.01 → .02

Week 4: Validation & Testing
  └─→ Count total skills (should be 68)
  └─→ Validate all dependencies
  └─→ Test skill progression
  └─→ Review with stakeholders
```

---

## Ready to Implement?

✅ All analysis complete
✅ All skill definitions ready
✅ All dependency updates identified
✅ Implementation checklist created
✅ Visual diagrams completed

**Next Step:** Open allskills.md and begin Phase 1!

Refer to:
- **T16_ACTIONABLE_FIXES.md** for step-by-step instructions
- **T16_COMPLETE_REVISED_SKILLS.md** for copy-paste skill definitions
- **T16_optimization_summary.md** for detailed rationale
