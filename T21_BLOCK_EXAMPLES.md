# T21 AI Media - Block Usage Examples
## Practical Code Examples for All New Skills

---

## ChatGPT/LLM Examples (9 skills)

### G5.06: Basic ChatGPT Request
```scratch
when green flag clicked
ask [What question would you like to ask AI?] and wait
OpenAI ChatGPT: request (answer) result [ai_response v] mode [waiting v] length [200] temperature [1] session [new chat v]
say (ai_response) for (5) secs
```

### G5.07: Experimenting with Temperature
```scratch
when green flag clicked
set [question v] to [Tell me a story about a robot]

// Low temperature (predictable)
OpenAI ChatGPT: request (question) result [response_low v] mode [waiting v] length [200] temperature [0.2] session [new chat v]

// High temperature (creative)
OpenAI ChatGPT: request (question) result [response_high v] mode [waiting v] length [200] temperature [1.8] session [new chat v]

say (join [Low temp: ] (response_low)) for (3) secs
say (join [High temp: ] (response_high)) for (3) secs
```

### G6.10: System Instructions
```scratch
when green flag clicked
// Set system instruction to make AI speak like a pirate
OpenAI ChatGPT: system request [You are a friendly pirate. Always respond in pirate speak with "arrr" and nautical terms.] session [pirate_bot v] result [system_result v] temperature [1]

ask [What would you like to ask the pirate?] and wait
OpenAI ChatGPT: request (answer) result [pirate_response v] mode [waiting v] length [200] temperature [1] session [pirate_bot v]
say (pirate_response) for (5) secs
```

### G7.07: ChatGPT Vision
```scratch
when green flag clicked
switch costume to [photo1 v]
attach costume [photo1] to chat
OpenAI ChatGPT: request [Describe what you see in this image in detail] result [description v] mode [waiting v] length [300] temperature [1] session [vision_chat v]
say (description) for (5) secs
```

### G7.08: Multiple Conversation Threads
```scratch
when green flag clicked
// Bot 1 for story narration
select ChatGPT bot [1]
OpenAI ChatGPT: system request [You are a story narrator. Keep responses concise and dramatic.] session [narrator v] result [r1 v] temperature [1]

// Bot 2 for game hints
select ChatGPT bot [2]
OpenAI ChatGPT: system request [You are a helpful game guide. Give short, clear hints.] session [guide v] result [r2 v] temperature [0.5]

when [space v] key pressed
// Get narration from bot 1
select ChatGPT bot [1]
OpenAI ChatGPT: request [Continue the story] result [narration v] mode [waiting v] length [150] temperature [1] session [narrator v]
say (narration)

when [h v] key pressed
// Get hint from bot 2
select ChatGPT bot [2]
OpenAI ChatGPT: request [I'm stuck on this puzzle] result [hint v] mode [waiting v] length [100] temperature [0.5] session [guide v]
say (hint)
```

---

## Computer Vision Examples (8 skills)

### G6.11: Face Detection
```scratch
when green flag clicked
delete all of [face_data v]
run face detection debug [yes v] and write into table [face_data v]

forever
  if <(number of rows in table [face_data v]) > [0]> then
    say (join [I see ] (number of rows in table [face_data v])) for (1) secs
  else
    say [No faces detected] for (1) secs
  end
end
```

### G6.12: 2D Body Tracking for Gesture
```scratch
when green flag clicked
run 2D body part recognition single person [yes v] table [body_data v] debug [yes v]

forever
  // Check if person is raising their hand
  set [left_wrist_y v] to (value in table [body_data v] column [y] row where [part] = [left_wrist])
  set [left_shoulder_y v] to (value in table [body_data v] column [y] row where [part] = [left_shoulder])

  if <(left_wrist_y) > (left_shoulder_y)> then
    say [Hand raised! Starting game...] for (2) secs
    broadcast [start_game v]
  end
end
```

### G7.09: Hand Gesture Controls
```scratch
when green flag clicked
run hand detection table [hand_data v] debug [yes v] show video [no v]

forever
  // Check for closed fist (all fingers curled)
  set [thumb_curl v] to (value in table [hand_data v] column [curl] row where [part] = [thumb])
  set [index_curl v] to (value in table [hand_data v] column [curl] row where [part] = [index])

  if <<(thumb_curl) < [90]> and <(index_curl) < [90]>> then
    say [Fist detected - Grab!] for (0.5) secs
    broadcast [grab_object v]
  end

  // Check for open hand (all fingers straight)
  if <<(thumb_curl) > [150]> and <(index_curl) > [150]>> then
    say [Open hand - Release!] for (0.5) secs
    broadcast [release_object v]
  end
end
```

### G7.11: 3D Pose Detection
```scratch
when green flag clicked
run 3D pose detection debug [yes v] table [pose_3d v]

forever
  // Get 3D position of right hand
  set [hand_x v] to (value in table [pose_3d v] column [x] row where [part] = [right wrist])
  set [hand_y v] to (value in table [pose_3d v] column [y] row where [part] = [right wrist])
  set [hand_z v] to (value in table [pose_3d v] column [z] row where [part] = [right wrist])

  // Move 3D avatar to match hand position
  go to 3D x: (hand_x * 10) y: (hand_y * 10) z: (hand_z * 10)
end
```

### G8.09: Fitness Tracker (Squat Counter)
```scratch
when green flag clicked
set [squat_count v] to [0]
set [is_down v] to [false]
run 2D body part recognition single person [yes v] table [body_data v] debug [yes v]

forever
  // Get hip and knee positions to detect squat
  set [hip_y v] to (value in table [body_data v] column [y] row where [part] = [left_hip])
  set [knee_y v] to (value in table [body_data v] column [y] row where [part] = [left_knee])

  // Check if person is in squat position (hip below knee)
  if <<(hip_y) < (knee_y)> and <(is_down) = [false]>> then
    set [is_down v] to [true]
    say [Down!] for (0.5) secs
  end

  // Check if person stood up
  if <<(hip_y) > ((knee_y) + [50])> and <(is_down) = [true]>> then
    set [is_down v] to [false]
    change [squat_count v] by (1)
    say (join [Squats: ] (squat_count)) for (1) secs
  end
end
```

---

## Neural Network Examples (6 skills)

### G7.13: Create and Train Neural Network
```scratch
when green flag clicked
// Create a simple neural network for classifying numbers
create neural network model named [digit_classifier]

// Add layers: input (784 neurons), hidden (128 neurons), output (10 neurons)
add dense layer to model [digit_classifier] units [128] activation [relu v]
add dense layer to model [digit_classifier] units [10] activation [softmax v]

// Compile model
compile neural network model [digit_classifier] optimizer [adam v] loss [categoricalCrossentropy v]

// Train model (using training data in a table)
say [Training model...] for (2) secs
train neural network model [digit_classifier] from table [training_data v] epochs [10] batch size [32]

say [Training complete!] for (2) secs
```

### G7.14: Save and Load Model
```scratch
// Save trained model
when [s v] key pressed
save neural network model [digit_classifier]
say [Model saved!] for (2) secs

// Load previously trained model
when [l v] key pressed
load neural network model [digit_classifier]
say [Model loaded!] for (2) secs
```

### G8.10: Use Neural Network for Prediction
```scratch
when green flag clicked
load neural network model [digit_classifier]

forever
  ask [Draw a digit (0-9) and press enter] and wait

  // Get drawn digit data into table
  get drawing data into table [input_data v]

  // Make prediction
  predict with neural network model [digit_classifier] from table [input_data v] store in [prediction v]

  say (join [I think you drew: ] (prediction)) for (3) secs
end
```

---

## KNN Machine Learning Examples (3 skills)

### G7.16: Create KNN Classifier
```scratch
when green flag clicked
// Prepare training data table with labeled examples
// Table has columns: label, feature1, feature2, feature3, ...

say [Creating KNN classifier...] for (2) secs
create KNN number classifier from table [training_data v] K [5] named [gesture_classifier]
say [Classifier ready!] for (2) secs
```

### G8.13: Real-Time Classification with KNN
```scratch
when green flag clicked
create KNN number classifier from table [training_data v] K [3] named [activity_classifier]

forever
  // Collect real-time sensor data into table
  get sensor readings into table [current_data v]

  // Classify the activity
  use KNN classifier [activity_classifier] to predict label from table [current_data v] show neighbors [no v]

  // Get predicted label from first row of table
  set [activity v] to (value in table [current_data v] column [label] row [1])

  say (join [Activity: ] (activity)) for (1) secs
end
```

---

## Semantic Search Examples (3 skills)

### G8.14: Create Semantic Database
```scratch
when green flag clicked
// Prepare a table with 'key' column and optional metadata
// Example: key | category | author
//          "How do I reset password?" | FAQ | Admin
//          "What's your phone number?" | Contact | Support

say [Creating semantic database...] for (2) secs
create semantic database from table [knowledge_base v]
say [Database created!] for (2) secs
```

### G8.15: Semantic Search
```scratch
when green flag clicked
ask [What would you like to know?] and wait

// Search database and get top 3 results
search semantic database with (answer) store top [3] in table [search_results v] filter by column [] of value []

// Display results
say [Found these matches:] for (2) secs
repeat (number of rows in table [search_results v])
  say (value in table [search_results v] column [key] row (counter)) for (2) secs
end
```

### G8.16: Knowledge Base with ChatGPT
```scratch
when green flag clicked
create semantic database from table [knowledge_base v]

forever
  ask [Ask me anything!] and wait

  // Step 1: Search knowledge base
  search semantic database with (answer) store top [3] in table [results v] filter by column [] of value []

  // Step 2: Build context from results
  set [context v] to []
  repeat (number of rows in table [results v])
    set [context v] to (join (context) (value in table [results v] column [key] row (counter)))
    set [context v] to (join (context) [. ])
  end

  // Step 3: Send to ChatGPT for natural answer
  set [prompt v] to (join [Based on this information: ] (context))
  set [prompt v] to (join (prompt) (join [. Answer this question: ] (answer)))

  OpenAI ChatGPT: request (prompt) result [ai_answer v] mode [waiting v] length [300] temperature [0.7] session [kb_chat v]

  say (ai_answer) for (5) secs
end
```

---

## Web Search Examples (3 skills)

### G8.17: Basic Web Search
```scratch
when green flag clicked
ask [What would you like to search for?] and wait

web search (answer) store top [5] in table [search_results v]

say [Found search results!] for (2) secs

// Display results
repeat (number of rows in table [search_results v])
  set [title v] to (value in table [search_results v] column [title] row (counter))
  set [snippet v] to (value in table [search_results v] column [snippet] row (counter))
  say (join (title) (join [: ] (snippet))) for (3) secs
end
```

### G8.18: Research Assistant (Web + ChatGPT)
```scratch
when green flag clicked
ask [What question can I research for you?] and wait
set [question v] to (answer)

// Step 1: Web search
say [Searching the web...] for (2) secs
web search (question) store top [5] in table [web_results v]

// Step 2: Extract snippets from web results
set [context v] to []
repeat (number of rows in table [web_results v])
  set [snippet v] to (value in table [web_results v] column [snippet] row (counter))
  set [context v] to (join (context) (join (snippet) [. ]))
end

// Step 3: Ask ChatGPT to synthesize information
say [Analyzing information...] for (2) secs
set [prompt v] to (join [Based on these web search results: ] (context))
set [prompt v] to (join (prompt) (join [. Answer this question in 2-3 sentences: ] (question)))

OpenAI ChatGPT: request (prompt) result [synthesized_answer v] mode [waiting v] length [300] temperature [0.5] session [research v]

// Step 4: Present answer with sources
say [Here's what I found:] for (2) secs
say (synthesized_answer) for (5) secs

say [Sources:] for (2) secs
repeat (number of rows in table [web_results v])
  set [source v] to (value in table [web_results v] column [title] row (counter))
  say (source) for (2) secs
end
```

---

## NLP Example (1 skill)

### G7.17: Parts-of-Speech Analysis
```scratch
when green flag clicked
ask [Enter a sentence to analyze:] and wait

// Analyze text with NLP
analyze parts of speech in (answer) store in table [pos_results v]

say [Analysis complete!] for (2) secs

// Show word types
repeat (number of rows in table [pos_results v])
  set [word v] to (value in table [pos_results v] column [word] row (counter))
  set [pos v] to (value in table [pos_results v] column [pos] row (counter))
  say (join (join (word) [ is a ]) (pos)) for (2) secs
end
```

---

## Multi-Modal Integration Examples

### G7.05: Synchronized AI Media (ChatGPT + DALL-E + TTS)
```scratch
when green flag clicked
// Step 1: Generate narration with ChatGPT
OpenAI ChatGPT: request [Write one sentence describing a magical forest at sunset] result [narration v] mode [waiting v] length [100] temperature [1.2] session [story v]

// Step 2: Generate matching image with DALL-E
set [image_prompt v] to (join [magical forest at sunset, ] [cinematic lighting, fantasy art style])
OpenAI DALL-E: generate costume image name [forest_scene] description (image_prompt) with resolution [512x512 v]

// Step 3: Wait for image to load
wait (3) seconds

// Step 4: Display image and speak narration simultaneously
switch costume to [forest_scene]
say (narration) in [English (United States) v] as [Female v] speed (90) pitch (100) volume (100) store sound as []
```

### G8.05: Voice-Controlled Creative Assistant
```scratch
when green flag clicked
say [Say a command to generate an image!] for (3) secs

start continuous speech recognition in [English (United States) v] into list [voice_commands v]

forever
  if <(length of [voice_commands v]) > [0]> then
    set [command v] to (item (length of [voice_commands v]) of [voice_commands v])

    // Check for appropriate content
    set [mod_result v] to (get moderation result for (command))

    if <(mod_result) = [Pass]> then
      say [Generating image...] for (2) secs
      OpenAI DALL-E: generate costume image name [generated] description (command) with resolution [512x512 v]
      wait (3) seconds
      switch costume to [generated]
      say [Image complete!] in [English (United States) v] as [Female v] speed (100) pitch (100) volume (100) store sound as []
    else
      say [That prompt isn't appropriate. Try something else!] for (2) secs
    end

    delete (length of [voice_commands v]) of [voice_commands v]
  end
end
```

---

## Best Practices for Each Category

### ChatGPT/LLM
✓ Always use appropriate temperature (0-0.5 for facts, 0.7-1.5 for creative)
✓ Limit length to avoid overwhelming responses
✓ Use system instructions for consistent personality
✓ Moderate user inputs before sending to AI

### Computer Vision
✓ Test with good lighting conditions
✓ Use debug mode during development
✓ Handle cases when tracking fails (empty tables)
✓ Consider privacy implications of camera use

### Machine Learning
✓ Prepare sufficient training data
✓ Validate model accuracy before deployment
✓ Save trained models to avoid retraining
✓ Monitor for overfitting/underfitting

### Semantic Search
✓ Use descriptive keys in database
✓ Include relevant metadata for filtering
✓ Test with various query phrasings
✓ Combine with ChatGPT for natural answers

### Web Search
✓ Verify result relevance before using
✓ Cite sources when presenting information
✓ Combine with AI for synthesis
✓ Handle cases with no results

---

**Document Purpose:** Practical code examples for implementing T21 skills
**Last Updated:** 2025-11-21
**Block Syntax:** Based on blockdes8.txt specifications
