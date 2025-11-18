#!/usr/bin/env python3
"""
Create a comprehensive CSTA backfill implementation plan with
coverage analysis, manual review requirements, and next steps.
"""
import json
from collections import defaultdict

# Load assignment data
with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/SKILL_CSTA_ASSIGNMENTS.json', 'r') as f:
    assignment_data = json.load(f)

stats = assignment_data['statistics']
assignments = assignment_data['assignments']

# Load mapping rules for context
with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/TOPIC_TO_CSTA_MAPPING_RULES.json', 'r') as f:
    mapping_rules = json.load(f)

# Analyze manual review needs
needs_review = [a for a in assignments if a['assignment_method'] == 'needs_review']
by_topic_review = defaultdict(list)
for a in needs_review:
    by_topic_review[a['topic_id']].append(a)

# Create markdown plan
md = f"""# CSTA Standards Backfill Implementation Plan

**Version:** 1.0
**Created:** 2025-11-17
**Status:** Ready for Implementation

---

## Executive Summary

### Current State
- **Total Skills:** {stats['total_skills']} (K-8)
- **Skills with CSTA Codes (Before):** 240 (21.4%)
- **Skills with CSTA Codes (After Automated Assignment):** {stats['skills_assigned']} ({stats['skills_assigned']/stats['total_skills']*100:.1f}%)
- **Improvement:** +{stats['skills_assigned'] - 240} skills ({(stats['skills_assigned'] - 240)/stats['total_skills']*100:.1f}% increase)

### Automated Coverage Achievement
**✅ {stats['skills_auto_assigned']} skills auto-assigned** via rule-based mapping ({stats['skills_auto_assigned']/stats['total_skills']*100:.1f}% of total)

**✅ {stats['skills_kept_existing']} existing assignments validated and kept**

**⚠️ {stats['skills_needing_review']} skills require manual review** ({stats['skills_needing_review']/stats['total_skills']*100:.1f}% of total)

### Coverage Goals
- **Phase 1 (Automated):** ✅ {stats['skills_auto_assigned']+stats['skills_kept_existing']}/1,119 ({(stats['skills_auto_assigned']+stats['skills_kept_existing'])/stats['total_skills']*100:.1f}%) - COMPLETE
- **Phase 2 (Manual Review):** {stats['skills_needing_review']} skills - 2-3 hours estimated
- **Phase 3 (Validation):** All 1,119 skills - 1-2 hours estimated
- **Final Target:** 100% coverage (1,119/1,119 skills)

---

## Phase 1: Automated Assignment (COMPLETE ✅)

### What Was Accomplished

1. **Extracted 163 K-8 CSTA Standards**
   - Algorithms and Design (ALG): 33 standards
   - Programming (PRO): 37 standards
   - Data and Analysis (DAA): 32 standards
   - Systems and Security (SAS): 32 standards
   - Computing and Society (CAS): 29 standards

2. **Created Comprehensive Mapping Rules**
   - All 36 CreatiCode topics mapped to CSTA topic areas
   - Grade-specific mappings for K through 8
   - Primary and secondary standard alignments
   - Context-aware assignments (e.g., AI topics → CAS-ET + DAA-IM)

3. **Automated 834 Skill Assignments**
   - Rule-based mapping engine
   - Topic + Grade → CSTA codes
   - High confidence assignments
   - Preserved 240 existing valid assignments

### Coverage by Grade (After Phase 1)

| Grade | Skills | Assigned | Coverage | Status |
|-------|--------|----------|----------|--------|
| K | 61 | 61 | 100.0% | ✅ Complete |
| 1 | 69 | 69 | 100.0% | ✅ Complete |
| 2 | 91 | 91 | 100.0% | ✅ Complete |
| 3 | 146 | 132 | 90.4% | ⚠️ 14 need review |
| 4 | 149 | 134 | 89.9% | ⚠️ 15 need review |
| 5 | 152 | 136 | 89.5% | ⚠️ 16 need review |
| 6 | 151 | 151 | 100.0% | ✅ Complete |
| 7 | 148 | 148 | 100.0% | ✅ Complete |
| 8 | 152 | 152 | 100.0% | ✅ Complete |
| **TOTAL** | **1,119** | **1,074** | **96.0%** | **Outstanding** |

**Key Insight:** K-2 and 6-8 have 100% automated coverage. Grades 3-5 need minor manual review (primarily T11, T24, T29, T33).

### Coverage by Topic Area

**Perfect Coverage (100%)** - 32 topics:
"""

# Add perfect coverage topics
perfect_topics = []
for topic_id, data in stats['by_topic'].items():
    pct = data['assigned'] / data['total'] * 100 if data['total'] > 0 else 0
    if pct == 100.0:
        topic_name = mapping_rules['topic_mappings'].get(topic_id, {}).get('name', '')
        perfect_topics.append((topic_id, topic_name, data['total']))

for topic_id, topic_name, total in sorted(perfect_topics):
    md += f"- {topic_id}: {topic_name} ({total} skills)\n"

md += f"""

**Needs Manual Review** - 4 topics ({stats['skills_needing_review']} skills):
"""

# Add topics needing review
for topic_id, skills_list in sorted(by_topic_review.items(), key=lambda x: len(x[1]), reverse=True):
    topic_name = mapping_rules['topic_mappings'].get(topic_id, {}).get('name', '')
    count = len(skills_list)
    total = stats['by_topic'][topic_id]['total']
    assigned = stats['by_topic'][topic_id]['assigned']
    pct = assigned / total * 100 if total > 0 else 0
    md += f"- **{topic_id}**: {topic_name} - {count} skills need review ({assigned}/{total}, {pct:.1f}% coverage)\n"

md += f"""

---

## Phase 2: Manual Review ({stats['skills_needing_review']} Skills)

### Why Manual Review is Needed

These {stats['skills_needing_review']} skills require manual review because:
1. **T11 (Functions & Procedures):** Grade 3-5 skills - CSTA has limited elementary function standards
2. **T29 (Text Analysis & NLP):** Advanced topic with sparse elementary coverage
3. **T33 (APIs & Cloud Services):** Modern topic not fully addressed in K-5 CSTA standards
4. **T24 (XO & AI-Supported Coding):** Emerging AI tools topic with limited direct standards

### Manual Review Process

**Step 1: Review Each Skill (Est. 5-7 minutes per skill)**

For each of the {stats['skills_needing_review']} skills:

1. Read skill title and description from `SKILL_CSTA_ASSIGNMENTS.json`
2. Consult `CSTA_STANDARDS_REFERENCE.md` for appropriate grade/topic standards
3. Assign 1-3 CSTA codes that best align with skill objectives
4. Consider both primary and secondary alignments
5. Document rationale in notes field

**Step 2: Common Assignment Patterns**

**For T11 (Functions & Procedures) - Grades 3-5:**
- Grade 3-5: No direct elementary function standards → Use `E3-PRO-PD-xx` (Program Development)
- Or map to decomposition: `E3-ALG-PS-03`, `E4-ALG-PS-03`, `E5-ALG-PS-03`
- Alternatively, if skill is more advanced, consider: "Skill may be better suited for Grade 6+" with `MS-PRO-PD-08`

**For T29 (Text Analysis & NLP) - Grades 3-5:**
- Grade 3-5: Use data investigation standards: `E3-DAA-DI-03`, `E4-DAA-DI-02`, `E5-DAA-DI-02`
- Plus emerging tech: `E3-CAS-ET-02`, `E4-CAS-ET-02`, `E5-CAS-ET-02`
- Grade 6-8: Already mapped to `MS-DAA-DP-05`, `MS-DAA-IM-15`, `MS-CAS-ET-05`

**For T33 (APIs & Cloud Services) - Grades 3-5:**
- Grade 3-5: Use network/systems standards: `E3-SAS-NW-02`, `E4-SAS-NW-02`, `E5-SAS-NW-02`
- Plus software: `E3-SAS-HW-01`, `E4-SAS-HW-01`, `E5-SAS-HW-01`
- Or consider: Skills may need to be redesigned for appropriate grade level

**For T24 (XO & AI-Supported Coding) - Grades 3-5:**
- Grade 3-5: Use program development: `E3-PRO-PD-xx` (if standard exists)
- Plus emerging tech: `E3-CAS-ET-02`, `E4-CAS-ET-02`, `E5-CAS-ET-02`
- Plus impacts: `E3-ALG-IM-04`, `E4-ALG-IM-04`, `E5-ALG-IM-04`
- Note: XO AI assistant is cutting-edge, may exceed K-5 standards scope

### Detailed Review List

#### T11: Functions & Procedures ({len(by_topic_review.get('T11', []))} skills)

"""

# Add specific skills for T11
if 'T11' in by_topic_review:
    for skill in by_topic_review['T11'][:5]:  # Show first 5 as examples
        md += f"- **{skill['skill_id']}** (Grade {skill['grade']}): {skill['title']}\n"
        md += f"  - Suggested: `E{skill['grade']}-ALG-PS-03` (Decomposition) or `MS-PRO-PD-08` if advanced\n"
    if len(by_topic_review['T11']) > 5:
        md += f"- ... and {len(by_topic_review['T11']) - 5} more (see SKILL_CSTA_ASSIGNMENTS.json)\n"

md += f"""

#### T29: Text Analysis & NLP ({len(by_topic_review.get('T29', []))} skills)

"""

if 'T29' in by_topic_review:
    for skill in by_topic_review['T29'][:5]:
        md += f"- **{skill['skill_id']}** (Grade {skill['grade']}): {skill['title']}\n"
        if int(skill['grade']) <= 5:
            md += f"  - Suggested: `E{skill['grade']}-DAA-DI-02` or `E{skill['grade']}-DAA-DI-03` + `E{skill['grade']}-CAS-ET-02`\n"
    if len(by_topic_review['T29']) > 5:
        md += f"- ... and {len(by_topic_review['T29']) - 5} more\n"

md += f"""

#### T33: APIs & Cloud Services ({len(by_topic_review.get('T33', []))} skills)

"""

if 'T33' in by_topic_review:
    for skill in by_topic_review['T33'][:5]:
        md += f"- **{skill['skill_id']}** (Grade {skill['grade']}): {skill['title']}\n"
        if int(skill['grade']) <= 5:
            md += f"  - Suggested: `E{skill['grade']}-SAS-NW-02` + `E{skill['grade']}-SAS-HW-01` OR redesign for Grade 6+\n"
    if len(by_topic_review['T33']) > 5:
        md += f"- ... and {len(by_topic_review['T33']) - 5} more\n"

md += f"""

#### T24: XO & AI-Supported Coding ({len(by_topic_review.get('T24', []))} skills)

"""

if 'T24' in by_topic_review:
    for skill in by_topic_review['T24'][:5]:
        md += f"- **{skill['skill_id']}** (Grade {skill['grade']}): {skill['title']}\n"
        md += f"  - Suggested: `E{skill['grade']}-CAS-ET-02` + `E{skill['grade']}-ALG-IM-04` (AI ethics/impacts)\n"
    if len(by_topic_review['T24']) > 5:
        md += f"- ... and {len(by_topic_review['T24']) - 5} more\n"

md += f"""

### Time Estimate
- **Per skill:** 5-7 minutes (read, research, assign, document)
- **Total time:** {stats['skills_needing_review'] * 5} - {stats['skills_needing_review'] * 7} minutes ({stats['skills_needing_review'] * 5 / 60:.1f} - {stats['skills_needing_review'] * 7 / 60:.1f} hours)
- **Recommended:** 2-3 focused sessions

---

## Phase 3: Validation & Quality Assurance

### Validation Checklist

**✅ Automated Validation (Complete)**
1. All assigned codes exist in CSTA K-8 standards
2. Grade levels match (E3 codes for Grade 3 skills, etc.)
3. Topic areas align with skill content
4. No duplicate or conflicting assignments

**Manual Validation (To Do)**

For each topic (36 total):
- [ ] Review 3-5 sample skills per grade level
- [ ] Verify CSTA codes match skill learning objectives
- [ ] Check for consistency within topic
- [ ] Ensure progression across grades makes sense

**Sample Review Process:**

1. **Pick a topic** (e.g., T07: Loops)
2. **Review grades K-8** for that topic
3. **Check 3-5 skills per grade:**
   - Does CSTA code match skill content?
   - Is complexity appropriate for grade?
   - Are dependencies honored?
4. **Document issues** in a spreadsheet
5. **Adjust assignments** as needed

**Time Estimate:** 1-2 hours (3-5 min per topic × 36 topics)

---

## Phase 4: Implementation & Update

### Update Skills JSON

**Option 1: Bulk Update Script (Recommended)**

```python
import json

# Load current skills
with open('skills_k8_ai_complete.json', 'r') as f:
    skills = json.load(f)

# Load assignments
with open('SKILL_CSTA_ASSIGNMENTS.json', 'r') as f:
    assignments_data = json.load(f)
    assignments = {{a['skill_id']: a for a in assignments_data['assignments']}}

# Update each skill
for skill in skills:
    skill_id = skill['id']
    if skill_id in assignments:
        assignment = assignments[skill_id]
        if assignment['assigned_csta_codes']:
            # Use first code as primary, or join multiple
            skill['csta_code'] = ', '.join(assignment['assigned_csta_codes'])

# Save updated skills
with open('skills_k8_ai_complete_CSTA_UPDATED.json', 'w') as f:
    json.dump(skills, f, indent=2)

print("Updated skills file created!")
```

**Option 2: Manual Updates**
- Use `SKILL_CSTA_ASSIGNMENTS.json` as reference
- Update `skills_k8_ai_complete.json` manually
- Focus on the {stats['skills_needing_review']} manual review items first

### Verification Steps

After updating:
1. **Count coverage:**
   ```bash
   jq '[.[] | select(.csta_code and .csta_code != "" and .csta_code != "Unknown")] | length' skills_k8_ai_complete_CSTA_UPDATED.json
   # Should be 1074 or more (after manual review: 1119)
   ```

2. **Check for errors:**
   - No "Unknown" or empty csta_code values (except the {stats['skills_needing_review']} pending review)
   - All codes match E[K-5] or MS format
   - Codes exist in CSTA standards

3. **Run validation script** (create if needed):
   - Validate all CSTA codes exist
   - Check grade alignment
   - Report any anomalies

---

## Standards Alignment Reporting

### Current Coverage by CSTA Topic Area

After automated assignment, skills map to these CSTA topic areas:

| CSTA Topic Area | CreatiCode Topics | Skills Mapped | Notes |
|-----------------|-------------------|---------------|-------|
| ALG (Algorithms) | T01-T05, T14-T20 | ~300 | Strong coverage |
| PRO (Programming) | T06-T13, T14-T24 | ~450 | Excellent coverage |
| DAA (Data & Analysis) | T25-T29, T21-T24 | ~200 | Good coverage |
| SAS (Systems & Security) | T30-T33, T19, T23 | ~100 | Adequate coverage |
| CAS (Computing & Society) | T34-T36, T21-T24 | ~150 | Good coverage |

### Standards Not Yet Mapped

Some CSTA standards may not have corresponding CreatiCode skills:
- Advanced cybersecurity topics (MS-SAS-SC-10)
- Specialty high school topics (not in scope for K-8)
- Some niche middle school standards

**Recommendation:** Review unmapped CSTA standards to identify potential skill gaps for future development.

---

## Known Limitations & Future Work

### Current Limitations

1. **Multiple codes per skill:** Some skills map to 2-3 CSTA codes. Current JSON schema uses a single `csta_code` field (string). Consider:
   - Change to `csta_codes` (array) in schema v3
   - Or concatenate: "E3-PRO-PF-01, E3-ALG-AF-01"

2. **Granularity mismatch:** CSTA standards are broader than individual CreatiCode skills. Multiple skills may map to same standard.

3. **Emerging topics:** AI/ML topics (T21-T24, T29) push boundaries of K-8 CSTA standards. Some assignments are approximate.

4. **Elementary functions:** T11 (Functions) in grades 3-5 lacks direct CSTA mapping. Manual review needed.

### Future Enhancements

**Short-term (Next sprint):**
1. Complete Phase 2 manual review ({stats['skills_needing_review']} skills)
2. Run Phase 3 validation
3. Update `skills_k8_ai_complete.json` with all assignments
4. Generate standards coverage report for stakeholders

**Medium-term (Next quarter):**
1. Extend schema to support multiple CSTA codes per skill
2. Add reverse mapping: CSTA code → list of CreatiCode skills
3. Create standards coverage dashboard for teachers
4. Identify CSTA standards with no CreatiCode coverage (skill gaps)

**Long-term (Next year):**
1. Align with CSTA Standards 2.0 final version (published summer 2026)
2. Add depth-of-knowledge (DOK) levels to each skill
3. Create assessment items explicitly tied to CSTA standards
4. Publish alignment documentation for state adoption

---

## Success Metrics

### Phase 1 (COMPLETE ✅)
- [x] 163 CSTA K-8 standards extracted and documented
- [x] 36 topic-to-CSTA mapping rules created
- [x] {stats['skills_auto_assigned']} skills auto-assigned ({stats['skills_auto_assigned']/stats['total_skills']*100:.1f}%)
- [x] 96% coverage achieved through automation

### Phase 2 (In Progress)
- [ ] {stats['skills_needing_review']} manual review skills assigned
- [ ] 100% coverage achieved (1,119/1,119)
- [ ] All assignments documented with rationale

### Phase 3 (Planned)
- [ ] Validation checklist completed
- [ ] 36 topics spot-checked (3-5 skills per grade)
- [ ] Anomalies identified and resolved

### Phase 4 (Planned)
- [ ] `skills_k8_ai_complete.json` updated with all CSTA codes
- [ ] Coverage report generated for stakeholders
- [ ] Documentation updated (README, spec)

---

## Deliverables

### Completed ✅
1. **CSTA_STANDARDS_REFERENCE.md** - Comprehensive K-8 standards reference (163 standards)
2. **TOPIC_TO_CSTA_MAPPING_RULES.json** - Automated mapping rules for all 36 topics
3. **SKILL_CSTA_ASSIGNMENTS.json** - All 1,119 skills with assigned/suggested CSTA codes
4. **CSTA_BACKFILL_PLAN.md** - This implementation plan

### In Progress
5. **Manual review** of {stats['skills_needing_review']} skills (Est. 2-3 hours)

### Planned
6. **Updated skills_k8_ai_complete.json** with all CSTA codes populated
7. **Coverage validation report** for quality assurance
8. **Standards alignment documentation** for external stakeholders

---

## Getting Started

### Immediate Next Steps (Phase 2)

1. **Open `SKILL_CSTA_ASSIGNMENTS.json`**
2. **Filter for `"assignment_method": "needs_review"`**
3. **For each skill:**
   - Read title/description
   - Consult `CSTA_STANDARDS_REFERENCE.md`
   - Assign 1-3 appropriate CSTA codes
   - Update JSON with assignments
   - Add brief rationale in `notes` field

4. **Start with T24** (10 skills, manageable scope)
5. **Then T33** (11 skills)
6. **Then T11** (12 skills)
7. **Finally T29** (12 skills)

### Resources

- **CSTA_STANDARDS_REFERENCE.md**: Quick lookup of all K-8 standards
- **TOPIC_TO_CSTA_MAPPING_RULES.json**: See mapping patterns for similar topics
- **SKILL_CSTA_ASSIGNMENTS.json**: All skill data in one place

### Questions or Issues?

Refer to:
- CSTA K-12 Standards Draft 2.0: `/media/binyu/USB2/dev/CreatiCodeSkillMap/cstastandard.md`
- CreatiCode Spec v2: `/media/binyu/USB2/dev/CreatiCodeSkillMap/spec_v2_updated.md`

---

**Document Version:** 1.0
**Last Updated:** 2025-11-17
**Status:** ✅ Phase 1 Complete | ⏳ Phase 2 Ready to Start
**Estimated Completion:** 3-5 hours total remaining

---

**END OF PLAN**
"""

# Write to file
with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/CSTA_BACKFILL_PLAN.md', 'w') as f:
    f.write(md)

print("Created CSTA_BACKFILL_PLAN.md")
print(f"\n✓ Comprehensive backfill plan created!")
print(f"✓ Document length: {len(md)} characters")
print(f"✓ Ready for Phase 2 implementation")
print(f"\n📋 Summary:")
print(f"   - Phase 1: ✅ COMPLETE (96% automated coverage)")
print(f"   - Phase 2: {stats['skills_needing_review']} skills for manual review (2-3 hours)")
print(f"   - Phase 3: Validation (1-2 hours)")
print(f"   - Phase 4: Implementation (< 1 hour)")
print(f"\n🎯 Total estimated time remaining: 4-6 hours to 100% coverage")
