# T26 Optimization - Quick Reference

## Critical Findings

**Coverage Gap:** T26 currently covers only **44% (11/25)** of CreatiCode's data collection features.

**Missing Major Features:**
1. Cloud storage (save/load data by name)
2. Database collections (MongoDB-style CRUD)
3. Player score recording & leaderboards
4. Google Sheets integration (comprehensive)
5. Sensor data to tables (face/hand/pose/body)
6. Console logging (print blocks)
7. Semantic databases (embedding search)
8. Multiplayer data logging
9. Variable file export/import
10. Advanced data operations

---

## Recommended Changes Summary

### New Skills to Add: 12

| Grade | Skill ID | Title | Priority |
|-------|----------|-------|----------|
| G5 | G5.05 | Save and load table data from cloud storage | CRITICAL |
| G5 | G5.06 | Record and display player scores with leaderboards | CRITICAL |
| G5 | G5.07 | Collect face detection data into a table | HIGH |
| G5 | G5.08 | Export and import variables to files | MEDIUM |
| G6 | G6.05 | Insert data into a database collection | CRITICAL |
| G6 | G6.06 | Query data from a database collection | CRITICAL |
| G6 | G6.07 | Import data from Google Sheets into tables | CRITICAL |
| G6 | G6.08 | Export data to Google Sheets for collaboration | CRITICAL |
| G6 | G6.09 | Log multiplayer game session data | HIGH |
| G7 | G7.05 | Update and delete database records | HIGH |
| G7 | G7.06 | Update and append data in Google Sheets | HIGH |
| G8 | G8.05 | Create and query a semantic database | HIGH |

### Skills to Modify: 6

| Skill ID | Current Issue | Modification Needed |
|----------|---------------|---------------------|
| G5.01 | Confuses console logging with list logging | Add explicit console logging with `print [] in [console v]` |
| G5.02 | Violates X-2 rule (depends on K skills) | Remove T26.GK.02 and T26.GK.03 dependencies |
| G6.02 | Too vague about sensor data | Specify face/hand/pose/body detection to tables |
| G6.03 | Missing cloud/database privacy | Add privacy for cloud storage, databases, leaderboards, Google Sheets |
| G7.03 | CSV import not explicit | Expand to explicitly teach `import file into table []` |
| G8.01 | Too abstract | Add specific blocks for each pipeline stage |

---

## New Skill Count by Grade

| Grade | Current Skills | New Skills | Modified Skills | Total Skills |
|-------|----------------|------------|-----------------|--------------|
| K | 3 | 0 | 0 | 3 |
| G1 | 3 | 0 | 0 | 3 |
| G2 | 5 | 0 | 0 | 5 |
| G3 | 5 | 0 | 0 | 5 |
| G4 | 4 | 0 | 0 | 4 |
| G5 | 4 | +4 | +2 | 8 |
| G6 | 4 | +5 | +2 | 9 |
| G7 | 4 | +2 | +1 | 6 |
| G8 | 4 | +1 | +1 | 5 |
| **Total** | **40** | **+12** | **+6** | **52** |

---

## Implementation Phases

### Phase 1: Critical Gaps (Immediate Priority)
These enable foundational cloud/database workflows.

1. **G5.05** - Cloud save/load tables
2. **G5.06** - Leaderboards
3. **G6.05** - Database insert
4. **G6.06** - Database query
5. **G6.07** - Google Sheets import
6. **G6.08** - Google Sheets export

**Impact:** Enables cloud persistence, game scoring, database storage, collaborative data

---

### Phase 2: Advanced Features (High Priority)
These enable sensor data, advanced operations, AI features.

7. **G5.07** - Face detection to table
8. **G6.02 (MODIFY)** - All sensor data to tables
9. **G7.05** - Database update/delete
10. **G7.06** - Google Sheets append/update
11. **G8.05** - Semantic database

**Impact:** Enables AI perception data logging, full database CRUD, semantic search

---

### Phase 3: Supporting Features (Medium Priority)
These improve existing skills and add supporting features.

12. **G5.01 (MODIFY)** - Console logging
13. **G5.08** - Variable export
14. **G6.09** - Multiplayer data
15. **G6.03 (MODIFY)** - Privacy updates
16. **G7.03 (MODIFY)** - CSV import expansion
17. **G8.01 (MODIFY)** - Pipeline specificity

**Impact:** Improves debugging, file I/O, multiplayer analytics, privacy coverage

---

## Key CreatiCode Blocks to Cover

### Cloud Storage
```
save table [tt v] to server as [mydata]
load [mydata] from server into table [tt v]
```

### Database Collections
```
insert from table [t v] rows [1] to [10] into collection [items]
fetch from collection [items] condition [type = "weapon"] limit [20] into table [t v]
update collection [items] from table [t v]
remove rows from collection [items] where [quantity = 0]
```

### Leaderboards
```
record player score (100)
show game leaderboard [highest v] rows [10] header [#0000FF] background [#FFFFFF]
hide game leaderboard
```

### Google Sheets
```
read from google sheet: url [URL] sheet name [Sheet1] range [A1:D10] into table [t v]
write into google sheet: url [URL] sheet name [Sheet1] starting cell [A1] from table [t v]
append row (1) from table [t v] to sheet [Sheet1] in Google Sheet at URL [URL]
```

### Sensor Data to Tables
```
run face detection debug [yes v] and write into table [faces v]
run 3D pose detection debug [yes v] table [poses v]
run hand detection table [hands v] debug [yes v] show video [yes v]
run 2D body part recognition into table [bodyparts v]
```

### Console Logging
```
print [Debug: level started] in [console v] color [#FF0000]
get console log
```

### Semantic Database
```
create semantic database from table [faq v]
search semantic database with [what is your refund policy?] store top (3) in table [results v]
```

---

## Coverage Improvement

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| **Total Skills** | 40 | 52 | +12 (+30%) |
| **Feature Coverage** | 11/25 (44%) | 25/25 (100%) | +14 features |
| **G5 Skills** | 4 | 8 | +4 |
| **G6 Skills** | 4 | 9 | +5 |
| **G7 Skills** | 4 | 6 | +2 |
| **G8 Skills** | 4 | 5 | +1 |

---

## Cross-Topic Dependencies

### New skills integrate with:
- **T10** (Lists & Tables): All new skills use tables
- **T23** (AI Perception): G5.07, G6.02 log sensor data
- **T22** (Chatbots): G8.05 semantic database enables FAQ bots
- **T19** (Multiplayer): G6.09 logs multiplayer sessions
- **T14** (Games): G5.06 leaderboards bridge games and data
- **T27** (Data Analysis): All new collection skills feed analysis

---

## Privacy & Ethics Integration

### Modified Privacy Coverage:
- **G6.03** expanded to include:
  - Cloud storage privacy (consent before saving)
  - Database privacy (opt-out from collection inserts)
  - Leaderboard privacy (anonymous vs named scores)
  - Google Sheets privacy (data sharing implications)

### Privacy Skill Progression:
- **G4.04**: Basic privacy reflection (personal data)
- **G6.03**: Consent workflows + cloud/database privacy
- **G7.03**: External dataset provenance
- **G8.04**: Data privacy agreements

---

## Quick Skill Lookup

### Cloud & Persistence
- G5.05: Cloud save/load
- G5.08: Variable export
- G6.05: Database insert
- G6.06: Database query
- G7.05: Database update/delete

### Collaboration & Sharing
- G6.07: Google Sheets import
- G6.08: Google Sheets export
- G7.06: Google Sheets append/update

### Games & Engagement
- G5.06: Leaderboards
- G6.09: Multiplayer data

### AI & Sensors
- G5.07: Face detection to table
- G6.02: All sensor data to tables
- G8.05: Semantic database

### Debugging & Development
- G5.01: Console logging
- G5.04: CSV export
- G7.03: CSV import

---

## Next Steps

1. **Review** this analysis with curriculum team
2. **Prioritize** Phase 1 skills for immediate implementation
3. **Draft** detailed skill descriptions for new skills
4. **Validate** dependencies across all new skills
5. **Create** example projects for each new skill
6. **Update** auto-grading system for new challenges

---

**Full Analysis:** See `/media/binyu/USB2/dev/CreatiCodeSkillMap/T26_OPTIMIZATION_ANALYSIS.md`

**Related Documents:**
- `/media/binyu/USB2/dev/CreatiCodeSkillMap/T26_COMPREHENSIVE_ANALYSIS.md` (original analysis)
- `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/skills_T26_data_collection_organization.md` (current skills)
