#!/usr/bin/env python3
"""
Grade 2 Cross-Topic Dependency Analysis and Fixes
Phase 2: Focus on Grade 2 skills only
"""

import re
from collections import defaultdict
from typing import Dict, List, Set, Tuple

class Grade2Analyzer:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.all_skills = {}  # skill_id -> skill_dict
        self.grade2_skills = {}  # skill_id -> skill_dict
        self.skills_by_topic = defaultdict(list)  # topic -> [skill_ids]
        self.skills_by_grade = defaultdict(list)  # grade -> [skill_ids]

        # Track changes
        self.dependencies_added = []
        self.dependencies_removed = []
        self.violations_fixed = []
        self.cross_topic_connections = []

    def parse_file(self):
        """Parse allskills.md and extract all skills"""
        print("Reading allskills.md...")
        with open(self.file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Split by skill entries (look for ID: pattern)
        skills = re.split(r'\n(?=ID:\s+T\d+\.)', content)

        print(f"Found {len(skills)} potential skill entries")

        for skill_text in skills:
            if not skill_text.strip():
                continue

            # Extract skill_id (e.g., T01.G2.01)
            id_match = re.search(r'ID:\s+(T\d+\.(GK|G\d+)\.\d+)', skill_text)
            if not id_match:
                continue

            skill_id = id_match.group(1)

            # Extract grade from ID (GK=0, G1=1, G2=2, etc.)
            grade_part = id_match.group(2)
            if grade_part == 'GK':
                grade = 0
            else:
                grade = int(grade_part[1:])

            # Extract topic (from "Topic:" line)
            topic_match = re.search(r'Topic:\s+([^\n]+)', skill_text)
            topic_raw = topic_match.group(1) if topic_match else ''
            # Extract just the topic code (e.g., "T01")
            topic_code_match = re.search(r'(T\d+)', topic_raw)
            topic = topic_code_match.group(1) if topic_code_match else skill_id.split('.')[0]

            # Extract skill title (from "Skill:" line)
            title_match = re.search(r'Skill:\s+([^\n]+)', skill_text)
            title = title_match.group(1) if title_match else ''

            # Extract dependencies (lines starting with * after "Dependencies:")
            dependencies = []
            deps_section = re.search(r'Dependencies:(.*?)(?=\n\n|\n[A-Z]|\Z)', skill_text, re.DOTALL)
            if deps_section:
                deps_text = deps_section.group(1)
                # Find all lines starting with * and extract the ID
                dep_matches = re.findall(r'\*\s+(T\d+\.[A-Z0-9]+\.\d+)', deps_text)
                dependencies = dep_matches

            skill = {
                'skill_id': skill_id,
                'title': title,
                'topic': topic,
                'grade': grade,
                'dependencies': dependencies,
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
        print(f"Topics: {len(self.skills_by_topic)}")

    def analyze_cross_topic_needs(self):
        """Analyze cross-topic dependencies for Grade 2 skills"""
        print("\n=== CROSS-TOPIC DEPENDENCY ANALYSIS ===")

        # Define knowledge requirements for each topic's Grade 2 skills
        cross_topic_rules = self._define_cross_topic_rules()

        for skill_id, skill in self.grade2_skills.items():
            topic = skill['topic']
            title = skill['title']
            current_deps = set(skill['dependencies'])

            # Check what cross-topic deps this skill should have
            needed_deps = self._get_needed_cross_topic_deps(skill, cross_topic_rules)

            # Find missing dependencies
            missing_deps = needed_deps - current_deps

            if missing_deps:
                # Verify these deps exist and are grade 0-2
                valid_missing = set()
                for dep_id in missing_deps:
                    if dep_id in self.all_skills:
                        dep_grade = self.all_skills[dep_id]['grade']
                        if dep_grade <= 2:
                            valid_missing.add(dep_id)

                if valid_missing:
                    self.dependencies_added.append({
                        'skill_id': skill_id,
                        'title': title,
                        'topic': topic,
                        'added': list(valid_missing),
                        'reason': 'Cross-topic prerequisite knowledge'
                    })
                    skill['dependencies'].extend(valid_missing)

    def _define_cross_topic_rules(self) -> Dict:
        """Define cross-topic dependency rules for Grade 2 skills"""
        # Map topic to required prerequisite topics/skills
        return {
            'game': {
                'needs': ['variables', 'loops', 'graphics', 'motion', 'events'],
                'key_skills': ['T01-G1', 'T02-G1', 'T03-G1', 'T04-G1', 'T07-G1']
            },
            'animation': {
                'needs': ['motion', 'looks', 'events', 'control'],
                'key_skills': ['T04-G1', 'T05-G1', 'T07-G1', 'T09-G1']
            },
            'physics': {
                'needs': ['variables', 'math', 'motion'],
                'key_skills': ['T01-G1', 'T03-G1', 'T04-G1']
            },
            'simulation': {
                'needs': ['variables', 'randomness', 'motion'],
                'key_skills': ['T01-G1', 'T06-G1', 'T04-G1']
            }
        }

    def _get_needed_cross_topic_deps(self, skill: Dict, rules: Dict) -> Set[str]:
        """Determine which cross-topic dependencies a skill needs"""
        needed = set()
        topic = skill['topic']
        title_lower = skill['title'].lower()

        # Game-related skills need fundamental building blocks
        if 'game' in title_lower or 'score' in title_lower or 'lives' in title_lower:
            # Need variables for score tracking
            needed.update(self._find_skills_by_topic_grade('variables', [0, 1]))
            # Need events for game start/control
            needed.update(self._find_skills_by_topic_grade('events', [0, 1]))

        # Animation skills need motion and looks
        if 'animat' in title_lower or 'move' in title_lower or 'costume' in title_lower:
            needed.update(self._find_skills_by_topic_grade('motion', [0, 1]))
            needed.update(self._find_skills_by_topic_grade('looks', [0, 1]))

        # Physics/simulation needs math and variables
        if 'physics' in title_lower or 'gravity' in title_lower or 'velocity' in title_lower:
            needed.update(self._find_skills_by_topic_grade('variables', [0, 1]))
            needed.update(self._find_skills_by_topic_grade('math', [0, 1]))

        # Interactive features need sensing
        if 'click' in title_lower or 'touch' in title_lower or 'detect' in title_lower:
            needed.update(self._find_skills_by_topic_grade('sensing', [0, 1]))

        # List operations need list basics
        if 'list' in title_lower and topic != 'list-operations':
            needed.update(self._find_skills_by_topic_grade('list-operations', [0, 1]))

        # Remove self and same-topic dependencies (those should already exist)
        needed.discard(skill['skill_id'])
        needed = {d for d in needed if d in self.all_skills and
                 self.all_skills[d]['topic'] != topic}

        return needed

    def _find_skills_by_topic_grade(self, topic: str, grades: List[int]) -> Set[str]:
        """Find all skills in a topic with specific grades"""
        found = set()
        for skill_id in self.skills_by_topic.get(topic, []):
            if self.all_skills[skill_id]['grade'] in grades:
                found.add(skill_id)
        return found

    def validate_dependencies(self):
        """Validate X-2 rule, circular deps, and transitive redundancy"""
        print("\n=== DEPENDENCY VALIDATION ===")

        for skill_id, skill in self.grade2_skills.items():
            grade = skill['grade']
            deps = skill['dependencies']

            # Check X-2 rule (Grade 2 can only depend on 0, 1, 2)
            invalid_deps = []
            for dep_id in deps[:]:
                if dep_id not in self.all_skills:
                    print(f"Warning: {skill_id} depends on non-existent {dep_id}")
                    invalid_deps.append(dep_id)
                    continue

                dep_grade = self.all_skills[dep_id]['grade']
                if dep_grade > 2:  # Violates X-2 rule
                    invalid_deps.append(dep_id)
                    self.violations_fixed.append({
                        'skill_id': skill_id,
                        'title': skill['title'],
                        'removed': dep_id,
                        'reason': f'Violates X-2 rule (dep grade {dep_grade} > 2)'
                    })

            # Remove invalid dependencies
            for dep_id in invalid_deps:
                if dep_id in skill['dependencies']:
                    skill['dependencies'].remove(dep_id)
                    self.dependencies_removed.append({
                        'skill_id': skill_id,
                        'title': skill['title'],
                        'removed': dep_id,
                        'reason': 'X-2 rule violation'
                    })

            # Check for circular dependencies
            self._check_circular_deps(skill_id)

    def _check_circular_deps(self, skill_id: str, visited: Set[str] = None, path: List[str] = None):
        """Check for circular dependencies"""
        if visited is None:
            visited = set()
            path = []

        if skill_id in visited:
            if skill_id in path:
                print(f"Circular dependency detected: {' -> '.join(path + [skill_id])}")
            return

        visited.add(skill_id)
        path.append(skill_id)

        if skill_id in self.all_skills:
            for dep_id in self.all_skills[skill_id]['dependencies']:
                self._check_circular_deps(dep_id, visited.copy(), path.copy())

    def generate_report(self) -> str:
        """Generate comprehensive analysis report"""
        report = []
        report.append("=" * 80)
        report.append("GRADE 2 CROSS-TOPIC DEPENDENCY ANALYSIS REPORT")
        report.append("=" * 80)
        report.append("")

        # Summary statistics
        report.append("SUMMARY STATISTICS")
        report.append("-" * 80)
        report.append(f"Total Grade 2 skills analyzed: {len(self.grade2_skills)}")
        report.append(f"Dependencies added: {len(self.dependencies_added)}")
        report.append(f"Dependencies removed: {len(self.dependencies_removed)}")
        report.append(f"X-2 violations fixed: {len(self.violations_fixed)}")
        report.append("")

        # Dependencies added
        if self.dependencies_added:
            report.append("DEPENDENCIES ADDED (Cross-Topic)")
            report.append("-" * 80)
            by_topic = defaultdict(list)
            for item in self.dependencies_added:
                by_topic[item['topic']].append(item)

            for topic in sorted(by_topic.keys()):
                report.append(f"\n{topic.upper()}:")
                for item in by_topic[topic]:
                    report.append(f"  {item['skill_id']}: {item['title']}")
                    for dep in item['added']:
                        if dep in self.all_skills:
                            dep_info = self.all_skills[dep]
                            report.append(f"    + {dep} ({dep_info['topic']}, G{dep_info['grade']})")
            report.append("")

        # Dependencies removed
        if self.dependencies_removed:
            report.append("DEPENDENCIES REMOVED")
            report.append("-" * 80)
            by_reason = defaultdict(list)
            for item in self.dependencies_removed:
                by_reason[item['reason']].append(item)

            for reason in sorted(by_reason.keys()):
                report.append(f"\n{reason}:")
                for item in by_reason[reason]:
                    report.append(f"  {item['skill_id']}: {item['title']}")
                    report.append(f"    - {item['removed']}")
            report.append("")

        # Violations fixed
        if self.violations_fixed:
            report.append("X-2 RULE VIOLATIONS FIXED")
            report.append("-" * 80)
            for item in self.violations_fixed:
                report.append(f"{item['skill_id']}: {item['title']}")
                report.append(f"  Removed: {item['removed']} - {item['reason']}")
            report.append("")

        return "\n".join(report)

    def apply_fixes_to_file(self):
        """Apply all fixes back to allskills.md"""
        print("\n=== APPLYING FIXES TO FILE ===")

        with open(self.file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        modifications = 0

        # For each modified Grade 2 skill, update its dependencies
        for skill_id, skill in self.grade2_skills.items():
            # Find the skill section (from ID: to next ID: or end)
            skill_pattern = rf'(ID:\s+{re.escape(skill_id)}\n.*?)(Dependencies:.*?)(?=\n\nID:|\n\n\nID:|\Z)'
            match = re.search(skill_pattern, content, re.DOTALL)

            if not match:
                # Try without Dependencies section (skill has no current dependencies)
                skill_pattern = rf'(ID:\s+{re.escape(skill_id)}\n.*?Description:[^\n]+(?:\n_[^\n]+)?)((?=\n\nID:|\n\n\nID:|\Z))'
                match = re.search(skill_pattern, content, re.DOTALL)

                if match and skill['dependencies']:
                    # Add Dependencies section
                    before_text = match.group(1)
                    after_text = match.group(2)

                    new_deps_text = "\n\nDependencies:\n" + "\n".join(
                        f"* {dep}: {self.all_skills[dep]['title']}"
                        for dep in sorted(set(skill['dependencies']))
                        if dep in self.all_skills
                    )

                    new_section = before_text + new_deps_text + after_text
                    content = content.replace(match.group(0), new_section)
                    modifications += 1
                continue

            if not match:
                print(f"Warning: Could not find skill {skill_id} in file")
                continue

            # Get the dependencies section
            before_deps = match.group(1)
            deps_section = match.group(2)

            # Build new dependencies section
            if skill['dependencies']:
                new_deps_lines = []
                for dep in sorted(set(skill['dependencies'])):
                    if dep in self.all_skills:
                        dep_title = self.all_skills[dep]['title']
                        new_deps_lines.append(f"* {dep}: {dep_title}")

                new_deps_text = "Dependencies:\n" + "\n".join(new_deps_lines)
            else:
                new_deps_text = ""

            # Replace the old section with new one
            old_section = match.group(0)
            if new_deps_text:
                new_section = before_deps + new_deps_text
            else:
                new_section = before_deps.rstrip()

            content = content.replace(old_section, new_section)
            modifications += 1

        # Write back to file
        with open(self.file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"File updated successfully ({modifications} skills modified)")

    def run(self):
        """Run the complete analysis"""
        self.parse_file()
        self.analyze_cross_topic_needs()
        self.validate_dependencies()

        # Generate report
        report = self.generate_report()
        print("\n" + report)

        # Save report
        report_path = '/media/binyu/USB2/dev/CreatiCodeSkillMap/PHASE2_G2_ANALYSIS_REPORT.md'
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"\nReport saved to: {report_path}")

        # Apply fixes
        self.apply_fixes_to_file()

        return report

if __name__ == '__main__':
    analyzer = Grade2Analyzer('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md')
    analyzer.run()
