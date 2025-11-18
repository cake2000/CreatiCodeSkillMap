#!/usr/bin/env python3
"""
Comprehensive Dependency Enrichment for K-8 CreatiCode Skill Map

This script systematically enriches dependencies for all 1,155 skills
following the analysis framework to create a world-class dependency map.
"""

import json
import re
from typing import List, Dict, Set
from collections import defaultdict

class DependencyEnricher:
    def __init__(self, skills_file: str):
        with open(skills_file, 'r') as f:
            self.skills = json.load(f)

        # Build lookup indices
        self.skill_by_id = {s['id']: s for s in self.skills}
        self.skills_by_topic_grade = defaultdict(list)

        for skill in self.skills:
            key = (skill['topic_id'], skill['grade'])
            self.skills_by_topic_grade[key].append(skill)

        # Track enrichment statistics
        self.stats = {
            'original_deps': sum(len(s.get('dependencies', [])) for s in self.skills),
            'added_deps': 0,
            'by_topic': defaultdict(int),
            'by_grade': defaultdict(int)
        }

    def get_prerequisite_skills(self, topic_id: str, max_grade: int,
                                exclude_id: str = None) -> List[str]:
        """Get all skills from a topic up to a certain grade."""
        prereqs = []
        for grade in range(1, max_grade + 1):
            skills = self.skills_by_topic_grade.get((topic_id, grade), [])
            for skill in skills:
                if skill['id'] != exclude_id:
                    prereqs.append(skill['id'])
        return prereqs

    def find_skill(self, topic: str, grade: int, position: int = 1) -> str:
        """Find a specific skill ID."""
        skill_id = f"{topic}.G{grade}.{position:02d}"
        return skill_id if skill_id in self.skill_by_id else None

    def add_dependency(self, skill: Dict, dep_id: str, reason: str = ""):
        """Add a dependency if it doesn't already exist and is valid."""
        if dep_id not in self.skill_by_id:
            return False

        dep_skill = self.skill_by_id[dep_id]

        # Validate: no forward references in grade
        if dep_skill['grade'] > skill['grade']:
            return False

        # Validate: don't add self
        if dep_id == skill['id']:
            return False

        # Add if not already present
        if 'dependencies' not in skill:
            skill['dependencies'] = []

        if dep_id not in skill['dependencies']:
            skill['dependencies'].append(dep_id)
            self.stats['added_deps'] += 1
            self.stats['by_topic'][skill['topic_id']] += 1
            self.stats['by_grade'][skill['grade']] += 1
            return True

        return False

    def enrich_foundational_topics(self):
        """Enrich T01-T05: Foundational Concepts"""
        print("Enriching T01-T05: Foundational Concepts...")

        for skill in self.skills:
            topic = skill['topic_id']
            grade = skill['grade']

            if topic not in ['T01', 'T02', 'T03', 'T04', 'T05']:
                continue

            # Mostly within-topic progressions already exist
            # Add cross-foundational connections for grades 3+

            if grade >= 3:
                # T02 (Representing/Tracing) can depend on T01 (Algorithms)
                if topic == 'T02':
                    t01_base = self.find_skill('T01', min(grade, 2), 1)
                    if t01_base:
                        self.add_dependency(skill, t01_base, "Algorithm understanding")

                # T03 (Decomposition) can depend on T01 (Algorithms)
                if topic == 'T03':
                    t01_base = self.find_skill('T01', min(grade, 2), 1)
                    if t01_base:
                        self.add_dependency(skill, t01_base, "Algorithm understanding")

                # T04 (Patterns) can depend on T01 (Algorithms)
                if topic == 'T04':
                    t01_base = self.find_skill('T01', min(grade, 2), 1)
                    if t01_base:
                        self.add_dependency(skill, t01_base, "Algorithm understanding")

    def enrich_programming_core(self):
        """Enrich T06-T13: Programming Core"""
        print("Enriching T06-T13: Programming Core...")

        for skill in self.skills:
            topic = skill['topic_id']
            grade = skill['grade']

            if topic not in ['T06', 'T07', 'T08', 'T09', 'T10', 'T11', 'T12', 'T13']:
                continue

            # Add connections to foundational concepts for grades 2+
            if grade >= 2:
                # All programming concepts build on T01 (Algorithms)
                t01_base = self.find_skill('T01', min(grade, 1), 1)
                if t01_base:
                    self.add_dependency(skill, t01_base, "Algorithm foundation")

            # Cross-programming dependencies for grades 3+
            if grade >= 3:
                # T07 (Loops) needs T06 (Events) for execution context
                if topic == 'T07':
                    t06_prereq = self.find_skill('T06', min(grade, 3), 1)
                    if t06_prereq:
                        self.add_dependency(skill, t06_prereq, "Event-driven execution")

                # T08 (Conditionals) needs T06 (Events) and can use T09 (Variables)
                if topic == 'T08':
                    t06_prereq = self.find_skill('T06', min(grade, 3), 1)
                    if t06_prereq:
                        self.add_dependency(skill, t06_prereq, "Event-driven execution")

                    # Add variables if available at this grade
                    if grade >= 3:
                        t09_prereq = self.find_skill('T09', min(grade, 3), 1)
                        if t09_prereq:
                            self.add_dependency(skill, t09_prereq, "Variable-based conditions")

                # T09 (Variables) needs T06 (Events) for context
                if topic == 'T09' and grade >= 3:
                    t06_prereq = self.find_skill('T06', min(grade, 3), 1)
                    if t06_prereq:
                        self.add_dependency(skill, t06_prereq, "Event-driven execution")

                # T10 (Lists) needs T09 (Variables) and T07 (Loops)
                if topic == 'T10':
                    t09_prereq = self.find_skill('T09', min(grade, 3), 1)
                    if t09_prereq:
                        self.add_dependency(skill, t09_prereq, "Variable foundation")

                    t07_prereq = self.find_skill('T07', min(grade, 3), 1)
                    if t07_prereq:
                        self.add_dependency(skill, t07_prereq, "Iteration over lists")

                # T11 (Functions) needs T09 (Variables) and T06 (Events)
                if topic == 'T11' and grade >= 4:
                    t09_prereq = self.find_skill('T09', min(grade - 1, 3), 1)
                    if t09_prereq:
                        self.add_dependency(skill, t09_prereq, "Parameters and returns")

                    t06_prereq = self.find_skill('T06', min(grade - 1, 3), 1)
                    if t06_prereq:
                        self.add_dependency(skill, t06_prereq, "Function invocation")

                # T12 (Program Organization) needs multiple concepts
                if topic == 'T12' and grade >= 4:
                    # Needs functions, variables, events
                    for dep_topic in ['T06', 'T09', 'T11']:
                        dep_id = self.find_skill(dep_topic, min(grade - 1, 3), 1)
                        if dep_id:
                            self.add_dependency(skill, dep_id, "Organizational foundation")

                # T13 (Testing/Debugging) needs understanding of what to test
                if topic == 'T13' and grade >= 3:
                    # Needs events, conditionals, variables
                    for dep_topic in ['T06', 'T08', 'T09']:
                        dep_id = self.find_skill(dep_topic, min(grade, 3), 1)
                        if dep_id:
                            self.add_dependency(skill, dep_id, "Testing foundation")

    def enrich_application_skills(self):
        """Enrich T14-T24: Application Skills - This is where most enrichment happens"""
        print("Enriching T14-T24: Application Skills...")

        for skill in self.skills:
            topic = skill['topic_id']
            grade = skill['grade']

            if topic not in ['T14', 'T15', 'T16', 'T17', 'T18', 'T19',
                           'T20', 'T21', 'T22', 'T23', 'T24']:
                continue

            # Grade 1-2: Minimal dependencies (exploration phase)
            if grade <= 2:
                # Add T06 (Events) as baseline for interaction
                t06_base = self.find_skill('T06', min(grade, 1), 1)
                if t06_base:
                    self.add_dependency(skill, t06_base, "Basic interaction")
                continue

            # Grade 3: THE GATEWAY - First major cross-topic integration
            if grade == 3:
                # Core programming fundamentals
                self.add_dependency(skill, 'T06.G3.01', "Event handling")
                self.add_dependency(skill, 'T07.G3.01', "Basic repetition")
                self.add_dependency(skill, 'T08.G3.01', "Simple logic")
                self.add_dependency(skill, 'T09.G3.01', "Variable tracking")

                # Decomposition for project structure
                t03_base = self.find_skill('T03', 3, 1)
                if t03_base:
                    self.add_dependency(skill, t03_base, "Project decomposition")

                continue

            # Grades 4-5: Rich cross-topic dependencies (4-6 deps)
            if grade in [4, 5]:
                # Events (always)
                t06_prereq = self.find_skill('T06', grade, 1)
                if t06_prereq:
                    self.add_dependency(skill, t06_prereq, "Event handling")

                # Loops (for animation, iteration)
                if any(keyword in skill['description'].lower()
                      for keyword in ['animation', 'repeat', 'multiple', 'move', 'iterate']):
                    t07_prereq = self.find_skill('T07', grade, 1)
                    if t07_prereq:
                        self.add_dependency(skill, t07_prereq, "Repetition/animation")

                # Conditionals (for game logic, branching)
                if any(keyword in skill['description'].lower()
                      for keyword in ['logic', 'if', 'choice', 'decide', 'check', 'game', 'rule']):
                    t08_prereq = self.find_skill('T08', grade, 1)
                    if t08_prereq:
                        self.add_dependency(skill, t08_prereq, "Logic/branching")

                # Variables (almost always for state tracking)
                t09_prereq = self.find_skill('T09', grade, 1)
                if t09_prereq:
                    self.add_dependency(skill, t09_prereq, "State management")

                # Lists (for collections)
                if any(keyword in skill['description'].lower()
                      for keyword in ['list', 'collection', 'multiple', 'items', 'enemies', 'data']):
                    t10_prereq = self.find_skill('T10', min(grade, 4), 1)
                    if t10_prereq:
                        self.add_dependency(skill, t10_prereq, "Data collections")

                # Functions (for modular design in grade 4+)
                if any(keyword in skill['description'].lower()
                      for keyword in ['function', 'procedure', 'modular', 'reusable']):
                    t11_prereq = self.find_skill('T11', min(grade, 4), 1)
                    if t11_prereq:
                        self.add_dependency(skill, t11_prereq, "Modular design")

                # Debugging (for complex projects)
                if any(keyword in skill['description'].lower()
                      for keyword in ['debug', 'test', 'complex', 'multi-step']):
                    t13_prereq = self.find_skill('T13', min(grade, 3), 1)
                    if t13_prereq:
                        self.add_dependency(skill, t13_prereq, "Testing/debugging")

                continue

            # Grades 6-8: Advanced integration (6-10 deps)
            if grade >= 6:
                # Core programming (events, loops, conditionals, variables always)
                for core_topic in ['T06', 'T07', 'T08', 'T09']:
                    prereq_id = self.find_skill(core_topic, min(grade, 5), 1)
                    if prereq_id:
                        self.add_dependency(skill, prereq_id, "Core programming")

                # Lists (almost always at this level)
                t10_prereq = self.find_skill('T10', min(grade, 5), 1)
                if t10_prereq:
                    self.add_dependency(skill, t10_prereq, "Data structures")

                # Functions (modular design expected)
                t11_prereq = self.find_skill('T11', min(grade, 5), 1)
                if t11_prereq:
                    self.add_dependency(skill, t11_prereq, "Functions/modularity")

                # Program organization (for complex projects)
                t12_prereq = self.find_skill('T12', min(grade, 5), 1)
                if t12_prereq:
                    self.add_dependency(skill, t12_prereq, "Project organization")

                # Testing/Debugging (essential at advanced levels)
                t13_prereq = self.find_skill('T13', min(grade, 5), 1)
                if t13_prereq:
                    self.add_dependency(skill, t13_prereq, "Testing/debugging")

                # Topic-specific advanced dependencies

                # Games (T14) - needs physics awareness for advanced games
                if topic == 'T14' and grade >= 7:
                    t17_prereq = self.find_skill('T17', min(grade - 1, 6), 1)
                    if t17_prereq:
                        self.add_dependency(skill, t17_prereq, "Physics integration")

                # 3D Games (T18) - needs prior game experience
                if topic == 'T18':
                    t14_prereq = self.find_skill('T14', min(grade - 1, 5), 1)
                    if t14_prereq:
                        self.add_dependency(skill, t14_prereq, "Game fundamentals")

                # Multiplayer (T19) - needs games + internet concepts
                if topic == 'T19':
                    t14_prereq = self.find_skill('T14', min(grade - 1, 5), 1)
                    if t14_prereq:
                        self.add_dependency(skill, t14_prereq, "Game fundamentals")

                    t31_prereq = self.find_skill('T31', min(grade - 1, 5), 1)
                    if t31_prereq:
                        self.add_dependency(skill, t31_prereq, "Network concepts")

                # AI Media (T21) - needs media + basic AI understanding
                if topic == 'T21' and grade >= 6:
                    t15_prereq = self.find_skill('T15', min(grade - 1, 5), 1)
                    if t15_prereq:
                        self.add_dependency(skill, t15_prereq, "Media fundamentals")

                # Chatbots (T22) - needs understanding of logic and text
                if topic == 'T22':
                    # Text/NLP awareness
                    t29_prereq = self.find_skill('T29', min(grade - 1, 5), 1)
                    if t29_prereq:
                        self.add_dependency(skill, t29_prereq, "Text processing")

                # Voice/Vision/Gesture (T23) - advanced AI applications
                if topic == 'T23':
                    t21_prereq = self.find_skill('T21', min(grade - 1, 6), 1)
                    if t21_prereq:
                        self.add_dependency(skill, t21_prereq, "AI media foundation")

                # Responsible AI (T24) - needs exposure to AI applications
                if topic == 'T24':
                    t21_prereq = self.find_skill('T21', min(grade - 1, 6), 1)
                    if t21_prereq:
                        self.add_dependency(skill, t21_prereq, "AI application context")

                    t22_prereq = self.find_skill('T22', min(grade - 1, 6), 1)
                    if t22_prereq:
                        self.add_dependency(skill, t22_prereq, "AI ethics context")

    def enrich_data_skills(self):
        """Enrich T25-T29: Data & Analysis Skills"""
        print("Enriching T25-T29: Data Skills...")

        for skill in self.skills:
            topic = skill['topic_id']
            grade = skill['grade']

            if topic not in ['T25', 'T26', 'T27', 'T28', 'T29']:
                continue

            # Grade 1-2: Basic exploration
            if grade <= 2:
                continue

            # Grade 3+: Programming fundamentals for data
            if grade >= 3:
                # Variables (essential)
                t09_prereq = self.find_skill('T09', min(grade, 3), 1)
                if t09_prereq:
                    self.add_dependency(skill, t09_prereq, "Data storage")

                # Lists (essential for data collections)
                t10_prereq = self.find_skill('T10', min(grade, 3), 1)
                if t10_prereq:
                    self.add_dependency(skill, t10_prereq, "Data collections")

                # Loops (for processing data)
                t07_prereq = self.find_skill('T07', min(grade, 3), 1)
                if t07_prereq:
                    self.add_dependency(skill, t07_prereq, "Data iteration")

                # Conditionals (for filtering/categorization)
                if any(keyword in skill['description'].lower()
                      for keyword in ['filter', 'categorize', 'classify', 'if', 'condition']):
                    t08_prereq = self.find_skill('T08', min(grade, 3), 1)
                    if t08_prereq:
                        self.add_dependency(skill, t08_prereq, "Data filtering")

            # Grade 4+: Functions for analysis operations
            if grade >= 4:
                if any(keyword in skill['description'].lower()
                      for keyword in ['analyze', 'calculate', 'compute', 'function']):
                    t11_prereq = self.find_skill('T11', min(grade, 4), 1)
                    if t11_prereq:
                        self.add_dependency(skill, t11_prereq, "Analysis functions")

            # Cross-data topic dependencies

            # T26 (Collection) builds on T25 (Representation)
            if topic == 'T26' and grade >= 3:
                t25_prereq = self.find_skill('T25', min(grade, 3), 1)
                if t25_prereq:
                    self.add_dependency(skill, t25_prereq, "Data representation")

            # T27 (Analysis) needs T25 and T26
            if topic == 'T27' and grade >= 3:
                t25_prereq = self.find_skill('T25', min(grade, 3), 1)
                if t25_prereq:
                    self.add_dependency(skill, t25_prereq, "Data representation")

                t26_prereq = self.find_skill('T26', min(grade, 3), 1)
                if t26_prereq:
                    self.add_dependency(skill, t26_prereq, "Data collection")

            # T28 (Chance/Sampling) needs T27 for statistical concepts
            if topic == 'T28' and grade >= 4:
                t27_prereq = self.find_skill('T27', min(grade - 1, 3), 1)
                if t27_prereq:
                    self.add_dependency(skill, t27_prereq, "Data analysis foundation")

            # T29 (Text/NLP) needs variables, lists, and basic analysis
            if topic == 'T29' and grade >= 4:
                t27_prereq = self.find_skill('T27', min(grade - 1, 3), 1)
                if t27_prereq:
                    self.add_dependency(skill, t27_prereq, "Data analysis foundation")

    def enrich_systems_society(self):
        """Enrich T30-T36: Systems & Society"""
        print("Enriching T30-T36: Systems & Society...")

        for skill in self.skills:
            topic = skill['topic_id']
            grade = skill['grade']

            if topic not in ['T30', 'T31', 'T32', 'T33', 'T34', 'T35', 'T36']:
                continue

            # Lighter programming dependencies, more conceptual

            # Grade 3+: Add programming context where relevant
            if grade >= 3:
                # T30 (Hardware) - minimal programming deps
                # T31 (Internet) - connect to applications that use it
                if topic == 'T31' and grade >= 5:
                    # Multiplayer games use internet
                    t19_prereq = self.find_skill('T19', min(grade - 1, 5), 1)
                    if t19_prereq:
                        self.add_dependency(skill, t19_prereq, "Internet application context")

                # T32 (Cybersecurity) - needs internet understanding
                if topic == 'T32' and grade >= 4:
                    t31_prereq = self.find_skill('T31', min(grade, 3), 1)
                    if t31_prereq:
                        self.add_dependency(skill, t31_prereq, "Network foundation")

                # T33 (Platforms/APIs) - needs programming and internet
                if topic == 'T33' and grade >= 5:
                    t31_prereq = self.find_skill('T31', min(grade - 1, 4), 1)
                    if t31_prereq:
                        self.add_dependency(skill, t31_prereq, "Internet/cloud foundation")

                    # Programming for API usage
                    t11_prereq = self.find_skill('T11', min(grade - 1, 4), 1)
                    if t11_prereq:
                        self.add_dependency(skill, t11_prereq, "Function/API calls")

                # T34 (History) - minimal dependencies

                # T35 (Impacts) - connect to AI applications for context
                if topic == 'T35' and grade >= 6:
                    t21_prereq = self.find_skill('T21', min(grade - 1, 5), 1)
                    if t21_prereq:
                        self.add_dependency(skill, t21_prereq, "AI impact context")

                # T36 (Ethics/Careers) - connect to AI for ethics discussions
                if topic == 'T36' and grade >= 6:
                    t21_prereq = self.find_skill('T21', min(grade - 1, 5), 1)
                    if t21_prereq:
                        self.add_dependency(skill, t21_prereq, "AI ethics context")

                    t24_prereq = self.find_skill('T24', min(grade - 1, 5), 1)
                    if t24_prereq:
                        self.add_dependency(skill, t24_prereq, "Responsible AI practices")

    def enrich_all(self):
        """Run all enrichment passes."""
        print("\n=== Starting Comprehensive Dependency Enrichment ===\n")

        self.enrich_foundational_topics()
        self.enrich_programming_core()
        self.enrich_application_skills()
        self.enrich_data_skills()
        self.enrich_systems_society()

        print("\n=== Enrichment Complete ===\n")

    def update_dependency_counts(self):
        """Update dependency_count field for all skills."""
        for skill in self.skills:
            skill['dependency_count'] = len(skill.get('dependencies', []))

    def save(self, output_file: str):
        """Save enriched skills to file."""
        self.update_dependency_counts()
        with open(output_file, 'w') as f:
            json.dump(self.skills, f, indent=2)
        print(f"\nSaved enriched skills to: {output_file}")

    def generate_statistics(self) -> dict:
        """Generate comprehensive statistics."""
        total_skills = len(self.skills)
        total_deps = sum(len(s.get('dependencies', [])) for s in self.skills)
        avg_deps = total_deps / total_skills if total_skills > 0 else 0

        # By topic
        topic_stats = {}
        for skill in self.skills:
            topic = skill['topic_id']
            if topic not in topic_stats:
                topic_stats[topic] = {'count': 0, 'deps': 0}
            topic_stats[topic]['count'] += 1
            topic_stats[topic]['deps'] += len(skill.get('dependencies', []))

        # By grade
        grade_stats = {}
        for skill in self.skills:
            grade = skill['grade']
            if grade not in grade_stats:
                grade_stats[grade] = {'count': 0, 'deps': 0}
            grade_stats[grade]['count'] += 1
            grade_stats[grade]['deps'] += len(skill.get('dependencies', []))

        return {
            'total_skills': total_skills,
            'original_deps': self.stats['original_deps'],
            'final_deps': total_deps,
            'added_deps': self.stats['added_deps'],
            'avg_deps': avg_deps,
            'topic_stats': topic_stats,
            'grade_stats': grade_stats
        }


def main():
    # Load and enrich
    enricher = DependencyEnricher('/media/binyu/USB2/dev/CreatiCodeSkillMap/skills_final.json')
    enricher.enrich_all()

    # Save enriched version
    enricher.save('/media/binyu/USB2/dev/CreatiCodeSkillMap/skills_final_enriched.json')

    # Generate statistics
    stats = enricher.generate_statistics()

    print("\n=== ENRICHMENT STATISTICS ===\n")
    print(f"Total skills: {stats['total_skills']}")
    print(f"Original dependencies: {stats['original_deps']}")
    print(f"Final dependencies: {stats['final_deps']}")
    print(f"Added dependencies: {stats['added_deps']}")
    print(f"Original average: {stats['original_deps'] / stats['total_skills']:.2f}")
    print(f"Final average: {stats['avg_deps']:.2f}")
    print(f"\nBy Grade:")
    for grade in sorted(stats['grade_stats'].keys()):
        gstats = stats['grade_stats'][grade]
        avg = gstats['deps'] / gstats['count'] if gstats['count'] > 0 else 0
        print(f"  Grade {grade}: {gstats['deps']} deps ({avg:.2f} avg)")

    print(f"\nBy Topic:")
    for topic in sorted(stats['topic_stats'].keys()):
        tstats = stats['topic_stats'][topic]
        avg = tstats['deps'] / tstats['count'] if tstats['count'] > 0 else 0
        print(f"  {topic}: {tstats['deps']} deps ({avg:.2f} avg)")

    # Save stats to JSON for report generation
    with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/enrichment_stats.json', 'w') as f:
        json.dump(stats, f, indent=2)

    print(f"\nStatistics saved to: enrichment_stats.json")


if __name__ == '__main__':
    main()
