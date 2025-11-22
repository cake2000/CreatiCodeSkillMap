# T26 Quick Reference - Data Collection & Logging

## One-Page Summary

**Total Skills:** 45 (11 unplugged K-2, 34 coding G3-8)
**Overall Quality:** A- (Strong)
**Platform Support:** 100% (24% strongly supported with specialized features)

---

## Critical Issues Found

### HIGH PRIORITY (Fix Immediately)

**H2: X-2 Rule Violation in G5.02**
- **Skill:** T26.G5.02 - Plan sampling strategies
- **Problem:** Depends on T26.GK.02 and T26.GK.03 (Kindergarten skills)
- **Fix:** Remove both K dependencies - students don't need K-level tokens to understand sampling at G5
- **Updated Dependencies:**
  ```
  * T08.G3.01: Use a simple if in a script
  * T09.G3.05: Trace code with variables to predict outcomes
  * T10.G3.03: Add and remove items from a list
  ```

**H3: G4 Skills Using G3 Dependencies**
- **Skills:** T26.G4.01, T26.G4.02, T26.G4.04
- **Problem:** All three depend on T06.G3.01, T09.G3.05, T10.G3.03 (G3 versions)
- **Action Needed:** Investigate if G4 equivalents exist and should be used instead:
  - T06.G3.01 → T06.G4.01?
  - T09.G3.05 → T09.G4.04?
  - T10.G3.03 → T10.G4.02?

---

## Medium Priority Issues

**M1: Title Change Documentation**
- T26.G6.04 changed from "Capture measurement error estimates" to "Note when measurements might be inaccurate"
- Update references or use IDs consistently

**M2: Privacy Instruction Starts Late**
- First privacy skill at G4.04
- Consider adding G3.06: "Identify questions that protect privacy"

**M3: Missing Intermediate Step**
- Jump from G3.01 (simple survey loop) to G3.04 (raw vs summary) might be steep
- Consider intermediate skill on modifying lists during collection

---

## Skills by Grade

| Grade | Unplugged | Coding | Focus Area |
|-------|-----------|--------|------------|
| K | 3 | 0 | Counting, tokens, yes/no cards |
| G1 | 3 | 0 | Picture surveys, observation logs |
| G2 | 5 | 0 | Two-column sheets, timers, sample size |
| G3 | 0 | 5 | Survey loops, counters, raw vs summary |
| G4 | 0 | 4 | Tables, protocols, privacy |
| G5 | 0 | 4 | Print logging, validation, export |
| G6 | 0 | 4 | Stakeholder mapping, multi-input, consent |
| G7 | 0 | 4 | Reusable modules, quality monitoring, bias |
| G8 | 0 | 4 | Telemetry pipelines, scheduled exports, AI review |

---

## Progression Highlights

**K-2 Foundation (Unplugged):**
- Counting objects in pictures
- Using physical tokens to track events
- Running picture-based surveys
- Building two-column record sheets
- Understanding sample size

**G3 Transition (Coding Begins):**
- T26.G3.01: First coding skill - survey loop with `ask` and lists
- T26.G3.03: Sensor-style event logging with counters
- T26.G3.04: KEY CONCEPT - separating raw from summary data

**G4-G5 Expansion:**
- G4.02: Tables for multi-attribute logging (critical shift from lists to tables)
- G5.04: Export to CSV (first persistence skill)

**G6-G8 Advanced:**
- G6.01: Requirements mapping (stakeholder-driven)
- G7.01: Reusable collection modules (custom blocks)
- G8.01: End-to-end telemetry pipelines

**Privacy Thread:**
- G4.04: Reflect on privacy in collection
- G6.03: Create consent and opt-out workflows
- G7.03: Document provenance for external datasets
- G8.04: Publish data privacy agreements for peers

---

## CreatiCode Platform Strengths

**Strongly Supported Features:**
1. **Tables** - 50+ table operations (add/delete rows/columns, sort, aggregate, pivot)
2. **Google Sheets** - Direct read/write integration
3. **CSV Export** - `export table [] as []`
4. **Multiple Inputs** - Pose detection, voice, sensing all log to tables
5. **XO AI Assistant** - G8.03 uses platform feature directly

**Key Blocks for T26:**
- Survey: `ask [] and wait`, `answer`
- Lists: `add [] to []`, `item () of []`, `sort list []`
- Tables: `add to table []`, `item at row () column []`, `export table []`
- Google Sheets: `read from google sheet...`, `write into google sheet...`
- Custom Blocks: Define/use for reusable logging (G7+)

**No Blockers:** All skills are fully supported or have acceptable pedagogical workarounds

---

## Dependency Patterns

**Within T26:**
- Most skills depend on 0-2 prior T26 skills (good modularity)
- Key chains:
  - GK.01 → GK.02, GK.03 → G1.01 → G1.02 → G2.01 → G3.01
  - G3.03 → G3.04 → G4.01, G4.02
  - G5.04 → G6.01 → G7.01 → G8.01

**Cross-Topic (Most Common):**
- T08 (Conditionals): 12 dependencies - validation, error checking
- T09 (Variables): 22 dependencies - counters, storage
- T10 (Lists/Tables): 19 dependencies - data structures
- T06 (Events): 9 dependencies - trigger-based logging

---

## Quality Metrics

| Criterion | Rating | Notes |
|-----------|--------|-------|
| Internal Coherence | 8/10 | Strong progression, minor X-2 violation |
| Duplicates/Overlaps | 9/10 | No duplicates found |
| Dependencies (Within T26) | 7/10 | One X-2 violation, G4 pattern needs check |
| Grade Appropriateness | 9/10 | Perfect K-2 unplugged, G3+ coding split |
| Missing Skills | 7/10 | Privacy could start earlier, debugging gap |
| Skill Quality (CSAA) | 9/10 | Clear, specific, actionable, assessable |
| **OVERALL** | **A-** | **Strong with minor fixes needed** |

CSAA = Clear, Specific, Actionable, Assessable

---

## Recommended Actions

### Immediate (Next Sprint)
1. **Fix T26.G5.02:** Remove T26.GK.02 and T26.GK.03 dependencies
2. **Investigate G4 dependencies:** Check if T06/T09/T10 G4 versions should be used

### Short Term (Next Month)
3. **Add G3.06:** "Identify questions that protect privacy" skill
4. **Document title change:** Note T26.G6.04 rename in changelog
5. **Create dependency map:** Visual diagram of T26 skill progression

### Long Term (Nice to Have)
6. **Add G7.05:** "Debug collection scripts with missing or wrong data"
7. **Create block mapping:** Document exact CreatiCode blocks for each skill
8. **Align privacy thread:** Map G4.04, G6.03, G7.03, G8.04 to AI4K12 Big Idea #4

---

## Skills Requiring External Review

**T26.G4.01, G4.02, G4.04:** Check if dependencies should use G4 block versions
**T26.G5.02:** CONFIRMED needs fix (remove K dependencies)
**T26.G6.04:** Ensure all references use current title or note change

---

## Key Insights

1. **Strong Foundation:** K-2 unplugged activities provide excellent conceptual grounding
2. **Natural Progression:** Lists (G3) → Tables (G4) → Export (G5) → Pipelines (G8) is pedagogically sound
3. **Ethics Integration:** Privacy thread throughout G4-G8 aligns with AI4K12
4. **Platform Match:** CreatiCode's table features are perfect for this topic
5. **Modularity:** Most skills can be taught independently with just 0-2 T26 prerequisites

---

**For Full Analysis:** See T26_COMPREHENSIVE_ANALYSIS.md
**Analysis Date:** 2025-11-21
**Skills File:** /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md
**Blocks Reference:** /media/binyu/USB2/ScratchCopilot/blockdes8.txt
