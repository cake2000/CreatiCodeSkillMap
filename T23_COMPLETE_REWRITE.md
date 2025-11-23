# T23 - AI Perception (Complete Rewrite)
# Ready to replace lines 13579-14167 in allskills.md
# Incorporates ALL fixes from T23_COMPREHENSIVE_ISSUES_ANALYSIS.md

ID: T23.GK.01
Topic: T23 – AI Perception
Skill: Match pictures of sensing
Description: Students drag friendly icons (eye, ear, hand) onto photos showing someone looking, listening, or pressing a big button, building the idea that helpers need different kinds of sensing. All activities use pictures and physical objects—no screens or blocks.




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
Description: Students learn that AI vision blocks can detect specific features: hand detection finds finger positions and curl angles, body detection finds body part positions, and face detection finds face locations. They sort picture cards showing different detection types (hand/body/face) to their data outputs (finger angles, body positions, face landmarks). They match detection types to data outputs (tables with x, y coordinates, angles, etc.) to prepare for G6 coding.

Dependencies:
* T10.G5.04: Read a cell value from a table
* T23.G5.01: Compare what people see vs what pixels show

ID: T23.G5.06
Topic: T23 – AI Perception
Skill: Understand perception API workflow patterns
Description: Students learn the common pattern for using perception APIs: (1) start detection with configuration, (2) read results from output table, (3) process data with conditionals, (4) stop detection. They examine annotated code examples for hand, speech, and body detection showing this pattern. They match API blocks to workflow steps (start→read→process→stop) using diagrams. Picture-based workflow analysis, no coding yet.

Dependencies:
* T23.G5.05: Identify what data hand, body, and face detection provides

Grade: 5

ID: T23.G6.01.01
Topic: T23 – AI Perception
Skill: Capture a single spoken phrase with basic speech recognition
Description: Students use the basic speech recognition flow: `start recognizing speech in [English (United States) v] record as []` (with default language), wait briefly, then `end speech recognition` to capture a single spoken word or phrase. The recognized text is stored in a variable (not in a table). They display the result using the `text from speech` reporter block and a `say` block or variable monitor. Common issues include silent rooms (no input detected), background noise (mis-recognition), and recognition delay (typically 1-3 seconds after speaking stops).

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
Description: Students use the `say [TEXT] in [LANGUAGE v] as [VOICETYPE v] speed (SPEEDRATIO) pitch (PITCHRATIO) volume (VOLUMERATIO) store sound as []` block to convert text to speech. They experiment with different languages, voice types (Male/Female), and adjust speed/pitch/volume parameters (default 100, range 50-200) to create different speaking styles.

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
* T23.G6.02.01: Convert text to speech with basic settings
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
Description: Students read the result table from `run hand detection table [result v] debug [yes v] show video [yes v]` to get hand detection data. The table contains 47 rows per detected hand with complete structure: the first 5 rows contain finger summaries (one row per finger: thumb, index, middle, ring, pinky) with columns [hand, part, curl, dir, x, y, z]; followed by 21 rows of 2D landmark positions; then 21 rows of 3D landmark positions. Curl angles range from 0° (fully curled/fist) to 180° (fully extended/straight). Direction (dir) ranges from 0° to 360° indicating pointing direction. X and Y are screen coordinates, Z is depth. They display curl values on screen and recognize simple gestures like pointing (index curl > 170, others < 170) or fist (all curl < 90).

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

ID: T23.G6.04.04
Topic: T23 – AI Perception
Skill: Recognize basic gestures from hand detection data
Description: Students use hand detection curl and direction data to identify 3-5 basic gestures: fist (all fingers curl < 90), open hand (all curl > 150), pointing (index curl > 170, others < 90), thumbs up (thumb curl > 170 and dir near 0°), peace sign (index and middle curl > 170, others < 90). They use if-blocks to check conditions and display gesture names. No UI integration yet, just gesture recognition logic.

Dependencies:
* T23.G6.04.03: Read finger direction data for advanced gesture recognition

Grade: 6

ID: T23.G6.05
Topic: T23 – AI Perception
Skill: Drive UI elements with live hand detection
Description: Students read x/y coordinates from the hand detection table (wrist or index finger position) and convert them into UI widget interactions: move a pointer sprite, adjust a slider, trigger hover states. They learn to hide the camera feed (`show video [no v]`) to reduce distraction while keeping detection active.

Dependencies:
* T10.G5.04: Read a cell value from a table
* T08.G3.01: Use a simple if in a script
* T23.G6.04.04: Recognize basic gestures from hand detection data

ID: T23.G6.06
Topic: T23 – AI Perception
Skill: Smooth noisy sensor data and recover from dropouts
Description: Students implement smoothing techniques on sensor data: moving average (average last 5 wrist positions before moving sprite), clamping (limit values to valid range), debouncing (wait for stable value). They add watchdog timers to reinitialize detection if data stops updating (e.g., if hand leaves frame twice in a row, show "hand not detected" message).

Dependencies:
* T08.G3.01: Use a simple if in a script
* T09.G5.05: Use the accumulator pattern to compute running totals
* T23.G6.04.02: Read and display finger curl angles from hand detection
* T23.G4.03: Identify noise and simple fixes

ID: T23.G6.06B
Topic: T23 – AI Perception
Skill: Choose continuous vs. event-driven detection patterns
Description: Students compare two detection patterns: (1) continuous polling in forever loop (constantly read table and update), (2) event-driven (start detection, wait for specific condition, then act). They implement both patterns with hand detection: continuous mode moves sprite smoothly following hand, event-driven mode triggers action when gesture detected. They discuss trade-offs: continuous is smooth but CPU-intensive, event-driven is efficient but may miss quick gestures.

Dependencies:
* T23.G6.04.04: Recognize basic gestures from hand detection data
* T23.G6.06: Smooth noisy sensor data and recover from dropouts

Grade: 6

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
Description: Students use `run 2D body part recognition single person [yes v] table [TABLENAME v] debug [yes v]` to detect body landmarks with x/y coordinates. The detection identifies all 17 keypoints: nose, left_eye, right_eye, left_ear, right_ear, left_shoulder, right_shoulder, left_elbow, right_elbow, left_wrist, right_wrist, left_hip, right_hip, left_knee, right_knee, left_ankle, right_ankle. The table also includes 4 limb measurements (left_arm, right_arm, left_leg, right_leg) with curl and dir values. Table columns are: id, part, x, y, curl, dir. They display keypoint positions on screen and create simple applications like a virtual mirror. Multi-person mode (`single person [no v]`) assigns each person a unique ID in the table.

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

ID: T23.G6.08.03
Topic: T23 – AI Perception
Skill: Use 3D pose detection for depth-aware body tracking
Description: Students use `run 3D pose detection debug [yes v] table [TABLENAME v]` to detect body landmarks with depth information (x, y, z coordinates). They compare 2D vs 3D pose detection, understanding that 3D provides distance from camera. They visualize the z-coordinate to understand depth perception and build applications that measure 3D movements (e.g., squat depth, forward reach).

Dependencies:
* T10.G5.04: Read a cell value from a table
* T08.G3.01: Use a simple if in a script
* T09.G3.01.04: Display variable value on stage using the variable monitor
* T23.G6.08.02: Detect body poses and trigger actions

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
Description: Students read the face detection table to get face position and attributes. The table contains 13 rows per detected face: 1 row for tilt angle, plus 12 rows for 6 facial landmark positions (left_eye, right_eye, nose, mouth, left_ear, right_ear, each with x and y coordinates). Table columns are: ID, variable, value. They use this data to trigger events: move a sprite to follow the face, display a message when a face is detected, or count the number of faces. They understand how lighting affects detection accuracy, note that face data can be noisy and may need smoothing, and implement error handling for "no face detected."

Dependencies:
* T10.G5.04: Read a cell value from a table
* T08.G3.01: Use a simple if in a script
* T09.G3.01.04: Display variable value on stage using the variable monitor
* T23.G6.09.01: Set up face detection and view detected faces

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
* T23.G6.04.04: Recognize basic gestures from hand detection data
* T23.G6.05: Drive UI elements with live hand detection

ID: T23.G7.01B
Topic: T23 – AI Perception
Skill: Combine inputs with simple OR logic
Description: Students build interactions where users can choose different input methods: "say 'next' OR perform swipe gesture" to advance, "press space bar OR raise hand" to start game. They use OR conditions to check multiple inputs and trigger the same action. They learn when OR logic is appropriate (giving users choices) vs. when specific input is required. Simpler than AND multimodal confirmation (G7.02).

Dependencies:
* T23.G7.01: Define a reusable gesture dictionary
* T23.G6.02: Map speech commands to UI widgets

Grade: 7

ID: T23.G7.02
Topic: T23 – AI Perception
Skill: Require multimodal confirmation (voice + gesture)
Description: Students design safety-critical interactions (purchase confirmation, delete save file, launch simulation) that require matching voice command AND specific gesture to proceed. They manage sequence state (which input came first?), implement timeouts (confirmation expires after 5 seconds), and provide clear feedback on partial completion ("voice confirmed, waiting for gesture").

Dependencies:
* T09.G5.05: Use the accumulator pattern to compute running totals
* T23.G7.01: Define a reusable gesture dictionary
* T23.G6.02: Map speech commands to UI widgets
* T23.G6.05: Drive UI elements with live hand detection

ID: T23.G7.03
Topic: T23 – AI Perception
Skill: Score a pose-based challenge with coaching tips
Description: Students build a fitness or dance coaching app using `run 3D pose detection debug [yes v] table [result v]`. They detect whether player meets angle/position thresholds for a sequence (squat → jump → arms up), award points, display progress timeline, and show coaching text ("raise elbows higher," "squat deeper") based on which landmarks failed. They use z-coordinates to measure depth movements.

Dependencies:
* T23.G6.08.03: Use 3D pose detection for depth-aware body tracking
* T23.G6.06: Smooth noisy sensor data and recover from dropouts

ID: T23.G7.04
Topic: T23 – AI Perception
Skill: Monitor detection accuracy across different users
Description: Students design an accessibility log where each speech/gesture event is recorded with user metadata (age range, device type, lighting condition, language) plus outcome (success/failure). They calculate accuracy rates per group (success rate = correct detections / total attempts) and identify significant disparities (>20% difference between groups), such as low-light users having 40% success vs 90% in good light. They propose adjustments based on data.

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

ID: T23.G7.06B
Topic: T23 – AI Perception
Skill: Optimize perception system performance
Description: Students identify and fix perception performance issues: reduce detection frame rate (process every 3rd frame instead of every frame), limit table size (clear old data), disable debug visualization in production, use efficient data structures (variables for single values instead of searching tables). They measure and compare performance before/after optimization using timer blocks. They understand trade-offs between accuracy and speed.

Dependencies:
* T23.G7.06: Build a calibration wizard for sensors
* T23.G6.06B: Choose continuous vs. event-driven detection patterns

Grade: 7

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

ID: T23.G8.01A
Topic: T23 – AI Perception
Skill: Practice KNN classification with simple numeric data
Description: Students practice KNN with a simple dataset before gesture classification: given a table of measurements (height, weight) and labels (category), they use `create KNN number classifier from table [training v] K [3] named [simple]` to train a classifier, then test it with new data using `predict for table [test v] with classifier [simple] show neighbors [yes v]`. They experiment with K values (1, 3, 5) and observe how it affects predictions. They understand KNN finds "similar" examples.

Dependencies:
* T23.G8.00A: Understand supervised learning for perception classification
* T10.G6.02: Sort a table by a column

Grade: 8

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

