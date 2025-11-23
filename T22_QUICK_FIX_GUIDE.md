# T22 Quick Fix Reference Guide

## Skills That Changed

### ID Changes (3 skills)

| Old ID | New ID | Skill Name | Change Reason |
|--------|--------|------------|---------------|
| T22.G5.1.5 | T22.G5.04 | Use a chatbot block to get AI responses | Invalid format (dot notation), reordered to foundational position |
| T22.G5.04 | T22.G5.05 | Identify ChatGPT block parameters | Renumbered to make room for foundational skill |
| T22.G6.05.5 | T22.G6.05 | Implement session management | Invalid format (dot notation), enhanced description |

### Description Changes (1 skill)

**T22.G6.05** (formerly T22.G6.05.5):
- **Old Title**: "Understand chatbot session types"
- **New Title**: "Implement session management for multi-turn conversations"
- **Enhancement**: Changed from passive observation to active implementation with specific deliverable (build project, implement "New Chat" button)

### Dependency Updates (3 skills)

**T22.G5.05** (formerly T22.G5.04):
- Changed dependency from T22.G5.1.5 → T22.G5.04

**T22.G6.01**:
- Changed dependency from T22.G5.04 → T22.G5.05

**T22.G6.04.01**:
- Changed dependency from T22.G5.1.5 → T22.G5.04

---

## Grade 5 New Sequence

1. **T22.G5.01**: Flag risky vs safe chatbot prompts
2. **T22.G5.02**: Observe chatbot strengths and weaknesses through testing
3. **T22.G5.03**: Experiment with prompt phrasing to improve responses
4. **T22.G5.04**: Use a chatbot block to get AI responses ← **MOVED HERE**
5. **T22.G5.05**: Identify ChatGPT block parameters in starter code ← **RENUMBERED**

---

## Quick Checklist for Updating References

- [ ] Update any reference to T22.G5.1.5 → T22.G5.04
- [ ] Update any reference to T22.G5.04 → T22.G5.05
- [ ] Update any reference to T22.G6.05.5 → T22.G6.05
- [ ] Verify all dependencies point to correct new IDs
- [ ] Update curriculum materials with new IDs
- [ ] Update assessment rubrics with new skill numbers

---

## What Was NOT Changed

- **No skills deleted**: All 38 original skills preserved
- **No skills added**: Focused on fixing existing issues only
- **All cross-topic dependencies preserved**: T06, T08, T09, T16, T21, T03 references unchanged
- **K-4 skills unchanged**: All foundational skills remain as-is
- **G7-8 skills unchanged**: All advanced skills remain as-is
- **Most G6 skills unchanged**: Only dependency references updated

---

## Files Generated

1. **T22_FIXED_COMPLETE.md** - Complete T22 section ready to paste into allskills.md
2. **T22_COMPREHENSIVE_CHANGES_SUMMARY.md** - Detailed documentation of all changes
3. **T22_QUICK_FIX_GUIDE.md** - This quick reference guide

---

## How to Apply the Fix

1. Open `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md`
2. Locate the T22 section (starts at ID: T22.GK.01)
3. Delete the entire T22 section (stop before ID: T23.GK.01)
4. Copy the entire contents of `T22_FIXED_COMPLETE.md`
5. Paste into allskills.md where T22 section was
6. Save the file
7. Verify git diff shows only the 3 ID changes and 1 description enhancement

---

## Verification Steps

After applying the fix, verify:

✅ All T22 skill IDs follow T22.GX.XX or T22.GX.XX.XX format (no dots like G5.1.5)
✅ T22.G5.04 comes before T22.G5.05 in the file
✅ T22.G6.05 exists (not T22.G6.05.5)
✅ All dependencies reference existing skill IDs
✅ No forward references within T22 (skills only depend on earlier skills)
✅ All cross-topic dependencies (T06, T08, T09, etc.) preserved
