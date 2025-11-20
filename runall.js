const {execSync} = require('child_process');

function runAllScripts() {
  const gradeList = ['K', '1', '2', '3', '4', '5', '6', '7', '8'];

  for (const grade of gradeList) {
    // if (grade == '2') break;
    const prompt = `## Introduction
we are aiming for "IXL for coding based on creaticode", and we need top quality result. No one has done this before in the world. It will be a unique contribution that will benefit all kids learning to code to have a systematic map of skills laid out to go from newbies to master programmers and engineers. CSTA has a standard but it is too vague and also missing important skill categories like AI and 3D and project development. This skill map will become the new golden standard for all coding platforms/educators to rely on.

Read 00-START-HERE.md and spec_v2_updated.md to understand the whole project, and read the key referneces like csta standard draft, and ai priorities, and creaticode introduction in the root folder. ignore ACSL since it is too theoretic!

latest version of skills are in "skillsv4" folder (ignore the other skills folders)

now, we need to enhance the quality of the skills for this version. read the file skillsv4/allskills.md, which contains all skills. The ID tells you the topic and grade level "G1" means grade 1.

## your task

review allskills.md to identify any issue with the skills or dependencies, such as out of order issue (a grade 3 skill is depending on a grade 4 skill), or a dependency is missing, or there is a better dependency.

also, to keep dependencies simple, let's add additional rule that for a skill at grade X, the dependencies should be at same grade or 1 grade or 2 grade lower, that is grade X, X - 1 or X -2. It should not be X or lower than X -2. For example, a grade 4 skill can depend on grade 4 or grade 3 or grade 2 skills, but not grade 1 skills. Also avoid circular dependencies. Also avoid transitive dependencies (if A depends on B, and B depends on C, then A should not depend on C directly). Also, no need to add earlier skills in the same topic in the same grade as dependencies since they are assumed to be learned earlier in the same grade. So a skill's dependency should either come from earlier grades in same topic, or from other topics in same or earlier grades.

also, each skill should be clear and specific, and not too broad. if a skill is too broad, break it down into multiple skills and adjust IDs and dependencies accordingly.

if you need to modify skills, such as adding a new skill to fill a gap, or change the grade level of a skill, make sure you edit other files that may depend on that skill changed, such as the skills in the same topic, or all skills depending on that skill.

use subagents/task to keep main context clean and small.

Since this is going to be complicated, focus on skills **grade ${grade} only**. Do your best to identify and fix all issues and then update the skillsv4/allskills.md file accordingly.

You should automatically fix all high and medium priority issues you can find for grade ${grade} skills without asking for persmission. Ignore low priority issues for now. Use your best judgment since this is an non-interactive session.
`;

    // run claude -p with this prompt
    try {
      console.log(`\n\nRunning script for grade ${grade}...\n\n`);
      execSync(`claude -p "${prompt.replace(/"/g, '\\"')}"`, {stdio: 'inherit'});
    } catch (error) {
      console.error(`Error running script for grade ${grade}:`, error);
    }
  }
  
}

runAllScripts();