# T29 SKILL SPLITS - VISUAL BREAKDOWN
## How Overly Broad Skills Were Decomposed

---

## SPLIT 1: ChatGPT Request Block (Grade 4)

### Before (1 skill):
```
T29.G4.05.02: Generate AI summaries using ChatGPT blocks
├─ Learn the ChatGPT request block
├─ Understand prompt parameter
├─ Understand result variable parameter
├─ Understand mode parameter (streaming/waiting)
├─ Understand length parameter (max tokens)
├─ Understand temperature parameter (creativity)
├─ Understand session parameter (new/continue)
└─ Generate summaries with all these parameters
```

### After (5 skills):
```
T29.G4.05.02.01: Understand ChatGPT request block parameters
└─ Overview of all parameters and what they do

T29.G4.05.02.02: Send basic ChatGPT requests in waiting mode
├─ Depends on: T29.G4.05.02.01
└─ Focus: Use waiting mode, basic prompt/result usage

T29.G4.05.02.03: Use streaming mode for real-time responses
├─ Depends on: T29.G4.05.02.02
└─ Focus: Streaming mode, real-time updates, ✅ emoji detection

T29.G4.05.02.04: Control response length with max tokens
├─ Depends on: T29.G4.05.02.02
└─ Focus: Max length parameter, token limits (100 tokens ≈ 75 words)

T29.G4.05.02.05: Adjust creativity with temperature
├─ Depends on: T29.G4.05.02.02
└─ Focus: Temperature parameter (0-1 scale), creativity control
```

**Why split**: One skill tried to teach 6 different parameters. Students need to master basic usage before exploring advanced parameters.

---

## SPLIT 2: Prompt Engineering (Grade 5)

### Before (1 skill):
```
T29.G5.05: Build dynamic prompts with join and concatenation
├─ Use join blocks to build prompts
├─ Add variable placeholders
├─ Few-shot prompting with examples
├─ Role-based prompts
└─ Template-based prompt generation
```

### After (3 skills):
```
T29.G5.05.01: Build dynamic prompts with variable placeholders
└─ Focus: Join blocks, variable slots, basic templates

T29.G5.05.02: Engineer few-shot prompts with examples
├─ Depends on: T29.G5.05.01
└─ Focus: Few-shot learning, example-driven prompts

T29.G5.05.03: Use role-based prompts for ChatGPT
├─ Depends on: T29.G5.05.01
└─ Focus: Role assignment, persona-based prompts
```

**Why split**: Three distinct prompt engineering techniques. Each is a separate methodology.

---

## SPLIT 3: Parse Sentence Block (Grade 5)

### Before (1 skill):
```
T29.G5.06: Use the parse sentence block for parts of speech
├─ Understand the ai_parsesentence block
├─ Learn output table structure (7 columns)
├─ Extract TEXT column (original words)
├─ Extract LEMMA column (word stems)
├─ Extract TYPE column (part of speech)
├─ Extract LABEL column (grammatical role)
├─ Extract HEAD column (dependency parsing)
├─ Extract ID column (word position)
└─ Extract DEPENDENCY column (syntax trees)
```

### After (4 skills):
```
T29.G5.06.01: Understand the parse sentence block structure
└─ Focus: Block overview, table columns explained

T29.G5.06.02: Extract parts of speech using TEXT and TYPE columns
├─ Depends on: T29.G5.06.01
└─ Focus: Find nouns, verbs, adjectives using TYPE column

T29.G5.06.03: Extract word stems using the LEMMA column
├─ Depends on: T29.G5.06.01
└─ Focus: Lemmatization (running→run, better→good)

T29.G5.06.04: Analyze grammatical roles using the LABEL column
├─ Depends on: T29.G5.06.02
└─ Focus: Subject/object/modifier identification
```

**Why split**: The block outputs 7 columns of linguistic data. Original skill tried to teach all columns at once. Now students master one column type at a time.

---

## SPLIT 4: Speech-to-Text (Grade 6)

### Before (1 skill):
```
T29.G6.06: Convert speech to text using voice recognition
├─ Understand Azure vs OpenAI Whisper APIs
├─ Use single-utterance recognition
├─ Use continuous recognition
├─ Select from 40+ languages
├─ Store recorded audio
└─ Process recognized text
```

### After (6 skills):
```
T29.G6.06.01: Understand speech-to-text block options
└─ Focus: Azure vs OpenAI Whisper comparison

T29.G6.06.02: Use basic speech recognition (single utterance)
├─ Depends on: T29.G6.06.01
└─ Focus: Start/end recognition, get text from speech

T29.G6.06.03: Select language for speech recognition
├─ Depends on: T29.G6.06.02
└─ Focus: Language dropdown, testing different languages

T29.G6.06.04: Store recorded audio from speech recognition
├─ Depends on: T29.G6.06.02
└─ Focus: SOUNDNAME parameter, saving/replaying audio

T29.G6.06.05: Use continuous speech recognition
├─ Depends on: T29.G6.06.02
└─ Focus: Continuous mode, list output, real-time updates

T29.G6.06.06: Clear speech recognition results [NEW]
├─ Depends on: T29.G6.06.02
└─ Focus: Clear speech text block
```

**Why split**: Two different APIs, two different modes (single vs continuous), 40+ languages, audio storage. Each feature needs focused practice.

---

## SPLIT 5: Text-to-Speech (Grade 6)

### Before (1 skill):
```
T29.G6.07: Convert text to speech with voice selection
├─ Use Azure TTS block
├─ Select from 8 voice types (Male, Female, Boy, Girl, etc.)
├─ Select from 40+ languages
├─ Adjust speed (percentage)
├─ Adjust pitch (percentage)
├─ Adjust volume (percentage)
└─ Store synthesized audio
```

### After (5 skills):
```
T29.G6.07.01: Use basic text-to-speech with default settings
└─ Focus: Basic TTS block usage, default voice

T29.G6.07.02: Select voice types for text-to-speech
├─ Depends on: T29.G6.07.01
└─ Focus: 8 voice types, language compatibility

T29.G6.07.03: Customize TTS speed, pitch, and volume
├─ Depends on: T29.G6.07.01
└─ Focus: 3 parameters (speed/pitch/volume), expressive speech

T29.G6.07.04: Store synthesized speech as audio
├─ Depends on: T29.G6.07.01
└─ Focus: SOUNDNAME parameter, saving audio

T29.G6.07.05: Stop text-to-speech playback [NEW]
├─ Depends on: T29.G6.07.01
└─ Focus: Stop speaking block
```

**Why split**: Voice selection, language selection, 3 customization parameters (speed/pitch/volume), audio storage. Each needs separate attention.

---

## SPLIT 6: Pinecone Semantic Search (Grade 7)

### Before (1 skill):
```
T29.G7.01.02: Use Pinecone semantic search blocks (advanced)
├─ Create semantic database from table
├─ Understand vector embeddings
├─ Perform basic semantic search
├─ Filter by single metadata field
├─ Use complex conditional filters (AND/OR logic)
└─ Compare semantic vs keyword search
```

### After (4 skills):
```
T29.G7.01.02.01: Create semantic database from table
└─ Focus: addtabletopinecone block, 'key' column requirement

T29.G7.01.02.02: Perform basic semantic search without filters
├─ Depends on: T29.G7.01.02.01
└─ Focus: searchfrompinecone block, top K results

T29.G7.01.02.03: Filter semantic search by single metadata field
├─ Depends on: T29.G7.01.02.02
└─ Focus: Simple filter (column = value)

T29.G7.01.02.04: Use complex conditional filters
├─ Depends on: T29.G7.01.02.03
└─ Focus: searchfrompinecone2 block, WHERE conditions, AND/OR logic
```

**Why split**: Four distinct operations: database creation, basic search, simple filtering, complex filtering. Each builds on the previous.

---

## SPLIT 7: Web Search (Grade 7)

### Before (1 skill):
```
T29.G7.05: Integrate web search results into text analysis
├─ Use Google search API block
├─ Extract title/link/snippet from results
├─ Display results in user-friendly format
├─ Process snippets with text analysis
└─ Combine search with other text processing
```

### After (3 skills):
```
T29.G7.05.01: Use Google search API block
└─ Focus: googlesearch block, table with 3 columns

T29.G7.05.02: Extract and display web search results
├─ Depends on: T29.G7.05.01
└─ Focus: Extract title/link/snippet, display formatting

T29.G7.05.03: Analyze text from web search snippets
├─ Depends on: T29.G7.05.02
└─ Focus: Apply text analysis (frequency, sentiment, keywords)
```

**Why split**: Three distinct steps: API usage, result extraction/display, text analysis integration.

---

## SPLIT 8: Regex Pattern Matching (Grade 8)

### Before (1 skill):
```
T29.G8.05: Use regex for advanced pattern matching
├─ Learn regex syntax
├─ Use regex test block (check if pattern exists)
├─ Use regex match block (extract patterns)
├─ Use regex search block (find position)
├─ Use regex replace block (substitute text)
├─ Use regex split block (tokenize)
└─ Build validators and parsers
```

### After (5 skills):
```
T29.G8.05.01: Use regex test block for pattern matching
└─ Focus: operator_regex_test, true/false results

T29.G8.05.02: Use regex match block to extract patterns
├─ Depends on: T29.G8.05.01
└─ Focus: operator_regex_match_into_list, 'g' flag

T29.G8.05.03: Use regex search block to find positions
├─ Depends on: T29.G8.05.01
└─ Focus: operator_regex_search, position index

T29.G8.05.04: Use regex replace block for text substitution
├─ Depends on: T29.G8.05.02
└─ Focus: operator_regex_replace_with, 'g' flag

T29.G8.05.05: Use regex split block for advanced tokenization
├─ Depends on: T29.G8.05.01
└─ Focus: operator_regex_split_into_list, complex delimiters
```

**Why split**: CreatiCode has 5 separate regex blocks. Each block has different functionality and output. One skill per block ensures mastery.

---

## PATTERN ANALYSIS

### Common Reasons for Splitting:

1. **Multiple Blocks in One Skill**
   - Example: Regex (5 blocks) → 5 skills
   - Rule: 1 block = 1 skill (usually)

2. **Multiple Parameters to Master**
   - Example: ChatGPT (6 parameters) → 5 skills
   - Rule: Complex parameters deserve individual skills

3. **Multiple Output Types**
   - Example: Parse sentence (7 columns) → 4 skills
   - Rule: Group related outputs, but don't overwhelm

4. **Progressive Complexity**
   - Example: Pinecone search (basic → filtered → complex) → 4 skills
   - Rule: Scaffold from simple to complex

5. **Different Modes/APIs**
   - Example: Speech-to-text (Azure vs Whisper, single vs continuous) → 6 skills
   - Rule: Each mode/API combination gets focus

---

## PEDAGOGICAL BENEFITS

### Before Splitting:
- ❌ Students overwhelmed by too many concepts
- ❌ Can't practice one feature without getting distracted by others
- ❌ Hard to assess mastery of individual features
- ❌ Teachers can't target specific gaps
- ❌ Scope creep makes skills too large

### After Splitting:
- ✅ One clear learning objective per skill
- ✅ Students can master one feature at a time
- ✅ Easy to assess understanding of each feature
- ✅ Teachers can identify and address specific gaps
- ✅ Proper scaffolding with clear prerequisites

---

## DEPENDENCY STRUCTURE EXAMPLE

### ChatGPT Skills Dependency Chain:

```
T29.G4.05.01: Compare human vs AI summaries (conceptual)
    └─ No technical skills needed, just understanding

T29.G4.05.02.01: Understand ChatGPT parameters
    └─ Builds on: G4.05.01

T29.G4.05.02.02: Send basic requests (waiting mode)
    └─ Builds on: G4.05.02.01

    ├─→ T29.G4.05.02.03: Streaming mode
    │   └─ Builds on: G4.05.02.02
    │
    ├─→ T29.G4.05.02.04: Max tokens
    │   └─ Builds on: G4.05.02.02
    │
    └─→ T29.G4.05.02.05: Temperature
        └─ Builds on: G4.05.02.02

T29.G6.05.01: Session types (new vs continue)
    └─ Builds on: G4.05.02.02 (2 grades later)

T29.G7.02.01: System messages
    └─ Builds on: G5.05.03 (role-based prompts)
```

**Pattern**: Foundation skill → Multiple parallel advanced skills → Integration skills

---

## COVERAGE COMPLETENESS

### Block-to-Skill Mapping:

| CreatiCode Block | Skill(s) Covering It |
|-----------------|---------------------|
| ai_startspeech | G6.06.02, G6.06.03, G6.06.04 |
| ai_startopenaispeech | G6.06.01, G6.06.02 |
| ai_endspeech | G6.06.02 |
| ai_textfromspeech | G6.06.02 |
| ai_clearspeech | G6.06.06 |
| ai_startrecognizer | G6.06.05 |
| ai_stoprecognizer | G6.06.05 |
| ai_speakinlanguage | G6.07.01-04 |
| ai_stopspeaking | G6.07.05 |
| openaichatcompletion | G4.05.02.01-05 |
| openaichatcompletionsystem | G7.02.01 |
| openai_chatgpt_cancel | G6.05.02 |
| llmchatcompletion | G7.02.02 |
| llmsysteminstruction | G7.02.03 |
| switchchatbot | G7.02.04 |
| attachimagetochat | G7.02.05 |
| attachfilestochat | G7.02.06 |
| attachgooglefiletochat | G7.02.07 |
| getmoderationresult | G7.06.01 |
| getmoderationresult2 | G7.06.02 |
| getmoderationresult3 | G7.06.02 |
| ai_parsesentence | G5.06.01-04 |
| addtabletopinecone | G7.01.02.01 |
| searchfrompinecone | G7.01.02.02-03 |
| searchfrompinecone2 | G7.01.02.04 |
| googlesearch | G7.05.01 |
| operator_regex_test | G8.05.01 |
| operator_regex_match_into_list | G8.05.02 |
| operator_regex_search | G8.05.03 |
| operator_regex_replace_with | G8.05.04 |
| operator_regex_split_into_list | G8.05.05 |

**Result**: 100% coverage of all CreatiCode AI/NLP blocks

---

## END OF VISUAL BREAKDOWN
