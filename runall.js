const { execSync } = require("child_process");

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function waitWithCountdown(minutes) {
  const totalSeconds = minutes * 60;
  for (let remaining = totalSeconds; remaining > 0; remaining--) {
    const mins = Math.floor(remaining / 60);
    const secs = remaining % 60;
    process.stdout.write(`\r⏰ Waiting: ${mins}:${secs.toString().padStart(2, '0')} remaining...`);
    await sleep(1000);
  }
  process.stdout.write('\r                                        \r');
}

async function runAllScripts() {
  // Print start date and time
  const startTime = new Date();
  console.log("\n╔══════════════════════════════════════════════════════════╗");
  console.log(`║  Start Time: ${startTime.toLocaleString()}  ║`);
  console.log("╚══════════════════════════════════════════════════════════╝\n");

  // All 34 topics identified from the skill map (Updated v7)
  const topics = [
    { code: "T01", name: "Everyday Algorithms" },
    { code: "T02", name: "Algorithm Diagrams" },
    { code: "T03", name: "Problem Decomposition" },
    { code: "T04", name: "Algorithm Patterns" },
    { code: "T05", name: "Human-Centered Design" },
    { code: "T06", name: "Events & Sequences" },
    { code: "T07", name: "Loops" },
    { code: "T08", name: "Conditions & Logic" },
    { code: "T09", name: "Variables & Expressions" },
    { code: "T10", name: "Lists & Tables" },
    { code: "T11", name: "Functions & Organization" },
    { code: "T12", name: "Testing, Debugging & Error Handling" },
    { code: "T13", name: "2D Games" },
    { code: "T14", name: "Stories & Animation" },
    { code: "T15", name: "User Interfaces" },
    { code: "T16", name: "2D Motion & Physics" },
    { code: "T17", name: "3D Worlds & Games" },
    { code: "T18", name: "Multiplayer Apps" },
    { code: "T19", name: "Algorithmic Art & Creative Coding" },
    { code: "T20", name: "AI Media" },
    { code: "T21", name: "Chatbots & Prompting" },
    { code: "T22", name: "AI Perception" },
    { code: "T23", name: "Generative AI Practices" },
    { code: "T24", name: "Data Representation" },
    { code: "T25", name: "Data Collection & Logging" },
    { code: "T26", name: "Data Analysis & Storytelling" },
    { code: "T27", name: "Chance & Simulations" },
    { code: "T28", name: "Text Data & NLP Foundations" },
    { code: "T29", name: "Devices & Hardware Systems" },
    { code: "T30", name: "Internet & Cloud" },
    { code: "T31", name: "Cybersecurity & Digital Safety" },
    { code: "T32", name: "Digital Citizenship" },
    { code: "T33", name: "Connected Services & Tool Wrappers" },
    { code: "T34", name: "Computing History" }
  ];

  const gradeList = ["K", "1", "2", "3", "4", "5", "6", "7", "8"];

  // Number of iterations for each phase
  const TOPIC_ITERATIONS = 1; 
  const GRADE_ITERATIONS = 0; 

  console.log("===========================================");
  console.log("Starting Two-Phase Optimization Strategy");
  console.log("===========================================\n");
  console.log(`Phase 1: ${topics.length} topics × ${TOPIC_ITERATIONS} iterations = ${topics.length * TOPIC_ITERATIONS} focused topic passes`);
  console.log(`Phase 2: ${gradeList.length} grades × ${GRADE_ITERATIONS} iterations = ${gradeList.length * GRADE_ITERATIONS} focused grade passes`);
  console.log(`Total: ${topics.length * TOPIC_ITERATIONS + gradeList.length * GRADE_ITERATIONS} focused passes\n`);

  // PHASE 1: Topic-by-Topic Processing
  console.log("===========================================");
  console.log("PHASE 1: Topic-by-Topic Processing");
  console.log(`Started at: ${new Date().toLocaleString()}`);
  console.log("===========================================\n");

  for (let iteration = 0; iteration < TOPIC_ITERATIONS; iteration++) {
    console.log(`\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━`);
    console.log(`  Topic Phase - Iteration ${iteration + 1}/${TOPIC_ITERATIONS}`);
    console.log(`  ${new Date().toLocaleString()}`);
    console.log(`━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n`);

    // Back up allskills.md for this iteration
    const timestamp = Date.now();
    const backupPath = `./skillsv5/allskills_topic_phase_iter${iteration + 1}_${timestamp}.md`;
    execSync(`cp ./skillsv5/allskills.md "${backupPath}"`);
    console.log(`📁 Backed up allskills.md to: ${backupPath.split('/').pop()}\n`);

    for (let i = 0; i < topics.length; i++) {
      // if ( iteration == 0 && i < 32) continue;
      const topic = topics[i];
      console.log(`\n[${i + 1}/${topics.length}] Processing Topic ${topic.code}: ${topic.name}`);
      console.log(`${"─".repeat(50)}`);

      console.log(`  ${new Date().toLocaleString()}`);

      const topicPrompt = `## Introduction
We are aiming for "IXL for coding based on CreatiCode", and we need top quality results. This skill map will become the new golden standard for all coding platforms/educators to rely on. Our goal is not only to build solid foundations in coding concepts but also empower students to create amazing projects using CreatiCode's unique features, and along the way develop problem solving skills that will serve them for life.

Read 00-START-HERE.md and spec_v2_updated.md to understand the whole project, and read the key references like CSTA standard draft, AI priorities, and creaticode introduction in the root folder.

Latest version of skills are in "skillsv5" folder. Read the file skillsv5/allskills.md, which contains all skills.

## Phase 1: Topic-Focused Optimization for ${topic.code} - ${topic.name}

You are in PHASE 1 of a two-phase optimization process. In this phase, you are focusing ONLY on skills within topic ${topic.code}.

### Your Specific Tasks for Topic ${topic.code}:

1. **Internal Topic Coherence & Granularity**
   - Review ALL skills in topic ${topic.code} across grades K-8.
   - Ensure each skill is clear, specific, and manageable (atomic, IXL-style).
   - **Break down any skill** that is too broad (e.g., "Create a game") into sub-skills (e.g., "Move player," "Detect collision," "Update score"). Use sub-IDs like ${topic.code}.G4.05.01.
   - Check for duplicates or significant overlaps WITHIN this topic.
   - Verify logical progression from kindergarten through grade 8.

2. **Skill Quality & Assessability**
   - **Standardize verbs**: Ensure skill titles use active, measurable verbs (e.g., "Explain," "Trace," "Predict," "Debug") rather than vague ones like "Understand."
   - **Visual Assets**: For K-2 skills, ensure descriptions specify "picture cards" or "visual scenarios" clearly.
   - **CreatiCode Features**: Ensure skills accurately reflect CreatiCode's blocks (e.g., specific 3D, Physics, or AI blocks). Refer to blocks in 	 '../../ScratchCopilot/blockdes8.txt' if needed.
   - **Project Scoping**: For G8 capstone skills, ensure they are scoped as manageable mini-projects or properly broken down.

3. **Intra-Topic Dependencies ONLY**
   - Fix dependencies WITHIN topic ${topic.code} only.
   - Ensure no skill depends on a later skill in the same topic.
   - Remove unnecessary same-grade dependencies (linear progression is assumed).
   - Apply the X-2 rule: dependencies should be at grades X, X-1, or X-2 only.
   - **CRITICAL: PRESERVE all dependencies to OTHER topics.**

4. **Grade-Appropriate Content**
   - K-2 skills should be picture-based or unplugged.
   - Grade 3+ skills should involve block-based coding.
   - Ensure complexity increases appropriately.

CRITICAL RULES - NEVER VIOLATE THESE:
- **NEVER delete any skills** - only improve/clarify their descriptions or split them.
- **NEVER remove dependencies to skills from OTHER topics** (preserve all cross-topic dependencies).
- **NEVER modify skills from other topics** - focus ONLY on ${topic.code}.
- Only remove a dependency if it's genuinely incorrect AND within topic ${topic.code}.

IMPORTANT CONSTRAINTS:
- ONLY modify skills in topic ${topic.code}.
- Do NOT change inter-topic dependencies (those will be fixed in Phase 2).
- Focus on making this topic internally consistent and high quality.

Additional context about CreatiCode features is available at:
* client side: ../../scratch-workspace
* server side: ../../creaticode-ws
* AI copilot: ../../ScratchCopilot

Use subagents/task to keep main context clean and small.

Now, automatically fix all high and medium priority issues within topic ${topic.code}. For output, summarize the key changes you made to topic ${topic.code} skills in skillsv5/allskills.md.`;

      let success = false;
      let retryCount = 0;
      const maxRetries = 3; // Reduced from 30000 to 3 for realism in this script context

      while (!success && retryCount < maxRetries) {
        try {
          const output = execSync(
            `claude --add-dir ../../scratch-workspace --add-dir ../../creaticode-ws --add-dir ../../ScratchCopilot -p "${topicPrompt.replace(/"/g, '\"')}"`,
            { encoding: "utf8", maxBuffer: 1024 * 1024 * 10 }
          );

          // Check for API errors
          const outputLower = output.toLowerCase();
          if (outputLower.includes("api error") || outputLower.includes("usage limit")) {
            console.log(`\n⚠️  API rate limit hit for topic ${topic.code}`);
            console.log(`⏰ Waiting 3 minutes before retrying...`);
            await waitWithCountdown(3);
            console.log(`\nRetrying topic ${topic.code} (Attempt ${retryCount + 1}/${maxRetries})...`);
            retryCount++;
          } else {
            success = true;
            console.log(`✅ Completed topic ${topic.code}`);
            // wait one minute
            console.log(`⏳ Waiting 1 minute to avoid rate limits...`);
            await waitWithCountdown(1);
          }
        } catch (error) {
          console.error(`\n❌ Error processing topic ${topic.code}:`, error.message.substring(0, 100));
          const errorStr = error.toString().toLowerCase();
          if (1 || errorStr.includes("api error") || errorStr.includes("usage limit")) {
            console.log(`⏰ waiting 3 minutes ${new Date().toLocaleString()}...`);
            await waitWithCountdown(3);
            console.log(`\nRetrying topic ${topic.code} (Attempt ${retryCount + 1}/${maxRetries})...`);
            retryCount++;
          } else {
             // Break on non-rate-limit errors to avoid infinite loops in testing
             retryCount++;
          }
        }
      }

      if (!success) {
        console.log(`⚠️  Failed to process topic ${topic.code} after ${maxRetries} retries`);
      }
    }

    console.log(`\n✅ Completed Topic Phase Iteration ${iteration + 1}/${TOPIC_ITERATIONS}`);
  }

  // PHASE 2: Grade-by-Grade Processing
  console.log("\n\n===========================================");
  console.log("PHASE 2: Grade-by-Grade Cross-Topic Dependency Checking");
  console.log(`Started at: ${new Date().toLocaleString()}`);
  console.log("===========================================\n");

  for (let iteration = 0; iteration < GRADE_ITERATIONS; iteration++) {
    console.log(`\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━`);
    console.log(`  Grade Phase - Iteration ${iteration + 1}/${GRADE_ITERATIONS}`);
    console.log(`  ${new Date().toLocaleString()}`);
    console.log(`━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n`);

    // Back up allskills.md for this iteration
    const timestamp = Date.now();
    const backupPath = `./skillsv5/allskills_grade_phase_iter${iteration + 1}_${timestamp}.md`;
    execSync(`cp ./skillsv5/allskills.md "${backupPath}"`);
    console.log(`📁 Backed up allskills.md to: ${backupPath.split('/').pop()}\n`);

    for (let i = 0; i < gradeList.length; i++) {
      const grade = gradeList[i];
      console.log(`\n[${i + 1}/${gradeList.length}] Processing Grade ${grade}`);
      console.log(`${"─".repeat(50)}`);

      // print date time
      console.log(`  ${new Date().toLocaleString()}`);

      // Calculate allowed dependency grades
      let allowedGrades;
      if (grade === 'K') {
        allowedGrades = 'K only';
      } else if (grade === '1') {
        allowedGrades = 'K and 1';
      } else {
        const gradeNum = parseInt(grade);
        allowedGrades = `grades ${gradeNum - 2}, ${gradeNum - 1}, and ${gradeNum}`;
      }

      const gradePrompt = `## Introduction
We are aiming for "IXL for coding based on CreatiCode", and we need top quality results. This skill map will become the new golden standard for all coding platforms/educators to rely on.

Read 00-START-HERE.md and spec_v2_updated.md to understand the whole project.

Latest version of skills are in "skillsv5" folder. Read the file skillsv5/allskills.md, which contains all skills.

## Phase 2: Grade-Level Cross-Topic Dependency Checking for Grade ${grade}

You are in PHASE 2 of a two-phase optimization process. Phase 1 has already optimized individual topics. Now you are focusing on all skills in grade ${grade} to ensure proper cross-topic dependencies and grade-level coherence.

### Your Specific Tasks for Grade ${grade}:

1. **Inter-Topic Dependencies**
   - Review ALL skills at grade ${grade} across all 34 topics.
   - **ADD missing cross-topic dependencies**:
     - **Cybersecurity (T31) & DigCit (T32)** -> Connected Services (T33) & Multiplayer (T18).
     - **Math (T09/T27)** -> Data Science (T24-T26).
     - **UI (T15)** -> App projects in other topics.
   - Ensure skills from different topics that relate to each other have proper dependencies.

2. **Dependency Validation**
   - Enforce the X-2 rule strictly: Grade ${grade} skills can only depend on ${allowedGrades}.
   - Fix dependencies that violate this rule by finding appropriate scaffolding skills.
   - Check for circular dependencies across topics.

3. **Grade-Level Coherence**
   - Ensure all grade ${grade} skills work together as a cohesive curriculum.
   - Check that foundational skills are available for more advanced skills.
   - Add dependencies where skills clearly build on each other.

4. **Scaffolding Verification**
   - Ensure critical gateway skills have proper dependencies.
   - Check that complex skills have sufficient prerequisite skills.

CRITICAL RULES - NEVER VIOLATE THESE:
- **NEVER delete any skills** - Phase 1 already handled skill quality.
- **Only remove a dependency if it's genuinely incorrect or truly redundant.**
- **Add dependencies liberally** - better to over-specify than under-specify prerequisites.
- **Do not update skill ID** when removing a skill to avoid invalidating existing dependencies.
- **Preserve all valid dependencies** even if they seem numerous.

IMPORTANT CONSTRAINTS:
- Focus ONLY on grade ${grade} skills and their dependencies.
- Do NOT modify skill content or break down skills (that was Phase 1).
- Only modify dependency lists to ensure proper cross-topic connections.

Additional context about CreatiCode features is available at:
* client side: ../../scratch-workspace
* server side: ../../creaticode-ws
* AI copilot: ../../ScratchCopilot

Use subagents/task to keep main context clean and small.

Automatically fix all dependency issues for high and intermediate priorities automatically (no need to ask me) for grade ${grade} skills. For output, summarize the key dependency changes you made for grade ${grade} in skillsv5/allskills.md.`;

      let success = false;
      let retryCount = 0;
      const maxRetries = 30000000;

      while (!success && retryCount < maxRetries) {
        try {
          const output = execSync(
            `claude --add-dir ../../scratch-workspace --add-dir ../../creaticode-ws --add-dir ../../ScratchCopilot -p "${gradePrompt.replace(/"/g, '\"')}"`,
            { encoding: "utf8", maxBuffer: 1024 * 1024 * 10 }
          );

          // Check for API errors
            console.log(`\n⚠️  OUPUT for grade ${grade}: ${output}`);
          const outputLower = output.toLowerCase();
          if (outputLower.includes("api error") || outputLower.includes("usage limit")) {
            console.log(`\n⚠️  API rate limit hit for grade ${grade}`);
            console.log(`⏰ Waiting 3 minutes before retrying...`);
            await waitWithCountdown(3);
            retryCount++;
          } else {
            success = true;
            console.log(`✅ Completed grade ${grade}`);
          }
        } catch (error) {
          console.error(`\n❌ Error processing grade ${grade}:`, error.message.substring(0, 100));
          const errorStr = error.toString().toLowerCase();
          if (1 || errorStr.includes("api error") || errorStr.includes("usage limit")) {
            console.log(`⏰ API limit - waiting 3 minutes...`);
            await waitWithCountdown(3);
            retryCount++;
          } else {
            console.error(`⚠️  Skipping grade ${grade} after error`);
            break;
          }
        }
      }

      if (!success) {
        console.log(`⚠️  Failed to process grade ${grade} after ${maxRetries} retries`);
      }
    }

    console.log(`\n✅ Completed Grade Phase Iteration ${iteration + 1}/${GRADE_ITERATIONS}`);
  }

  const endTime = new Date();
  const elapsedTime = Math.round((endTime - startTime) / 1000); // in seconds
  const hours = Math.floor(elapsedTime / 3600);
  const minutes = Math.floor((elapsedTime % 3600) / 60);
  const seconds = elapsedTime % 60;

  console.log("\n\n===========================================");
  console.log("✨ Two-Phase Optimization Complete!");
  console.log("===========================================");
  console.log(`\nCompleted at: ${endTime.toLocaleString()}`);
  console.log(`Total elapsed time: ${hours}h ${minutes}m ${seconds}s`);
  console.log(`\nSummary:`);
  console.log(`- Phase 1: Processed ${topics.length} topics × ${TOPIC_ITERATIONS} iterations`);
  console.log(`- Phase 2: Processed ${gradeList.length} grades × ${GRADE_ITERATIONS} iterations`);
  console.log(`- Total: ${topics.length * TOPIC_ITERATIONS + gradeList.length * GRADE_ITERATIONS} focused optimization passes`);
  console.log(`\nCheck skillsv5/allskills.md for the optimized skill map.\n`);
}

// Run the script
runAllScripts().catch(error => {
  console.error("\n\n❌ Fatal error:", error);
  process.exit(1);
});
