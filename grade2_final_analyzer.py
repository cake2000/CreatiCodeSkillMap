#!/usr/bin/env python3
"""
Final Grade 2 Cross-Topic Dependency Analysis
Focus: Validate existing dependencies and add only critical missing ones
"""

import re
from collections import defaultdict, deque
from typing import Dict, List, Set, Tuple

class FinalG2Analyzer:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.all_skills = {}
        self.grade2_skills = {}
        self.skills_by_topic = defaultdict(list)
        self.skills_by_grade = defaultdict(list)

        self.dependencies_added = []
        self.dependencies_removed = []
        self.violations_fixed = []
        self.circular_deps_found = []

        self.topic_names = {
            'T01': 'algorithms', 'T02': 'decomposition', 'T03': 'variables',
            'T04': 'motion', 'T05': 'looks', 'T06': 'randomness',
            'T07': 'events', 'T08': 'pen', 'T09': 'control',
            'T10': 'sensing', 'T11': 'operators', 'T12': 'cloning',
            'T13': 'list-operations', 'T14': 'broadcasting', 'T15': 'sound',
            'T16': 'video-sensing', 'T17': 'text-to-speech', 'T18': 'translate',
            'T19': 'custom-blocks', 'T20': 'music', 'T21': 'game-mechanics',
            'T22': 'animation', 'T23': 'storytelling', 'T24': 'art',
            'T25': 'math', 'T26': 'science', 'T27': 'social-studies',
            'T28': 'coordinate-systems', 'T29': 'data-collection', 'T30': 'debugging',
            'T31': 'user-input', 'T32': 'sprites', 'T33': 'backdrops',
            'T34': 'costumes', 'T35': 'project-planning', 'T36': 'physics-simulation'
        }

    def parse_file(self):
        """Parse allskills.md"""
        print("Reading allskills.md...")
        with open(self.file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        skills = re.split(r'\n(?=ID:\s+T\d+\.)', content)
        print(f"Found {len(skills)} potential skill entries")

        for skill_text in skills:
            if not skill_text.strip():
                continue

            id_match = re.search(r'ID:\s+(T\d+\.(GK|G\d+)\.\d+)', skill_text)
            if not id_match:
                continue

            skill_id = id_match.group(1)
            grade_part = id_match.group(2)
            grade = 0 if grade_part == 'GK' else int(grade_part[1:])

            topic_match = re.search(r'Topic:\s+([^\n]+)', skill_text)
            topic_raw = topic_match.group(1) if topic_match else ''
            topic_code_match = re.search(r'(T\d+)', topic_raw)
            topic = topic_code_match.group(1) if topic_code_match else skill_id.split('.')[0]

            title_match = re.search(r'Skill:\s+([^\n]+)', skill_text)
            title = title_match.group(1) if title_match else ''

            desc_match = re.search(r'Description:\s+([^\n]+(?:\n(?!Dependencies:|ID:)[^\n]+)*)', skill_text)
            description = desc_match.group(1) if desc_match else ''

            dependencies = []
            deps_section = re.search(r'Dependencies:(.*?)(?=\n\nID:|\n\n\nID:|\Z)', skill_text, re.DOTALL)
            if deps_section:
                dep_matches = re.findall(r'\*\s+(T\d+\.[A-Z0-9]+\.\d+)', deps_section.group(1))
                dependencies = dep_matches

            skill = {
                'skill_id': skill_id,
                'title': title,
                'topic': topic,
                'grade': grade,
                'dependencies': dependencies[:],  # Copy
                'description': description,
                'original_text': skill_text
            }

            self.all_skills[skill_id] = skill
            if grade == 2:
                self.grade2_skills[skill_id] = skill
            if topic:
                self.skills_by_topic[topic].append(skill_id)
            if grade >= 0:
                self.skills_by_grade[grade].append(skill_id)

        print(f"Parsed {len(self.all_skills)} total skills")
        print(f"Found {len(self.grade2_skills)} Grade 2 skills")

    def validate_existing_dependencies(self):
        """Validate X-2 rule, remove circular deps, check for non-existent deps"""
        print("\n=== VALIDATING EXISTING DEPENDENCIES ===")

        for skill_id, skill in self.grade2_skills.items():
            deps_to_remove = []

            for dep_id in skill['dependencies'][:]:
                # Check if dependency exists
                if dep_id not in self.all_skills:
                    print(f"  Warning: {skill_id} depends on non-existent {dep_id}")
                    deps_to_remove.append((dep_id, 'Non-existent dependency'))
                    continue

                # Check X-2 rule (Grade 2 can only depend on 0, 1, 2)
                dep_grade = self.all_skills[dep_id]['grade']
                if dep_grade > 2:
                    deps_to_remove.append((dep_id, f'X-2 violation (grade {dep_grade} > 2)'))
                    continue

                # Check for self-reference
                if dep_id == skill_id:
                    deps_to_remove.append((dep_id, 'Self-reference'))
                    continue

            # Remove invalid dependencies
            for dep_id, reason in deps_to_remove:
                if dep_id in skill['dependencies']:
                    skill['dependencies'].remove(dep_id)
                    self.dependencies_removed.append({
                        'skill_id': skill_id,
                        'title': skill['title'],
                        'removed': dep_id,
                        'reason': reason
                    })
                    self.violations_fixed.append({
                        'skill_id': skill_id,
                        'title': skill['title'],
                        'removed': dep_id,
                        'reason': reason
                    })

        # Check for circular dependencies
        self._detect_circular_dependencies()

        print(f"  Removed {len(self.dependencies_removed)} invalid dependencies")
        print(f"  Found {len(self.circular_deps_found)} circular dependency chains")

    def _detect_circular_dependencies(self):
        """Detect circular dependencies using DFS"""
        def has_cycle(skill_id, visited, rec_stack, path):
            visited.add(skill_id)
            rec_stack.add(skill_id)
            path.append(skill_id)

            if skill_id in self.all_skills:
                for dep_id in self.all_skills[skill_id]['dependencies']:
                    if dep_id not in visited:
                        if has_cycle(dep_id, visited, rec_stack, path):
                            return True
                    elif dep_id in rec_stack:
                        # Found cycle
                        cycle_start = path.index(dep_id)
                        cycle = path[cycle_start:] + [dep_id]
                        self.circular_deps_found.append(cycle)
                        return True

            path.pop()
            rec_stack.remove(skill_id)
            return False

        visited = set()
        for skill_id in self.grade2_skills:
            if skill_id not in visited:
                has_cycle(skill_id, visited, set(), [])

    def add_critical_cross_topic_dependencies(self):
        """Add only critical missing cross-topic dependencies"""
        print("\n=== ADDING CRITICAL CROSS-TOPIC DEPENDENCIES ===")

        # Only add deps for skills that have NONE or very few
        for skill_id, skill in sorted(self.grade2_skills.items()):
            current_dep_count = len(skill['dependencies'])

            # Skip skills that already have many dependencies
            if current_dep_count > 5:
                continue

            topic = skill['topic']
            title_lower = skill['title'].lower()
            desc_lower = skill['description'].lower()
            combined_text = f"{title_lower} {desc_lower}"

            current_deps = set(skill['dependencies'])
            needed_deps = set()

            # Critical cross-topic rules (very selective)
            # Only add if skill clearly needs it and doesn't have it

            # Skills working with variables but no variable deps
            if ('variable' in combined_text or 'score' in combined_text) and topic != 'T03':
                has_var_dep = any(self.all_skills.get(d, {}).get('topic') == 'T03' for d in current_deps)
                if not has_var_dep:
                    needed_deps.update(self._get_minimal_deps('T03', 1))

            # Skills working with loops but no control deps
            if ('repeat' in combined_text or 'loop' in combined_text or 'forever' in combined_text) and topic != 'T09':
                has_control_dep = any(self.all_skills.get(d, {}).get('topic') == 'T09' for d in current_deps)
                if not has_control_dep:
                    needed_deps.update(self._get_minimal_deps('T09', 1))

            # Skills working with sensing but no sensing deps
            if ('touch' in combined_text or 'mouse' in combined_text or 'keyboard' in combined_text or 'ask' in combined_text) and topic != 'T10':
                has_sensing_dep = any(self.all_skills.get(d, {}).get('topic') == 'T10' for d in current_deps)
                if not has_sensing_dep:
                    needed_deps.update(self._get_minimal_deps('T10', 1))

            # Skills working with events but no event deps
            if ('when clicked' in combined_text or 'when key' in combined_text or 'start' in combined_text) and topic != 'T07':
                has_event_dep = any(self.all_skills.get(d, {}).get('topic') == 'T07' for d in current_deps)
                if not has_event_dep:
                    needed_deps.update(self._get_minimal_deps('T07', 1))

            # Filter: only cross-topic, valid, not already present
            valid_new_deps = set()
            for dep_id in needed_deps:
                if dep_id in current_deps:
                    continue
                if dep_id not in self.all_skills:
                    continue
                dep_skill = self.all_skills[dep_id]
                if dep_skill['topic'] == topic:
                    continue
                if dep_skill['grade'] > 2:
                    continue
                valid_new_deps.add(dep_id)

            if valid_new_deps:
                reason = self._determine_reason(combined_text, valid_new_deps)
                self.dependencies_added.append({
                    'skill_id': skill_id,
                    'title': skill['title'],
                    'topic': topic,
                    'added': list(valid_new_deps),
                    'reason': reason
                })
                skill['dependencies'].extend(valid_new_deps)
                print(f"  {skill_id}: +{len(valid_new_deps)} deps ({current_dep_count} existing)")

        print(f"\nTotal new dependencies added: {sum(len(item['added']) for item in self.dependencies_added)}")

    def _get_minimal_deps(self, topic: str, max_grade: int) -> Set[str]:
        """Get 1-2 foundational skills from a topic"""
        skills = []
        for skill_id in self.skills_by_topic.get(topic, []):
            skill = self.all_skills[skill_id]
            if skill['grade'] <= max_grade:
                skills.append((skill['grade'], skill_id))

        skills.sort()
        return {s[1] for s in skills[:2]}  # Only first 2

    def _determine_reason(self, text: str, deps: Set[str]) -> str:
        """Determine reason for adding dependencies"""
        dep_topics = set()
        for dep_id in deps:
            if dep_id in self.all_skills:
                dep_topics.add(self.all_skills[dep_id]['topic'])

        topic_names = [self.topic_names.get(t, t) for t in sorted(dep_topics)]
        return f"Missing essential cross-topic prerequisites: {', '.join(topic_names)}"

    def generate_report(self) -> str:
        """Generate comprehensive report"""
        report = []
        report.append("=" * 80)
        report.append("PHASE 2: GRADE 2 CROSS-TOPIC DEPENDENCY ANALYSIS")
        report.append("Final Report - Validation & Critical Additions")
        report.append("=" * 80)
        report.append("")

        report.append("EXECUTIVE SUMMARY")
        report.append("-" * 80)
        report.append(f"Total Grade 2 skills analyzed: {len(self.grade2_skills)}")
        report.append(f"Skills with existing dependencies: {sum(1 for s in self.grade2_skills.values() if s['dependencies'])}")
        report.append("")
        report.append(f"Dependencies removed (violations): {len(self.dependencies_removed)}")
        report.append(f"X-2 rule violations fixed: {sum(1 for v in self.violations_fixed if 'X-2' in v['reason'])}")
        report.append(f"Circular dependency chains found: {len(self.circular_deps_found)}")
        report.append("")
        report.append(f"Critical cross-topic dependencies added: {sum(len(item['added']) for item in self.dependencies_added)}")
        report.append(f"Skills enhanced with new dependencies: {len(self.dependencies_added)}")
        report.append("")

        # Violations section
        if self.violations_fixed:
            report.append("VIOLATIONS FIXED")
            report.append("-" * 80)
            by_reason = defaultdict(list)
            for item in self.violations_fixed:
                by_reason[item['reason']].append(item)

            for reason in sorted(by_reason.keys()):
                report.append(f"\n{reason}:")
                for item in by_reason[reason][:10]:  # Limit to 10 per reason
                    report.append(f"  {item['skill_id']}: Removed {item['removed']}")
                if len(by_reason[reason]) > 10:
                    report.append(f"  ... and {len(by_reason[reason]) - 10} more")
            report.append("")

        # Circular dependencies
        if self.circular_deps_found:
            report.append("CIRCULAR DEPENDENCIES DETECTED")
            report.append("-" * 80)
            for cycle in self.circular_deps_found[:5]:  # Show first 5
                report.append(f"  {' -> '.join(cycle)}")
            if len(self.circular_deps_found) > 5:
                report.append(f"  ... and {len(self.circular_deps_found) - 5} more cycles")
            report.append("")

        # New dependencies added
        if self.dependencies_added:
            report.append("CRITICAL CROSS-TOPIC DEPENDENCIES ADDED")
            report.append("-" * 80)
            by_topic = defaultdict(list)
            for item in self.dependencies_added:
                by_topic[item['topic']].append(item)

            for topic in sorted(by_topic.keys()):
                topic_name = self.topic_names.get(topic, topic)
                report.append(f"\n{topic} ({topic_name}):")
                for item in by_topic[topic]:
                    report.append(f"  {item['skill_id']}: {item['title']}")
                    report.append(f"    Reason: {item['reason']}")
                    for dep in sorted(item['added']):
                        if dep in self.all_skills:
                            dep_skill = self.all_skills[dep]
                            dep_topic_name = self.topic_names.get(dep_skill['topic'], dep_skill['topic'])
                            report.append(f"      + {dep} (G{dep_skill['grade']}, {dep_topic_name}): {dep_skill['title'][:60]}")
            report.append("")

        # Summary by topic
        report.append("SUMMARY BY TOPIC")
        report.append("-" * 80)
        topic_stats = defaultdict(lambda: {'total': 0, 'with_deps': 0, 'avg_deps': 0})
        for skill_id, skill in self.grade2_skills.items():
            topic = skill['topic']
            topic_stats[topic]['total'] += 1
            if skill['dependencies']:
                topic_stats[topic]['with_deps'] += 1
                topic_stats[topic]['avg_deps'] += len(skill['dependencies'])

        for topic in sorted(topic_stats.keys()):
            topic_name = self.topic_names.get(topic, topic)
            stats = topic_stats[topic]
            avg = stats['avg_deps'] / stats['with_deps'] if stats['with_deps'] > 0 else 0
            report.append(f"{topic} ({topic_name}): {stats['total']} skills, {stats['with_deps']} with deps, avg {avg:.1f} deps/skill")

        report.append("")

        return "\n".join(report)

    def apply_fixes_to_file(self):
        """Apply all fixes to allskills.md"""
        print("\n=== APPLYING FIXES TO FILE ===")

        with open(self.file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        modified = 0

        for skill_id, skill in self.grade2_skills.items():
            # Find skill section
            pattern = rf'(ID:\s+{re.escape(skill_id)}\n.*?)(Dependencies:.*?)(?=\n\nID:|\n\n\nID:|\Z)'
            match = re.search(pattern, content, re.DOTALL)

            if not match:
                # No dependencies section
                pattern = rf'(ID:\s+{re.escape(skill_id)}\n.*?Description:[^\n]+(?:\n_[^\n]+)?)((?=\n\nID:|\n\n\nID:|\Z))'
                match = re.search(pattern, content, re.DOTALL)

                if match and skill['dependencies']:
                    # Add new dependencies section
                    before = match.group(1)
                    new_deps = "\n\nDependencies:\n" + "\n".join(
                        f"* {dep}: {self.all_skills[dep]['title']}"
                        for dep in sorted(set(skill['dependencies']))
                        if dep in self.all_skills
                    )
                    content = content.replace(match.group(0), before + new_deps)
                    modified += 1
                continue

            # Update existing dependencies
            before_deps = match.group(1)

            if skill['dependencies']:
                new_deps = "Dependencies:\n" + "\n".join(
                    f"* {dep}: {self.all_skills[dep]['title']}"
                    for dep in sorted(set(skill['dependencies']))
                    if dep in self.all_skills
                )
                content = content.replace(match.group(0), before_deps + new_deps)
                modified += 1
            else:
                # Remove dependencies section if no deps left
                content = content.replace(match.group(0), before_deps.rstrip())
                modified += 1

        with open(self.file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  Updated {modified} skills in file")

    def run(self):
        """Run complete analysis"""
        self.parse_file()
        self.validate_existing_dependencies()
        self.add_critical_cross_topic_dependencies()

        report = self.generate_report()
        print("\n" + report[:2000])  # Print first part
        print("\n... (see full report in file)")

        report_path = '/media/binyu/USB2/dev/CreatiCodeSkillMap/PHASE2_G2_FINAL_REPORT.md'
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"\nFull report saved to: {report_path}")

        self.apply_fixes_to_file()

        # Return summary
        return {
            'total_g2_skills': len(self.grade2_skills),
            'violations_fixed': len(self.violations_fixed),
            'circular_deps': len(self.circular_deps_found),
            'deps_added': sum(len(item['added']) for item in self.dependencies_added),
            'deps_removed': len(self.dependencies_removed)
        }

if __name__ == '__main__':
    analyzer = FinalG2Analyzer('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md')
    summary = analyzer.run()

    print("\n" + "=" * 80)
    print("QUICK SUMMARY")
    print("=" * 80)
    print(f"Total Grade 2 skills processed: {summary['total_g2_skills']}")
    print(f"Violations fixed: {summary['violations_fixed']}")
    print(f"Circular dependency chains: {summary['circular_deps']}")
    print(f"Dependencies added: {summary['deps_added']}")
    print(f"Dependencies removed: {summary['deps_removed']}")
    print("=" * 80)
