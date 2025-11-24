#!/usr/bin/env python3
"""
Apply cross-topic dependency fixes using safer string replacement approach.
"""

import re

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def apply_dependency(content, skill_id, new_dep_id, new_dep_title):
    """
    Add a dependency to a skill by finding its Dependencies section
    and appending the new dependency.
    """
    # Find the skill's Dependencies section
    pattern = rf'(ID: {re.escape(skill_id)}.*?Dependencies:\n)((\*[^\n]+\n)*)'

    def replacement(match):
        header = match.group(1)
        existing_deps = match.group(2)

        # Check if dependency already exists
        if new_dep_id in existing_deps:
            print(f"  Dependency {new_dep_id} already exists for {skill_id}")
            return match.group(0)

        # Add new dependency
        new_dep_line = f"* {new_dep_id}: {new_dep_title}\n"
        return header + existing_deps + new_dep_line

    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    if new_content == content:
        print(f"  WARNING: Could not find or modify dependencies for {skill_id}")
        return content, False

    return new_content, True

def main():
    print("Reading allskills.md...")
    content = read_file('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md')

    # Define the dependencies to add
    # Format: (skill_id, new_dep_id, new_dep_title, reason)
    dependencies_to_add = [
        ('T01.GK.02', 'T01.GK.01', 'Put pictures in order for getting ready for bed',
         'Putting 4 pictures in order builds on basic 3-picture sequencing'),

        ('T01.GK.03', 'T01.GK.01', 'Put pictures in order for getting ready for bed',
         'Finding first/last positions requires sequencing foundation'),

        ('T20.GK.04', 'T01.GK.01', 'Put pictures in order for getting ready for bed',
         'Fixing mixed-up plan requires understanding correct order'),

        ('T24.GK.03', 'T01.GK.01', 'Put pictures in order for getting ready for bed',
         'Giving step-by-step instructions requires sequencing'),

        ('T20.GK.02', 'T04.GK.01', 'Identify a simple repeating pattern',
         'Describing patterns requires recognizing them'),
    ]

    successful = []
    failed = []

    print("\nApplying dependencies...")
    for skill_id, new_dep_id, new_dep_title, reason in dependencies_to_add:
        print(f"\n{skill_id} -> {new_dep_id}")
        print(f"  Reason: {reason}")

        new_content, success = apply_dependency(content, skill_id, new_dep_id, new_dep_title)

        if success:
            content = new_content
            successful.append((skill_id, new_dep_id, reason))
            print(f"  ✓ Applied")
        else:
            failed.append((skill_id, new_dep_id, reason))
            print(f"  ✗ Failed")

    print(f"\n\nSummary:")
    print(f"  Successful: {len(successful)}")
    print(f"  Failed: {len(failed)}")

    if successful:
        print("\nWriting modified allskills.md...")
        write_file('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md', content)
        print("✓ File updated")

        # Write report
        print("\nWriting report...")
        report = "# Cross-Topic Dependencies Applied\n\n"
        report += f"Total modifications: {len(successful)}\n\n"

        by_hub = {}
        for skill_id, hub_id, reason in successful:
            if hub_id not in by_hub:
                by_hub[hub_id] = []
            by_hub[hub_id].append((skill_id, reason))

        for hub_id, items in sorted(by_hub.items()):
            if hub_id == 'T01.GK.01':
                report += "## Sequencing Foundation (T01.GK.01)\n\n"
            elif hub_id == 'T04.GK.01':
                report += "## Pattern Recognition (T04.GK.01)\n\n"

            for skill_id, reason in items:
                report += f"- **{skill_id}** now depends on **{hub_id}**\n"
                report += f"  - Reason: {reason}\n\n"

        write_file('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/cross_topic_changes_applied.md', report)
        print("✓ Report written")

    if failed:
        print("\nFailed modifications:")
        for skill_id, hub_id, reason in failed:
            print(f"  {skill_id} -> {hub_id}")

if __name__ == '__main__':
    main()
