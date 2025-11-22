# T15 Quality Issues - Quick Reference

**Generated:** 2025-11-22
**Full Report:** `/media/binyu/USB2/dev/CreatiCodeSkillMap/T15_QUALITY_ISSUES_ANALYSIS.md`

---

## CRITICAL ISSUES (HIGH PRIORITY)

### Platform Accuracy - Non-Existent Blocks

| Issue ID | Skills Affected | Problem | Action |
|----------|----------------|---------|--------|
| **ACC-001** | T15.G3.01, G3.02, G4.02 | References `switch costume`, `next costume` - **DON'T EXIST** | **DELETE** all 3 skills |
| **ACC-002** | T15.G4.03, G4.04 | References `switch backdrop`, `when backdrop switches` - **DON'T EXIST** | **DELETE** G4.03, **MODIFY** G4.04 |
| **ACC-003** | T15.G4.01 | References `change [ghost] effect` - **DOESN'T EXIST** | **REPLACE** with fade gradually |

**Impact:** 5 skills must be deleted, 2 modified
**Replacement Skills:** Need 3-5 new skills for CreatiCode's actual animation methods

---

## MEDIUM PRIORITY ISSUES

### Missing CreatiCode-Unique Features

| Issue ID | Gap | Current Skills | Action |
|----------|-----|----------------|--------|
| **ACC-004** | Styled say/think blocks | Basic say/think only | **ADD** 2-3 skills for text size, colors, backgrounds |
| **ACC-006** | AI Text-to-Speech | 1 vague accessibility skill | **ADD** 4-5 scaffolded TTS skills (basic → voices → multi-lang) |
| **ACC-007** | Widget-based interaction | Only `ask` block used | **ADD** 4 skills for textboxes, buttons, chat windows, tabs |
| **ACC-008** | Drawing blocks for scenes | Not mentioned | **ADD** 2 optional skills for programmatic scene creation |

**Impact:** Missing ~12 skills covering CreatiCode's powerful unique features
**Opportunity Cost:** Students missing out on AI voices, rich UI, modern interaction patterns

---

### Skill Quality Issues

| Issue ID | Skills Affected | Problem | Action |
|----------|----------------|---------|--------|
| **QUAL-001** | T15.G3.04-G3.07 | Over-complex dependencies (variables, loops, custom blocks for basic say block) | **SIMPLIFY** - remove unnecessary cross-topic deps |
| **QUAL-002** | T15.G3.02, G3.03 | "Animation" without costume blocks - vague | **REWRITE** with movement/size animation |
| **QUAL-003** | Entire topic | Missing narrative craft skills (story arc, pacing, character) | **ADD** 4 skills for storytelling concepts |
| **QUAL-004** | T15.G3.04 vs G3.05 | Say vs Think poorly differentiated | **ENHANCE** G3.05 to teach when to use each |
| **QUAL-005** | T15.G5.03 | Camera pan too complex (move all sprites) | **REPLACE** with viewport blocks |

**Impact:** Delays access to storytelling, misses pedagogical opportunities

---

## LOW PRIORITY ISSUES

### Dependency Problems

| Issue ID | Skills Affected | Problem | Action |
|----------|----------------|---------|--------|
| **DEP-001** | T15.GK.02, GK.03 | K skills depend on T01/T03 | **OPTIONAL** - simplify if needed |
| **DEP-002** | All T15.G4 (8 skills) | All share identical 4 dependencies (copy-paste error) | **CUSTOMIZE** per skill |
| **DEP-003** | T15.G3.04+ | Depend on deleted skills (G3.01-G3.03) | **UPDATE** after deletions |

**Impact:** Maintenance and scheduling issues

---

## SKILLS INVENTORY

### Delete (5 skills):
- T15.G3.01 - Switch costume (block doesn't exist)
- T15.G3.02 - Simple animation loop (uses next costume)
- T15.G3.03 - Reset appearance (uses costume blocks)
- T15.G4.02 - Costume number logic (block doesn't exist)
- T15.G4.03 - Switch backdrop (block doesn't exist)

### Major Revision (6 skills):
- T15.G4.01 - Change to gradual fade/reveal
- T15.G4.04 - Remove backdrop event trigger, use broadcasts
- T15.G5.03 - Replace sprite-moving with viewport blocks
- T15.G8.02 - Add TTS details and scaffolding
- T15.G3.04-G3.07 - Simplify dependencies

### New Skills Needed (17+ skills):

#### Animation Replacements (3):
- T15.G3.NEW13 - Movement animation (change x/y in loop)
- T15.G3.NEW14 - Size animation (change size in loop)
- T15.G3.NEW15 - Reset animation state (position, size, visibility)

#### Costume Management (2):
- T15.G4.NEW1 - Add costume from URL
- T15.G5.NEW2 - Multi-sprite character states

#### Scene Management (1):
- T15.G4.NEW3 - Scene changes with broadcasts + drawing/widgets

#### Styled Say/Think (2):
- T15.G5.NEW3 - Style speech bubbles (colors, sizes)
- T15.G5.NEW4 - Persistent bubbles (T=0)

#### Text-to-Speech (4):
- T15.G5.NEW5 - Basic TTS (say in language/voice)
- T15.G6.NEW6 - Customize voices (speed, pitch, volume)
- T15.G7.NEW7 - Multi-language stories
- T15.G8.02-REVISED - Full accessibility suite

#### Widget Interaction (4):
- T15.G6.NEW8 - Widget-based input (textboxes)
- T15.G7.NEW9 - Button-based choices
- T15.G7.NEW10 - Chat window stories
- T15.G8.NEW11 - Tabbed story chapters

#### Drawing (2 - optional):
- T15.G6.NEW12 - Draw simple scenes
- T15.G7.NEW13 - Programmatic scene transitions

#### Narrative Craft (4):
- T15.G4.NEW14 - Three-part story structure
- T15.G5.NEW15 - Pacing with wait blocks
- T15.G6.NEW16 - Character consistency via variables
- T15.G7.NEW17 - Emotional arc mapping

---

## BLOCKS REFERENCE

### ❌ DOESN'T EXIST IN CREATICODE:
```
switch costume to [name]
next costume
costume [number v]
switch costume to (1)

switch backdrop to [name]
next backdrop
when backdrop switches to [name]

change [ghost v] effect by (10)
set [ghost v] effect to (50)
change [color v] effect by (25)
clear graphic effects
```

### ✅ CREATICODE HAS INSTEAD:
```
# Styled Say/Think
say [TEXT] for (T) seconds text size (SIZE) [TEXTCOLOR] background [BGCOLOR] edge [EDGECOLOR]
think [TEXT] for (T) seconds text size (SIZE) [TEXTCOLOR] background [BGCOLOR] edge [EDGECOLOR]

# Gradual Effects
[fade/reveal v] sprite gradually in (T) seconds

# Costume Management
add costume from URL [URL] name [NAME]

# Text-to-Speech
say [TEXT] in [LANGUAGE v] as [VOICETYPE v] speed (SPEED) pitch (PITCH) volume (VOL) store sound as [NAME]

# Widgets
add textbox [NAME] at x (X) y (Y) width (W) height (H)
add button [NAME] at x (X) y (Y) width (W) height (H) text [TEXT]
add label [NAME] at x (X) y (Y) width (W) height (H) text [TEXT]
create chat window [NAME] at x (X) y (Y) width (W) height (H)
add tabs [NAME] at x (X) y (Y) width (W) height (H)
when widget [NAME] clicked
value from widget [NAME]

# Drawing
draw rectangle x (X) y (Y) width (W) height (H) color [COLOR] filled (FILLED)
draw oval x (X) y (Y) width (W) height (H) color [COLOR] filled (FILLED)
draw text [TEXT] at x (X) y (Y) text size (SIZE) [COLOR]
clear all drawings

# Viewport
move viewport to x (X) y (Y)
lock viewport to sprite [NAME v]
attach to viewport at x (X) y (Y)
detach from viewport
```

---

## IMPLEMENTATION PHASES

### Phase 1: Critical Fixes (HIGH PRIORITY)
1. Delete 5 skills with non-existent blocks
2. Revise T15.G4.01 (ghost → fade gradually)
3. Revise T15.G4.04 (backdrop events → broadcasts)
4. Add 3 animation replacement skills (movement, size, reset)
5. Add 2 costume management skills (URL, multi-sprite states)
6. Add 1 scene management skill (broadcasts + drawing)

**Deliverable:** Functional T15 with ~40 accurate skills

### Phase 2: CreatiCode Features (MEDIUM PRIORITY)
1. Add 2 styled say/think skills
2. Add 4 TTS skills (basic → voices → multi-lang → accessibility)
3. Add 4 widget interaction skills (textboxes → buttons → chat → tabs)
4. Revise T15.G5.03 (viewport instead of sprite-moving)

**Deliverable:** T15 showcasing CreatiCode's unique power (~50 skills)

### Phase 3: Quality Enhancement (MEDIUM PRIORITY)
1. Add 4 narrative craft skills (structure, pacing, character, emotion)
2. Simplify G3 dependencies (enable early storytelling)
3. Customize G4 dependencies (remove copy-paste)
4. Enhance G3.05 (when to use say vs think)

**Deliverable:** Polished T15 with pedagogy + platform alignment (~54 skills)

### Phase 4: Optional Enhancements (LOW PRIORITY)
1. Add 2 drawing scene skills (optional)
2. Clean up K dependency chains (optional)
3. Add speech recognition skills (advanced, optional)

**Deliverable:** Comprehensive T15 with all possibilities (~56 skills)

---

## METRICS SUMMARY

| Metric | Before | After Phase 1 | After Phase 2 | After Phase 3 |
|--------|--------|---------------|---------------|---------------|
| **Total Skills** | 47 | 40 | 50 | 54 |
| **Platform Accuracy** | 60% | 100% | 100% | 100% |
| **CreatiCode Features** | 15% | 30% | 80% | 85% |
| **Scaffolding Quality** | 70% | 75% | 80% | 95% |
| **Dependency Health** | 60% | 70% | 75% | 90% |

---

## QUICK ACTION CHECKLIST

### Immediate:
- [ ] Delete T15.G3.01, G3.02, G3.03, G4.02, G4.03
- [ ] Revise T15.G4.01 (ghost → fade gradually)
- [ ] Revise T15.G4.04 (remove backdrop event trigger)
- [ ] Add T15.G3.NEW13-15 (movement/size/reset animation)
- [ ] Add T15.G4.NEW1-3 (costume URL, multi-sprite, scene broadcasts)

### Next:
- [ ] Add T15.G5.NEW3-5 (styled say, persistent, basic TTS)
- [ ] Add T15.G6.NEW6-8 (voice customize, widget input)
- [ ] Add T15.G7.NEW7-10 (multi-lang, buttons, chat windows)
- [ ] Revise T15.G5.03 (viewport blocks)

### Then:
- [ ] Add T15.G4.NEW14, G5.NEW15, G6.NEW16, G7.NEW17 (narrative craft)
- [ ] Simplify T15.G3.04-G3.07 dependencies
- [ ] Customize T15.G4.01-G4.08 dependencies
- [ ] Update all dependencies after deletions

### Optional:
- [ ] Add T15.G6.NEW12-13 (drawing scenes)
- [ ] Simplify K dependencies
- [ ] Add speech recognition skills

---

**Full Details:** See `/media/binyu/USB2/dev/CreatiCodeSkillMap/T15_QUALITY_ISSUES_ANALYSIS.md`
