# T31 (Internet & Cloud) Skills Analysis Report

**Report Generated:** 2025-11-21
**Total T31 Skills Found:** 22

---

## Grade 5 Skills (5 skills)

### T31.G5.01: Trace how a device reaches an online service
- **Grade:** 5
- **Description:** Students follow a diagram showing data leaving a laptop, passing through a router/modem, traveling across the internet, and reaching a web or game server before returning. They articulate why each hop exists.
- **Dependencies:**
  - T02.G3.01: Identify start, action, and end symbols
- **CSTA Code:** None specified

### T31.G5.02: Decide when apps need the internet vs work offline
- **Grade:** 5
- **Description:** Students evaluate scenarios (watching a downloaded movie, editing a shared doc, joining a multiplayer match) and choose whether each requires connectivity. They justify their reasoning.
- **Dependencies:**
  - T01.G3.01: Complete a simple script with missing blocks
  - T30.G3.01: Connect project ideas to required sensors/actuators
  - T31.G5.01: Trace how a device reaches an online service
- **CSTA Code:** None specified

### T31.G5.03: Save and reload a preference using a cloud variable
- **Grade:** 5
- **Description:** Students create a cloud variable (e.g., `preferredAvatar`) and add logic to save it before the project closes, then reload it on startup.
- **Dependencies:**
  - T09.G3.01: Create and use a numeric variable for score or count
- **CSTA Code:** None specified

### T31.G5.04: Isolate cloud data with sessions
- **Grade:** 5
- **Description:** Students use `create cloud session` or `join cloud session` blocks before reading/writing cloud variables so that multiple classes or practice sessions do not share the same dataset.
- **Dependencies:**
  - T09.G3.01: Create and use a numeric variable for score or count
  - T31.G5.03: Save and reload a preference using a cloud variable
- **CSTA Code:** None specified

### T31.G5.05: Interpret connection status indicators in CreatiCode
- **Grade:** 5
- **Description:** Students read CreatiCode's multiplayer/cloud status outputs (connecting, waiting for host, disconnected) and update on-screen guidance accordingly.
- **Dependencies:**
  - T09.G3.01: Create and use a numeric variable for score or count
  - T31.G5.03: Save and reload a preference using a cloud variable
  - T31.G5.04: Isolate cloud data with sessions
- **CSTA Code:** None specified

---

## Grade 6 Skills (6 skills)

### T31.G6.01: Trace the steps of an HTTP/HTTPS request
- **Grade:** 6
- **Description:** Students identify the sequence: client sends request, server processes, server responds, client renders, and—if HTTPS—encryption occurs before transit.
- **Dependencies:**
  - T01.G3.01: Complete a simple script with missing blocks
  - T01.G3.02: Match a story description to a code sequence
  - T31.G5.01: Trace how a device reaches an online service
- **CSTA Code:** None specified

### T31.G6.02: Read and display cloud variable from another session
- **Grade:** 6
- **Description:** Students create a project that reads a cloud variable value set by another player or session (e.g., a shared message or high score) and displays it on screen. This scaffolds understanding of how cloud data is shared across different users.
- **Dependencies:**
  - T09.G3.01: Create and use a numeric variable for score or count
  - T31.G5.03: Save and reload a preference using a cloud variable
  - T31.G5.04: Isolate cloud data with sessions
- **CSTA Code:** None specified

### T31.G6.03: Build a shared leaderboard with cloud data
- **Grade:** 6
- **Description:** Students apply cloud variable knowledge from T31.G5.03 to store `{player, score}` records in cloud variables or tables, refreshing the leaderboard whenever any player updates their entry.
- **Dependencies:**
  - T08.G3.01: Use a simple if in a script
  - T09.G3.01: Create and use a numeric variable for score or count
  - T31.G5.03: Save and reload a preference using a cloud variable
  - T31.G6.02: Read and display cloud variable from another session
- **CSTA Code:** None specified

### T31.G6.04: Measure and analyze how latency affects AI responsiveness and fairness
- **Grade:** 6
- **Description:** Students use timer blocks to measure network latency in scenarios where it affects T22 chatbot conversations, T21 image generation feedback, and T23 real-time gesture recognition. They record and compare response times, then propose mitigation strategies (local caching, progressive responses, graceful degradation) and analyze fairness implications.
- **Dependencies:**
  - T31.G5.01: Trace how a device reaches an online service
  - T31.G5.02: Decide when apps need the internet vs work offline
- **CSTA Code:** None specified

### T31.G6.05: Evaluate privacy when sharing AI-generated content and data
- **Grade:** 6
- **Description:** Students review datasets containing T24 XO conversation logs, T21 generated images, T23 sensor recordings, and T22 chatbot interactions. They decide when to anonymize prompts, restrict access to AI outputs, rotate session IDs, and implement consent mechanisms.
- **Dependencies:**
  - T31.G5.01: Trace how a device reaches an online service
  - T31.G5.02: Decide when apps need the internet vs work offline
  - T31.G6.04: Measure and analyze how latency affects AI responsiveness and fairness
- **CSTA Code:** None specified

### T31.G6.06: Distinguish stage-level vs sprite-level cloud variables
- **Grade:** 6
- **Description:** Students experiment with CreatiCode's ability to scope cloud variables to the stage (global) or to individual sprites/clone IDs (per-player). They choose the right scope for scores vs avatar cosmetics.
- **Dependencies:**
  - T09.G3.01: Create and use a numeric variable for score or count
  - T31.G5.04: Isolate cloud data with sessions
  - T31.G5.05: Interpret connection status indicators in CreatiCode
  - T31.G6.03: Build a shared leaderboard with cloud data
- **CSTA Code:** None specified

---

## Grade 7 Skills (5 skills)

### T31.G7.01: Model a distributed multiplayer server
- **Grade:** 7
- **Description:** Students diagram how a central server receives updates from each client and broadcasts them back, noting timing and ordering constraints.
- **Dependencies:**
  - T02.G3.01: Identify start, action, and end symbols in flowcharts
  - T31.G5.01: Trace how a device reaches an online service
  - T31.G6.06: Distinguish stage-level vs sprite-level cloud variables
- **CSTA Code:** None specified

### T31.G7.02: Design a protocol for multiplayer state sync
- **Grade:** 7
- **Description:** Students specify required fields (player ID, x, y, action, timestamp) and implement serialization/deserialization using lists or JSON-like strings.
- **Dependencies:**
  - T31.G6.06: Distinguish stage-level vs sprite-level cloud variables
  - T31.G7.01: Model a distributed multiplayer server
- **CSTA Code:** None specified

### T31.G7.03: Compare network topology options
- **Grade:** 7
- **Description:** Students analyze physical and logical network topologies (star, mesh, and peer-to-peer), focusing on how nodes are arranged and connected. They evaluate trade-offs in terms of latency, resilience, and implementation complexity.
- **Dependencies:**
  - T31.G6.06: Distinguish stage-level vs sprite-level cloud variables
  - T31.G7.01: Model a distributed multiplayer server
- **CSTA Code:** None specified

### T31.G7.04: Client-server vs peer-to-peer architecture
- **Grade:** 7
- **Description:** Students understand the architectural differences between centralized client-server models (like CreatiCode's multiplayer system) and peer-to-peer approaches. They analyze trade-offs including latency, trust/authority, scalability, and ease of implementation.
- **Dependencies:**
  - T31.G6.06: Distinguish stage-level vs sprite-level cloud variables
  - T31.G7.03: Compare network topology options
- **CSTA Code:** None specified

### T31.G7.05: Analyze societal impacts of networked systems
- **Grade:** 7
- **Description:** Students research societal impacts of widely used networked tools: (1) Benefits such as enabling collaboration, expanding access to information, and connecting communities; (2) Harms such as privacy loss, spread of misinformation, and digital divide issues. They ground arguments in real examples and propose mitigation strategies.
- **Dependencies:**
  - T31.G6.05: Evaluate privacy when sharing AI-generated content and data
  - T31.G6.06: Distinguish stage-level vs sprite-level cloud variables
  - T31.G7.04: Client-server vs peer-to-peer architecture
- **CSTA Code:** None specified

---

## Grade 8 Skills (6 skills)

### T31.G8.01: Architect edge vs cloud processing pipelines for AI
- **Grade:** 8
- **Description:** Students design diagrams showing which AI computations happen on-device (T23 camera preprocessing for privacy, real-time gesture recognition) and which require cloud resources (T21 DALL-E generation, T22 ChatGPT reasoning). They cite latency, privacy, and cost reasons while connecting to T21-T24 dependencies.
- **Dependencies:**
  - T02.G6.01: Design a flowchart for a simple guessing game
  - T31.G6.01: Trace the steps of an HTTP/HTTPS request
  - T31.G7.04: Client-server vs peer-to-peer architecture
  - T31.G7.05: Analyze societal impacts of networked systems
- **CSTA Code:** None specified

### T31.G8.02: Understand AI service network requirements
- **Grade:** 8
- **Description:** Students analyze bandwidth, latency, and reliability requirements for T21-T24 AI features (real-time voice for T22, image upload for T21, continuous sensor data for T23) and design network architectures that support these needs.
- **Dependencies:**
  - T31.G7.04: Client-server vs peer-to-peer architecture
  - T31.G7.05: Analyze societal impacts of networked systems
  - T31.G8.01: Architect edge vs cloud processing pipelines for AI
- **CSTA Code:** None specified

### T31.G8.03: Design secure AI-powered cloud systems
- **Grade:** 8
- **Description:** Students outline authentication, encryption, and server-side validation for AI-powered apps using T21-T24 features. They address prompt injection attacks on T22 chatbots, unauthorized access to T21 image generation, and privacy protection for T23 sensor data.
- **Dependencies:**
  - T31.G7.04: Client-server vs peer-to-peer architecture
  - T31.G7.05: Analyze societal impacts of networked systems
  - T31.G8.02: Understand AI service network requirements
- **CSTA Code:** None specified

### T31.G8.04: Implement privacy protection for AI data
- **Grade:** 8
- **Description:** Students implement privacy measures for AI data: hashing T24 XO prompt logs, encrypting T23 sensor data before cloud storage, and anonymizing T22 chatbot conversations. They use simple encryption techniques while understanding AI-specific privacy needs.
- **Dependencies:**
  - T31.G7.05: Analyze societal impacts of networked systems
  - T31.G8.03: Design secure AI-powered cloud systems
- **CSTA Code:** None specified

### T31.G8.05: Evaluate AI service resilience and fallbacks
- **Grade:** 8
- **Description:** Students analyze failure scenarios for T21-T24 AI dependencies (OpenAI API downtime, speech recognition failures) and design graceful degradation strategies (cached responses, offline modes, manual fallbacks).
- **Dependencies:**
  - T31.G8.02: Understand AI service network requirements
  - T31.G8.03: Design secure AI-powered cloud systems
- **CSTA Code:** None specified

### T31.G8.06: Build AI service monitoring and ethics dashboards
- **Grade:** 8
- **Description:** Students create monitoring dashboards that track T21-T24 AI service usage (API call counts, response times, error rates) and ethical metrics (content moderation flags, bias detection alerts, user consent tracking). They connect monitoring to T35 ethics requirements.
- **Dependencies:**
  - T31.G8.04: Implement privacy protection for AI data
  - T31.G8.05: Evaluate AI service resilience and fallbacks
- **CSTA Code:** None specified

---

## Summary Statistics

### Skills by Grade Level:
- **Grade K:** 0 skills
- **Grade 1:** 0 skills
- **Grade 2:** 0 skills
- **Grade 3:** 0 skills
- **Grade 4:** 0 skills
- **Grade 5:** 5 skills
- **Grade 6:** 6 skills
- **Grade 7:** 5 skills
- **Grade 8:** 6 skills

### Key Observations:

1. **Grade Distribution:** T31 skills are concentrated in grades 5-8, with no skills in K-4. This aligns with the topic's advanced nature (Internet & Cloud concepts).

2. **Progression Pattern:**
   - Grade 5: Foundation concepts (tracing connections, cloud variables, sessions)
   - Grade 6: Applied cloud features (HTTP/HTTPS, shared data, privacy, AI integration)
   - Grade 7: Network architecture (multiplayer servers, protocols, topologies, societal impacts)
   - Grade 8: Advanced AI-cloud integration (edge computing, security, monitoring, ethics)

3. **AI Integration:** Heavy emphasis on AI-cloud integration in grades 6-8, with skills connecting to T21 (AI Image Generation), T22 (AI Chatbots), T23 (AI Sensors), and T24 (AI XO).

4. **CSTA Codes:** None of the T31 skills have CSTA codes specified.

5. **Dependency Patterns:**
   - Most Grade 5 skills depend on foundational skills from T09 (variables) and T02 (flowcharts)
   - Grade 6-8 skills build progressively on earlier T31 skills
   - Strong cross-topic dependencies with AI topics (T21-T24) and ethics (T35)

6. **Thematic Focus Areas:**
   - Cloud variable management (5 skills)
   - Network architecture and protocols (5 skills)
   - AI-cloud integration (7 skills)
   - Security and privacy (5 skills)

---

## Recommendations for Optimization:

1. **Consider adding lower grade skills** (K-4) for age-appropriate internet safety and basic connectivity concepts

2. **Add CSTA code mappings** for all skills to align with national standards

3. **Evaluate AI integration density** - 7 out of 22 skills (32%) are heavily AI-focused, which may be appropriate but worth reviewing

4. **Check dependency complexity** - Some Grade 8 skills have long dependency chains that might need scaffolding

5. **Privacy and security thread** - Strong focus on these themes could be highlighted as a learning progression
