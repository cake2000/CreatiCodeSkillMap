# T33 – Connected Services & Tool Wrappers: G6–8 Skill List (Draft v2)

Topic reference: `T33 Platforms & Services` in `domains_topics_overview.md`
Domain: Systems & Security (D4) · CSTA focus: SAS‑IM, SAS‑NW, CAS‑ET (links to PRO‑PF, DAA‑DF)

Each skill below has:

- a stable **ID** (`T33.G<grade>.<nn>`),
- an IXL-style **short name**,
- a **description** (what understanding/behavior it targets),
- a **challenge format** (the typical problem type to assess it).

Where relevant, a primary **CSTA code** is noted.

**Role and scope in v3:** CreatiCode doesn’t expose raw APIs; instead, students use **blocks and tools that wrap external services** (ChatGPT, DALL·E, Pinecone, speech recognition). T33 now begins in **Grade 6**, when learners already manage data (T25–T27), understand AI blocks (T21–T24), and can reason about third-party dependencies. The topic focuses on: recognizing when a block relies on an external service, handling latency/limits, securing credentials, respecting terms of use, and evaluating when to build vs reuse. Skills progress from conceptual diagrams to implementing robust integration patterns for AI-powered apps, aligning with AI4K12’s emphasis on human oversight and societal impact.

---

## Grade 6

### T33.G6.01 – Identify blocks that call external services

- **Short name:** Which blocks talk to other servers?
- **Description:** Students examine CreatiCode AI block palettes (T21-T24) and identify which blocks contact external services (ChatGPT for T22, DALL·E for T21, speech services for T23, Pinecone for T24). They explain data flows and analyze ethical implications: what personal data leaves projects, potential bias in responses, and user privacy concerns.
- **Challenge format:** AI service mapping + ethics analysis. Auto-grading checks correct T21-T24 service identification and ethical reasoning about data flows and societal impacts.
- **CSTA:** MS‑SAS‑IM‑03, CAS‑ET‑06.
- **AI4K12:** D1 Ethical Design; E1 Societal Impacts.

### T33.G6.02 – Draw data flow diagrams for AI wrapper blocks

- **Short name:** Map prompt → service → response
- **Description:** Learners create simple diagrams showing how a block collects user input, sends it to an external service, and returns the response. They include labels for privacy-sensitive data and highlight where logging happens (T24 dependency).
- **Challenge format:** Diagram + reflection. Auto-grading checks diagrams contain input, CreatiCode client, third-party service, and return path with appropriate arrows.
- **CSTA:** MS‑SAS‑NW‑02, CAS‑ET‑06.

### T33.G6.03 – Handle latency and error states in service calls

- **Short name:** What if the service is slow or down?
- **Description:** Students design UI patterns (loading spinners, “try again” buttons) that respond gracefully when ChatGPT blocks take too long or fail. They learn to detect error tokens in the result variable.
- **Challenge format:** Coding + UI. Auto-grading simulates slow/failed responses and checks whether the app shows status updates and allows retry.
- **CSTA:** MS‑PRO‑PF‑02, SAS‑IM.

### T33.G6.04 – Respect usage limits and credits

- **Short name:** Track how many calls you’ve made
- **Description:** Learners implement counters and cool-down timers so projects don’t spam AI blocks, reflecting resource limits and fair use.
- **Challenge format:** Coding. Auto-grading triggers repeated calls to ensure counters decrement and throttling logic blocks extra requests.
- **CSTA:** MS‑SAS‑IM‑03.

---

## Grade 7

### T33.G7.01 – Securely store and reference service credentials (conceptual)

- **Short name:** Where do API keys live in CreatiCode?
- **Description:** Students learn that CreatiCode’s AI blocks encapsulate credentials and why they should never attempt to expose or share keys. They document rules for safeguarding teacher-provided tokens (if any) and explain legal/ethical consequences.
- **Challenge format:** Concept policy. Auto-grading checks mention of “keys stay server-side” and guidelines about not hardcoding secrets.
- **CSTA:** MS‑SAS‑SC‑03, CAS‑ET.

### T33.G7.02 – Build wrappers that combine multiple services

- **Short name:** Chain speech → ChatGPT → TTS
- **Description:** Learners orchestrate a multi-service workflow using speech recognition, ChatGPT, and AI speaker blocks. They handle intermediate data, ensure privacy (e.g., redacting user names), and log interactions responsibly (T24 dependency).
- **Challenge format:** Coding + documentation. Auto-grading runs sample conversations to verify the chain works and that logs include required metadata.
- **CSTA:** MS‑PRO‑PF‑02, SAS‑IM.

### T33.G7.03 – Compare service options and pick the right tool

- **Short name:** Which AI block fits this scenario?
- **Description:** Students analyze requirements (needs image generation vs text vs semantic search) and select the appropriate CreatiCode block, justifying the choice and tradeoffs (latency, cost, capabilities).
- **Challenge format:** Decision matrix. Auto-grading ensures each scenario references capabilities/limits of the chosen block.
- **CSTA:** MS‑CAS‑ET‑05.

### T33.G7.04 – Implement caching/memoization for repeated requests

- **Short name:** Don’t re-call the service when you already have the answer
- **Description:** Learners store previous prompt/response pairs in a table and reuse them to reduce external calls, improving performance and respecting limits.
- **Challenge format:** Coding. Auto-grading replays identical prompts to confirm cached responses are served instantly and new prompts hit the service.
- **CSTA:** MS‑PRO‑PF‑02, SAS‑IM.

---

## Grade 8

### T33.G8.01 – Analyze legal and ethical obligations when integrating services

- **Short name:** What do terms of use require?
- **Description:** Students read summarized terms for services (OpenAI, speech APIs) and document obligations (attribution, safety filters, prohibited content). They tie requirements to their project design.
- **Challenge format:** Policy brief referencing actual ToS excerpts. Rubric ensures they cite obligations and describe compliance steps.
- **CSTA:** MS‑CAS‑ET‑06, CAS‑HC‑02.

### T33.G8.02 – Simulate service outages and design fallbacks

- **Short name:** What happens if the AI service is unavailable?
- **Description:** Learners create an outage simulator (forcing error responses) and design fallback experiences (offline mode, manual input). They document recovery procedures.
- **Challenge format:** Coding + incident plan. Auto-grading triggers outages to confirm fallbacks engage and that logs capture the incident.
- **CSTA:** MS‑SAS‑NW‑02, PRO‑TR‑12.

### T33.G8.03 – Integrate third-party tool output into moderation workflows

- **Short name:** Multi-layered AI safety and fairness checking
- **Description:** Students create comprehensive moderation workflows for T21-T24 AI outputs: content safety filters for T21 images and T22 text, bias detection for all AI responses, consent verification for T23 sensor data, and academic integrity checks for T24 XO assistance. They implement escalation procedures connecting to T35 ethics frameworks.
- **Challenge format:** Multi-stage moderation implementation. Auto-grading tests various problematic inputs to ensure all safety, bias, and ethical concerns are detected and handled appropriately.
- **CSTA:** MS‑SAS‑SC‑03, CAS‑ET‑06.
- **AI4K12:** D1 Ethical Design; D2 Bias and Fairness; E1 Societal Impacts.

### T33.G8.04 – Document build-vs-buy decisions for new features

- **Short name:** Should we use a service or build our own?
- **Description:** Learners evaluate criteria (time, accuracy, privacy, cost) and write recommendations on whether to rely on existing CreatiCode blocks or implement a custom algorithm for a feature.
- **Challenge format:** Decision memo referencing data (latency measurements, accuracy tests). Rubric checks discussion of tradeoffs and final recommendation.
- **CSTA:** MS‑CAS‑ET‑05, PRO‑PM‑03.

---
