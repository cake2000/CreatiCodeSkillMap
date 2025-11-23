# T29 Visual Issue Summary

## TOPIC OVERVIEW
**T29 - Text Data & NLP Foundations**
- **Scope**: K-8 text processing and natural language understanding
- **Current Skills**: 56 skills
- **Proposed Skills**: ~70 core skills (78 with optional)
- **Issues Found**: 36 total (18 high, 12 medium, 6 low)

---

## ISSUE HEAT MAP BY GRADE

```
Grade K:  ✅ OK (no issues)
Grade 1:  ✅ OK (no issues)
Grade 2:  ✅ OK (no issues)
Grade 3:  ⚠️ MINOR (1 missing skill)
Grade 4:  🔴 CRITICAL (9 issues - reordering, overload, missing foundations)
Grade 5:  ⚠️ MODERATE (5 issues - splitting complex skills, adding scaffolding)
Grade 6:  ⚠️ MODERATE (4 issues - regex too advanced, missing skills)
Grade 7:  🔴 HIGH (6 issues - missing feature, dependency violations, splits needed)
Grade 8:  ⚠️ MINOR (3 issues - scope creep, need moves from earlier grades)
```

---

## TOP 5 CRITICAL ISSUES

### 🔴 #1: GRADE 4 SEQUENCING DISASTER
**Issue**: Foundation skill (split/join) comes AFTER advanced skills (AI summaries)
**Impact**: Students try to use AI before understanding basic text manipulation
**Fix**: Reorder entire G4 sequence - put split/join FIRST
**Priority**: CRITICAL - FIX IMMEDIATELY

---

### 🔴 #2: MISSING CREATICODE FEATURE
**Issue**: T29.G7.06 references "AI moderation blocks" that don't exist
**Impact**: Skill is completely unimplementable
**Fix**: DELETE or replace with keyword-based filter
**Priority**: CRITICAL - FIX IMMEDIATELY

---

### 🔴 #3: REGEX IN GRADE 6
**Issue**: Regular expressions introduced in 6th grade
**Impact**: Developmentally inappropriate; regex is typically HS/college topic
**Fix**: Move T29.G6.05 → T29.G8.05
**Priority**: HIGH - FIX IN PHASE 1

---

### 🔴 #4: COMPLEX SKILL WITHOUT SCAFFOLDING
**Issue**: T29.G4.08 "Count words and report most frequent" combines 5+ sub-tasks
**Impact**: Too much cognitive load; students need step-by-step guidance
**Fix**: Break into T29.G5.08.01 + T29.G5.08.02, move to G5
**Priority**: HIGH - FIX IN PHASE 1

---

### 🔴 #5: MISSING FOUNDATIONAL SKILLS
**Issue**: Multiple missing prerequisites:
- No text input/output skill
- No text equality comparison skill
- No simple tables for text skill
**Impact**: Students jump into complex operations without basics
**Fix**: Add T29.G4.00, T29.G3.05, T29.G4.10
**Priority**: HIGH - FIX IN PHASE 1

---

## ISSUES BY CATEGORY

### A. SEQUENCING/ORDERING ISSUES (5)
1. ✅ G4 split/join comes after AI summaries (H9)
2. ✅ Case-insensitive matching before case conversion taught (H17)
3. ✅ Word frequency too early (before stop-words) (H2)
4. ✅ Sentiment analysis without concept introduction (H13)
5. ✅ Tables schema before tables introduction (H6)

**Fix Approach**: Reorder skills, add prerequisites

---

### B. MISSING SKILLS (14)
1. ✅ Text input/output (ask/answer blocks) - T29.G4.00
2. ✅ Text equality comparison - T29.G3.05
3. ✅ Simple tables for text - T29.G4.10
4. ✅ Emotional tone recognition - T29.G4.11
5. ✅ Tokenization concepts - T29.G5.10
6. ✅ Text normalization pipelines - T29.G5.11
7. ✅ Multiline text processing - T29.G5.12
8. ✅ Text length limits - T29.G6.09
9. ✅ Input validation - T29.G6.10
10. ✅ Stop-words concept - T29.G5.03.01
11. ⭐ Text encoding (optional) - T29.G7.07
12. ⭐ Compare manual vs AI sentiment (optional) - T29.G7.08
13. ⭐ Multilingual text (optional) - T29.G7.09
14. ⭐ Capstone project (optional) - T29.G8.06

**Fix Approach**: Add 10 core skills, 4 optional skills

---

### C. SKILLS TOO COMPLEX (7)
1. ✅ T29.G4.08 - Word frequency (split into 2)
2. ✅ T29.G5.03 - Stop-words (split into 2)
3. ✅ T29.G7.01 - Mini-RAG (split into 2)
4. ✅ T29.G8.01 - Text pipelines (clarify description)
5. ⚠️ T29.G5.06 - Parse sentence (consider split)
6. ⚠️ T29.G7.02 - ML feature engineering (move to G8)
7. ⚠️ T29.G8.02 - Precision/recall/F1 (move to T22 or simplify)

**Fix Approach**: Split into sub-skills with .01/.02 IDs

---

### D. GRADE-INAPPROPRIATE SKILLS (3)
1. ✅ T29.G6.05 - Regex in G6 (move to G8)
2. ✅ T29.G7.02 - ML in G7 with G6 dependency (move to G8)
3. ⚠️ T29.G8.02 - Too much math for text topic (consider moving to T22)

**Fix Approach**: Move to later grades or different topics

---

### E. DEPENDENCY VIOLATIONS (4)
1. ✅ T29.G4.01.02 → T29.G4.02 (both in G4, wrong order) - H9
2. ✅ T29.G7.02 → T22.G6.01 (X-2 violation) - H11
3. ✅ T29.G7.04 → T29.G6.03 (unrelated dependency) - M6
4. ✅ T29.G8.01 missing custom blocks dependency - M2

**Fix Approach**: Reorder, remove unnecessary deps, add missing deps

---

### F. MISSING/WRONG FEATURES (2)
1. ✅ T29.G7.06 - AI moderation blocks don't exist - H1
2. ⚠️ T29.G5.04 - No sentiment API (workaround with ChatGPT) - Partial alignment

**Fix Approach**: Remove, replace, or document workarounds

---

### G. DESCRIPTION CLARITY (5)
1. ✅ T29.G3.03 - Doesn't emphasize coding vs unplugged G1.03 - H15
2. ✅ T29.G5.06 - "Analyze" vs "parse" sentence - L1
3. ✅ T29.G6.08 - Unclear if manual or built-in edit distance - M9
4. ✅ T29.G8.01 - Vague pipeline description - M1
5. ⚠️ Multiple skills - Text vs string terminology - L3

**Fix Approach**: Rewrite descriptions for clarity

---

## SKILL REDISTRIBUTION

### Skills LEAVING Each Grade
```
G4 LOSES:
  - T29.G4.08 → T29.G5.08 (word frequency)
  - T29.G4.09 → T29.G5.09 (highlight keywords)

G6 LOSES:
  - T29.G6.05 → T29.G8.05 (regex)

G7 LOSES:
  - T29.G7.02 → T29.G8.07 (ML feature engineering)
  - T29.G7.06 → DELETED (AI moderation)
```

### Skills JOINING Each Grade
```
G3 GAINS:
  + T29.G3.05 - Text equality comparison

G4 GAINS:
  + T29.G4.00 - Text I/O
  + T29.G4.10 - Simple tables
  + T29.G4.11 - Emotional tone
  + (reordered existing skills)

G5 GAINS:
  + T29.G5.03.01/.02 - Stop-words (split)
  + T29.G5.08.01/.02 - Word frequency (from G4, split)
  + T29.G5.09 - Highlight keywords (from G4)
  + T29.G5.10 - Tokenization
  + T29.G5.11 - Normalization pipelines
  + T29.G5.12 - Multiline text

G6 GAINS:
  + T29.G6.09 - Length limits
  + T29.G6.10 - Input validation

G7 GAINS:
  + T29.G7.01.01/.02 - Mini-RAG (split)
  + T29.G7.07 - Text encoding (optional)
  + T29.G7.08 - Compare sentiment (optional)
  + T29.G7.09 - Multilingual (optional)

G8 GAINS:
  + T29.G8.05 - Regex (from G6)
  + T29.G8.06 - Capstone project (optional)
  + T29.G8.07 - ML features (from G7)
```

---

## GRADE 4 BEFORE/AFTER

### BEFORE (9 skills, poor ordering)
```
T29.G4.01.01 - Compare human vs AI summaries ❌ (comes before foundation)
T29.G4.01.02 - Generate AI summaries ❌ (comes before foundation)
T29.G4.02 - Use split and join ⭐ (FOUNDATION - should be first!)
T29.G4.03 - Access characters
T29.G4.04 - Count characters/words
T29.G4.05 - Test includes/starts/ends ❌ (before case conversion)
T29.G4.06.01 - Convert case
T29.G4.06.02 - Remove punctuation
T29.G4.07 - Extract substrings
T29.G4.08 - Word frequency ❌ (too complex, needs stop-words)
T29.G4.09 - Highlight keywords ❌ (better fit in G5)
```

### AFTER (12 skills, logical progression)
```
T29.G4.00 - Text I/O (ask/answer) ✅ NEW
T29.G4.01 - Use split and join ✅ FOUNDATION FIRST!
T29.G4.02 - Access characters ✅
T29.G4.03 - Count characters/words ✅
T29.G4.04.01 - Convert case ✅ MOVED EARLIER
T29.G4.04.02 - Test includes/starts/ends ✅ AFTER CASE
T29.G4.05.01 - Compare human vs AI summaries ✅ AFTER FOUNDATION
T29.G4.05.02 - Generate AI summaries ✅ AFTER FOUNDATION
T29.G4.06 - Remove punctuation ✅
T29.G4.07 - Extract substrings ✅
T29.G4.10 - Simple tables for text ✅ NEW
T29.G4.11 - Emotional tone recognition ✅ NEW
```
*(Word frequency and highlight keywords moved to G5)*

---

## ALIGNMENT WITH CREATICODE BLOCKS

### ✅ WELL SUPPORTED (14 skill types)
- Split/join (list blocks)
- Letter # of, length of (Scratch built-in)
- Case conversion (operator_texttransform)
- String comparison (includes, starts, ends)
- Trim (operator_trim)
- Substring (operator_substring)
- Regex (operator_regex_*)
- Parse sentence (ai_parsesentence)
- Speech-to-text (ai_startspeech, ai_startopenaispeech)
- Text-to-speech (ai_speakinlanguage)
- Edit distance (operator_stringdiff)
- Pinecone semantic search
- ChatGPT integration
- Web search (googlesearch)

### ⚠️ PARTIAL SUPPORT (3 skill types)
- Sentiment analysis (workaround: manual OR ChatGPT prompt)
- Token counting (workaround: estimate from char/word count)
- Emotional tone (workaround: manual labeling OR ChatGPT)

### ❌ NOT SUPPORTED (1 skill type)
- AI content moderation (NO BLOCKS EXIST)
  - **Fix**: Remove T29.G7.06 or replace with keyword filter

---

## IMPLEMENTATION ROADMAP

### PHASE 1: CRITICAL FIXES (Week 1)
**Goal**: Fix sequencing disasters and remove broken skills

```
□ Reorder all Grade 4 skills (new sequence)
□ Add T29.G4.00 (text I/O)
□ Add T29.G3.05 (text equality)
□ Remove/replace T29.G7.06 (AI moderation)
□ Move T29.G6.05 → T29.G8.05 (regex)
□ Split T29.G4.08 → T29.G5.08.01 + T29.G5.08.02
```

**Impact**: Fixes 6 critical issues affecting 15+ skills

---

### PHASE 2: ADD SCAFFOLDING (Week 2)
**Goal**: Add missing prerequisite and bridging skills

```
□ Add T29.G4.10 (simple tables)
□ Add T29.G4.11 (emotional tone)
□ Split T29.G5.03 → .01 + .02 (stop-words)
□ Add T29.G5.10 (tokenization concepts)
□ Add T29.G6.09 (length limits)
□ Add T29.G6.10 (input validation)
□ Split T29.G7.01 → .01 + .02 (mini-RAG)
□ Move T29.G7.02 → T29.G8.07 (ML features)
```

**Impact**: Adds 8 core skills, improves learning progression

---

### PHASE 3: ENHANCEMENTS (Week 3-4)
**Goal**: Add advanced/optional skills and polish descriptions

```
□ Add T29.G5.11 (normalization pipelines)
□ Add T29.G5.12 (multiline text)
□ Add T29.G7.07 (text encoding - optional)
□ Add T29.G7.08 (compare sentiment - optional)
□ Add T29.G7.09 (multilingual - optional)
□ Add T29.G8.06 (capstone project - optional)
□ Update all skill descriptions per clarity guidelines
□ Fix all dependency references
```

**Impact**: Adds 6 optional skills, improves all descriptions

---

## SUCCESS METRICS

### Before Fixes
- ❌ 18 high-priority issues
- ❌ 12 medium-priority issues
- ❌ 6 low-priority issues
- ❌ 1 completely broken skill (T29.G7.06)
- ❌ Grade 4 sequencing disaster
- ❌ 56 skills with uneven distribution

### After Phase 1
- ✅ 0 broken skills
- ✅ Grade 4 properly sequenced
- ✅ All critical dependencies fixed
- ⚠️ ~12 medium-priority issues remain
- ⚠️ 6 low-priority issues remain
- ✅ ~62 skills

### After Phase 2
- ✅ All high-priority issues resolved
- ✅ Strong scaffolding in place
- ⚠️ ~6 low-priority issues remain
- ✅ ~70 core skills

### After Phase 3
- ✅ All issues resolved
- ✅ Optional enrichment available
- ✅ Clear, specific descriptions
- ✅ Complete dependency graph
- ✅ ~78 total skills (70 core + 8 optional)

---

## RISK ASSESSMENT

### HIGH RISK if Not Fixed
1. **Grade 4 sequencing** - Students will be confused and frustrated
2. **T29.G7.06 broken skill** - Teachers/students hit dead end
3. **Regex in G6** - Developmentally inappropriate, likely failure
4. **Missing foundations** - Students lack prerequisites for success

### MEDIUM RISK if Not Fixed
1. **Complex skills without splits** - High cognitive load, some students fall behind
2. **Missing scaffolding skills** - Learning gaps, uneven progression
3. **Dependency violations** - Curriculum changes break other topics

### LOW RISK if Not Fixed
1. **Description clarity** - Minor confusion, but students can still succeed
2. **Optional skills missing** - Curriculum works but less enrichment
3. **Terminology inconsistencies** - Minimal impact on learning

---

## NEXT STEPS

1. ✅ **Review this analysis** with curriculum team
2. ✅ **Approve Phase 1 fixes** for immediate implementation
3. ✅ **Assign Phase 2 skills** to curriculum developers
4. ✅ **Decide on optional skills** - which to include in core vs advanced track
5. ✅ **Update allskills.md** systematically
6. ✅ **Create lesson plans** for new skills
7. ✅ **Test sequence** with pilot teachers/students

---

**END OF VISUAL SUMMARY**
