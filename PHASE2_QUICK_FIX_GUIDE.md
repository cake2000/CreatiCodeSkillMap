# Phase 2: Quick Fix Guide for Grade K Dependencies

**Total Fixes Needed:** 6 dependency additions

---

## Fix 1: T14.GK.02 - Add counting dependency

**Location:** T14 - 2D Games section

**Current state:**
```
ID: T14.GK.02
Topic: T14 – 2D Games
Skill: Recognize a score in simple games
Description: ...
[No dependencies listed]
```

**Add this dependency:**
```
Dependencies:
* T10.GK.02: Count items in each group
```

---

## Fix 2: T14.GK.03 - Add event sequence dependency

**Location:** T14 - 2D Games section

**Current state:**
```
ID: T14.GK.03
Topic: T14 – 2D Games
Skill: Identify when a game starts and ends
Description: ...
[No dependencies listed]
```

**Add this dependency:**
```
Dependencies:
* T06.GK.01: Order pictures showing a morning routine (event sequence concept)
```

---

## Fix 3: T26.GK.01 - Add counting dependency

**Location:** T26 - Data Collection & Logging section

**Current state:**
```
ID: T26.GK.01
Topic: T26 – Data Collection & Logging
Skill: Identify countable things in a picture
Description: ...
[No dependencies listed]
```

**Add this dependency:**
```
Dependencies:
* T10.GK.02: Count items in each group
```

---

## Fix 4: T26.GK.02 - Add counting dependency

**Location:** T26 - Data Collection & Logging section

**Current state:**
```
ID: T26.GK.02
Topic: T26 – Data Collection & Logging
Skill: Use tokens to log repeated events
Description: ...

Dependencies:
* T26.GK.01: Identify countable things in a picture
```

**Add this additional dependency (keep T26.GK.01):**
```
Dependencies:
* T10.GK.02: Count items in each group
* T26.GK.01: Identify countable things in a picture
```

---

## Fix 5: T27.GK.01 - Add sorting/grouping dependency

**Location:** T27 - Data Analysis & Storytelling section

**Current state:**
```
ID: T27.GK.01
Topic: T27 – Data Analysis & Storytelling
Skill: Sort objects by a rule and explain it
Description: ...
[No dependencies listed]
```

**Add this dependency:**
```
Dependencies:
* T10.GK.01: Sort picture cards into groups
```

---

## Fix 6: T27.GK.02 - Add sorting/grouping dependency (Optional)

**Location:** T27 - Data Analysis & Storytelling section

**Current state:**
```
ID: T27.GK.02
Topic: T27 – Data Analysis & Storytelling
Skill: Compare which group has more
Description: ...

Dependencies:
* T27.GK.01: Sort objects by a rule and explain it
```

**Option A - Add explicit dependency (recommended):**
```
Dependencies:
* T10.GK.01: Sort picture cards into groups
* T27.GK.01: Sort objects by a rule and explain it
```

**Option B - Keep as transitive (if T27.GK.01 gets T10.GK.01):**
```
Dependencies:
* T27.GK.01: Sort objects by a rule and explain it
```
(T10.GK.01 becomes reachable transitively through T27.GK.01)

**Recommendation:** Use Option A for clarity - explicit is better in educational contexts.

---

## Priority Order for Implementation

1. **High Priority (Must do first):**
   - Fix 1: T14.GK.02
   - Fix 3: T26.GK.01
   - Fix 4: T26.GK.02
   - Fix 5: T27.GK.01

2. **Medium Priority (Should do):**
   - Fix 2: T14.GK.03
   - Fix 6: T27.GK.02

---

## Validation Commands

After making changes, run these checks:

```bash
# Check that all referenced skills exist
grep "T10.GK.02:" allskills.md
grep "T06.GK.01:" allskills.md
grep "T10.GK.01:" allskills.md

# Verify no duplicate dependencies were created
grep -A 20 "ID: T14.GK.02" allskills.md | grep "Dependencies:" -A 10
grep -A 20 "ID: T14.GK.03" allskills.md | grep "Dependencies:" -A 10
grep -A 20 "ID: T26.GK.01" allskills.md | grep "Dependencies:" -A 10
grep -A 20 "ID: T26.GK.02" allskills.md | grep "Dependencies:" -A 10
grep -A 20 "ID: T27.GK.01" allskills.md | grep "Dependencies:" -A 10
grep -A 20 "ID: T27.GK.02" allskills.md | grep "Dependencies:" -A 10
```

---

## What NOT to Change

**DO NOT add T13 (debugging) dependencies to these skills:**
- T01.GK.05 (Move the picture that's in the wrong place)
- T02.GK.04 (Fix one picture that is out of order)
- T04.GK.04 (Fix a broken pattern by replacing one tile)
- T20.GK.04 (Fix the mixed-up art plan)

**Reason:** These are about sequence correction, NOT runtime debugging. Keep them in their respective algorithm/pattern topics.

**DO NOT remove these "transitive" dependencies:**
- T02.GK.03 listing both T01.GK.01 and T02.GK.02
- T02.GK.04 listing both T02.GK.02 and T02.GK.03
- T24.GK.03 listing both T24.GK.01 and T24.GK.02
- T28.GK.03 listing both T28.GK.01 and T28.GK.02
- T29.GK.03 listing both T29.GK.01 and T29.GK.02

**Reason:** Explicit is better than implicit for learning paths.

---

## Summary Statistics

**Before fixes:**
- Total GK skills: 100
- Total dependencies: 76
- Cross-topic dependencies: 15
- Missing critical links: 6

**After fixes:**
- Total GK skills: 100
- Total dependencies: 82 (+6)
- Cross-topic dependencies: 21 (+6)
- Missing critical links: 0

---

**Quick Fix Guide End**
