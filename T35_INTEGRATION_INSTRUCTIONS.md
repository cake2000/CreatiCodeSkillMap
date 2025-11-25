# T35 Integration Instructions

## How to Integrate Optimized T35 Skills into allskills.md

### Step 1: Backup Current File
```bash
cp skillsv4/allskills.md skillsv4/allskills_backup_before_T35_optimization_$(date +%s).md
```

### Step 2: Locate T35 Section
The T35 section in allskills.md starts at approximately line 29850 with:
```
ID: T35.GK.01
Topic: T35 – Impacts & Ethics
Skill: Identify a helpful use of technology
```

And ends before the next topic (T36) starts:
```
ID: T36.GK.01
Topic: T36 – Careers, Collaboration & Future Paths
```

### Step 3: Replace Section
1. Open allskills.md in your editor
2. Find the T35 section (search for "ID: T35.GK.01")
3. Select all T35 skills (from T35.GK.01 through T35.G8.04)
4. Replace with the content from `T35_OPTIMIZED_COMPLETE.md`

### Step 4: Verify Cross-Topic References
After integration, check if any other topics reference old T35 skill IDs that have been broken down:

**Skills that were broken down and need cross-topic reference updates:**
- T35.G4.01 → Now T35.G4.01.01, T35.G4.01.02, T35.G4.01.03
- T35.G5.01 → Now T35.G5.01.01, T35.G5.01.02, T35.G5.01.03
- T35.G6.01 → Now T35.G6.01.01, T35.G6.01.02, T35.G6.01.03, T35.G6.01.04
- T35.G6.03.01 → Now T35.G6.03.01a, T35.G6.03.01b, T35.G6.03.01c
- T35.G7.01.01 → Now T35.G7.01.01a, T35.G7.01.01b, T35.G7.01.01c
- T35.G7.03 → Now T35.G7.03.01, T35.G7.03.02, T35.G7.03.03
- T35.G7.05.01 → Now T35.G7.05.01a, T35.G7.05.01b, T35.G7.05.01c
- T35.G8.01 → Now T35.G8.01.01, T35.G8.01.02, T35.G8.01.03
- T35.G8.03.01 → Now T35.G8.03.01a, T35.G8.03.01b, T35.G8.03.01c

**Search commands to find cross-topic references:**
```bash
# Check if other topics depend on T35.G4.01 (now broken into 3)
grep -n "T35\.G4\.01[^.]" skillsv4/allskills.md | grep -v "^ID: T35"

# Check if other topics depend on T35.G5.01 (now broken into 3)
grep -n "T35\.G5\.01[^.]" skillsv4/allskills.md | grep -v "^ID: T35"

# Repeat for other broken-down skills...
```

**How to update cross-topic references:**
- If a topic depends on old T35.G4.01, decide which sub-skill it actually needs:
  - T35.G4.01.01 if it needs case study organization
  - T35.G4.01.02 if it needs widget building
  - T35.G4.01.03 if it needs tradeoff analysis
  - Keep all three if it needs the complete sequence

### Step 5: Validate Changes

**Run validation checks:**
```bash
# 1. Count total T35 skills (should be 71)
grep "^ID: T35\." skillsv4/allskills.md | wc -l

# 2. Count by grade
for grade in GK G1 G2 G3 G4 G5 G6 G7 G8; do
  count=$(grep "^ID: T35\.$grade\." skillsv4/allskills.md | wc -l)
  echo "$grade: $count skills"
done

# Expected output:
# GK: 4 skills
# G1: 4 skills
# G2: 4 skills
# G3: 4 skills
# G4: 7 skills
# G5: 8 skills
# G6: 13 skills
# G7: 17 skills
# G8: 10 skills

# 3. Check for broken dependencies (dependencies that don't exist)
# This will extract all T35 dependencies and check if they exist
grep "^\* T35\." skillsv4/allskills.md | sort -u > /tmp/t35_deps.txt
grep "^ID: T35\." skillsv4/allskills.md | sed 's/ID: //' | sed 's/ .*//' | sort > /tmp/t35_ids.txt
comm -23 /tmp/t35_deps.txt /tmp/t35_ids.txt
# Should output nothing (all dependencies exist)
```

### Step 6: Test Run Analysis Script
If you have the runall.js script:
```bash
node runall.js --topic T35
```

This should analyze all 66 T35 skills and verify:
- All dependencies exist
- No circular dependencies
- X-2 rule compliance
- Proper grade progression

### Step 7: Update Documentation
After successful integration, update:
1. Topic overview documents
2. Teacher guides referencing T35
3. Lesson plans using old T35 IDs
4. Assessment rubrics

### Step 8: Communicate Changes
Notify stakeholders of:
1. **24 new skills** (from breakdowns and additions)
2. **Renumbered skills** (T35.G4.01 → T35.G4.01.01-03, etc.)
3. **Dependency fix** (T35.G5.03 now depends on T09.G4.01 not T09.G3.03)
4. **Clarified skills** (T35.G2.02, T35.G2.03, T35.G5.02, T35.G6.04)

---

## Quick Integration Script

If you want to automate the integration:

```bash
#!/bin/bash
# integrate_t35.sh

# 1. Backup
cp skillsv4/allskills.md skillsv4/allskills_backup_before_T35_optimization_$(date +%s).md

# 2. Extract everything before T35
sed -n '1,/^ID: T35\.GK\.01/p' skillsv4/allskills.md | head -n -1 > /tmp/before_t35.txt

# 3. Extract everything after T35 (starting with T36)
sed -n '/^ID: T36\./,$p' skillsv4/allskills.md > /tmp/after_t35.txt

# 4. Combine: before + optimized T35 + after
cat /tmp/before_t35.txt > skillsv4/allskills_new.md
echo "" >> skillsv4/allskills_new.md
cat T35_OPTIMIZED_COMPLETE.md | grep -v "^# T35" >> skillsv4/allskills_new.md
echo "" >> skillsv4/allskills_new.md
cat /tmp/after_t35.txt >> skillsv4/allskills_new.md

# 5. Validate
echo "Validation:"
echo "Total T35 skills: $(grep '^ID: T35\.' skillsv4/allskills_new.md | wc -l) (should be 71)"

# 6. If validation passes, replace
# mv skillsv4/allskills_new.md skillsv4/allskills.md
```

**Note:** Review the merged file manually before replacing the original!

---

## Rollback Plan

If issues are found after integration:

```bash
# Find the most recent backup
ls -lt skillsv4/allskills_backup_before_T35_optimization_*.md | head -1

# Restore it
cp skillsv4/allskills_backup_before_T35_optimization_TIMESTAMP.md skillsv4/allskills.md
```

---

## Post-Integration Checklist

- [ ] Backup created
- [ ] T35 section replaced with optimized version
- [ ] Cross-topic references checked and updated
- [ ] Skill count verified (71 total)
- [ ] Grade distribution verified (GK:4, G1:4, G2:4, G3:4, G4:7, G5:8, G6:13, G7:17, G8:10)
- [ ] Dependency validation passed (no broken dependencies)
- [ ] X-2 rule compliance verified
- [ ] runall.js analysis passed
- [ ] Documentation updated
- [ ] Stakeholders notified
- [ ] Changes committed to version control

---

## Expected Results After Integration

### File Changes
- **allskills.md**: ~71 T35 skills (was 50)
- **Size increase**: ~21 additional skills worth of content

### Analysis Results
When running analysis tools, expect:
- **No X-2 violations** (fixed T35.G5.03)
- **No overly broad skills** (all broken down)
- **Complete progression** (K-8 with scaffolding)
- **Clear dependencies** (sequential within breakdowns)

### Benefits
1. **Teachers**: Clearer learning objectives, easier assessment
2. **Students**: Better scaffolding, focused practice
3. **Curriculum**: No gaps, proper progression, comprehensive AI ethics

---

## Support

If you encounter issues during integration:

1. **Check file locations**: Ensure paths are correct
2. **Verify formatting**: T35 skills should match allskills.md format
3. **Review dependencies**: Use grep to find broken references
4. **Test incrementally**: Integrate one grade at a time if needed
5. **Keep backups**: Never delete old versions until validated

For questions or issues, refer to:
- `T35_OPTIMIZATION_SUMMARY.md` - Detailed changes
- `T35_QUICK_REFERENCE.md` - Skill listings
- `T35_OPTIMIZED_COMPLETE.md` - Full optimized content
