# T30 (Devices & Hardware Systems) Analysis Report

## Executive Summary

**Total T30 Skills: 42**
- GK: 3 skills
- G1: 3 skills
- G2: 4 skills
- G3: 4 skills
- G4: 4 skills
- G5: 4 skills
- G6: 4 skills
- G7: 5 skills
- G8: 4 skills

**Overall Assessment**: T30 has significant platform misalignment issues. Many skills reference generic hardware concepts (motherboards, CPUs, GPUs, TPUs, storage devices) that are not directly relevant to CreatiCode's browser-based coding environment. The topic needs refocusing to emphasize the actual device capabilities students can leverage in CreatiCode projects.

---

## CreatiCode Platform Hardware Capabilities

Based on analysis of `/media/binyu/USB2/ScratchCopilot/blockdes8.txt`, CreatiCode supports:

### 1. Input Devices
- **Keyboard**: Key press detection
- **Mouse**: Left/right button clicks, drag events, mouse wheel, pointer position
- **Touch**: Drag events for sprites
- **Virtual Joysticks**: Left/right joysticks for 3D scenes

### 2. Camera & Vision
- **3D Scene Cameras**: Orbit camera, follow camera, free camera with various configurations
- **Device Camera (AI-powered)**:
  - Face detection
  - 2D/3D body pose detection
  - Hand detection
  - Video feed processing

### 3. Microphone & Audio
- **Speech Recognition**: Microsoft Azure and OpenAI Whisper APIs
- **Continuous Speech Recognition**: Real-time streaming
- **Text-to-Speech**: Azure voice synthesis
- **Audio Recording**: Save voice input

### 4. Output Devices
- **Display**: Stage rendering, speech bubbles, 3D graphics
- **Audio**: Sound playback, text-to-speech output

### 5. AI-Powered Hardware Integration
- Camera-based computer vision (face, body, hand tracking)
- Microphone-based speech recognition
- Real-time sensor data processing

**CRITICAL FINDING**: CreatiCode does NOT provide direct access to:
- Motherboards, CPUs, RAM, storage internals
- Physical sensors (accelerometers, gyroscopes)
- GPUs/TPUs for custom AI training
- Network hardware or protocols
- Physical peripheral ports (USB, HDMI, etc.)

---

## HIGH Priority Issues

### H1: Platform Misalignment - CPU/GPU/Motherboard Focus (G4-G8)
**Affected Skills**: T30.G4.01, G4.02, G5.01, G6.02, G7.01, G7.04, G8.01

**Problem**: Multiple skills focus on internal computer components (motherboards, CPU cores, GPUs, TPUs, SSDs vs HDDs) that students cannot interact with or observe in CreatiCode's browser-based environment.

**Examples**:
- T30.G4.01: "Diagram motherboard data flow" - Not observable in CreatiCode
- T30.G4.02: "Explain how CPU speed/core count affects tasks" - Not controllable in CreatiCode
- T30.G7.04: "Compare CPUs, GPUs, and TPUs for AI workloads" - CreatiCode uses cloud APIs, students don't choose hardware
- T30.G6.02: "Evaluate storage solutions (SSD, HDD, cloud)" - Not relevant to browser-based coding

**Recommendation**: Replace these skills with platform-aligned alternatives focusing on:
- How to optimize projects for different devices (mobile vs desktop)
- Understanding API response times and cloud processing
- Device capabilities detection (does device have camera/microphone?)
- Performance monitoring within CreatiCode projects

**Impact**: 7+ skills need major revision


### H2: Missing Core CreatiCode Hardware Features
**Problem**: Critical device interaction capabilities are completely missing from the skill map.

**Missing Skills**:
1. **Camera Integration** (G3-G5 range):
   - Access device camera for AI vision projects
   - Understand camera permissions and privacy
   - Use face/hand/body detection blocks

2. **Microphone Integration** (G3-G5 range):
   - Access device microphone for speech recognition
   - Record and process audio input
   - Use speech-to-text and text-to-speech blocks

3. **Input Device Programming** (G2-G4 range):
   - Detect keyboard key presses in projects
   - Respond to mouse events (click, drag, wheel)
   - Use virtual joysticks in 3D games

4. **3D Camera Controls** (G5-G7 range):
   - Configure orbit/follow/free cameras
   - Understand camera target and viewport
   - Control camera with keyboard/mouse input

**Recommendation**: Add 8-10 new skills covering actual CreatiCode device capabilities

**Impact**: Major gap in practical hardware skills


### H3: Dependency Issues

#### H3a: Cross-grade dependency violations
**T30.G3.02** depends on **T09.G3.01** (variables)
- Problem: Students are learning about peripheral ports while simultaneously learning variables? These concepts are unrelated and shouldn't be co-dependent.
- **Fix**: Remove T09.G3.01 dependency; peripheral ports is a conceptual skill that doesn't require coding

**T30.G3.01** depends on **T07.G3.01** (loops)
- Problem: Connecting sensors to project ideas shouldn't require understanding loops first
- **Fix**: This dependency makes sense only if the skill involves actually USING sensors in code. If conceptual, remove it.

#### H3b: Inappropriate dependencies from other topics
**T30.G4.01** depends on **T02.G3.01** (flowchart symbols)
- Problem: Why does understanding motherboard data flow require knowing flowchart symbols from T02? These are different abstraction levels.
- **Fix**: If keeping the motherboard skill, use T30's own input→process→output skill as dependency instead

**T30.G4.02** depends on **T08.G3.01** (conditionals)
- Problem: Explaining CPU performance doesn't require coding knowledge
- **Fix**: Remove this dependency

**T30.G4.04** depends on **T04.G2.01** (patterns)
- Problem: Exploring accessibility hardware doesn't relate to pattern recognition
- **Fix**: Should depend on T30.G3.01 (sensors/actuators) instead


### H4: Circular/Problematic Internal Dependencies

**T30.G3.02 → T30.G3.01 → T30.G2.01 + T30.G2.02**
- Problem: G3.02 (peripheral ports) depends on G3.01 (sensors/actuators), which makes sense
- However, G3.02 also lists as dependency in the grep output for later skills
- **Verify**: Ensure no circular dependencies

**T30.G7.02 and G7.03**:
- G7.03 depends on G7.02 (design redundancy → plan degradation) - GOOD
- But both appear in G8 dependencies - ensure no circularity

---

## MEDIUM Priority Issues

### M1: Grade Appropriateness - Too Abstract for K-2

**T30.GK-G2 Skills Assessment**: Generally appropriate (picture-based, concrete)
- GK.01: Identify devices ✓
- GK.02: Match devices to actions ✓
- GK.03: Input vs output ✓
- G1.01: Label computer parts ✓
- G1.02: Hardware vs software ✓
- G1.03: Recognize sensors ✓
- G2.01: CPU/RAM/Storage analogies ⚠️ (borderline - might be too abstract)
- G2.02: Input→Process→Output ✓
- G2.03: Wired vs wireless ✓
- G2.04: Device care ✓

**Issue with G2.01**: Using analogies (brain, backpack) for CPU/RAM/storage might be too abstract for Grade 2. Consider making this more concrete with observable examples.


### M2: Vague or Unclear Skill Descriptions

**T30.G3.03**: "Compare saving locally vs in the cloud"
- Problem: CreatiCode projects are cloud-saved by default. What does "locally" mean in a browser environment? Downloaded JSON files?
- **Fix**: Clarify what local vs cloud means in CreatiCode context, or refocus on online vs offline access


**T30.G5.01**: "Match CreatiCode AI features to hardware requirements"
- Problem: Students don't choose hardware for CreatiCode - it runs in browser and uses cloud APIs
- **Fix**: Change to "Identify device requirements for CreatiCode AI features" (camera for vision, microphone for speech, etc.)


**T30.G6.04**: "Plan hardware requirement checklists for AI projects"
- Problem: Too vague - what specific hardware? What level of detail?
- **Fix**: Make more specific: "Create device capability checklists for AI projects (camera resolution for face detection, microphone quality for speech recognition, internet speed for cloud APIs)"


### M3: Missing Scaffolding

**Gap between G1.03 and G3.01**:
- G1.03: Recognize sensors in environment (automatic doors, faucets)
- [G2 has no sensor-related skills]
- G3.01: Connect project ideas to sensors/actuators

**Missing**: G2 skill about types of sensors (camera, microphone, motion) and what they detect
- **Recommendation**: Add T30.G2.05: "Identify common device sensors and their inputs"


**Gap in camera/microphone progression**:
- No introduction to camera/microphone before jumping to AI features in G5+
- **Recommendation**: Add G3-G4 skills about basic camera/microphone usage before AI applications


### M4: Inconsistent CreatiCode Integration

**Good Examples** (mention CreatiCode appropriately):
- T30.G3.01: "map CreatiCode ideas (voice assistant, motion game...)"
- T30.G3.03: "saving a project... vs CreatiCode cloud"
- T30.G5.01: "Match CreatiCode AI features..."

**Missing CreatiCode Context**:
- T30.G6.01: "analyze sensor specifications" - no mention of which sensors are in CreatiCode
- T30.G7.02: "design redundancy for sensors" - which sensors? CreatiCode-specific examples?
- T30.G8.01: "edge vs cloud processing" - good concept but needs CreatiCode framing

**Recommendation**: Add CreatiCode context to G6-G8 skills to ground abstract concepts


### M5: Accessibility Skills Placement Issues

**T30.G4.04**: "Explore accessibility hardware"
- Dependencies: T04.G2.01 (patterns) + T30.G3.01 (sensors)
- Problem: The pattern dependency is bizarre and unmotivated

**T30.G5.04**: "Relate hardware choices to accessibility outcomes"
- Dependencies: T30.G5.01 + T30.G4.04
- This progression makes sense internally

**Issue**: Accessibility is introduced at G4, which is good, but the skill itself needs better integration with CreatiCode's actual accessibility features (if any).

**Recommendation**:
- Check if CreatiCode has accessibility APIs or features
- If yes, make skills more specific to those features
- If no, frame skills around designing accessible projects despite hardware limitations

---

## LOW Priority Issues

### L1: Minor Wording Improvements

**T30.G2.01**: "match simplified analogies (brain, short-term memory, backpack) to CPU, RAM, and storage"
- Suggestion: Clarify this is an educational analogy, not how computers actually work
- Better: "use everyday analogies to understand computer components"


**T30.G3.04**: "Identify power sources for portable devices"
- Suggestion: Add CreatiCode context - "and explain how power affects project runtime"


**T30.G7.05**: "Debate privacy implications of AI-powered sensors"
- Good skill but very long description
- Suggestion: Shorten to key point: "Analyze privacy tradeoffs when using cameras/microphones in AI projects"


### L2: Standards Alignment Gaps

**T30.G7.03** is the ONLY skill with CSTA/AI4K12 standards listed:
- CSTA: MS-SAS-HW-01, CAS-ET-05
- AI4K12: A3 Human Agency; D1 Ethical Design

**Issue**: Other skills likely align with standards too but aren't tagged

**Recommendation**: Add standards to other relevant skills:
- GK-G2: CSTA 1A-CS-01, 1A-CS-02 (computing systems)
- G3-G5: CSTA 1B-CS-01, 2-CS-01 (devices, components)
- G6-G8: CSTA 2-CS-02, 2-CS-03 (troubleshooting, collaboration)
- AI skills: AI4K12 perception, sensors


### L3: Sustainability Skill Position

**T30.G8.02**: "Evaluate sustainability & lifecycle impacts"
- Good topic but somewhat disconnected from other G8 skills
- Could be expanded or moved to a broader "responsible computing" topic
- Consider adding earlier introduction to sustainability concepts

---

## Recommended Skill Additions

### New Skills Needed for CreatiCode Alignment

**T30.G3.05**: Access device camera for projects
- Description: Students enable camera permissions and display camera feed in CreatiCode projects, understanding when and why camera access is needed.
- Dependencies: T30.G2.02 (input→process→output), T30.G1.03 (recognize sensors)

**T30.G3.06**: Access device microphone for audio input
- Description: Learners enable microphone permissions and record audio in CreatiCode, explaining when microphone access is appropriate.
- Dependencies: T30.G2.02 (input→process→output), T30.G1.03 (recognize sensors)

**T30.G4.05**: Respond to keyboard and mouse events
- Description: Students program sprites to respond to specific key presses, mouse clicks, and pointer movements in CreatiCode projects.
- Dependencies: T30.G3.01 (connect inputs to projects), T08.G3.01 (conditionals)

**T30.G4.06**: Detect device capabilities in projects
- Description: Learners write code to check if device has camera/microphone and display appropriate messages when hardware is unavailable.
- Dependencies: T30.G3.05, T30.G3.06, T08.G3.01 (conditionals)

**T30.G5.05**: Configure 3D cameras for game scenes
- Description: Students add and configure orbit, follow, and free cameras in 3D CreatiCode projects, controlling camera distance, angles, and input methods.
- Dependencies: T30.G4.05 (keyboard/mouse), T30.G3.01 (sensors/actuators)

**T30.G5.06**: Use face detection in interactive projects
- Description: Learners use CreatiCode face detection blocks to create projects that respond to facial recognition, understanding data privacy implications.
- Dependencies: T30.G3.05 (camera access), T30.G4.06 (capability detection)

**T30.G6.05**: Use speech recognition in voice-controlled projects
- Description: Students implement speech-to-text and text-to-speech blocks to create voice-controlled CreatiCode projects, comparing Azure and OpenAI APIs.
- Dependencies: T30.G3.06 (microphone), T30.G5.01 (AI hardware requirements)

**T30.G6.06**: Implement hand/body tracking features
- Description: Learners use hand and body pose detection to create gesture-controlled games, analyzing when computer vision is more appropriate than keyboard/mouse input.
- Dependencies: T30.G5.06 (face detection), T30.G4.05 (input events)

**T30.G7.06**: Optimize projects for mobile vs desktop devices
- Description: Students analyze how their CreatiCode projects perform on different devices and make design decisions based on screen size, touch vs mouse, and processing capabilities.
- Dependencies: T30.G4.05 (input methods), T30.G5.05 (camera config)

**T30.G7.07**: Handle camera/microphone permission errors
- Description: Learners design error handling for when users deny camera/microphone permissions, implementing graceful fallbacks and informative messages.
- Dependencies: T30.G4.06 (capability detection), T08.G5.01 (error handling if it exists)

---

## Skills to Remove or Heavily Revise

### Remove (Not Platform-Aligned)

1. **T30.G4.01**: Diagram motherboard data flow
   - Reason: Students can't observe this in CreatiCode
   - Replacement: "Trace data flow in CreatiCode AI projects (camera → detection → sprite action)"

2. **T30.G6.02**: Evaluate storage solutions (SSD, HDD, cloud)
   - Reason: Not relevant to browser-based coding
   - Replacement: "Compare browser storage options (local storage, cloud save, export)"

3. **T30.G7.01**: Analyze energy consumption & thermal limits
   - Reason: Not observable or controllable in CreatiCode
   - Possible Revision: "Monitor project performance and frame rate" (if CreatiCode has performance metrics)

### Heavily Revise (Platform Misalignment)

4. **T30.G4.02**: Explain how CPU speed/core count affects tasks
   - Revision: "Explain how device performance affects project responsiveness (frame rate, AI processing time)"

5. **T30.G5.01**: Match CreatiCode AI features to hardware requirements
   - Revision: "Identify device requirements for CreatiCode AI features (camera for vision, microphone for speech, internet for cloud APIs)"

6. **T30.G7.04**: Compare CPUs, GPUs, and TPUs for AI workloads
   - Revision: "Explain cloud vs edge processing in CreatiCode AI projects (local camera processing vs cloud API calls)"

7. **T30.G8.01**: Architect edge vs cloud processing for AI pipelines
   - Keep concept but revise: "Design CreatiCode projects that balance local device processing (camera feed, user input) with cloud API calls (speech recognition, image generation)"

---

## Summary of Issues by Category

| Category | High | Medium | Low | Total |
|----------|------|--------|-----|-------|
| Platform Misalignment | 7 | 3 | 0 | 10 |
| Missing Skills | 10 | 3 | 0 | 13 |
| Dependencies | 7 | 0 | 0 | 7 |
| Grade Appropriateness | 0 | 1 | 0 | 1 |
| Clarity | 0 | 3 | 3 | 6 |
| Standards Alignment | 0 | 0 | 1 | 1 |
| **TOTAL** | **24** | **10** | **4** | **38** |

---

## Recommended Action Plan

### Phase 1: Critical Fixes (HIGH Priority)
1. Remove or revise 7 CPU/GPU/motherboard-focused skills (H1)
2. Add 10 new skills for camera, microphone, input devices (H2)
3. Fix 7 cross-topic dependency issues (H3)

### Phase 2: Improvements (MEDIUM Priority)
1. Clarify 3 vague skill descriptions (M2)
2. Add missing G2 sensor skill and G3-G4 camera/mic skills (M3)
3. Add CreatiCode context to G6-G8 skills (M4)
4. Fix accessibility skill dependencies (M5)

### Phase 3: Polish (LOW Priority)
1. Minor wording improvements (L1)
2. Add CSTA/AI4K12 standards to all relevant skills (L2)
3. Consider sustainability skill placement (L3)

---

## Conclusion

T30 (Devices & Hardware Systems) requires significant revision to align with CreatiCode's actual platform capabilities. The current skill map focuses heavily on internal computer hardware (motherboards, CPUs, storage) that students cannot interact with in a browser-based coding environment.

The topic should be refocused to emphasize:
- Device input/output capabilities students can actually use (camera, microphone, keyboard, mouse)
- CreatiCode-specific hardware integration (AI vision, speech recognition, 3D cameras)
- Practical device capability detection and error handling
- Cloud vs local processing tradeoffs in web-based coding

By implementing the recommended changes, T30 will become a practical, platform-aligned topic that teaches students how to leverage real device capabilities in their CreatiCode projects while building conceptual understanding of hardware systems.
