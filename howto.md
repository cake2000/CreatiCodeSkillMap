read spec_v2_updated.md to understand the whole project, and read the key referneces like csta standard draft, and ai priorities, and creaticode introduction.

ignore ACSL since it is too theoretic!

latest skills and topic definitions are in "skillsv3" folder (ignore the "skills" folder)

we are aiming for "IXL for coding based on creaticode", and we need top quality result.

now, we need to enhance the quality of the skills. let's review and update ALL the skills in this 2 topics:

/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv3/skills_T21_ai_media.md
/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv3/skills_T22_chatbots.md

needless to say these are fairly advanced usage of AI to build apps, so they should be at least starting in 6th grade, and they should go hand in hand with the topic on widgets: /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv3/skills_T16_ui_widgets.md

our skills should focus on application of AI and prompting LLM, and not so much on theory or how it works internally since this is for middle school.

make sure you consider AI4K12 priorities in 

/media/binyu/USB2/dev/CreatiCodeSkillMap/docs/AI-Priorities-for-All-K-12-Students-Report-from-CSTA-AI4K12.md




read this file docs/TOPIC_IXL_MICROSTEP_GUIDE.md to learn how to do it. note that k-2 level skills will not touch code blocks yet. They start to do any coding or do scripts/blocks in grade 3. 

Also you need to check this topic against other topics to ensure no duplicates and skills progress well from grade to grades.

The key is scaffolding and ordering/sequencing logically. also always keep skill challenges engaging/fun.

also you should learn the AI blocks from 

/media/binyu/USB2/scratch-workspace/scratch-vm-3d/src/blocks/scratch3_ai.js
/media/binyu/USB2/ScratchCopilot/blockdes8.txt

also, for reference, below is a list of AI related lessons developed on CreatiCode:

Module 2	Basic Generative AI Apps			900	
Lesson 2.1	Introduction to the ChatGPT Block	Link		50	How the ChatGPT block functions in CreatiCode, including parameters like prompt, temperature, and output variable. Activity: Test different parameter settings to observe effects on AI outputs.
Lesson 2.2	A Simple “Ask-Me-Anything” App	Link		50	Creating a basic text-based conversation flow (user input → ChatGPT → sprite “says” response). Activity: Wire up a simple “ask and wait” block to ChatGPT and display the response in a speech bubble.
Lesson 2.3	A “Chat with Einstein” App	Link	Link	50	Prompting ChatGPT to “role-play” as Einstein, introducing role prompts. 
Lesson 2.4	An Improved Chat App	Link		50	Enhancing chat functionality with streaming responses and refined prompt techniques. 
Lesson 2.5	“Guess a Historical Figure” Game	Link		50	Adjusting prompts to change an app’s logic for a guessing game. 
Lesson 2.6	An MBTI Personality Test App	Link		50	Step-by-step prompt adaptation to achieve a goal. 
Lesson 2.7	Effective Prompting with the TIRE Method	Link		70	Learning the T.I.R.E. method for effective prompting and conducting an assessment. 
Lesson 2.8	AI-based Story Writer	Link		50	Leveraging ChatGPT for creative text generation, using a non-chat user interface
Lesson 2.9	A Quiz Writer	Link		70	Generating quiz questions and evaluating answers. 
Lesson 2.10	An AI Book Writer	Link		70	Generating an entire book on a given topic. 
Lesson 2.11	A Cloze Game	Link		70	Creating complex prompts to produce fill-in-the-blank texts. 
Lesson 2.12	2 Chatbots Debating Each Other	Link		70	Setting up two AIs to engage in debate with each other. 
Lesson 2.13	Group Project A	Link		200	Apply learned prompting techniques and app development skills to build a new app.
					
Module 3	Voice & Vision AI Apps			815	
Lesson 3.1	Speech to Text Recognition	Link		75	Converting spoken words from a microphone into text. 
Lesson 3.2	Text to Speech Synthesis	Link		50	Synthesizing speech from text. 
Lesson 3.3	Talk to an AI Sprite	Link		50	Combining speech-to-text with ChatGPT and optional text-to-speech. 
Lesson 3.4	AI Voice Translator	Link		50	Integrating speech-to-text with ChatGPT and adding optional text-to-speech. 
Lesson 3.5	Vision-based AI Assistant	Link		80	Developing a multi-modal AI that can interpret camera images. 
Lesson 3.6	Introduction to AI Motion Sensor	Link		50	Basics of video sensing blocks for movement detection. 
Lesson 3.7	Bouncing Ball with Motion Sensor	Link		50	Using motion input to move sprites or detect collisions. 
Lesson 3.8	AI for Hand Tracking	Link		120	Detecting finger keypoints to recognize gestures. 
Lesson 3.9	Fitness Game Using Body Pose	Link		90	Designing a game using body pose input (for example, squatting to move a sprite). 
Lesson 3.10	Group Project B	Link		200	Apply all learned lessons to create a new app, particularly utilizing voice or vision-based AI capabilities.
					
Module 4	Advanced Generative AI Apps			885	
Lesson 4.1	Who’s the Spy?	Link		80	Using ChatGPT as a reasoning engine to drive an interactive detective game. 
Lesson 4.2	Guardian of History (more difficult)	Link		100	Using LLM as a reasoning engine to drive an interactive time-travel mystry game
Lesson 4.3	Text Summarization: Product Review	Link		70	Summarizing or analyzing large blocks of text (e.g., product reviews) using ChatGPT. 
Lesson 4.4	Text Summarization: Web Search	Link		60	Using the web search block to fetch snippets and then summarizing them with ChatGPT. 
Lesson 4.5	Tool Use: Math Calculations	Link		65	Instructing ChatGPT to perform math calculations using a calculator tool. 
Lesson 4.6	Tool Use: Web Search	Link		80	Enabling ChatGPT to utilize a web search tool. 
Lesson 4.7	Tool Use: An AI-Powered Calendar Assistant	Link		120	Enable LLM to utilize Google Sheets as storage for calendar events
Lesson 4.8	A QA Bot Using Semantic Search (RAG)	Link		110	Building or importing a knowledge base and embedding/indexing it for semantic retrieval. 
Lesson 4.9	Group Project C	Link		200	Leveraging advanced LLM capabilities (text processing/summarization, reasoning, tool use, semantic search) to develop a new app.