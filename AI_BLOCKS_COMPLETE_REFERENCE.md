# COMPREHENSIVE AI BLOCKS ANALYSIS - CreatiCode Platform
## Extracted from blockdes8.txt - Complete Reference for T24 Skills Verification

**Total AI Category Blocks: 43**

---

## CATEGORY 1: SPEECH RECOGNITION (Speech-to-Text)

### Block ID: ai_startspeech
- **Syntax:** `start recognizing speech in [LANGUAGE v] record as [SOUNDNAME]`
- **Usage:** `start recognizing speech in [English (United States) v] record as []`
- **Quick Description:** Turn on microphone to start recording voice input to prepare for recognition in the specified LANGUAGE. Uses Microsoft Azure API.
- **Full Description:** Supports all major languages (English US/UK, Spanish, French, Chinese Mandarin/Taiwanese/Cantonese, German, Japanese, Danish, Filipino, Finnish, Greek, Hindi, Hungarian, Indonesian, Irish, Italian, Javanese, Korean, Arabic, etc.). Optional SOUNDNAME parameter stores recorded sound. Speech recognition ends when 'end speech recognition' block runs.

### Block ID: ai_startopenaispeech
- **Syntax:** `OpenAI: start recognizing speech in [LANGUAGE v] record as [SOUNDNAME]`
- **Usage:** `OpenAI: start recognizing speech in [English v] record as []`
- **Quick Description:** Turn on microphone for speech recognition using OpenAI Whisper API
- **Full Description:** Same functionality as Azure version but uses OpenAI Whisper API. Supports all major languages.

### Block ID: ai_endspeech
- **Syntax:** `end speech recognition`
- **Usage:** `end speech recognition`
- **Quick Description:** Stops recording and sends speech to API for recognition
- **Full Description:** Stops microphone recording, sends to either Microsoft Azure or OpenAI Whisper API (depending on which start block was used), stores result in 'text from speech' block.

### Block ID: ai_textfromspeech
- **Syntax:** `text from speech`
- **Usage:** `text from speech`
- **Quick Description:** Reporter block that returns recognized text from speech
- **Full Description:** Returns the text recognized from speech after 'end speech recognition' runs.

### Block ID: ai_clearspeech
- **Syntax:** `clear speech text`
- **Usage:** `clear speech text`
- **Quick Description:** Clears speech recognition results
- **Full Description:** Clears the content of the 'text from speech' block.

### Block ID: ai_startrecognizer
- **Syntax:** `start continuous speech recognition in [LANGUAGE v] into list [LISTNAME v]`
- **Usage:** `start continuous speech recognition in [English (United States) v] into list [k v]`
- **Quick Description:** Continuous real-time speech recognition with Microsoft Azure API
- **Full Description:** Records voice and streams to Azure API, returns recognized text continuously. Each sentence stored as new item in list. Current sentence is last item, continuously updated. Stops when 'stop continuous speech recognition' block runs. Ideal for displaying recognition on-the-fly.

### Block ID: ai_stoprecognizer
- **Syntax:** `stop continuous speech recognition`
- **Usage:** `stop continuous speech recognition`
- **Quick Description:** Stops continuous speech recognition
- **Full Description:** Stops the continuous speech recognition process.

---

## CATEGORY 2: TEXT-TO-SPEECH

### Block ID: ai_speakinlanguage
- **Syntax:** `say [TEXT] in [LANGUAGE v] as [VOICETYPE v] speed (SPEEDRATIO) pitch (PITCHRATIO) volume (VOLUMERATIO) store sound as [SOUNDNAME]`
- **Usage:** `say [Hi] in [English (United States) v] as [Male v] speed (100) pitch (100) volume (100) store sound as []`
- **Quick Description:** Converts TEXT to audio using Microsoft Azure text-to-speech API
- **Full Description:** Supports all major languages. VOICETYPE options: Male, Female, Male2, Female2, Male3, Female3, Boy, Girl (not all voice types supported for all languages; Male/Female guaranteed for all). Customizable speed/pitch/volume (percentage values). Optional sound storage.

### Block ID: ai_stopspeaking
- **Syntax:** `stop speaking`
- **Usage:** `stop speaking`
- **Quick Description:** Stop AI speech playback
- **Full Description:** Stops the AI speech from text-to-speech block.

---

## CATEGORY 3: CHATGPT / LLM INTEGRATION

### Block ID: openaichatcompletion
- **Syntax:** `OpenAI ChatGPT: request [PROMPT] result [VARIABLE v] mode [MODE v] length [MAXLENGTH] temperature [TEMPERATURE] session [SESSIONTYPE v]`
- **Usage:** `OpenAI ChatGPT: request [hi] result [v1 v] mode [waiting v] length [100] temperature [1] session [new chat v]`
- **Quick Description:** Send prompt to ChatGPT Turbo 3.5 API
- **Full Description:** MODE options: 'streaming' (update variable with partial responses) or 'waiting' (wait for complete response). MAXLENGTH in tokens (100 tokens ≈ 75 words). TEMPERATURE: 0-1 (creativity control). SESSIONTYPE: 'new chat' or 'continue' (maintains context). Strong school-appropriate moderation applied. Streaming responses end with ✅ emoji.

### Block ID: openaichatcompletionsystem
- **Syntax:** `OpenAI ChatGPT: system request [PROMPT] session [SESSIONTYPE v] result [VARIABLE v] temperature [T]`
- **Usage:** `OpenAI ChatGPT: system request [you are an assistant] session [new chat v] result [t v] temperature [0.8]`
- **Quick Description:** Set system-level instruction for ChatGPT
- **Full Description:** Sets system-level prompts to control ChatGPT behavior/personality.

### Block ID: openai_chatgpt_cancel
- **Syntax:** `OpenAI ChatGPT: cancel request`
- **Usage:** `OpenAI ChatGPT: cancel request`
- **Quick Description:** Cancel ongoing ChatGPT request
- **Full Description:** Cancels an ongoing request to ChatGPT.

### Block ID: llmchatcompletion
- **Syntax:** `LLM model [PROVIDER] request [PROMPT] result [VARIABLE v] mode [MODE v] length [MAXLENGTH] temperature [TEMPERATURE] session [SESSIONTYPE v]`
- **Usage:** `LLM model [small v] request [hi] result [v1 v] mode [waiting v] length [100] temperature [1] session [new chat v]`
- **Quick Description:** Generic LLM interface with model selection
- **Full Description:** Similar to ChatGPT block but with PROVIDER selection (small/large models).

### Block ID: llmsysteminstruction
- **Syntax:** `LLM set system instruction [INSTRUCTION] for model [PROVIDER]`
- **Usage:** `LLM set system instruction [Pretend you are a chef] for model [large v]`
- **Quick Description:** Set system instruction for LLM model
- **Full Description:** Sets system-level instruction for specified LLM provider (small or large).

### Block ID: switchchatbot
- **Syntax:** `select chatbot [BOTID v]`
- **Usage:** `select chatbot [1 v]`
- **Quick Description:** Switch between multiple chatbot threads
- **Full Description:** Select which chatbot to use (1/2/3/4). Allows up to 4 parallel ChatGPT message threads.

### Block ID: attachimagetochat
- **Syntax:** `attach costume [COSTUMENAME] to chat`
- **Usage:** `attach costume [Front] to chat`
- **Quick Description:** Attach image costume to ChatGPT request
- **Full Description:** Finds costume by name and sends it as part of next ChatGPT request (vision capabilities).

### Block ID: attachfilestochat
- **Syntax:** `attach files to chat`
- **Usage:** `attach files to chat`
- **Quick Description:** Attach local files to chat session
- **Full Description:** Reporter block that triggers file selection window. User selects files from local drive, files added to LLM chat session. Returns list of file paths separated by "\n".

### Block ID: attachgooglefiletochat
- **Syntax:** `attach file from Google Drive [URL] to chat`
- **Usage:** `attach file from Google Drive [https://xxx] to chat`
- **Quick Description:** Attach Google Drive file to chat
- **Full Description:** Adds file from Google Drive (via shared URL) to LLM chat session.

---

## CATEGORY 4: IMAGE GENERATION

### Block ID: ai_openaiimagereporter
- **Syntax:** `OpenAI DALL-E: generate image with request [DESCRIPTION] resolution [RESOLUTION v]`
- **Usage:** `OpenAI DALL-E: generate image with request [a dog] with resolution [256x256 v]`
- **Quick Description:** Generate image using DALL-E API
- **Full Description:** Reporter block that generates image via OpenAI DALL-E based on DESCRIPTION. RESOLUTION options: '256x256', '512x512', or '1024x1024'. Returns image URL.

### Block ID: ai_xoimagereporter
- **Syntax:** `search for AI image of [TYPE v] with query [QUERY]`
- **Usage:** `search for AI image of [Object v] with query [a cat]`
- **Quick Description:** Search AI image library
- **Full Description:** Search for new image from AI image library using QUERY. TYPE options: Object, Character, or Backdrop.

---

## CATEGORY 5: CONTENT MODERATION

### Block ID: getmoderationresult
- **Syntax:** `get moderation result for [TEXT]`
- **Usage:** `get moderation result for [hell]`
- **Quick Description:** AI moderation for text content
- **Full Description:** Reporter block that uses AI moderation to check text input. Returns "Pass" or "Fail".

### Block ID: getmoderationresult2
- **Syntax:** `get moderation result for image at URL [INPUT]`
- **Usage:** `get moderation result for image at URL [https://xxx]`
- **Quick Description:** AI moderation for images at URL
- **Full Description:** Reporter block that uses AI moderation to check image at given URL. Returns "Pass" or "Fail".

### Block ID: getmoderationresult3
- **Syntax:** `get moderation result for costume named [INPUT]`
- **Usage:** `get moderation result for costume named [c1]`
- **Quick Description:** AI moderation for costume images
- **Full Description:** Reporter block that uses AI moderation to check costume image. Returns "Pass" or "Fail".

---

## CATEGORY 6: NLP / SENTENCE ANALYSIS

### Block ID: ai_parsesentence
- **Syntax:** `analyze sentence [SENTENCE] and write into table [TABLENAME v]`
- **Usage:** `analyze sentence [What is your name?] and write into table [k v]`
- **Quick Description:** Natural language processing for sentence analysis
- **Full Description:** Analyzes sentence structure and writes grammatical information to table. Identifies parts of speech (verbs, pronouns, etc.), lemmas, and word types.

---

## CATEGORY 7: COMPUTER VISION - FACE DETECTION

### Block ID: ai_facedetection
- **Syntax:** `run face detection debug [DODEBUG v] and write into table [TABLENAME v]`
- **Usage:** `run face detection debug [yes v] and write into table [m v]`
- **Quick Description:** Real-time face detection from camera
- **Full Description:** Turns on front camera, detects faces in real-time. Table columns: ID (face identifier 0,1,2...), variable (tilt angle, left/right eye x/y, nose x/y, mouth x/y, left/right ear x/y), value (coordinates/angles). Debug mode shows red rectangles and blue dots on detected features. X range: -240 to 240, Y range: -180 to 180. Each face = 13 table rows. User clicks red STOP to end.

---

## CATEGORY 8: COMPUTER VISION - BODY DETECTION

### Block ID: ai_bodydetection
- **Syntax:** `run 2D body part recognition single person [ISSINGLE v] table [TABLENAME v] debug [DODEBUG v]`
- **Usage:** `run 2D body part recognition single person [yes v] table [n v] debug [yes v]`
- **Quick Description:** 2D body part recognition from camera
- **Full Description:** Turns on front camera, recognizes 2D body parts. ISSINGLE: 'yes' for single person, 'no' for multiple. Table columns: id, part, x, y, curl, dir. Parts include: nose, eyes, ears, shoulders, elbows, wrists, hips, knees, ankles, plus computed left/right arm/leg. Curl/dir only for arms/legs (180° = straight, dir: 0° = up). Debug mode shows skeleton overlay.

### Block ID: ai_stopbodydetection
- **Syntax:** `stop 2D body part recognition`
- **Usage:** `stop 2D body part recognition`
- **Quick Description:** Stop body part recognition
- **Full Description:** Stops 2D body part recognition.

### Block ID: ai_bodydetection3
- **Syntax:** `run 3D pose detection debug [DODEBUG v] table [TABLENAME v]`
- **Usage:** `run 3D pose detection debug [yes v] table [r v]`
- **Quick Description:** 3D pose detection for single person
- **Full Description:** Turns on front camera, detects 3D pose of single person. Table columns: part, x, y, z. 33 body parts including: nose, eyes (inner/outer), ears, mouth corners, shoulders, elbows, wrists, fingers (pinky/index/thumb), hips, knees, ankles, heels, foot index. Mirror-like view: x=right, y=up, z=forward. Debug mode shows 3D skeleton.

---

## CATEGORY 9: COMPUTER VISION - HAND DETECTION

### Block ID: ai_handdetection3
- **Syntax:** `run hand detection table [TABLENAME v] debug [DODEBUG v] show video [SHOWVIDEO v]`
- **Usage:** `run hand detection table [o v] debug [yes v] show video [yes v]`
- **Quick Description:** Hand detection and gesture recognition
- **Full Description:** Detects hands from camera. Table columns: hand (left/right), part, curl, dir, x, y, z. 47 rows per hand: 5 fingers (thumb/index/middle/ring/pinky with curl/dir), 21 2D keypoints (wrist, finger joints 1-4 with x/y), 21 3D keypoints (same points with x/y/z). Curl: 180° = straight. Dir: 0° = pointing up. SHOWVIDEO controls camera visibility.

### Block ID: ai_updatedebug
- **Syntax:** `set debug mode [DODEBUG v]`
- **Usage:** `set debug mode [yes v]`
- **Quick Description:** Update debug mode on-the-fly
- **Full Description:** Updates debug mode for ongoing tasks (hand/face/body detection).

---

## CATEGORY 10: MACHINE LEARNING - KNN CLASSIFIER

### Block ID: ai_createknnclassifier
- **Syntax:** `create KNN number classifier from table [TABLENAME v] K [KVALUE] named [NAME]`
- **Usage:** `create KNN number classifier from table [p v] K [3] named [classifier1]`
- **Quick Description:** Create K-Nearest Neighbor classifier
- **Full Description:** Creates KNN classifier from table data. First column must be 'label' (class). Remaining columns are numeric properties. KVALUE = number of neighbors.

### Block ID: ai_predictknnclassifier
- **Syntax:** `predict for table [TABLENAME v] with classifier [NAME] show neighbors [SHOW v]`
- **Usage:** `predict for table [q v] with classifier [classifier1] show neighbors [yes v]`
- **Quick Description:** Predict class using KNN classifier
- **Full Description:** Uses KNN classifier to predict 'label' for data in table. Writes predicted label to first column. SHOW='yes' adds column with nearest neighbor indices. Table structure must match training table.

---

## CATEGORY 11: MACHINE LEARNING - NEURAL NETWORKS

### Block ID: create_nn_model
- **Syntax:** `create NN model named [NAME]`
- **Usage:** `create NN model named [model1]`
- **Quick Description:** Create neural network model
- **Full Description:** Creates TensorFlow sequential model with specified NAME.

### Block ID: addlayertomodel
- **Syntax:** `add layer to NN model [NAME] input shape (SHAPESIZE) output size (OUTPUTSIZE) activation [FUNCTION v]`
- **Usage:** `add layer to NN model [model1] input shape (10) output size (5) activation [relu v]`
- **Quick Description:** Add layer to neural network
- **Full Description:** Adds layer to NN model with input shape, output size, and activation function (relu, sigmoid, etc.).

### Block ID: compile_model
- **Syntax:** `compile NN model [NAME] loss [LOSSFUNCTION v] optimizer [OPTIMIZER v] learning rate (RATE)`
- **Usage:** `compile NN model [model1] loss [meanSquaredError v] optimizer [adam v] learning rate (0.01)`
- **Quick Description:** Compile neural network model
- **Full Description:** Compiles NN model with loss function (meanSquaredError/poisson), optimizer (adam/sgd/adagrad), and learning rate.

### Block ID: train_model
- **Syntax:** `train NN model [NAME] using table [TABLENAME v] rows from [STARTROW] to [ENDROW] input columns [INPUTCOLUMNS] output column [OUTPUTCOLUMN] batch size [BATCHSIZE] epochs [EPOCHS]`
- **Usage:** `train NN model [model1] using table [table1 v] rows from [1] to [1000] input columns [x, y] output column [z] batch size [32] epochs [500]`
- **Quick Description:** Train neural network with table data
- **Full Description:** Trains NN model using table data. Specify row range, input columns (comma-separated), output column, batch size, and epochs.

### Block ID: predict_by_model
- **Syntax:** `predict using NN model [NAME] for table [TABLENAME v] rows from [STARTROW] to [ENDROW] input columns [INPUTCOLUMNS] output column [OUTPUTCOLUMN]`
- **Usage:** `predict using NN model [model1] for table [table2 v] rows from [1] to [100] input columns [x,y] output column [z]`
- **Quick Description:** Predict using trained neural network
- **Full Description:** Uses pretrained NN model to predict outputs for new data. Specify row range, input columns, output column for results.

### Block ID: save_model
- **Syntax:** `save NN model named [NAME]`
- **Usage:** `save NN model named [model1]`
- **Quick Description:** Save neural network model
- **Full Description:** Saves NN model to CreatiCode server for future use.

### Block ID: load_model
- **Syntax:** `load NN model named [NAME]`
- **Usage:** `load NN model named [model1]`
- **Quick Description:** Load saved neural network model
- **Full Description:** Loads previously saved NN model from CreatiCode server.

---

## CATEGORY 12: SEMANTIC SEARCH / VECTOR DATABASE

### Block ID: addtabletopinecone
- **Syntax:** `create semantic database from table [TABLE v]`
- **Usage:** `create semantic database from table [t1 v]`
- **Quick Description:** Create semantic vector database
- **Full Description:** Builds semantic database using table data. One database per project. Table must have 'key' column (other columns optional). Converts key values to embedding vectors, stores in Pinecone index with other columns as metadata.

### Block ID: searchfrompinecone
- **Syntax:** `search semantic database with [QUERY] store top (K) in table [t1 v] filter by column [FIELD] of value [VALUE]`
- **Usage:** `search semantic database with [what's your phone number?] store top [3] in table [w v] filter by column [state] of value [NY]`
- **Quick Description:** Search semantic database with filter
- **Full Description:** Searches semantic database. QUERY converted to embedding vector, searches Pinecone index. Returns top K records to table. Optional filter: FIELD must equal VALUE.

### Block ID: searchfrompinecone2
- **Syntax:** `search semantic database with [QUERY] where [CONDITION] store top (K) in table [TABLE v]`
- **Usage:** `search semantic database with [is scratch free?] where [(state = "NY") and (points > 35)] store top [3] in table [result v]`
- **Quick Description:** Search semantic database with complex conditions
- **Full Description:** Semantic search with complex WHERE conditions (supports AND/OR logic, comparisons).

---

## CATEGORY 13: WEB SEARCH

### Block ID: googlesearch
- **Syntax:** `web search [QUERY] store top (K) in table [TABLE v]`
- **Usage:** `web search [price of MSFT stock today] store top (3) in table [result_table v]`
- **Quick Description:** Web search with results to table
- **Full Description:** Runs web search, stores top K results in table with 3 columns: title, link, snippet.

---

## SUMMARY BY FUNCTIONALITY

### Speech Recognition (7 blocks)
- Azure speech-to-text (ai_startspeech)
- OpenAI Whisper speech-to-text (ai_startopenaispeech)
- End recognition (ai_endspeech)
- Get recognized text (ai_textfromspeech)
- Clear speech text (ai_clearspeech)
- Continuous recognition (ai_startrecognizer)
- Stop continuous recognition (ai_stoprecognizer)

### Text-to-Speech (2 blocks)
- Azure TTS with voice/speed/pitch control (ai_speakinlanguage)
- Stop speaking (ai_stopspeaking)

### ChatGPT/LLM (9 blocks)
- ChatGPT request (openaichatcompletion)
- ChatGPT system prompt (openaichatcompletionsystem)
- Cancel ChatGPT (openai_chatgpt_cancel)
- Generic LLM request (llmchatcompletion)
- LLM system instruction (llmsysteminstruction)
- Switch chatbot thread (switchchatbot)
- Attach costume/image (attachimagetochat)
- Attach local files (attachfilestochat)
- Attach Google Drive files (attachgooglefiletochat)

### Image Generation (2 blocks)
- DALL-E generation (ai_openaiimagereporter)
- AI image search (ai_xoimagereporter)

### Content Moderation (3 blocks)
- Text moderation (getmoderationresult)
- Image URL moderation (getmoderationresult2)
- Costume moderation (getmoderationresult3)

### NLP (1 block)
- Sentence analysis (ai_parsesentence)

### Computer Vision - Face (1 block)
- Face detection (ai_facedetection)

### Computer Vision - Body (3 blocks)
- 2D body detection (ai_bodydetection)
- Stop 2D body detection (ai_stopbodydetection)
- 3D pose detection (ai_bodydetection3)

### Computer Vision - Hand (1 block)
- Hand detection/gestures (ai_handdetection3)

### Computer Vision - Utility (1 block)
- Update debug mode (ai_updatedebug)

### Machine Learning - KNN (2 blocks)
- Create KNN classifier (ai_createknnclassifier)
- Predict with KNN (ai_predictknnclassifier)

### Machine Learning - Neural Networks (6 blocks)
- Create model (create_nn_model)
- Add layer (addlayertomodel)
- Compile model (compile_model)
- Train model (train_model)
- Predict (predict_by_model)
- Save/Load models (save_model, load_model)

### Semantic Search (3 blocks)
- Create semantic DB (addtabletopinecone)
- Search with filter (searchfrompinecone)
- Search with conditions (searchfrompinecone2)

### Web Search (1 block)
- Web search (googlesearch)

---

## KEY FINDINGS FOR T24 SKILLS VERIFICATION

1. **Total AI blocks: 43** across 13 functional categories
2. **Speech Recognition**: Both Azure and OpenAI Whisper supported
3. **ChatGPT Integration**: Full support including vision (image attachments), file attachments, streaming
4. **Computer Vision**: Comprehensive - face, 2D body, 3D pose, hand detection
5. **Machine Learning**: Both traditional (KNN) and deep learning (TensorFlow NN)
6. **Advanced Features**: Semantic search with vector embeddings (Pinecone), content moderation
7. **Multi-modal**: Text, speech, images, video all supported

This comprehensive list should be used to verify that T24 skills accurately reflect all available AI capabilities.
