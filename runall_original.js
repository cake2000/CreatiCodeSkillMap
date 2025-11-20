const { execSync } = require("child_process");

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function runAllScripts() {
  const gradeList = ["K", "1", "2", "3", "4", "5", "6", "7", "8"];

  for (let j = 0; j < 100; j++) {
    console.log(`\n\n=== Run iteration j = ${j} ===\n\n`);

    // back up allskills.md
    execSync(
      `cp ./skillsv4/allskills.md ./skillsv4/allskills_backup_${Date.now()}.md`
    );
    console.log("✓ Backed up allskills.md\n");

    for (let i = 0; i < gradeList.length; i++) {
      const grade = gradeList[i];
      // if (grade == '2') break;
      const prompt = `## Introduction
we are aiming for "IXL for coding based on creaticode", and we need top quality result. No one has done this before in the world. It will be a unique contribution that will benefit all kids learning to code to have a systematic map of skills laid out to go from newbies to master programmers and engineers. CSTA has a standard but it is too vague and also missing important skill categories like AI and 3D and project development. This skill map will become the new golden standard for all coding platforms/educators to rely on.

Read 00-START-HERE.md and spec_v2_updated.md to understand the whole project, and read the key referneces like csta standard draft, and ai priorities, and creaticode introduction in the root folder. ignore ACSL since it is too theoretic!

latest version of skills are in "skillsv4" folder (ignore the other skills folders)

now, we need to enhance the quality of the skills for this version. read the file skillsv4/allskills.md, which contains all skills. The ID tells you the topic and grade level "G1" means grade 1.

## your task

review allskills.md to identify any issue with the skills or dependencies, such as out of order issue (a grade 3 skill is depending on a grade 4 skill), or a dependency is missing, or there is a better dependency.

each skill should be clear and specific, similar to IXL skills, which is very managable and students can even self-study, and not too broad. if a skill is too broad or complex, break it down into multiple skills and adjust IDs and dependencies accordingly. The skills should also not duplicate each other or overlap significantly, both within a topic and across topics. If you find such cases, remove the skill or rephrase them. If you remove skills, don't need to change ID of other skills. We will sort out the IDs again at the end.

When you break down a skill into multiple skills, you should assign the new skills an ID that does not conflict with existing IDs. For example, if a skill is "T01.G4.05" and you break it into 3, then call them "T01.G4.05", "T01.G4.05.01", "T01.G4.05.02", and update dependencies accordingly.

also, to keep dependencies simple, let's add additional rule that for a skill at grade X, the dependencies should be at same grade or 1 grade or 2 grade lower, that is grade X, X - 1 or X -2. It should not be lower than X -2. For example, a grade 4 skill can depend on grade 4 or grade 3 or grade 2 skills, but not grade 1 skills. Also avoid circular dependencies. Also avoid transitive dependencies (if A depends on B, and B depends on C, then A should not depend on C directly). Also, no need to add earlier skills in the same topic in the same grade as dependencies since they are assumed to be learned earlier in the same grade. So a skill's dependency should either come from earlier grades in same topic, or from other topics in same or earlier grades.

if you need to modify skills, such as adding a new skill to fill a gap, or change the grade level of a skill, make sure you edit other files that may depend on that skill changed, such as the skills in the same topic, or all skills depending on that skill.

Some skills rely on knowledge about creaticode, and you should read creaticode introduction and explore creaticode repos directly to understand its key features and capabilities. They are located at
* client side: ../../scratch-workspace
* server side: ../../creaticode-ws
* AI copilot and image generation tool: ../../ScratchCopilot

use subagents/task to keep main context clean and small.

Since this is going to be complicated, focus on skills **grade ${grade} only**. Do your best to identify and fix all issues and then update the skillsv4/allskills.md file accordingly.

You should automatically fix all high and medium priority issues you can find for grade ${grade} skills without asking for persmission. Ignore low priority issues for now. Use your best judgment since this is an non-interactive session. For output, summarize the key changes you made to skillsv4/allskills.md in a concise way.
`;

      // run claude -p with this prompt
      let success = false;
      while (!success) {
        try {
          console.log(`\n\nRunning script for grade ${grade}...\n\n`);
          const output = execSync(
            `claude --add-dir ../../scratch-workspace --add-dir ../../creaticode-ws --add-dir ../../ScratchCopilot -p "${prompt.replace(/"/g, '\\"')}"`,
            { encoding: "utf8" }
          );

          // Check for API errors or usage limits (case-insensitive)
          const outputLower = output.toLowerCase();
          if (
            outputLower.includes("api error") ||
            outputLower.includes("usage limit")
          ) {
            console.log(
              `\n⚠️  Detected API Error or Usage Limit for grade ${grade}`
            );
            console.log("⏰ Waiting 15 minutes before retrying...\n");

            // Wait 15 minutes (900000 milliseconds)
            const waitTime = 15 * 60 * 1000;
            const startTime = Date.now();
            const endTime = startTime + waitTime;

            // Show countdown
            const interval = setInterval(() => {
              const remaining = Math.ceil((endTime - Date.now()) / 1000 / 60);
              if (remaining > 0) {
                process.stdout.write(
                  `\r⏰ Time remaining: ${remaining} minutes...`
                );
              }
            }, 10000); // Update every 10 seconds

            await sleep(waitTime);

            clearInterval(interval);
            console.log("\n✓ Wait complete. Retrying...\n");
          } else {
            // Success - move to next grade
            success = true;
            console.log(`✓ Completed grade ${grade}\n`);
          }
        } catch (error) {
          console.error(
            `Error running script for grade ${grade}:`,
            error.message
          );

          // Check if error output contains API Error or Usage Limit
          const errorStr = error.toString().toLowerCase();
          if (
            errorStr.includes("api error") ||
            errorStr.includes("usage limit")
          ) {
            console.log(
              `\n⚠️  Detected API Error or Usage Limit in error for grade ${grade}`
            );
            console.log("⏰ Waiting 15 minutes before retrying...\n");

            // Wait 15 minutes
            const waitTime = 15 * 60 * 1000;
            await sleep(waitTime);

            console.log("\n✓ Wait complete. Retrying...\n");
          } else {
            // Other error - skip to next grade
            console.error(`Skipping grade ${grade} due to error\n`);
            success = true;
          }
        }
      }
    }
  }
}

runAllScripts();
