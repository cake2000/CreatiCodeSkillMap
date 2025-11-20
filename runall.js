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
  // All 36 topics identified from the skill map
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
    { code: "T11", name: "Functions & Procedures" },
    { code: "T12", name: "Organizing Programs" },
    { code: "T13", name: "Testing, Debugging & Error Handling" },
    { code: "T14", name: "2D Games" },
    { code: "T15", name: "Stories & Animation" },
    { code: "T16", name: "User Interfaces" },
    { code: "T17", name: "2D Motion & Physics" },
    { code: "T18", name: "3D Worlds & Games" },
    { code: "T19", name: "Multiplayer Apps" },
    { code: "T20", name: "Algorithmic Art & Creative Coding" },
    { code: "T21", name: "AI Media" },
    { code: "T22", name: "Chatbots & Prompting" },
    { code: "T23", name: "AI Perception" },
    { code: "T24", name: "XO & Generative AI Practices" },
    { code: "T25", name: "Data Representation" },
    { code: "T26", name: "Data Collection & Logging" },
    { code: "T27", name: "Data Analysis & Storytelling" },
    { code: "T28", name: "Chance & Simulations" },
    { code: "T29", name: "Text Data & NLP Foundations" },
    { code: "T30", name: "Devices & Hardware Systems" },
    { code: "T31", name: "Internet & Cloud" },
    { code: "T32", name: "Cybersecurity & Digital Safety" },
    { code: "T33", name: "Connected Services & Tool Wrappers" },
    { code: "T34", name: "Computing History" },
    { code: "T35", name: "Impacts & Ethics" },
    { code: "T36", name: "Careers, Collaboration & Future Paths" }
  ];

  const gradeList = ["K", "1", "2", "3", "4", "5", "6", "7", "8"];

  // Number of iterations for each phase
  const TOPIC_ITERATIONS = 2; // 2 iterations as requested
  const GRADE_ITERATIONS = 2; // 2 iterations for grade-level checking

  console.log("===========================================");
  console.log("Starting Two-Phase Optimization Strategy");
  console.log("===========================================\n");
  console.log(`Phase 1: ${topics.length} topics × ${TOPIC_ITERATIONS} iterations = ${topics.length * TOPIC_ITERATIONS} focused topic passes`);
  console.log(`Phase 2: ${gradeList.length} grades × ${GRADE_ITERATIONS} iterations = ${gradeList.length * GRADE_ITERATIONS} focused grade passes`);
  console.log(`Total: ${topics.length * TOPIC_ITERATIONS + gradeList.length * GRADE_ITERATIONS} focused passes (vs. 900 unfocused)\n`);

  // PHASE 1: Topic-by-Topic Processing
  console.log("===========================================");
  console.log("PHASE 1: Topic-by-Topic Processing");
  console.log("===========================================\n");

  for (let iteration = 0; iteration < TOPIC_ITERATIONS; iteration++) {
    console.log(`\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━`);
    console.log(`  Topic Phase - Iteration ${iteration + 1}/${TOPIC_ITERATIONS}`);
    console.log(`━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n`);

    // Back up allskills.md for this iteration
    const timestamp = Date.now();
    const backupPath = `./skillsv4/allskills_topic_phase_iter${iteration + 1}_${timestamp}.md`;
    execSync(`cp ./skillsv4/allskills.md "${backupPath}"`);
    console.log(`📁 Backed up allskills.md to: ${backupPath.split('/').pop()}\n`);

    for (let i = 0; i < topics.length; i++) {
      const topic = topics[i];
      console.log(`\n[${i + 1}/${topics.length}] Processing Topic ${topic.code}: ${topic.name}`);
      console.log(`${"─".repeat(50)}`);

      const topicPrompt = `## Introduction
We are aiming for "IXL for coding based on creaticode", and we need top quality result. This skill map will become the new golden standard for all coding platforms/educators to rely on.

Read 00-START-HERE.md and spec_v2_updated.md to understand the whole project, and read the key references like CSTA standard draft, AI priorities, and creaticode introduction in the root folder.

Latest version of skills are in "skillsv4" folder. Read the file skillsv4/allskills.md, which contains all skills.

## Phase 1: Topic-Focused Optimization for ${topic.code} - ${topic.name}

You are in PHASE 1 of a two-phase optimization process. In this phase, you are focusing ONLY on skills within topic ${topic.code}.

### Your Specific Tasks for Topic ${topic.code}:

1. **Internal Topic Coherence**
   - Review ALL skills in topic ${topic.code} across grades K-8
   - Ensure each skill is clear, specific, and manageable (like IXL skills)
   - Check for duplicates or significant overlaps WITHIN this topic
   - Verify logical progression from kindergarten through grade 8

2. **Skill Quality Checks**
   - Break down any skills that are too broad or complex
   - Ensure skill descriptions are concrete and assessable
   - Remove or merge redundant skills within the topic
   - When breaking down skills, use sub-IDs like ${topic.code}.G4.05.01, ${topic.code}.G4.05.02

3. **Intra-Topic Dependencies**
   - Fix dependencies WITHIN topic ${topic.code} only
   - Ensure no skill depends on a later skill in the same topic
   - Remove unnecessary same-grade dependencies (earlier skills in same topic/grade are assumed)
   - Apply the X-2 rule: dependencies should be at grades X, X-1, or X-2 only

4. **Grade-Appropriate Content**
   - K-2 skills should be picture-based or unplugged
   - Grade 3+ skills should involve block-based coding
   - Ensure complexity increases appropriately with grade level

IMPORTANT CONSTRAINTS:
- ONLY modify skills in topic ${topic.code}
- Do NOT change inter-topic dependencies (those will be fixed in Phase 2)
- Focus on making this topic internally consistent and high quality
- When you identify inter-topic dependency issues, note them but DO NOT fix them

Additional context about CreatiCode features is available at:
* client side: ../../scratch-workspace
* server side: ../../creaticode-ws
* AI copilot: ../../ScratchCopilot

Use subagents/task to keep main context clean and small. For example, use Task with subagent_type=general-purpose to analyze and fix issues.

Automatically fix all high and medium priority issues within topic ${topic.code}. For output, summarize the key changes you made to topic ${topic.code} skills in skillsv4/allskills.md.`;

      let success = false;
      let retryCount = 0;
      const maxRetries = 3;

      while (!success && retryCount < maxRetries) {
        try {
          const output = execSync(
            `claude --add-dir ../../scratch-workspace --add-dir ../../creaticode-ws --add-dir ../../ScratchCopilot -p "${topicPrompt.replace(/"/g, '\\"')}"`,
            { encoding: "utf8", maxBuffer: 1024 * 1024 * 10 }
          );

          // Check for API errors
          const outputLower = output.toLowerCase();
          if (outputLower.includes("api error") || outputLower.includes("usage limit")) {
            console.log(`\n⚠️  API rate limit hit for topic ${topic.code}`);
            console.log(`⏰ Waiting 15 minutes before retrying...`);
            await waitWithCountdown(15);
            retryCount++;
          } else {
            success = true;
            console.log(`✅ Completed topic ${topic.code}`);
          }
        } catch (error) {
          console.error(`\n❌ Error processing topic ${topic.code}:`, error.message.substring(0, 100));
          const errorStr = error.toString().toLowerCase();
          if (errorStr.includes("api error") || errorStr.includes("usage limit")) {
            console.log(`⏰ API limit - waiting 15 minutes...`);
            await waitWithCountdown(15);
            retryCount++;
          } else {
            console.error(`⚠️  Skipping topic ${topic.code} after error`);
            break;
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
  console.log("===========================================\n");

  for (let iteration = 0; iteration < GRADE_ITERATIONS; iteration++) {
    console.log(`\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━`);
    console.log(`  Grade Phase - Iteration ${iteration + 1}/${GRADE_ITERATIONS}`);
    console.log(`━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n`);

    // Back up allskills.md for this iteration
    const timestamp = Date.now();
    const backupPath = `./skillsv4/allskills_grade_phase_iter${iteration + 1}_${timestamp}.md`;
    execSync(`cp ./skillsv4/allskills.md "${backupPath}"`);
    console.log(`📁 Backed up allskills.md to: ${backupPath.split('/').pop()}\n`);

    for (let i = 0; i < gradeList.length; i++) {
      const grade = gradeList[i];
      console.log(`\n[${i + 1}/${gradeList.length}] Processing Grade ${grade}`);
      console.log(`${"─".repeat(50)}`);

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
We are aiming for "IXL for coding based on creaticode", and we need top quality result. This skill map will become the new golden standard for all coding platforms/educators to rely on.

Read 00-START-HERE.md and spec_v2_updated.md to understand the whole project, and read the key references like CSTA standard draft, AI priorities, and creaticode introduction in the root folder.

Latest version of skills are in "skillsv4" folder. Read the file skillsv4/allskills.md, which contains all skills.

## Phase 2: Grade-Level Cross-Topic Dependency Checking for Grade ${grade}

You are in PHASE 2 of a two-phase optimization process. Phase 1 has already optimized individual topics. Now you are focusing on grade ${grade} to ensure proper cross-topic dependencies and grade-level coherence.

### Your Specific Tasks for Grade ${grade}:

1. **Inter-Topic Dependencies**
   - Review ALL skills at grade ${grade} across all 36 topics
   - Identify and fix missing cross-topic dependencies
   - Ensure skills from different topics that relate to each other have proper dependencies
   - Example: A game skill might need to depend on loops, variables, and graphics skills

2. **Dependency Validation**
   - Enforce the X-2 rule strictly: Grade ${grade} skills can only depend on ${allowedGrades}
   - Remove any dependencies that violate this rule
   - Check for circular dependencies across topics
   - Remove transitive dependencies (if A→B and B→C, remove A→C)

3. **Grade-Level Coherence**
   - Ensure all grade ${grade} skills work together as a cohesive curriculum
   - Identify any skills that seem too advanced or too simple for grade ${grade}
   - Check that foundational skills are available for more advanced skills
   - ${grade !== 'K' ? `Verify that grade ${grade === '1' ? 'K' : parseInt(grade) - 1} provides adequate preparation` : 'Ensure kindergarten skills are truly introductory'}

4. **Scaffolding Verification**
   - Ensure critical gateway skills have proper dependencies
   - Check that complex skills have sufficient prerequisite skills
   - Verify learning pathways make sense across topics at this grade level
   - When needed skills are missing from allowed grades, find or create appropriate scaffolding

IMPORTANT CONSTRAINTS:
- Focus ONLY on grade ${grade} skills and their dependencies
- Do NOT modify skill content or break down skills (that was Phase 1)
- Only modify dependency lists to ensure proper cross-topic connections
- Maintain the integrity of intra-topic progressions from Phase 1

Additional context about CreatiCode features is available at:
* client side: ../../scratch-workspace
* server side: ../../creaticode-ws
* AI copilot: ../../ScratchCopilot

Use subagents/task to keep main context clean and small. For example, use Task with subagent_type=general-purpose to analyze and fix dependency issues.

Automatically fix all dependency issues for grade ${grade} skills. For output, summarize the key dependency changes you made for grade ${grade} in skillsv4/allskills.md.`;

      let success = false;
      let retryCount = 0;
      const maxRetries = 3;

      while (!success && retryCount < maxRetries) {
        try {
          const output = execSync(
            `claude --add-dir ../../scratch-workspace --add-dir ../../creaticode-ws --add-dir ../../ScratchCopilot -p "${gradePrompt.replace(/"/g, '\\"')}"`,
            { encoding: "utf8", maxBuffer: 1024 * 1024 * 10 }
          );

          // Check for API errors
          const outputLower = output.toLowerCase();
          if (outputLower.includes("api error") || outputLower.includes("usage limit")) {
            console.log(`\n⚠️  API rate limit hit for grade ${grade}`);
            console.log(`⏰ Waiting 15 minutes before retrying...`);
            await waitWithCountdown(15);
            retryCount++;
          } else {
            success = true;
            console.log(`✅ Completed grade ${grade}`);
          }
        } catch (error) {
          console.error(`\n❌ Error processing grade ${grade}:`, error.message.substring(0, 100));
          const errorStr = error.toString().toLowerCase();
          if (errorStr.includes("api error") || errorStr.includes("usage limit")) {
            console.log(`⏰ API limit - waiting 15 minutes...`);
            await waitWithCountdown(15);
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

  console.log("\n\n===========================================");
  console.log("✨ Two-Phase Optimization Complete!");
  console.log("===========================================");
  console.log(`\nSummary:`);
  console.log(`- Phase 1: Processed ${topics.length} topics × ${TOPIC_ITERATIONS} iterations`);
  console.log(`- Phase 2: Processed ${gradeList.length} grades × ${GRADE_ITERATIONS} iterations`);
  console.log(`- Total: ${topics.length * TOPIC_ITERATIONS + gradeList.length * GRADE_ITERATIONS} focused optimization passes`);
  console.log(`\nCheck skillsv4/allskills.md for the optimized skill map.\n`);
}

// Run the script
runAllScripts().catch(error => {
  console.error("\n\n❌ Fatal error:", error);
  process.exit(1);
});