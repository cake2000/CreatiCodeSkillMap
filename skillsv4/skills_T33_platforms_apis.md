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
- **Description:** Students examine CreatiCode block palettes and tag blocks that contact third-party services (ChatGPT, DALL·E, Pinecone, speech recognition). They explain what data leaves their project and why.
- **Challenge format:** Concept + annotation. Learners mark screenshots of block categories and write one sentence per block describing the external service. Auto-grading checks correct identification (e.g., “OpenAI ChatGPT” block) and presence of data-flow descriptions.
- **CSTA:** MS‑SAS‑IM‑03, CAS‑ET‑06.

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

- **Short name:** Check service responses for safety
- **Description:** Students apply moderation blocks (text/image) to verify AI-generated outputs before showing them to users, ensuring they meet class policies and AI4K12 priorities.
- **Challenge format:** Coding. Auto-grading injects disallowed content to ensure moderation intercepts it and that appropriate messages display.
- **CSTA:** MS‑SAS‑SC‑03, CAS‑ET‑06.

### T33.G8.04 – Document build-vs-buy decisions for new features

- **Short name:** Should we use a service or build our own?
- **Description:** Learners evaluate criteria (time, accuracy, privacy, cost) and write recommendations on whether to rely on existing CreatiCode blocks or implement a custom algorithm for a feature.
- **Challenge format:** Decision memo referencing data (latency measurements, accuracy tests). Rubric checks discussion of tradeoffs and final recommendation.
- **CSTA:** MS‑CAS‑ET‑05, PRO‑PM‑03.

---
