const { execSync, spawnSync } = require("child_process");
const fs = require("fs");

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

  const loadAvailableGradeTopics = () => {
    const content = fs.readFileSync("./skillsv5/allskills.md", "utf8");
    const set = new Set();
    const regex = /ID:\s*T(\d{2})\.G([K1-8])/g;
    let match;
    while ((match = regex.exec(content)) !== null) {
      const topicCode = `T${match[1]}`;
      const gradeCode = match[2].toUpperCase();
      set.add(`${gradeCode}-${topicCode}`);
    }
    return set;
  };

  // Number of iterations for each phase
  const TOPIC_ITERATIONS = 20; 
  const GRADE_ITERATIONS = 1; 

  console.log("===========================================");
  console.log("Starting Two-Phase Optimization Strategy");
  console.log("===========================================\n");
  console.log(`Phase 1: ${topics.length} topics × ${TOPIC_ITERATIONS} iterations = ${topics.length * TOPIC_ITERATIONS} focused topic passes`);
  const phase2Combos = gradeList.length * topics.length;
  console.log(`Phase 2: ${gradeList.length} grades × ${topics.length} topics × ${GRADE_ITERATIONS} iterations = ${phase2Combos * GRADE_ITERATIONS} possible grade-topic passes (skips combos with no skills)`);
  console.log(`Total: ${topics.length * TOPIC_ITERATIONS + phase2Combos * GRADE_ITERATIONS} focused passes\n`);

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
      if ( iteration == 0 && i < 28) continue;
      const topic = topics[i];
      console.log(`\n[${i + 1}/${topics.length}] Processing Topic ${topic.code}: ${topic.name}`);
      console.log(`${"─".repeat(50)}`);

      console.log(`  ${new Date().toLocaleString()}`);

      const topicPrompt = `AUTONOMOUS MODE: Do NOT ask any questions. Do NOT ask for clarification. Do NOT ask for permission. Proceed immediately with your best judgment. This is a non-interactive batch session.

Your task: Optimize topic ${topic.code} (${topic.name}) in the skill map.

## Step 1: Read these files first
- skillmap_run_context.md for project context
- skillsv5/allskills.md for all current skills
- creaticode.md for CreatiCode platform details, especially new blocks (such as AI chatgpt, text to speech, speech recognition, hand/body tracking, tensorflow, 3D, widgets for UI, 2D physics, multiplayer, cloud/p2p, fast-updating cloud variables that can be private and can take text values, game, database, table variables, viewport blocks in motion, new operator blocks, microbit extension for hardware related skills),  and tools like XO ai assistant, AI image generation, block help info popup, step by step execution, console panel for logging, folder of sprites in sprite info pane, advanced costume editor tools. They will allow us to design skills and practice problems to cover all k-8 computational thinking and coding concepts effectively. So read the code to learn exactly what they do when a skill is related to them.

## Step 2: For topic ${topic.code} only, fix these issues

1. Internal Coherence & Granularity
   - Review ALL skills in ${topic.code} across grades K-8
   - Break down overly broad skills into sub-skills (use IDs like ${topic.code}.G4.05.01)
   - Remove duplicates WITHIN this topic
   - Verify logical K-8 progression

2. Skill Quality
   - Use active verbs (Explain, Trace, Predict, Debug) not vague ones (Understand)
   - K-2 skills: specify picture cards or visual scenarios
   - Reference CreatiCode blocks from ../../ScratchCopilot/blockdes8.txt if needed
   - No duplicate or overlapping skills within the topic.
   - Skills do not exceed current topic boundaries considering there are 34 topics total.
   - Skills have depth and range from foundational to advanced within the topic. Remember that as AI can do a lot of basic tasks, programming will become more challenging and complex and large-scale, and skills should reflect that trend.

3. Dependencies (intra-topic ONLY)
   - Fix dependencies WITHIN ${topic.code} only
   - Apply X-2 rule: deps at grades X, X-1, or X-2 only
   - PRESERVE all cross-topic dependencies unchanged

4. Grade-Appropriate Content
   - K-2: picture-based or unplugged
   - Grade 3+: block-based coding

## Rules
- Do NOT delete skills unless absolutely necessary
- Do NOT modify skills from other topics
- PRESERVE all dependencies to OTHER topics
- ONLY modify ${topic.code} skills
- DON'T be afraid of changes. Think outside the box and don't limit yourself by the existing skills design. We need to aim for top quality so every iteration should make significant improvements based on existing skills and go beyond it. There are ALWAYS ways to improve skills. Make bold changes if needed so that the skill map converge towards high quality faster.
- Rethink deeply how IXL structures skills and dependencies for inspiration, and consider how to adapt those ideas to CreatiCode's unique environment. We are using coding and AI as tools for teaching problem-solving and computational thinking, so focus on that. Of course, the skills need to be generic, not tied to CreatiCode only, otherwise teachers or students will feel they are not learning genericly useful skills.

## Step 3: Make the edits to skillsv5/allskills.md

## Step 4: Output a summary of changes made. You must say something.

Use subagents/Task tool to keep context small. For simple standalone tasks for subagents, such as searching in a file, searching in codebase, writing scripts, aggregating text, you **MUST** instruct the subagent to use the sonnet model instead of opus, which is faster and costs less tokens. Proceed now. Again, you MUST make some major bold improvements that significantly increase the overall quality of the skillmap!`;

      let success = false;
      let retryCount = 0;
      const maxRetries = 3000000; 

      while (!success && retryCount < maxRetries) {
        try {
          const result = spawnSync('claude', [
            '--dangerously-skip-permissions',
            '--add-dir', '../../scratch-workspace',
            '--add-dir', '../../creaticode-ws',
            '--add-dir', '../../ScratchCopilot',
            '-p', topicPrompt
          ], { encoding: 'utf8', maxBuffer: 1024 * 1024 * 10 });

          const output = result.stdout || '';
          if (result.error) throw result.error;

          // Check for API errors
          console.log(`\n⚠️  OUTPUT for topic ${topic.code}: ${output}`);
          const outputLower = output.toLowerCase();
          if (outputLower.includes("api error") || outputLower.includes("limit reached")) {
            console.log(`\n⚠️  API rate limit hit for topic ${topic.code}`);
            console.log(`⏰ Waiting 3 minutes before retrying...`);
            await waitWithCountdown(3);
            console.log(`\nRetrying topic ${topic.code} (Attempt ${retryCount + 1}/${maxRetries})...`);
            console.log(`⏰ time: ${new Date().toLocaleString()}...`);
            retryCount++;
          } else {
            success = true;
            console.log(`✅ Completed topic ${topic.code}`);
            // wait one minute
            console.log(`⏳ Waiting 0.1 minute to avoid rate limits...`);
            await waitWithCountdown(0.1);
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

  // PHASE 2: Grade+Topic Processing
  console.log("\n\n===========================================");
  console.log("PHASE 2: Grade+Topic Cross-Topic Dependency Checking");
  console.log(`Started at: ${new Date().toLocaleString()}`);
  console.log("===========================================\n");

  let completedGradeTopicCombos = 0;
  let skippedGradeTopicCombos = 0;

  for (let iteration = 0; iteration < GRADE_ITERATIONS; iteration++) {
    console.log(`\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━`);
    console.log(`  Grade+Topic Phase - Iteration ${iteration + 1}/${GRADE_ITERATIONS}`);
    console.log(`  ${new Date().toLocaleString()}`);
    console.log(`━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n`);

    // Back up allskills.md for this iteration
    const timestamp = Date.now();
    const backupPath = `./skillsv5/allskills_grade_phase_iter${iteration + 1}_${timestamp}.md`;
    execSync(`cp ./skillsv5/allskills.md "${backupPath}"`);
    console.log(`📁 Backed up allskills.md to: ${backupPath.split('/').pop()}\n`);

    const availableGradeTopics = loadAvailableGradeTopics();

    for (let i = 0; i < gradeList.length; i++) {
      const grade = gradeList[i];
      console.log(`\n[${i + 1}/${gradeList.length}] Processing Grade ${grade} across topics`);
      console.log(`${"─".repeat(50)}`);

      for (let j = 0; j < topics.length; j++) {
        const topic = topics[j];
        const comboKey = `${grade}-${topic.code}`;

        if (!availableGradeTopics.has(comboKey)) {
          console.log(`  ⏭️  Skipping Grade ${grade} Topic ${topic.code} (${topic.name}) - no skills found`);
          skippedGradeTopicCombos++;
          continue;
        }

        const comboIndex = (i * topics.length) + j + 1;
        const comboTotal = gradeList.length * topics.length;
        console.log(`\n  [${comboIndex}/${comboTotal}] Processing Grade ${grade} Topic ${topic.code}: ${topic.name}`);
        console.log(`  ${"─".repeat(48)}`);

        // print date time
        console.log(`    ${new Date().toLocaleString()}`);

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

        const gradeTopicPrompt = `AUTONOMOUS MODE: Do NOT ask any questions. Do NOT ask for clarification. Do NOT ask for permission. Proceed immediately with your best judgment. This is a non-interactive batch session.

Your task: Fix cross-topic dependencies for Grade ${grade} skills in Topic ${topic.code} (${topic.name}).

## Step 1: Read these files first
- skillmap_run_context.md for project context
- skillsv5/allskills.md for all current skills
- creaticode.md for CreatiCode platform details, especially new blocks (such as AI chatgpt, text to speech, speech recognition, hand/body tracking, tensorflow, 3D, widgets for UI, 2D physics, multiplayer, cloud/p2p, fast-updating cloud variables that can be private and can take text values, game category, database, table variables, viewport blocks in motion, new operator blocks),  and tools like XO ai assistant, AI image generation, block help info popup, step by step execution, console panel for logging, folder of sprites in sprite info pane, advanced costume editor tools. They will allow us to design skills and practice problems to cover all k-8 computational thinking and coding concepts effectively. So read the code to learn exactly what they do when a skill is related to them.

## Step 2: For Grade ${grade} skills in ${topic.code} only, fix these issues

1. Inter-Topic Dependencies
   - Review ALL Grade ${grade} skills in ${topic.code}
   - ADD missing cross-topic dependencies:
     - Cybersecurity (T31) & DigCit (T32) -> Connected Services (T33) & Multiplayer (T18)
     - Math (T09/T27) -> Data Science (T24-T26)
     - UI (T15) -> App projects in other topics

2. Dependency Validation
   - X-2 rule: Grade ${grade} skills can only depend on ${allowedGrades}
   - Fix violations by finding appropriate scaffolding skills
   - Check for circular dependencies

3. Grade-Level Coherence
   - Ensure foundational skills are available for advanced skills
   - Add dependencies where skills build on each other

## Rules
- NEVER delete any skills
- Only remove deps if genuinely incorrect
- Add dependencies liberally
- Focus ONLY on Grade ${grade} dependencies inside ${topic.code}

## Step 3: Make the edits to skillsv5/allskills.md

## Step 4: Output a summary of dependency changes. You must say something.

Use subagents/Task tool to keep context small. For simple standalone tasks for subagents, such as searching in a file, searching in codebase, writing scripts, aggregating text, you **MUST** instruct the subagent to use the sonnet model instead of opus, which is faster and costs less tokens. Proceed now. Again, you MUST make some major bold improvements that significantly increase the overall quality of the skillmap!`;

        let success = false;
        let retryCount = 0;
        const maxRetries = 30000000;

        while (!success && retryCount < maxRetries) {
          try {
            const result = spawnSync('claude', [
              '--dangerously-skip-permissions',
              '--add-dir', '../../scratch-workspace',
              '--add-dir', '../../creaticode-ws',
              '--add-dir', '../../ScratchCopilot',
              '-p', gradeTopicPrompt
            ], { encoding: 'utf8', maxBuffer: 1024 * 1024 * 10 });

            const output = result.stdout || '';
            if (result.error) throw result.error;

            // Check for API errors
              console.log(`\n⚠️  OUPUT for grade ${grade} topic ${topic.code}: ${output}`);
            const outputLower = output.toLowerCase();
            if (outputLower.includes("api error") || outputLower.includes("limit reached")) {
              console.log(`\n⚠️  API rate limit hit for grade ${grade} topic ${topic.code}`);
              console.log(`⏰ Waiting 3 minutes before retrying...`);
              await waitWithCountdown(3);
              console.log(`⏰ retry time: ${new Date().toLocaleString()}...`);
              retryCount++;
            } else {
              success = true;
              completedGradeTopicCombos++;
              console.log(`✅ Completed grade ${grade} topic ${topic.code}`);
            }
          } catch (error) {
            console.error(`\n❌ Error processing grade ${grade} topic ${topic.code}:`, error.message.substring(0, 100));
            const errorStr = error.toString().toLowerCase();
            if (1 || errorStr.includes("api error") || errorStr.includes("usage limit")) {
              console.log(`⏰ API limit - waiting 3 minutes...`);
              await waitWithCountdown(3);
              retryCount++;
            } else {
              console.error(`⚠️  Skipping grade ${grade} topic ${topic.code} after error`);
              break;
            }
          }
        }

        if (!success) {
          console.log(`⚠️  Failed to process grade ${grade} topic ${topic.code} after ${maxRetries} retries`);
        }
      }
    }

    console.log(`\n✅ Completed Grade+Topic Phase Iteration ${iteration + 1}/${GRADE_ITERATIONS}`);
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
  const totalPassesCompleted = topics.length * TOPIC_ITERATIONS + completedGradeTopicCombos;
  console.log(`- Phase 1: Processed ${topics.length} topics × ${TOPIC_ITERATIONS} iterations`);
  console.log(`- Phase 2: Processed ${completedGradeTopicCombos} grade-topic combos across ${GRADE_ITERATIONS} iteration(s); skipped ${skippedGradeTopicCombos} empty combos`);
  console.log(`- Total: ${totalPassesCompleted} focused optimization passes executed`);
  console.log(`\nCheck skillsv5/allskills.md for the optimized skill map.\n`);
}

// Run the script
runAllScripts().catch(error => {
  console.error("\n\n❌ Fatal error:", error);
  process.exit(1);
});
