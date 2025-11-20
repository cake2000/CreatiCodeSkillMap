# Grade 8 Fix Script Documentation

## Overview

The `apply_g8_fixes.py` script automatically fixes HIGH and MEDIUM priority issues in Grade 8 skills based on the analysis in `G8_ANALYSIS_REPORT_FINAL.json`.

## What It Fixes

### 1. Circular Dependencies (8 HIGH priority)

Fixes self-references in 4 G1 skills that were causing circular dependency chains:
- **T25.G1.01** - Remove self-reference
- **T34.G1.01** - Remove self-reference
- **T35.G1.01** - Remove self-reference
- **T36.G1.01** - Remove self-reference

These G1 skills had dependencies pointing back to themselves, creating circular chains like:
```
T25.G8.02 → T25.G1.01 → T25.G1.01 (circular!)
```

### 2. Grade Constraint Violations (160+ HIGH priority)

**Rule:** Grade 8 skills can depend on G8, G7, or G6 ONLY (not G5 or lower).

The script implements a pragmatic approach:
- **Remove dependencies MORE than 2 grades lower** (G5, G4, G3, G2, G1 for G8)
- **Keep dependencies exactly 2 grades lower** (G6 is kept for G8)
- **Try to upgrade** dependencies by finding G6+ alternatives in the same topic
- **If no G6+ alternative exists**, remove the dependency and document it

#### Example Fixes:
```
T01.G8.02 depends on T01.G3.01 (G3)
→ Search for T01.G6.01 or T01.G7.01 in same topic
→ If found, replace; if not, remove
```

### 3. Transitive Dependencies (8 MEDIUM priority)

Removes redundant transitive dependencies from these G8 skills:
- **T25.G8.02, T25.G8.04**
- **T34.G8.01, T34.G8.03**
- **T35.G8.02, T35.G8.03, T35.G8.04**
- **T36.G8.04**

#### What are transitive dependencies?
If skill A depends on B, and B depends on C, then A already has C transitively.
A direct dependency from A to C is redundant.

Example:
```
T25.G8.02 → T25.G7.01 → T25.G1.01
T25.G8.02 → T25.G1.01 (redundant - already reachable via G7.01)
```

## How to Use

### Basic Usage

```bash
python3 apply_g8_fixes.py
```

### What Happens

1. **Backup Creation**: Creates `allskills.md.backup_g8_TIMESTAMP` before any changes
2. **Phase 1**: Fixes G1 self-references
3. **Phase 2**: Upgrades/removes low-grade dependencies in G8 skills
4. **Phase 3**: Removes transitive dependencies
5. **Report Generation**: Creates `G8_FIXES_APPLIED_REPORT.md` with detailed changes

### Output Files

- **Backup**: `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md.backup_g8_TIMESTAMP`
- **Report**: `/media/binyu/USB2/dev/CreatiCodeSkillMap/G8_FIXES_APPLIED_REPORT.md`
- **Modified**: `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md`

## Safety Features

1. **Automatic Backup**: Always creates timestamped backup before modifications
2. **Detailed Logging**: Shows every change as it's applied
3. **Comprehensive Report**: Documents all modifications for review
4. **Preservation**: Keeps skill descriptions and other metadata intact
5. **No Data Loss**: Only modifies dependency sections

## Expected Results

### Statistics You'll See:
- G1 self-references fixed: ~4
- G8 skills modified: ~160
- Dependencies upgraded: varies (depends on G6+ alternatives found)
- Dependencies removed: varies (when no G6+ alternative exists)
- Transitive dependencies removed: ~8

### Upgrade Patterns:
The script will report upgrade statistics like:
- G5 → G6: X
- G5 → G7: X
- G4 → G6: X
- G3 → G6: X
- G2 → G6: X
- G1 → G6: X

## How It Works Internally

### Dependency Replacement Algorithm

1. **Parse** all skills from allskills.md
2. **For each low-grade dependency**:
   - Extract topic and grade
   - Search for G6 or G7 skills in same topic
   - Prefer G6 over G7 (closer grade)
   - If found: replace dependency ID and description
   - If not found: remove dependency entirely

### Transitive Detection Algorithm

1. **Build dependency graph** for each skill
2. **Find indirect paths**: dependencies of dependencies
3. **Identify redundant edges**: direct deps that are also indirect
4. **Remove redundant deps** from dependency list

### Self-Reference Removal

1. **Parse Dependencies section** of skill
2. **Check each dependency line** for skill's own ID
3. **Remove matching lines**
4. **If no deps remain**, remove entire Dependencies section

## Validation

After running the script, you can validate with:

```bash
# Check that G8 skills no longer depend on G5 or lower
python3 << 'EOF'
import re
with open('skillsv4/allskills.md', 'r') as f:
    content = f.read()
g8_blocks = re.findall(r'ID: (T\d+\.G8\.\d+).*?Dependencies:\s*\n((?:\*.*\n)*)', content, re.DOTALL)
violations = []
for skill_id, deps in g8_blocks:
    low_deps = re.findall(r'T\d+\.G[1-5]\.\d+', deps)
    if low_deps:
        violations.append((skill_id, low_deps))
print(f"G8 skills still depending on G5 or lower: {len(violations)}")
for skill, deps in violations[:10]:
    print(f"  {skill}: {deps}")
EOF
```

## Recovery

If anything goes wrong, restore from backup:

```bash
# Find your backup
ls -lt skillsv4/allskills.md.backup_g8_* | head -1

# Restore it
cp skillsv4/allskills.md.backup_g8_TIMESTAMP skillsv4/allskills.md
```

## Design Decisions

### Why remove instead of keeping low-grade dependencies?

**Rationale**: The grade constraint rule exists to ensure proper progression. Dependencies spanning too many grades suggest:
1. The lower-grade skill is too fundamental (should be implicit)
2. There's a missing intermediate skill that should be created
3. The dependency is incorrectly specified

Removing them forces review and ensures the dependency tree is accurate.

### Why prefer G6 over G7?

**Rationale**: Closer grades mean tighter coupling to similar skill levels. G6 is more appropriate for G8 than G7, as it represents the "prerequisite tier" better.

### Why fix G1 self-references?

**Rationale**: Self-references create infinite loops in dependency resolution and are always errors. They likely occurred from copy-paste mistakes or data corruption.

## Future Enhancements

Potential improvements:
1. **Interactive mode**: Ask user before removing deps with no replacement
2. **Suggestion engine**: Use NLP to find semantic matches for replacements
3. **Dry-run mode**: Preview changes without applying
4. **Undo functionality**: Track changes for easy rollback
5. **Dependency visualization**: Generate graphs showing before/after

## Questions?

If the script encounters issues or you need to understand specific changes, check:
1. The console output (shows all changes in real-time)
2. `G8_FIXES_APPLIED_REPORT.md` (comprehensive change log)
3. The backup file (original state for comparison)

---

**Generated**: 2025-11-20
**Script Version**: 1.0
**Author**: Claude (Anthropic)
