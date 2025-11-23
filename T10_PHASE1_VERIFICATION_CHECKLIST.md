# T10 Phase 1 Optimization - Verification Checklist

**Purpose:** Systematic verification that all Phase 1 optimization requirements are met
**Date:** 2025-11-22
**Use:** Check off each item as you verify it

---

## CRITICAL RULES COMPLIANCE

### Rule 1: Never Delete Skills ✓
- [ ] Verified: No existing skills were deleted
- [ ] Verified: All 88 original skills are preserved
- [ ] Verified: Only additions and enhancements made

### Rule 2: Only Focus on T10 ✓
- [ ] Verified: No modifications to T01-T09, T11+ skills
- [ ] Verified: All new skills are T10.* format
- [ ] Verified: Cross-topic dependencies preserved (not modified)

### Rule 3: Preserve Cross-Topic Dependencies ✓
- [ ] Verified: All T01, T06, T07, T08, T09 dependencies unchanged
- [ ] Verified: New skills use appropriate cross-topic dependencies
- [ ] Verified: No new cross-topic dependencies violate X-2 rule

### Rule 4: Only Flag Intra-T10 Issues ✓
- [ ] Verified: Only T10-to-T10 dependency issues flagged
- [ ] Verified: Cross-topic dependencies accepted as-is
- [ ] Verified: No false dependency violations reported

---

## HIGH PRIORITY ISSUES RESOLUTION

### A. Missing Critical Skills (19 new skills)

#### G3 Skills (1 new)
- [ ] **T10.G3.09:** Increment/decrement list item added
  - Block: data_changeitemoflist
  - Dependencies: T10.G3.02, T10.G3.04, T09.G3.01.02
  - CSTA code present
  - Description accurate

#### G4 Skills (7 new)
- [ ] **T10.G4.14:** Reverse list order added
  - Block: data_reverselist
- [ ] **T10.G4.15:** Shuffle list randomly added
  - Block: data_reshuffle
- [ ] **T10.G4.16:** Generate random list added
  - Block: data_setrandomlist
- [ ] **T10.G4.17:** Delete by value added
  - Block: data_deletevalueoflist
- [ ] **T10.G4.18:** Loop with index added
  - Block: data_for_each_index
- [ ] **T10.G4.19:** Find substring in list added
  - Block: data_itemnumoflist2
- [ ] **T10.G4.20:** Select N items by criteria added
  - Block: data_insertitemsfromlist

#### G5 Skills (8 new)
- [ ] **T10.G5.11:** Manage table columns added
  - Blocks: data_addcolatposition, data_deletecolumnfromtable, data_removeallcolumnsfromtable
- [ ] **T10.G5.12:** Copy list to column added
  - Block: data_setlisttocolumn
- [ ] **T10.G5.13:** Insert row at position added
  - Block: data_insertrowtotable
- [ ] **T10.G5.14:** Replace entire row added
  - Block: data_replacerowoftable
- [ ] **T10.G5.15:** Get row as list added
  - Block: data_rowatindexoftable
- [ ] **T10.G5.16:** Find row by substring added
  - Block: data_rowindexwithcondition2
- [ ] **T10.G5.17:** Increment/decrement cell added
  - Block: data_changeitematrowcolumn
- [ ] **T10.G5.18:** Show/hide table monitors added
  - Blocks: data_showtable, data_hidetable

#### G6 Skills (1 new)
- [ ] **T10.G6.08:** Shuffle table rows added
  - Block: data_reshuffletable

#### G7 Skills (3 new + 1 split)
- [ ] **T10.G7.09:** Split into read/write (core) and structure management
  - Core: p2p_readfromgooglesheet, p2p_writeintogooglesheet
  - Structure: 8 remaining Google Sheets blocks
- [ ] **T10.G7.11:** Display formatted snapshots added
  - Block: data_showsnapshotoftable
- [ ] **T10.G7.12:** Export table as CSV added
  - Block: data_exporttable
- [ ] **T10.G7.13:** Cloud save/load added
  - Blocks: data_savetable, data_loadtable, data_savedata, data_loaddata
- [ ] **T10.G7.14:** AI skill renumbered (was G7.10)

### B. Inaccurate Skill Descriptions (2 fixes)

- [ ] **T10.G5.02:** Fixed block syntax
  - OLD: "add column [name] to table"
  - NEW: "add column [name] at position (n) to table"
  - Verified syntax matches blockdes8.txt

- [ ] **T10.G5.10:** Verified block existence
  - Checked if "make table from list" block exists
  - If not, skill updated to use alternative approach
  - Documentation matches actual blocks

### C. Intra-Topic Dependency Violations (checked)

- [ ] Verified: No X-2 rule violations in existing skills
- [ ] Verified: No X-2 rule violations in new skills
- [ ] Verified: T10.G8.02 → T01.G6.01 dependency is VALID (8-2=6 ✓)
- [ ] Verified: All new skill dependencies are within X-2 range
- [ ] Verified: No circular dependencies created

### D. Overly Broad/Complex Skills (2 fixes)

- [ ] **T10.G7.09:** Split into focused skills
  - New G7.09: Read/write Google Sheets (2 core blocks)
  - New G7.10: Manage Sheets structure (8 structure blocks)
  - Both skills have clear, focused learning objectives

- [ ] **T10.G7.14 (was G7.10):** AI skill clarity
  - Two approaches clearly distinguished (NN vs KNN)
  - Description explains when to use each
  - Not split (kept together as introduction)

---

## MEDIUM PRIORITY ISSUES RESOLUTION

### E. Grade Appropriateness (checked)

- [ ] K-2 skills remain picture-based/unplugged
- [ ] G3+ skills use block coding appropriately
- [ ] No coding in K-2
- [ ] G2.07 provides conceptual bridge to G3.01

### F. Duplicate/Overlapping Skills (checked)

- [ ] Verified: No duplicate skills found
- [ ] Verified: Each skill teaches distinct concept
- [ ] Verified: No unnecessary redundancy

### G. Unclear/Vague Descriptions (enhanced)

- [ ] **T10.G8.07:** Enhanced with implementation details
  - Hash function approach specified
  - Collision handling method described
  - Implementation pattern provided

- [ ] **G7 Advanced Skills:** Enhanced with examples
  - T10.G7.01: Pivot example added
  - T10.G7.03: Schema design examples added
  - T10.G7.05: Cleaning transformation examples added
  - T10.G8.04: Simulation example added
  - T10.G8.06: Linked table example added

### H. Scaffolding Issues (addressed)

- [ ] **T10.G5.01:** Enhanced description
  - Explicit connection to parallel lists added
  - "Table = organized parallel lists" concept clear
  - Dependency on T10.G4.02 justified

- [ ] **G7 Skills:** Reordered thematically (optional)
  - Grouped by data pipeline: acquire → clean → transform → analyze → visualize
  - New order: G7.02, G7.09, G7.05, G7.06, G7.08, G7.01, G7.03, G7.07, G7.04, G7.14

---

## LOW PRIORITY ISSUES RESOLUTION

### I. Inconsistent Terminology (standardized)

- [ ] **Position vs Index:**
  - G3-G5 consistently use "position"
  - G6+ introduce "index" as technical synonym
  - Note added explaining equivalence

- [ ] **Reporter vs Stack Blocks:**
  - Complex skills note block types
  - Helps students understand usage patterns

### J. Missing Examples (added)

- [ ] **K-2 Skills:** Example themes added
  - Animals, shapes, colors, foods
  - Teacher guidance for assessment creation

---

## BLOCK COVERAGE VERIFICATION

### List Blocks (42 total)

#### Basic Scratch List Blocks (9/9) ✓
- [ ] add [item] to [list] - T10.G3.01
- [ ] delete (n) of [list] - T10.G3.04
- [ ] delete all of [list] - T10.G3.04
- [ ] insert [item] at (n) - T10.G4.03
- [ ] replace item (n) - T10.G4.04
- [ ] item (n) of [list] - T10.G3.02
- [ ] item # of [value] - T10.G4.01
- [ ] length of [list] - T10.G3.03
- [ ] [list] contains [item]? - T10.G3.06

#### Extended List Blocks (17/17) ✓
- [ ] data_changeitemoflist - T10.G3.09 ← NEW
- [ ] data_reduceitemoflist - (covered by G3.09 change by negative)
- [ ] data_joinlistwith - T10.G4.13
- [ ] data_set_list_to_split_of - T10.G4.12
- [ ] data_deletevalueoflist - T10.G4.17 ← NEW
- [ ] data_reverselist - T10.G4.14 ← NEW
- [ ] data_reshuffle - T10.G4.15 ← NEW
- [ ] data_sortlistby - T10.G4.05
- [ ] data_insertitemsfromlist - T10.G4.20 ← NEW
- [ ] data_copytolist - T10.G4.11
- [ ] data_appendtolist - T10.G4.11
- [ ] data_setrandomlist - T10.G4.16 ← NEW
- [ ] data_setrandomlistseed - (covered by G4.16)
- [ ] data_itemnumoflist2 - T10.G4.19 ← NEW
- [ ] data_itemspecificvalueoflist - T10.G4.06
- [ ] data_for_each - T10.G3.05
- [ ] data_for_each_index - T10.G4.18 ← NEW

#### Set & Regex Blocks (6/6) ✓
- [ ] union [list1] [list2] - T10.G6.06
- [ ] intersect [list1] [list2] - T10.G6.06
- [ ] [list1] minus [list2] - T10.G6.06
- [ ] unique items - T10.G6.07
- [ ] operator_regex_match_into_list - T10.G7.08
- [ ] operator_regex_split_into_list - T10.G7.08

**List Blocks Total: 32/32 core blocks covered ✓**

### Table Blocks (42 total)

#### Table Structure (18/18) ✓
- [ ] data_addcolatposition - T10.G5.11 ← NEW
- [ ] data_deletecolumnfromtable - T10.G5.11 ← NEW
- [ ] data_removeallcolumnsfromtable - T10.G5.11 ← NEW
- [ ] data_setlisttocolumn - T10.G5.12 ← NEW
- [ ] data_addrowtotable - T10.G5.03
- [ ] data_insertrowtotable - T10.G5.13 ← NEW
- [ ] data_replacerowoftable - T10.G5.14 ← NEW
- [ ] data_replaceitematrowcolumn - T10.G5.05
- [ ] data_changeitematrowcolumn - T10.G5.17 ← NEW
- [ ] data_reduceitematrowcolumn - (covered by G5.17 change by negative)
- [ ] data_rowatindexoftable - T10.G5.15 ← NEW
- [ ] data_rowindexwithcondition - T10.G5.06
- [ ] data_rowindexwithcondition2 - T10.G5.16 ← NEW
- [ ] data_rowcountoftable - T10.G5.06
- [ ] data_itematrowcolumnoftable - T10.G5.04
- [ ] data_deleterowoftable - T10.G5.09
- [ ] data_deleterowwithcondition - T10.G5.09
- [ ] data_deleteallrowsoftable - T10.G5.09 (expanded)

#### Table Operations (7/7) ✓
- [ ] data_computetable - T10.G5.08
- [ ] data_settabletocomputed - T10.G6.05
- [ ] data_copy_table_into_table - T10.G6.03
- [ ] data_append_table_into_table - T10.G6.03
- [ ] data_pivot_table_into_table - T10.G7.01
- [ ] data_lookuptable - T10.G6.04
- [ ] data_sorttablebycolumn - T10.G6.01
- [ ] data_reshuffletable - T10.G6.08 ← NEW

#### Table Display (3/3) ✓
- [ ] data_showtable - T10.G5.18 ← NEW
- [ ] data_hidetable - T10.G5.18 ← NEW
- [ ] data_showsnapshotoftable - T10.G7.11 ← NEW

#### Import/Export (6/6) ✓
- [ ] data_exporttable - T10.G7.12 ← NEW
- [ ] data_importtable - T10.G7.02
- [ ] data_savedata - T10.G7.13 ← NEW
- [ ] data_loaddata - T10.G7.13 ← NEW
- [ ] data_savetable - T10.G7.13 ← NEW
- [ ] data_loadtable - T10.G7.13 ← NEW

#### Google Sheets (10/10) ✓
- [ ] p2p_readfromgooglesheet - T10.G7.09
- [ ] p2p_writeintogooglesheet - T10.G7.09
- [ ] p2p_addsheet - T10.G7.10 (split from G7.09)
- [ ] p2p_removesheet - T10.G7.10
- [ ] p2p_insertcolumnsinsheet - T10.G7.10
- [ ] p2p_insertrowsinsheet - T10.G7.10
- [ ] p2p_removecolumnsfromsheet - T10.G7.10
- [ ] p2p_removerowsfromsheet - T10.G7.10
- [ ] p2p_clearsheet - T10.G7.10
- [ ] p2p_listSheetsInGoogleSheet - T10.G7.09 (expanded)

#### Charts & AI (7/7) ✓
- [ ] widget_drawchartusinglist - T10.G7.04
- [ ] widget_drawchartusingcolumn - T10.G7.04
- [ ] widget_drawchartusingcategory - T10.G7.04 (expanded)
- [ ] train_model - T10.G7.14 (renumbered)
- [ ] predict_by_model - T10.G7.14
- [ ] ai_createknnclassifier - T10.G7.14
- [ ] ai_predictknnclassifier - T10.G7.14

**Table Blocks Total: 42/42 blocks covered ✓**

### OVERALL COVERAGE
- **Total Blocks:** 75 (32 list + 42 table + 1 misc)
- **Blocks Covered:** 75/75 (100%) ✓
- **Before Optimization:** 54/75 (72%)
- **Improvement:** +21 blocks (+28%)

---

## SKILL QUALITY STANDARDS

### All New Skills Must Have:
- [ ] Unique skill ID (T10.GX.XX format)
- [ ] Clear, concise title
- [ ] Concrete description (no vague terms)
- [ ] Specific block references with exact syntax
- [ ] Dependencies listed (with IDs)
- [ ] CSTA standard code
- [ ] Grade-appropriate complexity
- [ ] Assessable learning objective

### All Skill Descriptions Must:
- [ ] Match actual CreatiCode block syntax exactly
- [ ] Not reference non-existent blocks
- [ ] Explain WHAT students learn (not just block name)
- [ ] Explain WHY the skill matters
- [ ] Include examples where helpful (G7-G8)
- [ ] Use consistent terminology
- [ ] Be clear enough for auto-grading

### All Dependencies Must:
- [ ] Be actual skill IDs that exist
- [ ] Follow X-2 rule (depend on X, X-1, X-2 grades only)
- [ ] Be necessary prerequisites (not tangential)
- [ ] Not create circular references
- [ ] Include cross-topic deps where needed

---

## FINAL VALIDATION

### Skill Counts
- [ ] Kindergarten: 8 skills (unchanged)
- [ ] Grade 1: 6 skills (unchanged)
- [ ] Grade 2: 7 skills (unchanged)
- [ ] Grade 3: 9 skills (+1 new)
- [ ] Grade 4: 20 skills (+7 new)
- [ ] Grade 5: 18 skills (+8 new)
- [ ] Grade 6: 8 skills (+1 new)
- [ ] Grade 7: 13 skills (+3 new, -1 renumbered)
- [ ] Grade 8: 8 skills (unchanged, 1 enhanced)
- [ ] **TOTAL: 107 skills** (+19 from 88)

### Coverage Metrics
- [ ] All 75 CreatiCode list/table blocks covered
- [ ] 100% block coverage achieved
- [ ] No blocks missing skill coverage
- [ ] No skills reference non-existent blocks

### Issue Resolution
- [ ] 31 HIGH priority issues → 0 remaining
- [ ] 12 MEDIUM priority issues → 0 remaining
- [ ] 8 LOW priority issues → 0 remaining
- [ ] All critical gaps filled
- [ ] All inaccuracies fixed

### Rule Compliance
- [ ] No skills deleted (only additions)
- [ ] Only T10 skills modified
- [ ] Cross-topic dependencies preserved
- [ ] X-2 rule followed throughout
- [ ] No intra-topic violations

---

## PHASE 1 COMPLETION CRITERIA

All items below must be checked before Phase 1 is considered complete:

### Documentation
- [ ] All new skills documented in proper format
- [ ] All enhancements clearly described
- [ ] All fixes validated against actual blocks
- [ ] All dependencies verified
- [ ] All CSTA codes assigned

### Quality
- [ ] No technical errors
- [ ] No broken dependencies
- [ ] No vague descriptions
- [ ] No overly complex skills
- [ ] Proper scaffolding progression

### Coverage
- [ ] 100% block coverage achieved
- [ ] All critical features covered
- [ ] No significant gaps remaining
- [ ] Ready for Phase 2 (if needed)

---

## SIGN-OFF

Phase 1 Optimization Complete: ☐ YES / ☐ NO

**Verified By:** _________________
**Date:** _________________
**Next Step:** Integrate into allskills.md or proceed to Phase 2

**Notes:**
