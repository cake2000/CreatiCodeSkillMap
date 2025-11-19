# T23 – AI Perception: G6–8 Skill List (Draft v2)

Topic reference: `T23 AI Perception` in `domains_topics_overview.md`
Domain: CreatiCode-specific AI (Voice/Vision/Gesture) · CSTA focus: MS-PRO-PF, MS-PRO-DH, MS-PRO-TR, MS-CAS-ET (links to MS-ALG-HD, MS-DAA-DF)

Each skill below has:

- a stable **ID** (`T23.G<grade>.<nn>`),
- an IXL-style **short name**,
- a **description** (what understanding/behavior it targets),
- a **challenge format** (the typical problem type to assess it).

Where relevant, a primary **CSTA code** is noted.

**Role and scope in v3:** AI Perception focuses on *applied* voice, vision, and gesture pipelines using the CreatiCode AI blocks in `scratch3_ai.js`. Grades 6–8 already know how to architect multi-screen interfaces (T16) and reason about prompting (T22); here they build reliable speech interfaces, pose-controlled gameplay, calibration dashboards, sensor-fusion logic, and equity checks. Theory about how the models work internally is handled elsewhere—T23 is “IXL for shipping microphone/camera features with polish and safeguards.”

---

## Grade 6

Grade 6 students master the core building blocks: mapping speech to UI intents, building first-pass voice conversations, reading AI detection tables, and smoothing noisy input so their apps remain usable.

### T23.G6.01 – Map speech commands to UI widgets

- **Short name:** Voice remote for your app
- **Description:** Students run `start recognizing speech` / `text from speech`, match the recognized phrase to 3–5 commands ("open map," "start game," "show help"), and trigger matching T16 widgets (e.g., calling `set value` on buttons or toggles). They design both the command list and the fallback text if the phrase is unknown.
- **Challenge format:** Coding, guided build. Prompt: “Add a voice remote to your multi-screen project.” Students must (1) start/stop speech recognition correctly, (2) normalize the resulting text (lowercase, trim), (3) route each phrase to a widget action, and (4) update a status label with the understood command or “I didn’t hear that.” Auto-grading injects sample transcripts and checks that the right widget fires and unknown phrases trigger the fallback.
- **CSTA:** MS-PRO-PF-02, MS-ALG-HD-03.

### T23.G6.02 – Build a two-way voice chatbot loop

- **Short name:** Listen, ask ChatGPT, speak back
- **Description:** Students combine speech-to-text, `OpenAI ChatGPT: request … result [variable]`, and the AI Speaker block (`say [TEXT] in [LANGUAGE] as [VOICE] …`) to build a basic voice assistant. They tune `mode`, `temperature`, and `max tokens` for kid-friendly answers and show the transcript on screen.
- **Challenge format:** Coding, conversational project. Starter UI includes microphone + “Stop” buttons. Students wire: microphone on/off, ChatGPT prompt template (with safety instructions), text-to-speech playback, and chat log widgets. Auto-grading feeds scripted voice inputs and verifies: (1) speech is captured before the ChatGPT call, (2) ChatGPT runs in `waiting` mode to prevent overlap, (3) the reply is spoken with AI Speaker, and (4) the transcript panel shows alternating user/bot entries.
- **CSTA:** MS-PRO-PF-02, MS-PRO-TR-11.

### T23.G6.03 – Drive UI elements with live hand detection

- **Short name:** Hand-controlled cursor or slider
- **Description:** Using `run hand detection table [TABLENAME] debug [ ] show video [ ]`, students read the `x/y` columns for the wrist or index finger and convert them into widget interactions (e.g., move a pointer sprite, adjust a slider, trigger hover states). They must also hide the camera feed when not needed to reduce distraction.
- **Challenge format:** Coding, interaction build. Prompt: “Create a hand-tracking volume knob.” Students (1) start/stop hand detection via buttons, (2) read from the result table safely (handling empty rows), (3) map positions to a numeric range, and (4) update both a visible widget (slider/label) and a functional variable (e.g., actual volume). Auto-grading simulates detection table values and checks correct mapping plus safe handling when no hand is found.
- **CSTA:** MS-PRO-DH-04, MS-PRO-PF-02.

### T23.G6.04 – Smooth noisy sensor data and recover from dropouts

- **Short name:** Make perception input stable
- **Description:** Students implement smoothing (moving average, clamp, debounce) on speech or vision signals and add watchdog timers to reinitialize detection if the camera/mic feed drops. Example: average the last 5 wrist positions before moving a sprite; if `text from speech` is empty twice in a row, prompt the user to retry.
- **Challenge format:** Coding + debugging. Starter project intentionally injects noisy hand positions and random empty speech strings. Students add helper lists/variables, smoothing loops, and timeout logic. Auto-grading runs a noisy script and checks that (1) the UI responds with dampened motion, (2) detection restarts or shows a “Please retry” prompt after timeouts, and (3) no crashes occur when data is missing.
- **CSTA:** MS-PRO-TR-12.

---

## Grade 7

Grade 7 students orchestrate multi-modal experiences: defining gesture dictionaries, combining speech + pose for complex commands, logging accuracy/fairness, and running pose-controlled scoring loops.

### T23.G7.01 – Define a reusable gesture dictionary

- **Short name:** Store finger curls/dirs as named gestures
- **Description:** Students capture hand detection output (finger `curl` + `dir`, keypoint positions) into a table, label each pattern (“thumbs up,” “peace sign,” “stop”), and create helper blocks that return the detected gesture name. They prove the system handles at least four gestures plus a “none detected” state.
- **Challenge format:** Coding, data-structure build. Learners implement a calibration screen where users hold each gesture for two seconds; the app stores averaged values per gesture. During gameplay a loop compares live values to the stored template (tolerance thresholds). Auto-grading feeds synthetic table rows with known gestures and checks that the dictionary lookup returns the correct label or fallback.
- **CSTA:** MS-PRO-DH-04, MS-PRO-PD-08.

### T23.G7.02 – Require multimodal confirmation (voice + gesture)

- **Short name:** Combine “say it + show it” for critical actions
- **Description:** Students design safety-critical flows (purchases, deleting saves, launching rockets) that require a matching voice command *and* a specific gesture or pose to proceed. They manage the sequence state (voice heard first? gesture first?) and timeouts so the confirmation expires if not completed promptly.
- **Challenge format:** Coding, UX workflow. Starter UI has confirm/cancel widgets. Students implement a finite state machine (variables for current step, timer) and integrate speech + gesture events. Auto-grading replays sequences (voice-only, gesture-only, mismatched order) and verifies that only the full, ordered combo triggers the action and failure cases reset the UI politely.
- **CSTA:** MS-PRO-PF-02, MS-ALG-HD-04.

### T23.G7.03 – Score a pose-based challenge with coaching tips

- **Short name:** Build a pose workout judge
- **Description:** Using `run 3D pose detection … table [result]`, students detect whether a player meets angle/position thresholds for a sequence (e.g., squat → jump → pose). They award points, display a progress timeline, and surface text tips ("raise elbows higher") based on which landmarks failed the check.
- **Challenge format:** Coding, interactive challenge. Provided: table-reading helpers and sample target ranges. Students add loops that compare live data to targets, maintain streak counters, and call out corrections in real time. Auto-grading feeds pose data for success/failure cases to ensure scoring and feedback logic behave as intended.
- **CSTA:** MS-PRO-PF-02, MS-ALG-HD-03.

### T23.G7.04 – Monitor detection accuracy across different users

- **Short name:** Log who the system works for
- **Description:** Students design an accessibility log: each time a speech/gesture event succeeds or fails, they store user metadata (age range, device, lighting) plus outcome, then calculate accuracy rates per group. They interpret the data to spot bias (e.g., low-light users have lower success) and propose adjustments.
- **Challenge format:** Coding + data analysis. Starter template includes a table and logging helper. Students add UI inputs for metadata, log rows with timestamps, and implement summary reporters (success %, failure notes). Auto-grading replays scripted sessions to ensure logs capture the metadata and summary labels update correctly; rubric scoring checks that reflections mention at least one disparity and concrete mitigation.
- **CSTA:** MS-CAS-ET-05, MS-DAA-DF-03.

### T23.G7.05 – Build a calibration wizard for sensors

- **Short name:** Help users tune the camera/mic setup
- **Description:** Students create a multi-step UI wizard (using T16 patterns) that walks users through microphone checks, lighting tests, and gesture framing. Each step runs a quick sensor test, shows the current readings, and offers fixes ("move closer," "increase room light").
- **Challenge format:** Coding, multi-screen flow. Students implement per-step widgets, store pass/fail flags, and lock access to the main app until calibration succeeds. Auto-grading walks through the wizard, intentionally failing steps to ensure messages display and the main app remains locked until all checks pass.
- **CSTA:** MS-PRO-PM-03, MS-PRO-PF-02.

---

## Grade 8

Grade 8 students treat AI perception as production infrastructure: they support multiple input modes, train custom classifiers, fuse modalities into rich simulations, and formalize privacy/ethics policies.

### T23.G8.01 – Offer interchangeable input modes with accessibility rules

- **Short name:** Build a voice/gesture accessibility layer
- **Description:** Students add a settings panel where users can choose “voice only,” “gesture only,” or “hybrid” control. Each mode automatically updates instructions, disables irrelevant widgets, and logs which mode is active for analytics. They also implement auto-switching if the active sensor fails.
- **Challenge format:** Coding, systems integration. Learners create a settings widget group, state variables, and mode-specific event handlers. Auto-grading toggles modes and injects sensor failures to verify that the UI updates, disabled inputs no longer fire, and the system switches to a safe fallback when needed.
- **CSTA:** MS-PRO-PF-02, MS-CAS-ET-06.

### T23.G8.02 – Train and deploy a custom gesture classifier

- **Short name:** Collect, train, and run your own model
- **Description:** Students record labeled gesture samples into a table, use `create KNN number classifier from table … named [NAME]`, and then call `predict for table … with classifier [NAME]` in real time to classify new gestures. They compare performance with manual thresholds and document tuning decisions (K value, feature set).
- **Challenge format:** Coding + data science. Starter project includes buttons to record training samples. Students finish the pipeline: feature extraction, training invocation, prediction loop, accuracy tracker. Auto-grading feeds held-out samples to ensure predictions write to the table and that misclassifications trigger the student’s “retrain/tune” workflow.
- **CSTA:** MS-DAA-DF-03, MS-PRO-TR-12.

### T23.G8.03 – Fuse voice, pose, and UI widgets into a cooperative simulation

- **Short name:** Run a multi-modal control room
- **Description:** Students build a scenario (e.g., space mission, emergency drill) where different team members use different modalities simultaneously: one issues spoken commands, another performs gestures to manipulate tools, and an operator confirms via widgets. The system must coordinate timing, prevent conflicts, and surface a live log of events.
- **Challenge format:** Coding, complex simulation. Learners implement event queues, timestamps, and arbitration rules (e.g., gesture override voice only if within 2 seconds). Auto-grading replays scripted multi-user sequences to check that events are ordered, logs capture source + modality, and conflict rules behave as documented.
- **CSTA:** MS-PRO-PD-08, MS-ALG-HD-04.

### T23.G8.04 – Publish a privacy and deployment plan for perception apps

- **Short name:** Document how you protect sensor data
- **Description:** Students research real voice/vision privacy concerns (storage, consent, retention) and write a policy for their app: what data is captured, how long it stays, who sees it, how to request deletion, and when to fall back to offline modes. They tie recommendations to their own logging/calibration features.
- **Challenge format:** Concept, policy memo + presentation. Learners submit a 1–2 page policy plus a short video/slide pitch referencing evidence from their telemetry (e.g., “hand detection logs 50 samples/minute; we purge after 24 hours”). Rubric-based auto-grading checks coverage of consent, storage, transparency, and alignment with AI4K12 priorities on responsible AI.
- **CSTA:** MS-CAS-HC-02, MS-CAS-ET-06.

---
