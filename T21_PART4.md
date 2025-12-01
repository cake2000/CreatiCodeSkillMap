# T21 - Chatbots & Prompting - PART 4 (Grades 7-8)

## GRADE 7 SKILLS




ID: T21.G7.01
Topic: T21 – Chatbots & Prompting
Skill: Implement chain-of-thought prompting for complex reasoning tasks
Description: Students build prompts that explicitly request step-by-step reasoning for complex problems. They add instructions like "Let's solve this step by step," "First analyze..., then consider..., finally conclude..." to guide the AI through multi-stage reasoning. They test on challenging tasks (word problems, logic puzzles, multi-step analysis) and compare chain-of-thought responses to direct answers, documenting accuracy improvements. They create a "reasoning template" that structures prompts into: (1) problem statement, (2) reasoning instructions, (3) format for showing work, (4) final answer format.

Dependencies:
* T21.G6.08: Use chain-of-thought prompting for complex questions




ID: T21.G7.02
Topic: T21 – Chatbots & Prompting
Skill: Create self-consistency prompting with multiple reasoning paths
Description: Students implement self-consistency by requesting the AI generate multiple independent reasoning paths for the same problem, then identify the most common answer. They build a system that runs the same complex question 3-5 times with chain-of-thought prompting, collects all answers, and uses voting or pattern detection to find consensus. They test on problems with definitive answers (math, logic) to verify that self-consistency improves accuracy. They document cases where answers diverge and analyze why.

Dependencies:
* T21.G7.01: Implement chain-of-thought prompting for complex reasoning tasks




ID: T21.G7.03
Topic: T21 – Chatbots & Prompting
Skill: Implement tree-of-thought prompting with branching exploration
Description: Students design prompts that explore multiple solution strategies simultaneously, creating a "tree" of possibilities. They prompt the AI to: (1) generate 2-3 different approaches to a problem, (2) evaluate pros/cons of each approach, (3) select the most promising path, (4) solve using that approach. They build a visual display showing the branching exploration process. They compare tree-of-thought to linear chain-of-thought on complex planning tasks (game strategy, project planning, creative problem-solving).

Dependencies:
* T21.G7.02: Create self-consistency prompting with multiple reasoning paths




ID: T21.G7.04
Topic: T21 – Chatbots & Prompting
Skill: Parse and validate structured outputs against schemas
Description: Students create prompts that request specific structured formats (JSON, CSV, key-value pairs) and build code to validate the response matches the expected schema. They define schema requirements (required fields, data types, value constraints), parse the AI response, and check each requirement. They implement error handling for malformed outputs with retry logic. Example: request "Generate 3 product records with fields: name (text), price (number 0-1000), category (one of: Electronics, Clothing, Food)" and validate each field.

Dependencies:
* T21.G5.08: Build a complete voice-to-voice chatbot
* T21.G6.04: Display streaming responses in real-time




ID: T21.G7.05
Topic: T21 – Chatbots & Prompting
Skill: Implement prompt compression to reduce token usage
Description: Students learn techniques to compress prompts while maintaining effectiveness: abbreviations, removing redundancy, using symbols over words, condensing examples. They take verbose prompts and systematically reduce token count by 30-50% while testing that outputs remain equivalent. They measure token usage before/after using a token counter, document compression strategies, and create a "compression checklist." They balance token savings against clarity loss.

Dependencies:
* T21.G5.05: Create a prompt template with fill-in-the-blank variables
* T21.G6.09: Request specific output formats in prompts




ID: T21.G7.06
Topic: T21 – Chatbots & Prompting
Skill: Create role-based prompts for domain expertise simulation
Description: Students design prompts that assign the AI a specific expert role with appropriate knowledge, tone, and constraints. They create role definitions for different domains: "You are a patient science teacher explaining to 7th graders," "You are a professional editor reviewing academic writing," "You are a friendly coding tutor helping beginners debug." They test how role framing affects response style, vocabulary, explanation depth, and accuracy. They build a role library with 5+ distinct personas and document when each is most effective.

Dependencies:
* T21.G6.04: Display streaming responses in real-time




ID: T21.G7.07
Topic: T21 – Chatbots & Prompting
Skill: Implement instruction hierarchy in prompts (system, user, context)
Description: Students structure prompts into distinct layers with clear precedence: SYSTEM instructions (unchanging behavioral rules), USER CONTEXT (session information), TASK (current request). They learn that system-level instructions take priority and user inputs cannot override them. They build a chatbot with layered prompts: system="Always respond in simple language. Never discuss politics," context="User is 12 years old learning about history," task=user's question. They test boundary cases where user tries to override system rules.

Dependencies:
* T21.G7.06: Create role-based prompts for domain expertise simulation




ID: T21.G7.08
Topic: T21 – Chatbots & Prompting
Skill: Build conversational agents with personality consistency across sessions
Description: Students create chatbots with persistent personality traits that remain consistent across multiple conversations and sessions. They define personality dimensions (formality, humor, enthusiasm, verbosity) and encode them in system prompts. They implement session memory that recalls personality-relevant facts ("You mentioned you like science fiction in our last chat"). They test personality consistency by running multiple conversations and checking that tone, vocabulary, and behavioral patterns remain stable. They document what breaks consistency.

Dependencies:
* T21.G6.09: Request specific output formats in prompts
* T21.G7.06: Create role-based prompts for domain expertise simulation




ID: T21.G7.09
Topic: T21 – Chatbots & Prompting
Skill: Implement semantic similarity search for context retrieval
Description: Students build a system that finds relevant past conversations or knowledge based on meaning rather than exact keyword matches. They maintain a list of previous Q&A pairs, compute which are semantically similar to the current question (using AI to judge relevance), and include the most relevant past exchanges in the prompt context. They compare keyword search vs semantic search for retrieving helpful context. Example: "What causes rain?" should retrieve past conversation about "water cycle" even without the word "rain."

Dependencies:
* T21.G6.09: Request specific output formats in prompts




ID: T21.G7.10
Topic: T21 – Chatbots & Prompting
Skill: Create prompts that handle ambiguity through clarification questions
Description: Students design prompts that detect ambiguous or underspecified user requests and respond with clarifying questions before attempting a full answer. They build logic to identify ambiguity signals (vague pronouns, missing details, multiple interpretations) and generate targeted questions. Example: User asks "How do I fix it?" → Bot responds "What are you trying to fix? Can you describe the problem?" They implement multi-turn clarification dialogs and test on intentionally vague requests.

Dependencies:
* T21.G7.07: Implement instruction hierarchy in prompts (system, user, context)




ID: T21.G7.11
Topic: T21 – Chatbots & Prompting
Skill: Implement function calling for external tool integration
Description: Students learn to describe available tools/functions in prompts so the AI can decide when and how to call them. They define function signatures (name, description, parameters, return type) and include them in the system prompt. When the AI generates a function call request in structured format, they parse it, execute the actual function, and feed results back to the AI. Example tools: calculator, web search, database lookup, unit converter. They build a tool registry and dispatcher system.

Dependencies:
* T21.G7.04: Parse and validate structured outputs against schemas




ID: T21.G7.11.01
Topic: T21 – Chatbots & Prompting
Skill: Design function calling prompts with clear tool descriptions
Description: Students focus on writing effective tool descriptions that help the AI understand when and how to use each function. They learn to specify: tool purpose, when it should be used, parameter requirements, example inputs/outputs, and error conditions. They create descriptions for 5+ diverse tools (math, data lookup, formatting, external APIs) and test whether the AI correctly chooses appropriate tools for various user requests. They iterate on descriptions that cause confusion or misuse.

Dependencies:
* T21.G7.11: Implement function calling for external tool integration




ID: T21.G7.12
Topic: T21 – Chatbots & Prompting
Skill: Build tool-use orchestration with sequential tool calls
Description: Students implement systems where the AI chains multiple tool calls to accomplish complex tasks. They prompt the AI to create multi-step plans (call tool A, use result in tool B, combine with tool C) and execute them sequentially. They handle data passing between tools, track execution state, and display progress. Example: "What's the weather in Tokyo in Fahrenheit?" requires: (1) get weather in Celsius, (2) convert to Fahrenheit, (3) format response. They build error recovery when any step fails.

Dependencies:
* T21.G7.11: Implement function calling for external tool integration




ID: T21.G7.13
Topic: T21 – Chatbots & Prompting
Skill: Implement error handling and retry logic for tool calls
Description: Students build robust error handling for tool call failures: network errors, invalid parameters, tool unavailability, timeout. They implement retry strategies (exponential backoff, retry with modified parameters), fallback alternatives (use different tool, skip step, ask user for help), and user-friendly error messages. They test failure scenarios systematically and document recovery paths. They add logging to track error patterns and success rates for each tool.

Dependencies:
* T21.G7.12: Build tool-use orchestration with sequential tool calls




ID: T21.G7.14
Topic: T21 – Chatbots & Prompting
Skill: Create evaluation metrics for prompt quality assessment
Description: Students develop quantitative and qualitative metrics to measure prompt effectiveness: accuracy (% correct answers on test set), relevance (response addresses the question), completeness (includes all requested information), format compliance (follows structure instructions), tone appropriateness. They build a test suite with 20+ diverse prompts and expected outputs, run evaluations automatically, and generate quality scores. They use metrics to compare prompt variations objectively.

Dependencies:
* T21.G6.12: Handle speech recognition errors gracefully




ID: T21.G7.15
Topic: T21 – Chatbots & Prompting
Skill: Analyze prompts for potential bias in outputs
Description: Students systematically test prompts for biased outputs across demographic dimensions (gender, race, age, culture), topic areas (politics, religion, social issues), and language patterns. They create test cases with role reversal (swapping gendered names, changing cultural context) and check for different responses. They identify bias sources: training data, prompt framing, default assumptions. They document bias patterns and severity. Example: testing if "Tell me about a successful scientist" shows gender bias in pronoun use or example selection.

Dependencies:
* T21.G7.14: Create evaluation metrics for prompt quality assessment




ID: T21.G7.16
Topic: T21 – Chatbots & Prompting
Skill: Implement bias mitigation strategies in prompt design
Description: Students apply strategies to reduce bias in chatbot outputs: neutral language in prompts, explicit diversity instructions ("Include examples from multiple cultures/genders"), bias-checking constraints ("Avoid stereotypes about..."), balanced framing. They implement bias detection in responses (flagging stereotypical language) and automatic reprompting with bias mitigation instructions when detected. They test effectiveness using their bias evaluation suite from G7.15.

Dependencies:
* T21.G7.15: Analyze prompts for potential bias in outputs




ID: T21.G7.17
Topic: T21 – Chatbots & Prompting
Skill: Implement rate limiting and error handling for production use
Description: Students build production-ready error handling: rate limiting (maximum requests per user/timeframe), quota management, API error handling (service unavailable, authentication failures), timeout handling, graceful degradation. They implement user-facing status messages, request queuing for high load, and fallback responses when the service is down. They test edge cases: rapid-fire requests, network failures mid-stream, quota exhaustion.

Dependencies:
* T21.G7.13: Implement error handling and retry logic for tool calls




ID: T21.G7.18
Topic: T21 – Chatbots & Prompting
Skill: Monitor and log chatbot usage for cost and performance analysis
Description: Students implement comprehensive logging: request/response tracking, token usage per request, response latency, error rates, user satisfaction ratings. They build analytics dashboards showing: cost trends, most expensive prompts, slowest requests, error patterns, usage by feature. They identify optimization opportunities (compress high-token prompts, cache common requests) and estimate cost for different usage levels. They implement cost alerts when spending exceeds thresholds.

Dependencies:
* T21.G7.17: Implement rate limiting and error handling for production use




ID: T21.G7.19
Topic: T21 – Chatbots & Prompting
Skill: Design prompts preventing common security vulnerabilities
Description: Students learn prompt injection vulnerabilities and defenses. They test attacks: users trying to override system instructions ("Ignore previous instructions and..."), extract sensitive data, generate harmful content, bypass filters. They implement defenses: input sanitization, instruction hierarchy enforcement (system > user), output filtering, harmful content detection. They build a security test suite with 10+ attack vectors and verify their chatbot resists each. They document the security model and limitations.

Dependencies:
* T21.G7.07: Implement instruction hierarchy in prompts (system, user, context)


----

## GRADE 8 SKILLS




ID: T21.G8.01
Topic: T21 – Chatbots & Prompting
Skill: Implement meta-prompting where AI generates its own prompts
Description: Students build systems where AI analyzes a high-level goal and generates optimized prompts to achieve it. They create a two-stage process: (1) meta-prompt asks AI to design an effective prompt for a specific task, (2) use the AI-generated prompt for the actual task. They compare human-written vs AI-generated prompts for effectiveness. They build a prompt improvement loop: AI generates prompt → test it → AI analyzes failures → AI generates improved version. They explore when meta-prompting helps vs adds unnecessary complexity.

Dependencies:
* T21.G7.01: Implement chain-of-thought prompting for complex reasoning tasks




ID: T21.G8.02
Topic: T21 – Chatbots & Prompting
Skill: Design automatic prompt optimization through feedback loops
Description: Students implement systems that automatically improve prompts based on performance feedback. They track success metrics (accuracy, user ratings, task completion), identify underperforming prompts, and systematically test variations. They implement A/B testing with automatic variant generation, measure comparative performance, and promote winning variants. They build optimization history tracking and rollback capability. They set up continuous improvement cycles: monitor → identify issues → generate alternatives → test → deploy.

Dependencies:
* T21.G8.01: Implement meta-prompting where AI generates its own prompts
* T21.G7.14: Create evaluation metrics for prompt quality assessment




ID: T21.G8.03
Topic: T21 – Chatbots & Prompting
Skill: Implement constitutional AI prompting with principle-based constraints
Description: Students design chatbots governed by explicit principles codified in prompts. They define a "constitution" of behavioral rules (helpfulness, harmlessness, honesty) and encode them as constraints the AI must follow. They implement principle prioritization for conflict resolution (when principles conflict, which takes precedence). They test edge cases where principles clash (being honest vs being kind) and verify the AI resolves them according to priority rules. They document the constitutional framework and its limitations.

Dependencies:
* T21.G7.16: Implement bias mitigation strategies in prompt design




ID: T21.G8.04
Topic: T21 – Chatbots & Prompting
Skill: Create retrieval-augmented generation (RAG) systems with vector databases
Description: Students build RAG systems that retrieve relevant information from a knowledge base before generating responses. They create a document collection, split it into chunks, generate embeddings (vector representations) for each chunk, and store in a vector database. When users ask questions, they: (1) convert question to vector, (2) find most similar document chunks, (3) include them in the prompt context, (4) generate answer grounded in retrieved information. They compare RAG responses to pure generation for accuracy and hallucination reduction.

Dependencies:
* T21.G7.09: Implement semantic similarity search for context retrieval




ID: T21.G8.05
Topic: T21 – Chatbots & Prompting
Skill: Implement hybrid search combining keyword and semantic retrieval
Description: Students enhance RAG systems by combining traditional keyword search (BM25, TF-IDF) with semantic vector search. They implement parallel retrieval: run both keyword and semantic search, combine results using weighted ranking or reciprocal rank fusion. They test on diverse queries showing when each method excels (keyword for exact terms/names, semantic for concepts/paraphrases). They build a hybrid system that adaptively weights methods based on query characteristics.

Dependencies:
* T21.G8.04: Create retrieval-augmented generation (RAG) systems with vector databases




ID: T21.G8.06
Topic: T21 – Chatbots & Prompting
Skill: Design prompt caching strategies to reduce latency and cost
Description: Students implement intelligent caching to avoid redundant API calls: cache identical prompts, recognize semantically similar prompts, cache partial prompts (system instructions) separately from dynamic content. They implement cache invalidation policies (time-based, usage-based), measure cache hit rates, and calculate cost savings. They handle cache staleness (when cached responses become outdated) and implement smart refresh strategies. They balance cache memory usage against API cost savings.

Dependencies:
* T21.G7.05: Implement prompt compression to reduce token usage
* T21.G7.18: Monitor and log chatbot usage for cost and performance analysis




ID: T21.G8.07
Topic: T21 – Chatbots & Prompting
Skill: Build streaming response handlers for real-time chat experiences
Description: Students implement production-quality streaming: display tokens as they arrive with smooth animation, handle partial sentences gracefully, update UI progressively without flicker, implement cancel-during-stream functionality. They handle streaming errors (connection drops mid-stream, partial responses), implement resume/retry logic, and provide seamless UX. They optimize rendering performance for long responses, add features like "copy partial response" and "pause stream." They compare streaming latency and UX across different network conditions.

Dependencies:
* T21.G7.17: Implement rate limiting and error handling for production use




ID: T21.G8.08
Topic: T21 – Chatbots & Prompting
Skill: Implement context window management for long conversations
Description: Students build systems to handle conversations exceeding the model's context window (token limit). They implement strategies: conversation summarization (periodically compress old messages), selective message retention (keep important messages, drop filler), sliding window (keep recent N messages), hierarchical summary (summaries of summaries). They track context usage in real-time, warn users approaching limits, and automatically apply compression when needed. They test that conversation coherence is maintained after compression.

Dependencies:
* T21.G6.09: Request specific output formats in prompts
* T21.G8.06: Design prompt caching strategies to reduce latency and cost




ID: T21.G8.09
Topic: T21 – Chatbots & Prompting
Skill: Create prompt ensembles combining multiple model outputs
Description: Students build ensemble systems that combine outputs from multiple AI calls for improved quality. They implement strategies: majority voting (for classification), averaging (for numeric outputs), best-of-N selection (generate N responses, use quality heuristic to pick best), mixture-of-experts (route different question types to specialized prompts). They measure ensemble accuracy vs single-model baseline, document quality-cost tradeoffs, and identify which strategies work best for different tasks.

Dependencies:
* T21.G6.07: Use multiple chatbot sessions for different characters
* T21.G7.02: Create self-consistency prompting with multiple reasoning paths




ID: T21.G8.10
Topic: T21 – Chatbots & Prompting
Skill: Implement output verification with fact-checking mechanisms
Description: Students build automated fact-checking for chatbot responses. They implement verification strategies: cross-reference with trusted sources (RAG with curated documents), consistency checking (ask same fact multiple ways, check agreement), confidence scoring (parse "I think" vs "definitely"), explicit source citation requirements. They flag low-confidence or unverifiable claims for review. They test on factual domains (history, science) and measure false-positive and false-negative rates.

Dependencies:
* T21.G8.04: Create retrieval-augmented generation (RAG) systems with vector databases
* T21.G8.05: Implement hybrid search combining keyword and semantic retrieval




ID: T21.G8.11
Topic: T21 – Chatbots & Prompting
Skill: Design systematic prompt debugging workflows
Description: Students create structured debugging processes for prompt failures: isolate the problem (which part of prompt causes issue), create minimal reproducing example, test hypotheses systematically (change one variable at a time), document findings, apply fixes, verify resolution. They build debugging tools: prompt diff viewer (compare working vs broken versions), variable isolation testing (test each prompt component separately), regression test suite (verify fixes don't break other cases). They practice on 5+ realistic debugging scenarios.

Dependencies:
* T21.G6.10: Build a prompt library using lists
* T21.G7.15: Analyze prompts for potential bias in outputs




ID: T21.G8.12
Topic: T21 – Chatbots & Prompting
Skill: Implement hallucination detection and mitigation strategies
Description: Students build systems to detect and reduce AI hallucinations (confident false statements). They implement detection methods: fact verification against knowledge base, consistency checking across multiple responses, confidence calibration (ask AI to rate certainty), source attribution (require citations). They apply mitigation: constrain responses to retrieved documents only, add "I don't know" instructions, temperature tuning for factual tasks. They measure hallucination rates before/after interventions on a test set with known facts.

Dependencies:
* T21.G8.10: Implement output verification with fact-checking mechanisms




ID: T21.G8.13
Topic: T21 – Chatbots & Prompting
Skill: Create adversarial test suites for robustness evaluation
Description: Students build comprehensive test suites to probe chatbot weaknesses: edge cases (very long/short inputs, special characters, multiple languages), adversarial inputs (prompt injections, jailbreak attempts, manipulation), domain boundaries (questions outside training data), ambiguous/contradictory requests. They automate testing, track failure modes, measure robustness scores, and prioritize fixes. They document attack vectors and defensive measures.

Dependencies:
* T21.G7.19: Design prompts preventing common security vulnerabilities
* T21.G8.11: Design systematic prompt debugging workflows




ID: T21.G8.14
Topic: T21 – Chatbots & Prompting
Skill: Implement multi-agent systems with specialized agent roles
Description: Students design systems where multiple AI agents collaborate, each with specialized roles. They create agent architectures: researcher (gathers information), analyzer (evaluates options), writer (creates content), critic (reviews quality). Each agent has distinct prompts, capabilities, and expertise. They build agent coordination: agents communicate by passing structured messages, maintain shared context, and work toward common goals. They test on complex tasks requiring diverse skills (research report, product analysis, creative projects).

Dependencies:
* T21.G7.12: Build tool-use orchestration with sequential tool calls




ID: T21.G8.14.01
Topic: T21 – Chatbots & Prompting
Skill: Design agent communication protocols and message passing
Description: Students create structured communication systems for multi-agent collaboration. They define message schemas (sender, recipient, message type, payload, metadata), implement message routing (direct, broadcast, subscription-based), and build message queues. They design protocols for common patterns: request-response, event notification, collaborative editing. They implement message logging for debugging and tracing agent interactions. They test communication reliability and handle message delivery failures.

Dependencies:
* T21.G8.14: Implement multi-agent systems with specialized agent roles




ID: T21.G8.15
Topic: T21 – Chatbots & Prompting
Skill: Create agent orchestration with task decomposition and delegation
Description: Students build orchestration systems where a "manager" agent decomposes complex tasks and delegates to specialist agents. The manager: analyzes task requirements, breaks into subtasks, assigns to appropriate agents, monitors progress, integrates results. They implement task dependencies (subtask B needs subtask A's output), parallel execution (independent subtasks run simultaneously), error handling (reassign failed tasks). They test on multi-step projects and measure efficiency gains from parallelization.

Dependencies:
* T21.G8.14: Implement multi-agent systems with specialized agent roles




ID: T21.G8.16
Topic: T21 – Chatbots & Prompting
Skill: Implement ReAct pattern (Reasoning and Acting) for agentic AI
Description: Students build ReAct agents that interleave reasoning (thinking about what to do) and acting (using tools). They implement the ReAct loop: (1) agent observes current state, (2) reasons about next action using chain-of-thought, (3) selects and executes tool/action, (4) observes result, (5) reasons about new state, (6) repeat until task complete. They trace ReAct execution showing thought-action-observation sequences. They test on tasks requiring multi-step tool use with adaptive planning.

Dependencies:
* T21.G7.12: Build tool-use orchestration with sequential tool calls
* T21.G8.15: Create agent orchestration with task decomposition and delegation




ID: T21.G8.17
Topic: T21 – Chatbots & Prompting
Skill: Build self-correction loops where agents review and improve outputs
Description: Students implement iterative refinement where agents critique and improve their own work. They create multi-stage pipelines: (1) agent generates initial response, (2) critic agent identifies flaws, (3) generator revises based on critique, (4) repeat until quality threshold met or max iterations reached. They implement quality scoring to decide when to stop iterating. They test on tasks where quality improves with revision (writing, code, analysis) and measure quality-vs-iteration tradeoffs.

Dependencies:
* T21.G8.16: Implement ReAct pattern (Reasoning and Acting) for agentic AI




ID: T21.G8.18
Topic: T21 – Chatbots & Prompting
Skill: Implement prompt versioning and A/B testing in production
Description: Students build production systems for managing prompt versions and testing variations. They implement: version control for prompts (track changes, rollback capability), A/B testing infrastructure (randomly assign users to variants, collect metrics), statistical significance testing, gradual rollout (expose new versions to increasing user percentages). They run real A/B tests comparing prompt variants, analyze results, and make data-driven deployment decisions. They document the testing methodology and results.

Dependencies:
* T21.G6.12: Handle speech recognition errors gracefully
* T21.G7.18: Monitor and log chatbot usage for cost and performance analysis




ID: T21.G8.19
Topic: T21 – Chatbots & Prompting
Skill: Design fallback strategies for chatbot failures
Description: Students implement comprehensive fallback mechanisms when primary systems fail. They create fallback chains: primary AI → simplified prompt → cached response → static helpful message → escalation to human. They implement failure detection (timeouts, error rates, quality checks), automatic fallback triggering, and recovery monitoring (when to retry primary system). They test all failure modes and verify graceful degradation. They balance user experience against cost/complexity of fallback layers.

Dependencies:
* T21.G7.17: Implement rate limiting and error handling for production use
* T21.G8.13: Create adversarial test suites for robustness evaluation




ID: T21.G8.20
Topic: T21 – Chatbots & Prompting
Skill: Create human-in-the-loop workflows with review and approval gates
Description: Students design systems where humans review and approve AI outputs before delivery. They implement review queues (flag responses needing human review based on confidence, content type, user role), approval workflows (submit → review → approve/reject/edit → deliver), and feedback loops (human edits train future AI behavior). They build reviewer dashboards showing pending items, approval rates, common issues. They measure impact of human review on quality and identify which outputs most benefit from review.

Dependencies:
* T21.G8.17: Build self-correction loops where agents review and improve outputs
* T21.G8.19: Design fallback strategies for chatbot failures




ID: T21.G8.21
Topic: T21 – Chatbots & Prompting
Skill: Implement comprehensive observability for production chatbot systems
Description: Students build complete observability: distributed tracing (track requests across multiple AI calls, tools, agents), structured logging (searchable, filterable logs with context), metrics dashboards (latency, error rates, token usage, cost), alerting (automated notifications for anomalies), and incident response playbooks. They instrument their chatbot to track the full request lifecycle, diagnose issues from logs, and optimize based on metrics. They simulate production issues and use observability tools to debug them.

Dependencies:
* T21.G7.18: Monitor and log chatbot usage for cost and performance analysis
* T21.G8.07: Build streaming response handlers for real-time chat experiences




ID: T21.G8.22
Topic: T21 – Chatbots & Prompting
Skill: Design ethical deployment frameworks for chatbot applications
Description: Students create comprehensive ethical frameworks for deploying AI chatbots. They address: informed consent (users know they're talking to AI), data privacy (handling user information responsibly), fairness (bias testing and mitigation), transparency (explaining AI limitations), accountability (human oversight and appeals process), safety (preventing harmful outputs). They implement ethical review checklists, conduct stakeholder impact analysis, and create incident response plans for ethical violations. They document the ethical framework and justify design choices.

Dependencies:
* T21.G8.03: Implement constitutional AI prompting with principle-based constraints
* T21.G8.13: Create adversarial test suites for robustness evaluation
* T21.G8.20: Create human-in-the-loop workflows with review and approval gates
