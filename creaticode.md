# CreatiCode Platform Capabilities and Features

CreatiCode is an innovative, Scratch-based coding platform that extends MIT Scratch 3.0 with many new features for creative projects  $^{1}$ . It maintains all the standard block-coding functionalities of Scratch while adding powerful new blocks and AI tools. This allows users (especially K-12 students) to build everything from classic Scratch animations to AI chatbots, 3D games, and interactive applications that incorporate voice, vision, and even multiplayer capabilities  $^{1}$ . Below is a comprehensive overview of CreatiCode's capabilities, focusing on end-user visible features: the full range of Scratch blocks (unchanged from MIT Scratch) and the new extensions like 3D programming, AI integration, widgets (UI controls), multiplayer, augmented reality, and more  $^{2}$ .

# Standard Scratch Features in CreatiCode

CreatiCode is built on the foundation of MIT Scratch 3.0, so all the original Scratch block categories and blocks are available. Users can create projects in the familiar drag-and-drop interface and share them in the CreatiCode online community just as they would on Scratch (e.g. with a "My Stuff" area for personal projects, the ability to remix others' projects, and project sharing/publishing)  $^{3}$ . The editor interface and basic workflow (sprites, costumes, backdrops, code area, green flag to start, etc.) remain the same as Scratch  $^{4}$ . Below is a list of the Scratch block categories and their blocks included in CreatiCode:

- Motion (blue blocks): Blocks to move and orient sprites. These include move (10) steps, turn  $\odot$  (15) degrees (clockwise) and turn  $\odot$  (15) degrees (counter-clockwise), go to x: (0) y: (0), glide (1) secs to x: (0) y: (0), point in direction (90), point towards [Sprite], change x by (10), set x to (0), change y by (10), set y to (0), if on edge, bounce, and set rotation style [left-right/all-around/none]. These work exactly as in Scratch, controlling sprite movement on the 2D stage.  
- Looks (purple blocks): Blocks for sprite and stage appearance. For example: say [Hello!] for (2) seconds, say [Hello!] (indefinitely), think [Hmm...] for (2) seconds, switch costume to [costume2], next costume, switch backdrop to [backdrop2], change size by (10), set size to (100)% show, hide, go to front layer / go back (1) layer, etc. These allow changing costumes, backdrops, visible text bubbles, size, effects, and layering of sprites.  
- Sound (pink blocks): Blocks to play and manipulate sounds. They include play sound [pop] until done, start sound [meow], stop all sounds, change volume by (-10), set volume to (100)% change tempo by (20), set tempo to (60) bpm, etc. Users can still add sound files to sprites and use these blocks to incorporate audio.  
- Events (brown blocks): Hat blocks that trigger scripts on events, just like in Scratch. For example: when clicked (when green flag clicked), when [key space] pressed, when this sprite clicked, when backdrop switches to [backdrop1], when

[loudness] > (10) (an event from microphone input), and broadcast events such as when I receive [message1] paired with the stack block broadcast [message1] (and broadcast [message1] and wait). These blocks initiate scripts based on user actions or broadcasts.

- Control (gold blocks): Blocks for loops, conditional logic, and control flow. These include wait (1) seconds, repeat (10) (loop), forever loop, if <(condition)> then (and if <> then ... else), wait until <(condition)>, repeat until <(condition)>, stop [all this script/other scripts], when I start as a clone (hat block for clones), create clone of [myself/other sprite], and delete this clone. All standard Scratch control structures are present for managing script execution and cloning.  
- Sensing (light-blue blocks): Blocks that detect various states or inputs. For example: touching [Mouse-pointer] ?, touching color [#FF0000]? ask [What's your name?] and wait (with the answer stored in the Answer reporter), key [space] pressed?, mouse x / mouse y position reporters, loudness and timer reporters, of() sensing blocks (like [costume #] of [Sprite] or [x position] of [Sprite] to get another sprite's property), current [year/month/date...], days since 2000, and user input related reporters (Answer, Mouse Down?, etc.). These allow a project to respond to the environment (keyboard, mouse, mic) and inquire about object properties.  
- Operators (light-green blocks): Blocks for math and logic operations. These include arithmetic  $(\text{()} + \text{()}, \text{()} - \text{()}, \text{()} * \text{()}, \text{()} / \text{()})$ , random number generation (pick random (1) to (10)), comparisons ( $\text{()} > \text{()}$ ,  $\text{()} < \text{()}$ ,  $\text{()} = \text{()}$ ), boolean logic (<condition> and <condition>, or, not), and other operators like joining strings (join [Hello] [World]), string length (length of [text]), character extraction (letter (1) of [text]), and conversions ([foo] contains [o]? rounding, modulo, etc.). All standard Scratch operators are available for use in CreatiCode.  
- Variables and Lists (orange blocks): Blocks to store and manipulate data. Users can create their own variables (global or sprite-local) and lists, just as in Scratch. Variable blocks include set [var] to (0), change [var] by (1), show variable [var], hide variable [var]. List blocks include add [thing] to [list], delete (1) of [list], insert [thing] at (1) of [list], replace item (1) of [list] with [value], and reporters like item (1) of [list], length of [list], [list] contains [thing]? These work identically to Scratch, enabling data storage and manipulation.  
- My Blocks (red, custom): CreatiCode allows defining custom blocks (procedures) just like Scratch's My Blocks. Users can create a block with optional parameters and define its script. The ability to "Make a Block" and use it for procedural abstraction is supported, which helps organize code in both Scratch and CreatiCode.  
- Pen & Music Extensions: CreatiCode includes the standard Scratch extensions like Pen (drawing on the stage) and Music. The Pen extension adds blocks such as pen down, pen up, set pen color to [ ] change pen color by ( ) , set pen size to ( ) , clear etc., allowing drawing with sprites . The Music extension provides blocks like play note (60) for (0.5)

beats and instruments selection, enabling musical projects. These extensions function the same as in Scratch.

- Text-to-Speech and Translate Extensions: CreatiCode incorporates Scratch's Text to Speech extension (with far more capabilities via new AI blocks, discussed below) and the Translate extension. The Translate extension includes blocks like translate [hello] to [Spanish] reporter, which uses Google Translate service (as in Scratch). This can be used to translate text between languages. (Note: CreatiCode also provides AI-based translation alternatives through ChatGPT blocks, described later.)  
- Video Sensing Extension: The platform supports Scratch's Video Sensing extension, which uses the computer's camera. Blocks such as turn video [on/off/on-flipped], set video transparency to (50)% when video motion > (10) (an event hat), and the reporter video [motion] on [sprite/stage] are available 7 8 . These allow projects to detect motion or direction of motion from the camera feed, enabling simple augmented reality interactions (e.g. moving a sprite when the user moves). CreatiCode's curriculum uses these to teach concepts of motion detection via camera 9 10 .

(All the above blocks and features function just as they do in standard Scratch 3.0. CreatiCode's enhancements are additive, meaning users familiar with Scratch can immediately use all these blocks on CreatiCode.)

# 3D Programming with Physics

One of the most significant expansions in CreatiCode is the introduction of 3D coding capabilities. CreatiCode adds an entire 3D game engine and physics system accessible through new 3D block categories  $^{2}$ . This lets users create and manipulate 3D scenes within the otherwise 2D Scratch stage. Key features of the 3D extension include:

- 3D Scene and Camera: Users can initialize a 3D scene in their project (e.g. using a block to set up a 3D world) and control a camera. For example, there are blocks to initialize a 3D scene (often an empty scene or with a preset environment) and to add cameras. CreatiCode supports different camera types like a follow-camera that can attach to an object (sprite) and follow it from a set angle/ distance  $^{11}$ . Users can adjust camera perspective to view the 3D world (e.g. a follow camera that tracks a moving object from behind or above).  
- 3D Objects and Models: A variety of 3D objects can be created via blocks. Primitive shapes (cube, sphere, cylinder, plane, etc.) can be added to the scene, as well as more complex models. For example, blocks allow adding shapes like a "3D box" of specified size or a "rectangle tube" (hollow box) to use as objects  $^{12}$ $^{13}$ .Sprites in a 3D project can act as containers for 3D models (the curriculum often uses an "Empty" sprite as a placeholder for 3D content  $^{14}$ ). CreatiCode also supports importing 3D models (like .obj files or other predefined models) via blocks, enabling use of complex characters or props in games. These models can be textured or colored with materials (e.g. a grid material for a floor grid) using additional blocks  $^{13}$ .  
- Positioning and Movement in 3D: Blocks exist to set or change an object's position (x, y, z coordinates in the 3D space) and rotation (around x, y, z axes). Just like moving sprites in 2D (x-y), 3D

blocks allow moving objects along depth (z) and turning in 3 axes. Users can move objects, have them point towards points or other objects in 3D, and even attach objects together as parent/child (for example, attaching propellers to a drone model as children, so they move with the drone 15).

- 3D Physics Engine: CreatiCode includes a physics engine for 3D projects, enabling realistic motion (gravity, falling, collision, bounce, etc.)  $^{12}$ . Users can turn on physics with a block (e.g. "initialize 3D physics"). Once enabled, sprites/objects can be given physical properties by adding a physics body to them (via blocks). For instance, one can assign a mass to an object (mass  $>0$  means gravity will affect it)  $^{13}$ . Blocks allow applying forces or impulses to objects to make them move realistically  $^{16}$ ,  $^{17}$ , and setting properties like friction or bounciness. The physics engine automatically handles continuous movement and collisions once set up. For example, a tutorial shows adding a physics body to a drone object (mass 100) so it falls due to gravity, and preventing it from rotating on certain axes to keep it upright  $^{13}$ ,  $^{18}$ . Gravity is adjustable (the user can set gravity strength in the physics init block; e.g. in one project gravity was set to -1000 in Y to make things drop faster  $^{19}$ ).

- Collision Detection and Constraints: With 3D physics, objects will collide with each other and with a default ground or walls if defined. Users can add an invisible floor or walls (e.g. a large flat box as ground) so objects don't fall indefinitely  $^{13}$ . There are also blocks for special physics constraints (e.g. hinge joints, attaching objects together with physics). For example, the drone carrying a box tutorial used a physics constraint to attach a box to the drone, simulating a carried load  $^{12}$ . These advanced features allow projects like simulators and games to have realistic physical interactions.

- User Input in 3D Projects: CreatiCode recognizes that controlling 3D experiences differs from 2D. It provides special blocks for 3D user controls. One notable addition is the Virtual Joystick widget for mobile or touch input in 3D games  $20 \quad 21$ . A block can "add a joystick" (left or right side of screen, with specified colors and size) to the stage  $21$ . Another reporter block lets you read the joystick's status ( $x$ ,  $y$  displacement, direction, pressed or not)  $22 \quad 23$  so you can use it to steer a character or camera in a 3D game. This is very useful for smartphone or tablet users in 3D projects  $24$ . Traditional controls like keyboard (WASD) can also be used as usual (since those are just key events).

- Rendering and Visuals: CreatiCode's 3D engine handles rendering 3D graphics on the stage.Sprites in 3D projects essentially become 3D object holders. Users can still use costumes and backdrops in 3D projects (e.g. a backdrop might act as sky or environment). Additionally, lighting and camera perspective are managed automatically, but some blocks may allow adding lights or switching camera modes (e.g. perspective vs orthographic). For example, the platform's demo projects include things like a 3D glass object that can be rotated via joystick input  $^{25}$ .

In summary, the 3D blocks empower students to make simple 3D games and simulations without leaving the Scratch paradigm  $^{26}$ . They do not need to learn a separate 3D engine or language - CreatiCode provides "easy-to-understand blocks for 3D programming"  $^{27}$ , extending Scratch's simplicity into the third dimension. All 3D features are optional: you start a project as 2D by default, and by initializing a 3D scene you unlock these new blue-colored 3D blocks in the palette.

# 2D Physics Engine

In addition to 3D physics, CreatiCode also offers a 2D physics engine for regular 2D Scratch projects  $^{28}$ . This feature allows more realistic movements and collisions in 2D games (akin to how many popular games

use physics). The 2D physics is provided as an extension/category (often called "2D Physics" in the blocks menu) that can be enabled when needed. Key aspects include:

- Physics World Initialization: To start using 2D physics, the user must initialize a physics world. A block (in the 2D Physics category) creates a physics world that runs in the background  $^{29}$ . This world has gravity and boundaries. For example, you can specify gravity in the X and Y directions when initializing (e.g. gravity  $X = 0$ ,  $Y = -100$  for a normal downward gravity)  $^{30}$ . Once initialized, invisible walls are automatically added at the stage edges to contain the physics simulation  $^{31}$ .  
- Adding Physics Bodies: After initializing the physics world, sprites can be given physics properties by adding a physics body to them. CreatiCode provides blocks to attach a physics body to a sprite (making that sprite subject to physics). Options include setting the body type (dynamic or static), mass (which affects gravity and inertia), and other properties like whether it's allowed to rotate. Once a sprite has a physics body, the engine will handle its movement and collision responses automatically  $^{32}$ $^{33}$ . For example, a ball sprite with a physics body will fall down, bounce off walls, or collide with other physics-enabled sprites, without manual scripting of gravity or bounce logic.  
- Forces and Impulses: Blocks are available to apply forces or impulses to 2D physics sprites. This allows the user to, say, simulate a push or a jump. After adding a physics body, one can use a block (e.g. "apply force (vx, vy) to [sprite]" or "apply impulse") to influence the sprite's motion. The physics engine then carries out the motion over time (taking into account friction, gravity, etc.)  $^{34}$ . This greatly simplifies movement code - instead of updating x/y each frame, the user relies on the physics simulation to move the object naturally.  
- Collisions and Collision Groups: The physics engine detects when physics-enabled sprites collide and can respond by bouncing or stopping them. CreatiCode includes more advanced blocks to manage collisions, such as setting collision groups or categories so that certain sprites collide with some objects but not others  $^{35}$ . This is useful for scenarios like a game where the player passes through some objects but not others, or projectile vs target collisions. There are also blocks to adjust restitution (bounciness), friction, and to detect collision events (e.g. an event block or a reporter that checks if two objects are touching in the physics simulation).  
- Constraints and Joints: For more complex mechanisms, CreatiCode's 2D physics provides blocks for joints (constraints) as well. For example, you could create a weld joint between two sprites (so they act as one object after being joined), or a pivot joint to connect sprites like links. These blocks allow constructing structures (like a car with wheels, or a swinging rope) within the 2D world.

Using the 2D physics engine can make games feel more realistic and also simplify code by offloading motion calculations to the engine  $^{32}$ . Classic game styles (Angry Birds-style trajectory, platformer gravity, bouncing balls, etc.) are easier to implement. The educational benefit noted is that the physics engine acts like an "AI assistant" for movement: you describe what should happen (e.g. "make this ball fall with gravity") and the engine handles how to do it  $^{32}$ . This not only produces realistic results but also keeps the block scripts concise and focused  $^{37}$ .

# AI Integration and Tools

CreatiCode's most distinctive features involve Artificial Intelligence (AI) integration. The platform introduces new blocks and tools that allow projects to generate text, converse using AI (chatbot behavior), generate or search for images via AI, recognize speech, and more. These features bring generative AI and machine learning capabilities into a Scratch-like environment, greatly expanding what students can create. Key AI-related capabilities include:

- ChatGPT Blocks (AI Chatbot): CreatiCode provides a block to connect with OpenAI's ChatGPT model (a large language model) directly within a project  $^{38}$ . This ChatGPT request block (found in the new "AI" category of blocks) lets the user send a prompt to ChatGPT and get the response back into their program  $^{38}$ . The block has multiple parameters:  
- Request: a text input (the prompt/question for ChatGPT) 39.  
- Result: a dropdown to choose a variable where the AI's response will be stored 40.  
- Mode: either "waiting" or "streaming". In waiting mode, the block will pause the script until the full response is received (similar to Scratch's "broadcast and wait") and then continue. In streaming mode, the script continues immediately, and the response variable is updated in real-time as the AI generates text. This allows the project to display partial results (e.g. progressively show the AI's answer).  
- Length: (token limit) - a parameter for maximum response length. Note: Due to changes in OpenAI's API, this parameter became obsolete and is generally ignored; users are encouraged to control length via the prompt instead 44 .  
- Temperature: a number 0.0–1.0 controlling the creativity/randomness of the AI's response 45 . Higher values yield more varied outputs, lower values give more deterministic answers.  
- Session: controls conversation context 46. "New chat" means each use of the block starts a fresh conversation (no memory of previous prompts), whereas a continued session will have ChatGPT remember prior Q&A in that session variable 47. This is crucial for multi-turn conversations (the project can maintain context by using the same session ID for related queries).

Using these blocks, students can create sprites that act as chatbots – for example a character sprite that you can ask questions and it replies with ChatGPT-generated answers 48. CreatiCode's curriculum even nicknames this feature "Chat with Einstein" for an AI sprite impersonating a famous figure 49 50. Projects might use the ask and wait block to get user input, then feed the answer or question into the ChatGPT block, and finally have a sprite speak out or display the AI's answer. The Act 4 AI curriculum involves activities like "Ask Me Anything" chatbots 51 and role-playing chatbots (e.g. pretend to be Einstein 52). The ChatGPT integration opens up creative projects such as AI story generators, Q&A bots, and educational tutors, all within Scratch-style coding 53.

- AI Image Generation (Backdrops &Sprites): CreatiCode has a built-in AI image generator and library, allowing users to create graphics using text prompts  $^{54}$ . This is exposed not as a code block but as a tool in the editor UI: when adding a sprite or backdrop, users have an "AI" option. By clicking the AI button (a circular button at bottom-right of the editor), you can open the AI Image Library window  $^{55}$ . From there:  
- You can search a huge library of images that have been generated by the CreatiCode community (all user-generated images are shared in a common library)  $^{56}$ . For example, typing a query like "parking lot" and hitting Search will retrieve existing backdrop images tagged or described as parking lots  $^{57}$ . This is very fast and encourages re-use of community assets.

- You can refine searches with more descriptive terms if too many results appear (e.g. "parking lot dark" to find nighttime parking lot images)  $^{58}$ , or search by image name specifically  $^{59}$ .  
- If no suitable image exists, you can Generate a new image by entering a detailed prompt and clicking "Generate" 60 61 . The system (likely using a generative model akin to DALL-E or Stable Diffusion behind the scenes) will create a new backdrop or sprite image from the description. For best results, students are guided to write at least a 10-word description, specifying details so the AI can produce a fitting image 60 . For example, "a large and empty parking lot" might be used to generate a backdrop if nothing suitable was found in search 61 .  
- When generating sprites versus backdrops, CreatiCode uses different AI models suited to the task. The sprite-generation tool even lets you choose the model type: Human (for people or characters with limbs, faces), Non-Human (for objects, animals, etc.), or Vector (for flatter, clipart-style or SVG-like images). This selection helps the AI produce appropriate results (for instance, the "Human" model is better at generating a character with arms/legs, whereas "Non-Human" might produce cars, chairs, etc.) . The Vector option generates images that look more like illustrations or SVG graphics, useful for certain styles .  
- Once generated, the new image is added to the project either as a backdrop or a sprite costume (whichever context you opened the tool from). All generated images also get saved to the community library (though they are only usable within CreatiCode's platform due to licensing) 64

The image generator is heavily moderated for K-12 appropriateness 66 67 . Inappropriate prompts are blocked and CreatiCode staff can remove unsuitable images. This ensures the tool remains classroom-friendly. With AI image generation, students are no longer limited to Scratch's small built-in image library - they can create virtually any backdrop or character their story needs, by writing a description. This feature empowers more creative storytelling and game design, and also introduces students to the concept of prompt engineering (crafting effective descriptions for AI) 68 60

- Speech Recognition (Speech-to-Text): CreatiCode projects can utilize voice input via new speech recognition blocks. This feature allows the computer's microphone to be used to convert spoken words into text  $^{69}$ . It's analogous to giving a Scratch project the ability to "hear" and transcribe user speech. The blocks involved (found in the AI or sensing category) include:  
- start speech recognition [language] (save audio as [sound]?) - Begins listening via the mic 70 71. You can specify the language/accent to improve accuracy (e.g. English US vs English UK) 72. Optionally, it can save the recorded audio into the sprite's Sounds tab (if a name is given) 73, which is useful if you want to play back what was said.  
end speech recognition - Stops the listening process 74 . Once this block executes, the recorded audio is sent to an AI service to be transcribed into text 75 .  
- text from speech - A reporter block that holds the recognized text result 76 . The transcribed speech will appear here after end speech recognition is called. This acts like a variable containing whatever the user just said.  
- clear speech text - Resets the text from speech value (useful to clear out old input before a new session)

Typically, a project will use these in sequence: start recognition (possibly wait a few seconds or prompt the user to speak), then end recognition, then use the text from speech value. For example, a voice-controlled app might have the user press a "Start Listening" button (which triggers the start speech recognition block), then press "Stop" to end and process the result 78 79. The recognized text can be used just like typed input - e.g. fed to a ChatGPT block to ask a question, or matched against commands

(like interpreting voice commands "up", "down" in a game). This feature is noted as important for accessibility (users with limited ability to type can use voice) 80 . CreatiCode's tutorials include projects like a voice-controlled chatbot or a voice translator, where speech input is recognized, then perhaps translated or answered by AI 81 82.

- Text-to-Speech (AI Speaker): While Scratch has a basic Text-to-Speech extension, CreatiCode enhances this with an advanced AI Speaker block that can vocalize any text with flexible voice options  $^{83}$ . The AI Speaker block (in the AI category) is essentially a "say [text]" that generates spoken audio:  
It can speak a given sentence or phrase in a chosen language and voice style 84 85.  
- There are many languages available (with multiple dialect options for some) – e.g. English (US, UK, etc.), Spanish, Chinese, etc. 86 . You typically match the language to the text for natural sound, but you can also have, say, a French voice speak English for effect 87 .  
- You can select voice type (often male/female or different character voices) for the language  $^{85}$ . Not all voices apply to all languages, and the editor will warn if a voice isn't available  $^{88}$ .  
- Speaking rate (speed) can be set: 100 is normal,  $> {100}$  faster,  $< {100}$  slower  ${}^{89}$  .  
Pitch can be adjusted: 100 normal, higher for squeaky, lower for deep voice  ${}^{90}$  .  
Volume can also be controlled (100 normal, higher/lower for loud/soft) 91.  
- Critically, the block also has an option to save the speech as a sound clip in the project's Sounds tab by providing a name  $^{92}$ . This means if your project needs to reuse a phrase, you can generate it once and then just play the saved sound subsequently, improving efficiency.

The AI Speaker block is triggered like a stack block that takes the text and parameters; when run, it will output audio (and optionally store it). This allows sprite characters to literally talk in any language or voice, making storytelling and multi-lingual projects much richer. For example, a project can take a ChatGPT-generated answer and then have the AI Speaker read it aloud as if the sprite is talking to you 93 . Voice output also makes projects more accessible to young kids or language learners who might prefer to listen rather than read text on screen 83 . In CreatiCode's AI curriculum, students combine speech recognition and text-to-speech to create conversational agents (voice-driven chatbots) 94 95 .

- Computer Vision (Hand and Body Tracking): CreatiCode introduces AI-powered vision blocks that go beyond Scratch's simple video motion sensing. These allow the detection of specific things from the camera feed:  
- Hand Detection: A block in the AI category will detect a hand (or hands) in the camera view and provide detailed data about it  $96$ . When activated (e.g. placing the "start hand detection" block in your script), the camera turns on and the system identifies 21 landmark points on each detected hand (the joints of fingers and the wrist)  $97$ . The output of this block is stored in a table variable (discussed more below) - by default named "i" - which continuously updates with data for each frame  $98$ . For each hand, multiple rows of data are provided; in fact, 47 rows per hand are used in the data table  $99$ . These include information like each finger's curl angle (how bent or straight it is) and possibly 3D coordinates of each landmark. Students can use this data to, for example, count how many fingers are being held up. Indeed, one tutorial shows checking the first 5 rows (each finger's curl) and counting those with curl angle  $>150^{\circ}$  as "stretched out" to determine the number of fingers showing  $100 \times 101$ . This hand-tracking runs in real time, enabling interactive projects controlled by hand gestures (e.g. making a sprite respond to a thumbs-up, or moving a character by pointing).

- Body Pose Detection: Similar to hand tracking, there is an AI body pose detection capability. A block can detect human body keypoints (like shoulders, elbows, knees, etc.) from the camera feed and output them into a table variable. The curriculum refers to this as an "AI for Body Part Recognition" block 102. The data is stored in a table where each row represents a body joint with coordinates. Students use this for projects like counting exercises or simple fitness games – for example, detecting if someone is doing a "squat" by calculating distances between hip and knee points in the pose data 103. The data is accessible via table operations and allows real-time pose-based interactivity (like moving a sprite according to your body movement, or detecting certain poses/gestures).

- Face or Other Detection: (The curriculum documents primarily mention hand and full-body; face detection is not explicitly described, but it's possible CreatiCode has or may add face landmark detection similarly. If present, it would likely follow a similar pattern: an AI block that outputs positions of eyes, nose, etc., in a table.)

These computer vision blocks leverage machine learning models (likely MediaPipe or similar) under the hood, but expose them in a beginner-friendly way. By using table variables to hold results, CreatiCode avoids overwhelming beginners with complex data structures - it provides custom blocks to read from these tables (like "row count of table", or searching for values) and emphasizes conceptual understanding (e.g. explaining that motion is difference between camera frames 104, or that a hand's pose is represented by keypoints and angles 105 100). This gives students a gentle introduction to AI vision concepts while making fun interactive programs (like a game controlled by waving hands, or an app that counts your fingers) 106 107.

- Other AI Tools and Extensions: CreatiCode continues to expand AI tools. For instance, it has an extension for machine learning classification (the curriculum touches on a project classifying hand-drawn digits using pen drawing and simple edge detection logic as an analogy for AI 5). There is also mention of advanced topics like neural networks and self-driving cars in the curriculum 1 - for example, later units involve a simplified self-driving car simulation where students code the logic for lane detection or turning using sensors and possibly AI blocks (like a pre-trained model or just algorithmic approach) 108 109 . While these are mostly educational simulations rather than training neural networks from scratch, CreatiCode gives a platform to explore these concepts with block coding.

Another notable tool is CreatiCode XO, the AI assistant integrated into the editor (discussed below, since it's more about helping the user design projects rather than a block used inside the project).

# UI Widgets and Custom Interfaces

CreatiCode enriches the user interface aspect of projects by introducing Widget blocks - essentially GUI elements like buttons, text fields, and labels that can be placed on the stage as part of the project's interface (independent of sprites). In standard Scratch, the primary way to get user input is via the "ask and wait" popup or key presses, and to display text either via sprites or "say" bubbles. CreatiCode's widgets allow more flexible, app-like UIs to be built. Key widget features:

- Types of Widgets: The platform provides at least Label and Button widgets, and possibly others like Text Input ordropdown. The Widgets category in the block palette lets you add these elements.

For example, one tutorial has the user add a Label widget with the text "Say something in English" to serve as a prompt on screen 110. Another example is adding Buttons for "Start" and "Stop" in a speech recognition demo 111. The presence of dropdown menus in a project is hinted (e.g. a challenge to "Add two dropdown menus so the user can pick languages" in a translator project 112), indicating a dropdown widget exists for selections. These widgets are UI components that appear over the stage.

- Adding and Positioning Widgets: When a widget is added via a block (e.g. an "add label widget" block), it appears on the stage. CreatiCode provides a Widget Positioning Tool (a drag-and-resize interface) that allows users to manually place the widget and set its size 113. As you drag the widget or its corners, the corresponding position and size parameters in the widget's block update automatically 114. This live adjustment makes designing the layout easier. Widgets use stage coordinates (and possibly percentages for sizing) for placement.  
- Styling Widgets: There are blocks to set widget properties like text content, font size, color, and background. In the voice translator example, after adding the label, they use blocks to "set background to transparent" and "set text size larger" for that label 115. Likely, each widget block (like "add label") returns an identifier (or the widget's name is used) which subsequent blocks reference (e.g. "set [widgetName] text to ..., "set [widgetName] font size to ..., etc.). The user can select the widget from a dropdown in those setter blocks once it's created 116. This is similar to how Scratch's video or pen blocks work (except here we refer to specific widget instances).  
- Interacting with Widgets: For buttons specifically, there are event blocks or reporters to handle clicks. A button widget likely has an associated hat block like "when [buttonName] clicked" or at least a reporter "widget [buttonName] clicked?" In absence of seeing the exact block, we infer this from forum discussions - e.g., users requested a block "name of widget last clicked" for identifying which widget was clicked most recently 117. The speech recognition example uses two buttons for start/stop, which probably rely on when clicked events to call start speech recognition and end speech recognition respectively 111. This indicates that clicking a widget triggers scripts in the project.  
- Dynamic Updates: Widgets can be updated during runtime. For example, after recognizing speech, the program uses a block to set the label's text to the recognized phrase 118. This updates the on-screen label to show the transcribed speech. Similarly, in a translator, after translation the code updates a second label's text to show the translated sentence 119. The widgets act like UI output elements that can reflect changing variables.  
- Use Cases: With widgets, projects can have a more polished interface: instructions labels, score displays, input fields for player name, on-screen buttons to control the game (useful on touchscreen devices where keyboard isn't available), sliders to adjust parameters, etc. Essentially, this brings some simple UI design into Scratch-style projects, turning them into mini-apps. The AI curriculum uses widgets in projects such as the voice translator (labels for prompts and outputs, perhaps a dropdown to choose languages) 120 119. The presence of a "label widget" and references to text boxes suggests a "text input" widget might exist as well (since one tutorial shows the recognized speech being displayed in a text box). This opens possibilities like chat log windows, form inputs, etc., which go beyond Scratch's native capabilities.

In summary, the `Widgets` extension in `CreatiCode` enables creating custom user interfaces (buttons, labels, etc.) that make projects feel more like real applications. They are added and controlled with specialized blocks (add, set text, on click, etc.), and they integrate seamlessly with the rest of the code (e.g. you can combine widget input with AI output: taking a text from a text field, translating it, and then showing it in another label).

# Multiplier Online Games

CreatiCode simplifies the creation of multiplayer networked games – a feature far outside the scope of vanilla Scratch. Using a provided game server and a set of high-level blocks, students can make projects where multiple people can join and play together over the internet 121 . The platform handles the low-level networking, allowing users to focus on game logic. Key aspects:

- Game Server and Rooms: CreatiCode runs a central game server that coordinates games and players  $^{122}$ . Projects can create a game room (like a session) on this server and other users can join it. The server relays messages between all instances of the project so they stay in sync  $^{123}$ .  
- Creating a Game (Host): A "create game" block (in the Multiplayer extension) allows a project to start hosting a game session  $^{124}$ . The host can provide:  
A Game Name (identifier for others to find the game) 125.  
- An optional Password (so only players who know it can join) 126 - default is "123" if not changed.  
- The host's Display Name (how the player will be named in the game) 127.  
- A Role for the host 128 - roles can be any string that the game uses to distinguish players (e.g. "red team" vs "blue team", or "seeker" vs "hider"). It's up to the game's design.  
- Choice of Server location (the server infrastructure might have multiple regional servers; host picks one, and joiners must use the same) 129.  
- Capacity (max number of players allowed in the game) 130.  
- World dimensions (width/height) if the game world is larger than the stage, to manage out-of-bounds movement in multiplayer 131.

When this block runs, it registers a new game room on the server. Only one game can be hosted per user per project at a time (starting another would end the first)  $^{132}$ . Also, idle games auto-close after a few minutes of no activity to free resources  $^{133}$ .

Listing and Joining Games: There is a block to list all available games for a given project/server 134 . This block outputs a table variable containing info on each open game (rows might include game name, host name, number of players, etc.) 135 . A player who wants to join can use this to populate a menu or just to decide which game to join.

To join a game, a corresponding block is used, providing the required details: Game Name, Host Name (from the list or known), Server, Password, plus the joining player's own Display Name and chosen Role 136 137 . If the info matches an existing open game, the player will connect to that game room on the server.

Under the hood, the project on that player's side now knows it's in a multiplayer context and can communicate with others.

- Synchronizing Game State: CreatiCode's multiplayer API likely provides blocks for sending and receiving data among players. Common ones include:  
- Broadcasting a message to all players (synchronously)  $^{138}$  - e.g. "broadcast message to all" which sends a signal to every instance so they can all run some event (like resetting positions, spawning an enemy, etc.). A forum snippet suggests a block that makes a sprite change costume on all players' screens at once via a synchronous broadcast  $^{139}$ .  
- Sending data to specific players or to the server (perhaps "send [value] to player [X]" or similar).  
- Reading player info, like a list of players in the game (there is mention of a block to list players and their roles in the room, likely returns a table of players) 140.  
- Possibly, shared variables or cloud variables that sync across players. Scratch itself has cloud variables (which in Scratch are global across all plays, not per game room), but CreatiCode might repurpose or extend that concept for game-specific state.

The Multiplayer blocks count (~a dozen) suggests a manageable API covering creating/joining games, sending/receiving messages, and maybe synchronized variables  $^{141}$ . The platform's forum indicates that you can sync numeric variables quite easily and even had a separate older Cloud variable system, but multiplayer is now the preferred method for interactive multi-user projects  $^{142}$ .

- Use Cases: With minimal code, students can implement games like chat rooms, multiplayer pong, races, collaborative drawing, etc. For example, one could make a 2-player pong where one player's paddle is controlled by the guest and the other by the host, with ball position synced. CreatiCode's documentation even references projects like a 2-player 3D Doom game  $^{143}$ , showing the potential complexity available. Another scenario: a project where players join and their sprites appear as clones on each others' screens, moving in real-time – all handled by these blocks rather than manual server programming. This is an introduction to networked programming concepts within a familiar interface.

Overall, the Multiplayer extension provides a kid-friendly way to create online multiplayer experiences, which is a rare capability in educational coding platforms. It's abstracted enough that "most types of multiplayer games [can be built] using a dozen blocks" 141 , which lowers the barrier significantly. It teaches about hosts, guests, and messaging in a visual way, and it's backed by CreatiCode's server infrastructure to handle the heavy lifting.

# Data and Cloud Features (Table Variables and Cloud Data)

CreatiCode introduces more advanced data structures and cloud connectivity than vanilla Scratch:

- Table Variables: Unlike Scratch, which only has single-value variables and one-dimensional lists, CreatiCode provides Table variables to handle tabular (2D) data. A table is essentially like a spreadsheet or database table that can store rows and columns of values. We saw their use in AI blocks: the hand detection auto-created a table variable "i" to store many rows of hand landmark data  $^{98}$ . But users can also create and manipulate their own tables:  
- One can create a new empty table (likely via Data blocks or a special "make table" block).  
- There are blocks to insert rows, delete rows, set cell values, get cell values by row/column.  
- Blocks like row count of [table] report the number of rows, as used in tutorials to check if any data is present (e.g. if table row count > 0 means at least one hand detected) 149.  
- Possibly blocks to search or filter table entries.

Tables are extremely useful for structured data. For instance, a student could use a table to store high scores (multiple columns like name and score), or to handle inventory in a game (each row an item with properties), or to log sensor data over time. In the curriculum, tables are taught when introducing AI data like pose keypoints 150 151 . They compare tables vs lists conceptually and show how each row can represent an "item" with multiple attributes (columns) 152 153 . By interacting with tables, learners practice more complex data management, akin to arrays of records in traditional programming.

- Cloud Data / Cloud Blocks: CreatiCode originally had Cloud variable blocks (to store data online across sessions or share data among players), and it appears they evolved into or were

supplemented by the Multiplayer system. Forum posts suggest cloud variables were used for things like chat rooms and then replaced by multiplayer for real-time sync 154 142 . However, cloud storage is still present for certain features:

- Projects can store data on the cloud or even in Google Sheets via specialized blocks 155. For example, there might be a block to write to a Google Sheet or a cloud table (useful for a project that logs sensor readings or questionnaire results).  
- Cloud data is also used to simulate real databases in projects. In one unit, students use CreatiCode's cloud blocks to save and retrieve data as part of an app (maybe a simple login or high score list) 156.

There is also a mention of a [fetch] block in forum discussions (fetching web content) 157, which implies the ability to make HTTP requests. If implemented, that allows projects to call web APIs and retrieve information (under appropriate security rules). This would be an advanced tool to bring in external data (weather, facts, etc.) into a project dynamically.

In summary, CreatiCode's data capabilities go beyond Scratch: table variables allow handling complex data easily, and cloud blocks (and multiplayer) enable persistent or shared data storage and communication. These are powerful for creating apps that require saving user progress, multi-user data, or integrating with real-world data sources - expanding the scope of what students can build (e.g., a collaborative app or a simple social platform project).

# CreatiCode XO - AI Project Assistant

Aside from blocks that go inside projects, CreatiCode also features CreatiCode XO, an AI-powered assistant to help users during project development. XO is essentially an integrated chat assistant that has knowledge of CreatiCode and coding, aimed at guiding students in designing and troubleshooting projects. Notably:

- Purpose of XO: Starting a big project can be daunting, so XO is there to provide suggestions and guidance  $^{158}$ . XO has "seen" many projects (likely meaning it's trained on data of Scratch/CreatiCode projects and tutorials) and can offer advice on how to implement an idea  $^{158}$ . It's like a mentor that students can ask, "How do I make X?", and it will outline a plan.  
- Project Design Help: Students can ask XO questions like "How to build a 3D platformer game?" and XO will generate a structured project outline  $^{159}$ . The responses usually include an overview, key components needed (sprites, backdrops, etc.), major steps to implement each part, and links to relevant tutorials or demo projects if available  $^{160}$ . This helps students break down complex projects into manageable steps.  
- Interactive Guidance: XO encourages an iterative dialogue. If the user provides only a very brief prompt, XO's suggestions will be generic; but if the user includes more specific details about their idea, XO's suggestions become more tailored  $^{161}$ $^{162}$ . For example, specifying game mechanics (like "an alien that can jump and platforms that move" in a platformer request) yields a more detailed and "original" plan from XO  $^{163}$ .  
- Limited Scope (Not Autopilot): XO is intentionally constrained to not just do the whole project for the student  $^{164}$ . It won't output full code; in fact, if asked to produce all the code, it will likely refuse or give a high-level answer  $^{165}$ . XO is optimized for short answers - giving hints, explaining concepts, suggesting next steps - rather than lengthy code dumps  $^{164}$ . This is by design: the goal is

to support learning rather than replace it. The platform emphasizes that students should use XO as an assistant, not a crutch, and that their own creativity and effort are key to actually build the project 166.

# - Use Cases for XO:

- Brainstorming: If a student doesn't know what to make, they can ask "Give me some project ideas to practice chatGPT blocks," and XO will list a few creative project prompts 167 168.  
- Step-by-step help: After getting an outline, a student can ask more granular questions like "How do I implement the first step?" and XO will help with that part specifically 169 170 . Then the student can proceed, and ask about the next step, and so on - effectively using XO as a pair programmer that focuses on one piece at a time.  
- Debugging/Explaining: Although not explicitly described above, XO could presumably answer "why doesn't this code work?" or general coding questions, given it's integrated and knows CreatiCode's blocks. (It likely has knowledge base context to answer common questions about block usage.)  
- AI Knowledge Base: XO's advice is based on a "vast database of project insights" 171. It likely incorporates CreatiCode's knowledge base content and example projects. For instance, XO would know about the new block categories and how they're used, which is valuable since some of these features (like multiplayer or 3D) are unique to CreatiCode. XO can point users to relevant tutorials or documentation (the outlines sometimes explicitly include tutorial links if available 160).

XO is essentially a built-in tutor. It represents CreatiCode's commitment to AI literacy not just by giving AI blocks to use, but by using AI to enhance the learning process itself. By interacting with XO, students practice formulating questions and prompts (a skill in itself) and get guided help. This aligns with the curriculum's focus on integrating AI into education thoughtfully 172.

# Sources:

- Computing and AI for All - Overview of the CreatiCode platform's capabilities 1 .  
- CreatiCode Forum - List of new block categories introduced (AI, 3D, etc.)  ${}^{2}$  .  
- ECforALL Curriculum (Act 4) - Description of integrating ChatGPT ("Chat with Einstein") and CreatiCode XO AI tools 49.  
- CreatiCode Knowledge Base - Details on the OpenAI ChatGPT request block and its parameters 38  
- CreatiCode Tutorials - Using AI image generation for backdrops and sprites, and emphasis on prompt detail and moderation 54 60.  
- CreatiCode Knowledge Base - Speech recognition blocks (start speech recognition, etc.) and their usage 174 175.  
- CreatiCode Knowledge Base - AI text-to-speech ("AI Speaker") block with voice/language options and controls 84 85.  
- CreatiCode AI Tutorial - Hand detection block usage and the data table of hand landmarks (finger curl angles) 97 100.  
- ECforALL Curriculum (Act 4) - Lessons on video sensing and hand/body tracking in CreatiCode (motion detection, pose data in tables) 7 151.

- CreatiCode Forum - Multiplayer extension overview, creating/joining game blocks and game listing 141 176.  
- CreatiCode Forum - 2D physics engine introduction and gravity initialization block 32 177.  
- CreatiCode Forum - Virtual joystick for 3D games (adding and reading joystick blocks) 21 22.  
- CreatiCode Forum - XO AI assistant usage and philosophy (project outline generation and its limits) 158 165.

# 1 CAI - Overview

https://www.computingandaiforall.org/

2 28 158 159 160 161 162 163 164 165 166 167 168 169 170 171 CreatiCode XO (AI Assistant) - New Project

Design | CreatiCode Scratch Forum

https://forum creaticode.com/topic/1103/creaticode-xo-ai-assistant-new-project-design

3 4 5 6 7 8 9 10 49 68 94 95 102 103 104 144 145 146 147 148 150 151 152 153 155 156 172 Act 4 |

https://www.curriculum.elemententarycomputingforall.org/act4

11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 Knowledge Base | CreatiCode Scratch Forum

https://www/forum creticode.com/category/2/knowledge-base

26 Need help learning creticode features : r/scratch - Reddit

https://www.reddit.com/r/scratch/comments/1mnus7c/need_help_learningCreaticode_features/

27 CreatiCode - Scratch + AI + 3D

https://creativecommons.com/

29 30 31 32 33 37 177 Physics Engine for 2D Projects | CreatiCode Scratch Forum

https://forum.creaticode.com/topic/805/physics-engine-for-2d-projects

34 Use Forces in 2D Physics | CreatiCode Scratch Forum

https://forum.creaticode.com/topic/818/use-forces-in-2d-physics

35 Collision Groups in 2D Physics | CreatiCode Scratch Forum

https://forum.creaticode.com/topic/841/collision-groups-in-2d-physics

36 Welded Blocks | CreatiCode Scratch Forum

https://forum.creaticode.com/topic/1543/welded-blocks

38 39 40 41 42 43 44 45 46 47 53 173 AI - OpenAI ChatGPT | CreatiCode Scratch Forum

https://forum creaticode.com/topic/867/ai-openai-chatgpt

ChatGPT AI: Chat with Einstein (Difficulty: 3)

https://forum.creaticode.com/topic/925/chatgpt-ai-chat-with-einstein-difficulty-3

51 ChatGPT AI - Ask Me Anything! (Difficulty: 1)

https://forum.creaticode.com/topic/1776/chatgpt-ai-ask-me-anything-difficulty-1

54 55 56 57 58 59 60 61 64 65 66 Search or Generate Backdrop Images Using AI | CreatiCode Scratch

# Forum

https://www/forum Creatorode.com/topic/1153/search-or-generate-backdrop-images-using-ai/1

Search or Generate Sprite Images Using AI | CreatiCode Scratch Forum

https://www/forum.creaticode.com/topic/1154/search-or-genrate-sprite-images-using-ai/1

69 70 71 72 73 74 75 76 77 78 79 80 111 174 175 Speech to Text | CreatiCode Scratch Forum

https://forum.creaticode.com/topic/338/speech-to-text

81 Learning Pathway for AI Coding | CreatiCode Scratch Forum

https://forum.creaticode.com/topic/1569/learning-pathway-for-ai-coding

82 110 112 113 114 115 116 118 119 120 AI - A Voice Translator (Difficulty: 2) | CreatiCode Scratch Forum

https://forum.creaticode.com/topic/342/ai-a-voice-translator-difficulty-2

83 84 85 86 87 88 89 90 91 92 Say Sentences with an AI Speaker | CreatiCode Scratch Forum

https://forum.creaticode.com/topic/341/say-sentences-with-an-ai-speaker/1?lang  $\equiv$  en-US

93 A new video tutorial was posted on how to make a sprite talk to us ...

https://www.facebook.com/creaticode2021/posts/a-new-video-tutorial-was-posted-on-how-to-make-a-sprite-talk-to-us-using-chatgpt/449166404303550/

96 97 98 99 100 101 105 106 107 149 AI - Counting Fingers with Hand Detection (Difficulty 3) | CreatiCode Scratch Forum

https://forum.creaticode.com/topic/728/ai-counting-fingers-with-hand-detection-difficulty-3

108 109 143 Tutorials | CreatiCode Scratch Forum

https://www/forum creaticode.com/category/17/tutorials

117 new block ideas | CreatiCode Scratch Forum

https://forum.creaticode.com/topic/1322/new-block-ideas

121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 140 141 176 Multiplayer Network Games - Creating and Joining Games | CreatiCode Scratch Forum

https://forum.creaticode.com/topic/1086/multiplayer-network-games-creating-and-joining-games

138 139 Multiplayer Network Games - Broadcasting Messages to All

https://forum.creaticode.com/topic/1090/multiplayer-network-games-broadcasting-messages-to-all

142 Tyller_ | CreatiCode Scratch Forum

https://forum.creaticode.com/user/tyller_

154 Cloud Blocks dont work | CreatiCode Scratch Forum

https://forum.creaticode.com/topic/1199/cloud-blocks-dont-work

157 Topics tagged under "cloud-blocks" | CreatiCode Scratch Forum

https://forum.creaticode.com-tags/cloud-blocks
