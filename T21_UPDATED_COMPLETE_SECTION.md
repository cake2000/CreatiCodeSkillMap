# COMPLETE UPDATED T21 SECTION
## Ready to replace lines 9806-10113 in skillsv4/allskills.md

---

ID: T21.G3.01
Topic: T21 – AI Media
Skill: Tell whether media was AI-generated or recorded
Description: Students compare pairs of images or short sounds (one AI-generated, one recorded) and pick which seems AI-made, explaining clues (odd shadows, repeated textures, robotic voice tone).

Dependencies:
* T20.G3.01: Translate art recipe cards into blocks


ID: T21.G3.02
Topic: T21 – AI Media
Skill: Describe what you want AI to create using simple words
Description: Students practice turning an idea into a short description by naming the subject (what), colors, and setting (where). For example, they turn "I want a cat picture" into "orange cat sitting on a blue couch." This builds foundational prompt vocabulary before working with AI tools.

Dependencies:
* T21.G3.01: Tell whether media was AI-generated or recorded


ID: T21.G4.01
Topic: T21 – AI Media
Skill: Choose safe and specific prompts for images
Description: Given a vague or risky image request ("make a person" or "draw my house address"), students rewrite it to be specific, safe, and privacy-friendly (e.g., "Draw a friendly robot in a park, daytime").

Dependencies:
* T21.G3.01: Tell whether media was AI-generated or recorded


ID: T21.G4.02
Topic: T21 – AI Media
Skill: Describe AI media you've experienced
Description: Students share examples of AI-generated content they've encountered (AI art, AI voices in videos, chatbot responses). They describe what made it useful or confusing, building vocabulary for discussing AI media quality and appropriateness.

Dependencies:
* T21.G3.01: Tell whether media was AI-generated or recorded


ID: T21.G4.03
Topic: T21 – AI Media
Skill: Identify strengths and limits of AI image generation
Description: Students examine several AI-generated images and list what AI does well (colorful backgrounds, patterns, fantasy scenes) and struggles with (drawing hands correctly, readable text, counting objects). This understanding helps them know when AI is the right tool.

Dependencies:
* T21.G3.01: Tell whether media was AI-generated or recorded
* T21.G4.02: Describe AI media you've experienced


ID: T21.G5.01
Topic: T21 – AI Media
Skill: Decide AI vs hand-made for a single asset type
Description: Given one asset need (e.g., "we need a background for our story"), students explain whether AI generation or hand-drawing would work better, considering factors like uniqueness, consistency, and time. They justify their choice with one reason.

Dependencies:
* T21.G4.01: Choose safe and specific prompts for images
* T21.G4.03: Identify strengths and limits of AI image generation


ID: T21.G5.02
Topic: T21 – AI Media
Skill: Generate a single AI image using a simple prompt
Description: Students use the `OpenAI DALL-E: generate costume image name [NAME] description [TEXT] with resolution [SIZE]` block to create one image from a descriptive prompt. They observe how the AI interprets their words and compare the result to their expectation. Resolution options are 256x256, 512x512, or 1024x1024.

Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T21.G4.01: Choose safe and specific prompts for images


ID: T21.G5.03
Topic: T21 – AI Media
Skill: Use AI text-to-speech to read text aloud
Description: Students use the `say [TEXT] in [LANGUAGE] as [VOICETYPE] speed (N) pitch (N) volume (N)` block to have the computer speak a sentence aloud. They experiment with different voice types (Male, Female, Boy, Girl, Male2, Female2, Male3, Female3), languages (30+ options), and speech parameters (speed, pitch, volume) to understand how text-to-speech works.

Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T21.G3.01: Tell whether media was AI-generated or recorded


ID: T21.G5.04
Topic: T21 – AI Media
Skill: Understand how speech-to-text works
Description: Students explore how computers convert spoken words into text. They learn that clear speech, good microphone quality, and minimal background noise improve accuracy. They test by speaking clearly vs mumbling to see how recognition quality changes.

Dependencies:
* T21.G3.01: Tell whether media was AI-generated or recorded


ID: T21.G5.05
Topic: T21 – AI Media
Skill: Explain why AI content needs safety review
Description: Students discuss why AI-generated images and text need human review before sharing publicly. They identify potential issues (inappropriate content, bias, misinformation) and explain the role of content moderation in keeping AI outputs safe.

Dependencies:
* T21.G4.01: Choose safe and specific prompts for images
* T21.G4.03: Identify strengths and limits of AI image generation


ID: T21.G5.06
Topic: T21 – AI Media
Skill: Ask ChatGPT a simple question and display the response
Description: Students use the `OpenAI ChatGPT: request [PROMPT] result [VARIABLE] mode [waiting] length [200] temperature [1] session [new chat]` block to ask ChatGPT a simple question and display the response. They observe how the AI generates human-like text responses.

Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T09.G3.01: Create and use a numeric variable for score or count


ID: T21.G5.07
Topic: T21 – AI Media
Skill: Understand ChatGPT parameters (temperature and length)
Description: Students learn what temperature (0-2, controls randomness/creativity) and max length (controls response length) parameters do. They experiment by asking the same question with different parameter values and comparing responses to see how these settings affect AI output.

Dependencies:
* T21.G5.06: Ask ChatGPT a simple question and display the response


ID: T21.G6.01
Topic: T21 – AI Media
Skill: Plan a mixed-source asset kit for a game or story project
Description: Given a specific project (e.g., a simple platformer game or an interactive story), students list all visual and audio assets needed, categorize each as "AI-generated," "hand-created," or "library," and justify each choice (e.g., "AI for varied backgrounds because we need many unique scenes, hand-drawn for the main character for consistent appearance across frames").

Dependencies:
* T21.G4.01: Choose safe and specific prompts for images
* T21.G5.01: Decide AI vs hand-made for a single asset type


ID: T21.G6.02
Topic: T21 – AI Media
Skill: Write structured prompts to maintain consistent visual style
Description: Students transform vague ideas (e.g., "dragon in a cave") into detailed prompts with five components: subject, action, camera angle, color palette, and mood. By reusing this structure across multiple assets, they ensure all generated images share a consistent visual style suitable for a cohesive project.

Dependencies:
* T21.G5.01: Decide AI vs hand-made for a single asset type
* T21.G5.02: Generate a single AI image using a simple prompt


ID: T21.G6.03
Topic: T21 – AI Media
Skill: Build a prompt test bench inside CreatiCode
Description: Students design a screen with a text input, dropdown style selector, and gallery of preview sprites. Pressing a "Generate" button triggers the `OpenAI DALL-E: generate costume image` block, loads three variations, and logs each prompt + URL in a table so the designer can choose a winner.

Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T09.G3.01: Create and use a numeric variable for score or count
* T10.G3.03: Add and remove items from a list
* T21.G5.02: Generate a single AI image using a simple prompt


ID: T21.G6.04
Topic: T21 – AI Media
Skill: Iterate when an AI output fails requirements
Description: Students practice reading a failed generation (wrong colors, missing character, awkward proportions), identifying the cause (prompt missing detail, wrong style, conflicting terms), and rewriting the prompt to address the issue. They compare "before/after" versions to show how iteration improves fit.

Dependencies:
* T10.G3.03: Add and remove items from a list
* T21.G5.02: Generate a single AI image using a simple prompt


ID: T21.G6.05
Topic: T21 – AI Media
Skill: Use AI speech recognition to capture user voice input
Description: Students use `start recognizing speech in [LANGUAGE] record as [SOUNDNAME]` (Azure or OpenAI Whisper), `end speech recognition`, and `text from speech` blocks to record their voice and convert it to text. They verify the transcription accuracy and understand speech-to-text limitations. Students can choose between Microsoft Azure or OpenAI Whisper providers.

Dependencies:
* T06.G4.01: Use broadcast to coordinate sprite actions
* T21.G5.04: Understand how speech-to-text works


ID: T21.G6.06
Topic: T21 – AI Media
Skill: Check user input with AI content moderation
Description: Students use the `get moderation result for [TEXT]` block to check whether user-submitted text is appropriate. They build a simple input checker that displays "Pass" or "Fail" based on the moderation result.

Dependencies:
* T08.G4.01: Add else to handle the opposite case
* T21.G5.05: Explain why AI content needs safety review


ID: T21.G6.07
Topic: T21 – AI Media
Skill: Use image moderation to check visual content
Description: Students use `get moderation result for image at URL [URL]` or `get moderation result for costume named [NAME]` to check whether uploaded or AI-generated images meet content guidelines. They build a checker that flags inappropriate visuals before display.

Dependencies:
* T21.G5.02: Generate a single AI image using a simple prompt
* T21.G6.06: Check user input with AI content moderation


ID: T21.G6.08
Topic: T21 – AI Media
Skill: Use ChatGPT to generate story text or dialogue
Description: Students use ChatGPT to generate creative text content for their projects, such as story narration, character dialogue, or scene descriptions. They provide clear prompts that specify the tone, style, and content they want, then integrate the generated text into their CreatiCode projects.

Dependencies:
* T21.G5.06: Ask ChatGPT a simple question and display the response
* T21.G5.07: Understand ChatGPT parameters (temperature and length)


ID: T21.G6.09
Topic: T21 – AI Media
Skill: Compare ChatGPT responses with different temperatures
Description: Students experiment with the temperature parameter (0 = predictable/focused, 2 = creative/random) by asking ChatGPT the same question multiple times with different temperature values. They analyze how temperature affects creativity, consistency, and appropriateness of responses for different use cases.

Dependencies:
* T21.G5.07: Understand ChatGPT parameters (temperature and length)


ID: T21.G6.10
Topic: T21 – AI Media
Skill: Use system instructions to guide ChatGPT behavior
Description: Students use the `OpenAI ChatGPT: system request [PROMPT] session [SESSION] result [VARIABLE] temperature [T]` block to set system-level instructions that guide how ChatGPT responds. They learn how system prompts (e.g., "You are a friendly pirate," "Always respond in rhymes") shape the AI's personality and output style.

Dependencies:
* T21.G5.06: Ask ChatGPT a simple question and display the response


ID: T21.G6.11
Topic: T21 – AI Media
Skill: Detect faces in camera video
Description: Students use the `run face detection debug [yes/no] and write into table [TABLE]` block to turn on the device camera and detect faces in real-time. The results (face positions, landmarks) are written to a table. They understand how face detection works and what data it provides.

Dependencies:
* T06.G4.01: Use broadcast to coordinate sprite actions
* T10.G3.03: Add and remove items from a list


ID: T21.G6.12
Topic: T21 – AI Media
Skill: Track 2D body parts for gesture recognition
Description: Students use the `run 2D body part recognition single person [yes/no] table [TABLE] debug [yes/no]` block to detect body parts (nose, eyes, shoulders, elbows, wrists, hips, knees, ankles) in camera video. They read the resulting table to understand body positions and use this data to trigger actions (e.g., raise hand to start, jump to jump).

Dependencies:
* T06.G4.01: Use broadcast to coordinate sprite actions
* T10.G4.01: Use a list to solve a problem with many similar items


ID: T21.G7.01
Topic: T21 – AI Media
Skill: Create a reusable prompt template library
Description: Students build a CreatiCode table with columns such as `subject`, `palette`, `camera`, `lighting`, and `tone`. A loop reads each row, assembles the prompt using placeholders, calls DALL-E, and records the returned costume name + URL. This ensures a whole level or comic chapter shares the same art direction.

Dependencies:
* T07.G5.01: Use a counted repeat loop
* T09.G5.01: Use variables to make a program more general or clear
* T10.G5.03: Add and remove items from a list
* T21.G6.03: Build a prompt test bench inside CreatiCode
* T21.G6.04: Iterate when an AI output fails requirements


ID: T21.G7.02
Topic: T21 – AI Media
Skill: Use ChatGPT to expand creative briefs before generating art
Description: Students combine the `OpenAI ChatGPT: request` block (with system message + role prompt) with DALL-E. ChatGPT converts a story outline into polished image prompts (e.g., "Scene 3: aerial view of neon market, magenta lighting"), then each prompt feeds the DALL-E block. Students compare raw vs. AI-enhanced prompts to see the quality improvement.

Dependencies:
* T08.G5.01: Use a simple if in a script
* T09.G5.01: Use variables to make a program more general or clear
* T10.G5.03: Add and remove items from a list
* T21.G6.03: Build a prompt test bench inside CreatiCode
* T21.G6.04: Iterate when an AI output fails requirements
* T21.G6.08: Use ChatGPT to generate story text or dialogue


ID: T21.G7.03
Topic: T21 – AI Media
Skill: Audit AI imagery for representation and bias
Description: Students design experiments (e.g., run "a scientist giving a talk" 10 times) and log characteristics (perceived gender, culture, age) into a table. They graph the distribution, identify gaps, and adjust prompts (adding descriptors, requesting diversity) to reach targeted representation goals, highlighting AI4K12's focus on societal impact.

Dependencies:
* T07.G5.01: Use a counted repeat loop
* T08.G5.01: Use a simple if in a script
* T09.G5.01: Use variables to make a program more general or clear
* T10.G5.03: Add and remove items from a list
* T21.G6.03: Build a prompt test bench inside CreatiCode
* T21.G6.04: Iterate when an AI output fails requirements


ID: T21.G7.04
Topic: T21 – AI Media
Skill: Blend AI frames with manual touch-ups for animation
Description: Students import AI-generated poses for a character, then fix artifacts (hands, faces, edges) using the costume editor or vector tools. They align all frames with equal sizing and anchor points, then script a timed animation that matches UI state (buttons, HUD cues).

Dependencies:
* T06.G5.01: Fix a behavior that runs at the wrong time
* T08.G5.01: Use a simple if in a script
* T09.G5.01: Use variables to make a program more general or clear
* T10.G5.03: Add and remove items from a list
* T21.G6.04: Iterate when an AI output fails requirements


ID: T21.G7.05
Topic: T21 – AI Media
Skill: Synchronize AI visuals with AI narration for a single scene
Description: Students create one immersive scene by combining ChatGPT (to craft narration text), DALL-E (to generate a matching background), and text-to-speech (to read the narration aloud). They focus on timing—ensuring the voiceover starts when the visual appears and describes what's on screen. This is a single-scene exercise in cross-modal alignment.

Dependencies:
* T06.G5.01: Fix a behavior that runs at the wrong time
* T09.G5.01: Use variables to make a program more general or clear
* T10.G5.03: Add and remove items from a list
* T21.G5.03: Use AI text-to-speech to read text aloud
* T21.G6.04: Iterate when an AI output fails requirements
* T21.G6.08: Use ChatGPT to generate story text or dialogue


ID: T21.G7.06
Topic: T21 – AI Media
Skill: Use continuous speech recognition for live dictation
Description: Students use `start continuous speech recognition in [LANGUAGE] into list [LISTNAME]` and `stop continuous speech recognition` blocks to capture ongoing speech as a list of recognized phrases. They build a live dictation or voice-command application that responds to speech in real-time.

Dependencies:
* T10.G5.03: Add and remove items from a list
* T21.G6.05: Use AI speech recognition to capture user voice input


ID: T21.G7.07
Topic: T21 – AI Media
Skill: Use ChatGPT vision to analyze images
Description: Students use the `attach costume [NAME] to chat` block followed by a ChatGPT request to have the AI analyze and describe what's in an image. They ask questions like "What objects do you see?" or "Describe the mood of this image" to understand how multimodal AI can process both text and visual information.

Dependencies:
* T21.G5.02: Generate a single AI image using a simple prompt
* T21.G6.08: Use ChatGPT to generate story text or dialogue


ID: T21.G7.08
Topic: T21 – AI Media
Skill: Manage multiple ChatGPT conversation threads
Description: Students learn that CreatiCode supports 4 parallel ChatGPT conversation threads (bot IDs 1-4) using the `select ChatGPT bot [BOTID]` block. They build an application that maintains separate conversations (e.g., one for game narration, one for hints, one for character dialogue) and switch between threads appropriately.

Dependencies:
* T21.G6.08: Use ChatGPT to generate story text or dialogue
* T21.G6.10: Use system instructions to guide ChatGPT behavior


ID: T21.G7.09
Topic: T21 – AI Media
Skill: Use hand detection for gesture-based controls
Description: Students use the `run hand detection table [TABLE] debug [yes/no] show video [yes/no]` block to detect hands in camera video. The resulting table contains hand data (left/right), finger positions, curl angles (180 = straight), and directions. They use this data to create gesture-based controls (e.g., pinch to select, fist to grab, open palm to release).

Dependencies:
* T08.G5.01: Use a simple if in a script
* T10.G5.03: Add and remove items from a list
* T21.G6.12: Track 2D body parts for gesture recognition


ID: T21.G7.10
Topic: T21 – AI Media
Skill: Build a pose-based interactive game
Description: Students create a simple game that responds to body movements detected by the 2D body tracking system. Examples include a fitness game (track squats by knee position), a dance game (match poses), or an obstacle game (duck/jump by changing body height). They read body part positions from the tracking table and trigger game events.

Dependencies:
* T08.G5.01: Use a simple if in a script
* T09.G5.01: Use variables to make a program more general or clear
* T21.G6.12: Track 2D body parts for gesture recognition


ID: T21.G7.11
Topic: T21 – AI Media
Skill: Track 3D body poses for avatar control
Description: Students use the `run 3D pose detection debug [yes/no] table [TABLE]` block to detect 33 body parts in 3D space (x, y, z coordinates). They use this detailed 3D tracking data to control a 3D avatar or character, mapping real body movements to virtual character movements for immersive interactions.

Dependencies:
* T08.G5.01: Use a simple if in a script
* T10.G5.03: Add and remove items from a list
* T21.G6.12: Track 2D body parts for gesture recognition


ID: T21.G7.12
Topic: T21 – AI Media
Skill: Understand what neural networks are and how they learn
Description: Students learn that neural networks are AI systems inspired by the brain, consisting of layers of connected nodes that learn patterns from data through training. They discuss examples (image recognition, voice assistants) and understand that neural networks need training data, learn through trial-and-error, and improve with more data.

Dependencies:
* T21.G4.03: Identify strengths and limits of AI image generation


ID: T21.G7.13
Topic: T21 – AI Media
Skill: Create and train a simple neural network model
Description: Students use TensorFlow.js blocks to create a neural network: `create neural network model named [NAME]`, add layers, compile the model, and train it on simple data (e.g., classifying numbers or patterns). They observe how training loss decreases over epochs and understand the basic training process.

Dependencies:
* T07.G5.01: Use a counted repeat loop
* T10.G5.03: Add and remove items from a list
* T21.G7.12: Understand what neural networks are and how they learn


ID: T21.G7.14
Topic: T21 – AI Media
Skill: Save and load trained neural network models
Description: Students learn that trained neural networks can be saved and reused without retraining. They use the save and load model blocks to persist their trained models, understanding the practical importance of model persistence for deployment and sharing.

Dependencies:
* T21.G7.13: Create and train a simple neural network model


ID: T21.G7.15
Topic: T21 – AI Media
Skill: Understand K-Nearest Neighbors (KNN) classification
Description: Students learn how KNN works: it classifies new data by finding the K closest training examples and taking a majority vote. They explore when KNN is useful (simple patterns, small datasets) vs when neural networks are better (complex patterns, large datasets), understanding trade-offs between different ML approaches.

Dependencies:
* T21.G7.12: Understand what neural networks are and how they learn


ID: T21.G7.16
Topic: T21 – AI Media
Skill: Create a KNN classifier from training data
Description: Students use the `create KNN number classifier from table [TABLE] K [K] named [NAME]` block to build a KNN classifier. They prepare a training data table with labeled examples, choose an appropriate K value (typically 3-5), and create the classifier. They understand how the K value affects classification decisions.

Dependencies:
* T10.G5.03: Add and remove items from a list
* T21.G7.15: Understand K-Nearest Neighbors (KNN) classification


ID: T21.G7.17
Topic: T21 – AI Media
Skill: Analyze text with parts-of-speech tagging
Description: Students use NLP blocks to analyze text and identify parts of speech (nouns, verbs, adjectives, etc.). They explore how computers understand language structure and use this analysis for applications like grammar checking, keyword extraction, or text summarization.

Dependencies:
* T10.G5.03: Add and remove items from a list
* T21.G6.08: Use ChatGPT to generate story text or dialogue


ID: T21.G8.01
Topic: T21 – AI Media
Skill: Build a user-facing generative art widget with guardrails
Description: Students design an in-app panel (text field, preset buttons, preview box) where users can request a fresh background. The script moderates the prompt with `get moderation result`, applies house style presets, runs DALL-E, and falls back to curated art if moderation fails. Users can save approved scenes to a gallery.

Dependencies:
* T06.G6.01: Trace event execution paths in a multi‑event program
* T08.G6.01: Use conditionals to control simulation steps
* T09.G6.01: Model real-world quantities using variables and formulas
* T10.G6.01: Sort a table by a column
* T21.G6.06: Check user input with AI content moderation
* T21.G7.01: Create a reusable prompt template library


ID: T21.G8.02
Topic: T21 – AI Media
Skill: Implement an approval pipeline for AI assets
Description: Students build a dashboard that lists each generated asset with metadata: prompt, author, moderation result, reviewer notes, and publish toggle. Only assets with "Approved" checked become visible in the live scene. This mirrors professional workflows and enforces accountability.

Dependencies:
* T08.G6.01: Use conditionals to control simulation steps
* T09.G6.01: Model real-world quantities using variables and formulas
* T10.G6.01: Sort a table by a column
* T21.G6.06: Check user input with AI content moderation
* T21.G7.01: Create a reusable prompt template library


ID: T21.G8.03
Topic: T21 – AI Media
Skill: Produce a multi-scene media experience from a creative brief
Description: Students receive a creative brief with setting and emotional arc (3-5 beats). They use ChatGPT to generate scene-by-scene descriptions, DALL-E to produce art for each scene, and text-to-speech for narration. Unlike G7.05's single-scene focus, this capstone requires managing multiple scenes with consistent style, scene-to-scene navigation UI, and coordinated transitions. Students must track scene state, implement navigation buttons, and ensure visual/audio consistency across all scenes.

Dependencies:
* T06.G6.01: Trace event execution paths in a multi‑event program
* T09.G6.01: Model real-world quantities using variables and formulas
* T10.G6.01: Sort a table by a column
* T21.G7.02: Use ChatGPT to expand creative briefs before generating art
* T21.G7.05: Synchronize AI visuals with AI narration for a single scene


ID: T21.G8.04
Topic: T21 – AI Media
Skill: Develop ethical guidelines for AI media use in a studio
Description: Students research a real example (e.g., a game studio using AI concept art), identify stakeholder concerns (artists, players, communities referenced), and draft a 5-point policy covering: disclosure requirements, credit attribution, data sourcing ethics, review process, and escalation paths. They connect guidelines to their in-class workflows (moderation logs, approval pipelines) to demonstrate practical accountability.

Dependencies:
* T08.G6.01: Use conditionals to control simulation steps
* T09.G6.01: Model real-world quantities using variables and formulas
* T10.G6.01: Sort a table by a column
* T21.G8.02: Implement an approval pipeline for AI assets


ID: T21.G8.05
Topic: T21 – AI Media
Skill: Build a voice-controlled creative assistant
Description: Students create an application that accepts voice commands through continuous speech recognition, interprets user intent (e.g., "draw a sunset over mountains"), generates AI images based on the spoken prompt, and announces results using text-to-speech. This capstone integrates all AI media threads: speech recognition, image generation, content moderation, and audio output.

Dependencies:
* T21.G7.06: Use continuous speech recognition for live dictation
* T21.G8.01: Build a user-facing generative art widget with guardrails


ID: T21.G8.06
Topic: T21 – AI Media
Skill: Build a multi-turn ChatGPT conversation system
Description: Students create an interactive chatbot that maintains conversation context across multiple turns. They use the session parameter to preserve conversation history, implement a chat interface showing conversation history, handle user input in real-time, and gracefully manage conversation resets or topic changes.

Dependencies:
* T06.G6.01: Trace event execution paths in a multi‑event program
* T09.G6.01: Model real-world quantities using variables and formulas
* T10.G6.01: Sort a table by a column
* T21.G7.08: Manage multiple ChatGPT conversation threads


ID: T21.G8.07
Topic: T21 – AI Media
Skill: Combine ChatGPT with web search for fact-checking
Description: Students build a fact-checking assistant that uses the `web search [QUERY] store top (K) in table [TABLE]` block to gather information from the web, then sends the search results to ChatGPT for analysis and summarization. They compare ChatGPT's knowledge (from training data) with current web information to understand AI limitations and the importance of up-to-date data.

Dependencies:
* T10.G6.01: Sort a table by a column
* T21.G6.08: Use ChatGPT to generate story text or dialogue


ID: T21.G8.08
Topic: T21 – AI Media
Skill: Create a gesture-controlled application with hand tracking
Description: Students build a complete application controlled entirely by hand gestures detected through the hand tracking system. Examples include a virtual instrument (finger positions control notes), a drawing app (index finger draws, fist erases), or a game controller (different gestures for different actions). They implement robust gesture recognition with error handling.

Dependencies:
* T08.G6.01: Use conditionals to control simulation steps
* T09.G6.01: Model real-world quantities using variables and formulas
* T21.G7.09: Use hand detection for gesture-based controls


ID: T21.G8.09
Topic: T21 – AI Media
Skill: Build a fitness tracker using pose detection
Description: Students create a fitness application that tracks exercises using 2D or 3D pose detection. The app counts repetitions (e.g., squats, push-ups, jumping jacks) by analyzing body part positions and angles, provides real-time form feedback, tracks progress over time, and displays statistics. This capstone demonstrates practical computer vision applications.

Dependencies:
* T08.G6.01: Use conditionals to control simulation steps
* T09.G6.01: Model real-world quantities using variables and formulas
* T10.G6.01: Sort a table by a column
* T21.G7.10: Build a pose-based interactive game


ID: T21.G8.10
Topic: T21 – AI Media
Skill: Build a neural network for number recognition
Description: Students create and train a neural network to recognize handwritten digits (0-9) or simple patterns. They prepare training data, design an appropriate network architecture (input layer, hidden layers, output layer), train the model with sufficient epochs, evaluate accuracy on test data, and build an interface where users can draw numbers for recognition.

Dependencies:
* T08.G6.01: Use conditionals to control simulation steps
* T09.G6.01: Model real-world quantities using variables and formulas
* T10.G6.01: Sort a table by a column
* T21.G7.13: Create and train a simple neural network model
* T21.G7.14: Save and load trained neural network models


ID: T21.G8.11
Topic: T21 – AI Media
Skill: Build a neural network for pattern classification
Description: Students create a neural network to classify patterns or categories in data (e.g., classifying animals by features, categorizing text by topic, or sorting images by content). They understand how to prepare categorical training data, choose appropriate output layers, interpret classification confidence scores, and evaluate model performance.

Dependencies:
* T08.G6.01: Use conditionals to control simulation steps
* T09.G6.01: Model real-world quantities using variables and formulas
* T10.G6.01: Sort a table by a column
* T21.G7.13: Create and train a simple neural network model


ID: T21.G8.12
Topic: T21 – AI Media
Skill: Evaluate neural network accuracy and improve performance
Description: Students learn to measure neural network performance using metrics like accuracy, precision, and recall. They test their models on new data, identify when models are overfitting or underfitting, and apply strategies to improve performance (adjust architecture, add more training data, tune hyperparameters like learning rate and epochs).

Dependencies:
* T09.G6.01: Model real-world quantities using variables and formulas
* T10.G6.01: Sort a table by a column
* T21.G8.10: Build a neural network for number recognition


ID: T21.G8.13
Topic: T21 – AI Media
Skill: Use KNN for real-time data classification
Description: Students build a real-time classification system using KNN. They use the `use KNN classifier [NAME] to predict label from table [TABLE] show neighbors [yes/no]` block to classify new data points as they arrive. Applications include gesture classification, sound recognition, or sensor data categorization. They compare KNN performance with neural networks for their use case.

Dependencies:
* T08.G6.01: Use conditionals to control simulation steps
* T10.G6.01: Sort a table by a column
* T21.G7.16: Create a KNN classifier from training data


ID: T21.G8.14
Topic: T21 – AI Media
Skill: Create a semantic search database
Description: Students use the `create semantic database from table [TABLE]` block to build a vector database using Pinecone. They prepare a table with a 'key' column (text to be searchable) and optional metadata columns. They understand how semantic search converts text to embeddings (vector representations) that capture meaning, enabling similarity-based search.

Dependencies:
* T10.G6.01: Sort a table by a column
* T21.G6.08: Use ChatGPT to generate story text or dialogue


ID: T21.G8.15
Topic: T21 – AI Media
Skill: Search with semantic similarity
Description: Students use `search semantic database with [QUERY] store top (K) in table [TABLE]` or `search semantic database with [QUERY] where [CONDITION] store top (K) in table [TABLE]` to perform semantic searches. Unlike keyword search, semantic search finds results based on meaning, so "What's your phone number?" matches "Contact: 555-1234" even without shared words.

Dependencies:
* T10.G6.01: Sort a table by a column
* T21.G8.14: Create a semantic search database


ID: T21.G8.16
Topic: T21 – AI Media
Skill: Build a knowledge base with semantic search
Description: Students create a complete knowledge base application where users can ask questions in natural language and receive relevant answers through semantic search. They combine semantic search with ChatGPT: search finds relevant information from the database, then ChatGPT synthesizes the information into a natural language answer. This demonstrates how modern AI systems combine retrieval and generation.

Dependencies:
* T08.G6.01: Use conditionals to control simulation steps
* T09.G6.01: Model real-world quantities using variables and formulas
* T21.G8.06: Build a multi-turn ChatGPT conversation system
* T21.G8.15: Search with semantic similarity


ID: T21.G8.17
Topic: T21 – AI Media
Skill: Use web search to gather information
Description: Students use the `web search [QUERY] store top (K) in table [TABLE]` block to search the web and retrieve results (title, link, snippet) in a table. They understand how web search works, evaluate result quality and relevance, and extract useful information from search results for their projects.

Dependencies:
* T10.G6.01: Sort a table by a column


ID: T21.G8.18
Topic: T21 – AI Media
Skill: Build a research assistant combining web search and ChatGPT
Description: Students create a research assistant that answers questions by combining web search and ChatGPT. When a user asks a question, the system: (1) searches the web for current information, (2) extracts relevant snippets from results, (3) sends the question and web data to ChatGPT for synthesis, (4) presents a comprehensive answer with sources. This capstone demonstrates AI system integration for real-world applications.

Dependencies:
* T08.G6.01: Use conditionals to control simulation steps
* T09.G6.01: Model real-world quantities using variables and formulas
* T10.G6.01: Sort a table by a column
* T21.G8.07: Combine ChatGPT with web search for fact-checking
* T21.G8.17: Use web search to gather information


---

## END OF T21 SECTION
**Total Skills:** 64 (G3: 2, G4: 3, G5: 7, G6: 12, G7: 17, G8: 23)
**Lines to Replace:** 9806-10113 in skillsv4/allskills.md
