# T31 Internet & Cloud - Migration Mapping

## Quick Reference: Old ID → New ID Mapping

This document provides a quick lookup table for migrating from old T31 skill IDs to new optimized IDs.

## Unchanged Skills (Same ID, Updated Content)

These skills kept their original IDs but have improved descriptions with specific block names:

| ID | Skill Title | Notes |
|----|-------------|-------|
| T31.GK.01 | Recognize devices that connect to internet | Description unchanged |
| T31.G1.01 | Identify when device is connected/disconnected | Description unchanged |
| T31.G2.01 | Understand internet connects many computers | Description unchanged |
| T31.G2.02 | Practice safe online behavior | Description unchanged |
| T31.G3.01 | Trace simple path from device to website | Description unchanged |
| T31.G3.02 | Recognize different types of online info sharing | Description unchanged |
| T31.G4.01 | Explain how data travels across internet | Description unchanged |
| T31.G4.02 | Identify secure vs insecure websites | Description unchanged |
| T31.G5.01 | Trace how device reaches online service | Description unchanged |
| T31.G5.02 | Decide when apps need internet vs offline | Description unchanged |
| T31.G5.03 | Fetch and display web page as markdown | Now includes specific block name |
| T31.G6.01 | Trace steps of HTTP/HTTPS request | Description unchanged |
| T31.G6.02 | Read data from Google Sheet | Now includes specific block name |
| T31.G6.03 | Write data to Google Sheet | Now includes specific block name |
| T31.G7.01 | Model distributed multiplayer server | Description unchanged |

## Renamed/Renumbered Skills

### Grade 5 Changes

| Old ID | Old Title | New ID | New Title | Notes |
|--------|-----------|--------|-----------|-------|
| T31.G5.04 | Create and join multiplayer game | **SPLIT INTO TWO** | | |
| | | T31.G5.05 | Create multiplayer game | "Create" operation only |
| | | T31.G5.06 | Join multiplayer game | "Join" operation only |
| T31.G5.04.01 | List available multiplayer games | T31.G5.07 | List available multiplayer games | Renumbered up |
| T31.G5.05 | Check multiplayer connection status | T31.G5.08 | Check multiplayer connection status | Renumbered up |

**New Grade 5 Additions:**
- T31.G5.04: Access user identity (NEW - username, user id, user avatar blocks)

### Grade 6 Changes

| Old ID | Old Title | New ID | New Title | Notes |
|--------|-----------|--------|-----------|-------|
| T31.G6.04 | Measure latency affects AI | T31.G6.10 | Measure latency affects AI | Renumbered to make room |
| T31.G6.05 | Evaluate privacy AI data | T31.G6.11 | Evaluate privacy AI data | Renumbered to make room |
| T31.G6.06 | Add sprites to multiplayer game | T31.G6.12 | Add sprites to multiplayer game | Renumbered to make room |
| T31.G6.06.01 | Manage players and game state | **SPLIT INTO TWO** | | |
| | | T31.G6.13 | Remove sprites from game | "Remove sprite" operation |
| | | T31.G6.15 | List players in game | "List players" operation |
| T31.G6.03.01 | Update entire rows in Google Sheets | T31.G6.04 | Set individual cell values | Changed to more specific skill |
| T31.G6.03.02 | List and manage multiple Google Sheets | T31.G6.07 | Manage Google Sheets structure | Focused on list/add/remove sheet blocks |
| T31.G6.03.03 | Manage Google Sheets structure programmatically | T31.G6.09 | Modify Google Sheet structure | Focused on insert/remove rows/columns |

**New Grade 6 Additions:**
- T31.G6.04: Set individual cell values (NEW - "set value to" block)
- T31.G6.05: Read individual cell values (NEW - "value at row column" block)
- T31.G6.06: Append rows to Google Sheet (NEW - "append row" block)
- T31.G6.08: Clear Google Sheet data (NEW - "clear sheet" block)
- T31.G6.14: Use "when added to game" event (NEW)
- T31.G6.16: Create cloud session (NEW)
- T31.G6.17: Join cloud session (NEW)
- T31.G6.18: Save cloud data (NEW)
- T31.G6.19: Load cloud data (NEW)
- T31.G6.20: Access Google Drive folder contents (NEW - moved from G8.04.01)
- T31.G6.21: Read URL parameters (NEW)

### Grade 7 Changes - MAJOR RESTRUCTURE

**Old structure had database nested under movement (T31.G7.02.03-05)**
**New structure has separate top-level skills**

| Old ID | Old Title | New ID | New Title | Notes |
|--------|-----------|--------|-----------|-------|
| T31.G7.02 | Synchronize sprite movement | T31.G7.02 | Synchronize sprite movement | Kept ID, focused on movement only |
| T31.G7.02.01 | Broadcast messages | T31.G7.03 | Broadcast messages | Promoted to top level |
| T31.G7.02.02 | Handle sprite collisions | T31.G7.04 | Handle sprite collisions | Promoted to top level |
| T31.G7.02.03 | Insert data into database | T31.G7.06 | Insert data into database | Promoted to top level |
| T31.G7.02.04 | Fetch data from database | T31.G7.07 | Fetch data from database | Promoted to top level |
| T31.G7.02.04.01 | Use advanced database queries | **SPLIT INTO TWO** | | Eliminated 3-level nesting |
| | | T31.G7.08 | Build query conditions (comparison) | Comparison operators |
| | | T31.G7.09 | Build query conditions (text/logical) | Text search + and/or/not |
| T31.G7.02.05 | Update and remove database records | **SPLIT INTO TWO** | | |
| | | T31.G7.10 | Update database records | Update operations only |
| | | T31.G7.11 | Remove database records | Delete operations only |
| T31.G7.03 | Compare network topology options | T31.G7.20 | Compare network topology options | Renumbered to end |
| T31.G7.04 | Client-server vs peer-to-peer | T31.G7.21 | Client-server vs peer-to-peer | Renumbered to end |
| T31.G7.05 | Analyze societal impacts | T31.G7.22 | Analyze societal impacts | Renumbered to end |

**New Grade 7 Additions:**
- T31.G7.05: Reset multiplayer game world (NEW)
- T31.G7.12: Use database field/collection reporters (NEW)
- T31.G7.13: Record player scores (NEW - leaderboard)
- T31.G7.14: Display game leaderboard (NEW)
- T31.G7.15: Manage leaderboard (NEW - hide/clear/remove)
- T31.G7.16: Store and read user data (NEW)
- T31.G7.17: Create semantic database (NEW)
- T31.G7.18: Search semantic database (basic) (NEW)
- T31.G7.19: Search semantic database (with conditions) (NEW)

### Grade 8 Changes

| Old ID | Old Title | New ID | New Title | Notes |
|--------|-----------|--------|-----------|-------|
| T31.G8.01 | Architect edge vs cloud AI | T31.G8.01 | Architect edge vs cloud AI | ID unchanged |
| T31.G8.02 | Understand AI service network reqs | T31.G8.02 | Understand AI service network reqs | ID unchanged |
| T31.G8.03 | Design secure AI cloud systems | T31.G8.03 | Design secure AI cloud systems | ID unchanged |
| T31.G8.04 | Implement privacy protection | T31.G8.04 | Implement privacy protection | ID unchanged |
| T31.G8.04.01 | Integrate Google Drive folder access | T31.G6.20 | Access Google Drive folder contents | MOVED to Grade 6 (implementation skill) |
| T31.G8.05 | Evaluate AI service resilience | T31.G8.05 | Evaluate AI service resilience | ID unchanged |
| T31.G8.06 | Build AI monitoring dashboards | T31.G8.06 | Build AI monitoring dashboards | ID unchanged |

## Migration Strategy

### For Lesson Plans Referencing Old IDs

1. **Check the mapping table above** for your old skill ID
2. **If "SPLIT INTO TWO"** - Update lesson to cover both new skills separately
3. **If "Renumbered"** - Simply update the ID in your documentation
4. **If "Unchanged"** - No changes needed (though description may be improved)

### For Assessment Rubrics

1. **Granular skills need granular rubrics** - One old skill that split needs two rubrics
2. **Update skill IDs** in all rubrics to match new numbering
3. **Preserve assessment criteria** - Learning objectives haven't changed, just organization

### For Student Progress Tracking

1. **Map old completions to new IDs** using this table
2. **For split skills** - If student completed old T31.G5.04, mark both T31.G5.05 and T31.G5.06 complete
3. **For renamed skills** - Simple ID update

## Common Patterns

### Pattern 1: Broad Skill Split
When one skill covered multiple operations, it was split:
- **Old:** T31.G5.04 (Create AND join)
- **New:** T31.G5.05 (Create), T31.G5.06 (Join)

### Pattern 2: Misplaced Skill Promoted
When skill was wrongly nested, it was promoted:
- **Old:** T31.G7.02.03 (Database under Movement)
- **New:** T31.G7.06 (Database as top-level)

### Pattern 3: 3-Level Eliminated
When 3-level nesting existed, it was flattened:
- **Old:** T31.G7.02.04.01 (Query operators)
- **New:** T31.G7.08 (Top-level Grade 7 skill)

### Pattern 4: Missing Feature Added
When blocks had no skills, new skills were created:
- **Old:** (none - leaderboard blocks not covered)
- **New:** T31.G7.13-15 (Complete leaderboard coverage)

## Validation Checklist

When updating references to T31 skills:

- [ ] Updated all lesson plan references
- [ ] Updated all assessment rubrics
- [ ] Updated all project tags
- [ ] Updated student progress records
- [ ] Updated curriculum maps
- [ ] Updated cross-topic dependencies (other topics referencing T31)
- [ ] Verified no broken links in documentation
- [ ] Tested new skill progression with sample students

## Quick Lookup: New Additions (No Old ID)

These skills are completely new and have no old equivalent:

**Grade 5:**
- T31.G5.04: User identity blocks (username, user id, user avatar)

**Grade 6:**
- T31.G6.04: Set individual cell values
- T31.G6.05: Read individual cell values
- T31.G6.06: Append rows to Google Sheet
- T31.G6.08: Clear Google Sheet data
- T31.G6.14: "when added to game" event
- T31.G6.16-19: Cloud sessions (4 skills)
- T31.G6.20: Google Drive folder access (moved from G8)
- T31.G6.21: Read URL parameters

**Grade 7:**
- T31.G7.05: Reset game world
- T31.G7.12: Database field/collection reporters
- T31.G7.13-16: Leaderboard and user data (4 skills)
- T31.G7.17-19: Semantic database (3 skills)

**Total new additions: 18 skills**

## Contact for Migration Support

If you encounter issues migrating from old to new skill IDs:
1. Refer to this mapping document first
2. Check T31_Phase1_Optimization_Summary.md for detailed explanations
3. Review T31_optimized_section.md for complete new skill definitions
4. Consult T31_BLOCK_COVERAGE_REFERENCE.md for block-to-skill mappings

---

*Last Updated: 2025-11-25*
*Migration Version: 1.0*
*Covers: T31.GK.01 through T31.G8.06*
