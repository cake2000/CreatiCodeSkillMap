# T19 – Algorithmic Art & Creative Coding
# GRADES 7 & 8 - IMPROVED VERSION
# Generated: 2025-12-02

## GRADE 7 SKILLS (Advanced Algorithms & Systems - 28 skills)

### PERFORMANCE & OPTIMIZATION (Skills 01-03)

ID: T19.G7.01
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Compare efficiency of two art algorithms that produce the same output
Description: Students evaluate two code samples that draw the same design but with different performance characteristics. They identify which uses fewer operations, has better loop structure, or avoids redundant calculations. They choose the more efficient approach and justify why based on operation count or execution time. They measure performance differences using console logging or timing.

Dependencies:
* T19.G6.01: Trace variable values through an art algorithm
* T07.G6.06: Fix a loop that runs too many or too few times







ID: T19.G7.02
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Optimize rendering by reducing redundant calculations
Description: Students identify and eliminate redundant calculations in art algorithms. They store frequently-used values in variables instead of recalculating (e.g., calculate cos/sin once per angle), move invariant calculations outside loops, and precompute lookup tables for complex functions. They measure performance improvement before and after optimization.

Dependencies:
* T19.G7.01: Compare efficiency of two art algorithms that produce the same output
* T09.G6.01: Model real-world quantities using variables and formulas







ID: T19.G7.03
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Profile art algorithms to identify bottlenecks
Description: Students use timing blocks and console logging to measure execution time of different algorithm sections. They identify performance bottlenecks (slowest sections), analyze why certain operations are slow (nested loops, complex math), and prioritize optimization efforts on the most impactful sections. They understand the profiling → optimization cycle.

Dependencies:
* T19.G7.02: Optimize rendering by reducing redundant calculations
* T12.G6.01: Trace complex code with multiple variables







### ADVANCED GENERATIVE TECHNIQUES (Skills 04-11)

ID: T19.G7.04
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Implement L-system string generation
Description: Students implement L-system (Lindenmayer system) rules by starting with an axiom string and repeatedly applying replacement rules. They understand that L-systems use string rewriting: each character is replaced according to rules (e.g., "A" → "AB", "B" → "A"). They generate strings through multiple iterations and see how simple rules create complex patterns. They implement rules for algae growth, binary trees, and fractal curves.

Dependencies:
* T19.G6.09: Create spirograph patterns with parametric equations
* T10.G6.02: Manipulate text with string operations







ID: T19.G7.05
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Draw L-system fractal trees
Description: Students translate L-system strings into visual patterns by interpreting characters as turtle graphics commands (F = forward, + = turn left, - = turn right, [ = save position/angle, ] = restore position/angle). They implement a stack-based drawing system to handle branching. They draw fractal trees, Koch curves, and Sierpinski triangles by processing the generated strings. They see how recursive rules create self-similar patterns.

Dependencies:
* T19.G7.04: Implement L-system string generation
* T11.G7.02: Understand recursive thinking through examples







ID: T19.G7.06
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Implement elementary cellular automaton rules
Description: Students create a rule lookup system that maps each 3-cell neighborhood pattern (000, 001, 010, ..., 111) to a next-state value (0 or 1). They implement rule numbers (e.g., Rule 30, Rule 110) by converting the rule number to its 8-bit binary representation and storing results in a list. They test their lookup by manually tracing specific neighborhood patterns.

Dependencies:
* T19.G6.04: Use variables and conditionals to branch designs
* T10.G6.03: Implement algorithms using 2D tables







ID: T19.G7.07
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Generate cellular automaton evolution patterns
Description: Students use their rule lookup table to generate new rows from previous rows. They iterate through each cell, extract its 3-cell neighborhood, look up the next state, and build the new row. They stack multiple generations vertically to visualize the automaton's evolution over time. They observe how different rules produce distinct emergent patterns (stable, chaotic, complex).

Dependencies:
* T19.G7.06: Implement elementary cellular automaton rules







ID: T19.G7.08
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Visualize 2D cellular automaton patterns
Description: Students implement 2D cellular automata (Game of Life variants, other neighborhood rules). They draw the 2D grid of cells using nested loops, apply rules based on 8-neighbor counts (Moore neighborhood) or 4-neighbor counts (von Neumann neighborhood), and animate the evolution. They experiment with different initial patterns (gliders, oscillators, still lifes) and rules to create dynamic algorithmic art.

Dependencies:
* T19.G7.07: Generate cellular automaton evolution patterns
* T19.G6.15: Create 3D patterns with mathematical formulas







ID: T19.G7.09
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Create agent-based generative art systems
Description: Students design and implement art systems where multiple autonomous agents follow simple rules to create collective patterns. Each agent has position, direction, and drawing state. Agents move according to rules (bounce off boundaries, avoid neighbors, follow trails) and leave visual marks. Students observe emergent patterns from simple individual behaviors. This introduces swarm intelligence concepts through art.

Dependencies:
* T19.G6.04: Use variables and conditionals to branch designs
* T10.G6.03: Implement algorithms using 2D tables







ID: T19.G7.10
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Implement flocking behavior for artistic patterns
Description: Students implement Craig Reynolds' flocking algorithm with three rules: separation (avoid crowding neighbors), alignment (steer toward average heading of neighbors), and cohesion (steer toward average position of neighbors). They create visual art from flocking agents that leave trails, vary color by velocity, or change brush size by proximity to neighbors. They understand how simple behavioral rules create organic, flowing patterns.

Dependencies:
* T19.G7.09: Create agent-based generative art systems
* T09.G7.01: Use distance formula to calculate distance between points







ID: T19.G7.11
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Combine multiple generative techniques in one artwork
Description: Students integrate two or more generative techniques (e.g., L-system trees with flocking birds, cellular automata patterns as color maps for particle systems, or fractal geometry combined with physics simulation) in a single cohesive project. They identify how one technique can inform another and implement the connections. They create layered, complex generative art that showcases technical mastery.

Dependencies:
* T19.G7.05: Draw L-system fractal trees
* T19.G7.10: Implement flocking behavior for artistic patterns







### PARTICLE SYSTEMS (Skills 12-14)

ID: T19.G7.12
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Configure advanced particle emitter properties
Description: Students create particle emitters with sophisticated property control: color gradients over particle lifetime (start color → end color), size changes (start size → end size), alpha/transparency fading, velocity ranges, emission rates, and particle lifetime. They understand how each property affects visual appearance and combine settings to create fire, smoke, magic, water, and abstract effects.

Dependencies:
* T19.G6.10: Apply color materials to 3D shapes
* T19.G5.04: Animate a pattern with a counter variable







ID: T19.G7.13
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Control particle emitter position algorithmically
Description: Students move particle emitters programmatically using loops and formulas. They create emitters that trace paths (circular, spiral, wavy), follow mathematical curves, or respond to interactive input. They understand that moving the emission source creates particle trails and flowing effects. They combine multiple moving emitters to create complex particle-based compositions.

Dependencies:
* T19.G7.12: Configure advanced particle emitter properties
* T19.G6.07: Apply cosine functions to create circular patterns







ID: T19.G7.14
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Create particle-based generative art installations
Description: Students design standalone particle-based algorithmic art by combining color gradients, size changes, emission patterns, and algorithmic movement. They use particle systems to create effects like flowing energy streams, abstract motion paintings, or dynamic visualizations. They control aesthetic qualities (density, color harmony, motion quality) through systematic parameter adjustment.

Dependencies:
* T19.G7.13: Control particle emitter position algorithmically







### 3D ART & LIGHTING (Skills 15-19)

ID: T19.G7.15
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Add and position lights in 3D algorithmic art
Description: Students add different light types (point, directional, ambient) to their 3D generative art. They understand that point lights emit in all directions from a position, directional lights have parallel rays like sunlight, and ambient lights provide base illumination. They position lights using coordinates and control light color and intensity. They observe how lighting reveals 3D form and creates mood.

Dependencies:
* T19.G6.10: Apply color materials to 3D shapes
* T19.G5.15: Create 3D patterns with mathematical formulas







ID: T19.G7.16
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Position lights algorithmically to highlight 3D patterns
Description: Students place lights at calculated positions to emphasize specific parts of their 3D art. They use formulas to position lights relative to shape positions, create multiple lights in loops at symmetrical positions, and implement orbiting light sources. They understand how light direction creates shadows and highlights that reveal form and depth.

Dependencies:
* T19.G7.15: Add and position lights in 3D algorithmic art







ID: T19.G7.17
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Create mood with colored and dynamic lighting
Description: Students use light colors, intensities, and positions as artistic tools to create atmosphere. They create warm atmospheres (orange/yellow lights), cool atmospheres (blue/cyan lights), dramatic contrast (bright key light with dim fill), or mysterious effects (single colored spotlight). They animate lighting properties over time to create dynamic mood changes in their 3D art.

Dependencies:
* T19.G7.16: Position lights algorithmically to highlight 3D patterns
* T19.G5.04: Animate a pattern with a counter variable







ID: T19.G7.18
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Generate custom 3D shapes from vertex lists
Description: Students create original 3D shapes by calculating vertex positions using algorithms. They use loops to calculate x, y, z coordinates for each vertex based on mathematical formulas (parametric surfaces, revolution solids, extruded profiles). They store positions in nested lists and use these vertex lists with 3D shape creation blocks to generate unique geometric art beyond standard primitives.

Dependencies:
* T19.G6.13: Create 3D curves from calculated point lists
* T10.G6.03: Implement algorithms using 2D tables







ID: T19.G7.19
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Combine 3D shapes, lighting, and particle effects
Description: Students create comprehensive 3D sculptures by integrating algorithmic 3D shape placement, dynamic lighting, and particle systems. They emit particles from shape positions, attach particle trails to moving 3D objects, use lighting to highlight key shapes, or create immersive environments. They understand how combining techniques creates rich, professional-quality generative art.

Dependencies:
* T19.G7.17: Create mood with colored and dynamic lighting
* T19.G7.14: Create particle-based generative art installations







### INTERACTIVE & MULTIMODAL ART (Skills 20-24)

ID: T19.G7.20
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Create sound-reactive visualizations
Description: Students use the "loudness" sensing block to detect sound levels and map them to multiple visual parameters simultaneously. They create art where louder sounds trigger bigger shapes, brighter colors, faster particle emission, and more intense lighting. They implement smoothing techniques to prevent jerky visual changes and create visualizations that feel musically connected to the audio input.

Dependencies:
* T19.G5.19: Create sound-reactive art with microphone input
* T19.G7.17: Create mood with colored and dynamic lighting







ID: T19.G7.21
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Create body-tracking interactive installations
Description: Students use CreatiCode's body tracking blocks to detect full body pose keypoints and create large-scale interactive art installations. They read body keypoint positions (head, shoulders, elbows, hands, hips, knees, feet) from the tracking table and use them to control visual elements. They create art where the viewer's entire body becomes the interface, mapping body posture to colors, shapes, animations, or particle emissions.

Dependencies:
* T19.G6.16: Use finger gestures to control art parameters
* T10.G6.03: Implement algorithms using 2D tables







ID: T19.G7.22
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Implement gesture-based art control systems
Description: Students design and implement gesture recognition for art control. They detect specific body poses or hand configurations (arms raised, hands together, specific finger counts) and map them to discrete art actions (change color palette, trigger animation, reset canvas). They implement gesture filtering to avoid false triggers and provide visual feedback when gestures are recognized.

Dependencies:
* T19.G7.21: Create body-tracking interactive installations
* T08.G6.03: Use conditionals to control simulation steps







ID: T19.G7.23
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Generate AI sprites with algorithmic prompts
Description: Students use AI image generation blocks to create sprites from text prompts that they construct algorithmically. They build prompts by combining variables and lists (e.g., randomly selecting adjectives and subjects) to generate varied AI sprites. They use loops to generate multiple unique AI-created elements and integrate these AI-generated assets into algorithmic compositions. They explore AI as a generative art tool.

Dependencies:
* T19.G6.04: Use variables and conditionals to branch designs
* T20.G5.03: Build a prompt with variables for AI image generation







ID: T19.G7.24
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Create physics-driven generative art
Description: Students use CreatiCode's 2D physics engine to create art where physical forces drive visual compositions. They configure gravity, friction, bounciness, and density to control how art elements move and settle. They create constraint-based sculptures where physics determines final arrangements, collision-driven paint splatter effects, pendulum-based drawing machines, and falling-object patterns. They understand that physics rules are another form of algorithmic art.

Dependencies:
* T19.G7.09: Create agent-based generative art systems
* T08.G6.03: Use conditionals to control simulation steps







### DESIGN & AESTHETICS (Skills 25-28)

ID: T19.G7.25
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Apply color theory principles in algorithmic palettes
Description: Students implement algorithmic color selection based on color theory: complementary colors (opposite on hue wheel: hue and hue+180), analogous colors (adjacent hues: hue, hue+30, hue+60), triadic schemes (three evenly spaced hues: hue, hue+120, hue+240), and split-complementary. They calculate colors mathematically from a base hue and apply these harmonious palettes to their generative art. They evaluate how color relationships affect visual harmony.

Dependencies:
* T19.G6.10: Apply color materials to 3D shapes
* T09.G6.01: Model real-world quantities using variables and formulas







ID: T19.G7.26
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Study parameter impact on aesthetic qualities
Description: Students create a parameterized art piece with exposed controls (sliders for randomness, angle change, speed, density, color variation). They systematically adjust each parameter one at a time and document in a table how each change affects specific aesthetic qualities (symmetry, balance, density, motion, color harmony). They analyze which parameters have the strongest visual impact and explain why certain combinations create successful compositions.

Dependencies:
* T19.G7.25: Apply color theory principles in algorithmic palettes
* T09.G6.01: Model real-world quantities using variables and formulas







ID: T19.G7.27
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Implement compositionally balanced layouts algorithmically
Description: Students implement algorithms that consider visual composition principles: rule of thirds placement (divide canvas into 3x3 grid, place elements at intersections), golden ratio proportions (1.618:1 relationships), visual weight distribution (balance heavy/light elements), and focal point creation. They use mathematical formulas to position elements at compositionally strong locations and compare algorithmic compositions to intuitive human compositions.

Dependencies:
* T19.G7.26: Study parameter impact on aesthetic qualities
* T09.G7.01: Use distance formula to calculate distance between points







ID: T19.G7.28
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Recreate simplified versions of professional generative artworks
Description: Students examine professional algorithmic art or natural patterns (examples: Vera Molnár's grid disruptions, Manfred Mohr's hypercube projections, fractal geometry in nature, Bridget Riley's op art) and create simplified CreatiCode implementations. They identify the likely loops, math formulas, randomness parameters, and color systems, then build working code that approximates the original. They compare their output to the reference and iterate to improve the match.

Dependencies:
* T19.G7.27: Implement compositionally balanced layouts algorithmically
* T19.G6.09: Create spirograph patterns with parametric equations







## GRADE 8 SKILLS (Expert Techniques & Theory - 35 skills)

### ADVANCED DATA VISUALIZATION (Skills 01-03)

ID: T19.G8.01
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Implement multi-dimensional data mapping
Description: Students implement sophisticated algorithms to process complex datasets with 4+ attributes and map them to multiple visual channels simultaneously (size, color, motion speed, position, rotation, opacity, shape type). They use custom scaling functions to normalize different data ranges to visual ranges. They handle edge cases (missing data, outliers) and implement optimization strategies for larger datasets (data sampling, progressive rendering). This goes beyond G6 by handling more dimensions and considering performance.

Dependencies:
* T19.G6.05: Implement multi-field data visualization
* T10.G7.02: Implement algorithms using complex nested data structures







ID: T19.G8.02
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Create real-time data-driven art systems
Description: Students design art systems that visualize live or simulated data feeds: weather data affecting color palettes, time-of-day influencing lighting and composition, simulated sensor streams driving shape generation, or stock values determining growth patterns. They implement data polling patterns, smooth transitions between data states, fallback visuals when data is unavailable, and clear visual encoding that reveals data patterns.

Dependencies:
* T19.G8.01: Implement multi-dimensional data mapping
* T09.G7.01: Use distance formula to calculate distance between points







ID: T19.G8.03
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Design accessible data visualizations
Description: Students apply accessibility principles to data art: colorblind-safe palettes (avoid red-green), high contrast for readability, redundant encoding (use both color and shape to indicate categories), clear labeling, and adjustable parameters for individual needs. They test visualizations with simulated vision modes and evaluate whether data patterns remain clear under different viewing conditions.

Dependencies:
* T19.G8.01: Implement multi-dimensional data mapping
* T05.G6.01: Apply empathy, needs, and accessibility checklist to a design







### PROCEDURAL GENERATION & NOISE (Skills 04-08)

ID: T19.G8.04
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Implement value noise for organic patterns
Description: Students implement basic value noise by generating random values at grid points and interpolating between them. They use linear interpolation (lerp) or smooth interpolation (smoothstep, cosine interpolation) to create continuous gradients from discrete random samples. They apply noise values to control color, position offsets, or size variations, creating organic-looking patterns that avoid the harshness of pure randomness. They understand noise as structured randomness.

Dependencies:
* T19.G7.11: Combine multiple generative techniques in one artwork
* T10.G7.02: Implement algorithms using complex nested data structures







ID: T19.G8.05
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Layer multiple noise octaves for detail
Description: Students combine multiple layers of noise at different scales (octaves) to create rich, detailed patterns. They add high-frequency noise for fine detail and low-frequency noise for large-scale variation. They control amplitude and frequency per octave using multipliers (typically halving amplitude and doubling frequency each octave). They create fractal-like patterns (fbm - fractional Brownian motion) for natural textures like clouds, terrain, wood grain, or marble.

Dependencies:
* T19.G8.04: Implement value noise for organic patterns







ID: T19.G8.06
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Apply noise to modulate art parameters
Description: Students use noise values to modulate various art parameters across their compositions: color hue shifts create flowing color transitions, line thickness variation adds organic quality, shape displacement creates natural movement, rotation offsets introduce subtle asymmetry. They map noise output ranges (-1 to 1 or 0 to 1) to appropriate parameter ranges. They create cohesive organic variation across entire compositions using spatially coherent randomness.

Dependencies:
* T19.G8.05: Layer multiple noise octaves for detail







ID: T19.G8.07
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Implement flow field navigation for particles
Description: Students create a 2D grid of direction vectors (angles stored in a table) that guide particle movement. Particles sample the flow field at their current position to determine movement direction. They populate the flow field using noise functions (Perlin-like noise) or mathematical formulas (sine/cosine combinations). They create organic, flowing motion paths that look natural and cohesive, with smooth particle trajectories following invisible vector fields.

Dependencies:
* T19.G8.06: Apply noise to modulate art parameters
* T19.G7.14: Create particle-based generative art installations







ID: T19.G8.08
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Animate flow fields for dynamic visualizations
Description: Students animate flow fields by slowly changing the underlying direction vectors over time. They use time-varying noise (3D noise with z=time) or rotating angle offsets to create hypnotic, ever-changing flow patterns. They balance change rate with visual coherence—too fast creates chaos, too slow feels static. They create mesmerizing visualizations where particles continuously adapt to shifting invisible forces.

Dependencies:
* T19.G8.07: Implement flow field navigation for particles







### 3D ART & MATERIALS (Skills 09-12)

ID: T19.G8.09
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Apply procedural textures to 3D materials
Description: Students apply their procedurally-generated noise and pattern algorithms to 3D shape materials. They map calculated patterns to material properties: color (base color from noise), roughness (noise controls surface shininess variation), emission (glowing patterns), or alpha (transparency patterns). They create unique 3D sculptures with custom algorithmic surfaces that go beyond pre-made texture libraries.

Dependencies:
* T19.G8.06: Apply noise to modulate art parameters
* T19.G6.12: Apply roughness properties to 3D materials







ID: T19.G8.10
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Implement dynamic lighting systems
Description: Students create sophisticated lighting that changes over time or responds to art parameters. They animate light positions in loops (orbiting, oscillating), adjust light colors based on data or music, create pulsing or flickering light intensity, and implement color cycling. They coordinate multiple dynamic lights that interact with their 3D algorithmic sculptures, creating atmospheric and dramatic effects. They understand lighting as a temporal art element.

Dependencies:
* T19.G7.17: Create mood with colored and dynamic lighting
* T19.G6.04: Use variables and conditionals to branch designs







ID: T19.G8.11
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Create immersive 360° or VR-ready 3D art environments
Description: Students design 3D algorithmic art environments that surround the viewer, using spherical camera concepts. They position shapes, lights, and effects in all directions around the camera origin (not just in front). They consider how the viewer will explore the space and create art experiences that reward looking in different directions. They implement camera rotation controls and design immersive experiences that translate to VR/AR platforms.

Dependencies:
* T19.G8.10: Implement dynamic lighting systems
* T19.G7.19: Combine 3D shapes, lighting, and particle effects







ID: T19.G8.12
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Generate procedural 3D forms with mathematical surfaces
Description: Students generate complex 3D shapes using parametric surface equations: torus (circular cross-section revolved around axis), Möbius strip (twisted rectangular strip), Klein bottle (self-intersecting surface), seashells (logarithmic spirals in 3D), and other mathematical surfaces. They implement double-nested loops to generate UV-mapped vertex positions, apply materials and lighting, and create mathematically beautiful 3D art.

Dependencies:
* T19.G7.18: Generate custom 3D shapes from vertex lists
* T19.G6.09: Create spirograph patterns with parametric equations







### PERFORMANCE & SYSTEM DESIGN (Skills 13-17)

ID: T19.G8.13
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Profile rendering performance with timing measurements
Description: Students use timing blocks and frame counters to measure execution time of different algorithm sections. They calculate frames per second (FPS) for animated art and identify performance bottlenecks (slowest sections). They analyze why certain operations are slow (nested loops with heavy calculations, excessive drawing calls, redundant computations) and prioritize optimization efforts on the most impactful sections.

Dependencies:
* T19.G7.03: Profile art algorithms to identify bottlenecks
* T12.G7.01: Trace complex code with multiple variables and functions







ID: T19.G8.14
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Optimize algorithms to achieve target frame rates
Description: Students refactor slow algorithms using optimization techniques: reduce redundant calculations by caching values, decrease loop iterations by increasing step size, batch drawing operations, cull off-screen elements, use simpler approximations for complex math, or implement level-of-detail systems. They profile before and after optimization to measure improvement. They achieve target frame rates (30+ fps for smooth animation) while maintaining visual quality.

Dependencies:
* T19.G8.13: Profile rendering performance with timing measurements
* T07.G7.02: Refactor complex repeated patterns into loops with variables







ID: T19.G8.15
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Analyze computational complexity of art algorithms
Description: Students analyze the time and space complexity of their generative art algorithms using Big-O notation concepts. They identify O(n), O(n²), and O(n³) patterns in nested loops. They predict how performance will scale with increased resolution, particle count, or iteration depth. They make informed algorithm design decisions based on complexity analysis, choosing appropriate structures for their performance requirements.

Dependencies:
* T19.G8.14: Optimize algorithms to achieve target frame rates
* T12.G7.01: Trace complex code with multiple variables and functions







ID: T19.G8.16
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Design art systems with separation of concerns
Description: Students architect large generative art projects by separating concerns: data generation (math/noise), state management (variables/lists), rendering (draw blocks), interaction handling (events/input), and configuration (parameters/settings). They use custom blocks to encapsulate each concern. They design systems where each part can be modified independently, demonstrating software engineering principles in creative coding contexts.

Dependencies:
* T19.G8.02: Create real-time data-driven art systems
* T11.G7.01: Design custom blocks for code organization







ID: T19.G8.17
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Implement modular generative art systems
Description: Students create generative art systems with swappable modules: interchangeable color palette systems, pluggable shape generators, replaceable motion algorithms, and modular composition layouts. They design clear interfaces between modules (defined input/output parameters) so different implementations can be substituted without changing other parts. They demonstrate how modular design enables rapid artistic exploration and system reuse.

Dependencies:
* T19.G8.16: Design art systems with separation of concerns
* T11.G7.01: Design custom blocks for code organization







### AI INTEGRATION & COLLABORATION (Skills 18-21)

ID: T19.G8.18
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Create AI-human collaborative art systems
Description: Students design and implement art systems where AI generation and algorithmic code work together. They use ChatGPT blocks to generate creative descriptions or style suggestions, feed them to AI image generation to create sprites or textures, then algorithmically process or arrange the results (positioning, filtering, compositing). They create art pipelines that combine human-defined algorithms with AI creativity, exploring questions of authorship in hybrid systems.

Dependencies:
* T19.G7.23: Generate AI sprites with algorithmic prompts
* T20.G7.03: Chain AI calls to build multi-step workflows







ID: T19.G8.19
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Implement procedural AI prompt generation
Description: Students create sophisticated algorithms that generate varied AI image prompts using grammar systems, template filling, and constraint-based generation. They implement prompt component libraries (subjects, styles, modifiers, lighting, composition) and combinatorial logic to produce diverse yet coherent prompts. They generate large sets of AI images algorithmically and curate or composite the results into cohesive artworks.

Dependencies:
* T19.G8.18: Create AI-human collaborative art systems
* T10.G7.02: Implement algorithms using complex nested data structures







ID: T19.G8.20
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Build art systems that attribute algorithmic contributions
Description: Students create generative art projects that include metadata documenting what the algorithm vs human artist vs AI contributed. They implement attribution displays (e.g., "Pattern algorithm by [name], AI textures by DALL-E, randomness seed: [value], generated: [timestamp]"). They build systems that let viewers see how much of the output came from random vs deterministic code vs AI generation. This practical approach addresses authorship questions through implementation.

Dependencies:
* T19.G8.18: Create AI-human collaborative art systems
* T05.G7.01: Analyze stakeholder needs for a complex design problem







ID: T19.G8.21
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Use AI assistant to plan and debug generative art
Description: Students use CreatiCode's XO AI assistant or ChatGPT to brainstorm generative art concepts, get suggestions for mathematical formulas and parameter ranges, debug unexpected visual outputs, and refine algorithm structure. They formulate clear questions, evaluate AI suggestions critically, and make final implementation decisions themselves. They learn to use AI as a creative and technical collaborator while maintaining artistic vision and technical understanding.

Dependencies:
* T19.G8.16: Design art systems with separation of concerns
* T20.G7.14: Evaluate and refine AI responses for quality







### INTERACTIVE & MULTIMODAL (Skills 22-25)

ID: T19.G8.22
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Create adaptive art that responds to multiple sensor inputs
Description: Students create sophisticated interactive art installations that respond to multiple input sources simultaneously: combining hand tracking, body tracking, video motion sensing, keyboard, mouse, and microphone inputs. They implement priority systems when inputs conflict, smooth transitions between interaction modes, and contextual responses that adapt to how viewers choose to engage. They design art experiences with rich, multimodal interaction.

Dependencies:
* T19.G7.22: Implement gesture-based art control systems
* T19.G7.20: Create sound-reactive visualizations







ID: T19.G8.23
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Create real-time audio-reactive visualizations
Description: Students build sophisticated art systems that respond to audio input in real-time. They analyze audio into frequency bands (bass/low, mid, treble/high) and map different frequency ranges to distinct visual elements—bass triggers large movements and color shifts, mid-range controls shape density, treble triggers particle bursts or fine details. They implement temporal smoothing, beat detection, and dynamic range compression to create visualizations that feel musically connected.

Dependencies:
* T19.G7.20: Create sound-reactive visualizations
* T19.G8.14: Optimize algorithms to achieve target frame rates







ID: T19.G8.24
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Create speech-controlled art systems
Description: Students use CreatiCode's speech recognition blocks to create art that responds to spoken words and phrases. They implement voice-controlled parameter adjustment ("make it blue", "bigger", "faster"), voice-triggered preset loading ("show me fire", "abstract mode"), and voice-driven generative systems (spoken words influence shape, color, or composition). They design accessible art tools where voice becomes a creative interface, demonstrating multimodal interaction design.

Dependencies:
* T19.G8.22: Create adaptive art that responds to multiple sensor inputs
* T20.G7.08: Build voice-controlled interactions with speech recognition







ID: T19.G8.25
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Design art systems for asynchronous creative contribution
Description: Students create generative art systems that incorporate contributions from multiple sources over time. They design seed systems where initial parameters from different users produce unique variations, implement art that evolves based on accumulated user choices stored in cloud variables, and create collaborative canvases where each viewer's interaction leaves traces that affect future viewers' experiences. They explore distributed creativity in algorithmic art.

Dependencies:
* T19.G8.22: Create adaptive art that responds to multiple sensor inputs
* T19.G8.17: Implement modular generative art systems







### ADVANCED TECHNIQUES (Skills 26-30)

ID: T19.G8.26
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Implement shader-like color effects algorithmically
Description: Students create visual effects inspired by shader programming: gradient mapping (replacing colors based on brightness), color blending modes (multiply, screen, overlay, additive), chromatic aberration (RGB channel separation), bloom effects (glow around bright areas), and vignette (darkened edges). They apply these effects to their generative art through color calculations on existing drawn elements, understanding how professional graphics effects work algorithmically.

Dependencies:
* T19.G8.06: Apply noise to modulate art parameters
* T19.G7.25: Apply color theory principles in algorithmic palettes







ID: T19.G8.27
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Create constrained generative artwork
Description: Students combine randomness with sophisticated constraints implemented through conditionals, boundary checks, and rule systems. They enforce limited color palettes (only use colors from approved list), symmetry rules (mirror operations, rotational symmetry), compositional constraints (rule of thirds, golden ratio), style consistency (geometric only, or organic only), and bounding boxes. The output is unique due to randomness yet cohesive and professional due to constraints.

Dependencies:
* T19.G8.03: Design accessible data visualizations
* T19.G7.26: Study parameter impact on aesthetic qualities







ID: T19.G8.28
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Implement recursive visual patterns with custom blocks
Description: Students create custom blocks that call themselves with modified parameters to generate recursive visual patterns. They implement depth limits to prevent infinite recursion, use size/angle/position parameters that change with each recursion level, and apply color variations by depth. They create fractal trees, recursive spirals, Sierpinski triangles, Koch snowflakes, and dragon curves using true recursion. This is algorithmic art at its most elegant—patterns that define themselves.

Dependencies:
* T19.G7.05: Draw L-system fractal trees
* T11.G7.02: Understand recursive thinking through examples







ID: T19.G8.29
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Implement real-time style transfer concepts algorithmically
Description: Students create algorithmic systems that transform visual input (camera feed, images, or generated content) using style parameters. They implement simplified versions of style transfer: extracting color palettes from reference images, applying edge detection and line-art conversion, mapping brightness to pattern density (halftone effects), or quantizing colors to specific palettes. They understand how AI style transfer works conceptually and create manual algorithmic approximations.

Dependencies:
* T19.G8.26: Implement shader-like color effects algorithmically
* T19.G8.18: Create AI-human collaborative art systems







ID: T19.G8.30
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Create emergent narrative systems in generative art
Description: Students design generative art systems that tell or suggest stories through visual evolution. They implement state machines that transition between visual themes (dawn→day→dusk→night), create agent-based systems where interactions create narrative moments (predator-prey dynamics, cooperation-competition), or build systems that respond to accumulated history (patterns remember and react to past states). They explore how algorithmic systems can create narrative experiences.

Dependencies:
* T19.G8.27: Create constrained generative artwork
* T19.G7.10: Implement flocking behavior for artistic patterns







### CAPSTONE & PORTFOLIO (Skills 31-35)

ID: T19.G8.31
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Plan a multi-technique generative art capstone project
Description: Students design and outline a comprehensive generative art project that integrates at least four advanced techniques (e.g., 3D geometry with procedural materials, dynamic lighting, particle systems, noise-based motion, interactive controls, AI integration). They create a planning document specifying which techniques to combine, how they will interact, aesthetic goals, technical requirements, and success criteria. They consider performance, accessibility, and user experience.

Dependencies:
* T19.G8.09: Apply procedural textures to 3D materials
* T19.G8.10: Implement dynamic lighting systems
* T19.G8.11: Create immersive 360° or VR-ready 3D art environments
* T19.G8.27: Create constrained generative artwork







ID: T19.G8.32
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Implement a multi-technique generative art capstone
Description: Students build their planned comprehensive generative art piece by coding the integration of multiple advanced techniques. They combine 3D geometry, procedural materials, dynamic lighting, particle systems, noise functions, interactive controls, and potentially AI generation into a single cohesive project. They apply separation of concerns, optimize for performance, and test thoroughly. They create a polished, professional-quality generative artwork.

Dependencies:
* T19.G8.31: Plan a multi-technique generative art capstone project







ID: T19.G8.33
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Document and present generative artwork professionally
Description: Students create comprehensive documentation for their generative art project: artist statement explaining creative intent, technical documentation describing algorithms and techniques used, user guide for interactive elements, annotated code with clear comments, video or GIF demonstrations of dynamic behaviors, and reflection on the creative-technical process. They present their work to audiences, demonstrating how code creates art and articulating their artistic and technical decisions.

Dependencies:
* T19.G8.32: Implement a multi-technique generative art capstone







ID: T19.G8.34
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Build and iterate on generative art variations
Description: Students create a parameterized generative art system and produce a series of 8+ distinct variations by systematically adjusting parameters and constraints. They document the relationship between parameters and visual outcomes, explain which combinations create successful compositions and why, and identify emergent aesthetic discoveries. They practice the iterative refinement process used by professional generative artists, developing a personal aesthetic through systematic exploration.

Dependencies:
* T19.G8.27: Create constrained generative artwork
* T19.G7.26: Study parameter impact on aesthetic qualities







ID: T19.G8.35
Topic: T19 – Algorithmic Art & Creative Coding
Skill: Curate a digital portfolio of generative artworks
Description: Students select their best generative art pieces (8-12 works), document the algorithms and techniques used in each, organize them into a coherent portfolio that shows progression and range, and write artist statements that explain creative intent and technical approach. They create portfolio presentations (web page, PDF, or video) suitable for sharing with educators, peers, or for applications. They demonstrate ability to communicate about computational art to technical and non-technical audiences, preparing for creative coding careers or further study.

Dependencies:
* T19.G8.34: Build and iterate on generative art variations
* T19.G8.33: Document and present generative artwork professionally


---

# SUMMARY

## Grade 7: 28 Skills
- Performance & Optimization: 3 skills
- Advanced Generative Techniques: 8 skills (L-systems, cellular automata, agents, flocking)
- Particle Systems: 3 skills
- 3D Art & Lighting: 5 skills
- Interactive & Multimodal Art: 5 skills
- Design & Aesthetics: 4 skills

## Grade 8: 35 Skills
- Advanced Data Visualization: 3 skills
- Procedural Generation & Noise: 5 skills
- 3D Art & Materials: 4 skills
- Performance & System Design: 5 skills
- AI Integration & Collaboration: 4 skills
- Interactive & Multimodal: 4 skills
- Advanced Techniques: 5 skills
- Capstone & Portfolio: 5 skills

Total: 63 skills for Grades 7-8
