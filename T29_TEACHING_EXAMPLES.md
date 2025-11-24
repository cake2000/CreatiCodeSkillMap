# T29 SPLIT SKILLS - TEACHING EXAMPLES
## How to Use the New Focused Skills in Practice

---

## EXAMPLE 1: Teaching ChatGPT Progressively

### OLD APPROACH (1 skill - overwhelming):
**T29.G4.05.02**: "Today we'll learn the ChatGPT block. It has parameters for prompt, result, mode, length, temperature, and session. Let me show you all of them..."

**Student Experience**:
- 😵 Confused by 6 parameters at once
- ❓ Unclear which parameters are essential vs optional
- 🤷 Can't remember what each parameter does
- 😰 Feels overwhelmed and gives up

---

### NEW APPROACH (5 skills - scaffolded):

#### **Lesson 1 (T29.G4.05.02.01)**: Understanding the Parameters
**Focus**: Overview without hands-on coding yet

**Teacher**: "Let's explore the ChatGPT block together. I'll open it and we'll look at each input."

**Activity**:
- Display the block on screen
- Point to each parameter
- Explain what each one does (without expecting mastery)
- Create a reference chart: prompt → what to ask, result → where answer goes, etc.

**Student Experience**:
- 👀 See the whole block layout
- 📝 Take notes on what parameters exist
- 🤔 Start to understand the block structure
- ✅ Feel oriented (not overwhelmed)

---

#### **Lesson 2 (T29.G4.05.02.02)**: First Request (Waiting Mode)
**Focus**: Get something working

**Teacher**: "Today we'll send our first ChatGPT request. We'll use just 3 parameters: prompt, result variable, and mode."

**Activity**:
```
ask [What's your prompt for ChatGPT?] and wait
set [myPrompt v] to (answer)
OpenAI ChatGPT: request (myPrompt) result [aiResponse v] mode [waiting v] length [100] temperature [1] session [new chat v]
say (aiResponse) for (5) seconds
```

**Key Teaching Points**:
- Use 'waiting' mode first (simpler)
- Use default values for length/temperature/session
- Focus on: Does it work? Do you get a response?

**Student Experience**:
- 🎉 Success! I got ChatGPT to respond!
- ✅ I understand prompt → result flow
- 💪 I can build on this

---

#### **Lesson 3 (T29.G4.05.02.03)**: Streaming Mode
**Focus**: Real-time responses

**Teacher**: "Now let's make responses appear word-by-word like you see on ChatGPT's website."

**Activity**:
```
ask [What's your prompt?] and wait
set [myPrompt v] to (answer)
OpenAI ChatGPT: request (myPrompt) result [aiResponse v] mode [streaming v] length [100] temperature [1] session [new chat v]
repeat until <(aiResponse) contains [✅]?>
  say (aiResponse)
end
```

**Key Teaching Points**:
- 'streaming' updates the variable continuously
- ✅ emoji signals completion
- Use repeat-until to show updates

**Student Experience**:
- 😮 Cool! It updates in real-time!
- ✅ I understand streaming vs waiting
- 🎯 I know when to use each mode

---

#### **Lesson 4 (T29.G4.05.02.04)**: Length Control
**Focus**: Token limits

**Teacher**: "Let's control how long the AI response is."

**Activity**:
- Try length [50] → short response
- Try length [200] → longer response
- Discuss: 100 tokens ≈ 75 words

**Student Experience**:
- 📏 I can control response length
- ✅ I understand tokens ≈ words
- 🎯 I know when short vs long is better

---

#### **Lesson 5 (T29.G4.05.02.05)**: Temperature
**Focus**: Creativity control

**Teacher**: "Let's control how creative or predictable ChatGPT is."

**Activity**:
- Try temperature [0] → factual, predictable
- Try temperature [0.5] → balanced
- Try temperature [1] → creative, varied

**Student Experience**:
- 🎨 I can make AI more creative or factual
- ✅ I understand the 0-1 scale
- 🎯 I know when to use low vs high temperature

---

### RESULT:
✅ Students master each parameter individually
✅ Each lesson builds on previous success
✅ No overwhelm - clear progression
✅ Students can mix and match parameters confidently

---

## EXAMPLE 2: Teaching Speech-to-Text Progressively

### OLD APPROACH (1 skill - confusing):
**T29.G6.06**: "Speech-to-text can use Azure or OpenAI Whisper. You can do single utterance or continuous recognition. There are 40+ languages. You can store the audio. Let me show you all of this..."

**Student Experience**:
- 😵 Too many options at once
- ❓ Azure vs OpenAI - which do I pick?
- 🤷 Single vs continuous - what's the difference?
- 😰 Gives up before trying anything

---

### NEW APPROACH (6 skills - step-by-step):

#### **Lesson 1 (T29.G6.06.01)**: Understanding Options
**Focus**: Conceptual overview

**Teacher**: "CreatiCode offers two speech recognition APIs: Azure and OpenAI Whisper. Both work similarly, but let's understand the differences."

**Activity**:
- Compare side-by-side demos
- Discuss: Both convert speech to text
- Note: Azure has more voice options for some languages
- Note: Whisper is newer, may be more accurate

**Student Experience**:
- 👀 I see both options
- ✅ I understand they're similar
- 🤔 I can choose based on needs

---

#### **Lesson 2 (T29.G6.06.02)**: First Speech Recognition
**Focus**: Get it working

**Teacher**: "Let's capture your voice and see it as text."

**Activity**:
```
say [Say something after the beep!] for (2) seconds
start recognizing speech in [English (United States) v] record as []
wait (3) seconds
end speech recognition
say (text from speech) for (5) seconds
```

**Key Teaching Points**:
- Start recognition → speak → end recognition → get text
- Use 'text from speech' reporter to get results

**Student Experience**:
- 🎉 My voice turned into text!
- ✅ I understand the start→end→get text flow
- 💪 Ready for more

---

#### **Lesson 3 (T29.G6.06.03)**: Language Selection
**Focus**: International support

**Teacher**: "Let's try recognition in different languages."

**Activity**:
- Try English (US)
- Try Spanish
- Try Chinese
- Compare accuracy

**Student Experience**:
- 🌍 I can use any language!
- ✅ I understand the dropdown
- 🎯 I can build multilingual projects

---

#### **Lesson 4 (T29.G6.06.04)**: Storing Audio
**Focus**: Replay capability

**Teacher**: "Let's save the audio so we can replay it."

**Activity**:
```
start recognizing speech in [English (United States) v] record as [myRecording]
wait (3) seconds
end speech recognition
say (text from speech) for (3) seconds
play sound [myRecording v] until done
```

**Student Experience**:
- 🔊 I saved and replayed my voice!
- ✅ I understand the SOUNDNAME parameter
- 🎯 I can build voice recording apps

---

#### **Lesson 5 (T29.G6.06.05)**: Continuous Recognition
**Focus**: Real-time capture

**Teacher**: "Let's capture speech in real-time as you speak."

**Activity**:
```
start continuous speech recognition in [English (United States) v] into list [speechList v]
say [Speak continuously. Current sentence shows at bottom of list.] for (3) seconds
wait (10) seconds
stop continuous speech recognition
say (join [You said] (length of [speechList v]) [sentences]) for (3) seconds
```

**Student Experience**:
- 🎙️ It captures everything I say!
- ✅ I understand continuous mode
- 🎯 I can build dictation apps

---

#### **Lesson 6 (T29.G6.06.06)**: Clear Results
**Focus**: Reset between captures

**Teacher**: "Let's clear old results before new recognition."

**Activity**:
```
clear speech text
say (text from speech) for (2) seconds  // Shows empty
start recognizing speech in [English (United States) v] record as []
wait (3) seconds
end speech recognition
say (text from speech) for (5) seconds  // Shows new text
```

**Student Experience**:
- 🧹 I can reset between captures!
- ✅ I understand when to clear
- 🎯 I can build multi-capture apps

---

### RESULT:
✅ Students master each feature individually
✅ Can combine features in advanced projects
✅ Understand when to use each mode/option
✅ Build progressively complex voice apps

---

## EXAMPLE 3: Teaching Parse Sentence Block

### OLD APPROACH (1 skill - overwhelming):
**T29.G5.06**: "The parse sentence block analyzes grammar. It outputs 7 columns: TEXT, LEMMA, TYPE, LABEL, HEAD, ID, DEPENDENCY. Let me explain all of them..."

**Student Experience**:
- 😵 7 columns?! What are these?
- ❓ What's a lemma? What's a dependency?
- 🤷 Too much linguistic terminology
- 😰 I just wanted to find nouns!

---

### NEW APPROACH (4 skills - focused):

#### **Lesson 1 (T29.G5.06.01)**: Block Structure
**Focus**: Overview of output

**Teacher**: "The parse sentence block analyzes grammar and puts results in a table."

**Activity**:
- Analyze: "The quick brown fox jumps."
- Look at the output table
- Count rows: 5 rows (one per word)
- Count columns: 7 columns
- Overview of what each column shows (no details yet)

**Student Experience**:
- 👀 I see the table structure
- ✅ I understand: 1 row per word
- 🤔 Ready to explore columns

---

#### **Lesson 2 (T29.G5.06.02)**: Finding Parts of Speech
**Focus**: TEXT and TYPE columns only

**Teacher**: "Let's find all the nouns in a sentence."

**Activity**:
```
analyze sentence [The quick brown fox jumps over the lazy dog] and write into table [grammar v]
set [nounList v] to []
repeat (length of table [grammar v]) times
  if <(get row (i) column [TYPE] from table [grammar v]) = [NOUN]> then
    add (get row (i) column [TEXT] from table [grammar v]) to [nounList v]
  end
end
say (join [Nouns:] (nounList)) for (5) seconds
```

**Key Teaching Points**:
- TEXT column = original word
- TYPE column = part of speech (NOUN, VERB, ADJ, etc.)
- Filter by TYPE to find specific word types

**Student Experience**:
- 🎯 I found all the nouns!
- ✅ I understand TEXT and TYPE columns
- 💪 I can find verbs, adjectives, etc.

---

#### **Lesson 3 (T29.G5.06.03)**: Finding Word Stems
**Focus**: LEMMA column only

**Teacher**: "Let's find the root form of words."

**Activity**:
- Input: "The dogs were running quickly to their homes"
- Find lemmas:
  - dogs → dog
  - were → be
  - running → run
  - quickly → quick
  - their → they
  - homes → home

**Student Experience**:
- 🌱 I understand lemmatization!
- ✅ Words get reduced to roots
- 🎯 Useful for word frequency counting

---

#### **Lesson 4 (T29.G5.06.04)**: Grammatical Roles
**Focus**: LABEL column only

**Teacher**: "Let's find the subject and object of a sentence."

**Activity**:
- Input: "The cat chased the mouse"
- Find LABEL = "nsubj" (subject) → "cat"
- Find LABEL = "dobj" (direct object) → "mouse"

**Student Experience**:
- 🎯 I found who did what!
- ✅ I understand grammatical roles
- 💪 I can analyze sentence structure

---

### RESULT:
✅ Students master one column at a time
✅ Build understanding progressively
✅ Can combine columns for complex analysis
✅ Not overwhelmed by linguistic terminology

---

## EXAMPLE 4: Teaching Regex Blocks

### OLD APPROACH (1 skill - intimidating):
**T29.G8.05**: "Regex is powerful pattern matching. There are 5 blocks: test, match, search, replace, split. Let me show you how to use them with email patterns, phone numbers, URLs..."

**Student Experience**:
- 😵 5 blocks + complex patterns = overwhelmed
- ❓ When do I use test vs match vs search?
- 🤷 Regex syntax looks like gibberish
- 😰 This is too advanced for me

---

### NEW APPROACH (5 skills - one block at a time):

#### **Lesson 1 (T29.G8.05.01)**: Test Block
**Focus**: Yes/no pattern checking

**Teacher**: "Let's check if text matches a pattern."

**Activity**:
```
ask [Enter a word:] and wait
if <regex [^[A-Z]] test (answer)> then
  say [Starts with capital!] for (2) seconds
else
  say [Doesn't start with capital] for (2) seconds
end
```

**Student Experience**:
- ✅ I can check patterns!
- 🎯 Returns true/false
- 💪 Useful for validation

---

#### **Lesson 2 (T29.G8.05.02)**: Match Block
**Focus**: Extracting patterns

**Teacher**: "Let's extract all numbers from text."

**Activity**:
```
set [text v] to [My phone is 555-1234 and code is 9876]
regex [\d+] flag [g] match (text) into list [numbers v]
say (join [Found numbers:] (numbers)) for (3) seconds
// Output: Found numbers: 555 1234 9876
```

**Student Experience**:
- 🎯 I extracted all numbers!
- ✅ 'g' flag gets all matches
- 💪 Useful for data extraction

---

#### **Lesson 3 (T29.G8.05.03)**: Search Block
**Focus**: Finding position

**Teacher**: "Let's find where a pattern appears."

**Activity**:
```
set [text v] to [Hello World]
set [pos v] to (regex [W] search (text))
say (join [Found 'W' at position] (pos)) for (2) seconds
// Output: Found 'W' at position 7
```

**Student Experience**:
- 📍 I found the position!
- ✅ Returns index (1-based)
- 💪 Useful for parsing

---

#### **Lesson 4 (T29.G8.05.04)**: Replace Block
**Focus**: Substitution

**Teacher**: "Let's replace all digits with 'X'."

**Activity**:
```
set [text v] to [My PIN is 1234 and code is 5678]
set [hidden v] to (regex [\d] flag [g] replace (text) with [X])
say (hidden) for (3) seconds
// Output: My PIN is XXXX and code is XXXX
```

**Student Experience**:
- 🔒 I censored numbers!
- ✅ 'g' flag replaces all
- 💪 Useful for data masking

---

#### **Lesson 5 (T29.G8.05.05)**: Split Block
**Focus**: Advanced tokenization

**Teacher**: "Let's split on multiple delimiters."

**Activity**:
```
set [text v] to [apple,banana;cherry orange]
regex [,|;| ] flag [g] split (text) into list [fruits v]
// Result: [apple, banana, cherry, orange]
```

**Student Experience**:
- ✂️ I split on any delimiter!
- ✅ Regex patterns in split
- 💪 Better than simple split

---

### RESULT:
✅ Students learn one block at a time
✅ Build regex knowledge progressively
✅ Can combine blocks for complex tasks
✅ Not intimidated by advanced features

---

## KEY TEACHING PRINCIPLES

### 1. **Introduce → Practice → Extend**
- Introduce: Show the feature
- Practice: Students use it in simple context
- Extend: Add complexity progressively

### 2. **Success Before Complexity**
- Get something working first
- Add features one at a time
- Celebrate each small win

### 3. **Clear Learning Objectives**
- "Today we'll learn streaming mode"
- NOT "Today we'll learn all ChatGPT parameters"

### 4. **Build Prerequisites Explicitly**
- "Last time we learned waiting mode. Today we'll compare it to streaming mode."
- Students see connections between skills

### 5. **Allow Specialization**
- Students don't need ALL skills
- Some may focus on speech-to-text
- Others may focus on ChatGPT
- All have solid foundation

---

## ASSESSMENT EXAMPLES

### Micro-Assessments (Per Skill):

**T29.G4.05.02.03 (Streaming Mode)**:
✅ Student can set mode to 'streaming'
✅ Student uses repeat-until with ✅ emoji check
✅ Student explains streaming vs waiting

**T29.G6.06.03 (Language Selection)**:
✅ Student can select different languages
✅ Student tests recognition in 2+ languages
✅ Student discusses when to use each language

**T29.G8.05.02 (Match Block)**:
✅ Student uses regex match block
✅ Student uses 'g' flag correctly
✅ Student extracts patterns into list

### Project-Based Assessment:

**Voice-Controlled Chatbot** (Combines multiple skills):
- Uses T29.G6.06.02 (speech recognition)
- Uses T29.G4.05.02.02 (ChatGPT request)
- Uses T29.G6.07.01 (text-to-speech)
- Demonstrates mastery of 3 separate skills

---

## CONCLUSION

Split skills enable:
✅ **Progressive mastery** instead of overwhelm
✅ **Clear objectives** for each lesson
✅ **Targeted assessment** of specific features
✅ **Student confidence** through incremental success
✅ **Flexible pacing** - spend more time where needed

The "one skill = one feature" principle transforms complex topics into learnable progressions.

---

## END OF TEACHING EXAMPLES
