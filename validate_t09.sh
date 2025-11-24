#!/bin/bash
echo "==================================="
echo "T09 Optimization Validation Report"
echo "==================================="
echo ""

echo "1. Backup File:"
ls -lh skillsv4/allskills_backup_before_T09_optimization_*.md 2>/dev/null | tail -1
echo ""

echo "2. Total T09 Skills:"
grep -c "^ID: T09\." skillsv4/allskills.md
echo "   Expected: 73"
echo ""

echo "3. New Skills Added (should show 12):"
echo "   T09.G3.01.05 (reporter blocks):"
grep -c "^ID: T09.G3.01.05" skillsv4/allskills.md
echo "   T09.G3.02.01 (reduce block):"
grep -c "^ID: T09.G3.02.01" skillsv4/allskills.md
echo "   T09.G4.01.01 (subtraction):"
grep -c "^ID: T09.G4.01.01" skillsv4/allskills.md
echo "   T09.G4.02.01 (division):"
grep -c "^ID: T09.G4.02.01" skillsv4/allskills.md
echo "   T09.G4.06.01, .02, .03 (comparison ops):"
grep -c "^ID: T09.G4.06.0[1-3]" skillsv4/allskills.md
echo "   T09.G5.03.01 (multi-join):"
grep -c "^ID: T09.G5.03.01" skillsv4/allskills.md
echo "   T09.G6.04.01 (case conversion):"
grep -c "^ID: T09.G6.04.01" skillsv4/allskills.md
echo "   T09.G6.05.01 (substring):"
grep -c "^ID: T09.G6.05.01" skillsv4/allskills.md
echo "   T09.G7.01.02, .03 (math functions):"
grep -c "^ID: T09.G7.01.0[2-3]" skillsv4/allskills.md
echo ""

echo "4. Dependency Fixes:"
echo "   T09.G3.06 now depends on G3.01.02 (not G3.02):"
grep -A 2 "^ID: T09.G3.06" skillsv4/allskills.md | grep "T09.G3.01.02"
echo "   T09.G4.05 has added dependencies:"
grep -A 4 "^ID: T09.G4.05" skillsv4/allskills.md | grep -c "Dependencies:" 
echo ""

echo "5. No T10 or other topics affected:"
echo "   First T10 skill still at expected location:"
grep -n "^ID: T10.GK.01" skillsv4/allskills.md | head -1
echo ""

echo "6. Skills by Grade:"
for grade in K 1 2 3 4 5 6 7 8; do
  count=$(grep -c "^ID: T09.G${grade}\." skillsv4/allskills.md)
  echo "   Grade ${grade}: ${count} skills"
done
echo ""

echo "7. Summary Documents Created:"
ls -1 T09_*.md 2>/dev/null | grep -E "(Phase1|QUICK)" | head -5
echo ""

echo "==================================="
echo "Validation Complete"
echo "==================================="
