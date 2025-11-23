# T26 Data Collection & Logging - Quick Reference

**Total Skills**: 49 current → **52 recommended** (+3 new)

---

## CRITICAL ISSUES TO FIX

### 🔴 HIGH PRIORITY (Must Fix)

| Issue | Skills Affected | Fix Required |
|-------|----------------|--------------|
| **Cloud storage blocks don't exist** | T26.G5.05, G5.06, G5.08 | Replace with database/file export blocks |
| **Missing G4 persistence scaffolding** | Gap before G5.05 | Add T26.G4.05 (persistent vs temporary storage) |
| **Missing G4 sensor scaffolding** | Gap before G5.07 | Add T26.G4.06 (simple sensor data collection) |
| **Missing G5 multi-sensor scaffolding** | Gap before G6.02 | Add T26.G5.09 (two sensors simultaneously) |
| **G6.02 too complex (6 sensors)** | T26.G6.02 | Reduce to 2-3 sensors |
| **Vague descriptions** | T26.G2.02, G3.06, G5.02, G4.04 | Add concrete examples |

---

## NEW SKILLS TO ADD

### T26.G4.05: Understand persistent vs temporary data storage
- **Why**: Students need to understand data persistence before using cloud/database
- **What**: Compare variable/list reset vs file export persistence
- **Dependencies**: T09.G3.05, T10.G4.02, T26.G4.02

### T26.G4.06: Collect simple sensor data into lists
- **Why**: Need introduction to sensor data before face detection
- **What**: Capture mouse position or microphone level into lists
- **Dependencies**: T07.G3.01, T10.G3.03, T26.G3.03

### T26.G5.09: Collect data from two sensors simultaneously
- **Why**: Bridge from single sensor (G5.07) to multiple sensors (G6.02)
- **What**: Log 2 sensors into table with matching timestamps
- **Dependencies**: T10.G4.02, T23.G4.01-02, T26.G5.07

---

## SKILLS TO REVISE

### T26.G5.05: Save and load tables to/from CreatiCode cloud storage
**Problem**: Cloud variable blocks don't exist
**Fix**: Change to database blocks
**New**: "Store tables in cloud database for persistence"

### T26.G5.06: Record player scores and retrieve leaderboard data
**Problem**: References non-existent cloud storage
**Fix**: Use game leaderboard blocks (which exist)
**New blocks**: `record game score`, `show game leaderboard`

### T26.G5.08: Export and import variables to/from files
**Problem**: References cloud storage
**Fix**: Focus on file I/O only (which exists)
**New blocks**: `export variable`, `import variable`, `export table`, `import file into table`

### T26.G6.02: Automate logging from multiple CreatiCode sensors
**Problem**: Lists 6 different sensors (overwhelming)
**Fix**: Reduce to 2-3 sensors
**Add dependency**: T26.G5.09

### T26.G2.02, G3.06, G5.02, G4.04
**Problem**: Vague or too-specific descriptions
**Fix**: See full analysis for improved descriptions

### T26.G5.01: Add print statements
**Minor fix**: Clarify "say for 2 seconds" vs "print to console"

---

## SKILLS MISSING BLOCK HINTS

Add block specifications to:
- T26.G5.04: `tables, add row to table, set cell value`
- T26.G6.05: `insert from table into collection`
- T26.G6.06: `fetch from collection into table where`
- T26.G6.07: `read from google sheet into table`
- T26.G6.08: `write into google sheet from table`

---

## VERIFIED CREATICODE FEATURES

### ✅ Confirmed Available
- **Database blocks**: insert, fetch, update, delete from collections
- **Google Sheets blocks**: read, write, insert/remove rows/columns
- **File I/O blocks**: export/import variables and tables
- **Leaderboard blocks**: record score, show leaderboard
- **Widget blocks**: buttons, labels, textboxes (for consent dialogs)
- **Semantic database blocks**: create, search with embeddings
- **Multiplayer blocks**: create/join games

### ❌ NOT Found
- **Cloud variable save/load**: No dedicated blocks for this
- **Reality**: Cloud sessions exist for real-time sync (multiplayer), not persistent storage

---

## TOPIC HEALTH SUMMARY

### ✅ Strengths
- Excellent unplugged K-2 foundation
- Smooth digital transition in G3
- Clear data structure progression (lists → tables → database)
- Strong ethics integration (privacy, consent, bias)
- No duplicates, no X-2 violations, no backward dependencies

### ⚠️ Weaknesses
- Cloud storage feature mismatch (critical)
- Missing scaffolding at G4-G5 transitions
- Some vague descriptions
- Missing block hints

### 📊 Quality Score
- **Internal Coherence**: 8/10 (excellent progression, minor gaps)
- **Feature Accuracy**: 6/10 (cloud storage issue)
- **Skill Clarity**: 7/10 (most good, some vague)
- **Age Appropriateness**: 9/10 (excellent K-2, well-scaffolded)

---

## GRADE-LEVEL BREAKDOWN

| Grade | Count | Focus | Issues |
|-------|-------|-------|--------|
| GK | 3 | Physical counting, observation | ✅ None |
| G1 | 3 | Picture surveys, logs | ✅ None |
| G2 | 5 | Data types, sample size | ✅ None |
| G3 | 6 | First coding, privacy | ✅ None |
| G4 | 4→6 | Tables, protocols | ⚠️ Add 2 skills |
| G5 | 8→9 | Cloud/files, sensors | 🔴 Fix 3, add 1 |
| G6 | 9 | Database, integration | ⚠️ Fix 1 |
| G7 | 7 | Quality, CRUD | ✅ None |
| G8 | 5 | Pipelines, AI | ✅ None |

---

## DEPENDENCY CHECK RESULTS

✅ **No X-2 violations** (all dependencies within 2 grades)
✅ **No backward dependencies** (all point to earlier skills)
✅ **Same-grade dependencies justified** (sequential progression)
✅ **Cross-topic dependencies preserved** (T01, T06-11, T23-25)

---

## IMPLEMENTATION CHECKLIST

### Phase 1: Critical Fixes
- [ ] Revise T26.G5.05 (cloud → database)
- [ ] Revise T26.G5.06 (cloud → leaderboard blocks)
- [ ] Revise T26.G5.08 (cloud → file I/O)
- [ ] Add T26.G4.05 (persistence concept)
- [ ] Add T26.G4.06 (simple sensors)
- [ ] Add T26.G5.09 (two sensors)
- [ ] Simplify T26.G6.02 (reduce sensors)

### Phase 2: Quality Improvements
- [ ] Enhance T26.G2.02 description
- [ ] Enhance T26.G3.06 description
- [ ] Enhance T26.G5.02 description
- [ ] Enhance T26.G4.04 description
- [ ] Clarify T26.G5.01 print terminology
- [ ] Add blocks to T26.G5.04, G6.05-08

### Phase 3: Polish
- [ ] Consider splitting T26.G6.03
- [ ] Review all descriptions for consistency
- [ ] Add more examples where helpful

---

## FILES GENERATED

1. **T26_Phase1_Analysis_Report.md** - Full detailed analysis
2. **T26_Quick_Reference.md** - This file (quick lookup)

---

## NEXT STEPS

1. Review and approve recommendations
2. Implement Phase 1 critical fixes first
3. Test revised skills with CreatiCode platform
4. Verify all block names match blockdes8.txt
5. Update allskills.md with changes
6. Create T26_Phase1_Summary.md when complete
