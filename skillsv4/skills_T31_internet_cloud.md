# T31 – Internet & Cloud: Grade 5–8 Skill List (Draft v3)

Topic reference: `T31 Internet & Cloud` in `domains_topics_overview.md`
Domain: Systems & Security (D4) · CSTA focus: SAS‑NW (with links to SAS‑IM, PRO‑PD, DAA‑DF/DP)

Each skill below has:

- a stable **ID** (`T31.G<grade>.<nn>`),
- an IXL‑style **short name**,
- a **description** (what understanding/behavior it targets),
- a **challenge format** (typical assessment interaction).

Where relevant, a primary **CSTA code** is noted.

> **Note:** Internet, cloud, and multiplayer mechanics are introduced starting in Grade 5 to keep age expectations appropriate. Earlier grades focus on unplugged CS foundations in other topics.

---

## Grade 5 – Foundations of Internet Use and Cloud Storage

### T31.G5.01 – Trace how a device reaches an online service

_Dependency:_
  * T02.G3.01: Identify start, action, and end symbols


- **Short name:** Map the path to a server
- **Description:** Students follow a diagram showing data leaving a laptop, passing through a router/modem, traveling across the internet, and reaching a web or game server before returning. They articulate why each hop exists.
- **Challenge format:** Concept, labeling/sequencing. Learners drag labels (device, router, ISP, server) onto a diagram. Auto-grading verifies correct order.
- **CSTA:** E5‑SAS‑NW‑02.

### T31.G5.02 – Decide when apps need the internet vs work offline

_Dependency:_
  * T01.G3.01: Complete a simple script with missing blocks
  * T30.G3.01: Identify where data is stored locally on a device
  * T31.G5.01: Trace how a device reaches an online service


- **Short name:** Offline or online?
- **Description:** Students evaluate scenarios (watching a downloaded movie, editing a shared doc, joining a multiplayer match) and choose whether each requires connectivity. They justify their reasoning.
- **Challenge format:** Concept, categorization with explanation. Auto-grading checks placement plus a short rationale referencing shared storage or remote data.
- **CSTA:** E5‑SAS‑NW‑02; CAS‑ET (impacts of computing).

### T31.G5.03 – Save and reload a preference using a cloud variable

_Dependency:_
  * T09.G3.01: Create and use a numeric variable for score or count


- **Short name:** Store data in the cloud
- **Description:** Students create a cloud variable (e.g., `preferredAvatar`) and add logic to save it before the project closes, then reload it on startup.
- **Challenge format:** Coding, guided mini-project. Auto-grading runs the project twice to ensure the preference persists between sessions.
- **CSTA:** E5‑DAA‑DF‑01; PRO‑PD.

### T31.G5.04 – Configure a session ID to isolate practice data

_Dependency:_
  * T09.G3.01: Create and use a numeric variable for score or count


- **Short name:** Use class codes for cloud data
- **Description:** Students call `set session id [code]` before reading/writing cloud variables so that multiple classes or practice sessions do not share the same dataset.
- **Challenge format:** Coding, verification task. Auto-grading runs the project with two session IDs and checks that cloud values stay separate.
- **CSTA:** E5‑SAS‑NW‑02; PRO‑PD.

### T31.G5.05 – Interpret connection status indicators in CreatiCode

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T09.G3.01: Create and use a numeric variable for score or count


- **Short name:** What does this network status mean?
- **Description:** Students read CreatiCode’s multiplayer/cloud status outputs (connecting, waiting for host, disconnected) and update on-screen guidance accordingly.
- **Challenge format:** Coding + reasoning. Auto-grading injects status changes and checks that the UI responds with accurate instructions (e.g., “Waiting for host”).
- **CSTA:** E5‑PRO‑PD‑01 (robust program behavior).

---

## Grade 6 – Protocols, Shared Data, Latency, and Privacy

### T31.G6.01 – Trace the steps of an HTTP/HTTPS request

_Dependency:_
  * T01.G3.01: Complete a simple script with missing blocks
  * T01.G3.02: Match a story description to a code sequence
  * T31.G5.04: Configure a session ID to isolate practice data
  * T31.G5.05: Interpret connection status indicators in CreatiCode


- **Short name:** What happens when you press Play?
- **Description:** Students identify the sequence: client sends request, server processes, server responds, client renders, and—if HTTPS—encryption occurs before transit.
- **Challenge format:** Concept, sequencing or fill-in. Auto-grading checks correct ordering and inclusion of encryption for HTTPS.
- **CSTA:** MS‑SAS‑NW‑05.

### T31.G6.02 – Build a shared leaderboard with cloud data

_Dependency:_
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count
  * T31.G5.04: Configure a session ID to isolate practice data
  * T31.G5.05: Interpret connection status indicators in CreatiCode


- **Short name:** Everyone sees the same scores
- **Description:** Students store `{player, score}` records in cloud variables or tables, refreshing the leaderboard whenever any player updates their entry.
- **Challenge format:** Coding, data management. Auto-grading opens two instances, submits scores, and ensures both leaderboards stay consistent.
- **CSTA:** MS‑DAA‑DP‑05; PRO‑PD.

### T31.G6.03 – Analyze how latency affects AI responsiveness and fairness

_Dependency:_
  * T31.G5.01: Trace how a device reaches an online service
  * T31.G5.02: Decide when apps need the internet vs work offline
  * T31.G5.04: Configure a session ID to isolate practice data
  * T31.G5.05: Interpret connection status indicators in CreatiCode


- **Short name:** Network delays impact AI user experience
- **Description:** Students explore scenarios where network latency affects T22 chatbot conversations, T21 image generation feedback, and T23 real-time gesture recognition. They propose mitigation strategies (local caching, progressive responses, graceful degradation) and analyze fairness implications.
- **Challenge format:** Concept + AI analysis. Auto-grading checks identification of AI-specific latency impacts and appropriate mitigation strategies.
- **CSTA:** MS‑SAS‑IM‑11.
- **AI4K12:** A3 Human Agency; D2 Bias and Fairness.

### T31.G6.04 – Evaluate privacy when sharing AI-generated content and data

_Dependency:_
  * T31.G5.01: Trace how a device reaches an online service
  * T31.G5.02: Decide when apps need the internet vs work offline
  * T31.G5.04: Configure a session ID to isolate practice data
  * T31.G5.05: Interpret connection status indicators in CreatiCode


- **Short name:** Protecting AI inputs and outputs in the cloud
- **Description:** Students review datasets containing T24 XO conversation logs, T21 generated images, T23 sensor recordings, and T22 chatbot interactions. They decide when to anonymize prompts, restrict access to AI outputs, rotate session IDs, and implement consent mechanisms.
- **Challenge format:** AI privacy analysis. Auto-grading checks recommended protections specifically address AI data sensitivity and user consent.
- **CSTA:** MS‑SAS‑SC‑07; MS‑DAA‑IM‑13.
- **AI4K12:** D1 Ethical Design; E1 Societal Impacts.

### T31.G6.05 – Distinguish stage-level vs sprite-level cloud variables

_Dependency:_
  * T09.G3.01: Create and use a numeric variable for score or count
  * T31.G5.01: Trace how a device reaches an online service
  * T31.G5.04: Configure a session ID to isolate practice data
  * T31.G5.05: Interpret connection status indicators in CreatiCode


- **Short name:** Stage cloud vs sprite cloud
- **Description:** Students experiment with CreatiCode’s ability to scope cloud variables to the stage (global) or to individual sprites/clone IDs (per-player). They choose the right scope for scores vs avatar cosmetics.
- **Challenge format:** Coding, comparison task. Auto-grading ensures both scopes are implemented and used correctly.
- **CSTA:** MS‑DAA‑DP‑05; SAS‑NW.

---

## Grade 7 – Architectures, Protocols, and Societal Impact

### T31.G7.01 – Model a distributed multiplayer server

_Dependency:_
  * T02.G3.01: Identify start, action, and end symbols
  * T31.G5.01: Trace how a device reaches an online service
  * T31.G6.04: Evaluate privacy when sharing AI-generated content and data
  * T31.G6.05: Distinguish stage-level vs sprite-level cloud variables


- **Short name:** How the server relays player data
- **Description:** Students diagram how a central server receives updates from each client and broadcasts them back, noting timing and ordering constraints.
- **Challenge format:** Concept, diagramming. Auto-grading checks for required components (clients, server, arrows for request/response).
- **CSTA:** MS‑PRO‑PD‑07; MS‑SAS‑NW‑05.

### T31.G7.02 – Design a protocol for multiplayer state sync

_Dependency:_
  * T31.G5.01: Trace how a device reaches an online service
  * T31.G5.02: Decide when apps need the internet vs work offline
  * T31.G6.04: Evaluate privacy when sharing AI-generated content and data
  * T31.G6.05: Distinguish stage-level vs sprite-level cloud variables


- **Short name:** Define the message format
- **Description:** Students specify required fields (player ID, x, y, action, timestamp) and implement serialization/deserialization using lists or JSON-like strings.
- **Challenge format:** Coding + concept. Auto-grading checks the protocol structure and verifies that synced data reconstructs correctly on the receiver side.
- **CSTA:** MS‑DAA‑DF‑02; PRO‑PD.

### T31.G7.03 – Compare network topology options

_Dependency:_
  * T31.G5.01: Trace how a device reaches an online service
  * T31.G5.02: Decide when apps need the internet vs work offline
  * T31.G6.04: Evaluate privacy when sharing AI-generated content and data
  * T31.G6.05: Distinguish stage-level vs sprite-level cloud variables


- **Short name:** Star, mesh, or peer-to-peer?
- **Description:** Students analyze trade-offs among star (client/server), mesh, and peer-to-peer topologies in terms of latency, resilience, and implementation complexity.
- **Challenge format:** Concept, comparative reasoning. Auto-grading checks for mention of latency, reliability, and administrative trade-offs.
- **CSTA:** MS‑SAS‑NW‑04.

### T31.G7.04 – Compare centralized servers with peer-to-peer networks

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T09.G3.01: Create and use a numeric variable for score or count
  * T31.G6.04: Evaluate privacy when sharing AI-generated content and data
  * T31.G6.05: Distinguish stage-level vs sprite-level cloud variables


- **Short name:** When to use mp vs p2p
- **Description:** Students contrast CreatiCode’s standard multiplayer extension (server authoritative) with the `p2p` extension modes (message-only, Nengi/3D). They cite latency, trust, and scalability implications.
- **Challenge format:** Concept + exploration. Auto-grading expects a table/list of pros/cons referencing specific extension behavior.
- **CSTA:** MS‑SAS‑NW‑04; PRO‑PD.

### T31.G7.05 – Analyze societal impacts of networked systems

_Dependency:_
  * T04.G2.01: Identify the repeating unit in a longer pattern
  * T31.G5.01: Trace how a device reaches an online service
  * T31.G6.04: Evaluate privacy when sharing AI-generated content and data
  * T31.G6.05: Distinguish stage-level vs sprite-level cloud variables


- **Short name:** How the internet changes communities
- **Description:** Students research benefits (collaboration, access) and harms (privacy loss, misinformation) of widely used networked tools, grounding arguments in real examples.
- **Challenge format:** Concept, short reflection. Auto-grading uses a rubric requiring both benefits and harms.
- **CSTA:** MS‑SAS‑IM‑11; MS‑SAS‑IM‑12.

---

## Grade 8 – Protocol Depth, Security, Resilience, and Monitoring

### T31.G8.01 – Architect edge vs cloud processing pipelines for AI

_Dependency:_
  * T02.G3.01: Identify start, action, and end symbols
  * T31.G5.01: Trace how a device reaches an online service
  * T31.G5.02: Decide when apps need the internet vs work offline
  * T31.G7.04: Compare centralized servers with peer-to-peer networks
  * T31.G7.05: Analyze societal impacts of networked systems


- **Short name:** Design AI distribution for performance and privacy
- **Description:** Students design diagrams showing which AI computations happen on-device (T23 camera preprocessing for privacy, real-time gesture recognition) and which require cloud resources (T21 DALL-E generation, T22 ChatGPT reasoning). They cite latency, privacy, and cost reasons while connecting to T21-T24 dependencies.
- **Challenge format:** Architecture diagram + explanation referencing T21-T24. Auto-grading checks for both edge and cloud components with AI-specific rationale.
- **CSTA:** MS‑SAS‑CS‑02, CAS‑ET‑07.
- **AI4K12:** D1 Ethical Design; A3 Human Agency.

### T31.G8.02 – Understand AI service network requirements

_Dependency:_
  * T31.G5.01: Trace how a device reaches an online service
  * T31.G5.02: Decide when apps need the internet vs work offline
  * T31.G5.03: Save and reload a preference using a cloud variable
  * T31.G7.04: Compare centralized servers with peer-to-peer networks
  * T31.G7.05: Analyze societal impacts of networked systems


- **Short name:** Network needs for AI applications
- **Description:** Students analyze bandwidth, latency, and reliability requirements for T21-T24 AI features (real-time voice for T22, image upload for T21, continuous sensor data for T23) and design network architectures that support these needs.
- **Challenge format:** Requirements analysis + network design. Auto-grading checks connection between AI features and network specifications.
- **CSTA:** MS‑SAS‑NW‑05.
- **AI4K12:** A2 Capabilities & Limits.

### T31.G8.03 – Design secure AI-powered cloud systems

_Dependency:_
  * T31.G5.01: Trace how a device reaches an online service
  * T31.G5.02: Decide when apps need the internet vs work offline
  * T31.G5.03: Save and reload a preference using a cloud variable
  * T31.G7.04: Compare centralized servers with peer-to-peer networks
  * T31.G7.05: Analyze societal impacts of networked systems


- **Short name:** Protect AI services and user data
- **Description:** Students outline authentication, encryption, and server-side validation for AI-powered apps using T21-T24 features. They address prompt injection attacks on T22 chatbots, unauthorized access to T21 image generation, and privacy protection for T23 sensor data.
- **Challenge format:** Security design plan referencing T21-T24. Auto-grading uses rubric emphasizing AI-specific security measures and ethical data handling.
- **CSTA:** MS‑SAS‑SC‑08; MS‑SAS‑SC‑10.
- **AI4K12:** D1 Ethical Design.

### T31.G8.04 – Implement privacy protection for AI data

_Dependency:_
  * T31.G5.01: Trace how a device reaches an online service
  * T31.G5.02: Decide when apps need the internet vs work offline
  * T31.G5.03: Save and reload a preference using a cloud variable
  * T31.G7.04: Compare centralized servers with peer-to-peer networks
  * T31.G7.05: Analyze societal impacts of networked systems


- **Short name:** Protect AI inputs and outputs
- **Description:** Students implement privacy measures for AI data: hashing T24 XO prompt logs, encrypting T23 sensor data before cloud storage, and anonymizing T22 chatbot conversations. They use simple encryption techniques while understanding AI-specific privacy needs.
- **Challenge format:** Coding + privacy analysis. Auto-grading checks encryption implementation and analysis of AI privacy requirements.
- **CSTA:** MS‑SAS‑SC‑09.
- **AI4K12:** D1 Ethical Design; E1 Societal Impacts.

### T31.G8.05 – Evaluate AI service resilience and fallbacks

_Dependency:_
  * T31.G5.01: Trace how a device reaches an online service
  * T31.G5.02: Decide when apps need the internet vs work offline
  * T31.G5.03: Save and reload a preference using a cloud variable
  * T31.G7.04: Compare centralized servers with peer-to-peer networks
  * T31.G7.05: Analyze societal impacts of networked systems


- **Short name:** What happens if AI services fail?
- **Description:** Students analyze failure scenarios for T21-T24 AI dependencies (OpenAI API downtime, speech recognition failures) and design graceful degradation strategies (cached responses, offline modes, manual fallbacks).
- **Challenge format:** Failure analysis + resilience plan. Auto-grading checks identification of AI failure modes and appropriate fallback strategies.
- **CSTA:** MS‑SAS‑NW‑05.
- **AI4K12:** A3 Human Agency.

### T31.G8.06 – Build AI service monitoring and ethics dashboards

_Dependency:_
  * T31.G5.01: Trace how a device reaches an online service
  * T31.G5.02: Decide when apps need the internet vs work offline
  * T31.G5.03: Save and reload a preference using a cloud variable
  * T31.G7.04: Compare centralized servers with peer-to-peer networks
  * T31.G7.05: Analyze societal impacts of networked systems


- **Short name:** Monitor AI usage and ethical compliance
- **Description:** Students create monitoring dashboards that track T21-T24 AI service usage (API call counts, response times, error rates) and ethical metrics (content moderation flags, bias detection alerts, user consent tracking). They connect monitoring to T35 ethics requirements.
- **Challenge format:** Coding + ethics monitoring. Auto-grading checks technical monitoring plus ethical compliance tracking for AI systems.
- **CSTA:** MS‑PRO‑PD‑07; SAS‑NW.
- **AI4K12:** D1 Ethical Design; E1 Societal Impacts.

---

## Summary

Shifting T31 to Grades 5–8 keeps advanced concepts age-appropriate. Grade 5 builds the mental model for how connectivity works and introduces simple cloud storage. Grade 6 adds concrete protocol work, shared databases, latency, privacy, and cloud scoping. Grades 7–8 tackle architecture choices, security, resilience, encryption, and monitoring—providing the systems knowledge needed to support the multiplayer creations described in T19.
