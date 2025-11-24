#!/usr/bin/env python3
"""
Comprehensive Grade K Skills Analyzer
Analyzes ALL Grade K skills across all 36 topics for dependencies, violations, and cross-topic relationships
"""

import re
from collections import defaultdict
from typing import Dict, List, Set, Tuple

class GradeKAnalyzer:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.all_skills = {}  # skill_id -> skill_data
        self.grade_k_skills = {}  # skill_id -> skill_data
        self.topics = defaultdict(list)  # topic_id -> [skill_ids]
        self.dependencies = defaultdict(list)  # skill_id -> [dependency_ids]
        self.reverse_deps = defaultdict(list)  # skill_id -> [skills_that_depend_on_it]

    def parse_file(self):
        """Parse the entire allskills.md file"""
        with open(self.file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Split by skill blocks (ID: pattern)
        skill_blocks = re.split(r'\n(?=ID: T\d+\.)', content)

        for block in skill_blocks:
            if not block.strip() or not block.startswith('ID:'):
                continue

            skill_data = self._parse_skill_block(block)
            if skill_data:
                skill_id = skill_data['id']
                self.all_skills[skill_id] = skill_data

                # Extract topic
                topic_id = skill_id.split('.')[0]
                self.topics[topic_id].append(skill_id)

                # If Grade K, add to grade_k_skills
                if '.GK.' in skill_id:
                    self.grade_k_skills[skill_id] = skill_data

                # Parse dependencies
                deps = skill_data.get('dependencies', [])
                self.dependencies[skill_id] = deps
                for dep_id in deps:
                    self.reverse_deps[dep_id].append(skill_id)

    def _parse_skill_block(self, block: str) -> Dict:
        """Parse a single skill block"""
        lines = block.strip().split('\n')
        skill_data = {}

        # Parse ID
        id_match = re.search(r'ID:\s*(T\d+\.[A-Z0-9]+\.\d+)', block)
        if id_match:
            skill_data['id'] = id_match.group(1)
        else:
            return None

        # Parse Topic
        topic_match = re.search(r'Topic:\s*(.+)', block)
        if topic_match:
            skill_data['topic'] = topic_match.group(1).strip()

        # Parse Skill name
        skill_match = re.search(r'Skill:\s*(.+)', block)
        if skill_match:
            skill_data['skill'] = skill_match.group(1).strip()

        # Parse Description
        desc_match = re.search(r'Description:\s*(.+?)(?=\n\n|Dependencies:|$)', block, re.DOTALL)
        if desc_match:
            skill_data['description'] = desc_match.group(1).strip()

        # Parse Dependencies
        deps = []
        dep_section = re.search(r'Dependencies:\s*\n((?:\*.*\n?)+)', block)
        if dep_section:
            dep_lines = dep_section.group(1).strip().split('\n')
            for line in dep_lines:
                dep_match = re.search(r'\*\s*(T\d+\.[A-Z0-9]+\.\d+)', line)
                if dep_match:
                    deps.append(dep_match.group(1))
        skill_data['dependencies'] = deps

        return skill_data

    def analyze_x2_violations(self) -> List[Dict]:
        """Find X-2 rule violations (Grade K can only depend on Grade K)"""
        violations = []

        for skill_id, skill_data in self.grade_k_skills.items():
            deps = self.dependencies.get(skill_id, [])
            for dep_id in deps:
                if '.GK.' not in dep_id:
                    violations.append({
                        'skill': skill_id,
                        'skill_name': skill_data.get('skill', ''),
                        'invalid_dep': dep_id,
                        'invalid_dep_name': self.all_skills.get(dep_id, {}).get('skill', 'UNKNOWN'),
                        'reason': f'Grade K skill depends on {self._get_grade(dep_id)} skill'
                    })

        return violations

    def _get_grade(self, skill_id: str) -> str:
        """Extract grade from skill ID"""
        match = re.search(r'\.([A-Z0-9]+)\.', skill_id)
        if match:
            return match.group(1)
        return 'UNKNOWN'

    def find_circular_dependencies(self) -> List[List[str]]:
        """Find circular dependencies in Grade K skills"""
        cycles = []
        visited = set()
        rec_stack = set()

        def dfs(skill_id: str, path: List[str]) -> None:
            visited.add(skill_id)
            rec_stack.add(skill_id)
            path.append(skill_id)

            for dep_id in self.dependencies.get(skill_id, []):
                if '.GK.' not in dep_id:  # Only check within Grade K
                    continue

                if dep_id not in visited:
                    dfs(dep_id, path.copy())
                elif dep_id in rec_stack:
                    # Found a cycle
                    cycle_start = path.index(dep_id)
                    cycle = path[cycle_start:] + [dep_id]
                    if cycle not in cycles:
                        cycles.append(cycle)

            rec_stack.remove(skill_id)

        for skill_id in self.grade_k_skills:
            if skill_id not in visited:
                dfs(skill_id, [])

        return cycles

    def identify_cross_topic_relationships(self) -> Dict:
        """Identify existing and missing cross-topic dependencies"""
        cross_topic = {
            'existing': [],
            'missing': []
        }

        # Existing cross-topic deps
        for skill_id in self.grade_k_skills:
            skill_topic = skill_id.split('.')[0]
            deps = self.dependencies.get(skill_id, [])

            for dep_id in deps:
                if '.GK.' not in dep_id:
                    continue
                dep_topic = dep_id.split('.')[0]
                if dep_topic != skill_topic:
                    cross_topic['existing'].append({
                        'from': skill_id,
                        'from_topic': skill_topic,
                        'to': dep_id,
                        'to_topic': dep_topic,
                        'from_name': self.grade_k_skills[skill_id].get('skill', ''),
                        'to_name': self.grade_k_skills.get(dep_id, {}).get('skill', '')
                    })

        # Analyze for missing cross-topic dependencies
        cross_topic['missing'] = self._suggest_missing_cross_topic_deps()

        return cross_topic

    def _suggest_missing_cross_topic_deps(self) -> List[Dict]:
        """Suggest missing cross-topic dependencies based on skill content"""
        suggestions = []

        # Keywords that indicate potential dependencies
        dependency_keywords = {
            'loop': ['T04'],  # Patterns & Loops
            'repeat': ['T04'],
            'variable': ['T09'],  # Variables
            'event': ['T16'],  # Events
            'click': ['T16'],
            'touch': ['T16'],
            'sprite': ['T02', 'T03'],  # Motion, Graphics
            'move': ['T02'],
            'position': ['T02'],
            'coordinate': ['T02'],
            'shape': ['T03'],
            'color': ['T03'],
            'draw': ['T03'],
            'animation': ['T10'],  # Animation
            'sound': ['T11'],  # Sound
            'costume': ['T10'],
            'backdrop': ['T03'],
            'conditional': ['T06'],  # Conditionals
            'if': ['T06'],
            'question': ['T08'],  # Input
            'answer': ['T08'],
            'input': ['T08'],
            'message': ['T17'],  # Messages
            'broadcast': ['T17'],
            'clone': ['T18'],  # Clones
            'function': ['T20'],  # Functions
            'block': ['T20'],
            'list': ['T12'],  # Lists
            'array': ['T12'],
        }

        for skill_id, skill_data in self.grade_k_skills.items():
            skill_topic = skill_id.split('.')[0]
            skill_text = (skill_data.get('skill', '') + ' ' + skill_data.get('description', '')).lower()
            current_deps = set(self.dependencies.get(skill_id, []))

            # Check for keyword matches
            for keyword, potential_topics in dependency_keywords.items():
                if keyword in skill_text:
                    for topic in potential_topics:
                        if topic != skill_topic:
                            # Check if there's any dependency from that topic
                            has_dep_from_topic = any(dep.startswith(f'{topic}.GK.') for dep in current_deps)

                            if not has_dep_from_topic:
                                # Find fundamental skills from that topic
                                topic_skills = [s for s in self.topics[topic] if '.GK.' in s]
                                if topic_skills:
                                    suggestions.append({
                                        'skill': skill_id,
                                        'skill_name': skill_data.get('skill', ''),
                                        'keyword': keyword,
                                        'suggested_topic': topic,
                                        'reason': f'Skill mentions "{keyword}" but has no dependencies from {topic}',
                                        'candidate_deps': topic_skills[:3]  # First 3 skills from topic
                                    })

        return suggestions

    def find_redundant_transitive_deps(self) -> List[Dict]:
        """Find truly redundant transitive dependencies (conservative approach)"""
        redundant = []

        for skill_id in self.grade_k_skills:
            deps = set(self.dependencies.get(skill_id, []))

            for dep in list(deps):
                if '.GK.' not in dep:
                    continue

                # Check if this dep is reachable through other direct deps
                other_deps = deps - {dep}

                # Get all transitive deps from other direct deps
                transitive_from_others = set()
                for other_dep in other_deps:
                    if '.GK.' in other_dep:
                        transitive_from_others.update(self._get_all_transitive_deps(other_dep))

                # If dep is in transitive set, it might be redundant
                if dep in transitive_from_others:
                    # Be conservative: only mark as redundant if there's a clear path
                    paths = self._find_paths(skill_id, dep, exclude_direct=True)
                    if paths:
                        redundant.append({
                            'skill': skill_id,
                            'skill_name': self.grade_k_skills[skill_id].get('skill', ''),
                            'redundant_dep': dep,
                            'dep_name': self.grade_k_skills.get(dep, {}).get('skill', ''),
                            'reason': f'Reachable through: {" -> ".join(paths[0])}',
                            'paths': paths
                        })

        return redundant

    def _get_all_transitive_deps(self, skill_id: str, visited: Set[str] = None) -> Set[str]:
        """Get all transitive dependencies of a skill"""
        if visited is None:
            visited = set()

        if skill_id in visited:
            return set()

        visited.add(skill_id)
        transitive = set()

        for dep in self.dependencies.get(skill_id, []):
            if '.GK.' in dep:
                transitive.add(dep)
                transitive.update(self._get_all_transitive_deps(dep, visited))

        return transitive

    def _find_paths(self, start: str, target: str, exclude_direct: bool = False,
                    path: List[str] = None, visited: Set[str] = None) -> List[List[str]]:
        """Find all paths from start to target"""
        if path is None:
            path = [start]
        if visited is None:
            visited = set()

        if start in visited:
            return []

        visited.add(start)
        paths = []

        for dep in self.dependencies.get(start, []):
            if '.GK.' not in dep:
                continue

            # Skip direct dependency if requested
            if exclude_direct and start == path[0] and dep == target:
                continue

            if dep == target:
                paths.append(path + [dep])
            else:
                sub_paths = self._find_paths(dep, target, False, path + [dep], visited.copy())
                paths.extend(sub_paths)

        return paths

    def generate_report(self) -> str:
        """Generate comprehensive analysis report"""
        report = []
        report.append("=" * 100)
        report.append("COMPREHENSIVE GRADE K SKILLS ANALYSIS")
        report.append("=" * 100)
        report.append("")

        # Summary statistics
        report.append("## SUMMARY STATISTICS")
        report.append("=" * 100)
        report.append(f"Total skills in file: {len(self.all_skills)}")
        report.append(f"Total Grade K skills: {len(self.grade_k_skills)}")
        report.append(f"Topics with Grade K skills: {len([t for t in self.topics if any('.GK.' in s for s in self.topics[t])])}")
        report.append("")

        # List all Grade K skills by topic
        report.append("## ALL GRADE K SKILLS BY TOPIC")
        report.append("=" * 100)

        for topic_id in sorted(self.topics.keys()):
            topic_gk_skills = [s for s in self.topics[topic_id] if '.GK.' in s]
            if topic_gk_skills:
                report.append(f"\n### {topic_id} ({len(topic_gk_skills)} Grade K skills)")
                report.append("-" * 80)
                for skill_id in topic_gk_skills:
                    skill = self.grade_k_skills[skill_id]
                    deps = self.dependencies.get(skill_id, [])
                    report.append(f"\n{skill_id}: {skill.get('skill', 'N/A')}")
                    if deps:
                        report.append(f"  Dependencies ({len(deps)}):")
                        for dep in deps:
                            dep_name = self.all_skills.get(dep, {}).get('skill', 'UNKNOWN')
                            report.append(f"    - {dep} ({dep_name})")
                    else:
                        report.append(f"  Dependencies: None")

        report.append("\n\n")

        # X-2 Rule Violations
        report.append("## X-2 RULE VIOLATIONS")
        report.append("=" * 100)
        violations = self.analyze_x2_violations()
        if violations:
            report.append(f"Found {len(violations)} violations where Grade K skills depend on higher grade skills:")
            report.append("")
            for v in violations:
                report.append(f"VIOLATION: {v['skill']} ({v['skill_name']})")
                report.append(f"  -> Depends on: {v['invalid_dep']} ({v['invalid_dep_name']})")
                report.append(f"  -> Reason: {v['reason']}")
                report.append("")
        else:
            report.append("No X-2 rule violations found!")

        report.append("")

        # Circular Dependencies
        report.append("## CIRCULAR DEPENDENCIES")
        report.append("=" * 100)
        cycles = self.find_circular_dependencies()
        if cycles:
            report.append(f"Found {len(cycles)} circular dependency chains:")
            report.append("")
            for i, cycle in enumerate(cycles, 1):
                report.append(f"Cycle {i}: {' -> '.join(cycle)}")
                report.append("")
        else:
            report.append("No circular dependencies found!")

        report.append("")

        # Cross-Topic Relationships
        report.append("## CROSS-TOPIC DEPENDENCIES")
        report.append("=" * 100)
        cross_topic = self.identify_cross_topic_relationships()

        report.append(f"\n### EXISTING Cross-Topic Dependencies ({len(cross_topic['existing'])})")
        report.append("-" * 80)
        if cross_topic['existing']:
            # Group by source topic
            by_topic = defaultdict(list)
            for rel in cross_topic['existing']:
                by_topic[rel['from_topic']].append(rel)

            for topic in sorted(by_topic.keys()):
                report.append(f"\nFrom {topic}:")
                for rel in by_topic[topic]:
                    report.append(f"  {rel['from']} ({rel['from_name']})")
                    report.append(f"    -> {rel['to']} ({rel['to_name']}) [{rel['to_topic']}]")
        else:
            report.append("No cross-topic dependencies found!")

        report.append(f"\n\n### SUGGESTED Missing Cross-Topic Dependencies ({len(cross_topic['missing'])})")
        report.append("-" * 80)
        if cross_topic['missing']:
            # Group by topic
            by_topic = defaultdict(list)
            for sug in cross_topic['missing']:
                by_topic[sug['skill'].split('.')[0]].append(sug)

            for topic in sorted(by_topic.keys()):
                report.append(f"\n{topic}:")
                for sug in by_topic[topic]:
                    report.append(f"  {sug['skill']} ({sug['skill_name']})")
                    report.append(f"    Reason: {sug['reason']}")
                    report.append(f"    Suggested candidates from {sug['suggested_topic']}:")
                    for cand in sug['candidate_deps']:
                        cand_name = self.grade_k_skills.get(cand, {}).get('skill', 'N/A')
                        report.append(f"      - {cand} ({cand_name})")
                    report.append("")
        else:
            report.append("No missing cross-topic dependencies identified!")

        report.append("")

        # Redundant Transitive Dependencies
        report.append("## POTENTIALLY REDUNDANT TRANSITIVE DEPENDENCIES")
        report.append("=" * 100)
        redundant = self.find_redundant_transitive_deps()
        if redundant:
            report.append(f"Found {len(redundant)} potentially redundant dependencies:")
            report.append("(These are already reachable through other paths - consider removing only if truly transitive)")
            report.append("")
            for r in redundant:
                report.append(f"Skill: {r['skill']} ({r['skill_name']})")
                report.append(f"  Redundant dep: {r['redundant_dep']} ({r['dep_name']})")
                report.append(f"  Reason: {r['reason']}")
                report.append("")
        else:
            report.append("No redundant transitive dependencies found!")

        report.append("")

        # Specific Recommendations
        report.append("## SPECIFIC RECOMMENDATIONS FOR EACH SKILL NEEDING CHANGES")
        report.append("=" * 100)

        skills_needing_changes = set()

        # Add skills with violations
        for v in violations:
            skills_needing_changes.add(v['skill'])

        # Add skills with missing cross-topic deps
        for sug in cross_topic['missing']:
            skills_needing_changes.add(sug['skill'])

        # Add skills with redundant deps (conservative)
        for r in redundant:
            skills_needing_changes.add(r['skill'])

        if skills_needing_changes:
            report.append(f"Total skills needing changes: {len(skills_needing_changes)}")
            report.append("")

            for skill_id in sorted(skills_needing_changes):
                skill_data = self.grade_k_skills.get(skill_id)
                if not skill_data:
                    continue

                report.append(f"\n{skill_id}: {skill_data.get('skill', 'N/A')}")
                report.append("-" * 80)

                # Current dependencies
                current_deps = self.dependencies.get(skill_id, [])
                report.append(f"Current dependencies: {len(current_deps)}")
                for dep in current_deps:
                    dep_name = self.all_skills.get(dep, {}).get('skill', 'UNKNOWN')
                    report.append(f"  - {dep} ({dep_name})")

                report.append("")
                report.append("Recommended changes:")

                # Check for violations
                skill_violations = [v for v in violations if v['skill'] == skill_id]
                if skill_violations:
                    report.append("  REMOVE (X-2 violations):")
                    for v in skill_violations:
                        report.append(f"    - {v['invalid_dep']} ({v['invalid_dep_name']}) - {v['reason']}")

                # Check for missing deps
                skill_suggestions = [s for s in cross_topic['missing'] if s['skill'] == skill_id]
                if skill_suggestions:
                    report.append("  ADD (suggested cross-topic):")
                    for sug in skill_suggestions:
                        report.append(f"    - Consider adding dependency from {sug['suggested_topic']} (reason: {sug['reason']})")
                        for cand in sug['candidate_deps']:
                            cand_name = self.grade_k_skills.get(cand, {}).get('skill', 'N/A')
                            report.append(f"      Option: {cand} ({cand_name})")

                # Check for redundant deps
                skill_redundant = [r for r in redundant if r['skill'] == skill_id]
                if skill_redundant:
                    report.append("  CONSIDER REMOVING (transitive redundancy):")
                    for r in skill_redundant:
                        report.append(f"    - {r['redundant_dep']} ({r['dep_name']}) - {r['reason']}")

                report.append("")
        else:
            report.append("All Grade K skills are properly structured!")

        report.append("")
        report.append("=" * 100)
        report.append("END OF ANALYSIS")
        report.append("=" * 100)

        return '\n'.join(report)

def main():
    analyzer = GradeKAnalyzer('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md')

    print("Parsing file...")
    analyzer.parse_file()

    print("Generating comprehensive analysis...")
    report = analyzer.generate_report()

    # Save report
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/comprehensive_grade_k_analysis.md'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"Analysis complete! Report saved to: {output_file}")
    print(f"\nTotal Grade K skills analyzed: {len(analyzer.grade_k_skills)}")
    print(f"Total topics: {len([t for t in analyzer.topics if any('.GK.' in s for s in analyzer.topics[t])])}")

    # Print summary stats
    violations = analyzer.analyze_x2_violations()
    cycles = analyzer.find_circular_dependencies()
    cross_topic = analyzer.identify_cross_topic_relationships()
    redundant = analyzer.find_redundant_transitive_deps()

    print(f"\nX-2 violations: {len(violations)}")
    print(f"Circular dependencies: {len(cycles)}")
    print(f"Existing cross-topic deps: {len(cross_topic['existing'])}")
    print(f"Suggested missing cross-topic deps: {len(cross_topic['missing'])}")
    print(f"Potentially redundant deps: {len(redundant)}")

if __name__ == '__main__':
    main()
