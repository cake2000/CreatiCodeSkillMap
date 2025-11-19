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

- **Short name:** Map the path to a server
- **Description:** Students follow a diagram showing data leaving a laptop, passing through a router/modem, traveling across the internet, and reaching a web or game server before returning. They articulate why each hop exists.
- **Challenge format:** Concept, labeling/sequencing. Learners drag labels (device, router, ISP, server) onto a diagram. Auto-grading verifies correct order.
- **CSTA:** E5‑SAS‑NW‑02.

### T31.G5.02 – Decide when apps need the internet vs work offline

- **Short name:** Offline or online?
- **Description:** Students evaluate scenarios (watching a downloaded movie, editing a shared doc, joining a multiplayer match) and choose whether each requires connectivity. They justify their reasoning.
- **Challenge format:** Concept, categorization with explanation. Auto-grading checks placement plus a short rationale referencing shared storage or remote data.
- **CSTA:** E5‑SAS‑NW‑02; CAS‑ET (impacts of computing).

### T31.G5.03 – Save and reload a preference using a cloud variable

- **Short name:** Store data in the cloud
- **Description:** Students create a cloud variable (e.g., `preferredAvatar`) and add logic to save it before the project closes, then reload it on startup.
- **Challenge format:** Coding, guided mini-project. Auto-grading runs the project twice to ensure the preference persists between sessions.
- **CSTA:** E5‑DAA‑DF‑01; PRO‑PD.

### T31.G5.04 – Configure a session ID to isolate practice data

- **Short name:** Use class codes for cloud data
- **Description:** Students call `set session id [code]` before reading/writing cloud variables so that multiple classes or practice sessions do not share the same dataset.
- **Challenge format:** Coding, verification task. Auto-grading runs the project with two session IDs and checks that cloud values stay separate.
- **CSTA:** E5‑SAS‑NW‑02; PRO‑PD.

### T31.G5.05 – Interpret connection status indicators in CreatiCode

- **Short name:** What does this network status mean?
- **Description:** Students read CreatiCode’s multiplayer/cloud status outputs (connecting, waiting for host, disconnected) and update on-screen guidance accordingly.
- **Challenge format:** Coding + reasoning. Auto-grading injects status changes and checks that the UI responds with accurate instructions (e.g., “Waiting for host”).
- **CSTA:** E5‑PRO‑PD‑01 (robust program behavior).

---

## Grade 6 – Protocols, Shared Data, Latency, and Privacy

### T31.G6.01 – Trace the steps of an HTTP/HTTPS request

- **Short name:** What happens when you press Play?
- **Description:** Students identify the sequence: client sends request, server processes, server responds, client renders, and—if HTTPS—encryption occurs before transit.
- **Challenge format:** Concept, sequencing or fill-in. Auto-grading checks correct ordering and inclusion of encryption for HTTPS.
- **CSTA:** MS‑SAS‑NW‑05.

### T31.G6.02 – Build a shared leaderboard with cloud data

- **Short name:** Everyone sees the same scores
- **Description:** Students store `{player, score}` records in cloud variables or tables, refreshing the leaderboard whenever any player updates their entry.
- **Challenge format:** Coding, data management. Auto-grading opens two instances, submits scores, and ensures both leaderboards stay consistent.
- **CSTA:** MS‑DAA‑DP‑05; PRO‑PD.

### T31.G6.03 – Analyze how latency affects fairness

- **Short name:** Latency can change winners
- **Description:** Students explore scenarios where lag causes missed hits or delayed updates and propose mitigation strategies (server authority, buffering, slowdown).
- **Challenge format:** Concept, explanation. Auto-grading uses a rubric to check for clear identification of fairness concerns and a plausible mitigation.
- **CSTA:** MS‑SAS‑IM‑11.

### T31.G6.04 – Evaluate privacy when sharing cloud data

- **Short name:** Who should see this scoreboard?
- **Description:** Students review example datasets (names, locations, high scores) and decide when to anonymize data, restrict access, or rotate session IDs.
- **Challenge format:** Concept, scenario analysis. Auto-grading checks recommended protections against an answer key.
- **CSTA:** MS‑SAS‑SC‑07; MS‑DAA‑IM‑13.

### T31.G6.05 – Distinguish stage-level vs sprite-level cloud variables

- **Short name:** Stage cloud vs sprite cloud
- **Description:** Students experiment with CreatiCode’s ability to scope cloud variables to the stage (global) or to individual sprites/clone IDs (per-player). They choose the right scope for scores vs avatar cosmetics.
- **Challenge format:** Coding, comparison task. Auto-grading ensures both scopes are implemented and used correctly.
- **CSTA:** MS‑DAA‑DP‑05; SAS‑NW.

---

## Grade 7 – Architectures, Protocols, and Societal Impact

### T31.G7.01 – Model a distributed multiplayer server

- **Short name:** How the server relays player data
- **Description:** Students diagram how a central server receives updates from each client and broadcasts them back, noting timing and ordering constraints.
- **Challenge format:** Concept, diagramming. Auto-grading checks for required components (clients, server, arrows for request/response).
- **CSTA:** MS‑PRO‑PD‑07; MS‑SAS‑NW‑05.

### T31.G7.02 – Design a protocol for multiplayer state sync

- **Short name:** Define the message format
- **Description:** Students specify required fields (player ID, x, y, action, timestamp) and implement serialization/deserialization using lists or JSON-like strings.
- **Challenge format:** Coding + concept. Auto-grading checks the protocol structure and verifies that synced data reconstructs correctly on the receiver side.
- **CSTA:** MS‑DAA‑DF‑02; PRO‑PD.

### T31.G7.03 – Compare network topology options

- **Short name:** Star, mesh, or peer-to-peer?
- **Description:** Students analyze trade-offs among star (client/server), mesh, and peer-to-peer topologies in terms of latency, resilience, and implementation complexity.
- **Challenge format:** Concept, comparative reasoning. Auto-grading checks for mention of latency, reliability, and administrative trade-offs.
- **CSTA:** MS‑SAS‑NW‑04.

### T31.G7.04 – Compare centralized servers with peer-to-peer networks

- **Short name:** When to use mp vs p2p
- **Description:** Students contrast CreatiCode’s standard multiplayer extension (server authoritative) with the `p2p` extension modes (message-only, Nengi/3D). They cite latency, trust, and scalability implications.
- **Challenge format:** Concept + exploration. Auto-grading expects a table/list of pros/cons referencing specific extension behavior.
- **CSTA:** MS‑SAS‑NW‑04; PRO‑PD.

### T31.G7.05 – Analyze societal impacts of networked systems

- **Short name:** How the internet changes communities
- **Description:** Students research benefits (collaboration, access) and harms (privacy loss, misinformation) of widely used networked tools, grounding arguments in real examples.
- **Challenge format:** Concept, short reflection. Auto-grading uses a rubric requiring both benefits and harms.
- **CSTA:** MS‑SAS‑IM‑11; MS‑SAS‑IM‑12.

---

## Grade 8 – Protocol Depth, Security, Resilience, and Monitoring

### T31.G8.01 – Understand TCP/IP routing and packet reassembly

- **Short name:** Follow packets across the internet
- **Description:** Students trace how TCP splits data into packets, how IP addresses route them through multiple hops, and how packets are reassembled in order.
- **Challenge format:** Concept, simulation/worksheet. Auto-grading checks for accurate depiction of IP addressing and packet ordering.
- **CSTA:** MS‑SAS‑NW‑05.

### T31.G8.02 – Design a secure multiplayer/cloud system

- **Short name:** Protect shared systems
- **Description:** Students outline authentication, encryption, and server-side validation steps to defend a multiplayer or cloud-backed app from tampering.
- **Challenge format:** Concept, design plan. Auto-grading uses a rubric emphasizing concrete security measures.
- **CSTA:** MS‑SAS‑SC‑08; MS‑SAS‑SC‑10.

### T31.G8.03 – Implement basic data encryption for privacy

- **Short name:** Encrypt before sending
- **Description:** Students code a simple substitution or XOR cipher that scrambles sensitive values before storing them in the cloud, then decrypts them when read.
- **Challenge format:** Coding, mini-lab. Auto-grading checks that ciphertext differs from plaintext and that decryption restores the original.
- **CSTA:** MS‑SAS‑SC‑09.

### T31.G8.04 – Evaluate network resilience and redundancy

- **Short name:** What happens if a router fails?
- **Description:** Students analyze network diagrams with redundant links and explain how traffic reroutes around failures or how backup servers take over.
- **Challenge format:** Concept, reasoning. Auto-grading checks identification of alternate paths.
- **CSTA:** MS‑SAS‑NW‑05.

### T31.G8.05 – Build a monitoring dashboard for cloud/network events

- **Short name:** Log and monitor cloud updates
- **Description:** Students listen for `when variable changed` events or latency callbacks, log timestamps, and highlight anomalies (e.g., sudden spikes). They understand ongoing monitoring as part of system health.
- **Challenge format:** Coding, instrumentation task. Auto-grading generates test traffic and checks that logs capture events and flag anomalies.
- **CSTA:** MS‑PRO‑PD‑07; SAS‑NW.

---

## Summary

Shifting T31 to Grades 5–8 keeps advanced concepts age-appropriate. Grade 5 builds the mental model for how connectivity works and introduces simple cloud storage. Grade 6 adds concrete protocol work, shared databases, latency, privacy, and cloud scoping. Grades 7–8 tackle architecture choices, security, resilience, encryption, and monitoring—providing the systems knowledge needed to support the multiplayer creations described in T19.
