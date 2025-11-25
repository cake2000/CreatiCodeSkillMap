# T26 Data Collection & Logging - CreatiCode Blocks Quick Reference

## LISTS (25 blocks)

| Block | Category | Purpose |
|-------|----------|---------|
| `add to [list v] item [x]` | Variables | Add item to end |
| `delete (i) of [list v]` | Variables | Delete item at index |
| `delete all of [list v]` | Variables | Clear entire list |
| `insert [x] at (i) of [list v]` | Variables | Insert at position |
| `replace item (i) of [list v] with [x]` | Variables | Replace item value |
| `reduce item (i) of [list v] by (n)` | Variables | Reduce item value by n |
| `change item (i) of [list v] by (n)` | Variables | Change item value by n |
| `delete value [v] from [list v]` | Variables | Delete first matching value |
| `reverse [list v]` | Variables | Reverse order |
| `reshuffle [list v] randomly` | Variables | Random shuffle |
| `sort list [list v] from [method v]` | Variables | Sort ascending/descending |
| `copy [list1 v] to [list2 v]` | Variables | Copy (replace target) |
| `append [list1 v] to [list2 v]` | Variables | Append to end |
| `insert (n) [selector v] items from [list1 v] into [list2 v]` | Variables | Insert filtered items |
| `set [list v] to (n) random whole numbers between (min) (max) [method v]` | Variables | Generate random numbers |
| `set [list v] to (n) random numbers with seed (s)` | Variables | Generate seeded random |
| `join [list v] into text with [sep]` | Variables | Join to string |
| `set [list v] to split of [text] with splitter [sep]` | Variables | Split string to list |
| `for each item [var v] in [list v]` | Variables | Loop through values |
| `for each index [var v] in [list v]` | Variables | Loop through indices |
| `[method v] of list [list v]` | Variables | Statistics (min/max/sum/avg/median) |
| `# of item containing [text] in [list v]` | Variables | Find substring position |
| `item (i) of [list v]` | Variables | Get item at index (reporter) |
| `length of [list v]` | Variables | Get list length (reporter) |
| `[list v] contains [x]?` | Variables | Check if contains (boolean) |

## TABLES (25 blocks)

| Block | Category | Purpose |
|-------|----------|---------|
| `add to table [t v]: [cell1] ... [cell12]` | Variables | Add row (max 12 cells) |
| `insert at row (r) of table [t v]: [cell1] ...` | Variables | Insert row at position |
| `replace row (r) of table [t v] with: [cell1] ...` | Variables | Replace row data |
| `delete row (r) of table [t v]` | Variables | Delete single row |
| `delete all rows from table [t v]` | Variables | Clear all rows |
| `delete column [col] from table [t v]` | Variables | Delete column |
| `delete all columns from table [t v]` | Variables | Clear all columns |
| `reshuffle table [t v] randomly` | Variables | Random shuffle rows |
| `sort table [t v] by column [col] [order v]` | Variables | Sort by column |
| `copy table [t1] into [t2]` | Variables | Copy (replace target) |
| `append table [t1] to [t2]` | Variables | Append rows to end |
| `row (i) of table [t v] separator [sep]` | Variables | Get row as string (reporter) |
| `row count of table [t v]` | Variables | Get row count (reporter) |
| `item at row (r) column [col] of table [t v]` | Variables | Get cell value (reporter) |
| `[method] of column [col] in table [t v]` | Variables | Column statistics (reporter) |
| `export table [t v] as [filename]` | Variables | Export as CSV |
| `import file into table [t]` | Variables | Import from CSV |
| `save table [t v] to server as [name]` | Variables | Save to server |
| `load [name] from server into table [t v]` | Variables | Load from server |
| `set table [t1 v] to [method v] of column [c1] in table [t2 v] by column [c2]` | Variables | Aggregate/group by |
| `pivot [t1] into [t2] row groups [...] columns [...] methods [...]` | Variables | Pivot table |

## DATA PERSISTENCE (10 blocks)

| Block | Category | Purpose |
|-------|----------|---------|
| `export variable [var v]` | Variables | Export to txt file |
| `import variable [var v]` | Variables | Import from txt/csv |
| `save [visibility v] data [value] with name [key]` | Variables | Save to server (public/private) |
| `load data named [key]` | Variables | Load from server (reporter) |
| `remove [visibility v] data named [key]` | Variables | Remove from server |
| `data names` | Variables | List all data keys (reporter) |
| `export table [t v] as [filename]` | Variables | Export table to CSV |
| `import file into table [t]` | Variables | Import CSV to table |
| `save table [t v] to server as [name]` | Variables | Save table to server |
| `load [name] from server into table [t v]` | Variables | Load table from server |

## DATABASE (15 blocks)

| Block | Category | Purpose |
|-------|----------|---------|
| `insert from table [t v] row from (r1) to (r2) into collection [c v]` | Database | Insert rows |
| `fetch from collection [c v] into table [t v] where <cond> limit (n) sort by ...` | Database | Query and fetch |
| `update collection [c v] from table [t v]` | Database | Update via table |
| `update collection [c v] in-place where <cond> set (f1) to (v1) ...` | Database | Direct update |
| `remove all documents from collection [c v] where <cond>` | Database | Delete rows |
| `collection [c]` | Database | Get schema (reporter) |
| `<cond (field [f]) [op v] [v2]>` | Database | Compare condition (boolean) |
| `<cond (field [f]) contains [text]?>` | Database | Contains condition (boolean) |
| `<cond <> and <>>` | Database | AND condition (boolean) |
| `<cond <> or <>>` | Database | OR condition (boolean) |
| `<cond not <>>` | Database | NOT condition (boolean) |
| `field [fieldname]` | Database | Field reference (reporter) |
| `op [in1] [operator v] [in2]` | Database | Math operation (reporter) |

## GOOGLE SHEETS (15 blocks)

| Block | Category | Purpose |
|-------|----------|---------|
| `read from google sheet: url [url] sheet name [s] range [r] into table [t v]` | Cloud | Read to table |
| `write into google sheet: url [url] sheet name [s] start cell [c] from table [t v]` | Cloud | Write from table |
| `list all sheets in google sheet at URL [url] into list [l]` | Cloud | List sheet names |
| `add sheet [s] to google sheet at URL [url]` | Cloud | Create new sheet |
| `remove sheet [s] from google sheet at URL [url]` | Cloud | Delete sheet |
| `clear sheet [s] in Google Sheet at URL [url]` | Cloud | Clear content |
| `append row (r) from table [t v] to sheet [s] in Google Sheet at URL [url]` | Cloud | Append row |
| `set value to [v] at row (r) column (c) of sheet [s] in Google Sheet at URL [url]` | Cloud | Set cell |
| `value at row (r) column (c) of sheet [s] in Google Sheet at URL [url]` | Cloud | Get cell (reporter) |
| `insert (n) rows at row (r) in sheet [s] in Google Sheet at URL [url]` | Cloud | Insert rows |
| `insert (n) columns at column (c) in sheet [s] in Google Sheet at URL [url]` | Cloud | Insert columns |
| `remove rows [r1] to [r2] from sheet [s] in Google Sheet at URL [url]` | Cloud | Delete rows |
| `remove columns [c1] to [c2] from sheet [s] in Google Sheet at URL [url]` | Cloud | Delete columns |

## LOGGING (3 blocks)

| Block | Category | Purpose |
|-------|----------|---------|
| `print [msg] in [window v] color [color]` | Control | Log to console/alert |
| `get console log` | Control | Get all console output (reporter) |

## MULTIPLAYER (5 blocks)

| Block | Category | Purpose |
|-------|----------|---------|
| `create game named [name] password [pwd] my name [host] role [role] server [loc v] capacity (n) world width (w) height (h)` | Multiplayer | Create game |
| `list players in game [name] hosted by [host] from server [loc v] in table [t v]` | Multiplayer | List players |
| `reset game world` | Multiplayer | Reset game |
| `synchronously set speed x (x) y (y)` | Multiplayer | Sync sprite speed |
| `synchronously set speed (s) dir (d)` | Multiplayer | Sync speed+direction |

---

## TOTAL: 105+ blocks for data collection and logging

---

## QUICK PATTERNS

### Pattern 1: Simple Survey Loop (G3.01)
```
ask [What is your favorite color?] and wait
add (answer) to [responses v]
```

### Pattern 2: Count Events (G3.03)
```
when [space v] key pressed
change [jump_count v] by (1)
```

### Pattern 3: Log to Table (G4.02)
```
add to table [sensor_data v]:
  (timer) (temperature) (humidity) [] [] ...
```

### Pattern 4: Export CSV (G5.04)
```
export table [results v] as [experiment_data]
```

### Pattern 5: Google Sheets Sync (G6+)
```
write into google sheet:
  url [https://docs.google.com/spreadsheets/d/YOUR_ID/...]
  sheet name [Sheet1]
  start cell [A1]
  from table [collected_data v]
```

### Pattern 6: Console Logging (G5.01)
```
print (join [Collected ] (count) [ responses]) in [console v] color [#00FF00]
```

### Pattern 7: Validation Loop (G5.02)
```
repeat until <(answer) > [0]>
  ask [Enter a positive number:] and wait
  if <(answer) < [1]> then
    print [Invalid input!] in [console v] color [#FF0000]
  end
end
```

### Pattern 8: Privacy Check (G4.04)
```
ask [May we collect your age? (yes/no)] and wait
if <(answer) = [yes]> then
  ask [What is your age?] and wait
  add (answer) to [ages v]
else
  print [Skipped - user declined] in [console v] color [#FFAA00]
end
```

---

## FILE FORMATS

- **TXT**: Plain text export/import
- **CSV**: Table export/import (comma-separated values)
- **Google Sheets**: Full read/write integration
- **JSON**: Via database collections

---

## STORAGE COMPARISON

| Type | Persistence | Scope | Best For |
|------|-------------|-------|----------|
| Variables | Session only | Local | Temporary data |
| Lists | Session only | Local | Ordered collections |
| Tables | Session only | Local | Structured data |
| Export/Import | File system | User computer | Offline backup |
| Server Key-Value | Permanent | Project | Simple persistent data |
| Server Tables | Permanent | Project | Persistent structured data |
| Database | Permanent | Project | Complex queries |
| Google Sheets | Permanent | External | Collaboration |
| Multiplayer | Game session | Game world | Real-time sharing |

---

## SKILL → BLOCK MAPPING

### T26.G3.01: Survey loop
- `ask [] and wait`
- `add () to [list v]`
- `repeat ()`

### T26.G3.03: Event logging with counters
- `when [key v] pressed`
- `change [var v] by ()`
- `set [var v] to ()`

### T26.G3.04: Separate raw from summary
- Lists for raw data
- Variables for summaries
- `[method v] of list [list v]` for aggregation

### T26.G4.02: Multi-attribute logging
- `add to table [t v]: [] [] [] ...`
- `item at row () column [] of table [t v]`

### T26.G5.01: Print logging
- `print [] in [console v] color []`

### T26.G5.04: Export to CSV
- `export table [t v] as []`

### T26.G6.01: Stakeholder mapping
- Use tables with columns: stakeholder, data_needed, purpose

### T26.G7.01: Reusable collection module
- Custom blocks (My Blocks)
- Parameters for flexible inputs

### T26.G8.01: Telemetry pipeline
- Database operations
- Scheduled exports
- Google Sheets integration

---

## LIMITS & CONSTRAINTS

- **Table blocks**: Up to 12 cells per operation
- **Database sorting**: Up to 2 fields
- **Database update**: Up to 4 fields at once
- **List indices**: 1-based (first item = 1)
- **Server data**: Project-scoped only
- **Semantic database**: One per project

---

**For detailed analysis:** See T26_DATA_BLOCKS_ANALYSIS.md
**Source:** /media/binyu/USB2/ScratchCopilot/blockdes8.txt
**Date:** 2025-11-25
