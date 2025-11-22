# T21 New Skills Quick Reference Guide
## 33 New Skills Added in Phase 1 Optimization

---

## ChatGPT/LLM Skills (9 new)

### Grade 5 - Introduction
**T21.G5.06** - Ask ChatGPT a simple question and display the response
- Block: `OpenAI ChatGPT: request [PROMPT] result [VAR] mode [waiting] length [200] temperature [1] session [new chat]`
- Students send first ChatGPT request and see AI-generated text

**T21.G5.07** - Understand ChatGPT parameters (temperature and length)
- Concept: Temperature (0=predictable, 2=creative), max length (response size)
- Students experiment with same question, different parameters

### Grade 6 - Application & Customization
**T21.G6.08** - Use ChatGPT to generate story text or dialogue
- Students create story content, dialogue, descriptions using ChatGPT
- Integration with CreatiCode projects

**T21.G6.09** - Compare ChatGPT responses with different temperatures
- Experiment: Same question, different temperature values
- Understand when to use focused vs creative responses

**T21.G6.10** - Use system instructions to guide ChatGPT behavior
- Block: `OpenAI ChatGPT: system request [PROMPT] session [SESSION] result [VAR] temperature [T]`
- Set AI personality (e.g., "You are a friendly pirate")

### Grade 7 - Advanced Integration
**T21.G7.07** - Use ChatGPT vision to analyze images
- Block: `attach costume [NAME] to chat` + ChatGPT request
- Multimodal AI: Analyze image content with text questions

**T21.G7.08** - Manage multiple ChatGPT conversation threads
- Block: `select ChatGPT bot [BOTID]` (1-4 parallel threads)
- Separate conversations for different purposes

### Grade 8 - Complex Systems
**T21.G8.06** - Build a multi-turn ChatGPT conversation system
- Maintain conversation context, show history, handle resets
- Complete chatbot with UI

**T21.G8.07** - Combine ChatGPT with web search for fact-checking
- Web search → ChatGPT analysis → synthesized answer
- Compare AI training data vs current web info

---

## Computer Vision Skills (8 new)

### Grade 6 - Introduction
**T21.G6.11** - Detect faces in camera video
- Block: `run face detection debug [yes/no] and write into table [TABLE]`
- Real-time face detection, position/landmark data in table

**T21.G6.12** - Track 2D body parts for gesture recognition
- Block: `run 2D body part recognition single person [yes/no] table [TABLE] debug [yes/no]`
- 17 body parts: nose, eyes, shoulders, elbows, wrists, hips, knees, ankles
- Plus arm/leg curl angles and directions

### Grade 7 - Advanced Tracking
**T21.G7.09** - Use hand detection for gesture-based controls
- Block: `run hand detection table [TABLE] debug [yes/no] show video [yes/no]`
- 47 data points per hand: fingers (curl/direction), 21 key points (x/y), 21 3D points (x/y/z)
- Gesture controls: pinch, fist, open palm, etc.

**T21.G7.10** - Build a pose-based interactive game
- Use 2D body tracking for fitness/dance/obstacle games
- Track squats, jumps, arm raises by body part positions

**T21.G7.11** - Track 3D body poses for avatar control
- Block: `run 3D pose detection debug [yes/no] table [TABLE]`
- 33 body parts in 3D space (x, y, z coordinates)
- Control 3D avatars with real body movements

### Grade 8 - Complete Applications
**T21.G8.08** - Create a gesture-controlled application
- Complete app controlled entirely by hand gestures
- Examples: virtual instrument, drawing app, game controller

**T21.G8.09** - Build a fitness tracker using pose detection
- Count exercise reps (squats, push-ups, jumping jacks)
- Real-time form feedback, progress tracking

---

## Neural Network Skills (6 new)

### Grade 7 - Introduction & Training
**T21.G7.12** - Understand what neural networks are and how they learn
- Concept: Brain-inspired AI, layers of nodes, learning from data
- Examples: image recognition, voice assistants

**T21.G7.13** - Create and train a simple neural network model
- Blocks: `create neural network model named [NAME]`, add layers, compile, train
- Observe training loss decreasing over epochs

**T21.G7.14** - Save and load trained neural network models
- Model persistence for deployment and sharing
- Avoid retraining when reusing models

### Grade 8 - Applications & Evaluation
**T21.G8.10** - Build a neural network for number recognition
- Handwritten digit recognition (0-9) or simple patterns
- Design architecture, train, evaluate, build user interface

**T21.G8.11** - Build a neural network for pattern classification
- Classify animals, text topics, image content
- Categorical training data, output layers, confidence scores

**T21.G8.12** - Evaluate neural network accuracy and improve performance
- Metrics: accuracy, precision, recall
- Identify overfitting/underfitting, improve with tuning

---

## KNN Machine Learning Skills (3 new)

### Grade 7 - Introduction & Creation
**T21.G7.15** - Understand K-Nearest Neighbors (KNN) classification
- Concept: Classify by finding K closest training examples, majority vote
- When KNN works (simple patterns) vs neural networks (complex patterns)

**T21.G7.16** - Create a KNN classifier from training data
- Block: `create KNN number classifier from table [TABLE] K [K] named [NAME]`
- Prepare labeled training data, choose K value (typically 3-5)

### Grade 8 - Real-Time Application
**T21.G8.13** - Use KNN for real-time data classification
- Block: `use KNN classifier [NAME] to predict label from table [TABLE] show neighbors [yes/no]`
- Applications: gesture classification, sound recognition, sensor data
- Compare KNN vs neural networks for use case

---

## Semantic Search Skills (3 new)

### Grade 8 Only - Advanced AI Feature
**T21.G8.14** - Create a semantic search database
- Block: `create semantic database from table [TABLE]`
- Table with 'key' column + metadata, converted to embeddings
- Uses Pinecone vector database

**T21.G8.15** - Search with semantic similarity
- Block: `search semantic database with [QUERY] store top (K) in table [TABLE]`
- Block: `search semantic database with [QUERY] where [CONDITION] store top (K) in table [TABLE]`
- Meaning-based search: "What's your phone?" matches "Contact: 555-1234"

**T21.G8.16** - Build a knowledge base with semantic search
- Complete Q&A system with natural language queries
- Combines semantic search (retrieval) + ChatGPT (synthesis)

---

## NLP & Web Search Skills (4 new)

### Grade 7 - NLP Introduction
**T21.G7.17** - Analyze text with parts-of-speech tagging
- NLP analysis: identify nouns, verbs, adjectives, etc.
- Applications: grammar checking, keyword extraction, summarization

### Grade 8 - Web Search Integration
**T21.G8.17** - Use web search to gather information
- Block: `web search [QUERY] store top (K) in table [TABLE]`
- Returns: title, link, snippet for top K results
- Evaluate result quality and relevance

**T21.G8.18** - Build a research assistant combining web search and ChatGPT
- Complete pipeline: web search → extract snippets → ChatGPT synthesis → answer with sources
- Demonstrates AI system integration for real-world applications

---

## Skill Distribution by Grade

```
Grade 5: +2 skills (ChatGPT basics)
  └─ G5.06, G5.07

Grade 6: +5 skills (ChatGPT apps + computer vision intro)
  └─ G6.08, G6.09, G6.10, G6.11, G6.12

Grade 7: +11 skills (Advanced CV, ML intro, NLP)
  └─ G7.07, G7.08 (ChatGPT)
  └─ G7.09, G7.10, G7.11 (Computer Vision)
  └─ G7.12, G7.13, G7.14 (Neural Networks)
  └─ G7.15, G7.16 (KNN)
  └─ G7.17 (NLP)

Grade 8: +15 skills (All advanced/capstone projects)
  └─ G8.06, G8.07 (ChatGPT systems)
  └─ G8.08, G8.09 (CV applications)
  └─ G8.10, G8.11, G8.12 (Neural network projects)
  └─ G8.13 (KNN application)
  └─ G8.14, G8.15, G8.16 (Semantic search)
  └─ G8.17, G8.18 (Web search)
```

---

## Key Block Syntax Reference

### ChatGPT
```
OpenAI ChatGPT: request [PROMPT] result [VAR] mode [waiting] length [200] temperature [1] session [new chat]
OpenAI ChatGPT: system request [PROMPT] session [SESSION] result [VAR] temperature [T]
select ChatGPT bot [BOTID]  // 1-4 for parallel threads
attach costume [NAME] to chat
```

### Computer Vision
```
run face detection debug [yes/no] and write into table [TABLE]
run 2D body part recognition single person [yes/no] table [TABLE] debug [yes/no]
run 3D pose detection debug [yes/no] table [TABLE]
run hand detection table [TABLE] debug [yes/no] show video [yes/no]
stop 2D body part recognition
```

### Neural Networks (TensorFlow.js)
```
create neural network model named [NAME]
// add layers, compile, train blocks...
save neural network model [NAME]
load neural network model [NAME]
```

### KNN
```
create KNN number classifier from table [TABLE] K [K] named [NAME]
use KNN classifier [NAME] to predict label from table [TABLE] show neighbors [yes/no]
```

### Semantic Search (Pinecone)
```
create semantic database from table [TABLE]
search semantic database with [QUERY] store top (K) in table [TABLE] filter by column [FIELD] of value [VALUE]
search semantic database with [QUERY] where [CONDITION] store top (K) in table [TABLE]
```

### NLP & Web
```
// parts-of-speech analysis block
web search [QUERY] store top (K) in table [TABLE]
```

---

## Integration Patterns

### Pattern 1: ChatGPT + DALL-E
```
ChatGPT generates description → DALL-E creates image → Display result
```
Example: T21.G7.02 (Expand briefs before generating art)

### Pattern 2: Speech → ChatGPT → TTS
```
Speech recognition → ChatGPT processes → Text-to-speech responds
```
Example: T21.G8.05 (Voice-controlled creative assistant)

### Pattern 3: Web Search → ChatGPT
```
Web search gathers data → ChatGPT synthesizes → Present answer
```
Example: T21.G8.07, G8.18 (Fact-checking, research assistant)

### Pattern 4: Computer Vision → Game Logic
```
Camera tracking → Extract positions/gestures → Trigger game events
```
Example: T21.G7.10, G8.08, G8.09 (Pose games, gesture apps, fitness)

### Pattern 5: Semantic Search → ChatGPT
```
Semantic search retrieves relevant info → ChatGPT generates natural answer
```
Example: T21.G8.16 (Knowledge base)

---

**Document Purpose:** Quick lookup for educators implementing new T21 skills
**Last Updated:** 2025-11-21
**Total New Skills:** 33
