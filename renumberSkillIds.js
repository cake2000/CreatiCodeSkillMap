const fs = require("fs");
const path = require("path");

// This script renumbers every skill ID sequentially within each topic+grade pair.
// - New IDs start at .01 (no .00) and increment in file order.
// - Sub-skill IDs like T01.G4.02.01 are flattened and promoted to regular skills.
// - All references in the file (Dependencies and cross-topic mentions) are updated.
// - Output is written to skillsv6/allskills.md (input remains untouched).

const inputPath = path.join(__dirname, "skillsv5", "allskills.md");
const outputDir = path.join(__dirname, "skillsv6");
const outputPath = path.join(outputDir, "allskills.md");

const idRegex =
  /^ID:\s*(T\d{2})\.(G[K1-8])\.([0-9]{2}(?:\.[0-9]{2})*)/gm;
const anyIdRegex = /T\d{2}\.G[K1-8]\.[0-9]{2}(?:\.[0-9]{2})*/g;

const escapeRegExp = (str) =>
  str.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");

function buildMapping(content) {
  const skills = [];
  let match;
  while ((match = idRegex.exec(content)) !== null) {
    const topic = match[1];
    const grade = match[2];
    const oldId = `${topic}.${grade}.${match[3]}`;
    skills.push({ index: match.index, topic, grade, oldId });
  }

  if (skills.length === 0) {
    throw new Error("No skill IDs found in input file.");
  }

  const counters = new Map(); // key: topic.grade -> count
  const mapping = new Map(); // oldId -> newId
  const prefixMap = new Map(); // prefixId -> first child oldId
  const firstSkillMap = new Map(); // topic.grade -> first oldId encountered
  const collisions = [];

  for (const skill of skills) {
    const key = `${skill.topic}.${skill.grade}`;
    const next = (counters.get(key) || 0) + 1;
    if (next > 99) {
      throw new Error(
        `More than 99 skills found for ${key}; renumbering would overflow two digits.`
      );
    }
    counters.set(key, next);
    const newId = `${skill.topic}.${skill.grade}.${String(next).padStart(
      2,
      "0"
    )}`;
    if (mapping.has(skill.oldId)) {
      // Duplicate ID lines in source
      collisions.push(skill.oldId);
    }
    mapping.set(skill.oldId, newId);

    if (!firstSkillMap.has(key)) {
      firstSkillMap.set(key, skill.oldId);
    }

    // Track prefixes for sub-skills so base references can map to first child.
    const parts = skill.oldId.split(".");
    // parts: [topic, grade, seg1, seg2, ...]
    while (parts.length > 3) {
      parts.pop();
      const prefixId = parts.join(".");
      if (!prefixMap.has(prefixId)) {
        prefixMap.set(prefixId, skill.oldId);
      }
    }
  }

  if (collisions.length > 0) {
    console.warn(
      `Warning: duplicate ID lines detected for ${collisions.length} IDs.`
    );
  }

  return {
    mapping,
    prefixMap,
    firstSkillMap,
    counters,
    totalSkills: skills.length,
  };
}

function applyMapping(content, mapping, prefixMap, firstSkillMap) {
  const missing = new Set();
  const replaced = content.replace(anyIdRegex, (match) => {
    if (mapping.has(match)) {
      return mapping.get(match);
    }
    // Fallback: strip trailing segments until a mapped ID is found.
    let candidate = match;
    while (candidate.lastIndexOf(".") > -1) {
      candidate = candidate.slice(0, candidate.lastIndexOf("."));
      if (mapping.has(candidate)) {
        return mapping.get(candidate);
      }
    }
    if (prefixMap.has(match)) {
      const childOldId = prefixMap.get(match);
      return mapping.get(childOldId) || match;
    }
    const baseKey = match.split(".").slice(0, 2).join(".");
    if (firstSkillMap.has(baseKey)) {
      const firstOld = firstSkillMap.get(baseKey);
      const fallback = mapping.get(firstOld);
      if (fallback) return fallback;
    }
    missing.add(match);
    return match;
  });

  if (missing.size > 0) {
    console.warn(
      `Warning: ${missing.size} referenced ID(s) were not mapped (no matching skill definition):`
    );
    for (const id of missing) {
      console.warn(`  - ${id}`);
    }
  }

  return replaced;
}

function main() {
  if (!fs.existsSync(inputPath)) {
    throw new Error(`Input not found: ${inputPath}`);
  }
  const content = fs.readFileSync(inputPath, "utf8");
  const { mapping, prefixMap, firstSkillMap, counters, totalSkills } =
    buildMapping(content);
  const updated = applyMapping(content, mapping, prefixMap, firstSkillMap);

  fs.mkdirSync(outputDir, { recursive: true });
  fs.writeFileSync(outputPath, updated, "utf8");

  console.log("Renumbering complete.");
  console.log(`Total skills processed: ${totalSkills}`);
  console.log(`Output written to: ${outputPath}`);
  console.log("Counts per topic.grade (post-renumber):");
  for (const [key, count] of [...counters.entries()].sort()) {
    console.log(`- ${key}: ${count.toString().padStart(2, "0")} skill(s)`);
  }
}

main();
