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
  const TOPIC_ITERATIONS = 1; // 3 iterations as requested
  const GRADE_ITERATIONS = 3; // 3 iterations for grade-level checking

  console.log("===========================================");
  console.log("Starting Two-Phase Optimization Strategy");
  console.log("===========================================\n");
  console.log(`Phase 1: ${topics.length} topics × ${TOPIC_ITERATIONS} iterations = ${topics.length * TOPIC_ITERATIONS} focused topic passes`);
  console.log(`Phase 2: ${gradeList.length} grades × ${GRADE_ITERATIONS} iterations = ${gradeList.length * GRADE_ITERATIONS} focused grade passes`);
  console.log(`Total: ${topics.length * TOPIC_ITERATIONS + gradeList.length * GRADE_ITERATIONS} focused passes (vs. 900 unfocused)\n`);

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
    const backupPath = `./skillsv4/allskills_topic_phase_iter${iteration + 1}_${timestamp}.md`;
    execSync(`cp ./skillsv4/allskills.md "${backupPath}"`);
    console.log(`📁 Backed up allskills.md to: ${backupPath.split('/').pop()}\n`);

    for (let i = 0; i < topics.length; i++) {
      if ( iteration == 0 && i < 25) continue;
      const topic = topics[i];
      console.log(`\n[${i + 1}/${topics.length}] Processing Topic ${topic.code}: ${topic.name}`);
      console.log(`${"─".repeat(50)}`);

      console.log(`  ${new Date().toLocaleString()}`);

      const topicPrompt = `## Introduction
We are aiming for "IXL for coding based on creaticode", and we need top quality result. This skill map will become the new golden standard for all coding platforms/educators to rely on. Our goal is not only build solid foundations in coding concepts but also empower students to create amazing projects using CreatiCode's unique features, and along the way develop problem solving skills that will serve them for life.

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
   - Feel free to make MAJOR revisions to skill descriptions as needed or add/update skills
   - Break down any skills that are too broad or complex
   - Skills should be designed to help students gain problem solving skills beyond just learning how to use CreatiCode features or basic coding concepts
   - The list of skills has to be comprehensive and scaffolded. You are encouraged to add missing skills to ensure proper scaffolding and knowledge coverage within the topic.
   - Skill description should be actionable, relatable to the target age group, easy to understand, and implementable
   - If the skill is related how to use a CreatiCode feature, such as how a block or tool works, ensure it accurately reflects the feature's capabilities. You absolutely must check the creaticode repos to verify this by reviewing ALL blocks offered in the related categories and consider how they should be used to teach the skill. For example, for 2D physics or 3D skills, you have to look into what blocks are offered and how they work to design meaningful skills around them since these skills are totally depending on the specific features of the platform. For 3D skills, you would have to look into how to initialize a 3D scene, control the camera, adding shapes/models/avatars, moving/rotating, handle collision/physics. For 2D physics, we have to enable the 2D physics engine first and then define the physics body for sprites, etc. Similar for widget category for app development, which are essential when developping AI apps like adding buttons/labels/textbox/chat window and handle user interactions. You also hav to check out other categories like AI (how to call ChatGPT/LLM, hand/body gesture tracking, speech-to-text and text-to-speech, etc), multiplayer, cloud, etc, when you work with related topics. You can search in this file to get all blocks in any category: /media/binyu/USB2/ScratchCopilot/blockdes8.txt. For example, search "Category:" to find all categories in that file or find all blocks within one category by searching "Category: <category name>". The current skills may not fully reflect the actual features of CreatiCode, so you have to improve them based on what the platform actually offers, and maybe some big changes are needed.
   - Ensure skill descriptions are concrete and assessable
   - Merge truly redundant skills within the topic (but be conservative)
   - When breaking down skills, use sub-IDs like ${topic.code}.G4.05.01, ${topic.code}.G4.05.02

3. **Intra-Topic Dependencies ONLY**
   - Fix dependencies WITHIN topic ${topic.code} only
   - Ensure no skill depends on a later skill in the same topic
   - Remove unnecessary same-grade dependencies (earlier skills in same topic/grade are assumed)
   - Apply the X-2 rule: dependencies should be at grades X, X-1, or X-2 only. For example, for a grade 4 skill, dependencies can only be at grades 4, 3, or 2.
   - **CRITICAL: PRESERVE all dependencies to OTHER topics (T## where ## ≠ ${topic.code.slice(1)})**

4. **Grade-Appropriate Content**
   - K-2 skills should be picture-based or unplugged
   - Grade 3+ skills should involve block-based coding
   - Ensure complexity increases appropriately with grade level

CRITICAL RULES - NEVER VIOLATE THESE:
- **NEVER delete any skills** - only improve/clarify their descriptions
- **NEVER remove dependencies to skills from OTHER topics** (preserve all cross-topic dependencies)
- **NEVER modify skills from other topics** - focus ONLY on ${topic.code}
- Only remove a dependency if it's genuinely incorrect AND within topic ${topic.code}
- When you identify inter-topic dependency issues, ignore them

IMPORTANT CONSTRAINTS:
- ONLY modify skills in topic ${topic.code}
- Do NOT change inter-topic dependencies (those will be fixed in Phase 2)
- Focus on making this topic internally consistent and high quality
- Preserve the existing skill structure unless there's a compelling reason to change it

Additional context about CreatiCode features is available at:
* client side: ../../scratch-workspace
* server side: ../../creaticode-ws
* AI copilot: ../../ScratchCopilot

Use subagents/task to keep main context clean and small. For example, use Task with subagent_type=general-purpose to analyze and fix issues.

## Special Note On this run

I have reviewed the skills, and one BIG problem is the skills are still too big for some categories, such as 3D worlds. For one example, there is one skill T18.G3.04 that covers adding ALL shapes like boxes, spheres, etc. Although each shape is already a big skill by itself since many parameters are there for each block for customizing it. So for cases like this, that skill needs to be broken down into many smaller skills. And you can use additional skill IDs like T18.G3.04.01, T18.G3.04.02, etc. to define each smaller skill. Please make sure all skills are manageable and implementable by students. Do this for every topic where applicable and every skill. In general, when introducing new blocks/features, make sure each skill is focused on one SINGLE block/feature ONLY, so students can learn to use it well. If a skill is too big, break it down into smaller skills.

YOU ARE PERMITTED TO MAKE MAJOR CHANGES, especially breaking down overly broad skills into smaller, manageable ones.

Now, automatically fix all high and medium priority issues within topic ${topic.code}. For output, summarize the key changes you made to topic ${topic.code} skills in skillsv4/allskills.md.`;

      let success = false;
      let retryCount = 0;
      const maxRetries = 30000;

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
            console.log(`⏰ Waiting 3 minutes before retrying...`);
            await waitWithCountdown(3);
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
            retryCount++;
          } else {
            // console.error(`⚠️  Skipping topic ${topic.code} after error`);
            // break;
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
    const backupPath = `./skillsv4/allskills_grade_phase_iter${iteration + 1}_${timestamp}.md`;
    execSync(`cp ./skillsv4/allskills.md "${backupPath}"`);
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
We are aiming for "IXL for coding based on creaticode", and we need top quality result. This skill map will become the new golden standard for all coding platforms/educators to rely on.

Read 00-START-HERE.md and spec_v2_updated.md to understand the whole project, and read the key references like CSTA standard draft, AI priorities, and creaticode introduction in the root folder.

Latest version of skills are in "skillsv4" folder. Read the file skillsv4/allskills.md, which contains all skills.

## Phase 2: Grade-Level Cross-Topic Dependency Checking for Grade ${grade}

You are in PHASE 2 of a two-phase optimization process. Phase 1 has already optimized individual topics. Now you are focusing on all skills in grade ${grade} to ensure proper cross-topic dependencies and grade-level coherence.

### Your Specific Tasks for Grade ${grade}:

1. **Inter-Topic Dependencies**
   - Review ALL skills at grade ${grade} across all 36 topics
   - Check all of other topics that might be related to each skill's own topic
   - ADD missing cross-topic dependencies where needed
   - Ensure skills from different topics that relate to each other have proper dependencies
   - Example: A game skill might need to depend on loops, variables, and graphics skills

2. **Dependency Validation**
   - Enforce the X-2 rule strictly: Grade ${grade} skills can only depend on ${allowedGrades}.
   - Fix dependencies that violate this rule by finding appropriate scaffolding skills
   - Check for circular dependencies across topics
   - Remove transitive dependencies (if A→B and B→C, remove A→C) ONLY if truly redundant

3. **Grade-Level Coherence**
   - Ensure all grade ${grade} skills work together as a cohesive curriculum
   - Ensure skills from different topics complement each other well and there is no significant overlap between skills from different topics. If such cases are found, adjust skills or remove them, or add dependencies to clarify learning pathways.
   - Check that foundational skills are available for more advanced skills
   - ${grade !== 'K' ? `Verify that grade ${grade === '1' ? 'K' : parseInt(grade) - 1} provides adequate preparation` : 'Ensure kindergarten skills are truly introductory'}
   - Add dependencies where skills clearly build on each other

4. **Scaffolding Verification**
   - Ensure critical gateway skills have proper dependencies
   - Check that complex skills have sufficient prerequisite skills
   - Verify learning pathways make sense across topics at this grade level
   - When needed skills are missing from allowed grades, find appropriate scaffolding

CRITICAL RULES - NEVER VIOLATE THESE:
- **NEVER delete any skills** - Phase 1 already handled skill quality
- **Only remove a dependency if it's genuinely incorrect or truly redundant**
- **Be conservative** - when in doubt, keep the dependency
- **Add dependencies liberally** - better to over-specify than under-specify prerequisites
- **Do not update skill ID** when removing a skill to avoid invalidating existing dependencies
- **Preserve all valid dependencies** even if they seem numerous

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
      const maxRetries = 30000000;

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
          if (errorStr.includes("api error") || errorStr.includes("usage limit")) {
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
  console.log(`\nCheck skillsv4/allskills.md for the optimized skill map.\n`);
}

// Run the script
runAllScripts().catch(error => {
  console.error("\n\n❌ Fatal error:", error);
  process.exit(1);
});