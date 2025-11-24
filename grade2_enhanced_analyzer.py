#!/usr/bin/env python3
"""
Enhanced Grade 2 Cross-Topic Dependency Analysis
Uses keyword matching and topic relationships to find missing cross-topic dependencies
"""

import re
from collections import defaultdict
from typing import Dict, List, Set, Tuple

class EnhancedG2Analyzer:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.all_skills = {}
        self.grade2_skills = {}
        self.skills_by_topic = defaultdict(list)
        self.skills_by_grade = defaultdict(list)

        # Changes tracking
        self.dependencies_added = []
        self.dependencies_removed = []
        self.violations_fixed = []

        # Topic name normalization
        self.topic_names = {
            'T01': 'algorithms',
            'T02': 'decomposition',
            'T03': 'variables',
            'T04': 'motion',
            'T05': 'looks',
            'T06': 'randomness',
            'T07': 'events',
            'T08': 'pen',
            'T09': 'control',
            'T10': 'sensing',
            'T11': 'operators',
            'T12': 'cloning',
            'T13': 'list-operations',
            'T14': 'broadcasting',
            'T15': 'sound',
            'T16': 'video-sensing',
            'T17': 'text-to-speech',
            'T18': 'translate',
            'T19': 'custom-blocks',
            'T20': 'music',
            'T21': 'game-mechanics',
            'T22': 'animation',
            'T23': 'storytelling',
            'T24': 'art',
            'T25': 'math',
            'T26': 'science',
            'T27': 'social-studies',
            'T28': 'coordinate-systems',
            'T29': 'data-collection',
            'T30': 'debugging',
            'T31': 'user-input',
            'T32': 'sprites',
            'T33': 'backdrops',
            'T34': 'costumes',
            'T35': 'project-planning',
            'T36': 'physics-simulation'
        }

    def parse_file(self):
        """Parse allskills.md and extract all skills"""
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
                'dependencies': dependencies,
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

    def analyze_cross_topic_dependencies(self):
        """Comprehensive cross-topic dependency analysis"""
        print("\n=== CROSS-TOPIC DEPENDENCY ANALYSIS ===")

        for skill_id, skill in sorted(self.grade2_skills.items()):
            topic = skill['topic']
            title_lower = skill['title'].lower()
            desc_lower = skill['description'].lower()
            combined_text = f"{title_lower} {desc_lower}"

            current_deps = set(skill['dependencies'])
            needed_deps = set()

            # Analyze based on keywords and concepts
            needed_deps.update(self._analyze_by_keywords(combined_text, topic))
            needed_deps.update(self._analyze_by_topic_relationships(topic, combined_text))
            needed_deps.update(self._analyze_specific_cases(skill_id, skill, combined_text))

            # Filter: only cross-topic, grade 0-2, not already present
            valid_new_deps = set()
            for dep_id in needed_deps:
                if dep_id in current_deps:
                    continue
                if dep_id not in self.all_skills:
                    continue
                dep_skill = self.all_skills[dep_id]
                if dep_skill['topic'] == topic:  # Same topic, skip
                    continue
                if dep_skill['grade'] > 2:  # Too advanced
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
                print(f"  {skill_id}: +{len(valid_new_deps)} deps")

    def _analyze_by_keywords(self, text: str, current_topic: str) -> Set[str]:
        """Identify dependencies based on keyword presence"""
        deps = set()

        # Variable-related keywords
        if any(kw in text for kw in ['variable', 'score', 'counter', 'lives', 'points', 'track', 'store value']):
            deps.update(self._get_foundational_skills('T03', [0, 1]))  # Variables

        # Motion keywords
        if any(kw in text for kw in ['move', 'glide', 'go to', 'position', 'x:', 'y:', 'direction', 'turn', 'point']):
            deps.update(self._get_foundational_skills('T04', [0, 1]))  # Motion

        # Looks/appearance keywords
        if any(kw in text for kw in ['costume', 'size', 'show', 'hide', 'say', 'think', 'effect']):
            deps.update(self._get_foundational_skills('T05', [0, 1]))  # Looks

        # Events keywords
        if any(kw in text for kw in ['when clicked', 'when key', 'when backdrop', 'start', 'trigger', 'event']):
            deps.update(self._get_foundational_skills('T07', [0, 1]))  # Events

        # Control/loops keywords
        if any(kw in text for kw in ['repeat', 'forever', 'if', 'wait', 'loop', 'until']):
            deps.update(self._get_foundational_skills('T09', [0, 1]))  # Control

        # Sensing keywords
        if any(kw in text for kw in ['touching', 'mouse', 'keyboard', 'distance', 'ask', 'answer', 'detect']):
            deps.update(self._get_foundational_skills('T10', [0, 1]))  # Sensing

        # Operators/math keywords
        if any(kw in text for kw in ['add', 'subtract', 'multiply', 'divide', 'random', 'compare', '>', '<', '=']):
            deps.update(self._get_foundational_skills('T11', [0, 1]))  # Operators

        # Clone keywords
        if any(kw in text for kw in ['clone', 'copy', 'duplicate']):
            deps.update(self._get_foundational_skills('T12', [0, 1]))  # Cloning

        # List keywords
        if any(kw in text for kw in ['list', 'item', 'add to list', 'delete from list']):
            deps.update(self._get_foundational_skills('T13', [0, 1]))  # Lists

        # Broadcasting keywords
        if any(kw in text for kw in ['broadcast', 'message', 'receive']):
            deps.update(self._get_foundational_skills('T14', [0, 1]))  # Broadcasting

        # Sound keywords
        if any(kw in text for kw in ['sound', 'play', 'music', 'note', 'drum', 'volume']):
            deps.update(self._get_foundational_skills('T15', [0, 1]))  # Sound

        # Pen keywords
        if any(kw in text for kw in ['pen', 'stamp', 'draw', 'line', 'trail']):
            deps.update(self._get_foundational_skills('T08', [0, 1]))  # Pen

        return deps

    def _analyze_by_topic_relationships(self, topic: str, text: str) -> Set[str]:
        """Analyze based on known topic relationships"""
        deps = set()

        # Game mechanics need multiple foundational topics
        if topic == 'T21':  # Game mechanics
            deps.update(self._get_foundational_skills('T03', [0, 1]))  # Variables for score
            deps.update(self._get_foundational_skills('T07', [0, 1]))  # Events for control
            deps.update(self._get_foundational_skills('T09', [0, 1]))  # Control structures
            if 'collision' in text or 'touching' in text:
                deps.update(self._get_foundational_skills('T10', [0, 1]))  # Sensing

        # Animation needs motion and looks
        if topic == 'T22':  # Animation
            deps.update(self._get_foundational_skills('T04', [0, 1]))  # Motion
            deps.update(self._get_foundational_skills('T05', [0, 1]))  # Looks
            deps.update(self._get_foundational_skills('T09', [0, 1]))  # Control for timing

        # Storytelling needs multiple presentation topics
        if topic == 'T23':  # Storytelling
            deps.update(self._get_foundational_skills('T05', [0, 1]))  # Looks
            deps.update(self._get_foundational_skills('T07', [0, 1]))  # Events
            if 'sound' in text or 'say' in text:
                deps.update(self._get_foundational_skills('T15', [0, 1]))  # Sound

        # Art needs pen and looks
        if topic == 'T24':  # Art
            deps.update(self._get_foundational_skills('T08', [0, 1]))  # Pen
            deps.update(self._get_foundational_skills('T04', [0, 1]))  # Motion

        # Math/Science need variables and operators
        if topic in ['T25', 'T26']:  # Math or Science
            deps.update(self._get_foundational_skills('T03', [0, 1]))  # Variables
            deps.update(self._get_foundational_skills('T11', [0, 1]))  # Operators

        # Physics simulation needs motion, variables, operators
        if topic == 'T36':  # Physics
            deps.update(self._get_foundational_skills('T03', [0, 1]))  # Variables
            deps.update(self._get_foundational_skills('T04', [0, 1]))  # Motion
            deps.update(self._get_foundational_skills('T11', [0, 1]))  # Operators

        # Coordinate systems need motion
        if topic == 'T28':  # Coordinate systems
            deps.update(self._get_foundational_skills('T04', [0, 1]))  # Motion

        # User input needs sensing
        if topic == 'T31':  # User input
            deps.update(self._get_foundational_skills('T10', [0, 1]))  # Sensing

        return deps

    def _analyze_specific_cases(self, skill_id: str, skill: Dict, text: str) -> Set[str]:
        """Handle specific skill cases that need particular dependencies"""
        deps = set()
        topic = skill['topic']

        # Algorithms (T01) at G2 should know about basic Scratch blocks
        if topic == 'T01':
            if 'block' in text or 'scratch' in text or 'code' in text:
                deps.update(self._get_foundational_skills('T04', [0]))  # Basic motion
                deps.update(self._get_foundational_skills('T05', [0]))  # Basic looks

        # Decomposition (T02) should understand basic program structure
        if topic == 'T02':
            deps.update(self._get_foundational_skills('T07', [0]))  # Events (program start)

        # Any skill involving "repeat" or loops
        if 'repeat' in text or 'loop' in text or 'forever' in text:
            deps.update(self._get_foundational_skills('T09', [0, 1]))  # Control

        # Any skill involving randomness
        if 'random' in text:
            deps.update(self._get_foundational_skills('T06', [0, 1]))  # Randomness

        # Sprite-related skills need sprite basics
        if topic == 'T32' or 'sprite' in text:
            deps.update(self._get_foundational_skills('T04', [0]))  # Motion (sprite movement)
            deps.update(self._get_foundational_skills('T05', [0]))  # Looks (sprite appearance)

        return deps

    def _get_foundational_skills(self, topic: str, grades: List[int]) -> Set[str]:
        """Get foundational skills from a topic at specific grades"""
        skills = set()
        for skill_id in self.skills_by_topic.get(topic, []):
            if self.all_skills[skill_id]['grade'] in grades:
                skills.add(skill_id)
        return skills

    def _determine_reason(self, text: str, deps: Set[str]) -> str:
        """Determine a concise reason for adding dependencies"""
        dep_topics = set()
        for dep_id in deps:
            if dep_id in self.all_skills:
                dep_topics.add(self.all_skills[dep_id]['topic'])

        topic_names = [self.topic_names.get(t, t) for t in sorted(dep_topics)]
        return f"Cross-topic prerequisites: {', '.join(topic_names)}"

    def validate_dependencies(self):
        """Validate X-2 rule and circular dependencies"""
        print("\n=== DEPENDENCY VALIDATION ===")

        for skill_id, skill in self.grade2_skills.items():
            deps_to_remove = []

            for dep_id in skill['dependencies'][:]:
                if dep_id not in self.all_skills:
                    print(f"  Warning: {skill_id} depends on non-existent {dep_id}")
                    deps_to_remove.append(dep_id)
                    continue

                dep_grade = self.all_skills[dep_id]['grade']
                if dep_grade > 2:  # X-2 violation
                    deps_to_remove.append(dep_id)
                    self.violations_fixed.append({
                        'skill_id': skill_id,
                        'title': skill['title'],
                        'removed': dep_id,
                        'reason': f'X-2 violation (grade {dep_grade} > 2)'
                    })

            for dep_id in deps_to_remove:
                if dep_id in skill['dependencies']:
                    skill['dependencies'].remove(dep_id)
                    self.dependencies_removed.append({
                        'skill_id': skill_id,
                        'title': skill['title'],
                        'removed': dep_id,
                        'reason': 'X-2 rule violation'
                    })

        print(f"  Fixed {len(self.violations_fixed)} X-2 violations")

    def generate_report(self) -> str:
        """Generate comprehensive report"""
        report = []
        report.append("=" * 80)
        report.append("PHASE 2: GRADE 2 CROSS-TOPIC DEPENDENCY ANALYSIS")
        report.append("=" * 80)
        report.append("")

        report.append("SUMMARY")
        report.append("-" * 80)
        report.append(f"Total Grade 2 skills analyzed: {len(self.grade2_skills)}")
        report.append(f"Cross-topic dependencies added: {len(self.dependencies_added)}")
        report.append(f"Dependencies removed (violations): {len(self.dependencies_removed)}")
        report.append(f"X-2 rule violations fixed: {len(self.violations_fixed)}")
        report.append("")

        if self.dependencies_added:
            report.append("CROSS-TOPIC DEPENDENCIES ADDED")
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
                            report.append(f"      + {dep} (G{dep_skill['grade']}, {dep_topic_name})")
            report.append("")

        if self.violations_fixed:
            report.append("VIOLATIONS FIXED")
            report.append("-" * 80)
            for item in self.violations_fixed:
                report.append(f"  {item['skill_id']}: Removed {item['removed']} ({item['reason']})")
            report.append("")

        return "\n".join(report)

    def apply_fixes_to_file(self):
        """Apply fixes to allskills.md"""
        print("\n=== APPLYING FIXES ===")

        with open(self.file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        modified = 0

        for skill_id, skill in self.grade2_skills.items():
            # Find skill section
            pattern = rf'(ID:\s+{re.escape(skill_id)}\n.*?)(Dependencies:.*?)(?=\n\nID:|\n\n\nID:|\Z)'
            match = re.search(pattern, content, re.DOTALL)

            if not match:
                # No dependencies section, try to add one
                pattern = rf'(ID:\s+{re.escape(skill_id)}\n.*?Description:[^\n]+(?:\n_[^\n]+)?)((?=\n\nID:|\n\n\nID:|\Z))'
                match = re.search(pattern, content, re.DOTALL)

                if match and skill['dependencies']:
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

        with open(self.file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  Updated {modified} skills in file")

    def run(self):
        """Run complete analysis"""
        self.parse_file()
        self.analyze_cross_topic_dependencies()
        self.validate_dependencies()

        report = self.generate_report()
        print("\n" + report)

        report_path = '/media/binyu/USB2/dev/CreatiCodeSkillMap/PHASE2_G2_COMPREHENSIVE_REPORT.md'
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"\nReport saved to: {report_path}")

        self.apply_fixes_to_file()

        return report

if __name__ == '__main__':
    analyzer = EnhancedG2Analyzer('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md')
    analyzer.run()
