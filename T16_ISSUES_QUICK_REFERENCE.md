# T16 Issues Quick Reference
**Date**: 2025-11-22

---

## Summary
- **Total Issues**: 38
- **HIGH Priority**: 12 issues
- **MEDIUM Priority**: 18 issues
- **LOW Priority**: 8 issues

---

## HIGH PRIORITY (12 issues)

| # | Type | Issue | Action |
|---|------|-------|--------|
| 1 | Missing Feature | Menu bar widget not covered | ADD skill T16.G6.06 |
| 2 | Missing Feature | Hyperlink widget not covered | ADD skill T16.G4.10 |
| 7 | Vague Description | T16.G3.02 doesn't specify widget name parameter | UPDATE description |
| 8 | Missing Details | T16.G3.08 missing timing/blocking parameters | UPDATE description |
| 15 | Grade Mismatch | T16 should start G5, not G3 | DEFER to Phase 2 |
| 18 | X-2 Violation | T16.G6.04 → T16.G3.08 (3 grade gap) | ADD bridge skill T16.G5.09 |

**Quick Fixes Needed**:
- ✓ Add menu bar skill (G6)
- ✓ Add hyperlink skill (G4)
- ✓ Fix 2 vague descriptions (G3.02, G3.08)
- ✓ Add positioning comparison skill (G5.09)
- ⚠️ Grade remapping deferred to Phase 2

---

## MEDIUM PRIORITY (18 issues)

| # | Type | Issue | Action |
|---|------|-------|--------|
| 3 | Missing Pattern | Confirm dialog not explicit | UPDATE T16.G6.03.02 |
| 4 | Unclear Mechanism | Radio button grouping not explained | UPDATE T16.G4.07 |
| 5 | Missing Details | Chart type parameters not specified | UPDATE T16.G7.05 |
| 6 | Incomplete | Layout system under-explained | ADD sub-skill T16.G6.04.01 |
| 9 | Wrong Terms | "center" should be "Middle" in alignment | UPDATE T16.G4.01 |
| 10 | Missing How-To | Background image method not explained | UPDATE T16.G4.02 |
| 11 | Confusing Mix | Animation methods mixed without clarity | UPDATE T16.G5.04.02 |
| 12 | Missing Warning | HTML format complexity not warned | UPDATE T16.G5.06 |
| 13 | Incomplete Events | Toolbox value change event not mentioned | UPDATE T16.G5.07 |
| 14 | Missing Block | Enable widget block not mentioned | UPDATE T16.G6.03.02 |
| 16 | Complexity | G3 widgets too advanced | DEFER to Phase 2 |
| 17 | Complexity | Responsive layouts too hard for G6 | CONSIDER move to G7 |
| 19 | X-2 Borderline | T16.G7.05 → T16.G5.03 (2 grade gap) | ACCEPTABLE as-is |
| 20 | Same-Grade | Settings panel cluster at G4 | OPTIONAL move .01 to G5 |
| 22 | Scaffolding Gap | Jump from create to style widgets | ADD skill T16.G3.09 |
| 23 | Scaffolding Gap | Jump from single to multiple widgets | ADD skill T16.G4.11 |
| 29 | Organization | Consistent styling should be full skill | PROMOTE T16.G4.01.01 |
| 30 | Organization | Tabs should be full skill | PROMOTE T16.G4.07.01 |
| 32 | Missing Feature | Widget removal not covered | UPDATE T16.G3.07 |
| 33 | Missing Feature | Transparency block not explicit | UPDATE T16.G5.04.02 |

**Medium Updates**:
- 10 description updates
- 2 new skills (widget properties, multi-widget reading)
- 2 sub-skill promotions
- 1 optional reorganization

---

## LOW PRIORITY (8 issues)

| # | Type | Issue | Action |
|---|------|-------|--------|
| 21 | Tight Coupling | Tabs → checkbox dependency illogical | OPTIONAL fix |
| 24 | Missing Concept | Event types not explained | OPTIONAL update |
| 25 | Scaffolding Gap | Static to dynamic charts jump | OPTIONAL sub-skill |
| 26 | Missing Comparison | Plain vs rich textbox not compared | UPDATE T16.G5.06 |
| 27 | Overlap | HUD and progress bar overlap on "health" | CLARIFY descriptions |
| 28 | Overlap | Evaluate and analyze UI similar | CLARIFY descriptions |
| 31 | Organization | Progress bar & animations as sub-skills | OPTIONAL promote |
| 34 | Missing Blocks | Scale/rotate not in animations | UPDATE T16.G5.04.02 |
| 35 | Wrong Value | Z-index default may not be 10 | VERIFY & update |
| 36 | Incomplete | Camera flipped mode not mentioned | UPDATE T16.G6.05 |
| 37 | Regional | Bilibili video support unknown | CONDITIONAL update |
| 38 | Missing Concept | Widget containers not explained | UPDATE T16.G4.07.01 |

**Low Priority Notes**:
- Most are description polish
- Some are optional reorganizations
- Platform-specific features need verification

---

## ACTION CHECKLIST

### Must Do (HIGH Priority)
- [ ] Create T16.G6.06 (menu bar widget)
- [ ] Create T16.G4.10 (hyperlink widget)
- [ ] Create T16.G5.09 (positioning comparison bridge)
- [ ] Update T16.G3.02 (specify widget name parameter)
- [ ] Update T16.G3.08 (add timing/blocking details)
- [ ] Flag ISSUE #15 for Phase 2 (grade remapping)

### Should Do (MEDIUM Priority)
- [ ] Update 10 skill descriptions (issues 3,4,5,9-14)
- [ ] Add T16.G6.04.01 (layout sub-skill)
- [ ] Add T16.G3.09 (widget properties)
- [ ] Add T16.G4.11 (multi-widget reading)
- [ ] Promote T16.G4.01.01 to full skill
- [ ] Promote T16.G4.07.01 to full skill
- [ ] Update T16.G3.07 (add removal)
- [ ] Update T16.G5.04.02 (add transparency)

### Nice to Have (LOW Priority)
- [ ] Clarify 2 overlaps (issues 27, 28)
- [ ] Update 4 descriptions (issues 26, 36, 38, 34)
- [ ] Verify z-index default (issue 35)
- [ ] Check Bilibili support (issue 37)
- [ ] Optional: Fix tabs dependency (issue 21)
- [ ] Optional: Move responsive to G7 (issue 17)

---

## IMPACT ASSESSMENT

### New Skills Needed: 5-7
1. **T16.G4.10**: Hyperlink widget (HIGH)
2. **T16.G5.09**: Positioning comparison (HIGH)
3. **T16.G6.06**: Menu bar widget (HIGH)
4. **T16.G3.09**: Widget properties exploration (MED)
5. **T16.G4.11**: Multi-widget reading (MED)
6. **T16.G6.04.01**: Layout rows/cells (MED - sub-skill)
7. **T16.G7.05.01**: Update charts (LOW - sub-skill)

### Skills to Update: 12-15
Major updates needed for accuracy and completeness

### Skills to Reorganize: 2
- Promote consistent styling to full skill
- Promote tabs to full skill

### Phase 2 Deferrals: 2
- Grade level remapping (affects all T16)
- Cross-topic X-2 fixes

---

## FILES TO MODIFY

Primary file:
- `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md`

Sections affected:
- T16.G3: 2 updates + 1 new skill
- T16.G4: 5 updates + 2 new skills + 2 reorganizations
- T16.G5: 4 updates + 1 new skill + 2 sub-skills
- T16.G6: 3 updates + 2 new skills
- T16.G7: 2 updates + 1 sub-skill

Total changes: ~20-25 skill modifications

---

## VERIFICATION NEEDED

Before implementing fixes, verify:
1. ✓ Menu bar blocks exist in blockdes8.txt (confirmed)
2. ✓ Hyperlink block exists (confirmed: `add link widget`)
3. ✓ Transparency block exists (confirmed: `set transparency for widget`)
4. ✓ Scale/rotate blocks exist (confirmed: `scale widget`, `rotate widget`)
5. ? Z-index default value is 10 (needs verification)
6. ? Bilibili video support (needs verification)
7. ? Radio button grouping mechanism (needs clarification)

---

**End of Quick Reference**
