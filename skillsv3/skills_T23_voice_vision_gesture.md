# T23 – AI Perception: K–8 Skill List (Draft v1)

Topic reference: `T23 AI Perception` in `domains_topics_overview.md`
Domain: CreatiCode-specific AI, coding-heavy · CSTA focus: PRO‑PF, DAA‑DP, CAS‑ET

Each skill below has:

- a stable **ID** (`T23.G<grade>.<nn>`),
- an IXL‑style **short name**,
- a **description** (what understanding/behavior it targets),
- a **challenge format** (the typical problem type to assess it).

Where relevant, a primary **CSTA code** is noted.

---

## Grade K (PreK–K)

Grades K focuses on introducing the idea of listening to voices, seeing the camera, and recognizing simple gestures as natural ways to interact with computers.

### T23.GK.01 – Recognize that computers can "hear" spoken words

- **Short name:** Computers listen to voices
- **Description:** Students explore that computers can use a microphone to receive spoken input, similar to how they listen to a teacher. They understand this as one way to talk to a computer (beyond typing or clicking).
- **Challenge format:** Concept, interactive demonstration. A CreatiCode project uses speech recognition to capture what the student says (e.g., "Say your favorite animal"). The system displays the recognized text or plays it back, showing that the computer "heard" them. Auto‑grading checks that the text from speech is not empty and matches (approximately) what was spoken.
- **CSTA:** E‑CAS‑ET‑02 (Emerging technologies can help people).

### T23.GK.02 – Recognize that computers can "see" with a camera

- **Short name:** Cameras let computers see
- **Description:** Students learn that a computer camera can detect their movements, hands, or body position in real time. They see that this is different from a still photograph—it's live motion sensing that can trigger actions.
- **Challenge format:** Concept, interactive demonstration. A CreatiCode project turns on the camera and displays live video or moves a sprite when the student moves (using simple video motion sensing). Auto‑grading checks that camera is enabled and motion changes the sprite position.
- **CSTA:** E‑CAS‑ET‑02.

### T23.GK.03 – Make a sprite respond to your voice

- **Short name:** Say a word, the sprite moves
- **Description:** Students link speech input to sprite behavior in the simplest way: when they say a word, a sprite does something (e.g., jumps, makes a sound, changes color). This is the first experience combining speech and action.
- **Challenge format:** Coding, guided project. Provided: a sprite, a speech recognition block starting, and an empty section. Students add an action block (e.g., move, play sound, change color) inside or after the speech block. Auto‑grading checks that (1) speech recognition is triggered, (2) an action follows, and (3) the sprite visibly responds after sound input.
- **CSTA:** E‑PRO‑PF‑02 (Create programs that include sequence), E‑CAS‑ET‑02.

### T23.GK.04 – Make a sprite follow your hand

- **Short name:** Hand controls the sprite
- **Description:** Students enable hand detection and use the position or presence of a hand to move a sprite on screen (e.g., the sprite follows where their hand is in the camera view, or moves when any hand is detected).
- **Challenge format:** Coding, guided project. Starter includes hand detection block and a sprite. Students add motion blocks to make the sprite move based on whether a hand is detected or where it is on the screen. Auto‑grading checks that (1) hand detection is active, (2) the sprite responds to hand position, and (3) the connection is clearly functional.
- **CSTA:** E‑CAS‑ET‑02.

---

## Grade 1

Grade 1 students learn to read and interpret simple voice/gesture inputs, building on K's exploratory experiences.

### T23.G1.01 – Recognize different spoken words

- **Short name:** Understand which word was said
- **Description:** Students capture speech and compare the recognized text to one or more target words (e.g., "Is the word 'yes' or 'no'?"). They understand that speech recognition produces text that can be checked or matched.
- **Challenge format:** Concept and coding, speech matching. Starter project captures voice, then includes an `if [text from speech] = [word1]` block. Students choose or fill in target words. The script branches on the match. Auto‑grading checks that (1) speech recognition is present, (2) the condition correctly matches the recognized text, and (3) the branch runs appropriately for test inputs.
- **CSTA:** E1‑PRO‑PF‑01 (Create code from algorithm with sequence and events).

### T23.G1.02 – Respond to different hand positions (left or right)

- **Short name:** Hand position changes what happens
- **Description:** Students detect a hand and determine if it is on the left or right side of the screen, using that to trigger different behaviors. This introduces reading spatial data from a visual input.
- **Challenge format:** Coding, guided project. Starter includes hand detection and a conditional (e.g., `if hand x > 240`). Students add different actions for left vs right. Auto‑grading checks (1) hand detection runs, (2) conditions branch based on position, and (3) sprite behavior differs for each side when tested.
- **CSTA:** E1‑PRO‑PF‑01.

### T23.G1.03 – Count how many times a word is spoken

- **Short name:** How many times did you say it?
- **Description:** Students use a variable to count repeated speech inputs. Each time the word is recognized, they increment the counter. This bridges voice input with data collection.
- **Challenge format:** Coding, guided project. Starter includes speech recognition and an empty variable (e.g., `count`). Students add a loop or multiple speech calls, incrementing count each time a target word is detected. Auto‑grading checks (1) the variable updates correctly, (2) speech recognition is called multiple times, and (3) the final count is accurate.
- **CSTA:** E1‑PRO‑DH‑02 (Label different representations of information), E1‑ALG‑AF‑01 (Create algorithms with step-by-step instructions).

### T23.G1.04 – Make a sprite talk back (text-to-speech)

- **Short name:** Sprite speaks a sentence
- **Description:** Students use the AI Speaker block to make a sprite say text aloud. They learn that text can be converted to speech, enabling audio output in projects.
- **Challenge format:** Coding, guided project. Starter includes a sprite and an empty block for the AI Speaker. Students type a sentence or reference a variable containing text. Auto‑grading checks (1) the AI Speaker block is present and activated, (2) the text is non‑empty, and (3) audio output occurs when the green flag is clicked or event is triggered.
- **CSTA:** E1‑PRO‑PF‑01.

---

## Grade 2

Grade 2 students combine voice and vision in simple sequences and begin to extract meaningful data from gesture inputs.

### T23.G2.01 – Ask a question with the microphone

- **Short name:** Listen for an answer
- **Description:** Students combine the "ask" block (which prompts the user) with speech recognition to capture an answer by voice instead of keyboard input. They use the recognized text as if it were typed input.
- **Challenge format:** Coding, guided project. Starter includes a text-to-speech "ask" block (e.g., "What is your name?"), followed by speech recognition, and a response block (e.g., `say` the recognized text). Students ensure the voice input is captured and used. Auto‑grading checks that (1) the prompt is spoken aloud, (2) speech recognition captures input, and (3) the response is generated from the recognized text.
- **CSTA:** E2‑PRO‑PF‑01 (Create code with sequence, events, and iteration).

### T23.G2.02 – Count fingers held up (hand detection)

- **Short name:** How many fingers are showing?
- **Description:** Students use hand detection to identify raised fingers. The system data includes finger curl angles; students use a counter or conditional to count stretched fingers (not curled).
- **Challenge format:** Coding, guided challenge. Starter provides hand detection and a reference to the hand data table. Students create a counter variable and loop over finger rows, checking if curl angle > 150° (approximately straight). Auto‑grading checks (1) hand detection is active, (2) the loop iterates over fingers, (3) the counter increments for extended fingers, and (4) the final count is accurate when tested with different hand poses.
- **CSTA:** E2‑DAA‑DI‑03 (Explore how patterns can be used by machines to make predictions), E2‑PRO‑DH‑02.

### T23.G2.03 – Detect a raised hand (pose/gesture)

- **Short name:** Detect if arm is raised
- **Description:** Students use body pose detection to identify if an arm is raised (e.g., shoulder and elbow y-positions indicate arm is up). This applies pose keypoint data to recognize a simple gesture.
- **Challenge format:** Coding, guided project. Starter includes body pose detection and displays the pose table. Students access rows for shoulder and elbow y coordinates and create a condition (e.g., `if elbow y < shoulder y`). Auto‑grading checks (1) pose detection is enabled, (2) coordinates are read from the correct table rows, (3) the condition logic is sound, and (4) the sprite responds appropriately when the arm is raised/lowered.
- **CSTA:** E2‑DAA‑DI‑03.

### T23.G2.04 – Translate spoken words to another language

- **Short name:** Voice translator
- **Description:** Students capture speech in one language, translate it (using a built-in block or ChatGPT), and speak the translation aloud. This chains speech recognition, text processing, and text-to-speech.
- **Challenge format:** Coding, guided project. Starter includes speech recognition, a translate block (or prompt to ChatGPT), and AI Speaker. Students complete the flow and test with a simple phrase. Auto‑grading checks (1) speech is captured, (2) translation occurs, (3) the translated text is non‑empty, and (4) audio output is produced.
- **CSTA:** E2‑PRO‑PF‑01.

---

## Grade 3

Grade 3 students use voice and gesture in loops and conditionals, combining AI inputs with game/interaction logic.

### T23.G3.01 – Repeat until spoken confirmation

- **Short name:** Keep asking until they say yes
- **Description:** Students use a `repeat until` loop with speech input: the loop keeps prompting and listening for "yes" (or a target word) and stops when that word is recognized.
- **Challenge format:** Coding, guided project. Starter includes a `repeat until` loop with speech recognition inside. Students fill in the condition (e.g., `until [text from speech] = [yes]`) and the prompt block inside the loop. Auto‑grading checks (1) the loop structure is correct, (2) the speech block is inside the loop, (3) the condition matches the target word, and (4) the loop terminates when tested.
- **CSTA:** E3‑PRO‑PF‑01 (Develop code with sequence, events, iteration, and selection).

### T23.G3.02 – Use gesture to score points in a game

- **Short name:** Hand gesture triggers points
- **Description:** Students build a simple game where detecting a specific hand gesture (e.g., fist, thumbs-up, or hand at a certain position) increases the player's score. This combines pose/gesture detection with game state (a score variable).
- **Challenge format:** Coding, interactive game. Starter includes hand detection, a score variable, and a sprite. Students define what gesture counts (e.g., `if [finger count] = 0 then [fist]`), and add a `change score by 1` block. They may wrap it in a `forever` loop to continuously check. Auto‑grading checks (1) hand detection is active, (2) the gesture condition is appropriate, (3) the score changes correctly, and (4) the game runs without errors.
- **CSTA:** E3‑PRO‑PF‑01, E3‑ALG‑AF‑01 (Write algorithms with iteration and selection).

### T23.G3.03 – Build a voice-controlled menu

- **Short name:** Say a number to pick an option
- **Description:** Students create a simple menu where speech input selects between options (e.g., "Say 1, 2, or 3 to pick a game"). The recognized number/word is matched to an action.
- **Challenge format:** Coding, guided project. Starter has a prompt asking the user to say a number, speech recognition, and multiple branches (`if text = 1, if text = 2`, etc.). Students fill in the actions for each choice. Auto‑grading checks (1) the prompt is clear, (2) speech is captured, (3) conditions match the inputs, (4) each branch does something distinct, and (5) the menu responds correctly to test inputs.
- **CSTA:** E3‑PRO‑PF‑01, E3‑ALG‑AF‑01.

### T23.G3.04 – Create a gesture-based dance (pose detection)

- **Short name:** Your pose controls a dance
- **Description:** Students use body pose detection to trigger different animations or sprite movements based on their body position. For example, when they stand with arms up, the sprite dances one way; arms down, a different way.
- **Challenge format:** Coding, interactive project. Starter includes pose detection, multiple costume/sprite animations, and conditional blocks. Students map body positions (e.g., shoulder height, arm position) to different dance moves. Auto‑grading checks (1) pose detection is active, (2) multiple conditions are present, (3) each condition triggers a different animation, and (4) the sprite responds in real time.
- **CSTA:** E3‑PRO‑PF‑01, E3‑DAA‑DI‑04 (Explain how AI models can evolve with new data).

---

## Grade 4

Grade 4 deepens the use of voice and vision, introducing data extraction and more complex interaction patterns.

### T23.G4.01 – Analyze speech sentiment or intent

- **Short name:** Understand if speech is positive or negative
- **Description:** Students use a ChatGPT block to analyze a recognized sentence and determine its sentiment or intent (e.g., "Is this person asking, telling, or excited?"). The AI response is used to branch behavior.
- **Challenge format:** Coding, guided project. Starter includes speech recognition and a ChatGPT block with a prompt like "Is this sentence positive, negative, or neutral? Answer with one word." Students add conditionals to respond based on the AI's answer. Auto‑grading checks (1) speech is captured, (2) ChatGPT is called with a clear prompt, (3) the response is used in a conditional, and (4) different actions occur for different sentiments when tested.
- **CSTA:** E4‑PRO‑PF‑01 (Develop code with sequence, events, iteration, and selection), DAA‑DP (Data Processing).

### T23.G4.02 – Track hand movement across the screen

- **Short name:** Record hand position changes
- **Description:** Students collect hand position data over time (storing x, y coordinates in a list) as the hand moves on screen. They then visualize or analyze the movement pattern (e.g., a line or path trace).
- **Challenge format:** Coding, data-collection challenge. Starter includes hand detection, a `forever` loop, and an empty list. Students add blocks to retrieve hand x/y from the detection data and `add` them to the list each frame. Auto‑grading checks (1) hand detection is active, (2) the loop runs continuously, (3) coordinates are added to the list, and (4) the list contains multiple entries after 2–3 seconds of motion.
- **CSTA:** E4‑DAA‑DF‑01 (Organize data into tables), E4‑PRO‑PF‑01.

### T23.G4.03 – Count people in the camera view

- **Short name:** How many people are visible?
- **Description:** Students use hand or pose detection to estimate the number of distinct people in frame (e.g., if multiple hand detection results appear, each likely represents one person). They maintain a counter of detected individuals.
- **Challenge format:** Coding, guided challenge. Starter includes pose/hand detection code that returns data for each detected person. Students extract and count unique individuals (e.g., by checking table row counts or manually tracking). Auto‑grading checks (1) detection is active, (2) the counting logic attempts to differentiate multiple people, and (3) the count increases/decreases as people enter/leave the frame.
- **CSTA:** E4‑DAA‑DI‑02 (Investigate relationships between attributes), E4‑PRO‑PF‑01.

### T23.G4.04 – Build an accessibility feature (voice commands)

- **Short name:** Voice commands control a game or app
- **Description:** Students design a game or application where voice commands fully control the experience (no keyboard/mouse required). For example, a player says "jump," "left," or "right" to move and interact, promoting accessibility.
- **Challenge format:** Coding, project design. Students build a simple game (e.g., avoid obstacles or collect items) where speech input is the only control method. Instructions ask them to define 3–5 clear voice commands and implement them. Auto‑grading checks (1) speech recognition is the primary input, (2) commands are clearly defined, (3) each command has a distinct effect, and (4) the game is playable via voice alone.
- **CSTA:** E4‑PRO‑PF‑01, CAS‑ET (Emerging technologies).

---

## Grade 5

Grade 5 students design more sophisticated multi-modal experiences, combining voice, vision, and game mechanics.

### T23.G5.01 – Build a chatbot that responds to voice and speaks back

- **Short name:** Conversational voice bot
- **Description:** Students create a chatbot that listens (speech recognition), sends the recognized text to ChatGPT, receives a reply, and speaks it aloud (text-to-speech). This is a complete voice conversation cycle.
- **Challenge format:** Coding, guided project. Starter includes all blocks: speech recognition, ChatGPT request, and AI Speaker. Students fill in the prompt for ChatGPT (e.g., "You are a helpful assistant. Answer this question briefly: [text from speech]"), set it to "waiting" mode so the script pauses for the response, and add the AI Speaker to vocalize the result. Auto‑grading checks (1) speech is captured, (2) ChatGPT is called and waits for a response, (3) the response is spoken aloud, and (4) the full cycle runs without errors.
- **CSTA:** E5‑PRO‑PF‑01 (Develop code with variables), DAA‑DP, CAS‑ET.

### T23.G5.02 – Detect and respond to exercise/fitness movements

- **Short name:** Fitness game using body pose
- **Description:** Students use pose detection to identify when the player is doing a specific exercise (e.g., squat, jump, arm raise) and award points for correct form or repetitions. This combines movement detection with game scoring.
- **Challenge format:** Coding, interactive fitness challenge. Starter includes pose detection, pose data table access, and a scoring variable. Students define the keypoints for one exercise (e.g., squat = bend knees, drop hips) by comparing pose coordinates over time. They track repetitions in a variable. Auto‑grading checks (1) pose detection is active, (2) the movement detection logic is reasonable (comparing relevant keypoints), (3) repetitions are counted, and (4) points are awarded when tested.
- **CSTA:** E5‑PRO‑PF‑01, E5‑DAA‑DI‑02 (Analyze datasets to identify variability), E5‑DAA‑DI‑03 (Use AI platform to train model).

### T23.G5.03 – Log and analyze gesture data from a session

- **Short name:** Record gesture data, analyze patterns
- **Description:** Students collect gesture/hand/pose data over time (position, finger angles, etc.) into a table during a gameplay or interaction session. They then analyze this data to answer questions (e.g., "What was the most common gesture?", "How much did the hand move?").
- **Challenge format:** Coding, data investigation. Starter includes hand detection in a loop, an empty data table, and blocks to add rows. Students record hand position and finger data each frame. After a collection period (or on demand), they count rows, compute averages, or identify the maximum/minimum value. Auto‑grading checks (1) data collection loop runs and populates the table, (2) the table has multiple rows, (3) at least one analysis computation is present (e.g., row count, average, max), and (4) results are displayed.
- **CSTA:** E5‑DAA‑DF‑01 (Collect different types of data), E5‑DAA‑DI‑02, E5‑PRO‑PF‑01.

### T23.G5.04 – Design an interactive art piece controlled by voice and movement

- **Short name:** Voice and gesture art installation
- **Description:** Students create an artistic project where speech input (e.g., words or emotions) and hand/body movements drive visual changes (colors, shapes, animations). The project is expressive and combines both modalities.
- **Challenge format:** Coding, creative project. Students design an interactive artwork with at least two inputs: voice (recognized words or sentiment from ChatGPT) and one vision input (hand position or pose). Each input affects the visual output (sprite costumes, colors, stage effects). Auto‑grading checks (1) speech recognition is present and responds to input, (2) vision detection is present and responds to movement, (3) at least two different visual outcomes are produced, and (4) the project runs without errors and is visually distinct.
- **CSTA:** E5‑PRO‑PF‑01, E5‑ALG‑AF‑01 (Create visual representations of algorithms), CAS‑ET.

---

## Grade 6

In middle school, students design more robust AI voice/vision systems, considering data quality, bias, and broader impacts.

### T23.G6.01 – Handle speech recognition misheard words gracefully

- **Short name:** Deal with speech recognition errors
- **Description:** Students implement error handling for speech recognition failures (e.g., when the system doesn't understand the word clearly). They add a confidence check or allow the user to retry if a word isn't recognized.
- **Challenge format:** Coding, guided project. Starter includes speech recognition and a conditional. Students add logic like "if [text from speech] is empty or unclear, then ask the user to repeat." They may also add a retry counter (max 2–3 attempts). Auto‑grading checks (1) the project includes a check for empty or invalid input, (2) the user is prompted to retry, (3) the loop doesn't infinite-loop, and (4) the feature works when tested with unclear audio.
- **CSTA:** MS‑PRO‑PF‑01 (Analyze code and identify key components), MS‑PRO‑TR‑11 (Use standard practices to test and debug).

### T23.G6.02 – Evaluate fairness and bias in pose detection

- **Short name:** Does pose detection work for everyone?
- **Description:** Students test pose detection on people with different body types, heights, abilities, and dress (e.g., loose vs tight clothing). They document whether the detection works equally well for everyone and reflect on potential bias.
- **Challenge format:** Concept and data collection. Students run a pose detection project with 3–5 different people and rate whether detection is accurate, partially accurate, or fails for each. They document observations and discuss why (e.g., loose clothing makes joint detection harder). Auto‑grading checks (1) at least 3 people are tested, (2) observations are recorded, (3) at least one difference in accuracy is noted, and (4) a reflection on potential bias is provided (e.g., "Tight clothing gave better results").
- **CSTA:** MS‑ALG‑IM‑08 (Describe common societal impacts, ethical issues, and biases), DAA‑IM‑13 (Explain benefits and risks of personal data collection).

### T23.G6.03 – Improve speech recognition with feedback loop

- **Short name:** Learn from speech recognition mistakes
- **Description:** Students design a system that allows users to correct misheard words. Each correction is logged, helping the system (conceptually) improve over time. This introduces the idea of feedback-driven AI improvement.
- **Challenge format:** Coding, guided project. Starter includes speech recognition and a list to store corrections. When the system misrecognizes, the user can say or type the correct word, which is added to a "corrections" list. Optionally, the project displays how many corrections have been made. Auto‑grading checks (1) speech recognition is present, (2) a correction mechanism exists, (3) corrections are stored in a list, (4) the list grows as corrections are made, and (5) the feature is functional.
- **CSTA:** MS‑PRO‑PF‑01, MS‑DAA‑DI‑09 (Identify relationships and make predictions), DAA‑IM‑14 (Analyze how data processing decisions lead to bias).

### T23.G6.04 – Trace and understand hand detection data

- **Short name:** Read and interpret hand data table
- **Description:** Students trace through the hand detection data table, understanding that each row represents a keypoint (finger joint) with coordinates, and each column is an attribute (x, y, z, angle). They select and use specific rows to answer questions about hand position and posture.
- **Challenge format:** Concept and coding, data-reading challenge. Starter displays the hand detection table and asks students to identify specific information (e.g., "Find the row for the thumb tip" or "Which finger is most curled?"). Students use table-lookup blocks to extract the correct row and value. Auto‑grading checks (1) the student correctly identifies the relevant table rows, (2) operations on the data are syntactically correct, (3) answers match the actual hand positions/angles when tested, and (4) understanding of the data structure is demonstrated.
- **CSTA:** MS‑PRO‑DH‑04 (Represent data using appropriate structures), MS‑DAA‑DI‑08 (Pose questions that anticipate variability), MS‑DAA‑DP‑05 (Use computational tools to organize and aggregate data).

---

## Grade 7

Grade 7 emphasizes designing and refining voice/gesture interfaces for usability and accessibility, with attention to real-world applications.

### T23.G7.01 – Design and test a hands-free app interface

- **Short name:** Build a voice-controlled interface
- **Description:** Students design a small application (e.g., a quiz, a music player, a story reader) where all controls are voice-based. They test the interface with multiple users to evaluate how well voice commands are understood.
- **Challenge format:** Coding and testing, project design. Students build an app with 4–6 clear voice commands that control the application's main functions. They test with at least 2–3 people, recording whether commands work reliably. They document any improvements needed (e.g., shorter command words, clearer instructions). Auto‑grading checks (1) the app is voice-controlled, (2) at least 4 commands are implemented, (3) testing notes from multiple users are provided, (4) at least one usability improvement is suggested, and (5) the app functions without critical errors.
- **CSTA:** MS‑PRO‑PF‑01, MS‑ALG‑HD‑04 (Refine algorithms through user feedback), CAS‑ET.

### T23.G7.02 – Combine multiple AI modalities (voice + vision) in one project

- **Short name:** Multi-modal interaction
- **Description:** Students create a project that meaningfully uses both voice and vision (or gesture) at the same time, where each modality contributes distinct information (e.g., voice gives commands, vision confirms who is speaking or detects a pose to enable the command).
- **Challenge format:** Coding, integrated project. Students design a game or app where, for example, a player must say "jump" while their hand is raised, or must say a color while that color is shown in front of the camera. Auto‑grading checks (1) both speech recognition and vision detection are active, (2) both are used in the script logic (not just one), (3) the two inputs interact meaningfully, and (4) the project demonstrates clear synergy between the modalities.
- **CSTA:** MS‑PRO‑PF‑01, MS‑PRO‑PF‑02 (Develop code from algorithms that include variables and data), MS‑DAA‑DP‑05 (Use computational tools to organize and aggregate data).

### T23.G7.03 – Measure and optimize gesture recognition accuracy

- **Short name:** Test gesture accuracy
- **Description:** Students design a gesture (e.g., a thumbs-up, a specific hand shape, or pose) and test how consistently the system detects it. They measure accuracy (number of correct detections / total attempts) and try to improve it by refining the detection logic or providing clearer instructions to users.
- **Challenge format:** Coding and data analysis, measurement challenge. Students define a target gesture and implement detection logic using hand/pose data. They perform 10+ attempts (either by themselves or with a partner) and log successes. They then adjust the detection thresholds or conditions to improve accuracy and re-test. Auto‑grading checks (1) a gesture is clearly defined, (2) detection logic is implemented, (3) at least 10 test attempts are performed and logged, (4) accuracy is calculated, (5) an attempt to improve accuracy is made, and (6) improvement is demonstrated.
- **CSTA:** MS‑DAA‑DI‑08 (Pose questions anticipating variability), MS‑DAA‑DP‑05, MS‑PRO‑TR‑11 (Test, debug, document code).

### T23.G7.04 – Explain how AI voice/vision features affect user experience

- **Short name:** Accessibility and inclusion with AI
- **Description:** Students reflect on how voice and vision recognition technologies enable or restrict access for different user groups (e.g., voice helps non-typists, but fails for those who are non-verbal; gesture recognition may miss people with limited mobility). They identify potential improvements.
- **Challenge format:** Concept and reflection, written/oral response. Students are presented with scenarios describing a user with a specific need or disability (e.g., "a non-verbal user," "someone with severe arthritis," "a blind user"). For each, they explain how voice and/or gesture recognition might help or hurt, and suggest design changes. Auto‑grading checks (1) at least 3 different user scenarios are addressed, (2) accessibility implications are identified, (3) thoughtful suggestions for improvement are provided, and (4) responses show empathy and understanding of diverse needs.
- **CSTA:** MS‑ALG‑IM‑08, MS‑ALG‑HD‑04, CAS‑ET (Evaluate how emerging tech affects user experience).

---

## Grade 8

Grade 8 builds toward high school by requiring students to design, test, and justify voice/vision systems with data-driven reasoning.

### T23.G8.01 – Implement a complete voice-to-action pipeline with error handling

- **Short name:** Robust voice command system
- **Description:** Students build a voice application that includes speech recognition, command parsing/matching, error handling for misheard words, and feedback to the user. The system is robust enough to handle real-world speech variations (e.g., "go left" vs "turn left").
- **Challenge format:** Coding, comprehensive project. Students implement a system with: (1) speech recognition, (2) a list or set of valid commands, (3) a matching/fuzzy logic to handle variations, (4) error feedback if no match is found, and (5) user confirmation (e.g., "Say yes to confirm"). Auto‑grading checks (1) all components are present, (2) the system correctly matches close variations of commands, (3) error messages are helpful, (4) the user can confirm or cancel actions, and (5) the full pipeline works across 5+ test cases.
- **CSTA:** MS‑PRO‑PF‑01, MS‑PRO‑PF‑02, MS‑PRO‑PD‑08 (Create modular programs).

### T23.G8.02 – Analyze pose data to classify or predict movement patterns

- **Short name:** Predict movement from pose
- **Description:** Students collect pose data while a person performs different movements (e.g., walking, jumping, standing still) and use a table to organize and analyze the data. They look for patterns (e.g., differences in keypoint velocities, distances, or angles) that distinguish one movement from another.
- **Challenge format:** Coding and data analysis, classification challenge. Students collect pose data over time for 2–3 different movements, storing coordinates in a table. They compute derived measures (e.g., distance between shoulders, angle of knees) for each movement type. They create a simple decision rule (e.g., "if shoulder distance < 30 and knee angle < 45, then jumping") to classify new poses. Auto‑grading checks (1) pose data is collected for multiple movement types, (2) at least 20 samples per type are recorded, (3) derived features are computed, (4) a classification rule is implemented, and (5) classification accuracy is measured on new test data.
- **CSTA:** MS‑DAA‑DF‑01 (Examine relationship between data and metadata), MS‑DAA‑DI‑09 (Identify relationships and make classifications), MS‑PRO‑DH‑04 (Represent data using appropriate structures).

### T23.G8.03 – Design and justify a voice/vision accessibility feature

- **Short name:** Create an accessible feature
- **Description:** Students design a feature of an existing game or app that uses voice or vision to improve accessibility for a specific user group (e.g., a text-to-speech narrator for a reading game, hand-gesture controls for a player with limited fine motor control). They justify their design with evidence from user testing or accessibility research.
- **Challenge format:** Coding and project design, user-centered challenge. Students pick a user group and an app domain (e.g., "a student with dyslexia playing a word game"). They design and implement an AI voice/vision feature that helps that user. They conduct at least 2 user tests (or simulated tests) and document feedback. They write a brief justification explaining how the feature addresses the user's specific need. Auto‑grading checks (1) a real accessibility goal is targeted, (2) the feature is implemented, (3) at least 2 test sessions are documented with feedback, (4) the design shows thoughtfulness (not just adding features), and (5) justification is grounded in user feedback.
- **CSTA:** MS‑ALG‑HD‑03 (Design using human-centered design principles), MS‑ALG‑HD‑04, MS‑ALG‑IM‑08, CAS‑ET.

### T23.G8.04 – Evaluate and mitigate bias in AI detection systems

- **Short name:** Test and reduce bias in AI
- **Description:** Students build or use a pose/gesture/speech detection system and systematically test it across different demographic groups, lighting conditions, accents, etc. They measure and document disparities in accuracy and propose mitigations.
- **Challenge format:** Data analysis and reflection, testing project. Students select one AI feature (hand detection, speech recognition, or pose detection) and define a test protocol. They test with at least 2 demographic groups (varied by age, gender, body type, accent, clothing, etc.) across at least 10 samples per group. They compute accuracy for each group and document any disparities. They then propose at least two mitigation strategies (e.g., "improve lighting," "retrain with diverse data," "adjust detection threshold"). Auto‑grading checks (1) systematic testing protocol is followed, (2) at least 20 total samples from at least 2 groups, (3) accuracy is computed per group, (4) disparities are identified and quantified, (5) mitigations are proposed with reasoning, and (6) the reflection shows understanding of bias in AI systems.
- **CSTA:** MS‑DAA‑IM‑13 (Explain benefits and risks), MS‑DAA‑IM‑14 (Analyze how data and processing decisions lead to bias), MS‑DAA‑IM‑15 (Analyze societal impacts of data-driven systems), CAS‑ET.

---

## Grade 9–12 (High School Pathway – Optional Extension)

While the main scope is K–8, here is guidance for high school students continuing with T23:

### HS.T23.01 – Build a production voice assistant with NLP

- **Short name:** Natural language assistant
- **Description:** Students develop a voice assistant (similar to Alexa or Google Assistant) that understands natural language intent beyond simple keyword matching. Using ChatGPT or similar LLMs, they handle complex queries and context.

### HS.T23.02 – Train a custom gesture classifier with machine learning

- **Short name:** Custom gesture recognition model
- **Description:** Students collect gesture data, preprocess it, and train a simple machine learning classifier (e.g., a decision tree or neural network) to recognize custom gestures.

### HS.T23.03 – Analyze and address privacy in voice/vision systems

- **Short name:** Privacy and ethics in voice/vision AI
- **Description:** Students research and write a report on privacy concerns in voice and vision technologies (data storage, consent, retention). They propose privacy-preserving designs or policies.

---

## Summary of Topics Covered

- **Speech-to-Text (K–8):** Recognizing speech input, matching words, handling errors, building voice-controlled interfaces.
- **Text-to-Speech (K–8):** Making sprites speak, creating conversational bots, providing accessibility.
- **Hand Detection (K–8):** Counting fingers, detecting hand position, recognizing hand-based gestures, collecting hand motion data.
- **Body Pose Detection (K–8):** Identifying raised arms/limbs, detecting exercises, classifying movements, analyzing movement patterns.
- **Gesture Recognition (K–8):** Designing and testing custom gestures, improving accuracy, combining with other inputs.
- **Multi-Modal Interaction (G5–8):** Combining voice and vision in a single project, building complex interactive systems.
- **Accessibility & Inclusion (G4–8):** Designing voice/gesture features for users with different abilities, evaluating fairness and bias.
- **Data Analysis (G2–8):** Collecting and analyzing vision/audio data, identifying patterns, measuring accuracy and fairness.
- **AI Concepts (G5–8):** Understanding how AI improves with feedback, recognizing bias in detection systems, designing human-centered AI.

---
