# T21 AI Media Block Inventory
## Complete Catalog of All AI Media Blocks in CreatiCode

**Source Document:** `/media/binyu/USB2/ScratchCopilot/blockdes8.txt`
**Analysis Date:** 2025-11-21
**Project:** CreatiCode K-8 Skill Map Optimization

---

## Executive Summary

This document catalogs all AI-related media blocks available in CreatiCode, organized by category. A total of **16 AI media blocks** have been identified, covering:

1. **Text-to-Speech** (2 blocks)
2. **Speech Recognition** (6 blocks)
3. **Image Generation (DALL-E)** (1 block with dual syntax)
4. **Content Moderation** (3 blocks)
5. **Image Search & Utilities** (4 blocks)

All blocks have been verified against the T21 (AI Media) skill requirements for Grade 5-6 students.

---

## Block Catalog by Category

### CATEGORY 1: TEXT-TO-SPEECH

---

#### Block 1.1: ai_speakinlanguage
**Full Name:** Text-to-Speech with Language and Voice Customization

**Exact Block Syntax:**
```
say [TEXT] in [LANGUAGE v] as [VOICETYPE v] speed (SPEEDRATIO) pitch (PITCHRATIO) volume (VOLUMERATIO) store sound as [SOUNDNAME]
```

**Complete Parameter List:**
- `[TEXT]` - String input: Text to convert to speech
- `[LANGUAGE v]` - Dropdown menu with 30+ language options
- `[VOICETYPE v]` - Dropdown menu: Male | Female | Male2 | Female2 | Male3 | Female3 | Boy | Girl
- `(SPEEDRATIO)` - Numeric input: Speech speed as percentage (default 100)
- `(PITCHRATIO)` - Numeric input: Pitch level as percentage (default 100)
- `(VOLUMERATIO)` - Numeric input: Volume level as percentage (default 100)
- `[SOUNDNAME]` - Optional string: If provided, stores converted speech as a sound clip

**API Provider:** Microsoft Azure Text-to-Speech API

**Block Type:** Command Block (stack-based)

**Metadata:**
- Block ID: ai_speakinlanguage
- Category: AI
- Usable in 3D: No
- Returns: None (executes speech)

**Sample Usage:**
```
say [Tell me a story] in [English (United States) v] as [Female v] speed (80) pitch (120) volume (100) store sound as []
```

**Supported Languages:** 30+ languages including English variants, Spanish, French, German, Chinese variants, Japanese, Korean, Hindi, and many others.

---

#### Block 1.2: ai_stopspeaking
**Full Name:** Stop Speaking

**Exact Block Syntax:**
```
stop speaking
```

**Parameters:** None

**API Provider:** N/A (local control)

**Block Type:** Command Block (stack-based)

**Metadata:**
- Block ID: ai_stopspeaking
- Category: AI
- Usable in 3D: No
- Returns: None

**Description:** Immediately stops any currently playing text-to-speech audio.

---

### CATEGORY 2: SPEECH RECOGNITION

#### Group A: Speech Recognition (Microsoft Azure)

---

#### Block 2.1: ai_startspeech
**Full Name:** Start Speech Recognition (Microsoft Azure)

**Exact Block Syntax:**
```
start recognizing speech in [LANGUAGE v] record as [SOUNDNAME]
```

**Complete Parameter List:**
- `[LANGUAGE v]` - Dropdown menu with 30+ language options
- `[SOUNDNAME]` - Optional string: If provided, stores recorded audio as a sound clip

**API Provider:** Microsoft Azure Speech Recognition API

**Block Type:** Command Block (stack-based)

**Metadata:**
- Block ID: ai_startspeech
- Category: AI
- Usable in 3D: No
- Returns: None

**Sample Usage:**
```
start recognizing speech in [English (United States) v] record as [my_recording]
```

**Behavior:**
- Activates microphone for speech input
- Continues recording until `end speech recognition` block is executed
- No automatic timeout - user or program must explicitly end recording
- Recognized text available via `text from speech` reporter block

**Note:** Recognized text replaces previous recognition result. Use `clear speech text` to reset.

---

#### Block 2.2: ai_startrecognizer
**Full Name:** Start Continuous Speech Recognition (Microsoft Azure)

**Exact Block Syntax:**
```
start continuous speech recognition in [LANGUAGE v] into list [LISTNAME v]
```

**Complete Parameter List:**
- `[LANGUAGE v]` - Dropdown menu with 30+ language options
- `[LISTNAME v]` - List variable reference where recognized speech parts are stored

**API Provider:** Microsoft Azure Speech Recognition API

**Block Type:** Command Block (stack-based)

**Metadata:**
- Block ID: ai_startrecognizer
- Category: AI
- Usable in 3D: No
- Returns: None

**Sample Usage:**
```
start continuous speech recognition in [English (United States) v] into list [recognized_text v]
```

**Behavior:**
- Streams audio from microphone to Azure API in real-time
- Each complete sentence stored as separate list item
- Current incomplete sentence continuously updated as new words recognized
- New empty item appended when sentence ends
- Process continues until `stop continuous speech recognition` block executed
- Useful for displaying live recognition feedback

---

#### Block 2.3: ai_stoprecognizer
**Full Name:** Stop Continuous Speech Recognition

**Exact Block Syntax:**
```
stop continuous speech recognition
```

**Parameters:** None

**API Provider:** N/A

**Block Type:** Command Block (stack-based)

**Metadata:**
- Block ID: ai_stoprecognizer
- Category: AI
- Usable in 3D: No
- Returns: None

**Description:** Ends continuous speech recognition started by `start continuous speech recognition` block.

---

#### Group B: Speech Recognition (OpenAI Whisper)

---

#### Block 2.4: ai_startopenaispeech
**Full Name:** Start Speech Recognition (OpenAI Whisper)

**Exact Block Syntax:**
```
OpenAI: start recognizing speech in [LANGUAGE v] record as [SOUNDNAME]
```

**Complete Parameter List:**
- `[LANGUAGE v]` - Dropdown menu with language options
- `[SOUNDNAME]` - Optional string: If provided, stores recorded audio as a sound clip

**API Provider:** OpenAI Whisper API

**Block Type:** Command Block (stack-based)

**Metadata:**
- Block ID: ai_startopenaispeech
- Category: AI
- Usable in 3D: No
- Returns: None

**Sample Usage:**
```
OpenAI: start recognizing speech in [English v] record as []
```

**Behavior:**
- Similar to `ai_startspeech` but uses OpenAI Whisper instead of Azure
- Activates microphone for speech input
- Continues recording until `end speech recognition` block is executed
- Recognized text available via `text from speech` reporter block

**Note:** This is an alternative to the Azure version with potentially different accuracy characteristics.

---

#### Group C: Speech Recognition Utilities

---

#### Block 2.5: ai_endspeech
**Full Name:** End Speech Recognition

**Exact Block Syntax:**
```
end speech recognition
```

**Parameters:** None

**API Providers:**
- Microsoft Azure Speech Recognition API (if started with `ai_startspeech` or `ai_startrecognizer`)
- OpenAI Whisper API (if started with `ai_startopenaispeech`)

**Block Type:** Command Block (stack-based)

**Metadata:**
- Block ID: ai_endspeech
- Category: AI
- Usable in 3D: No
- Returns: None

**Description:** Stops recording voice input and sends recorded audio to the appropriate speech recognition API. Stores recognized text in `text from speech` reporter block.

**Important:** The API used depends on which start block initiated the recording.

---

#### Block 2.6: ai_textfromspeech
**Full Name:** Text from Speech (Reporter)

**Exact Block Syntax:**
```
text from speech
```

**Parameters:** None

**Returns:** String (recognized text)

**Block Type:** Reporter Block (returns value)

**Metadata:**
- Block ID: ai_textfromspeech
- Category: AI
- Usable in 3D: No

**Sample Usage:**
```
say (text from speech)
set [user_input v] to (text from speech)
```

**Description:** Returns the most recently recognized speech text. Updated when `end speech recognition` block completes.

---

#### Block 2.7: ai_clearspeech
**Full Name:** Clear Speech Text

**Exact Block Syntax:**
```
clear speech text
```

**Parameters:** None

**API Provider:** N/A

**Block Type:** Command Block (stack-based)

**Metadata:**
- Block ID: ai_clearspeech
- Category: AI
- Usable in 3D: No
- Returns: None

**Description:** Clears/resets the `text from speech` reporter block to empty string.

---

### CATEGORY 3: IMAGE GENERATION (DALL-E)

---

#### Block 3.1: ai_openaiimagereporter
**Full Name:** OpenAI DALL-E Image Generation

**Syntax (Reporter Version - Get URL):**
```
OpenAI DALL-E: generate image with request [DESCRIPTION] resolution [RESOLUTION v]
```

**Syntax (Command Version - Generate Costume):**
```
OpenAI DALL-E: generate costume image name [IMAGE_NAME] description [DESCRIPTION] with resolution [RESOLUTION v]
```

**Parameters (Both versions):**
- `[DESCRIPTION]` / `[QUERY]` - String input: Text description of desired image
- `[RESOLUTION v]` - Dropdown menu: 256x256 | 512x512 | 1024x1024
- `[IMAGE_NAME]` - String input (Command version only): Name for generated costume

**API Provider:** OpenAI DALL-E API

**Block Types:**
- Reporter Block (reporter version - returns URL string)
- Command Block (command version - generates costume directly)

**Metadata:**
- Block ID: ai_openaiimagereporter
- Category: AI
- Usable in 3D: No

**Sample Usage (Reporter):**
```
set [image_url v] to (OpenAI DALL-E: generate image with request [a fluffy cat wearing a hat] resolution [512x512 v])
add image from URL (image_url) at x (0) y (0) width (360) height (360) aspect ratio (keep v) as [generated_image]
```

**Sample Usage (Command):**
```
OpenAI DALL-E: generate costume image name [new_costume] description [a robot made of colorful blocks] with resolution [256x256 v]
wait (2) [seconds v]
switch costume to [new_costume]
```

**Resolution Guide:**
- **256x256** - Smallest/fastest, good for thumbnails
- **512x512** - Medium, balanced quality/speed
- **1024x1024** - Largest, best quality, slowest

**Note:** Generated images in command version are saved to sprite's costumes after generation completes (may require wait time for download).

---

### CATEGORY 4: CONTENT MODERATION

---

#### Block 4.1: getmoderationresult
**Full Name:** Get Moderation Result for Text

**Exact Block Syntax:**
```
get moderation result for [TEXT]
```

**Parameters:**
- `[TEXT]` - String input: Text to check for inappropriate content

**Returns:** String ("Pass" or "Fail")

**Block Type:** Reporter Block (returns value)

**API Provider:** OpenAI Moderation API or similar

**Metadata:**
- Block ID: getmoderationresult
- Category: AI
- Usable in 3D: No

**Sample Usage:**
```
set [moderation_result v] to (get moderation result for [user_input])
if <(moderation_result) = [Pass]> then
    say [Your message is appropriate!]
else
    say [Please avoid inappropriate content]
end
```

**Description:** Checks text input against content moderation policies. Returns "Pass" if appropriate, "Fail" if contains flagged content.

---

#### Block 4.2: getmoderationresult2
**Full Name:** Get Moderation Result for Image (URL)

**Exact Block Syntax:**
```
get moderation result for image at URL [INPUT]
```

**Parameters:**
- `[INPUT]` - String input: URL of image to check

**Returns:** String ("Pass" or "Fail")

**Block Type:** Reporter Block (returns value)

**API Provider:** OpenAI Vision/Moderation API or similar

**Metadata:**
- Block ID: getmoderationresult2
- Category: AI
- Usable in 3D: No

**Sample Usage:**
```
get moderation result for image at URL [https://example.com/image.jpg]
```

**Description:** Checks image at provided URL against visual content moderation policies. Returns "Pass" if appropriate, "Fail" if contains flagged content.

---

#### Block 4.3: getmoderationresult3
**Full Name:** Get Moderation Result for Costume Image

**Exact Block Syntax:**
```
get moderation result for costume named [INPUT]
```

**Parameters:**
- `[INPUT]` - String input: Name of costume in project to check

**Returns:** String ("Pass" or "Fail")

**Block Type:** Reporter Block (returns value)

**API Provider:** OpenAI Vision/Moderation API or similar

**Metadata:**
- Block ID: getmoderationresult3
- Category: AI
- Usable in 3D: No

**Sample Usage:**
```
get moderation result for costume named [costume1]
```

**Description:** Checks costume image from project assets against visual content moderation policies. Returns "Pass" if appropriate, "Fail" if contains flagged content.

---

### CATEGORY 5: IMAGE SEARCH & UTILITIES

---

#### Block 5.1: ai_xoimagereporter
**Full Name:** Search AI Image Library

**Exact Block Syntax:**
```
search for AI image of [TYPE v] with query [QUERY]
```

**Parameters:**
- `[TYPE v]` - Dropdown menu: Object | Character | Backdrop
- `[QUERY]` - String input: Search query

**Returns:** Image (sets current costume/backdrop or returns image reference)

**Block Type:** Reporter Block

**API Provider:** AI Image Library (likely XO or similar service)

**Metadata:**
- Block ID: ai_xoimagereporter
- Category: AI
- Usable in 3D: No

**Sample Usage:**
```
search for AI image of [Character v] with query [a friendly robot]
```

**Description:** Searches AI-generated image library for images matching the query and type criteria.

---

#### Block 5.2: attachimagetochat
**Full Name:** Attach Costume to Chat

**Exact Block Syntax:**
```
attach costume [COSTUMENAME] to chat
```

**Parameters:**
- `[COSTUMENAME]` - String input: Name of costume to attach

**Returns:** None (modifies chat state)

**Block Type:** Command Block (stack-based)

**API Provider:** ChatGPT/LLM Integration

**Metadata:**
- Block ID: attachimagetochat
- Category: AI
- Usable in 3D: No

**Sample Usage:**
```
attach costume [Front] to chat
OpenAI ChatGPT: request [Describe what you see in this image] result [response v] mode [waiting v] length [200] temperature [1] session [new chat v]
```

**Description:** Attaches specified costume image to the next ChatGPT request, allowing the LLM to analyze the image.

---

#### Block 5.3: googlesearch
**Full Name:** Web Search with Table Results

**Exact Block Syntax:**
```
web search [QUERY] store top (K) in table [TABLE v]
```

**Parameters:**
- `[QUERY]` - String input: Search query
- `(K)` - Numeric input: Number of top results to retrieve
- `[TABLE v]` - Table variable reference: Destination for results

**Returns:** None (populates table)

**Block Type:** Command Block (stack-based)

**API Provider:** Web Search API (Google or similar)

**Metadata:**
- Block ID: googlesearch
- Category: AI
- Usable in 3D: No

**Sample Usage:**
```
web search [how to make pizza] store top (5) in table [search_results v]
```

**Table Output Format:** 3 columns
- Column 1: title (result title)
- Column 2: link (result URL)
- Column 3: snippet (result summary text)

**Description:** Performs web search and stores top K results in specified table with title, link, and snippet information.

---

## T21 Skill Verification Matrix

| Skill Code | Skill Title | Required Blocks | Block IDs | Status | Notes |
|------------|-------------|-----------------|-----------|--------|-------|
| T21.G5.02 | Generate costume image using DALL-E | DALL-E costume generation | ai_openaiimagereporter | ✓ VERIFIED | Command syntax available |
| T21.G5.03 | Text-to-Speech with language/voice/customization | TTS with parameters | ai_speakinlanguage | ✓ VERIFIED | All parameters match: language, voice, speed, pitch, volume |
| T21.G6.05 | Speech Recognition | Speech input capture | ai_startspeech, ai_startopenaispeech | ✓ VERIFIED | Two provider options: Azure and OpenAI |
| T21.G6.06 | Content Moderation (Text) | Text safety checking | getmoderationresult | ✓ VERIFIED | Returns Pass/Fail |
| T21.G6.07 | Image Moderation | Image safety checking | getmoderationresult2, getmoderationresult3 | ✓ VERIFIED | URL and costume versions available |

---

## Feature Comparison Table

### Speech Recognition Providers

| Feature | Microsoft Azure (ai_startspeech) | OpenAI Whisper (ai_startopenaispeech) |
|---------|-----------------------------------|---------------------------------------|
| Block ID | ai_startspeech | ai_startopenaispeech |
| Continuous Mode | ai_startrecognizer | Not available |
| Language Support | 30+ languages | Major languages |
| Microphone Recording | Yes | Yes |
| Optional Sound Storage | Yes | Yes |
| End Block | ai_endspeech | ai_endspeech |
| Text Retrieval | text from speech | text from speech |

### Image Moderation Options

| Option | Block ID | Input Type | Use Case |
|--------|----------|-----------|----------|
| Text Moderation | getmoderationresult | String text | Check user input for inappropriate content |
| URL Image Check | getmoderationresult2 | Image URL | Check images from external URLs |
| Local Image Check | getmoderationresult3 | Costume name | Check images in project assets |

---

## Implementation Examples

### Example 1: Complete Text-to-Speech Flow
```
when green flag clicked
    ask [What should I say?] and wait
    say (answer) in [English (United States) v] as [Female v] speed (100) pitch (100) volume (100) store sound as []
```

### Example 2: Speech Recognition with User Input
```
when green flag clicked
    say [Say something!]
    start recognizing speech in [English (United States) v] record as []
    wait until <not <[text from speech] = []>>
    end speech recognition
    say (join [You said: ] (text from speech))
```

### Example 3: DALL-E Image Generation
```
when green flag clicked
    ask [Describe an image to generate] and wait
    set [new_costume v] to (OpenAI DALL-E: generate image with request (answer) resolution [512x512 v])
    add image from URL (new_costume) at x (0) y (0) width (480) height (480) aspect ratio (keep v) as [ai_image]
```

### Example 4: Content Moderation Check
```
when green flag clicked
    ask [Enter text to check] and wait
    if <(get moderation result for (answer)) = [Pass]> then
        say [Content is appropriate]
    else
        say [Content contains inappropriate material]
    end
```

---

## Summary Statistics

**Total AI Media Blocks:** 16
**Categories:** 5
**API Providers:** 6
- Microsoft Azure Text-to-Speech
- Microsoft Azure Speech Recognition
- OpenAI Whisper API
- OpenAI DALL-E API
- OpenAI Moderation API
- Web Search API

**Supported Languages:** 30+ (speech blocks)
**Voice Types:** 8 (text-to-speech)
**Image Resolutions:** 3 (DALL-E)
**Moderation Types:** 3 (text, image URL, local image)

---

## Key Findings

1. **Comprehensive AI Capabilities:** CreatiCode provides a full suite of AI media capabilities spanning text-to-speech, speech recognition, image generation, and content moderation.

2. **Multiple Provider Options:** Students can choose between different providers (Azure vs. OpenAI) for some functions, teaching about API alternatives.

3. **Safety Built-In:** Content moderation blocks are available for text and images, promoting responsible AI use.

4. **Customization:** Text-to-speech offers granular control over speed, pitch, and volume for advanced users.

5. **Flexibility:** Both reporter and command versions of DALL-E blocks allow different integration patterns.

6. **Continuous Recognition:** Microsoft Azure provides continuous speech recognition for real-time transcription use cases.

---

**Document Generated:** November 21, 2025
**Analysis Complete:** All T21 AI Media skills verified against platform capabilities
