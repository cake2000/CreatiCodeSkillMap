# T29 Quick Reference & Action Items

## Overview
- **Topic:** T29 – Text Data & NLP Foundations
- **Grade Range:** 3-8
- **Total Skills:** 28 skills
- **Quality Score:** 71% (needs improvement in dependencies)

## Critical Findings

### ✅ Strengths
1. Excellent progression from unplugged (G3) → coding (G4-G6) → advanced (G7-G8)
2. Strong AI/ML integration (ChatGPT, classifiers, semantic search)
3. Good alignment with CreatiCode's advanced NLP blocks
4. No forward dependencies found
5. Skills are generally clear and grade-appropriate

### ❌ Critical Issues
1. **29% of skills have wrong-grade cross-topic dependencies**
   - 8 skills depend on T06/T07/T08/T09/T10 from wrong grades
   - 4 instances of 4+ grade jumps (SEVERE)
   - 20+ instances of 2-grade jumps at boundary

2. **Missing foundational skills**
   - No skill for accessing characters by position (needed for G4.03)
   - No skill for counting characters/words (needed for G6.01)
   - No skill for table creation (needed for G5.01, G5.05)

3. **Missing loop dependencies**
   - G4.03, G4.04, G4.05 all need T07 but don't list it

4. **Inconsistent internal dependencies**
   - G4.05 should depend on G4.04 (both scan text)
   - G7.04 should depend on G4.01 (both compare summaries)

## Immediate Action Items

### Priority 1: Fix Dependencies (CRITICAL)

#### Fix 1: Update Cross-Grade Dependencies
**Affected Skills:** T29.G6.01, G6.02, G6.03, G6.04, G7.01, G7.02, G7.03, G7.04

**Changes Needed:**
```
G6 skills should depend on G6 equivalents (not G4):
- Replace T08.G4.01 → T08.G6.x
- Replace T09.G4.04 → T09.G6.x
- Replace T10.G4.03 → T10.G6.x
- Replace T07.G4.01 → T07.G6.x
- Replace T06.G4.01 → T06.G6.x

G7 skills should depend on G7 equivalents (not G3/G5):
- Replace T09.G3.05 → T09.G7.x (SEVERE - 4 grades back!)
- Replace T10.G5.03 → T10.G7.x
- Replace T08.G5.01 → T08.G7.x
- Replace T06.G5.01 → Remove (irrelevant for G7.03)
```

#### Fix 2: Add Missing Loop Dependencies
**Affected Skills:** T29.G4.03, G4.04, G4.05

**Changes:**
- T29.G4.03: Add T07.G4.01 (needs character iteration)
- T29.G4.04: Add T07.G4.01 (needs word iteration)
- T29.G4.05: Add T07.G4.01 (needs paragraph scanning)

#### Fix 3: Fix Within-Topic Dependencies
**Changes:**
- T29.G4.05: Add dependency on T29.G4.04
- T29.G7.04: Add dependency on T29.G4.01

#### Fix 4: Remove Irrelevant Dependency
**Change:**
- T29.G7.03: Remove T06.G5.01 (clones not needed for text auditing)

### Priority 2: Add Missing Skills (HIGH PRIORITY)

#### Add 1: T29.G4.01b - Access characters by position
**Placement:** Between G4.02 and G4.03
**Why:** G4.03 requires character-by-character iteration
**Dependencies:** T29.G4.02, T07.G4.01, T10.G4.03
**Enables:** T29.G4.03
**Blocks:** `letter (N) of [text]`, `length of [text]`

#### Add 2: T29.G4.02b - Count characters and words
**Placement:** After G4.02
**Why:** Foundation for G6.01 (characters vs words vs tokens)
**Dependencies:** T29.G4.02, T09.G4.04
**Enables:** T29.G6.01
**Blocks:** `length of [text]`, `length of [list]`

#### Add 3: T29.G5.01b - Create and populate text data tables
**Placement:** Before G5.01
**Why:** G5.01, G5.05, G6.04 all write to tables
**Dependencies:** T29.G4.04, T10.G5.03
**Enables:** T29.G5.01, T29.G5.05, T29.G6.04
**Blocks:** `add row to table`, `set cell`, `get cell value`

### Priority 3: Clarify Descriptions (MEDIUM PRIORITY)

#### Clarify 1: T29.G4.01
**Current:** "compare to a computer-generated summary"
**Change to:** "compare to a ChatGPT-generated summary"

#### Clarify 2: T29.G5.04
**Current:** "populate a structured form"
**Change to:** "extract key elements (subject, setting, mood) and format as structured prompt parameters"

#### Clarify 3: T29.G8.01
**Current:** "design scripts that ingest raw text, normalize it, extract features..."
**Change to:** Add specific pipeline stages:
1. Ingest text from source
2. Normalize (lowercase, remove punctuation)
3. Tokenize (split into words)
4. Extract features
5. Run analysis (sentiment/retrieval)
6. Store results for future use

## Complete Skill Inventory

### Grade 3 (Unplugged/Conceptual)
1. ✅ T29.G3.01: Distinguish text data from numbers and pictures
2. ✅ T29.G3.02: Count word occurrences manually
3. ✅ T29.G3.03: Group words by category
4. ✅ T29.G3.04: Explain why clean text helps AI
5. ➕ **NEW:** T29.G3.05: Identify characters, words, sentences (recommended)

### Grade 4 (Early Coding)
1. ⚠️ T29.G4.01: Compare human vs computer summary (needs clarification)
2. ✅ T29.G4.02: Use split and join blocks
3. ➕ **NEW:** T29.G4.01b: Access characters by position (CRITICAL)
4. ➕ **NEW:** T29.G4.02b: Count characters and words (CRITICAL)
5. ⚠️ T29.G4.03: Clean text (needs T07 dependency)
6. ➕ **NEW:** T29.G4.03b: Build custom text cleaning blocks (recommended)
7. ⚠️ T29.G4.04: Count words and report most frequent (needs T07 dependency)
8. ⚠️ T29.G4.05: Highlight keywords (needs T07 dependency + T29.G4.04 dependency)

### Grade 5 (Data Structures & NLP)
1. ➕ **NEW:** T29.G5.01b: Create and populate tables (CRITICAL)
2. ✅ T29.G5.01: Structure chat logs into tables
3. ✅ T29.G5.02: Build stop-word filters
4. ✅ T29.G5.03: Measure simple sentiment heuristics
5. ➕ **NEW:** T29.G5.03b: Apply sentiment to datasets (recommended)
6. ⚠️ T29.G5.04: Map story to AI prompt slots (needs clarification)
7. ✅ T29.G5.05: Use analyze sentence block for POS

### Grade 6 (Advanced Processing)
1. ⚠️ T29.G6.01: Explain characters vs words vs tokens (wrong dependencies)
2. ➕ **NEW:** T29.G6.01b: Implement token counting (recommended)
3. ⚠️ T29.G6.02: Compute n-gram frequencies (wrong dependencies)
4. ⚠️ T29.G6.03: Create autocomplete suggestions (wrong dependencies)
5. ➕ **NEW:** T29.G6.03b: Handle keyboard input (recommended)
6. ⚠️ T29.G6.04: Log XO prompts/responses (wrong dependencies)
7. ✅ T29.G6.05: Use regex patterns

### Grade 7 (Integration & Analysis)
1. ⚠️ T29.G7.01: Build keyword retrieval (RAG) (wrong dependencies)
2. ➕ **NEW:** T29.G7.01b: Compare keyword vs semantic retrieval (recommended)
3. ⚠️ T29.G7.02: Engineer text features for classifiers (wrong dependencies)
4. ➕ **NEW:** T29.G7.02b: Evaluate with train/test split (recommended)
5. ⚠️ T29.G7.03: Audit datasets for bias (wrong dependencies + irrelevant dep)
6. ⚠️ T29.G7.04: Compare human vs XO summaries (wrong dependencies + missing G4.01)

### Grade 8 (Pipelines & Evaluation)
1. ⚠️ T29.G8.01: Build end-to-end pipelines (needs clarification)
2. ✅ T29.G8.02: Compute precision/recall/F1
3. ✅ T29.G8.03: Integrate analytics into prompting
4. ✅ T29.G8.04: Publish datasheets for datasets

**Legend:**
- ✅ Good quality, no major issues
- ⚠️ Has dependency or clarity issues
- ➕ NEW: Recommended addition

## CreatiCode Block Coverage

### Well-Covered (Explicitly Taught)
- ✅ Split/join: `set list to split`, `join list into text`
- ✅ Case conversion: `uppercase/lowercase of text`
- ✅ Regex (all 5 blocks): test, match, search, replace, split
- ✅ NLP analysis: `analyze sentence`
- ✅ Semantic search: `create/search semantic database`
- ✅ Classifiers: `create/predict KNN classifier`
- ✅ ChatGPT: `ChatGPT request`

### Used But Not Explicitly Taught (Needs Skills)
- ⚠️ Character access: `letter (N) of [text]` ← Add T29.G4.01b
- ⚠️ String length: `length of [text]` ← Add T29.G4.02b
- ⚠️ Substring: `substring of [text]` ← Clarify in G4.03
- ⚠️ Replace: `replace [T1] with [T2]` ← Clarify in G4.03
- ⚠️ Contains: `[text1] includes [text2]` ← Clarify in G5.02
- ⚠️ Trim: `trim [text]` ← Could add to G4.03

### Advanced Blocks Not Covered (Appropriate)
- Speech recognition/text-to-speech (belongs in different topic)
- Neural network training (too advanced for K-8)
- Advanced string operations (LCS, string diff)

## Dependency Pattern Analysis

### Correct Patterns ✅
- G3 skills: No dependencies or only T29.G3.x
- G8 skills: Use appropriate G6-G8 cross-topic dependencies

### Problematic Patterns ❌

**Pattern 1: G6 skills depending on G4 cross-topic skills**
```
WRONG: T29.G6.01 → T08.G4.01, T09.G4.04, T10.G4.03
RIGHT: T29.G6.01 → T08.G6.x, T09.G6.x, T10.G6.x
```

**Pattern 2: G7 skills depending on G3 skills**
```
WRONG: T29.G7.01 → T09.G3.05 (4 grades back!)
RIGHT: T29.G7.01 → T09.G7.x or T09.G5.x (max 2 back)
```

**Pattern 3: Missing loop dependencies in G4**
```
WRONG: T29.G4.03 (character iteration) → no T07 dependency
RIGHT: T29.G4.03 → T07.G4.01
```

## Next Steps

### Step 1: Update Dependencies (1-2 hours)
1. Fix 8 skills with wrong-grade cross-topic dependencies
2. Add T07 dependencies to G4.03, G4.04, G4.05
3. Add within-topic dependencies (G4.05→G4.04, G7.04→G4.01)
4. Remove T06.G5.01 from G7.03

### Step 2: Add Critical Missing Skills (2-3 hours)
1. Write T29.G4.01b: Access characters by position
2. Write T29.G4.02b: Count characters and words
3. Write T29.G5.01b: Create and populate tables

### Step 3: Clarify Descriptions (1 hour)
1. Update T29.G4.01 description
2. Update T29.G5.04 description
3. Update T29.G8.01 description with pipeline stages

### Step 4: Validate (1 hour)
1. Check all dependencies follow X-2 rule
2. Verify no forward dependencies
3. Confirm all needed blocks exist in CreatiCode
4. Test example programs for each skill

### Step 5: Consider Enhancements (Optional)
1. Add 5 recommended skills (G3.05, G4.03b, G5.03b, G7.02b, etc.)
2. Develop example programs
3. Create assessment rubrics

## Metrics Summary

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Total Skills | 28 | 31+ | Needs 3+ additions |
| Clear Descriptions | 93% | 100% | Needs 3 clarifications |
| Correct Dependencies | 71% | 100% | Needs 8 fixes |
| X-2 Rule Compliance | 71% | 100% | Needs 8 fixes |
| Block Coverage | 57% | 80%+ | Needs 3 skills |
| Loop Dependencies | 75% | 100% | Needs 3 additions |

## Contact & Questions

For questions about this analysis:
- See `/media/binyu/USB2/dev/CreatiCodeSkillMap/T29_COMPREHENSIVE_ANALYSIS.md` for full details
- All skills from `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md`
- Blocks from `/media/binyu/USB2/ScratchCopilot/blockdes8.txt`
