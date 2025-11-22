# T32 Phase 1 Optimization - Quick Reference Guide

## At a Glance: Issues by Grade

### Kindergarten (4 skills)
- ✅ **GK.01-GK.02:** Good - picture-based, unplugged
- ⚠️ **GK.03:** Password example too complex - simplify to dots
- ✅ **GK.04:** Good - sorting activity

**Action:** Simplify GK.03 password visual

---

### Grade 1 (4 skills)
- ✅ **G1.01:** Good - categorization with cards
- ✅ **G1.02:** Good - illustrated scenarios
- ⚠️ **G1.03:** Too text-heavy - add pictures
- ⚠️ **G1.04:** Reading comprehension too advanced - focus on visuals only

**Actions:**
- Add picture support to G1.03
- Simplify G1.04 to visual cues only (no text analysis)

---

### Grade 2 (5 skills)
- ✅ **G2.01:** Good - guided template activity
- ✅ **G2.02:** Good - picture instructions
- ⚠️ **G2.03:** Needs visual scenarios/comic strips
- ⚠️ **G2.04:** "List practices" requires too much writing - convert to matching
- ✅ **G2.05:** Good - teacher-led scenarios

**Actions:**
- Add visual support to G2.03, G2.04
- **ADD G2.06:** Explain purpose of usernames and passwords (MISSING FOUNDATION)

---

### Grade 3 (4 skills)
- 🔴 **G3.01:** Depends on G3.01 (same grade) - verify ordering
- ⚠️ **G3.02:** Depends on G3.01 - ensure proper sequence
- ✅ **G3.03:** Good but VERIFY CreatiCode sharing features exist
- ✅ **G3.04:** Good progression

**Actions:**
- **ADD G3.00:** Identify parts of URLs/emails (MISSING FOUNDATION)
- Verify skill ordering within grade
- VERIFY CreatiCode project sharing panel exists

---

### Grade 4 (4 skills)
- 🔴 **G4.01:** X-2 VIOLATION - depends on T32.G2.03 (2 grades back)
- 🔴 **G4.02:** X-2 VIOLATION - depends on T32.G2.01 (2 grades back)
- ⚠️ **G4.03:** Description vague - specify article format
- ✅ **G4.04:** Good - builds on G3.01

**Actions:**
- FIX G4.01 - remove G2.03 dependency or add G3 bridge
- FIX G4.02 - remove G2.01 dependency or add G3 bridge
- Clarify G4.03 article specifications
- **ADD G4.05:** Recognize security indicators in apps (MISSING SCAFFOLDING)

---

### Grade 5 (6 skills)
- 🔴 **G5.01:** Too broad - covers 4 tactics - SPLIT into G5.01.01 and G5.01.02
- ⚠️ **G5.02:** Description vague - add template/structure
- 🔴 **G5.03.01:** CRITICAL X-2 VIOLATION - depends on T32.G1.01 (4 grades back!)
- ✅ **G5.03.02:** Good (depends on G5.03.01)
- ⚠️ **G5.03.03:** Should depend on G5.03.02 too (not just G5.03.01)
- 🔴 **G5.04:** Bad dependency on T09.G3.01.04 (unrelated) - REMOVE
- ✅ **G5.05:** Good
- ⚠️ **G5.06:** Terminology - clarify "encryption" vs "cipher"

**Actions:**
- SPLIT G5.01 into digital and physical social engineering
- FIX G5.03.01 - replace G1.01 with G3/G4 PII skill
- FIX G5.04 - remove T09.G3.01.04 dependency
- Add G5.03.02 to G5.03.03 dependencies
- **ADD G5.07:** Privacy vs security difference (MISSING CONCEPT)
- **ADD G5.08:** Software updates importance (MISSING CONCEPT)

---

### Grade 6 (5 skills)
- 🔴 **G6.01:** TOO BROAD - covers 5 attack types - SPLIT into G6.01.01 through G6.01.04
- ⚠️ **G6.02:** Complex (3 features) but manageable - VERIFY CreatiCode blocks exist
- ✅ **G6.03:** Good but has many AI dependencies (8 total across topics)
- ⚠️ **G6.04:** Description vague - specify bug bounty source
- ⚠️ **G6.05:** Depends on T10.G4.01 (2 grades back) - at edge of rule

**Actions:**
- SPLIT G6.01 into 4 separate skills (CRITICAL)
- **VERIFY CreatiCode string blocks exist:** `letter [N] of [word]`, `unicode of [letter]`, `unicode [N] as letter` (CRITICAL for G6.05)
- VERIFY CreatiCode UI widgets for G6.02
- Clarify G6.04 resources
- **ADD G6.06:** Where encryption is used daily (MISSING BRIDGE)
- **ADD G6.07:** Recognize deepfakes (MISSING MODERN TOPIC)
- **ADD G6.08:** Secure file sharing (MISSING PRACTICAL SKILL)

---

### Grade 7 (4 skills)
- 🔴 **G7.01:** Bad dependency on T06.G5.01 (events unrelated to cipher) - REMOVE
- 🔴 **G7.02:** Depends on G5.01, G5.02 (2 grades back) - at edge of rule
- ⚠️ **G7.03:** Unclear why T07.G5.01 (loop) dependency exists - clarify
- ✅ **G7.04.01:** Good AI ethics skill
- ✅ **G7.04.02:** Good progression from G7.04.01

**Actions:**
- FIX G7.01 - remove T06.G5.01 dependency
- **VERIFY CreatiCode string manipulation blocks** for G7.01 (same as G6.05) - CRITICAL
- Consider consolidating G7.02 dependencies through G6 skill
- Clarify or remove G7.03 loop dependency
- VERIFY CreatiCode table blocks for G7.03
- **ADD G7.05:** Public Wi-Fi security (MISSING MODERN TOPIC)
- **ADD G7.06:** IoT device security (MISSING MODERN TOPIC)
- **ADD G7.07:** Cyberbullying response (MISSING SOCIAL SKILL)

---

### Grade 8 (4 skills)
- ✅ **G8.01:** Good but could expand checklist details
- ✅ **G8.02:** Good role-based access
- 🔴 **G8.03:** TOO BROAD - covers security AND ethics - SPLIT into G8.03.01 and G8.03.02
- ⚠️ **G8.03:** 8 dependencies too many - consider consolidation
- ⚠️ **G8.04:** Only one scenario example - add more

**Actions:**
- SPLIT G8.03 into security audit and ethics audit
- Reduce/consolidate G8.03 dependencies if possible
- Add more scenarios to G8.04
- **ADD G8.05:** Ransomware understanding (MISSING MODERN TOPIC)

---

## Critical Actions Summary

### MUST DO (Phase 1)
1. ✅ **Fix X-2 violations:** G4.01, G4.02, G5.03.01
2. ✅ **VERIFY CreatiCode blocks (CRITICAL):** String manipulation for G6.05/G7.01
3. ✅ **Split broad skills:** G6.01 (4 parts), G5.01 (2 parts), G8.03 (2 parts)
4. ✅ **Add foundation skills:** G2.06, G3.00
5. ✅ **Fix bad dependencies:** G5.04→T09, G7.01→T06

### SHOULD DO (Phase 2)
1. ⚠️ Verify CreatiCode features: sharing (G3.03), backup (G5.04), UI (G6.02), tables (G7.03)
2. ⚠️ Add scaffolding skills: G4.05, G5.07, G6.06
3. ⚠️ Clarify vague descriptions: G4.03, G5.02, G6.04, G7.02
4. ⚠️ Improve K-2 visual support: G1.03, G1.04, G2.03, G2.04

### NICE TO HAVE (Phase 3-4)
1. 📝 Add modern topics: deepfakes, Wi-Fi, IoT, ransomware, cyberbullying
2. 📝 Add practical skills: software updates, file sharing, safe searching
3. 📝 Standardize terminology, add flexibility, polish descriptions

---

## X-2 Rule Violations Quick Fix Table

| Skill | Violating Dependency | Grade Gap | Fix |
|-------|---------------------|-----------|-----|
| **T32.G4.01** | T32.G2.03 | 2 grades | Remove or add G3 digital citizenship skill |
| **T32.G4.02** | T32.G2.01 | 2 grades | Remove or add G3 password skill |
| **T32.G5.03.01** | T32.G1.01 | 4 grades! | Replace with T32.G4.01 or G3.03 |
| T32.G6.05 | T10.G4.01 | 2 grades | Acceptable (cross-topic, at edge) |
| T32.G7.02 | T32.G5.01, G5.02 | 2 grades | Consider G6 consolidation |

---

## Skills to Split

### G6.01 → 4 skills
- G6.01.01: Identify common malware types
- G6.01.02: Analyze phishing attacks
- G6.01.03: Understand network attacks (DoS, MitM)
- G6.01.04: Recognize database vulnerabilities (SQL injection)

### G5.01 → 2 skills
- G5.01.01: Analyze digital social engineering (phishing, pretexting, baiting)
- G5.01.02: Recognize physical security risks (tailgating, shoulder surfing)

### G8.03 → 2 skills
- G8.03.01: Audit AI projects for security vulnerabilities
- G8.03.02: Audit AI projects for ethical concerns

### G6.02 → Consider 2 skills
- G6.02.01: Validate password strength
- G6.02.02: Implement login security controls

---

## Skills to Add

### Foundation Skills (High Priority)
- **T32.G2.06:** Explain purpose of usernames and passwords
- **T32.G3.00:** Identify parts of URLs and email addresses
- **T32.G4.05:** Recognize security indicators in apps
- **T32.G5.07:** Understand privacy vs security difference
- **T32.G6.06:** Identify where encryption is used daily

### Modern Topics (Medium Priority)
- **T32.G6.07:** Recognize deepfakes and AI misinformation
- **T32.G7.05:** Understand public Wi-Fi security risks
- **T32.G7.06:** Evaluate IoT device security
- **T32.G8.05:** Understand ransomware

### Practical Skills (Medium Priority)
- **T32.G4.00:** Practice safe searching
- **T32.G5.08:** Understand software updates
- **T32.G6.08:** Practice secure file sharing
- **T32.G7.07:** Recognize and respond to cyberbullying

---

## CreatiCode Feature Verification Checklist

### CRITICAL (Must verify for implementation)
- [ ] **String manipulation blocks:** `letter [N] of [word]`, `join`, `unicode of [letter]`, `unicode [N] as letter` (G6.05, G7.01)
- [ ] **Project sharing:** Privacy settings (private/class/public), invite users, permission verification (G3.03)
- [ ] **File operations:** Download project, upload project, format preservation (G5.04)

### HIGH (Important features)
- [ ] **UI widgets:** Password input/masking, button enable/disable, string length (G6.02)
- [ ] **Table blocks:** Create table, append row, timestamp (G7.03)

### MEDIUM (Nice to have)
- [ ] **Image editing:** Blur regions of images (G5.03.02) - may need external tool
- [ ] **Calculator:** Password cracking calculator (G7.02) - likely teacher-provided
- [ ] **Role variables:** Store roles, conditional access control (G8.02)

---

## Dependency Removal List

| Skill | Remove This Dependency | Reason |
|-------|----------------------|--------|
| **T32.G5.04** | T09.G3.01.04 (variable monitor) | Unrelated to backups |
| **T32.G7.01** | T06.G5.01 (event patterns) | Unrelated to ciphers |
| T32.G7.03 | T07.G5.01 (loops)? | Unclear necessity - verify first |

---

## Files Generated
1. **T32_OPTIMIZATION_ANALYSIS.json** - Full detailed analysis
2. **T32_EXECUTIVE_SUMMARY.md** - Executive overview
3. **T32_QUICK_REFERENCE.md** - This quick reference (you are here)

---

**Next:** Review analysis, verify CreatiCode features, implement Phase 1 fixes
