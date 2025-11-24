# T33 Actionable Fixes - Quick Reference
**Date:** 2024-11-24

## Critical Issues Requiring Immediate Attention

### 1. SPLIT THESE 8 BROAD SKILLS

#### T33.G6.06 → Split into 3 skills
**Current:** Handle latency and error states in service calls
**Split into:**
- **T33.G6.06a**: Display loading indicators during service calls
- **T33.G6.06b**: Detect and display error messages from failed calls
- **T33.G6.06c**: Implement "try again" retry mechanisms

#### T33.G7.01 → Split into 3 skills
**Current:** List, add, and remove sheets in a Google Spreadsheet
**Split into:**
- **T33.G7.01a**: List sheets in a Google Spreadsheet
- **T33.G7.01b**: Add new sheets to organize data
- **T33.G7.01c**: Remove sheets dynamically

#### T33.G7.05 → Split into 3 skills
**Current:** Synchronize variables across projects using cloud sessions
**Split into:**
- **T33.G7.05a**: Understand cloud session isolation
- **T33.G7.05b**: Create and join cloud sessions
- **T33.G7.05c**: Synchronize variables across session members

#### T33.G7.07 → Split into 3 skills
**Current:** Build workflows that combine multiple services
**Split into:**
- **T33.G7.07a**: Chain web fetch with AI processing
- **T33.G7.07b**: Read from Sheets, process, and write results
- **T33.G7.07c**: Coordinate sequential service calls with dependencies

#### T33.G7.10 → Split into 3 skills
**Current:** Query cloud collections with WHERE conditions
**Split into:**
- **T33.G7.10a**: Use simple WHERE conditions with comparison operators
- **T33.G7.10b**: Use contains operator for text searches
- **T33.G7.10c**: Reference field values in WHERE conditions

#### T33.G7.11 → Split into 3 skills
**Current:** Update and delete cloud collection data
**Split into:**
- **T33.G7.11a**: Update collections from modified tables
- **T33.G7.11b**: Update collections in-place with WHERE conditions
- **T33.G7.11c**: Delete documents with WHERE conditions

#### T33.G7.12 → Split into 3 skills
**Current:** Build complex collection queries with AND/OR/NOT logic
**Split into:**
- **T33.G7.12a**: Combine conditions with AND and OR logic
- **T33.G7.12b**: Use NOT to invert conditions
- **T33.G7.12c**: Add LIMIT and SORT BY to optimize queries

#### T33.G8.01 → Consider splitting into 2 skills
**Current:** Insert and remove rows and columns dynamically in Google Sheets
**Option to split into:**
- **T33.G8.01a**: Insert and remove rows dynamically
- **T33.G8.01b**: Insert and remove columns dynamically

---

### 2. FIX THESE DEPENDENCY VIOLATIONS (X-2 Rule)

#### G6 Skills with G5 Dependencies (2 violations)

**T33.G6.09** - Understand cloud database collections versus Google Sheets
```
BEFORE: T10.G5.01
AFTER:  T10.G6.01 (Sort a table by a column)
```

**T33.G6.10** - Insert and fetch data from cloud database collections
```
BEFORE: T08.G5.01, T10.G5.01
AFTER:  T08.G6.01 (Use conditionals to control simulation steps)
        T10.G6.01 (Sort a table by a column)
```

#### G7 Skills with G5 Dependencies (10 violations)

**T33.G7.01** - Sheet management
```
BEFORE: T08.G5.01, T10.G5.01, T31.G5.01
AFTER:  T08.G6.01, T10.G6.01, T31.G6.01
```

**T33.G7.02** - Cell operations
```
BEFORE: T08.G5.01, T10.G5.01, T31.G5.01
AFTER:  T08.G6.01, T10.G6.01, T31.G6.01
```

**T33.G7.03** - Append rows
```
BEFORE: T08.G5.01, T10.G5.01, T31.G5.01
AFTER:  T08.G6.01, T10.G6.01, T31.G6.01
```

**T33.G7.04** - Google Drive folder
```
BEFORE: T08.G5.01, T10.G5.01, T31.G5.01
AFTER:  T08.G6.01, T10.G6.01, T31.G6.01
```

**T33.G7.05** - Cloud sessions
```
BEFORE: T09.G5.01, T31.G5.01
AFTER:  T09.G6.01, T31.G6.01
```

**T33.G7.06** - Service authorization
```
BEFORE: T08.G5.01, T31.G5.01
AFTER:  T08.G6.01, T31.G6.01
```

**T33.G7.07** - Multi-service workflows
```
BEFORE: T06.G5.01, T09.G5.01, T31.G5.01
AFTER:  T06.G6.01, T09.G6.01, T31.G6.01
```

**T33.G7.08** - Compare service options
```
BEFORE: T08.G5.01, T31.G5.01
AFTER:  T08.G6.01, T31.G6.01
```

**T33.G7.09** - Cache responses
```
BEFORE: T09.G5.01, T10.G5.01, T31.G5.01
AFTER:  T09.G6.01, T10.G6.01, T31.G6.01
```

**T33.G7.10** - WHERE conditions
```
BEFORE: T08.G5.01, T10.G5.01, T31.G5.01
AFTER:  T08.G6.01, T10.G6.01, T31.G6.01
```

**T33.G7.11** - Update/delete collections
```
BEFORE: T08.G5.01, T10.G5.01, T31.G5.01
AFTER:  T08.G6.01, T10.G6.01, T31.G6.01
```

#### G7 Skills with Mixed Violations (1 violation)

**T33.G7.12** - Complex queries
```
BEFORE: T08.G6.01, T10.G5.01, T31.G6.01
AFTER:  T08.G6.01, T10.G6.01, T31.G6.01
```

---

### 3. ADD THESE 5 MISSING FOUNDATION SKILLS

#### T33.G6.05b - Check if service call succeeded
**Placement:** Between T33.G6.05 and T33.G6.06
**Description:** Students learn to check if a Cloud block call succeeded by examining the returned value. They use if-else to test for empty strings or error indicators. They create simple "success" or "failed" messages.
**Dependencies:** T08.G4.01, T09.G4.01, T33.G6.02

#### T33.G6.09b - Identify collection blocks and their purposes
**Placement:** Between T33.G6.09 and T33.G6.10
**Description:** Students explore Database category blocks: insert, fetch, update, remove. They identify which blocks read data versus write data. They compare collection block parameters to Google Sheets block parameters.
**Dependencies:** T33.G6.09

#### T33.G6.10b - Understand collection documents and fields
**Placement:** After T33.G6.10, before T33.G7.10
**Description:** Students learn that collection records are called "documents" and each document has named fields. They examine a sample collection's data structure. They map document fields to table columns.
**Dependencies:** T10.G6.01, T33.G6.10

#### T33.G7.06b - Call two services in sequence
**Placement:** Between T33.G7.06 and T33.G7.07
**Description:** Students practice calling two Cloud blocks in sequence: first call completes, then use its result in second call. They ensure first call finishes before starting second. They build simple two-step workflows (e.g., fetch URL, then write to Sheet).
**Dependencies:** T09.G6.01, T31.G6.01, T33.G6.02, T33.G6.04

#### T33.G7.09b - Understand query field references
**Placement:** Between T33.G7.09 and T33.G7.10
**Description:** Students learn the `field [FIELDNAME]` block syntax used in database queries. They understand that field blocks refer to column names in collection documents. They practice constructing simple field references before using them in WHERE conditions.
**Dependencies:** T10.G6.01, T33.G6.10b

---

### 4. ADDRESS GRADE-INAPPROPRIATE CONTENT

#### T33.G6.07 - Respect usage limits and rate limiting
**Issue:** Too complex for G6 - requires implementing counters and timers
**Options:**
1. **Simplify:** Change to "Understand that services have usage limits" (conceptual)
2. **Move to G7:** Keep implementation focus but move up one grade
3. **Split:** G6 = understand limits exist, G7 = implement rate limiting

**Recommendation:** Simplify for G6, add implementation skill in G7

#### T33.G7.09 - Cache service responses
**Issue:** Implementing cache with timestamps and expiration is complex
**Options:**
1. **Simplify:** Remove timestamp/expiration, just basic caching
2. **Move to G8:** Keep full implementation but move up one grade
3. **Split:** G7 = basic cache lookup, G8 = add expiration logic

**Recommendation:** Simplify for G7 (basic caching), add advanced caching in G8

#### T33.G7.06 - Understand automatic service authorization
**Issue:** Purely conceptual, no hands-on component
**Options:**
1. **Add hands-on:** Have students test with/without account, explore limitations
2. **Make it a note:** Add to G6.01 or G7.06b as extended information
3. **Combine:** Merge with another skill as a "why this works" section

**Recommendation:** Make it a note in T33.G6.01 (when introducing Cloud blocks)

#### T33.G8.02 - Review terms of service
**Issue:** This is literacy/ethics, not a coding skill
**Options:**
1. **Move to ethics track:** Not a T33 skill
2. **Add coding component:** Build TOS compliance checker
3. **Make it cross-topic:** Add TOS notes to multiple topics

**Recommendation:** Move to separate ethics/digital citizenship curriculum OR add coding component (analyze project for compliance)

---

## Quick Dependency Replacement Guide

### Common G5 → G6/G7 Replacements

| OLD (G5) | NEW (G6/G7) | Topic |
|----------|-------------|-------|
| T06.G5.01 | T06.G6.01 | Events - multi-event programs |
| T08.G5.01 | T08.G6.01 | Conditionals - control simulations |
| T09.G5.01 | T09.G6.01 | Variables - model quantities |
| T10.G5.01 | T10.G6.01 | Tables - sort tables |
| T31.G5.01 | T31.G6.01 | Networks - HTTP/HTTPS requests |

---

## Skill Count Changes

### Before Fixes:
- K-5: 8 skills
- G6: 10 skills
- G7: 12 skills
- G8: 6 skills
- **Total: 36 skills**

### After Fixes:
- K-5: 8 skills (no change)
- G6: 13-14 skills (+3-4: split G6.06, add 2 foundation skills)
- G7: 20-22 skills (+8-10: split G7.01, G7.05, G7.07, G7.10, G7.11, G7.12, add 3 foundation skills)
- G8: 7-9 skills (+1-3: possibly split G8.01, add advanced caching)
- **Total: 48-53 skills**

---

## Priority Order for Implementation

### Phase 1: Fix Dependency Violations (2-3 hours)
1. Update all G6 dependencies (2 skills)
2. Update all G7 dependencies (11 skills)
3. Verify no circular dependencies

### Phase 2: Split Critical Broad Skills (1 day)
1. Split T33.G7.01 (sheet management)
2. Split T33.G7.11 (update/delete)
3. Split T33.G6.06 (error handling)
4. Update all dependencies pointing to these skills

### Phase 3: Split Remaining Broad Skills (1 day)
1. Split T33.G7.05 (cloud sessions)
2. Split T33.G7.10 (WHERE conditions)
3. Split T33.G7.12 (complex queries)
4. Split T33.G7.07 (workflows)
5. Decide on T33.G8.01 (rows/columns)

### Phase 4: Add Foundation Skills (4 hours)
1. Add T33.G6.05b (check success)
2. Add T33.G6.09b (identify blocks)
3. Add T33.G6.10b (document structure)
4. Add T33.G7.06b (two services)
5. Add T33.G7.09b (field references)

### Phase 5: Address Grade-Inappropriate Content (2 hours)
1. Simplify or move T33.G6.07 (rate limiting)
2. Simplify or move T33.G7.09 (caching)
3. Address T33.G7.06 (authorization)
4. Address T33.G8.02 (TOS review)

---

## Testing Checklist

After implementing fixes:
- [ ] No X-2 rule violations remain
- [ ] No skills depend on themselves (direct or indirect)
- [ ] All split skills have updated descriptions
- [ ] All skills align with actual CreatiCode blocks
- [ ] Grade levels are appropriate for complexity
- [ ] Scaffolding gaps are filled
- [ ] Total skill count is reasonable (~48-53)
- [ ] K-5 foundation remains unchanged
- [ ] G6 introduces blocks properly
- [ ] G7 develops skills appropriately
- [ ] G8 provides capstone experiences

---

## Questions for Curriculum Team

1. **Collection timing:** Should G6.09/G6.10 stay in G6 or move to G7?
2. **Rate limiting:** Simplify, move, or split T33.G6.07?
3. **Caching:** Keep complex caching in G7 or move to G8?
4. **TOS review:** Keep in T33 or move to ethics curriculum?
5. **Target skill count:** Aim for ~50 skills or try to stay under 45?
6. **Row/column operations:** Keep T33.G8.01 as one skill or split?
7. **Authorization:** Add hands-on component or make it a note?
8. **Workflow patterns:** Are 3 workflow skills enough or need more?

---

## Files to Update

1. `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md` - Main skills file
2. Any visualization or summary documents referencing T33
3. Dependency tracking spreadsheets
4. Assessment/rubric materials for affected skills

---

**END OF ACTIONABLE FIXES**
