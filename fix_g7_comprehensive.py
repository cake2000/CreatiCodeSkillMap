#!/usr/bin/env python3
"""
Fix ALL HIGH and MEDIUM priority issues in Grade 7 skills.

This script:
1. Removes 116 transitive dependencies
2. Adds 31 missing dependencies
3. Creates backups and detailed reports
"""

import re
import os
from datetime import datetime
from collections import defaultdict

# File paths
ALLSKILLS_PATH = "/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md"
ANALYSIS_PATH = "/media/binyu/USB2/dev/CreatiCodeSkillMap/G7_COMPREHENSIVE_ANALYSIS.txt"

class SkillFixer:
    def __init__(self):
        self.skills = {}  # skill_id -> skill_data
        self.all_skill_ids = set()
        self.changes = []
        self.stats = {
            'transitive_removed': 0,
            'missing_added': 0,
            'skills_modified': 0
        }

    def parse_allskills(self, content):
        """Parse allskills.md into structured data."""
        skills = []
        current_skill = None
        lines = content.split('\n')
        i = 0

        while i < len(lines):
            line = lines[i]

            # Start of new skill
            if line.startswith('ID: '):
                if current_skill:
                    skills.append(current_skill)

                skill_id = line[4:].strip()
                self.all_skill_ids.add(skill_id)
                current_skill = {
                    'id': skill_id,
                    'start_line': i,
                    'topic': '',
                    'skill': '',
                    'description': '',
                    'dependencies': [],
                    'raw_lines': [line]
                }
                i += 1
                continue

            if current_skill:
                current_skill['raw_lines'].append(line)

                if line.startswith('Topic: '):
                    current_skill['topic'] = line[7:].strip()
                elif line.startswith('Skill: '):
                    current_skill['skill'] = line[7:].strip()
                elif line.startswith('Description: '):
                    current_skill['description'] = line[13:].strip()
                elif line.startswith('Dependencies:'):
                    # Read all dependency lines
                    i += 1
                    while i < len(lines) and lines[i].startswith('* '):
                        dep_line = lines[i]
                        current_skill['raw_lines'].append(dep_line)
                        # Extract dependency ID
                        match = re.match(r'\* ([^:]+):', dep_line)
                        if match:
                            current_skill['dependencies'].append(match.group(1))
                        i += 1
                    continue

            i += 1

        if current_skill:
            skills.append(current_skill)

        return skills

    def build_dependency_graph(self):
        """Build a map of skill_id -> direct dependencies."""
        dep_graph = {}
        for skill in self.skills.values():
            dep_graph[skill['id']] = set(skill['dependencies'])
        return dep_graph

    def get_transitive_deps(self, skill_id, dep_graph, visited=None):
        """Get all transitive dependencies for a skill."""
        if visited is None:
            visited = set()

        if skill_id in visited or skill_id not in dep_graph:
            return set()

        visited.add(skill_id)
        transitive = set()

        for dep in dep_graph.get(skill_id, []):
            transitive.add(dep)
            transitive.update(self.get_transitive_deps(dep, dep_graph, visited))

        return transitive

    def find_transitive_dependencies(self):
        """Find and return transitive dependencies to remove."""
        dep_graph = self.build_dependency_graph()
        to_remove = defaultdict(list)

        for skill_id, skill in self.skills.items():
            if not skill_id.startswith('T') or '.G7.' not in skill_id:
                continue

            deps = skill['dependencies']
            if len(deps) <= 1:
                continue

            # For each pair of dependencies, check if one implies the other
            for dep_a in deps:
                for dep_b in deps:
                    if dep_a == dep_b:
                        continue

                    # Get transitive deps of dep_a
                    trans_deps = self.get_transitive_deps(dep_a, dep_graph)

                    # If dep_b is in transitive deps of dep_a, then dep_b is redundant
                    if dep_b in trans_deps:
                        to_remove[skill_id].append({
                            'remove': dep_b,
                            'implied_by': dep_a,
                            'reason': f'{dep_b} is implied by {dep_a}'
                        })

        return to_remove

    def parse_analysis_for_missing_deps(self):
        """Parse the analysis file to find missing dependencies."""
        missing_deps = defaultdict(list)

        with open(ANALYSIS_PATH, 'r') as f:
            content = f.read()

        # Split by skill sections
        skill_sections = re.split(r'\n-{80,}\n', content)

        for section in skill_sections:
            # Extract skill ID
            skill_match = re.search(r'SKILL: (T\d+\.G7\.\d+)', section)
            if not skill_match:
                continue

            skill_id = skill_match.group(1)

            # Find missing dependency issues
            missing_matches = re.finditer(
                r'Issue #\d+: \[Missing dependency\]\s+Problem: (.+?)\s+Fix: (.+?)(?=\n  Issue #|\n-|$)',
                section,
                re.DOTALL
            )

            for match in missing_matches:
                problem = match.group(1).strip()
                fix = match.group(2).strip()

                # Parse the fix to extract dependency to add
                suggested_dep = None

                if 'T10' in fix:
                    # List dependency
                    if 'T10.G3.01' in fix:
                        suggested_dep = 'T10.G3.01'
                    elif 'T10.G3.02' in fix:
                        suggested_dep = 'T10.G3.02'
                    elif 'T10.G6.04' in fix:
                        suggested_dep = 'T10.G6.04'
                    elif 'T10.G5' in fix:
                        suggested_dep = 'T10.G5.01'
                    else:
                        suggested_dep = 'T10.G3.01'  # Default

                elif 'T07' in fix:
                    # Loop dependency
                    suggested_dep = 'T07.G3.01'

                elif 'T09' in fix:
                    # Variable dependency
                    suggested_dep = 'T09.G3.01'

                elif 'T08' in fix:
                    # Condition dependency
                    if 'T08.G6.03' in fix:
                        suggested_dep = 'T08.G6.03'
                    else:
                        suggested_dep = 'T08.G3.01'

                if suggested_dep and suggested_dep in self.all_skill_ids:
                    missing_deps[skill_id].append({
                        'add': suggested_dep,
                        'reason': problem
                    })

        return missing_deps

    def apply_fixes(self, transitive_to_remove, missing_to_add):
        """Apply all fixes to G7 skills."""
        modified_skills = set()

        for skill_id, skill in self.skills.items():
            if not skill_id.startswith('T') or '.G7.' not in skill_id:
                continue

            original_deps = skill['dependencies'][:]
            modified = False

            # Remove transitive dependencies
            if skill_id in transitive_to_remove:
                deps_to_remove = set()
                for item in transitive_to_remove[skill_id]:
                    deps_to_remove.add(item['remove'])

                # Remove duplicates - keep only first occurrence
                unique_removes = []
                seen = set()
                for item in transitive_to_remove[skill_id]:
                    if item['remove'] not in seen:
                        unique_removes.append(item)
                        seen.add(item['remove'])

                for item in unique_removes:
                    dep_to_remove = item['remove']
                    if dep_to_remove in skill['dependencies']:
                        skill['dependencies'].remove(dep_to_remove)
                        self.changes.append({
                            'skill_id': skill_id,
                            'type': 'REMOVE',
                            'dependency': dep_to_remove,
                            'reason': item['reason']
                        })
                        self.stats['transitive_removed'] += 1
                        modified = True

            # Add missing dependencies
            if skill_id in missing_to_add:
                for item in missing_to_add[skill_id]:
                    dep_to_add = item['add']
                    if dep_to_add not in skill['dependencies']:
                        skill['dependencies'].append(dep_to_add)
                        self.changes.append({
                            'skill_id': skill_id,
                            'type': 'ADD',
                            'dependency': dep_to_add,
                            'reason': item['reason']
                        })
                        self.stats['missing_added'] += 1
                        modified = True

            if modified:
                modified_skills.add(skill_id)

        self.stats['skills_modified'] = len(modified_skills)
        return modified_skills

    def rebuild_skill_text(self, skill):
        """Rebuild the text for a skill with updated dependencies."""
        lines = []

        # Add ID, Topic, Skill, Description
        lines.append(f"ID: {skill['id']}")
        lines.append(f"Topic: {skill['topic']}")
        lines.append(f"Skill: {skill['skill']}")
        lines.append(f"Description: {skill['description']}")

        # Add dependencies if any
        if skill['dependencies']:
            lines.append('')
            lines.append('Dependencies:')
            for dep_id in skill['dependencies']:
                # Find the skill name for this dependency
                dep_name = ""
                if dep_id in self.skills:
                    dep_name = self.skills[dep_id]['skill']
                lines.append(f"* {dep_id}: {dep_name}")

        return lines

    def write_fixed_allskills(self, output_path):
        """Write the fixed allskills.md file."""
        output_lines = []

        for skill in sorted(self.skills.values(), key=lambda s: s['id']):
            skill_lines = self.rebuild_skill_text(skill)
            output_lines.extend(skill_lines)
            output_lines.append('')
            output_lines.append('')
            output_lines.append('')

        with open(output_path, 'w') as f:
            f.write('\n'.join(output_lines))

    def generate_report(self):
        """Generate a detailed fix report."""
        report = []
        report.append("=" * 80)
        report.append("G7 SKILLS FIX REPORT")
        report.append("=" * 80)
        report.append(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")
        report.append("SUMMARY:")
        report.append(f"  Total G7 skills: {len([s for s in self.skills if '.G7.' in s])}")
        report.append(f"  Skills modified: {self.stats['skills_modified']}")
        report.append(f"  Transitive dependencies removed: {self.stats['transitive_removed']}")
        report.append(f"  Missing dependencies added: {self.stats['missing_added']}")
        report.append(f"  Total changes: {len(self.changes)}")
        report.append("")
        report.append("=" * 80)
        report.append("DETAILED CHANGES")
        report.append("=" * 80)
        report.append("")

        # Group changes by skill
        changes_by_skill = defaultdict(list)
        for change in self.changes:
            changes_by_skill[change['skill_id']].append(change)

        for skill_id in sorted(changes_by_skill.keys()):
            skill = self.skills[skill_id]
            report.append(f"SKILL: {skill_id}")
            report.append(f"TITLE: {skill['skill']}")
            report.append("")

            changes = changes_by_skill[skill_id]
            removals = [c for c in changes if c['type'] == 'REMOVE']
            additions = [c for c in changes if c['type'] == 'ADD']

            if removals:
                report.append(f"  REMOVED {len(removals)} transitive dependencies:")
                for change in removals:
                    report.append(f"    - {change['dependency']}")
                    report.append(f"      Reason: {change['reason']}")
                report.append("")

            if additions:
                report.append(f"  ADDED {len(additions)} missing dependencies:")
                for change in additions:
                    report.append(f"    + {change['dependency']}")
                    report.append(f"      Reason: {change['reason']}")
                report.append("")

            report.append("-" * 80)
            report.append("")

        return '\n'.join(report)


def main():
    print("=" * 80)
    print("G7 SKILLS COMPREHENSIVE FIX SCRIPT")
    print("=" * 80)
    print()

    # Create backup
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = f"{ALLSKILLS_PATH}.backup_g7_{timestamp}"

    print(f"Creating backup: {backup_path}")
    with open(ALLSKILLS_PATH, 'r') as f:
        original_content = f.read()

    with open(backup_path, 'w') as f:
        f.write(original_content)
    print("Backup created successfully")
    print()

    # Initialize fixer
    fixer = SkillFixer()

    # Parse allskills.md
    print("Parsing allskills.md...")
    skills_list = fixer.parse_allskills(original_content)
    for skill in skills_list:
        fixer.skills[skill['id']] = skill
    print(f"Parsed {len(fixer.skills)} total skills")
    g7_count = len([s for s in fixer.skills if '.G7.' in s])
    print(f"Found {g7_count} G7 skills")
    print()

    # Find transitive dependencies
    print("Analyzing transitive dependencies...")
    transitive_to_remove = fixer.find_transitive_dependencies()
    trans_count = sum(len(items) for items in transitive_to_remove.values())
    print(f"Found {trans_count} transitive dependencies to remove")
    print()

    # Parse missing dependencies from analysis
    print("Parsing missing dependencies from analysis file...")
    missing_to_add = fixer.parse_analysis_for_missing_deps()
    missing_count = sum(len(items) for items in missing_to_add.values())
    print(f"Found {missing_count} missing dependencies to add")
    print()

    # Apply fixes
    print("Applying fixes...")
    modified_skills = fixer.apply_fixes(transitive_to_remove, missing_to_add)
    print(f"Modified {len(modified_skills)} skills")
    print(f"  - Removed {fixer.stats['transitive_removed']} transitive dependencies")
    print(f"  - Added {fixer.stats['missing_added']} missing dependencies")
    print()

    # Write fixed file
    print(f"Writing fixed allskills.md...")
    fixer.write_fixed_allskills(ALLSKILLS_PATH)
    print("File written successfully")
    print()

    # Generate report
    print("Generating detailed report...")
    report = fixer.generate_report()
    report_path = "/media/binyu/USB2/dev/CreatiCodeSkillMap/G7_FIX_REPORT.txt"
    with open(report_path, 'w') as f:
        f.write(report)
    print(f"Report saved to: {report_path}")
    print()

    # Print summary
    print("=" * 80)
    print("FIX COMPLETE!")
    print("=" * 80)
    print(f"Backup: {backup_path}")
    print(f"Report: {report_path}")
    print()
    print("Summary:")
    print(f"  - {fixer.stats['skills_modified']} skills modified")
    print(f"  - {fixer.stats['transitive_removed']} transitive dependencies removed")
    print(f"  - {fixer.stats['missing_added']} missing dependencies added")
    print()

    # Print sample changes
    if fixer.changes:
        print("Sample changes:")
        for change in fixer.changes[:5]:
            if change['type'] == 'REMOVE':
                print(f"  - [{change['skill_id']}] Removed {change['dependency']}")
            else:
                print(f"  + [{change['skill_id']}] Added {change['dependency']}")
        if len(fixer.changes) > 5:
            print(f"  ... and {len(fixer.changes) - 5} more changes")
    print()


if __name__ == '__main__':
    main()
