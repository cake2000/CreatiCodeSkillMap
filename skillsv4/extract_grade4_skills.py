#!/usr/bin/env python3
"""
Extract all Grade 4 skills from allskills.md
"""

import re
import json
from collections import defaultdict

def parse_skills(filepath):
    """Parse the markdown file and extract Grade 4 skills"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by skill entries (ID: pattern)
    skill_blocks = re.split(r'\n(?=ID: T\d+\.G4\.)', content)

    skills = []
    topic_distribution = defaultdict(int)

    for block in skill_blocks:
        # Check if this is a Grade 4 skill
        id_match = re.search(r'^ID: (T\d+\.G4\.\d+(?:\.\d+)?)', block, re.MULTILINE)
        if not id_match:
            continue

        skill_id = id_match.group(1)

        # Extract topic number
        topic_num = skill_id.split('.')[0]
        topic_distribution[topic_num] += 1

        # Extract topic line
        topic_match = re.search(r'^Topic: (.+)$', block, re.MULTILINE)
        topic = topic_match.group(1).strip() if topic_match else ""

        # Extract skill title
        skill_match = re.search(r'^Skill: (.+)$', block, re.MULTILINE)
        skill_title = skill_match.group(1).strip() if skill_match else ""

        # Extract description
        desc_match = re.search(r'^Description: (.+?)(?=\n\n|\nDependencies:|\Z)', block, re.MULTILINE | re.DOTALL)
        description = desc_match.group(1).strip() if desc_match else ""

        # Extract dependencies
        dependencies = []
        deps_section = re.search(r'Dependencies:\s*\n((?:\* .+\n?)+)', block, re.MULTILINE)
        if deps_section:
            dep_lines = deps_section.group(1).strip().split('\n')
            for dep_line in dep_lines:
                dep_match = re.match(r'\* (T\d+\.[A-Z]\d+\.\d+(?:\.\d+)?): (.+)', dep_line.strip())
                if dep_match:
                    dependencies.append({
                        "id": dep_match.group(1),
                        "title": dep_match.group(2).strip()
                    })

        skills.append({
            "id": skill_id,
            "topic": topic,
            "skill": skill_title,
            "description": description,
            "dependencies": dependencies
        })

    return skills, dict(topic_distribution)

def main():
    input_file = "/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md"
    output_file = "/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/grade4_skills_extracted.json"

    print("Extracting Grade 4 skills...")
    skills, topic_dist = parse_skills(input_file)

    # Save to JSON
    output_data = {
        "total_skills": len(skills),
        "topic_distribution": topic_dist,
        "skills": skills
    }

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    print(f"\nTotal Grade 4 skills found: {len(skills)}")
    print(f"\nDistribution across topics:")
    for topic in sorted(topic_dist.keys()):
        print(f"  {topic}: {topic_dist[topic]} skills")

    print(f"\nSample of 5 skills with their dependencies:")
    for i, skill in enumerate(skills[:5]):
        print(f"\n{i+1}. {skill['id']}: {skill['skill']}")
        print(f"   Description: {skill['description'][:100]}...")
        if skill['dependencies']:
            print(f"   Dependencies ({len(skill['dependencies'])}):")
            for dep in skill['dependencies']:
                print(f"     - {dep['id']}: {dep['title']}")
        else:
            print(f"   Dependencies: None")

    print(f"\n\nResults saved to: {output_file}")

if __name__ == "__main__":
    main()
