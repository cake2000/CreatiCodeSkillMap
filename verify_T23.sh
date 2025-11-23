#!/bin/bash
echo "=== T23 AI Perception Optimization Verification ==="
echo ""
echo "1. Total T23 Skills:"
grep "^ID: T23\." skillsv4/allskills.md | wc -l
echo "   Expected: 58"
echo ""
echo "2. New Skills Added:"
for id in T23.G5.06 T23.G6.04.04 T23.G6.06B T23.G7.01B T23.G7.06B T23.G8.01A; do
    if grep -q "^ID: $id" skillsv4/allskills.md; then
        echo "   ✅ $id found"
    else
        echo "   ❌ $id MISSING"
    fi
done
echo ""
echo "3. Backup File:"
ls -lh skillsv4/allskills_backup_T23_*.md 2>/dev/null | tail -1 | awk '{print "   "$9" ("$5")"}'
echo ""
echo "4. File Size:"
echo "   Current: $(wc -l < skillsv4/allskills.md) lines"
echo "   Backup:  $(wc -l < skillsv4/allskills_backup_T23_*.md 2>/dev/null | head -1 | awk '{print $1}') lines"
echo ""
echo "5. T23 Section Boundaries:"
echo "   Start: $(grep -n "^ID: T23.GK.01" skillsv4/allskills.md | cut -d: -f1)"
echo "   End:   $(grep -n "^ID: T24.GK.01" skillsv4/allskills.md | cut -d: -f1)"
echo ""
echo "6. Grade Distribution:"
grep -B2 "^ID: T23\." skillsv4/allskills.md | grep "^Grade:" | sort | uniq -c | awk '{print "   Grade "$2": "$1" skills"}'
echo ""
echo "7. Dependencies Check:"
echo "   T23 internal dependencies:"
grep "^ID: T23\." skillsv4/allskills.md -A20 | grep "^\* T23\." | wc -l
echo "   Cross-topic dependencies (preserved):"
grep "^ID: T23\." skillsv4/allskills.md -A20 | grep "^\* T" | grep -v "^\* T23\." | wc -l
echo ""
echo "=== Verification Complete ==="
