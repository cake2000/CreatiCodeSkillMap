# T30 Quick Reference: Skills Requiring Action

**Date:** 2024-11-24

---

## 🔴 CRITICAL - Must Fix (5 skills)

### Split These Broad Skills

**T30.G4.05** – Respond to keyboard and mouse events in CreatiCode
- 🔨 Split into: keyboard events + mouse events + sprite drag events

**T30.G6.05** – Use speech recognition in voice-controlled CreatiCode projects
- 🔨 Split into: one-shot speech + continuous streaming + text-to-speech

**T30.G6.06** – Implement hand and 2D body tracking in CreatiCode projects
- 🔨 Split into: hand tracking + 2D body tracking

### Fix These Overlaps

**T30.G3.03** vs **T30.G6.02** – Storage comparison overlap
- 🔨 Keep G3.03 as cloud vs export
- 🔨 Revise G6.02 to focus on browser storage APIs (localStorage, IndexedDB)

### Review Sub-skill Logic

**T30.G4.03.01** – Compare 2D camera widgets vs 3D webcam backgrounds
- ❓ Why is this a sub-skill of G4.03 (latency vs bandwidth)?
- 🔨 Review dependency logic, consider making standalone

---

## ⚠️ HIGH PRIORITY - Should Fix (8 skills)

### Make These More Hands-On

**T30.G4.01** – Trace data flow in CreatiCode AI projects
- 🔨 Change from "diagram" to "implement and diagram"
- 🔨 Add specific deliverable requirements

**T30.G5.03** – Explain how different sensors collect data
- 🔨 Change from "explain" to "capture and display raw sensor data"
- 🔨 Add hands-on component for G5

**T30.G6.01** – Analyze sensor specifications for CreatiCode projects
- 🔨 Add implementation: "analyze specs AND implement adaptive project"
- 🔨 Needs coding component for G6

**T30.G7.01** – Monitor and optimize CreatiCode project performance
- 🔨 Specify exact metrics (FPS, lag, memory)
- 🔨 Specify exact tools (Chrome DevTools, etc.)

### Add Missing Skills

**[NEW] G4/G5** – Basic audio recording and playback
- 🆕 Gap between G3.06 (microphone access) and G6.05 (speech AI)
- 🆕 Add non-AI audio skill

**[NEW] G5** – Raw sensor data processing
- 🆕 Skills for working with pixels, waveforms, raw data
- 🆕 Bridge between access and AI processing

**[NEW] G3/G4** – Camera/microphone ready events
- 🆕 Basic event handling before full AI projects
- 🆕 Transition skill between G3.05/06 and G4.01

### Fix Dependencies

**T30.G4.05** and many others
- 🔨 Add T08 (conditionals) dependency (event handlers need if statements)
- 🔨 Add T09 (variables) where sensor data is stored

---

## ℹ️ MEDIUM PRIORITY - Consider (6 skills)

### Review Conceptual Skills for Coding

**T30.G5.02** – Plan safe device-handling procedures for group work
- ℹ️ This is classroom management, not CS
- 🔄 Consider moving to teacher guide or removing

**T30.G5.04** – Relate hardware choices to accessibility outcomes
- ℹ️ Important but belongs in T16 (Accessibility)
- 🔄 Consider moving to T16

**T30.G7.05** – Debate privacy implications of AI-powered sensors
- ℹ️ Good ethics skill but needs coding component
- 🔄 Add: "implement privacy controls in project"

**T30.G8.02** – Evaluate sustainability & lifecycle impacts
- ℹ️ Research skill, not coding
- 🔄 Add: "measure and optimize energy usage in project"

### Review Sub-skill Placement

**T30.G5.06.01** – Select appropriate sensors for different project types
- ❓ Why is this a sub-skill of G5.06 (face detection)?
- 🔄 Consider making standalone or moving to different parent

**T30.G6.06.02** – Implement 3D object dragging with mouse
- ❓ Is this placement logical under G6.06 (body tracking)?
- 🔄 Review dependency

---

## All T30 Skills by Grade (54 total)

### Kindergarten (3 skills) ✅
- T30.GK.01 – Identify everyday computing devices
- T30.GK.02 – Match devices to actions
- T30.GK.03 – Recognize input vs output examples

### Grade 1 (3 skills) ✅
- T30.G1.01 – Label basic computer parts
- T30.G1.02 – Describe hardware vs software
- T30.G1.03 – Recognize sensors in the environment

### Grade 2 (5 skills) ✅
- T30.G2.01 – Explain core internal components
- T30.G2.02 – Trace input → process → output
- T30.G2.03 – Compare wired vs wireless connections
- T30.G2.04 – Share best practices for caring for devices
- T30.G2.05 – Identify common device sensors and their inputs

### Grade 3 (6 skills) ✅
- T30.G3.01 – Connect project ideas to required sensors/actuators
- T30.G3.02 – Identify device input types for CreatiCode projects
- T30.G3.03 – Compare CreatiCode cloud save vs local export options
- T30.G3.04 – Explain how sensors provide input to computer programs
- T30.G3.05 – Access device camera in CreatiCode projects ⚡
- T30.G3.06 – Access device microphone for audio input ⚡

### Grade 4 (6 skills + 1 sub) ⚠️
- T30.G4.01 – Trace data flow in CreatiCode AI projects [needs hands-on]
- T30.G4.02 – Explain how device performance affects project responsiveness
- T30.G4.03 – Differentiate latency vs bandwidth
  - T30.G4.03.01 – Compare 2D camera widgets vs 3D webcam [sub-skill logic?]
- T30.G4.04 – Explore accessibility hardware
- T30.G4.05 – Respond to keyboard and mouse events ⚡ [TOO BROAD - split]
  - T30.G4.05.01 – Add camera preview widgets ⚡

### Grade 5 (7 skills + 2 subs) ⚠️
- T30.G5.01 – Identify device requirements for CreatiCode AI features
- T30.G5.02 – Plan safe device-handling procedures [move to teacher guide?]
- T30.G5.03 – Explain how different sensors collect data [needs hands-on]
- T30.G5.04 – Relate hardware choices to accessibility [move to T16?]
- T30.G5.05 – Configure 3D cameras for CreatiCode game scenes ⚡
  - T30.G5.05.01 – Enable mouse picking and hovering for 3D objects ⚡
- T30.G5.06 – Use face detection in CreatiCode interactive projects ⚡
  - T30.G5.06.01 – Select appropriate sensors for project types [placement?]

### Grade 6 (7 skills + 3 subs) ⚠️
- T30.G6.01 – Analyze sensor specifications [needs hands-on]
- T30.G6.02 – Compare browser storage options [FIX OVERLAP with G3.03]
- T30.G6.03 – Explain camera and microphone privacy permissions
- T30.G6.04 – Plan device capability checklists for CreatiCode AI projects
- T30.G6.05 – Use speech recognition ⚡ [TOO BROAD - split]
  - T30.G6.05.01 – Use webcam as 3D scene background for AR effects ⚡
- T30.G6.06 – Implement hand and 2D body tracking ⚡ [TOO BROAD - split]
  - T30.G6.06.01 – Use 3D pose detection for depth-aware tracking ⚡
  - T30.G6.06.02 – Implement 3D object dragging with mouse ⚡

### Grade 7 (7 skills) ⚠️
- T30.G7.01 – Monitor and optimize CreatiCode project performance [needs specifics]
- T30.G7.02 – Design redundancy and fail-safes for CreatiCode sensors
- T30.G7.03 – Plan graceful degradation strategies
- T30.G7.04 – Explain cloud vs edge processing in CreatiCode AI projects
- T30.G7.05 – Debate privacy implications of AI-powered sensors [add coding]
- T30.G7.06 – Optimize CreatiCode projects for mobile vs desktop ⚡
- T30.G7.07 – Handle camera and microphone permission errors ⚡

### Grade 8 (4 skills) ✅
- T30.G8.01 – Design device-cloud architecture for CreatiCode AI projects
- T30.G8.02 – Evaluate sustainability & lifecycle impacts [add coding]
- T30.G8.03 – Plan hardware integration tests
- T30.G8.04 – Publish hardware requirement/playbooks for teams

**Legend:**
- ✅ Grade level is good
- ⚠️ Grade level needs review
- ⚡ Hands-on coding skill
- [issue] = Notes on problems

---

## Summary Counts

| Issue Type | Count |
|------------|-------|
| Skills too broad (need splitting) | 3 |
| Skills overlap/duplicate | 2 |
| Skills need hands-on coding | 5 |
| Skills need clearer specs | 2 |
| Sub-skills with unclear placement | 3 |
| Missing skills (gaps in progression) | 3 |
| Skills that might belong elsewhere | 3 |

**Total skills needing attention: 21 out of 54 (39%)**

---

## Next Actions Checklist

- [ ] Split T30.G4.05 into 2-3 skills
- [ ] Split T30.G6.05 into 2-3 skills
- [ ] Split T30.G6.06 into 2 skills
- [ ] Fix T30.G6.02 to avoid G3.03 overlap
- [ ] Review all 6 sub-skill placements for logic
- [ ] Add hands-on coding to G4.01, G5.03, G6.01, G7.01
- [ ] Add missing G4/G5 audio skill
- [ ] Add T08 dependencies to event-based skills
- [ ] Review G5.02, G5.04 for potential removal/move
- [ ] Add coding components to G7.05, G8.02
- [ ] Specify exact tools/metrics for G7.01
- [ ] Add success criteria to all skills

---

**For full analysis, see:** T30_COMPREHENSIVE_ANALYSIS_2024-11-24.md
