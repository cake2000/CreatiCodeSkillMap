const { execSync, spawnSync } = require("child_process");
const fs = require("fs");

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function waitWithCountdown(minutes) {
  const totalSeconds = Math.ceil(minutes * 60);
  for (let remaining = totalSeconds; remaining > 0; remaining--) {
    const mins = Math.floor(remaining / 60);
    const secs = remaining % 60;
    process.stdout.write(
      `\rWaiting ${mins}:${secs.toString().padStart(2, "0")} before retry...`
    );
    await sleep(1000);
  }
  process.stdout.write("\r                                   \r");
}

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
  { code: "T34", name: "Computing History" },
];

const loadAvailableTopics = () => {
  const content = fs.readFileSync("./skillsv5/allskills.md", "utf8");
  const set = new Set();
  const regex = /ID:\s*(T\d{2})\.G[K1-8]\.\d{2}/g;
  let match;
  while ((match = regex.exec(content)) !== null) {
    set.add(match[1]);
  }
  return set;
};

const buildPrompt = (topic) => {
  return `AUTONOMOUS MODE: Do NOT ask questions or seek confirmation. This is a batch run. Use your best judgment and complete all steps without pausing.

Goal: For topic ${topic.code} (${topic.name}), divide every skill into IXL-style strands and renumber IDs so strands and ordering are explicit.

Read first:
- skillmap_run_context.md for project context
- skillsv5/allskills.md (source of truth)
- creaticode.md for platform capabilities, blocks, and constraints

Work inside skillsv5/allskills.md for ${topic.code} ONLY (all grades K-8):

1) Create strands (like IXL progressions)
- Identify the full set of ${topic.code} skills across all grades.
- Define 3-6 strands that cover the whole progression; name them with short, clear labels and a one-line description of what each strand teaches.
- Order strands from most foundational to most advanced and reuse the same strand codes across every grade.
- Assign every ${topic.code} skill to exactly one strand; no misc bucket.
- Add a Strand line immediately under the Topic line for each skill: "Strand: S02 - <strand name>" (two-digit strand codes S01, S02, ...).
- Re-order skills if needed so each strand reads coherently from K through 8; keep K-2 unplugged/picture-based and G3+ block coding.

2) Renumber IDs to encode strand and sequence
- New ID format: ${topic.code}.S<two-digit strand>.G<grade>.NN (two-digit skill order). Example: ${topic.code}.S02.G4.03.
- Use the strand order to assign S01, S02, etc. Restart NN numbering at 01 for each grade within a strand, ordered by progression and dependency flow.
- Update every reference to ${topic.code} IDs, including all Dependencies lists and any cross-topic references pointing into ${topic.code}, so nothing points to an old ID.
- Keep dependencies to other topics intact; inside ${topic.code}, ensure dependencies obey the X-2 grade rule and follow the new ordering.

3) Editing rules
- Do NOT delete skills. Only adjust Skill/Description text if needed to align with the strand definition or to clarify progression.
- Do NOT touch topics other than ${topic.code}. Preserve cross-topic dependencies unless an internal ID changed.
- Maintain the existing markdown spacing and bullet style (blank lines between skills; Dependencies as bullet list).

4) Output
- Write changes directly to skillsv5/allskills.md.
- End with a concise summary: strand definitions, counts per strand, and confirmation that IDs and dependencies were updated to the new scheme.

Proceed now.`;
};

async function runAddStrands() {
  const startTime = new Date();
  console.log("=== Strand + ID renumbering run ===");
  console.log(`Started at ${startTime.toLocaleString()}`);

  const backupPath = `./skillsv5/allskills_strands_backup_${Date.now()}.md`;
  execSync(`cp ./skillsv5/allskills.md "${backupPath}"`);
  console.log(`Backed up skillsv5/allskills.md -> ${backupPath}`);

  const availableTopics = loadAvailableTopics();
  const topicsWithSkills = topics.filter((t) => availableTopics.has(t.code));
  if (topicsWithSkills.length === 0) {
    console.log("No topics found in skillsv5/allskills.md. Exiting.");
    return;
  }

  console.log(
    `Processing ${topicsWithSkills.length} topic(s) that have skills defined.`
  );

  const maxRetries = 8;
  const claudeArgsBase = [
    "--dangerously-skip-permissions",
    "--add-dir",
    "../../scratch-workspace",
    "--add-dir",
    "../../creaticode-ws",
    "--add-dir",
    "../../ScratchCopilot",
  ];

  for (let i = 0; i < topicsWithSkills.length; i++) {
    const topic = topicsWithSkills[i];
    console.log(
      `\n[${i + 1}/${topicsWithSkills.length}] ${topic.code} - ${
        topic.name
      }`
    );

    const prompt = buildPrompt(topic);
    let success = false;
    let attempt = 0;

    while (!success && attempt < maxRetries) {
      try {
        const result = spawnSync(
          "claude",
          [...claudeArgsBase, "-p", prompt],
          { encoding: "utf8", maxBuffer: 1024 * 1024 * 20 }
        );

        const output = (result.stdout || "").toString();
        const lower = output.toLowerCase();

        if (result.error) {
          throw result.error;
        }

        if (result.status !== 0) {
          throw new Error(
            `claude exited with status ${result.status} ${result.stderr || ""}`
          );
        }

        if (
          lower.includes("api error") ||
          lower.includes("limit reached") ||
          lower.includes("overloaded") ||
          lower.includes("rate limit")
        ) {
          attempt += 1;
          console.log(
            `API limit detected for ${topic.code}. Waiting 3 minutes before retry (${attempt}/${maxRetries})...`
          );
          await waitWithCountdown(3);
          continue;
        }

        success = true;
        console.log(`Completed ${topic.code} successfully.`);
      } catch (err) {
        attempt += 1;
        console.error(
          `Error on ${topic.code} attempt ${attempt}/${maxRetries}: ${err.message}`
        );
        if (attempt < maxRetries) {
          console.log("Waiting 3 minutes before retry...");
          await waitWithCountdown(3);
        }
      }
    }

    if (!success) {
      console.log(
        `Skipped ${topic.code} after ${maxRetries} failed attempt(s).`
      );
    }
  }

  const endTime = new Date();
  console.log("\n=== Strand + ID renumbering complete ===");
  console.log(`Finished at ${endTime.toLocaleString()}`);
  const elapsed = Math.round((endTime - startTime) / 1000);
  const hours = Math.floor(elapsed / 3600);
  const minutes = Math.floor((elapsed % 3600) / 60);
  const seconds = elapsed % 60;
  console.log(`Elapsed: ${hours}h ${minutes}m ${seconds}s`);
}

runAddStrands().catch((err) => {
  console.error("Fatal error:", err);
  process.exit(1);
});
