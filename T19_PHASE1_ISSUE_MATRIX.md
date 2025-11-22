# T19 Phase 1 - Issue Priority Matrix

**Visual guide for prioritizing T19 optimization work**

---

## 🔴 HIGH PRIORITY - Must Fix (11 Issues)

| ID | Issue | Impact | Effort | Fix Type | Blocks Other Work? |
|----|-------|---------|--------|----------|-------------------|
| H1 | No K-5 skills | 🔥🔥🔥 | 3h | Add Skills | ✅ YES - Foundation |
| H2 | Missing G6 foundations | 🔥🔥🔥 | 2h | Add Skills | ✅ YES - Scaffolding |
| H3 | Heavy G6→G6 chaining | 🔥🔥🔥 | 1h | Remove Deps | ❌ No |
| H4 | Inconsistent numbering | 🔥🔥 | 2h | Rename | ❌ No |
| H5 | Skills too broad | 🔥🔥🔥 | 3h | Split Skills | ⚠️ Maybe |
| H6 | Testing too late | 🔥🔥🔥 | 30m | Reorder | ❌ No |
| H7 | Missing cross-topic deps | 🔥🔥 | 1h | Add Deps | ❌ No |
| H8 | No first game milestone | 🔥🔥🔥 | 2h | Restructure | ⚠️ Maybe |
| H9 | Dependency title mismatches | 🔥🔥 | 30m | Fix Refs | ❌ No |
| H10 | Vague conceptual descriptions | 🔥🔥 | 2h | Rewrite | ❌ No |
| H11 | Missing error handling | 🔥🔥 | 1h | Add Skill | ❌ No |

**Total High Priority Effort:** ~18 hours
**Critical Path Items:** H1, H2, H5, H8 (must complete before others)

---

## 🟡 MEDIUM PRIORITY - Should Fix (15 Issues)

| ID | Issue | Impact | Effort | Fix Type | Notes |
|----|-------|---------|--------|----------|-------|
| M1 | Vague conceptual descriptions | 🔥🔥 | 2h | Enhance | Add observable outcomes |
| M2 | Missing cross-topic deps | 🔥🔥 | 1h | Add Deps | T09, T10, T11, T14 |
| M3 | Duplicate concept explanations | 🔥 | 1h | Remove | Redundant replication, sync |
| M4 | Missing testing criteria | 🔥🔥 | 2h | Enhance | All implementation skills |
| M5 | Unclear T19.G6.00D dependency | 🔥 | 10m | Remove | T14.G4.01 not needed |
| M6 | Age-inappropriate jargon | 🔥 | 1h | Rewrite | Replace technical terms |
| M7 | Missing actionable outcomes (G7) | 🔥🔥 | 2h | Enhance | Add deliverables |
| M8 | Inconsistent dependency naming | 🔥 | 1h | Audit | Fix all cross-topic refs |
| M9 | Missing parameter understanding | 🔥 | 30m | Add Dep | T11.G5.01 |
| M10 | Over-specified implementation | 🔥 | 30m | Rewrite | Make flexible |
| M11 | Missing "room" concept | 🔥 | 30m | Enhance | Add to description |
| M12 | Unclear G6→G7 progression | 🔥 | 30m | Document | Add conceptual shift |
| M13 | Missing error handling | 🔥🔥 | 1h | Add Skill | Common errors |
| M14 | No capstone project | 🔥🔥 | 1h | Add Skill | T19.G6.13 |
| M15 | Redundant player list skills | 🔥 | 30m | Clarify | Different purposes |

**Total Medium Priority Effort:** ~15 hours

---

## 🔵 LOW PRIORITY - Nice to Have (6 Issues)

| ID | Issue | Impact | Effort | Fix Type | Notes |
|----|-------|---------|--------|----------|-------|
| L1 | Consider K-2 conceptual skills | 🔥 | 3h | Add Skills | Unplugged concepts |
| L2 | Visual diagrams in descriptions | 🔥 | 2h | Enhance | ASCII art |
| L3 | Split G6 into G6A/G6B | 🔥 | 2h | Reorganize | Semester split |
| L4 | Game design patterns skill | 🔥 | 1h | Add Skill | Common patterns |
| L5 | Ethics/safety skill | 🔥 | 1h | Add Skill | Digital citizenship |
| L6 | Playtesting skill | 🔥 | 1h | Add Skill | Peer testing |

**Total Low Priority Effort:** ~10 hours

---

## 📊 EFFORT vs IMPACT MATRIX

```
HIGH IMPACT, LOW EFFORT (Do First!)     HIGH IMPACT, HIGH EFFORT (Critical Path)
┌─────────────────────────┐              ┌─────────────────────────┐
│ H3  Remove G6→G6 deps   │              │ H1  Add K-5 skills      │
│ H6  Move testing early  │              │ H2  Add G6 foundations  │
│ H7  Add cross-deps      │              │ H5  Split broad skills  │
│ H9  Fix title mismatches│              │ H8  Restructure for     │
│ M5  Remove wrong dep    │              │     first game          │
└─────────────────────────┘              └─────────────────────────┘
        (4-5 hours)                              (10 hours)

LOW IMPACT, LOW EFFORT (Quick Wins)     LOW IMPACT, HIGH EFFORT (Defer)
┌─────────────────────────┐              ┌─────────────────────────┐
│ M9  Add T11 dependency  │              │ H4  Renumber all skills │
│ M10 Make tag flexible   │              │ L1  Add K-2 skills      │
│ M11 Add room concept    │              │ L2  Add diagrams        │
│ M12 Document progression│              │ L3  Split G6 into 2     │
└─────────────────────────┘              └─────────────────────────┘
        (2 hours)                                (8 hours)
```

---

## 🎯 RECOMMENDED IMPLEMENTATION SEQUENCE

### Week 1: Foundation Fixes (8 hours)
**Goal:** Fix structural issues that block other work

1. **H1** - Add T19.G5.01 (local 2-player bridge) - 3h
2. **H2** - Add missing G6 foundations (lag, testing) - 2h
3. **H6** - Move testing earlier - 30m
4. **H3** - Remove 10-15 G6→G6 dependencies - 1h
5. **H7** - Add cross-topic dependencies - 1h
6. **H9** - Fix dependency title mismatches - 30m

**Deliverable:** T19 has proper K-8 structure and correct dependencies

### Week 2: Quality Improvements (10 hours)
**Goal:** Enhance skill descriptions and add missing skills

7. **H10** - Rewrite conceptual descriptions (add outcomes) - 2h
8. **H11** - Add error handling skill - 1h
9. **M14** - Add capstone project skill - 1h
10. **M1** - Enhance vague descriptions - 2h
11. **M4** - Add testing criteria - 2h
12. **M6** - Replace jargon - 1h
13. **M7** - Add actionable outcomes to G7 - 1h

**Deliverable:** All skills have clear, concrete, testable descriptions

### Week 3: Advanced Fixes (7 hours)
**Goal:** Restructure and split skills for better scaffolding

14. **H5** - Split 3 overly broad skills - 3h
15. **H8** - Restructure for faster first game - 2h
16. **M2** - Add remaining cross-topic deps - 1h
17. **M8** - Audit all dependency names - 1h

**Deliverable:** Clear learning progression, students succeed faster

### Week 4: Polish & Documentation (5 hours)
**Goal:** Final quality pass and documentation

18. **M3** - Remove duplicate explanations - 1h
19. **M10-M12, M15** - Quick fixes (flexibility, concepts, clarifications) - 2h
20. **Documentation** - Create learning path guide - 1h
21. **Testing** - Verify all dependencies resolve - 1h

**Deliverable:** T19_PHASE1_OPTIMIZATION_REPORT.md complete

**TOTAL ESTIMATED TIME: 30 hours**

---

## 🚨 CRITICAL DEPENDENCIES BETWEEN FIXES

```
H1 (Add G5 bridge)
  └── Must complete BEFORE starting H8 (restructure)

H2 (Add G6 foundations)
  └── Must complete BEFORE H3 (remove deps)
      └── Must complete BEFORE H10 (rewrite descriptions)

H5 (Split broad skills)
  └── Affects H8 (restructure)
  └── Affects H3 (dependencies change)

H6 (Move testing)
  └── Must complete BEFORE H8 (restructure)
```

**Critical Path:** H1 → H2 → H5 → H3 → H6 → H8 → Rest

---

## ✅ QUICK WIN OPPORTUNITIES

**Can be done independently in < 1 hour each:**

1. ✅ H6 - Move T19.G6.02A earlier (30 min)
2. ✅ H9 - Fix T13.G6.01 reference (10 min)
3. ✅ M5 - Remove T14.G4.01 dependency (10 min)
4. ✅ M9 - Add T11.G5.01 dependency (10 min)
5. ✅ M10 - Make tag game flexible (15 min)
6. ✅ M11 - Add room concept explanation (15 min)
7. ✅ M12 - Document G6→G7→G8 shift (15 min)

**Total Quick Wins:** 7 fixes in 2 hours

---

## 📋 CHECKLIST FOR COMPLETION

### Structure
- [ ] At least 1 G5 skill exists (bridge to G6)
- [ ] G6→G6 dependencies reduced to < 10
- [ ] All cross-topic dependencies added
- [ ] Testing methodology taught early
- [ ] Students reach first game in ≤ 7 skills

### Content Quality
- [ ] All conceptual skills have observable outcomes
- [ ] All implementation skills have testing criteria
- [ ] No skills teach 3+ concepts
- [ ] No jargon without kid-friendly explanation
- [ ] All dependency titles match exactly

### Completeness
- [ ] Error handling covered
- [ ] Capstone project exists
- [ ] Core/Intermediate/Advanced categorized
- [ ] G6→G7→G8 progression documented
- [ ] Block coverage verified (13/13)

### Documentation
- [ ] T19_PHASE1_OPTIMIZATION_REPORT.md created
- [ ] Changes documented in T19_changes_summary.md
- [ ] allskills.md updated
- [ ] Quality score > 90% (currently 75%)

---

## 🎓 LESSONS FROM T14 OPTIMIZATION

**What worked well in T14 (apply to T19):**

✅ **Removed same-grade dependencies** → Flexible learning
✅ **Added cross-grade bridges** → Smooth progression
✅ **Replaced jargon** → Age-appropriate language
✅ **Made descriptions concrete** → Testable outcomes
✅ **Added capstone projects** → Clear milestones

**What T19 should copy:**
- Remove artificial G6 chaining (like T14 did with G3)
- Ensure every grade builds on previous (like T14's G3→G4→G5)
- Make advanced skills accessible (like T14's G7-G8)
- Add testing criteria (like T14's observable outcomes)

---

## 💡 KEY INSIGHTS

### Why T19 is Different
1. **Advanced topic** - Networking is complex, G6+ is appropriate
2. **Requires strong foundation** - Students need T01-T14 first
3. **Unique challenges** - Network lag, synchronization, multi-client debugging
4. **Real-world relevance** - Kids love multiplayer games

### Why K-5 Gap Exists
- CreatiCode multiplayer blocks are genuinely advanced
- Networking concepts require abstract thinking
- Testing requires multiple windows/devices

### Why G5 Bridge is Critical
- Eases transition from single-player to multiplayer
- Teaches shared game state without network complexity
- Builds confidence before adding internet layer

---

**Created:** 2025-11-22
**Status:** 📊 Analysis Complete
**Next:** Begin Week 1 implementation
