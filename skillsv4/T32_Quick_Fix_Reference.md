# T32 Cybersecurity - Quick Fix Reference

**Analysis Date:** 2025-11-23

---

## CRITICAL FIXES (Must Do)

### 1. Fix Numbering: G3.00 → G3.01
**Current:** T32.G3.00 - Identify parts of URLs and email addresses
**Fix:** Renumber to T32.G3.01 and shift all subsequent G3 skills by +1

**Impact:** 5 skills need renumbering (G3.00-G3.04 → G3.01-G3.05)

---

### 2. Remove Unnecessary Dependency
**Skill:** T32.G3.02 (Recognize website safety indicators)
**Current Dependencies:** T32.G3.00 + T32.G3.01
**Fix:** Remove G3.01 dependency (MFA not needed for HTTPS/padlock recognition)
**New Dependencies:** T32.G3.01 only (URLs)

---

### 3. Flatten Sub-Skill Numbering

#### Grade 5 Changes:
- **T32.G5.01.01** → **T32.G5.01** (Analyze digital social engineering tactics)
- **T32.G5.01.02** → **T32.G5.02** (Recognize physical security risks)
- **T32.G5.02** → **T32.G5.03** (Compare privacy policies)
- **T32.G5.03.01** → **T32.G5.04** (Review PII in AI project data)
- **T32.G5.03.02** → **T32.G5.05** (Practice redacting sensitive data)
- **T32.G5.03.03** → **T32.G5.06** (Understand consent for AI data collection)
- **T32.G5.04** → **T32.G5.07** (Create backup plans)
- **T32.G5.05** → **T32.G5.08** (Add consent prompts)
- **T32.G5.06** → **T32.G5.09** (Understand encryption - unplugged)

#### Grade 6 Changes:
- **T32.G6.01.01** → **T32.G6.01** (Identify common malware types)
- **T32.G6.01.02** → **T32.G6.02** (Recognize phishing attack patterns)
- **T32.G6.01.03** → **T32.G6.03** (Understand network attacks)
- **T32.G6.01.04** → **T32.G6.04** (Database vulnerabilities)
- **T32.G6.02** → **T32.G6.05** (Design secure login flows)
- **T32.G6.03** → **T32.G6.06** (AI-specific threat modeling)
- **T32.G6.04** → **T32.G6.07** (Ethical vs malicious hacking)
- **T32.G6.05** → **T32.G6.08** (Explore simple cipher techniques)

#### Grade 7 Changes:
- **T32.G7.04.01** → **T32.G7.04** (Facial recognition ethics)
- **T32.G7.04.02** → **T32.G7.05** (Emotion detection ethics)

#### Grade 8 Changes:
- **T32.G8.03.01** → **T32.G8.03** (Audit AI for security vulnerabilities)
- **T32.G8.03.02** → **T32.G8.04** (Audit AI for ethical concerns)
- **T32.G8.04** → **T32.G8.05** (Create AI incident response plans)

---

### 4. Clarify MFA vs 2FA Differentiation
**Skill G3.01 (currently G3.01):** Focus description on WHAT MFA is
- Concept introduction
- "Two locks on a door" analogy
- Understanding that multiple proofs are needed

**Skill G4.04:** Focus description on WHY MFA prevents attacks
- Scenario analysis (password stolen, but attacker lacks 2nd factor)
- Real-world attack-defense thinking
- Specific attack prevention examples

---

## HIGH PRIORITY ADDITIONS

### 5. Add Missing Grade 4 Skill
**New Skill: T32.G4.06**
**Skill Name:** Practice reporting and verifying suspicious emails
**Description:** Students learn safe procedures for reporting suspected phishing emails to teachers or IT staff. They practice verifying email legitimacy by checking sender information through official channels (typing website address directly instead of clicking links). They understand what happens after reporting: IT investigates, blocks sender, and protects others. Students role-play scenarios using age-appropriate examples.

**Dependencies:**
- T32.G3.04 (Recognize phishing-like messages)
- T32.G4.01 (Digital citizenship principles)

**Fills Gap:** Between G3.04 (recognition) and G5.01 (analysis)

---

### 6. Add Missing Grade 5 Password Skill
**New Skill: T32.G5.10** (after renumbering)
**Skill Name:** Evaluate password strength patterns
**Description:** Students use a password strength checking tool (teacher-provided or online safe checker) to test various password patterns. They analyze factors affecting strength: length (4 vs 8 vs 12 characters), character variety (letters only vs letters+numbers vs letters+numbers+symbols), dictionary words vs random strings, and common patterns (123456, qwerty, password1). Based on testing results, they create class password strength guidelines with specific recommendations (minimum length, required character types, words to avoid).

**Dependencies:**
- T32.G4.02 (Use password managers - conceptual)
- T32.G3.01 (MFA)

**Fills Gap:** Between G4.02 (conceptual password management) and G6.05 (secure login coding)

---

## HIGH PRIORITY IMPROVEMENTS

### 7. Add Implementation Notes to All Skills
For each skill G3-G8, add note specifying:
- **Unplugged conceptual activity** (discussion, analysis, case study)
- **Platform UI exploration** (CreatiCode features, not blocks)
- **Block-based programming** (coding project)

**Example Format:**
```
_Implementation note: This is an unplugged discussion activity using teacher-provided case studies. No coding or digital platform required._
```

---

### 8. Add Mobile Device Security Skills

**New Skill: T32.G4.07**
**Skill Name:** Understand app permissions and why they matter
**Description:** Students examine app permission requests and learn to question why apps need certain access. Example: Why does a flashlight app need camera access? Why does a game need location data? They practice the "stop and think" approach before granting permissions and understand that permissions give apps control over personal data.

**Dependencies:** T32.G4.01 (Digital citizenship)

---

**New Skill: T32.G5.11** (after renumbering)
**Skill Name:** Practice setting up device locks
**Description:** Students learn about device lock options (PIN, pattern, fingerprint, face unlock) and practice setting up locks on classroom devices or in simulated environments. They discuss why device locks are the first line of defense against unauthorized physical access and understand lock screen best practices (don't use birthdays, don't share PINs).

**Dependencies:** T32.G4.01, T32.G2.02 (logging off devices)

---

**New Skill: T32.G6.09**
**Skill Name:** Evaluate app safety before installation
**Description:** Students learn to check app safety indicators before installing: developer reputation, user reviews, number of downloads, requested permissions, last update date, and official app store warnings. They practice with real examples (comparing legitimate and suspicious apps) and create a safety checklist for evaluating new apps.

**Dependencies:** T32.G4.07 (app permissions), T32.G4.05 (security indicators)

---

**New Skill: T32.G7.06**
**Skill Name:** Understand mobile malware distribution methods
**Description:** Students learn how mobile malware spreads: malicious apps in unofficial stores, fake apps mimicking legitimate ones, phishing links in text messages, and side-loading from unknown sources. They discuss mobile-specific risks (less visible security warnings, always-connected nature, location tracking) and practice safe mobile habits (only use official app stores, verify app authenticity, don't click links in unexpected texts).

**Dependencies:** T32.G6.01 (malware types), T32.G6.09 (evaluate apps)

---

## MEDIUM PRIORITY IMPROVEMENTS

### 9. Break Down Complex Multi-Objective Skills

#### T32.G4.01 → Split or Add Assessment Specificity
**Option A:** Keep as one skill, add specific assessment:
"Given 15 digital citizenship scenarios, students classify each as protecting (1) personal information, (2) treating others with respect, or (3) reporting problems. They must achieve 90% accuracy (13+/15 correct) and explain reasoning for 3 scenarios."

**Option B:** Split into 3 sub-skills with focused activities

---

#### T32.G6.01 Reorganization
**Current Structure:** G6.01.01 covers 4 malware types, then G6.01.02-.04 cover attacks

**Proposed New Structure:**
- **T32.G6.01** - Identify viruses and ransomware (malware that damages/blocks data)
- **T32.G6.02** - Identify spyware and trojans (malware that deceives/monitors)
- **T32.G6.03** - Recognize phishing attack patterns [MOVE FROM CURRENT .01.02]
- **T32.G6.04** - Understand network attacks (DoS, MitM) [MOVE FROM .01.03]
- **T32.G6.05** - Learn database vulnerabilities (SQL injection) [MOVE FROM .01.04]
- Continue with current G6.02 → G6.06, etc.

---

#### T32.G6.05 (currently G6.02) - Secure Login Components
**Option A:** Keep as one multi-session project
Add note: "_This is a 3-4 session coding project. Teachers may choose to complete components incrementally._"

**Option B:** Split into 3 sequential skills
- G6.05a: Implement password length validation
- G6.05b: Implement password masking display
- G6.05c: Implement failed login attempt tracking

---

## X-2 RULE BORDERLINE CASES

### 10. Address Borderline Dependencies

#### T32.G6.05 (currently G6.02) Dependency Issue
**Current:** Depends on T32.G4.02 (Grade 4 password managers)
**Gap:** 2 grades (exactly at X-2 limit)
**Fix:** Add intermediate dependency
**Recommendation:** Add dependency on new T32.G5.10 (password strength evaluation)

**Updated Dependencies:**
- T32.G5.10 (Evaluate password strength patterns)
- All coding dependencies (T07.G3.01, T08.G3.01, etc.)

---

#### T32.G6.08 (currently G6.05) String Manipulation Dependency
**Current:** Depends on T10.G4.01 (Grade 4 string concatenation)
**Gap:** 2 grades (exactly at X-2 limit)
**Fix:** Check if T10.G5.01 exists and use instead
**Recommendation:** Change dependency to T10.G5.01 (Extract substrings) which is more relevant to cipher work

**Updated Dependencies:**
- T10.G5.01 (Extract substrings and manipulate text)
- T32.G5.09 (Understand encryption - unplugged)

---

## SUMMARY CHECKLIST

### Must Complete Before Phase 2:
- [ ] Renumber G3.00 → G3.01 (shift all G3 skills)
- [ ] Flatten all sub-skill numbering (G5, G6, G7, G8)
- [ ] Remove G3.01 dependency from G3.02
- [ ] Update all dependency references to reflect new numbering
- [ ] Add T32.G4.06 (phishing reporting)
- [ ] Add T32.G5.10 (password strength evaluation)
- [ ] Clarify MFA (G3.01) vs 2FA (G4.04) descriptions

### Should Complete in Phase 2:
- [ ] Add implementation notes to all G3-G8 skills
- [ ] Add 4 mobile device security skills (G4.07, G5.11, G6.09, G7.06)
- [ ] Update X-2 borderline dependencies (G6.05, G6.08)
- [ ] Review G4.01 and add assessment specificity
- [ ] Consider reorganizing G6.01 malware sub-skills

### Consider for Future:
- [ ] Add social media safety skills (6+ skills across G3-G8)
- [ ] Add safe search/content credibility skills (G3-G6)
- [ ] Add cyberbullying prevention expansion
- [ ] Add misinformation/deepfakes skills (G7-G8)

---

## DEPENDENCY UPDATES AFTER RENUMBERING

### Skills That Reference Old Numbers (Update These):

#### References to G5.01.01 → Change to G5.01:
- T32.G5.02 (currently G5.01.02)
- T32.G6.01 (currently G6.01.01)
- T32.G6.06 (currently G6.03)
- T32.G7.02
- T32.G7.04 (currently G7.04.01)

#### References to G5.03.01 → Change to G5.04:
- T32.G5.05 (currently G5.03.02)
- T32.G5.06 (currently G5.03.03)
- T32.G7.04 (currently G7.04.01)

#### References to G6.01.01 → Change to G6.01:
- T32.G6.02 (becomes G6.02 phishing)
- T32.G6.03 (becomes G6.03 network)
- T32.G6.04 (becomes G6.04 SQL)
- T32.G6.06 (currently G6.03 AI threat)
- T32.G6.07 (currently G6.04 ethical hacking)
- T32.G7.03
- T32.G8.01
- T32.G8.02
- T32.G8.03 (currently G8.03.01)
- T32.G8.05 (currently G8.04)

#### References to other renumbered skills:
Update systematically using find-replace after implementing flat numbering scheme.

---

## SKILL COUNT BEFORE/AFTER

**Current (with sub-numbering):**
- Total: 47 skills
- K: 4, G1: 4, G2: 6, G3: 5, G4: 5, G5: 9, G6: 8, G7: 5, G8: 4

**After Critical Fixes (renumbering only):**
- Total: 47 skills (same)
- K: 4, G1: 4, G2: 6, G3: 5, G4: 5, G5: 9, G6: 8, G7: 5, G8: 5

**After High Priority Additions:**
- Total: 53 skills (+6)
- K: 4, G1: 4, G2: 6, G3: 5, G4: 7 (+2), G5: 11 (+2), G6: 9 (+1), G7: 6 (+1), G8: 5

**After All Recommended Additions:**
- Total: 59 skills (+12)
- Distribution more balanced across grades

---

**END OF QUICK REFERENCE**
