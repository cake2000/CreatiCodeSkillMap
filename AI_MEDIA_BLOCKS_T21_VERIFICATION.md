# AI Media Blocks (T21) Verification Report

## Source
Analysis of `/media/binyu/USB2/ScratchCopilot/blockdes8.txt`

---

## 1. Text-to-Speech Blocks

### Block: ai_speakinlanguage
**Exact Syntax:**
```
say [TEXT] in [LANGUAGE v] as [VOICETYPE v] speed (SPEEDRATIO) pitch (PITCHRATIO) volume (VOLUMERATIO) store sound as [SOUNDNAME]
```

**Parameters:**
- `[TEXT]`: Input text to convert to speech
- `[LANGUAGE v]`: Dropdown menu with languages (English US, Spanish, French, Chinese variants, German, Japanese, Korean, etc.)
- `[VOICETYPE v]`: Male, Female, Male2, Female2, Male3, Female3, Boy, Girl
- `(SPEEDRATIO)`: Percentage value for speech speed (default 100)
- `(PITCHRATIO)`: Percentage value for pitch (default 100)
- `(VOLUMERATIO)`: Percentage value for volume (default 100)
- `[SOUNDNAME]`: Optional - stores converted speech as sound clip if provided

**API:** Microsoft Azure Text-to-Speech API

**Block ID:** ai_speakinlanguage
**Category:** AI
**Can be used for 3D:** false

---

### Block: ai_stopspeaking
**Exact Syntax:**
```
stop speaking
```

**Description:** Stops the AI speech from the text-to-speech block

**Block ID:** ai_stopspeaking
**Category:** AI
**Can be used for 3D:** false

---

## 2. Speech Recognition Blocks (Microsoft Azure)

### Block: ai_startspeech
**Exact Syntax:**
```
start recognizing speech in [LANGUAGE v] record as [SOUNDNAME]
```

**Parameters:**
- `[LANGUAGE v]`: Dropdown menu with major languages (English US, Spanish, French, Chinese variants, German, Japanese, Korean, etc.)
- `[SOUNDNAME]`: Optional - stores recorded sound as sound clip if provided

**API:** Microsoft Azure Speech Recognition API

**Description:** Turns on microphone to start recording voice input. Recognition ends only when 'end speech recognition' block runs.

**Block ID:** ai_startspeech
**Category:** AI
**Can be used for 3D:** false

---

### Block: ai_startrecognizer
**Exact Syntax:**
```
start continuous speech recognition in [LANGUAGE v] into list [LISTNAME v]
```

**Parameters:**
- `[LANGUAGE v]`: Dropdown menu with major languages (English US, Spanish, French, Chinese variants, German, Japanese, Korean, etc.)
- `[LISTNAME v]`: List variable where recognized speech parts are stored

**API:** Microsoft Azure Speech Recognition API

**Description:** Starts continuous speech recognition from microphone. Each sentence stored as new item in list. Current sentence continuously updated as words recognized.

**Block ID:** ai_startrecognizer
**Category:** AI
**Can be used for 3D:** false

---

### Block: ai_stoprecognizer
**Exact Syntax:**
```
stop continuous speech recognition
```

**Description:** Stops continuous speech recognition

**Block ID:** ai_stoprecognizer
**Category:** AI
**Can be used for 3D:** false

---

## 3. Speech Recognition Blocks (OpenAI Whisper)

### Block: ai_startopenaispeech
**Exact Syntax:**
```
OpenAI: start recognizing speech in [LANGUAGE v] record as [SOUNDNAME]
```

**Parameters:**
- `[LANGUAGE v]`: Dropdown menu with languages (English, Chinese, Spanish Castilian, French, German, Hindi, Japanese, Korean, etc.)
- `[SOUNDNAME]`: Optional - stores recorded sound as sound clip if provided

**API:** OpenAI Whisper API

**Description:** Turns on microphone to start recording voice input for OpenAI Whisper API recognition. Recognition ends only when 'end speech recognition' block runs.

**Block ID:** ai_startopenaispeech
**Category:** AI
**Can be used for 3D:** false

---

## 4. Speech Recognition Utility Blocks

### Block: ai_endspeech
**Exact Syntax:**
```
end speech recognition
```

**Description:** Stops recording voice input and sends recorded speech to speech recognition API. Stores recognized text in 'text from speech' reporter block. API can be either Microsoft Azure or OpenAI Whisper depending on which start block was used.

**Block ID:** ai_endspeech
**Category:** AI
**Can be used for 3D:** false

---

### Block: ai_textfromspeech
**Exact Syntax:**
```
text from speech
```

**Description:** Reporter block that returns the text recognized from speech

**Block ID:** ai_textfromspeech
**Category:** AI
**Can be used for 3D:** false

---

### Block: ai_clearspeech
**Exact Syntax:**
```
clear speech text
```

**Description:** Clears the content of the 'text from speech' block

**Block ID:** ai_clearspeech
**Category:** AI
**Can be used for 3D:** false

---

## 5. Image Generation Blocks (OpenAI DALL-E)

### Block: ai_openaiimagereporter

**Syntax (Reporter version):**
```
OpenAI DALL-E: generate image with request [DESCRIPTION] resolution [RESOLUTION v]
```

**Syntax (Command version):**
```
OpenAI DALL-E: generate costume image name [IMAGE_NAME] description [DESCRIPTION] with resolution [RESOLUTION v]
```

**Parameters:**
- `[DESCRIPTION]` / `[QUERY]`: Text description of image to generate
- `[RESOLUTION v]`: Dropdown menu with options: 256x256, 512x512, 1024x1024
- `[IMAGE_NAME]`: Name for the generated costume image (command version only)

**API:** OpenAI DALL-E API

**Block ID:** ai_openaiimagereporter
**Category:** AI
**Can be used for 3D:** false

**Usage Examples:**
```
Reporter version:
set [image URL v] to (OpenAI DALL-E: generate image with request [a dog] with resolution [256x256 v])

Command version:
OpenAI DALL-E: generate costume image name [image1] description [answer] with resolution [256x256 v]
```

---

## 6. Content Moderation Blocks

### Block: getmoderationresult
**Exact Syntax:**
```
get moderation result for [TEXT]
```

**Parameters:**
- `[TEXT]`: Text input to check

**Returns:** Pass or Fail

**Description:** Reporter block that uses AI moderation to check input

**Block ID:** getmoderationresult
**Category:** AI
**Can be used for 3D:** false

**Usage Example:**
```
get moderation result for [hell]
```

---

### Block: getmoderationresult2
**Exact Syntax:**
```
get moderation result for image at URL [INPUT]
```

**Parameters:**
- `[INPUT]`: URL of image to check

**Returns:** Pass or Fail

**Description:** Reporter block that uses AI moderation to check the image at given URL

**Block ID:** getmoderationresult2
**Category:** AI
**Can be used for 3D:** false

**Usage Example:**
```
get moderation result for image at URL [https://xxx]
```

---

### Block: getmoderationresult3
**Exact Syntax:**
```
get moderation result for costume named [INPUT]
```

**Parameters:**
- `[INPUT]`: Name of costume to check

**Returns:** Pass or Fail

**Description:** Reporter block that uses AI moderation to check the given costume image

**Block ID:** getmoderationresult3
**Category:** AI
**Can be used for 3D:** false

**Usage Example:**
```
get moderation result for costume named [c1]
```

---

## 7. Other AI Media-Related Blocks

### Block: ai_xoimagereporter
**Exact Syntax:**
```
search for AI image of [TYPE v] with query [QUERY]
```

**Parameters:**
- `[TYPE v]`: Dropdown menu with options: Object, Character, Backdrop
- `[QUERY]`: Search query string

**Description:** Searches for new image from AI image library using given query

**Block ID:** ai_xoimagereporter
**Category:** AI
**Can be used for 3D:** false

---

### Block: attachimagetochat
**Exact Syntax:**
```
attach costume [COSTUMENAME] to chat
```

**Parameters:**
- `[COSTUMENAME]`: Name of costume to attach

**Description:** Finds costume with given name and sends it as part of the next ChatGPT request

**Block ID:** attachimagetochat
**Category:** AI
**Can be used for 3D:** false

---

### Block: googlesearch
**Exact Syntax:**
```
web search [QUERY] store top (K) in table [TABLE v]
```

**Parameters:**
- `[QUERY]`: Search query string
- `(K)`: Number of top results to store
- `[TABLE v]`: Table variable to store results

**Returns:** Table with 3 columns: title, link, snippet

**Description:** Runs a web search and stores top K results

**Block ID:** googlesearch
**Category:** AI
**Can be used for 3D:** false

**Usage Example:**
```
web search [price of MSFT stock today] store top (3) in table [result_table v]
```

---

## T21 Skills Verification Summary

### Verified Blocks for T21 Skills:

| T21 Skill | Required Block | Block ID | Status |
|-----------|----------------|----------|--------|
| T21.G5.02 | OpenAI DALL-E: generate costume image | ai_openaiimagereporter | ✓ VERIFIED |
| T21.G5.03 | say [TEXT] in [LANGUAGE] as [VOICETYPE] speed () pitch () volume () | ai_speakinlanguage | ✓ VERIFIED |
| T21.G6.05 | Speech recognition | ai_startspeech, ai_startopenaispeech, ai_startrecognizer | ✓ VERIFIED |
| T21.G6.06 | Content moderation | getmoderationresult | ✓ VERIFIED |
| T21.G6.07 | Image moderation | getmoderationresult2, getmoderationresult3 | ✓ VERIFIED |

### Additional AI Media Blocks Available:
- Text-to-speech utilities: ai_stopspeaking
- Speech recognition utilities: ai_endspeech, ai_textfromspeech, ai_clearspeech, ai_stoprecognizer
- Image generation alternatives: ai_openaiimagereporter (reporter version)
- Image search: ai_xoimagereporter
- Chat integration: attachimagetochat
- Web search: googlesearch

---

## Notes

1. **Language Support:** Most speech-related blocks support 20+ languages including major languages (English, Spanish, French, German, Chinese variants, Japanese, Korean, Hindi, etc.)

2. **Voice Options:** Text-to-speech supports 8 voice types with varying language support

3. **Resolution Options:** DALL-E blocks support 3 resolution options: 256x256, 512x512, 1024x1024

4. **Customization:** Text-to-speech allows speed, pitch, and volume customization via percentage values

5. **Optional Sound Storage:** Both speech recognition and text-to-speech blocks can optionally store audio as sound clips

6. **API Providers:**
   - Text-to-speech: Microsoft Azure
   - Speech recognition (standard): Microsoft Azure
   - Speech recognition (alternative): OpenAI Whisper
   - Image generation: OpenAI DALL-E
   - Image search: XO (or similar AI image library)

---

**Report Generated:** Based on blockdes8.txt analysis
**File Path:** /media/binyu/USB2/ScratchCopilot/blockdes8.txt
