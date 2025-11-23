# T31 Quick Fix Reference

## CRITICAL FIXES NEEDED

### 1. Database Insert (T31.G7.02.03) - WRONG DESCRIPTION
**Current (INCORRECT):**
"Students use CreatiCode's Database blocks to insert documents into a cloud-based collection"

**Should Be:**
"Students use CreatiCode's Database blocks to prepare data in a table, then insert rows from the table into a cloud-based collection. The table serves as intermediate storage."

**Why:** CreatiCode doesn't support direct insertion. Must use table first.

---

### 2. Google Sheets Read (T31.G6.02) - INCOMPLETE
**Add:** Mention both single-cell (`p2p_getvalue`) AND range (`p2p_readfromgooglesheet`) operations

---

### 3. Google Sheets Write (T31.G6.03) - INCOMPLETE
**Add:** Mention both single-cell (`p2p_setvalue`) AND table (`p2p_writeintogooglesheet`) operations

---

### 4. Sprite Lifecycle (T31.G6.06) - MISSING REMOVAL
**Add:** Mention `mp_removespritefromgame` block alongside adding sprites

---

### 5. Database Queries (T31.G7.02.04) - MISSING OPERATORS
**Add Explicitly:**
- `database_contains` - text search
- `database_not`, `database_and`, `database_or` - boolean logic
- `database_operator` - arithmetic (+, -, *, /)

---

## NEW SKILLS TO ADD

### G5 Level
**T31.G5.04.01** - List available multiplayer games
- Block: `mp_listmultiplayergames`

### G6 Level
**T31.G6.06.01** - List players in game
- Block: `mp_listmultiplayergameusers`

**T31.G6.03.03** - Advanced Google Sheets structure
- Blocks: `p2p_insertrowsinsheet`, `p2p_removerowsfromsheet`, `p2p_insertcolumnsinsheet`, `p2p_removecolumnsfromsheet`, `p2p_clearsheet`

### G7 Level
**T31.G7.02.02.01** - Reset multiplayer game
- Block: `mp_resetmultiplayergame`

### G8 Level
**T31.G8.04.01** - Google Drive integration
- Block: `p2p_getgooglefoldercontent`

---

## MISSING BLOCKS NOT YET COVERED

### Cloud Category (6 blocks)
1. `p2p_insertrowsinsheet` - Insert rows
2. `p2p_removerowsfromsheet` - Remove rows
3. `p2p_insertcolumnsinsheet` - Insert columns
4. `p2p_removecolumnsfromsheet` - Remove columns
5. `p2p_clearsheet` - Clear entire sheet
6. `p2p_getgooglefoldercontent` - List Google Drive files

### Multiplayer Category (3 blocks)
1. `mp_listmultiplayergames` - List games on server
2. `mp_listmultiplayergameusers` - List players in game
3. `mp_resetmultiplayergame` - Reset game world

### Database Category (1 block)
1. `database_collection` - Get collection schema

---

## BLOCK COUNTS

**Total Internet/Cloud Blocks:** 40
- Cloud: 15
- Multiplayer: 13
- Database: 13

**Coverage:**
- Well Covered: 22 (55%)
- Partially Covered: 9 (23%)
- Not Covered: 9 (22%)

---

## PRIORITY ORDER

1. Fix database insert description (CRITICAL ERROR)
2. Expand Google Sheets read/write (INCOMPLETE)
3. Add missing multiplayer discovery blocks
4. Add advanced Google Sheets operations
5. Add Google Drive integration
