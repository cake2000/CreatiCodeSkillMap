# T32 – Cybersecurity & Digital Safety: Phase 1 Optimization Summary

**Date:** November 25, 2025
**Topic:** T32 – Cybersecurity & Digital Safety
**Domain:** D5 – Systems & Society

## Overview

Phase 1 optimization focused on breaking down overly broad skills into smaller, manageable learning objectives following the "IXL for coding" model. Each skill should target ONE specific concept that can be assessed independently.

## Skills Broken Down (4 Original → 15 Sub-Skills)

### 1. T32.G6.01 - Identify common malware types (Split into 4)

**Original:** One skill covering viruses, ransomware, spyware, and trojans

**Now Split Into:**
| ID | Skill | Description |
|----|-------|-------------|
| T32.G6.01.01 | Understand viruses and worms | Self-replicating malware that spreads system-to-system |
| T32.G6.01.02 | Understand ransomware | Data hostage attacks that encrypt files for payment |
| T32.G6.01.03 | Understand spyware | Monitoring malware that collects personal information |
| T32.G6.01.04 | Understand trojans | Malware disguised as legitimate software |

**Rationale:** Each malware type has distinct characteristics, attack vectors, and defenses. Students learn better with focused, single-concept lessons.

---

### 2. T32.G6.05 - Design secure login flows (Split into 3)

**Original:** One skill covering password length validation, password masking, AND attempt tracking

**Now Split Into:**
| ID | Skill | Description |
|----|-------|-------------|
| T32.G6.05.01 | Validate password length | Use string length blocks to check minimum 8 characters |
| T32.G6.05.02 | Implement password masking | Replace input characters with asterisks using string operations |
| T32.G6.05.03 | Track login attempts | Use counter variable and lockout after 3 failures |

**Rationale:** Each component involves different programming concepts (string manipulation, text display, counter logic). Breaking them down allows progressive skill building.

---

### 3. T32.G8.01 - Conduct mini penetration tests (Split into 4)

**Original:** One skill covering multiple test types (input fuzzing, special characters, negative numbers, weak passwords)

**Now Split Into:**
| ID | Skill | Description |
|----|-------|-------------|
| T32.G8.01.01 | Test input validation | Boundary cases with long text and special characters |
| T32.G8.01.02 | Test numeric inputs | Edge cases like negative numbers, decimals, zero |
| T32.G8.01.03 | Test authentication | Weak passwords and bypass attempts |
| T32.G8.01.04 | Document vulnerabilities | Create reports with severity ratings |

**Rationale:** Different test types require different testing strategies. Documentation is a separate, important skill for professional security work.

---

### 4. T32.G8.03 - Audit AI projects for security vulnerabilities (Split into 4)

**Original:** One skill covering chatbot injection, image filter bypass, sensor privacy, and reporting

**Now Split Into:**
| ID | Skill | Description |
|----|-------|-------------|
| T32.G8.03.01 | Test chatbots for prompt injection | Attempt to bypass AI instructions with crafted inputs |
| T32.G8.03.02 | Audit image generation | Test for content filter bypass techniques |
| T32.G8.03.03 | Audit sensor systems | Examine privacy vulnerabilities in T23 projects |
| T32.G8.03.04 | Create security audit report | Document findings with risk ratings and recommendations |

**Rationale:** Each AI system type (chatbots, image generators, sensors) has unique security considerations. Professional reporting is a distinct skill.

---

## Dependency Updates Summary

### Updated to depend on T32.G6.01 sub-skills:
- T32.G6.02 → T32.G6.01.01
- T32.G6.03 → T32.G6.01.01
- T32.G6.04 → T32.G6.01.04 (trojans most relevant to injection attacks)
- T32.G6.06 → T32.G6.01.01
- T32.G6.07 → T32.G6.01.01
- T32.G7.03 → T32.G6.01.01
- T32.G7.04 → T32.G6.01.01
- T32.G8.01.01 → T32.G6.01.01
- T32.G8.02 → T32.G6.01.01
- T32.G8.03.01 → T32.G6.01.01
- T32.G8.05 → T32.G6.01.01

### Updated to depend on T32.G6.05 sub-skills:
- T32.G7.02 → T32.G6.05.03 (account lockout relevant to password cracking)
- T32.G8.02 → T32.G6.05.01, T32.G6.05.03

### Updated to depend on T32.G8.03 sub-skills:
- T32.G8.04 → T32.G8.03.04
- T32.G8.05 → T32.G8.03.04

---

## Statistical Summary

| Metric | Count |
|--------|-------|
| Original skills broken down | 4 |
| New sub-skills created | 15 |
| Net increase in skills | +11 |
| Dependency updates | 15 |
| Total T32 skills (K-8) | ~64 (was ~53) |

---

## Quality Assurance

- [x] No skills deleted (all converted to sub-skills)
- [x] All cross-topic dependencies preserved
- [x] Sub-skill numbering follows consistent pattern (T32.G#.##.##)
- [x] First sub-skill inherits original dependencies
- [x] Later sub-skills depend on first sub-skill (sequential learning)
- [x] All changes maintain X-2 rule
- [x] Each skill now targets ONE specific learning objective

---

## Skill Progression After Optimization

### Grade 6 Malware Unit (Example)
```
T32.G6.01.01 Viruses and Worms (foundational)
    ↓
T32.G6.01.02 Ransomware ─┐
T32.G6.01.03 Spyware    ├─ (can be parallel)
T32.G6.01.04 Trojans   ─┘
    ↓
T32.G6.02 Phishing patterns (builds on understanding malware delivery)
```

### Grade 6 Secure Login Unit (Example)
```
T32.G6.05.01 Password length validation
    ↓
T32.G6.05.02 Password masking
T32.G6.05.03 Login attempt tracking
    ↓
T32.G7.02 Password cracking simulation (uses lockout knowledge)
```

### Grade 8 Penetration Testing Unit (Example)
```
T32.G8.01.01 Input validation testing
    ↓
T32.G8.01.02 Numeric edge case testing ─┐
T32.G8.01.03 Authentication testing    ─┤ (parallel)
    ↓                                  ─┘
T32.G8.01.04 Vulnerability documentation (synthesis)
```

---

## Notes for Phase 2

The following items were NOT addressed in Phase 1 (intra-topic focus):
- Cross-topic dependency validation with T21-T24 (AI topics)
- Social media safety skills (potential addition)
- Mobile device security skills (potential addition)
- Distribution balance (G5-G6 have more skills than other grades)

These can be addressed in Phase 2 inter-topic coordination.

---

## Files Modified

- `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md` (lines 28627-28927)
