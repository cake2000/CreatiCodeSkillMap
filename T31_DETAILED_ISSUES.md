# T31 Detailed Issues by Priority

## HIGH PRIORITY ISSUES (18 total)

### HP-01: T31.G5.03 - Wrong Topic
**Skill:** Fetch and display a web page as markdown
**Issue:** Service-specific implementation, not networking concept
**Current Location:** T31.G5.03
**Should Be:** T33.G6.02 (already exists)
**Block:** `fetch web page as [markdown] from URL`
**Fix:** MOVE to T33 and update 2 dependencies
**Impact:** HIGH - students learning service usage, not networking

---

### HP-02: T31.G5.04 - Wrong Topic
**Skill:** Create and join a multiplayer game session
**Issue:** Multiplayer game mechanics, not networking
**Current Location:** T31.G5.04
**Should Be:** T19 (Multiplayer topic)
**Blocks:** `create game named [...]`, `join multiplayer game [...]`
**Fix:** MOVE to T19 and update 3 dependencies
**Impact:** HIGH - entire multiplayer sequence in wrong topic

---

### HP-03: T31.G5.05 - Wrong Topic
**Skill:** Check multiplayer connection status
**Issue:** Multiplayer implementation detail
**Current Location:** T31.G5.05
**Should Be:** T19
**Block:** `connected to game` (boolean)
**Fix:** MOVE to T19
**Impact:** HIGH - continuation of HP-02

---

### HP-04: T31.G6.02 - Wrong Topic + Duplicate
**Skill:** Read data from a Google Sheet cell
**Issue:** Service-specific, duplicates T33.G6.03
**Current Location:** T31.G6.02
**Should Be:** T33.G6.03 (already exists)
**Blocks:** `read from google sheet [...]`, `value at row column [...]`
**Fix:** MOVE to T33 (merge with existing)
**Impact:** HIGH - confusing duplication

---

### HP-05: T31.G6.03 - Wrong Topic + Duplicate
**Skill:** Write data to a Google Sheet cell
**Issue:** Service-specific, duplicates T33.G6.04
**Current Location:** T31.G6.03
**Should Be:** T33.G6.04 (already exists)
**Blocks:** `write into google sheet [...]`, `set value to [...]`
**Fix:** MOVE to T33 (merge with existing)
**Impact:** HIGH - confusing duplication

---

### HP-06: T31.G6.03.01 - Wrong Topic + Invalid ID
**Skill:** Update entire rows in Google Sheets
**Issue 1:** Service-specific (belongs in T33)
**Issue 2:** Invalid 3-level ID numbering
**Current Location:** T31.G6.03.01
**Should Be:** T33.G7.03 (already exists as "Append rows")
**Block:** `append row [...] from table to sheet`
**Fix:** MOVE to T33 and renumber
**Impact:** HIGH - ID violation + wrong topic

---

### HP-07: T31.G6.03.02 - Wrong Topic + Invalid ID + Duplicate
**Skill:** List and manage multiple Google Sheets
**Issue 1:** Service-specific (belongs in T33)
**Issue 2:** Invalid 3-level ID numbering
**Issue 3:** Duplicates T33.G7.01
**Current Location:** T31.G6.03.02
**Should Be:** T33.G7.01 (already exists)
**Blocks:** `list all sheets`, `add sheet`, `remove sheet`
**Fix:** MOVE to T33 (merge with existing) and renumber
**Impact:** HIGH - multiple violations

---

### HP-08: T31.G6.06 - Wrong Topic
**Skill:** Add sprites to multiplayer game world
**Issue:** Multiplayer implementation
**Current Location:** T31.G6.06
**Should Be:** T19
**Blocks:** `add this sprite to game as [...]`, `when added to game`, `remove sprite from game`
**Fix:** MOVE to T19
**Impact:** HIGH - core multiplayer mechanic

---

### HP-09: T31.G7.01 - Wrong Topic (possibly)
**Skill:** Model a distributed multiplayer server
**Issue:** Either make generic or move to T19
**Current Location:** T31.G7.01
**Should Be:** Either generalize to distributed systems OR move to T19
**Fix Option 1:** Rewrite as general distributed systems concept
**Fix Option 2:** MOVE to T19
**Impact:** MEDIUM-HIGH - could work in T31 if generalized

---

### HP-10: T31.G7.02 - Wrong Topic
**Skill:** Synchronize sprite movement in multiplayer games
**Issue:** Multiplayer implementation
**Current Location:** T31.G7.02
**Should Be:** T19
**Blocks:** `synchronously set speed x (X) y (Y)`, `synchronously set speed (SPEED) dir (DIR)`
**Fix:** MOVE to T19
**Impact:** HIGH - core multiplayer mechanic

---

### HP-11: T31.G7.02.01 - Wrong Topic + Invalid ID
**Skill:** Broadcast messages in multiplayer games
**Issue 1:** Multiplayer implementation
**Issue 2:** Invalid 3-level ID numbering
**Current Location:** T31.G7.02.01
**Should Be:** T19
**Block:** `broadcast [MESSAGE] with parameter [PARAMETER] mode [MODE]`
**Fix:** MOVE to T19 and renumber
**Impact:** HIGH - ID violation + wrong topic

---

### HP-12: T31.G7.02.02 - Wrong Topic + Invalid ID
**Skill:** Handle sprite collisions in multiplayer games
**Issue 1:** Multiplayer implementation
**Issue 2:** Invalid 3-level ID numbering
**Current Location:** T31.G7.02.02
**Should Be:** T19
**Block:** `when touching [SPRITE] will [STOPTYPE] and trigger [MESSAGE]`
**Fix:** MOVE to T19 and renumber
**Impact:** HIGH - ID violation + wrong topic

---

### HP-13: T31.G7.02.03 - Wrong Topic + Invalid ID
**Skill:** Insert data into a database collection
**Issue 1:** Database service implementation
**Issue 2:** Invalid 3-level ID numbering
**Current Location:** T31.G7.02.03
**Should Be:** T33 (need new skill)
**Block:** `insert from table [...] into collection`
**Fix:** MOVE to T33 and renumber
**Impact:** HIGH - database operations belong in T33

---

### HP-14: T31.G7.02.04 - Wrong Topic + Invalid ID
**Skill:** Fetch data from a database collection
**Issue 1:** Database service implementation
**Issue 2:** Invalid 3-level ID numbering
**Current Location:** T31.G7.02.04
**Should Be:** T33 (need new skill)
**Block:** `fetch from collection [...] where <CONDITION>`
**Fix:** MOVE to T33 and renumber
**Impact:** HIGH - database operations belong in T33

---

### HP-15: T31.G7.02.05 - Wrong Topic + Invalid ID
**Skill:** Update and remove database records
**Issue 1:** Database service implementation
**Issue 2:** Invalid 3-level ID numbering
**Current Location:** T31.G7.02.05
**Should Be:** T33 (need new skill)
**Blocks:** `update collection [...]`, `remove all documents`
**Fix:** MOVE to T33 and renumber
**Impact:** HIGH - database operations belong in T33

---

### HP-16: T31.G8.04 - Wrong Topic
**Skill:** Implement privacy protection for AI data
**Issue:** This is security/privacy, not networking
**Current Location:** T31.G8.04
**Should Be:** T32 (Cybersecurity)
**Fix:** MOVE to T32
**Impact:** HIGH - clearly belongs in security topic

---

### HP-17: Missing Skill - URL Parameters
**Issue:** Block exists but not taught
**Block:** `read URL parameter [PARAMETER]` (Sensing category)
**Should Add:** T31.G5.03 (new - after renumbering)
**Grade Level:** 5
**Description:** Read and use URL parameters in projects
**Dependencies:** T09.G3.01.04 (variables), T31.G5.01
**Impact:** HIGH - simple web communication concept missing

---

### HP-18: Missing Skill - User Data Storage
**Issue:** Blocks exist but not taught
**Blocks:** `store user data key [KEY] value [VALUE]`, `read user data key [KEY]`
**Should Add:** T31.G5.06 (new)
**Grade Level:** 5
**Description:** Store and retrieve persistent user data
**Dependencies:** T09.G4.04 (variables), T31.G5.01
**Impact:** HIGH - essential cloud storage concept missing

---

## MEDIUM PRIORITY ISSUES (12 total)

### MP-01: T31.G6.04 - Vague Implementation
**Skill:** Measure and analyze how latency affects AI responsiveness and fairness
**Issue:** Not clear what blocks to use or how to measure
**Current Status:** Conceptual skill with unclear implementation
**Fix:** Add specific implementation using timer blocks:
- Use `reset timer` and `timer` blocks
- Measure time before/after AI calls
- Record measurements in variables/lists
- Compare different scenarios
**Impact:** MEDIUM - good concept but needs specifics

---

### MP-02: T31.G6.05 - Possibly Wrong Topic
**Skill:** Evaluate privacy when sharing AI-generated content and data
**Issue:** This seems more like T32 (Cybersecurity) or T35 (Ethics)
**Current Location:** T31.G6.05
**Consideration:** Move to T32 or T35, or keep as cross-topic
**Fix:** Review with T32/T35 scope to decide
**Impact:** MEDIUM - borderline topic placement

---

### MP-03: T31.G8.01 - Unclear if Conceptual or Hands-On
**Skill:** Architect edge vs cloud processing pipelines for AI
**Issue:** Not clear what CreatiCode blocks demonstrate this
**Current Status:** Heavy AI dependencies (T21-T24), more conceptual than hands-on
**Fix:** Clarify as design/diagramming activity:
- Students create flowcharts/diagrams
- Identify which computations happen on-device vs cloud
- No specific CreatiCode blocks required
- Make it explicitly a design skill
**Impact:** MEDIUM - good skill but needs clarity

---

### MP-04: T31.G8.02 - Vague Requirements
**Skill:** Understand AI service network requirements
**Issue:** Not clear how to analyze or what to measure
**Current Status:** Conceptual without specific tasks
**Fix:** Add measurable analysis tasks:
- Estimate bandwidth for image upload (T21)
- Measure latency for chatbot responses (T22)
- Calculate data transfer for video streaming (T23)
- Create comparison charts
**Impact:** MEDIUM - needs specific metrics

---

### MP-05: T31.G8.03 - Possibly Wrong Topic
**Skill:** Design secure AI-powered cloud systems
**Issue:** This is security-focused, might belong in T32
**Current Location:** T31.G8.03
**Consideration:** Move to T32 or keep as networking security
**Fix:** Review with T32 to determine placement
**Impact:** MEDIUM - security vs networking architecture

---

### MP-06: T31.G8.05 - Vague Implementation
**Skill:** Evaluate AI service resilience and fallbacks
**Issue:** Not clear how to implement in CreatiCode
**Current Status:** Conceptual skill
**Fix:** Add specific implementation guidance:
- Use conditionals to check for empty responses
- Implement cached responses as fallback
- Create "offline mode" using local data
- Add error messages and retry buttons
**Impact:** MEDIUM - good concept needs specifics

---

### MP-07: T31.G8.06 - Too Advanced/Ambitious
**Skill:** Build AI service monitoring and ethics dashboards
**Issue:** Very complex, not clear what CreatiCode supports
**Current Status:** Ambitious capstone
**Fix Option 1:** Simplify to "Track AI service usage metrics"
**Fix Option 2:** Move to advanced track
**Suggested:** Create simple metrics display:
- Count API calls using variables
- Display response times
- Track error rates
- No full "dashboard" required
**Impact:** MEDIUM - too ambitious for Grade 8

---

### MP-08: Missing Scaffolding - Grade 3
**Issue:** No hands-on blocks introduced in Grade 3
**Current:** All G3 skills are conceptual
**Fix:** Add simple network communication concept:
- Understand programs can send/receive information
- Identify examples (messaging, weather apps)
- Prepares for Grade 5 hands-on
**Impact:** MEDIUM - improves progression

---

### MP-09: Missing Scaffolding - Grade 4
**Issue:** No hands-on blocks introduced in Grade 4
**Current:** All G4 skills are conceptual
**Fix:** Add network speed/bandwidth concept:
- Categorize activities by data usage
- Understand connection speed differences
- Prepares for latency measurements in G6
**Impact:** MEDIUM - improves progression

---

### MP-10: Missing Skill - Game Leaderboards
**Issue:** Leaderboard blocks exist but not taught
**Blocks:** `record player score`, `show game leaderboard`, `hide game leaderboard`, `clear scores for`
**Should Add:** T31.G6.07 (new)
**Grade Level:** 6
**Description:** Record scores and display leaderboards
**Dependencies:** T09.G4.04 (variables), T31.G5.06 (user data)
**Impact:** MEDIUM - important cloud data aggregation concept

---

### MP-11: Missing Skill - Network Error Handling
**Issue:** No skill teaches handling network failures
**Should Add:** T31.G7.06 (new)
**Grade Level:** 7
**Description:** Handle network errors and offline states
**Implementation:**
- Check if web fetch returns empty
- Detect offline status
- Show user-friendly errors
**Dependencies:** T08.G5.01 (conditionals), T31.G6.01 (HTTP)
**Impact:** MEDIUM - real-world skill missing

---

### MP-12: Heavy AI Cross-Dependencies
**Issue:** 11 skills in G6-G8 heavily reference T21-T24
**Affected Skills:** G6.04, G6.05, G8.01-G8.06
**Current Problem:** Too AI-specific
**Fix:** Make skills more generic:
- Provide non-AI examples alongside AI examples
- Make concepts applicable to any cloud service
- Reduce tight coupling to AI topics
**Impact:** MEDIUM - improves topic independence

---

## LOW PRIORITY ISSUES (7 total)

### LP-01: T31.G2.02 - Possibly Wrong Topic
**Skill:** Practice safe online behavior (picture-based)
**Issue:** Overlaps with T32 (Cybersecurity)
**Current Location:** T31.G2.02
**Consideration:** Might belong in T32 instead
**Impact:** LOW - works in either topic, minor overlap

---

### LP-02: T31.G4.02 - Possibly Wrong Topic
**Skill:** Identify secure vs insecure websites
**Issue:** Security-focused, might belong in T32
**Current Location:** T31.G4.02
**Consideration:** Might belong in T32 instead
**Impact:** LOW - works in either topic, could stay

---

### LP-03: Missing Transition K-2 to Grade 3
**Issue:** Could add transition skill
**Current:** Jump from G2 picture-based to G3 diagramming
**Fix:** Could add G3.03 as bridge activity
**Impact:** LOW - current progression acceptable

---

### LP-04: Missing Network Troubleshooting Concepts
**Issue:** No skills about debugging connection issues
**Examples:**
- Why isn't the internet working?
- How to diagnose network problems
- Understanding error messages
**Fix:** Could add to G7 or G8
**Impact:** LOW - nice to have but not essential

---

### LP-05: Missing Bandwidth/Data Transfer Details
**Issue:** No skills measuring how much data different activities use
**Examples:**
- Estimate data for different media types
- Understand data caps
- Compare data usage across activities
**Fix:** Could enhance G4.03 (if added) or create new G6 skill
**Impact:** LOW - practical but not core networking

---

### LP-06: Missing Local vs Cloud Storage Comparison
**Issue:** No T31 skill comparing storage options
**Note:** T33.G5.01 already covers this
**Fix:** Could add conceptual skill in T31.G6, or reference T33.G5.01
**Impact:** LOW - already covered in T33

---

### LP-07: Too Much AI Cross-Dependency (General)
**Issue:** T31 relies heavily on T21-T24 throughout
**Specific Skills:** 11 skills reference AI topics
**Impact on Learning:** Students might need AI skills before networking
**Fix:** Make AI examples optional, provide non-AI alternatives
**Impact:** LOW - AI is relevant to modern networking, but should be optional

---

## Summary Statistics

| Priority | Count | Category Breakdown |
|----------|-------|-------------------|
| HIGH | 18 | Wrong topic: 16, Missing skills: 2 |
| MEDIUM | 12 | Vague: 4, Missing: 3, Wrong topic: 2, Other: 3 |
| LOW | 7 | Topic overlap: 2, Missing optional: 5 |
| **TOTAL** | **37** | |

### Issues by Type

| Type | Count | Priority Distribution |
|------|-------|----------------------|
| Wrong Topic | 18 | HIGH: 16, MED: 2 |
| Invalid ID Format | 7 | HIGH: 7 (included in wrong topic count) |
| Missing Skill | 5 | HIGH: 2, MED: 3 |
| Vague/Unclear | 4 | MED: 4 |
| Topic Overlap | 4 | MED: 2, LOW: 2 |
| Missing Optional | 5 | LOW: 5 |

### Skills by Destination

| Destination | Count from T31 | Purpose |
|-------------|---------------|---------|
| **T33** (Connected Services) | 10 | Cloud service implementations |
| **T19** (Multiplayer) | 8 | Multiplayer game mechanics |
| **T32** (Cybersecurity) | 3-5 | Security/privacy focused skills |
| **Stay in T31** | 19 | Core networking concepts |
| **Add to T31** | 4 | Missing essential skills |

### Blocks Coverage

| Block Category | Total Blocks | Currently in T31 | Should Be |
|---------------|--------------|------------------|-----------|
| Cloud (Google Sheets/Drive/Fetch) | 15 | 7 skills ❌ | T33 ✅ |
| Multiplayer | 13 | 8 skills ❌ | T19 ✅ |
| Database | 12 | 3 skills ❌ | T33 ✅ |
| Game (Persistent Data) | 5 | 0 skills ❌ | T31 NEW ✅ |
| Sensing (URL params) | 1 | 0 skills ❌ | T31 NEW ✅ |
| **Conceptual (no blocks)** | N/A | 14 skills ✅ | T31 KEEP ✅ |

---

## Prioritized Action Plan

### Phase 1: Critical Fixes (Must Do)
1. Move 10 skills to T33 (HP-01, HP-04, HP-05, HP-06, HP-07, HP-13, HP-14, HP-15)
2. Move 8 skills to T19 (HP-02, HP-03, HP-08, HP-10, HP-11, HP-12)
3. Fix 7 ID numbering violations (included in above moves)
4. Add 2 missing skills (HP-17: URL params, HP-18: user data)

### Phase 2: Important Improvements (Should Do)
5. Clarify 4 vague skills (MP-01, MP-03, MP-04, MP-06)
6. Simplify G8.06 (MP-07)
7. Add leaderboard skill (MP-10)
8. Add network error handling (MP-11)
9. Review 3 skills for T32 move (HP-16, MP-02, MP-05)

### Phase 3: Polish (Nice to Have)
10. Add G3-G4 scaffolding (MP-08, MP-09)
11. Reduce AI coupling (MP-12)
12. Review topic overlaps (LP-01, LP-02)
13. Consider optional additions (LP-04, LP-05)

---

## Expected Outcomes

After addressing all HIGH and MEDIUM priority issues:

### T31 Will Have:
- **~25 total skills** (down from 37)
- **Clear focus** on networking concepts
- **No service-specific** implementation details
- **Proper scaffolding** from K-8
- **Complete block coverage** for network-related concepts
- **Valid ID format** throughout

### Students Will:
- ✅ Understand how the internet works (infrastructure, protocols)
- ✅ Understand network architectures (client-server, P2P, topologies)
- ✅ Understand cloud computing concepts (edge vs cloud, distributed systems)
- ✅ Practice with basic cloud features (URL params, user data, leaderboards)
- ✅ Understand performance concepts (latency, bandwidth)
- ✅ Understand societal impacts of networked systems

### Students Will NOT:
- ❌ Learn Google Sheets implementation (that's T33)
- ❌ Learn database operations (that's T33)
- ❌ Learn multiplayer game mechanics (that's T19)
- ❌ Get confused by duplicated skills
- ❌ Face ID numbering inconsistencies
