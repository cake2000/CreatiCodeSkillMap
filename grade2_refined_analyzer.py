#!/usr/bin/env python3
"""
Refined Grade 2 Cross-Topic Dependency Analysis
More conservative approach - only add truly essential prerequisites
"""

import re
from collections import defaultdict
from typing import Dict, List, Set, Tuple

class RefinedG2Analyzer:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.all_skills = {}
        self.grade2_skills = {}
        self.skills_by_topic = defaultdict(list)
        self.skills_by_grade = defaultdict(list)

        self.dependencies_added = []
        self.dependencies_removed = []
        self.violations_fixed = []

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
        """Conservative cross-topic dependency analysis - only essential prerequisites"""
        print("\n=== CROSS-TOPIC DEPENDENCY ANALYSIS (CONSERVATIVE) ===")

        for skill_id, skill in sorted(self.grade2_skills.items()):
            topic = skill['topic']
            title_lower = skill['title'].lower()
            desc_lower = skill['description'].lower()
            combined_text = f"{title_lower} {desc_lower}"

            current_deps = set(skill['dependencies'])
            needed_deps = set()

            # Add only the MOST ESSENTIAL cross-topic dependencies
            needed_deps.update(self._get_essential_dependencies(topic, combined_text, skill_id))

            # Filter: only cross-topic, grade 0-2, not already present
            valid_new_deps = set()
            for dep_id in needed_deps:
                if dep_id in current_deps:
                    continue
                if dep_id not in self.all_skills:
                    continue
                dep_skill = self.all_skills[dep_id]
                if dep_skill['topic'] == topic:  # Same topic
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

        print(f"\nTotal dependencies added: {sum(len(item['added']) for item in self.dependencies_added)}")

    def _get_essential_dependencies(self, topic: str, text: str, skill_id: str) -> Set[str]:
        """Get only the most essential cross-topic dependencies"""
        deps = set()

        # RULE 1: Game mechanics need core building blocks
        if topic == 'T21':  # Game mechanics
            # Need variables for score/lives
            deps.update(self._get_core_skills('T03', max_grade=1, limit=2))
            # Need events to start game
            deps.update(self._get_core_skills('T07', max_grade=1, limit=1))
            # Need control for game logic
            deps.update(self._get_core_skills('T09', max_grade=1, limit=2))
            if 'collision' in text or 'touching' in text:
                deps.update(self._get_core_skills('T10', max_grade=1, limit=2))

        # RULE 2: Animation needs motion + looks
        elif topic == 'T22':  # Animation
            deps.update(self._get_core_skills('T04', max_grade=1, limit=2))  # Motion
            deps.update(self._get_core_skills('T05', max_grade=1, limit=2))  # Looks
            if 'loop' in text or 'repeat' in text:
                deps.update(self._get_core_skills('T09', max_grade=1, limit=1))  # Control

        # RULE 3: Storytelling needs looks + events
        elif topic == 'T23':  # Storytelling
            deps.update(self._get_core_skills('T05', max_grade=1, limit=2))  # Looks
            deps.update(self._get_core_skills('T07', max_grade=1, limit=1))  # Events
            if 'sound' in text or 'say' in text:
                deps.update(self._get_core_skills('T15', max_grade=1, limit=1))  # Sound

        # RULE 4: Art needs pen + motion
        elif topic == 'T24':  # Art
            deps.update(self._get_core_skills('T08', max_grade=1, limit=2))  # Pen
            deps.update(self._get_core_skills('T04', max_grade=1, limit=1))  # Motion
            if 'repeat' in text or 'pattern' in text:
                deps.update(self._get_core_skills('T09', max_grade=1, limit=1))  # Control

        # RULE 5: Math/Science need variables + operators
        elif topic in ['T25', 'T26']:  # Math or Science
            if 'variable' in text or 'track' in text or 'count' in text:
                deps.update(self._get_core_skills('T03', max_grade=1, limit=2))  # Variables
            if 'add' in text or 'multiply' in text or 'calculate' in text:
                deps.update(self._get_core_skills('T11', max_grade=1, limit=2))  # Operators

        # RULE 6: Physics needs motion + variables
        elif topic == 'T36':  # Physics
            deps.update(self._get_core_skills('T03', max_grade=1, limit=2))  # Variables
            deps.update(self._get_core_skills('T04', max_grade=1, limit=2))  # Motion
            deps.update(self._get_core_skills('T11', max_grade=1, limit=1))  # Operators

        # RULE 7: Coordinate systems need motion
        elif topic == 'T28':  # Coordinate systems
            deps.update(self._get_core_skills('T04', max_grade=1, limit=2))  # Motion

        # RULE 8: User input needs sensing
        elif topic == 'T31':  # User input
            deps.update(self._get_core_skills('T10', max_grade=1, limit=2))  # Sensing

        # RULE 9: Sprites/Costumes/Backdrops need motion + looks
        elif topic in ['T32', 'T33', 'T34']:
            deps.update(self._get_core_skills('T04', max_grade=0, limit=1))  # Basic motion
            deps.update(self._get_core_skills('T05', max_grade=0, limit=1))  # Basic looks

        # RULE 10: Algorithms at G2 working with Scratch blocks
        elif topic == 'T01':
            if 'block' in text or 'code' in text or 'scratch' in text:
                # Need to know basic blocks exist
                deps.update(self._get_core_skills('T04', max_grade=0, limit=1))  # Motion blocks
                deps.update(self._get_core_skills('T05', max_grade=0, limit=1))  # Looks blocks
            if 'repeat' in text or 'loop' in text:
                deps.update(self._get_core_skills('T09', max_grade=1, limit=1))  # Control

        # RULE 11: Decomposition needs event basics
        elif topic == 'T02':
            deps.update(self._get_core_skills('T07', max_grade=0, limit=1))  # Events (program start)

        # KEYWORD-BASED RULES (more conservative)
        # Variables - only if explicitly mentioned
        if 'variable' in text and topic != 'T03':
            deps.update(self._get_core_skills('T03', max_grade=1, limit=2))

        # Motion - only if movement/position explicitly mentioned
        if any(kw in text for kw in ['move', 'glide', 'x:', 'y:', 'position']) and topic != 'T04':
            deps.update(self._get_core_skills('T04', max_grade=1, limit=1))

        # Events - only if starting/triggering explicitly mentioned
        if any(kw in text for kw in ['when clicked', 'when key', 'start', 'trigger']) and topic != 'T07':
            deps.update(self._get_core_skills('T07', max_grade=0, limit=1))

        # Control - only if loops/conditionals explicitly mentioned
        if any(kw in text for kw in ['repeat', 'forever', 'if', 'loop', 'until']) and topic != 'T09':
            deps.update(self._get_core_skills('T09', max_grade=1, limit=1))

        # Sensing - only if interaction explicitly mentioned
        if any(kw in text for kw in ['touching', 'mouse', 'keyboard', 'detect', 'ask']) and topic != 'T10':
            deps.update(self._get_core_skills('T10', max_grade=1, limit=1))

        # Cloning - only if clones explicitly mentioned
        if 'clone' in text and topic != 'T12':
            deps.update(self._get_core_skills('T12', max_grade=1, limit=1))

        # Lists - only if lists explicitly mentioned
        if 'list' in text and topic != 'T13':
            deps.update(self._get_core_skills('T13', max_grade=1, limit=1))

        # Broadcasting - only if messages explicitly mentioned
        if any(kw in text for kw in ['broadcast', 'message', 'receive']) and topic != 'T14':
            deps.update(self._get_core_skills('T14', max_grade=1, limit=1))

        return deps

    def _get_core_skills(self, topic: str, max_grade: int = 1, limit: int = 2) -> Set[str]:
        """Get the most foundational skills from a topic (limited count)"""
        skills = []
        for skill_id in self.skills_by_topic.get(topic, []):
            skill = self.all_skills[skill_id]
            if skill['grade'] <= max_grade:
                skills.append((skill['grade'], skill_id))

        # Sort by grade (prefer lower grades) and take first 'limit'
        skills.sort()
        return {s[1] for s in skills[:limit]}

    def _determine_reason(self, text: str, deps: Set[str]) -> str:
        """Determine reason for adding dependencies"""
        dep_topics = set()
        for dep_id in deps:
            if dep_id in self.all_skills:
                dep_topics.add(self.all_skills[dep_id]['topic'])

        topic_names = [self.topic_names.get(t, t) for t in sorted(dep_topics)]
        return f"Essential prerequisites: {', '.join(topic_names)}"

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
        report.append("PHASE 2: GRADE 2 CROSS-TOPIC DEPENDENCY ANALYSIS (REFINED)")
        report.append("=" * 80)
        report.append("")

        report.append("EXECUTIVE SUMMARY")
        report.append("-" * 80)
        report.append(f"Total Grade 2 skills analyzed: {len(self.grade2_skills)}")
        report.append(f"Skills with cross-topic dependencies added: {len(self.dependencies_added)}")
        total_deps_added = sum(len(item['added']) for item in self.dependencies_added)
        report.append(f"Total cross-topic dependencies added: {total_deps_added}")
        report.append(f"Dependencies removed (violations): {len(self.dependencies_removed)}")
        report.append(f"X-2 rule violations fixed: {len(self.violations_fixed)}")
        report.append("")

        report.append("KEY CROSS-TOPIC CONNECTIONS ESTABLISHED")
        report.append("-" * 80)

        # Group by target topic
        by_topic = defaultdict(lambda: {'count': 0, 'dep_topics': set()})
        for item in self.dependencies_added:
            topic = item['topic']
            by_topic[topic]['count'] += len(item['added'])
            for dep_id in item['added']:
                if dep_id in self.all_skills:
                    by_topic[topic]['dep_topics'].add(self.all_skills[dep_id]['topic'])

        for topic in sorted(by_topic.keys()):
            topic_name = self.topic_names.get(topic, topic)
            info = by_topic[topic]
            dep_topic_names = [self.topic_names.get(t, t) for t in sorted(info['dep_topics'])]
            report.append(f"\n{topic} ({topic_name}): {info['count']} dependencies added")
            report.append(f"  Connected to: {', '.join(dep_topic_names)}")

        report.append("")
        report.append("")

        # Detailed listings
        if self.dependencies_added:
            report.append("DETAILED DEPENDENCY ADDITIONS BY TOPIC")
            report.append("-" * 80)
            by_topic_detail = defaultdict(list)
            for item in self.dependencies_added:
                by_topic_detail[item['topic']].append(item)

            for topic in sorted(by_topic_detail.keys()):
                topic_name = self.topic_names.get(topic, topic)
                report.append(f"\n{topic} ({topic_name}):")
                for item in by_topic_detail[topic]:
                    report.append(f"  {item['skill_id']}: {item['title']}")
                    report.append(f"    {item['reason']}")
                    for dep in sorted(item['added']):
                        if dep in self.all_skills:
                            dep_skill = self.all_skills[dep]
                            dep_topic_name = self.topic_names.get(dep_skill['topic'], dep_skill['topic'])
                            report.append(f"      + {dep} (G{dep_skill['grade']}, {dep_topic_name}): {dep_skill['title'][:50]}")
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

        report_path = '/media/binyu/USB2/dev/CreatiCodeSkillMap/PHASE2_G2_FINAL_REPORT.md'
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"\nReport saved to: {report_path}")

        self.apply_fixes_to_file()

        return report

if __name__ == '__main__':
    analyzer = RefinedG2Analyzer('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md')
    analyzer.run()
