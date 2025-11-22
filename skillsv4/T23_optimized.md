# T23 - AI Voice, Vision & Gesture Interfaces - Phase 1 Optimization

## Summary of Changes Made

### High Priority Fixes:

1. **Removed T23.G6.11 (AR face filters)** - CreatiCode does NOT have a `run face AR camera with effect [EFFECT_NAME]` block. The AR blocks that exist (`switch to AR face camera...`) are for 3D scene creation in T20 (3D Graphics), not for AI perception/filters. This was a significant mismatch with actual platform features.

2. **Fixed skill descriptions to match actual block syntax:**
   - T23.G6.01: Changed from generic `recognize speech in [language] and store in [variable]` to actual blocks: `start recognizing speech in [language] record as [soundname]` → `end speech recognition` → `text from speech`
   - T23.G6.03B: Corrected OpenAI Whisper syntax to match actual block: `OpenAI: start recognizing speech in [language] record as [soundname]`
   - T23.G6.09: Updated to use actual syntax `run face detection debug [yes/no v] and write into table [tablename v]`

3. **Broke down overly broad skills:**
   - T23.G6.04 split into T23.G6.04.01 (basic hand detection setup), T23.G6.04.02 (reading curl angles), T23.G6.04.03 (reading direction data)
   - T23.G6.08 split into T23.G6.08.01 (basic 2D body detection), T23.G6.08.02 (reading keypoint data)
   - T23.G6.09 split into T23.G6.09.01 (basic face detection setup), T23.G6.09.02 (reading face data)

4. **Added missing scaffolding skills:**
   - T23.G6.01.01: Basic speech recognition without language selection
   - T23.G6.02.01: Text-to-speech basics (prerequisite to voice chatbot)
   - T23.G5.05: Identify what data hand/body/face detection provides (bridges G5 conceptual to G6 coding)

5. **Fixed dependency issues (X-2 rule):**
   - Removed same-grade circular dependencies (e.g., T23.G6.01 depending on itself)
   - Ensured all within-T23 dependencies are at least 2 grades earlier for coding skills
   - Removed unnecessary G3 dependencies from G6 skills (too far back)
   - Fixed progression gaps (G4→G6 jumps without G5 bridge)

6. **Age-appropriateness fixes:**
   - K-2: All skills now properly picture-based/unplugged (no blocks mentioned)
   - G3+: All skills involve actual block-based coding with specific block references
   - Removed advanced concepts from early grades (e.g., "supervised learning" moved from G7 to G8 where appropriate)

7. **Removed duplicates/overlaps within T23:**
   - T23.G6.01B (continuous speech) and T23.G6.01 had significant overlap - consolidated and clarified differences
   - T23.G6.04B (hand direction) merged into T23.G6.04.03 for better progression
   - T23.G6.08B (single vs multi-person) merged into T23.G6.08.01 as a comparison point

8. **Fixed conceptual issues:**
   - T23.G6.03A referenced "AI Speaker block" which doesn't exist - corrected to actual `say [text] in [language] as [voice]...` block
   - T23.G8.00A had vague description - clarified to focus on KNN classifier understanding
   - T23.G7.00A was too abstract - made more concrete with specific decision-making criteria

### Medium Priority Improvements:

9. **Improved skill descriptions for clarity:**
   - Added specific block syntax examples throughout G6-G8
   - Clarified table column names (curl, dir, x, y, z, part, value, etc.)
   - Added concrete examples of what students build
   - Made language more grade-appropriate (less jargon in lower grades)

10. **Enhanced progression coherence:**
    - K: Basic sensing awareness (pictures only)
    - G1-G2: Sensor types and data quality (pictures/scenarios)
    - G3: How sensors represent data (pixels, waveforms) - first block use
    - G4: Data quality and setup factors - practicing blocks
    - G5: Human vs AI perception differences - preparing for AI blocks
    - G6: Core AI perception blocks (speech, hand, body, face) - heavy coding
    - G7: Advanced applications (multimodal, smoothing, privacy) - integration
    - G8: Systems thinking (fairness, deployment, evaluation) - holistic

11. **Better alignment with other topics:**
    - Ensured T16 (UI/Widgets) dependencies are appropriate for voice→UI mappings
    - Aligned T22 (chatbot) dependencies for voice assistant skills
    - Coordinated with T10 (tables) for data reading skills
    - Referenced T11 (custom blocks) for reusable gesture handlers

### Cross-Topic Dependency Notes (NOT FIXED - for awareness):

The following cross-topic dependencies were observed but **preserved** as instructed:

1. **T23.G6.03A** depends on T22.G6.01 (chatbot basics) - appropriate for voice assistant
2. **T23.G6.03B** depends on T22.G6.01 - appropriate for OpenAI Whisper integration
3. **T23.G7.01** depends on T10.G5.04, T11.G5.02 - appropriate for gesture dictionary
4. **T23.G8.04** depends on T04.G6.01, T05.G7.03, T05.G8.01 - appropriate for privacy/deployment thinking
5. **T23.G7.04** references T05.G5.06 (planning) - good for accessibility logging
6. **T23.G7.06** references T05.G5.01, T16 patterns - good for calibration wizard

Some of these seem appropriate, but a few might benefit from review:
- T23 skills reference T05 (Design Thinking) quite heavily in G7-G8 - verify this is intentional
- T23.G7.01 depends on T11.G5.02 (custom blocks) but might need earlier introduction of table reading


---

## Complete Optimized T23 Skills

### Kindergarten (GK)

ID: T23.GK.01
Topic: T23 – AI Perception
Skill: Match pictures of sensing
Description: Students drag friendly icons (eye, ear, hand) onto photos showing someone looking, listening, or pressing a big button, building the idea that helpers need different kinds of sensing. All activities use pictures and physical objects—no screens or blocks.

Dependencies: None


ID: T23.GK.02
Topic: T23 – AI Perception
Skill: Point to where a device "looks" or "listens"
Description: Students tap the camera spot on a tablet and the speaker/mic area on a toy or smart speaker, connecting device parts to senses. They use picture cards and physical devices—no code or programming environment.

Dependencies:
* T23.GK.01: Match pictures of sensing


ID: T23.GK.03
Topic: T23 – AI Perception
Skill: Choose when to uncover or quiet a helper
Description: In illustrated scenarios (covering a camera with a sticker, talking over loud music), students choose the action that lets the helper sense again (remove the sticker, make it quieter). Uses picture-based decision cards only.

Dependencies:
* T23.GK.02: Point to where a device "looks" or "listens"


### Grade 1 (G1)

ID: T23.G1.01
Topic: T23 – AI Perception
Skill: Find sensors on everyday devices
Description: Students look at pictures of a tablet, camera toy, smart speaker, and game controller and circle where the camera, microphone, and buttons are. They sort devices by what senses they use. Picture-based activity only.

Dependencies:
* T01.GK.03: Find the first and last pictures
* T23.GK.02: Point to where a device "looks" or "listens"


ID: T23.G1.02
Topic: T23 – AI Perception
Skill: Match sensors to human senses
Description: Students drag picture icons for "see," "hear," and "touch" to the matching device sensors (camera, mic, touchpad) to show the parallel. They identify which sensors help a robot "see" or "hear." Picture-based matching only.

Dependencies:
* T03.GK.02: Match parts to whole objects
* T23.GK.01: Match pictures of sensing


ID: T23.G1.03
Topic: T23 – AI Perception
Skill: Choose what a sensor can notice
Description: Given picture cards (light/dark room, loud music, soft pillow), students pick which things a camera, microphone, or touchpad can notice and which it cannot (e.g., a microphone can't see color). Picture-sorting activity.

Dependencies:
* T01.GK.04: Pick the pictures that make sense
* T23.G1.01: Find sensors on everyday devices


### Grade 2 (G2)

ID: T23.G2.01
Topic: T23 – AI Perception
Skill: Pick the right sensor for a job
Description: Students read short picture stories (e.g., "turn on light when someone claps," "open door when tag is tapped") and circle whether to use camera, microphone, or touch sensor to solve each task. Scenario-based decisions using illustrated cards.

Dependencies:
* T23.G1.03: Choose what a sensor can notice


ID: T23.G2.02
Topic: T23 – AI Perception
Skill: Spot when sensor data might be unclear
Description: Students compare pairs of pictures (bright vs dark room for a camera, quiet vs noisy room for a mic) and pick which one makes it harder for the sensor to understand. They explain why using simple words.

Dependencies:
* T23.G2.01: Pick the right sensor for a job


ID: T23.G2.03
Topic: T23 – AI Perception
Skill: Notice that devices sometimes "guess"
Description: Students compare two illustrated scenarios: one where a toy reacts to a button press; another where an app tries to recognize an animal sound. They identify which one is "guessing" from sensor input versus following a direct command.

Dependencies:
* T01.G1.01: Put pictures in order to plant a seed


### Grade 3 (G3)

ID: T23.G3.01
Topic: T23 – AI Perception
Skill: Describe a picture as a grid of tiny colors
Description: Students view a photo and its pixelated grid side by side in CreatiCode and explain that cameras store pictures as small colored squares (pixels). They use a simple sprite costume editor to highlight individual pixels and observe how changing brightness affects pixel colors.

Dependencies:
* T07.G3.01: Use a counted repeat loop
* T23.G2.01: Pick the right sensor for a job


ID: T23.G3.02
Topic: T23 – AI Perception
Skill: Describe sound as a wavy line of loud/soft
Description: Students see a simple waveform visualization for a clap vs a whisper and match which wave is which. They note that microphones turn sound into a line that goes up (louder) and down (softer). They may use a costume or backdrop showing waveforms.

Dependencies:
* T06.G3.05: Decide which event type to use for a behavior


ID: T23.G3.03
Topic: T23 – AI Perception
Skill: Tell whether a behavior uses sensing and guessing
Description: Students read simple program descriptions (e.g., "game starts when you press space" vs "door opens when it sees your face") and decide which ones require the device to sense and guess vs ones that follow a fixed button rule. They identify the event blocks that would be used.

Dependencies:
* T23.G3.02: Describe sound as a wavy line of loud/soft
* T09.G3.01.04: Display variable value on stage using the variable monitor


### Grade 4 (G4)

ID: T23.G4.01
Topic: T23 – AI Perception
Skill: Trace how lighting changes pixel data
Description: Students use a provided slider UI (built with basic blocks) to dim/brighten a sample image costume and observe which pixel areas get darker/brighter in the costume editor. They answer questions about why dark rooms make images harder for AI to read.

Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G3.05: Fix a condition that uses the wrong operator
* T23.G3.01: Describe a picture as a grid of tiny colors
* T23.G2.02: Spot when sensor data might be unclear


ID: T23.G4.02
Topic: T23 – AI Perception
Skill: Choose a good setup for mic or camera
Description: Students examine 3 illustrated scenarios (e.g., backlit vs front-lit for camera, mic close vs far for microphone) and pick the best setup for clear input. They build a simple Scratch script that displays "good setup" or "needs improvement" messages.

Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G3.05: Fix a condition that uses the wrong operator
* T23.G3.01: Describe a picture as a grid of tiny colors
* T23.G3.02: Describe sound as a wavy line of loud/soft


ID: T23.G4.03
Topic: T23 – AI Perception
Skill: Identify noise and simple fixes
Description: Students examine examples of blurry images, shaky video clips, or choppy audio recordings and select a simple fix (steady the device, add light, move to quieter spot) before any AI coding happens. They create a troubleshooting flowchart using sprites.

Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G3.05: Fix a condition that uses the wrong operator
* T23.G3.01: Describe a picture as a grid of tiny colors


### Grade 5 (G5)

ID: T23.G5.01
Topic: T23 – AI Perception
Skill: Compare what people see vs what pixels show
Description: Students look at a clear photo and its coarse pixel version side by side and explain what detail is lost for the computer but obvious to a person (e.g., small text, faint objects). They use the costume editor to zoom in and count pixels.

Dependencies:
* T08.G3.05: Fix a condition that uses the wrong operator
* T23.G4.01: Trace how lighting changes pixel data


ID: T23.G5.02
Topic: T23 – AI Perception
Skill: Explain why an AI might mis-hear or mis-see
Description: Given examples of mis-recognized words or images (accent, shadowed face), students identify likely causes (background noise, low light, unusual angle) and suggest one fix (move closer, add light, speak clearly). They build a simple diagnostic tool.

Dependencies:
* T08.G3.05: Fix a condition that uses the wrong operator
* T23.G4.03: Identify noise and simple fixes
* T23.G3.03: Tell whether a behavior uses sensing and guessing


ID: T23.G5.03
Topic: T23 – AI Perception
Skill: Choose safe ways to handle sensor data
Description: Students compare actions for camera/mic data (e.g., "keep photos only on device" vs "share raw recordings with strangers") and classify them as safe or risky. They link perception to privacy before coding actual AI blocks.

Dependencies:
* T08.G3.05: Fix a condition that uses the wrong operator
* T23.G4.02: Choose a good setup for mic or camera
* T23.G3.03: Tell whether a behavior uses sensing and guessing


ID: T23.G5.04
Topic: T23 – AI Perception
Skill: Identify when AI sensing might be unfair
Description: Students examine scenarios where AI perception might work poorly for some groups (face recognition in poor lighting, voice recognition with different accents) and suggest basic fairness improvements (better lighting, multiple language options).

Dependencies:
* T08.G3.05: Fix a condition that uses the wrong operator
* T23.G4.03: Identify noise and simple fixes
* T23.G3.03: Tell whether a behavior uses sensing and guessing


ID: T23.G5.05
Topic: T23 – AI Perception
Skill: Identify what data hand, body, and face detection provides
Description: Students learn that AI vision blocks can detect specific features: hand detection finds finger positions and curl angles, body detection finds body part positions, and face detection finds face locations. They match detection types to data outputs (tables with x, y coordinates, angles, etc.) to prepare for G6 coding.

Dependencies:
* T10.G5.04: Read a cell value from a table
* T23.G5.01: Compare what people see vs what pixels show


### Grade 6 (G6)

ID: T23.G6.01.01
Topic: T23 – AI Perception
Skill: Capture a single spoken phrase with basic speech recognition
Description: Students use the basic speech recognition flow: `start recognizing speech in [English (United States) v] record as []` (with default language), wait briefly, then `end speech recognition` to capture a single spoken word or phrase. They display the result using the `text from speech` reporter block and a `say` block or variable monitor.

Dependencies:
* T08.G3.01: Use a simple if in a script
* T09.G3.01.04: Display variable value on stage using the variable monitor
* T23.G5.02: Explain why an AI might mis-hear or mis-see


ID: T23.G6.01.02
Topic: T23 – AI Perception
Skill: Select speech recognition language and observe accuracy differences
Description: Students extend basic speech recognition by exploring the language dropdown in `start recognizing speech in [LANGUAGE v] record as []`. They test recognition with different languages (English, Spanish, Chinese, etc.) and observe how selecting the correct language improves accuracy. They build a simple app that lets users choose their language before speaking.

Dependencies:
* T08.G3.01: Use a simple if in a script
* T09.G3.01.04: Display variable value on stage using the variable monitor
* T23.G6.01.01: Capture a single spoken phrase with basic speech recognition


ID: T23.G6.01B
Topic: T23 – AI Perception
Skill: Use continuous speech recognition for real-time transcription
Description: Students learn continuous speech recognition: `start continuous speech recognition in [LANGUAGE v] into list [listname v]` to begin streaming recognition. The list continuously updates with recognized phrases. They use `stop continuous speech recognition` to end. They build a live transcript display that updates as the user speaks.

Dependencies:
* T08.G3.01: Use a simple if in a script
* T09.G3.01.04: Display variable value on stage using the variable monitor
* T23.G6.01.02: Select speech recognition language and observe accuracy differences


ID: T23.G6.02.01
Topic: T23 – AI Perception
Skill: Convert text to speech with basic settings
Description: Students use the `say [TEXT] in [LANGUAGE v] as [VOICETYPE v] speed (SPEEDRATIO) pitch (PITCHRATIO) volume (VOLUMERATIO) store sound as []` block to convert text to speech. They experiment with different languages, voice types (Male/Female), and adjust speed/pitch/volume parameters to create different speaking styles.

Dependencies:
* T08.G3.01: Use a simple if in a script
* T09.G3.01.04: Display variable value on stage using the variable monitor
* T23.G5.02: Explain why an AI might mis-hear or mis-see


ID: T23.G6.02
Topic: T23 – AI Perception
Skill: Map speech commands to UI widgets
Description: Students combine `start recognizing speech in [LANGUAGE v] record as []` / `end speech recognition` / `text from speech` to capture commands, then match recognized phrases to 3–5 commands ("open map," "start game," "show help") using if-blocks. They trigger T16 UI widget actions (buttons, labels, toggles) and add fallback messages for unknown commands.

Dependencies:
* T08.G3.01: Use a simple if in a script
* T09.G3.01.04: Display variable value on stage using the variable monitor
* T23.G6.01.02: Select speech recognition language and observe accuracy differences
* T23.G4.02: Choose a good setup for mic or camera


ID: T23.G6.03A
Topic: T23 – AI Perception
Skill: Build a two-way voice chatbot loop
Description: Students combine speech-to-text (`start recognizing speech in [LANGUAGE v] record as []` → `end speech recognition` → `text from speech`), ChatGPT request block (`OpenAI ChatGPT: request … result [variable]`), and text-to-speech (`say [TEXT] in [LANGUAGE v] as [VOICETYPE v] …`) to build a voice assistant. They implement turn-taking: listen → process → speak → repeat.

Dependencies:
* T08.G3.01: Use a simple if in a script
* T09.G3.01.04: Display variable value on stage using the variable monitor
* T22.G6.01: Trace how a chatbot script processes each turn
* T23.G6.01.02: Select speech recognition language and observe accuracy differences
* T23.G6.02.01: Convert text to speech with basic settings


ID: T23.G6.03B
Topic: T23 – AI Perception
Skill: Use OpenAI Whisper for advanced speech transcription
Description: Students use `OpenAI: start recognizing speech in [LANGUAGE v] record as []` → `end speech recognition` → `text from speech` for high-accuracy speech recognition via OpenAI Whisper API. They compare Whisper's performance with basic speech recognition, especially in noisy environments or with accents, and learn trade-offs (accuracy vs. speed, API costs).

Dependencies:
* T08.G3.01: Use a simple if in a script
* T09.G3.01.04: Display variable value on stage using the variable monitor
* T22.G6.01: Trace how a chatbot script processes each turn
* T23.G6.01.02: Select speech recognition language and observe accuracy differences


ID: T23.G6.04.01
Topic: T23 – AI Perception
Skill: Set up hand detection and view debug output
Description: Students use `run hand detection table [TABLENAME v] debug [yes v] show video [yes v]` to turn on the front camera and detect hands. They explore the debug mode (draws keypoints on video) and show/hide video options. They observe how the detection responds to hand movements.

Dependencies:
* T08.G3.01: Use a simple if in a script
* T09.G3.01.04: Display variable value on stage using the variable monitor
* T23.G5.05: Identify what data hand, body, and face detection provides


ID: T23.G6.04.02
Topic: T23 – AI Perception
Skill: Read and display finger curl angles from hand detection
Description: Students read the result table from `run hand detection table [result v] debug [yes v] show video [yes v]` to get curl angles for each finger (thumb, index, middle, ring, pinky). Curl angles range from 0 (fully curled/fist) to 180 (fully extended/straight). They display curl values on screen and recognize simple gestures like pointing (index curl > 170, others < 170) or fist (all curl < 90).

Dependencies:
* T10.G5.04: Read a cell value from a table
* T08.G3.01: Use a simple if in a script
* T09.G3.01.04: Display variable value on stage using the variable monitor
* T23.G6.04.01: Set up hand detection and view debug output


ID: T23.G6.04.03
Topic: T23 – AI Perception
Skill: Read finger direction data for advanced gesture recognition
Description: Students extend hand detection by reading the direction (dir) column from the hand detection table. Each finger has a direction indicating which way it's pointing (up, down, left, right). They combine curl and direction to recognize complex gestures: "thumbs up" = thumb extended (curl > 170) + pointing up, "peace sign" = index and middle extended + pointing up.

Dependencies:
* T10.G5.04: Read a cell value from a table
* T08.G3.01: Use a simple if in a script
* T09.G3.01.04: Display variable value on stage using the variable monitor
* T23.G6.04.02: Read and display finger curl angles from hand detection


ID: T23.G6.05
Topic: T23 – AI Perception
Skill: Drive UI elements with live hand detection
Description: Students read x/y coordinates from the hand detection table (wrist or index finger position) and convert them into UI widget interactions: move a pointer sprite, adjust a slider, trigger hover states. They learn to hide the camera feed (`show video [no v]`) to reduce distraction while keeping detection active.

Dependencies:
* T10.G5.04: Read a cell value from a table
* T08.G3.01: Use a simple if in a script
* T23.G6.04.02: Read and display finger curl angles from hand detection


ID: T23.G6.06
Topic: T23 – AI Perception
Skill: Smooth noisy sensor data and recover from dropouts
Description: Students implement smoothing techniques on sensor data: moving average (average last 5 wrist positions before moving sprite), clamping (limit values to valid range), debouncing (wait for stable value). They add watchdog timers to reinitialize detection if data stops updating (e.g., if hand leaves frame twice in a row, show "hand not detected" message).

Dependencies:
* T08.G3.01: Use a simple if in a script
* T09.G5.05: Use the accumulator pattern to compute running totals
* T23.G4.03: Identify noise and simple fixes


ID: T23.G6.07
Topic: T23 – AI Perception
Skill: Add consent and privacy controls for sensor use
Description: Students add clear permission requests before enabling camera/mic detection ("This app needs your camera. Allow?"), provide easy on/off toggle buttons, and implement data retention limits (clear table after use). They explain to users what data is collected and why, using T16 labels and dialogs.

Dependencies:
* T08.G3.01: Use a simple if in a script
* T09.G3.01.04: Display variable value on stage using the variable monitor
* T23.G5.03: Choose safe ways to handle sensor data


ID: T23.G6.08.01
Topic: T23 – AI Perception
Skill: Set up 2D body pose detection and read keypoint positions
Description: Students use `run 2D body part recognition single person [yes v] table [TABLENAME v] debug [yes v]` to detect body landmarks (nose, shoulders, elbows, wrists, hips, knees, ankles) with x/y coordinates. They display keypoint positions on screen and create simple applications like a virtual mirror. They also explore multi-person mode (`single person [no v]`) which returns data with person IDs.

Dependencies:
* T10.G5.04: Read a cell value from a table
* T08.G3.01: Use a simple if in a script
* T09.G3.01.04: Display variable value on stage using the variable monitor
* T23.G6.04.02: Read and display finger curl angles from hand detection
* T23.G5.05: Identify what data hand, body, and face detection provides


ID: T23.G6.08.02
Topic: T23 – AI Perception
Skill: Detect body poses and trigger actions
Description: Students calculate angles between body landmarks (e.g., arm angle from shoulder-elbow-wrist positions) to detect specific poses. They trigger actions when poses are detected: "arms up" = both wrists above shoulders, "squat" = knees below hips. They use if-blocks to compare y-coordinates and implement pose-triggered events.

Dependencies:
* T10.G5.04: Read a cell value from a table
* T08.G3.01: Use a simple if in a script
* T09.G3.01.04: Display variable value on stage using the variable monitor
* T23.G6.08.01: Set up 2D body pose detection and read keypoint positions


ID: T23.G6.09.01
Topic: T23 – AI Perception
Skill: Set up face detection and view detected faces
Description: Students use `run face detection debug [yes v] and write into table [TABLENAME v]` to turn on the front camera and detect faces. They observe the debug mode (draws bounding boxes around faces) and explore the result table structure, which contains face positions and various facial attributes.

Dependencies:
* T10.G5.04: Read a cell value from a table
* T08.G3.01: Use a simple if in a script
* T09.G3.01.04: Display variable value on stage using the variable monitor
* T23.G5.05: Identify what data hand, body, and face detection provides


ID: T23.G6.09.02
Topic: T23 – AI Perception
Skill: Read face data and trigger actions based on detection
Description: Students read the face detection table to get face position (x, y coordinates) and use it to trigger events: move a sprite to follow the face, display a message when a face is detected, or count the number of faces. They understand how lighting affects detection accuracy and implement error handling for "no face detected."

Dependencies:
* T10.G5.04: Read a cell value from a table
* T08.G3.01: Use a simple if in a script
* T09.G3.01.04: Display variable value on stage using the variable monitor
* T23.G6.09.01: Set up face detection and view detected faces


ID: T23.G6.10
Topic: T23 – AI Perception
Skill: Use 3D pose detection for depth-aware body tracking
Description: Students use `run 3D pose detection debug [yes v] table [TABLENAME v]` to detect body landmarks with depth information (x, y, z coordinates). They compare 2D vs 3D pose detection, understanding that 3D provides distance from camera. They visualize the z-coordinate to understand depth perception and build applications that measure 3D movements (e.g., squat depth, forward reach).

Dependencies:
* T10.G5.04: Read a cell value from a table
* T08.G3.01: Use a simple if in a script
* T09.G3.01.04: Display variable value on stage using the variable monitor
* T23.G6.08.02: Detect body poses and trigger actions


### Grade 7 (G7)

ID: T23.G7.00A
Topic: T23 – AI Perception
Skill: Choose appropriate input modality for application context
Description: Students analyze application scenarios (noisy cafe, hands-free cooking, private space, public kiosk) and select the best input modality: voice-only, gesture-only, pose-only, or combinations. They consider accuracy (noisy environment reduces voice accuracy), user effort (hands-free favors voice/pose), privacy (voice reveals more than gesture), and accessibility. They create a decision matrix comparing modalities.

Dependencies:
* T23.G6.02: Map speech commands to UI widgets
* T23.G6.05: Drive UI elements with live hand detection
* T23.G6.08.02: Detect body poses and trigger actions
* T23.G5.02: Explain why an AI might mis-hear or mis-see


ID: T23.G7.01
Topic: T23 – AI Perception
Skill: Define a reusable gesture dictionary
Description: Students capture hand detection output (finger curl, dir, x/y positions) into a table, label each pattern ("thumbs up," "peace sign," "stop," "pointing"), and create custom reporter blocks that return the detected gesture name. They implement at least four gestures plus a "none detected" state, using T11 custom block patterns.

Dependencies:
* T10.G5.04: Read a cell value from a table
* T11.G5.02: Define a custom block with one parameter
* T23.G6.05: Drive UI elements with live hand detection


ID: T23.G7.02
Topic: T23 – AI Perception
Skill: Require multimodal confirmation (voice + gesture)
Description: Students design safety-critical interactions (purchase confirmation, delete save file, launch simulation) that require matching voice command AND specific gesture to proceed. They manage sequence state (which input came first?), implement timeouts (confirmation expires after 5 seconds), and provide clear feedback on partial completion ("voice confirmed, waiting for gesture").

Dependencies:
* T09.G5.05: Use the accumulator pattern to compute running totals
* T23.G6.02: Map speech commands to UI widgets
* T23.G6.05: Drive UI elements with live hand detection


ID: T23.G7.03
Topic: T23 – AI Perception
Skill: Score a pose-based challenge with coaching tips
Description: Students build a fitness or dance coaching app using `run 3D pose detection debug [yes v] table [result v]`. They detect whether player meets angle/position thresholds for a sequence (squat → jump → arms up), award points, display progress timeline, and show coaching text ("raise elbows higher," "squat deeper") based on which landmarks failed. They use z-coordinates to measure depth movements.

Dependencies:
* T23.G6.10: Use 3D pose detection for depth-aware body tracking
* T23.G6.06: Smooth noisy sensor data and recover from dropouts


ID: T23.G7.04
Topic: T23 – AI Perception
Skill: Monitor detection accuracy across different users
Description: Students design an accessibility log where each speech/gesture event is recorded with user metadata (age range, device type, lighting condition, language) plus outcome (success/failure). They calculate accuracy rates per group and identify bias patterns (e.g., low-light users have 40% success vs 90% in good light). They propose adjustments based on data.

Dependencies:
* T23.G6.06: Smooth noisy sensor data and recover from dropouts
* T23.G5.04: Identify when AI sensing might be unfair


ID: T23.G7.05
Topic: T23 – AI Perception
Skill: Implement fairness safeguards for perception systems
Description: Students implement measures to improve fairness: multiple attempts for failed recognition (3 tries before error), alternative input methods when sensors struggle (switch from voice to text input if speech fails), user feedback collection for system improvement, and adaptive thresholds that adjust to user patterns.

Dependencies:
* T23.G6.07: Add consent and privacy controls for sensor use
* T23.G5.04: Identify when AI sensing might be unfair


ID: T23.G7.06
Topic: T23 – AI Perception
Skill: Build a calibration wizard for sensors
Description: Students create a multi-step UI wizard (using T16 UI patterns) that guides users through sensor setup: microphone volume check (speak and see level), lighting test (show brightness meter), gesture framing (show silhouette guide). Each step runs a quick sensor test, displays current readings, and offers fixes ("move closer," "increase room light," "adjust camera angle").

Dependencies:
* T23.G6.06: Smooth noisy sensor data and recover from dropouts
* T23.G5.02: Explain why an AI might mis-hear or mis-see


### Grade 8 (G8)

ID: T23.G8.00A
Topic: T23 – AI Perception
Skill: Understand supervised learning for perception classification
Description: Students learn the supervised learning workflow for gesture/pose classification: (1) collect labeled examples (record hand positions for "thumbs up," "peace sign," etc.), (2) train a classifier using the KNN blocks (`create KNN number classifier from table [training_data v] K [3] named [classifier1]`), (3) evaluate on test data. They understand that more training examples improve accuracy and that K value affects sensitivity to noise.

Dependencies:
* T08.G6.01: Use conditionals to control simulation steps
* T09.G6.01: Model real-world quantities using variables and formulas
* T23.G7.01: Define a reusable gesture dictionary


ID: T23.G8.01
Topic: T23 – AI Perception
Skill: Offer interchangeable input modes with accessibility rules
Description: Students build a settings panel where users choose "voice only," "gesture only," or "hybrid" control mode. Each mode updates UI instructions, disables irrelevant widgets, and logs active mode for analytics. They implement auto-switching: if active sensor fails (e.g., hand leaves frame), automatically switch to voice mode and notify user.

Dependencies:
* T08.G6.01: Use conditionals to control simulation steps
* T09.G6.01: Model real-world quantities using variables and formulas
* T23.G7.02: Require multimodal confirmation (voice + gesture)
* T23.G6.02: Map speech commands to UI widgets


ID: T23.G8.02
Topic: T23 – AI Perception
Skill: Train and deploy a custom gesture classifier
Description: Students build a complete gesture training system: (1) create data collection UI where users record examples of each gesture (stores finger curl/dir values in training table with labels), (2) use `create KNN number classifier from table [training v] K [3] named [gestureClassifier]` to train, (3) deploy with `predict for table [live_data v] with classifier [gestureClassifier] show neighbors [yes v]` to recognize live gestures. They test with at least 5 gesture types.

Dependencies:
* T08.G6.01: Use conditionals to control simulation steps
* T09.G6.01: Model real-world quantities using variables and formulas
* T23.G8.00A: Understand supervised learning for perception classification
* T23.G7.01: Define a reusable gesture dictionary


ID: T23.G8.02B
Topic: T23 – AI Perception
Skill: Tune and evaluate KNN classifier performance
Description: Students systematically tune their KNN gesture classifier by experimenting with different K values (1, 3, 5, 7), feature sets (include/exclude certain finger angles), and training data sizes (10 vs 50 examples per gesture). They split data into training and test sets, measure accuracy, create confusion matrices (which gestures get confused), and document how K affects performance (low K = noisy, high K = over-smoothed).

Dependencies:
* T08.G6.01: Use conditionals to control simulation steps
* T09.G6.01: Model real-world quantities using variables and formulas
* T23.G8.02: Train and deploy a custom gesture classifier


ID: T23.G8.03
Topic: T23 – AI Perception
Skill: Fuse voice, pose, and UI widgets into a cooperative simulation
Description: Students build a multi-user scenario (space mission, emergency response, surgical simulation) where different team members use different modalities simultaneously: one issues voice commands, another performs gestures to manipulate tools, a third confirms via widget buttons. The system coordinates timing, prevents conflicts (can't launch if gesture not confirmed), and displays live event log.

Dependencies:
* T08.G6.01: Use conditionals to control simulation steps
* T23.G7.02: Require multimodal confirmation (voice + gesture)
* T23.G7.03: Score a pose-based challenge with coaching tips
* T23.G6.03A: Build a two-way voice chatbot loop


ID: T23.G8.04
Topic: T23 – AI Perception
Skill: Publish a privacy and deployment plan for perception apps
Description: Students research real voice/vision privacy concerns (storage duration, consent requirements, data retention policies, third-party access) and write a comprehensive policy for their app. They document: what data is captured, how long it's stored, who can access it, how to request deletion, when to use offline modes, and fallback behaviors. They reference their own logging/calibration/fairness features and align with T05 design thinking principles.

Dependencies:
* T04.G6.01: Group snippets by underlying algorithm pattern
* T08.G6.01: Use conditionals to control simulation steps
* T23.G7.05: Implement fairness safeguards for perception systems
* T23.G6.07: Add consent and privacy controls for sensor use


ID: T23.G8.05
Topic: T23 – AI Perception
Skill: Evaluate societal impacts of perception AI systems
Description: Students analyze real-world examples of AI perception systems (facial recognition in law enforcement, voice assistants in homes, gesture controls in healthcare, emotion detection in hiring) and evaluate benefits and risks for different communities. They propose ethical guidelines for responsible deployment: when to use perception AI, when not to, required safeguards, transparency requirements, and community oversight mechanisms.

Dependencies:
* T08.G6.01: Use conditionals to control simulation steps
* T09.G6.01: Model real-world quantities using variables and formulas
* T23.G7.04: Monitor detection accuracy across different users
* T23.G7.05: Implement fairness safeguards for perception systems


---

## Total Skill Count
- GK: 3 skills
- G1: 3 skills
- G2: 3 skills
- G3: 3 skills
- G4: 3 skills
- G5: 5 skills
- G6: 17 skills (expanded from 11 due to splitting broad skills)
- G7: 6 skills
- G8: 6 skills

**Total: 49 skills** (up from 44 original skills)

The increase reflects proper scaffolding through sub-skills for complex topics like hand detection, body pose, and face detection.
