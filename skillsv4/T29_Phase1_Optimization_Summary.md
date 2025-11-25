# T29 (Text Data & NLP Foundations) - Phase 1 Optimization Summary

## Overview
Topic T29 has been optimized to break down overly broad skills into smaller, more manageable units focused on single blocks/features. This ensures students can learn each concept thoroughly before moving on.

## Key Changes Made

### 1. Skills Broken Down into Sub-Skills

#### T29.G4.01 (Split/Join) → 3 Sub-Skills
- **T29.G4.01.01**: Use the split block to break text into a list
- **T29.G4.01.02**: Use the join block to combine list items into text
- **T29.G4.01.03**: Use the part-of block to get specific segments

#### T29.G4.03 (Count characters/words) → 2 Sub-Skills
- **T29.G4.03.01**: Count characters in text using "length of" operator
- **T29.G4.03.02**: Count words in text using split and list length

#### T29.G4.04.02 (String comparison) → 2 Sub-Skills
- **T29.G4.04.02**: Test if text includes a substring
- **T29.G4.04.03**: Test if text starts with or ends with a pattern

#### T29.G4.05.02 (ChatGPT blocks) → 3 Sub-Skills
- **T29.G4.05.02**: Make a basic ChatGPT request and store the result
- **T29.G4.05.03**: Use ChatGPT to summarize text
- **T29.G4.05.04**: Configure ChatGPT response length and temperature

#### T29.G4.06 (Replace/Remove punctuation) → 2 Sub-Skills
- **T29.G4.06.01**: Use the replace block to substitute text
- **T29.G4.06.02**: Remove punctuation using the replace block

#### T29.G4.07 (Substring/Position) → 2 Sub-Skills
- **T29.G4.07.01**: Find text position using "position of" block
- **T29.G4.07.02**: Extract substrings using "substring" block

#### T29.G5.06 (Parse sentence) → 3 Sub-Skills
- **T29.G5.06.01**: Use the parse sentence block to analyze grammar
- **T29.G5.06.02**: Extract lemmas (word stems) from parsed sentences
- **T29.G5.06.03**: Filter words by part of speech

#### T29.G6.06 (Speech-to-text) → 4 Sub-Skills
- **T29.G6.06.01**: Start and stop speech recognition with Azure
- **T29.G6.06.02**: Retrieve recognized text from speech
- **T29.G6.06.03**: Use OpenAI Whisper for speech recognition
- **T29.G6.06.04**: Use continuous speech recognition for real-time transcription

#### T29.G6.07 (Text-to-speech) → 3 Sub-Skills
- **T29.G6.07.01**: Convert text to speech using basic TTS block
- **T29.G6.07.02**: Customize TTS with speed, pitch, and volume
- **T29.G6.07.03**: Stop speech and manage TTS playback

#### T29.G7.05 (Web search) → 2 Sub-Skills
- **T29.G7.05.01**: Use the web search block to retrieve search results
- **T29.G7.05.02**: Extract and process text from web search results

#### T29.G8.05 (Regex) → 6 Sub-Skills
- **T29.G8.05.01**: Understand regex pattern basics
- **T29.G8.05.02**: Use regex test block for pattern validation
- **T29.G8.05.03**: Use regex match to extract patterns
- **T29.G8.05.04**: Use regex search to find pattern positions
- **T29.G8.05.05**: Use regex replace for advanced text transformation
- **T29.G8.05.06**: Use regex split for flexible tokenization

### 2. New Skills Added for Better Scaffolding

#### Grade 5
- **T29.G5.11**: Use content moderation to check text safety

#### Grade 6
- **T29.G6.03.01**: Use ChatGPT sessions for conversation context
- **T29.G6.03.02**: Set system instructions for ChatGPT behavior

### 3. Dependency Fixes

#### Fixed Incorrect Dependencies:
- **T29.G7.04**: Changed dependency from "T29.G5.01" (which was wrong) to "T29.G4.05.03: Use ChatGPT to summarize text"

#### Fixed Forward Dependencies:
- **T29.G5.06**: Removed forward dependency on T29.G5.08.02 (which came after it)

#### Simplified Over-Connected Dependencies:
- **T29.G4.02**: Simplified dependencies (removed unnecessary T01, T04 refs)
- **T29.G4.04.01**: Simplified dependencies
- **T29.G4.10**: Simplified dependencies
- **T29.G6.08**: Fixed reference to use new sub-skill ID
- **T29.G8.06**: Simplified dependencies (removed redundant lower-grade refs)

### 4. Skill Descriptions Improved

All skill descriptions were reviewed and improved to be:
- More specific about which block is being used
- More actionable with clear learning outcomes
- More concrete about what students will build or create

## Summary Statistics

| Category | Before | After |
|----------|--------|-------|
| Total T29 Skills | 57 | 80 |
| Grade 4 Skills | 12 | 20 |
| Grade 5 Skills | 12 | 15 |
| Grade 6 Skills | 10 | 17 |
| Grade 7 Skills | 5 | 6 |
| Grade 8 Skills | 6 | 10 |

## Cross-Topic Dependencies Preserved

All dependencies to other topics (T01-T28, T30+) were preserved unchanged, including:
- T04 (Algorithms), T05 (Design), T06 (Events), T07 (Loops)
- T08 (Conditionals), T09 (Variables), T10 (Lists), T11 (Tables)
- T15 (Animation), T17 (Physics), T22 (AI/ML)

## Notes for Phase 2

The following cross-topic dependencies may need review in Phase 2:
- Some T29 skills depend on T22 (AI/ML) skills for ML classification
- Consider if T15 (Animation state machine) dependency is necessary for text skills
- T17 (Physics) dependency in T29.G8.03 seems unusual and may need review
