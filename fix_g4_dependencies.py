#!/usr/bin/env python3
"""
Fix G4 dependency range violations by replacing GK/G1 dependencies with appropriate G2/G3 skills.
"""

import re

# Read the allskills.md file
with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md', 'r') as f:
    content = f.read()

# Define the fixes based on analysis of each topic
# Format: (skill_id, old_dependency, new_dependency, reason)
fixes = [
    # T01 - Everyday Algorithms (7 fixes)
    ("T01.G4.02", "T01.GK.08", "T01.G3.11", "G3.11 involves explaining what programs do, which is a more appropriate prerequisite for implementing written plans in code"),
    ("T01.G4.04", "T01.GK.07", "T01.G3.03", "G3.03 involves identifying repeated blocks in scripts, which is a direct prerequisite for replacing patterns with loops"),
    ("T01.G4.06", "T01.GK.07", "T01.G3.11", "G3.11 involves explaining programs and is at the right level for recognizing variables in programs"),
    ("T01.G4.07", "T01.GK.07", "T01.G3.05", "G3.05 involves replacing repeated blocks with loops, which is a prerequisite for tracing counter variables in loops"),
    ("T01.G4.09", "T01.GK.08", "T01.G3.08", "G3.08 involves adding if/then to scripts, which is appropriate for tracking game state with variables"),
    ("T01.G4.10", "T01.GK.08", "T01.G3.14", "G3.14 involves debugging loops with wrong repeat counts, which is a prerequisite for tracing multi-step algorithms"),
    ("T01.G4.11", "T01.GK.08", "T01.G3.14", "G3.14 involves debugging loops that repeat wrong number of times, which is directly related to off-by-one counting bugs"),

    # T02 - Algorithm Diagrams (5 fixes)
    ("T02.G4.01", "T02.GK.04", "T02.G3.01", "G3.01 involves tracing flowcharts with decisions, which is a prerequisite for adding loops to flowcharts"),
    ("T02.G4.02", "T02.GK.04", "T02.G3.01", "G3.01 involves tracing flowcharts with decisions, which is a prerequisite for designing flowcharts with repetition"),
    ("T02.G4.04", "T02.GK.04", "T02.G3.01", "G3.01 involves tracing flowcharts with decisions, which is a prerequisite for tracing flowcharts with loops"),
    ("T02.G4.05", "T02.GK.03", "T02.G3.02", "G3.02 involves matching code to flowcharts, which is a prerequisite for converting stories to pseudocode"),
    ("T02.G4.06", "T02.GK.03", "T02.G3.02", "G3.02 involves matching code to flowcharts, which is a prerequisite for matching pseudocode to flowcharts"),

    # T03 - Problem Decomposition (4 fixes)
    ("T03.G4.01", "T03.GK.03", "T03.G3.01", "G3.01 involves identifying sub-problems, which is a prerequisite for breaking medium-size projects into components"),
    ("T03.G4.02", "T03.G1.01", "T03.G3.02", "G3.02 involves breaking tasks into steps and grouping, which is a prerequisite for grouping components into modules"),
    ("T03.G4.03", "T03.G1.01", "T03.G3.02", "G3.02 involves breaking tasks into steps and grouping, which is a prerequisite for assigning project tasks to team roles"),
    ("T03.G4.04", "T03.G1.01", "T03.G3.02", "G3.02 involves breaking tasks into steps and grouping, which is a prerequisite for creating task lists with owners"),

    # T04 - Algorithm Patterns (3 fixes)
    ("T04.G4.01", "T04.GK.03", "T04.G3.01", "G3.01 involves identifying where loops could replace repeated blocks, which is a prerequisite for tracing loops that create visual patterns"),
    ("T04.G4.02", "T04.GK.03", "T04.G3.03", "G3.03 involves nested loops for rows and columns, which is a prerequisite for identifying nested pattern structures"),
    ("T04.G4.03", "T04.GK.03", "T04.G3.04", "G3.04 involves combining patterns with conditions, which is a prerequisite for recognizing if patterns that handle special cases"),

    # T05 - Human-Centered Design (6 fixes)
    ("T05.G4.01", "T05.G1.01", "T05.G3.01", "G3.01 involves interviewing users to understand needs, which is a prerequisite for identifying key details in personas"),
    ("T05.G4.02", "T05.G1.01", "T05.G3.02", "G3.02 involves creating basic user personas, which is a prerequisite for matching designs to personas"),
    ("T05.G4.03", "T05.G1.01", "T05.G3.03", "G3.03 involves listing accessibility needs, which is a prerequisite for recognizing accessibility issues"),
    ("T05.G4.04", "T05.G1.01", "T05.G3.03", "G3.03 involves listing accessibility needs, which is a prerequisite for choosing accessibility improvements"),
    ("T05.G4.05", "T05.G1.01", "T05.G3.04", "G3.04 involves identifying simplifications in models, which is a prerequisite for deciding what to include vs ignore in simulations"),
    ("T05.G4.06", "T05.G1.01", "T05.G3.04", "G3.04 involves identifying simplifications in models, which is a prerequisite for explaining why simplifications are reasonable"),

    # T25 - Data Representation (3 fixes)
    ("T25.G4.02", "T25.G1.01", "T25.G3.01", "G3.01 involves converting between number and text, which is a prerequisite for encoding facts in different formats"),
    ("T25.G4.03", "T25.G1.01", "T25.G3.02", "G3.02 involves comparing different data formats, which is a prerequisite for comparing dense vs sparse representations"),
    ("T25.G4.04", "T25.G1.01", "T25.G3.02", "G3.02 involves comparing different data formats, which is a prerequisite for documenting assumptions in data keys"),

    # T30 - Devices & Hardware Systems (1 fix)
    ("T30.G4.03", "T30.G1.01", "T30.G3.01", "G3.01 involves identifying input/output/storage devices, which is a prerequisite for understanding latency vs bandwidth"),

    # T32 - Cybersecurity & Digital Safety (3 fixes)
    ("T32.G4.01", "T32.G1.01", "T32.G3.01", "G3.01 involves identifying safe vs unsafe behaviors, which is a prerequisite for building digital citizenship agreements"),
    ("T32.G4.02", "T32.G1.01", "T32.G3.02", "G3.02 involves explaining why strong passwords matter, which is a prerequisite for using password managers"),
    ("T32.G4.04", "T32.G1.01", "T32.G3.03", "G3.03 involves recognizing phishing attempts, which is a prerequisite for practicing secure file sharing"),

    # T35 - Impacts & Ethics (2 fixes)
    ("T35.G4.01", "T35.G1.01", "T35.G3.01", "G3.01 involves identifying positive and negative impacts of technology, which is a prerequisite for analyzing case studies"),
    ("T35.G4.03", "T35.G1.01", "T35.G3.02", "G3.02 involves discussing fairness in algorithms, which is a prerequisite for reflecting on accessibility/inclusion in games"),

    # T36 - Careers, Collaboration & Future Paths (3 fixes)
    ("T36.G4.01", "T36.G1.01", "T36.G3.01", "G3.01 involves identifying tech jobs in the community, which is a prerequisite for exploring diverse tech careers"),
    ("T36.G4.02", "T36.G1.01", "T36.G3.02", "G3.02 involves pair programming basics, which is a prerequisite for tracking work with shared checklists"),
    ("T36.G4.03", "T36.G1.01", "T36.G3.02", "G3.02 involves pair programming basics, which is a prerequisite for role-playing project disagreements"),
]

# Apply fixes
report = []
report.append("=" * 80)
report.append("G4 DEPENDENCY FIXES - DETAILED REPORT")
report.append("=" * 80)
report.append("")
report.append(f"Total fixes applied: {len(fixes)}")
report.append("")

for skill_id, old_dep, new_dep, reason in fixes:
    # Find the skill section in the content
    skill_pattern = rf'(ID: {re.escape(skill_id)}\n.*?Dependencies:\n)(.*?)(\n\n\nID:|\Z)'
    match = re.search(skill_pattern, content, re.DOTALL)

    if match:
        before_deps = match.group(1)
        deps_section = match.group(2)
        after_deps = match.group(3)

        # Replace the old dependency with the new one
        old_line = f"* {old_dep}:"

        if old_line in deps_section:
            # Find the full line with the skill name
            old_line_pattern = rf'\* {re.escape(old_dep)}:.*?\n'
            old_match = re.search(old_line_pattern, deps_section)
            if old_match:
                old_full_line = old_match.group(0)

                # Get the skill name for the new dependency
                new_dep_pattern = rf'ID: {re.escape(new_dep)}\n.*?\nSkill: (.*?)\n'
                new_dep_match = re.search(new_dep_pattern, content)
                if new_dep_match:
                    new_skill_name = new_dep_match.group(1)
                    new_full_line = f"* {new_dep}: {new_skill_name}\n"

                    # Replace in deps_section
                    new_deps_section = deps_section.replace(old_full_line, new_full_line)

                    # Replace in content
                    old_section = before_deps + deps_section + after_deps
                    new_section = before_deps + new_deps_section + after_deps
                    content = content.replace(old_section, new_section)

                    # Add to report
                    report.append(f"FIXED: {skill_id}")
                    report.append(f"  Old dependency: {old_dep}")
                    report.append(f"  New dependency: {new_dep}")
                    report.append(f"  Reason: {reason}")
                    report.append("")
                else:
                    report.append(f"WARNING: Could not find skill name for {new_dep}")
                    report.append("")
        else:
            report.append(f"WARNING: Old dependency {old_dep} not found in {skill_id}")
            report.append("")
    else:
        report.append(f"WARNING: Could not find skill section for {skill_id}")
        report.append("")

# Write the updated content back
with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md', 'w') as f:
    f.write(content)

# Print report
report_text = "\n".join(report)
print(report_text)

# Save report to file
with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/G4_FIXES_REPORT.txt', 'w') as f:
    f.write(report_text)

print("\nFixes applied successfully!")
print("Report saved to: G4_FIXES_REPORT.txt")
