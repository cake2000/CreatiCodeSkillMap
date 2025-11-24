#!/usr/bin/env python3
"""
Final Grade K Analysis - Create actionable recommendations
"""

import re
from collections import defaultdict
from typing import Dict, List, Set

class GradeKAnalyzer:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.all_skills = {}
        self.grade_k_skills = {}

    def parse_file(self):
        """Parse allskills.md"""
        with open(self.file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        skill_blocks = re.split(r'\n(?=ID: T\d+\.)', content)

        for block in skill_blocks:
            if not block.strip() or not block.startswith('ID:'):
                continue

            skill_data = self._parse_skill_block(block)
            if skill_data:
                skill_id = skill_data['id']
                self.all_skills[skill_id] = skill_data

                if '.GK.' in skill_id:
                    self.grade_k_skills[skill_id] = skill_data

    def _parse_skill_block(self, block: str) -> Dict:
        """Parse a single skill block"""
        skill_data = {}

        id_match = re.search(r'ID:\s*(T\d+\.[A-Z0-9]+\.\d+)', block)
        if id_match:
            skill_data['id'] = id_match.group(1)
        else:
            return None

        topic_match = re.search(r'Topic:\s*(.+)', block)
        if topic_match:
            skill_data['topic'] = topic_match.group(1).strip()

        skill_match = re.search(r'Skill:\s*(.+)', block)
        if skill_match:
            skill_data['skill'] = skill_match.group(1).strip()

        desc_match = re.search(r'Description:\s*(.+?)(?=\n\n|Dependencies:|$)', block, re.DOTALL)
        if desc_match:
            skill_data['description'] = desc_match.group(1).strip()

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

    def analyze_comprehensive(self):
        """Create comprehensive analysis with specific recommendations"""
        
        # 1. Organize all Grade K skills by topic
        by_topic = defaultdict(list)
        for skill_id, skill in self.grade_k_skills.items():
            topic = skill_id.split('.')[0]
            by_topic[topic].append({
                'id': skill_id,
                'skill': skill['skill'],
                'deps': skill['dependencies'],
                'description': skill['description']
            })

        # 2. Analyze cross-topic relationships
        cross_topic_deps = defaultdict(list)
        skills_without_cross_topic = []
        
        for skill_id, skill in self.grade_k_skills.items():
            skill_topic = skill_id.split('.')[0]
            deps = skill['dependencies']
            
            has_cross_topic = False
            for dep_id in deps:
                dep_topic = dep_id.split('.')[0]
                if dep_topic != skill_topic and '.GK.' in dep_id:
                    has_cross_topic = True
                    cross_topic_deps[skill_topic].append({
                        'skill_id': skill_id,
                        'skill_name': skill['skill'],
                        'depends_on': dep_id,
                        'depends_on_topic': dep_topic
                    })
            
            if not has_cross_topic and deps:
                skills_without_cross_topic.append({
                    'id': skill_id,
                    'skill': skill['skill'],
                    'topic': skill_topic
                })

        # 3. Identify specific patterns requiring cross-topic dependencies
        missing_deps = self._identify_missing_cross_topic_deps()

        # 4. Generate report
        return self._generate_actionable_report(by_topic, cross_topic_deps, 
                                                skills_without_cross_topic, missing_deps)

    def _identify_missing_cross_topic_deps(self):
        """Identify specific missing cross-topic dependencies"""
        recommendations = []
        
        # Define clear dependency rules
        rules = [
            {
                'name': 'Game/Animation skills need Graphics basics',
                'source_topics': ['T18', 'T19', 'T20', 'T21'],
                'keywords': ['sprite', 'character', 'actor', 'animation', 'move', 'game'],
                'target_topics': ['T05', 'T06', 'T07'],
                'rationale': 'Visual games need understanding of sprites and graphics'
            },
            {
                'name': 'Loop-based skills need Pattern recognition',
                'source_topics': ['T01', 'T02', 'T03'],
                'keywords': ['repeat', 'again', 'over and over', 'many times'],
                'target_topics': ['T04'],
                'rationale': 'Understanding repetition requires pattern recognition'
            },
            {
                'name': 'Counting skills need Variables',
                'source_topics': ['T01', 'T10'],
                'keywords': ['count', 'number', 'how many', 'score', 'total'],
                'target_topics': ['T09'],
                'rationale': 'Counting involves storing and changing values'
            },
            {
                'name': 'Conditional skills need Event sequencing',
                'source_topics': ['T08'],
                'keywords': ['if', 'when', 'decide', 'choice', 'check'],
                'target_topics': ['T06'],
                'rationale': 'Conditionals build on understanding event sequences'
            },
            {
                'name': 'Complex sequencing needs Decomposition',
                'source_topics': ['T01', 'T02'],
                'keywords': ['steps', 'order', 'sequence', 'routine'],
                'target_topics': ['T03'],
                'rationale': 'Breaking down problems helps with sequencing'
            }
        ]

        for rule in rules:
            for skill_id, skill in self.grade_k_skills.items():
                skill_topic = skill_id.split('.')[0]
                
                if skill_topic not in rule['source_topics']:
                    continue
                
                skill_text = (skill['skill'] + ' ' + skill['description']).lower()
                
                # Check if skill matches keywords
                matches_keywords = any(kw in skill_text for kw in rule['keywords'])
                
                if matches_keywords:
                    # Check if it has dependencies from target topics
                    current_dep_topics = set(dep.split('.')[0] for dep in skill['dependencies'] if '.' in dep)
                    
                    missing_topics = set(rule['target_topics']) - current_dep_topics
                    
                    if missing_topics:
                        for target_topic in missing_topics:
                            # Find fundamental skills from target topic
                            target_skills = [
                                s_id for s_id in self.grade_k_skills
                                if s_id.startswith(f"{target_topic}.GK.")
                            ]
                            
                            if target_skills:
                                recommendations.append({
                                    'skill_id': skill_id,
                                    'skill_name': skill['skill'],
                                    'rule': rule['name'],
                                    'rationale': rule['rationale'],
                                    'missing_topic': target_topic,
                                    'suggested_deps': target_skills[:2],
                                    'matched_keywords': [kw for kw in rule['keywords'] if kw in skill_text]
                                })

        return recommendations

    def _generate_actionable_report(self, by_topic, cross_topic_deps, 
                                   skills_without_cross_topic, missing_deps):
        """Generate final actionable report"""
        lines = []
        
        lines.append("=" * 100)
        lines.append("GRADE K SKILLS - COMPREHENSIVE DEPENDENCY ANALYSIS")
        lines.append("=" * 100)
        lines.append("")
        
        # Executive Summary
        lines.append("## EXECUTIVE SUMMARY")
        lines.append("=" * 100)
        lines.append(f"Total Grade K skills analyzed: {len(self.grade_k_skills)}")
        lines.append(f"Topics with Grade K skills: {len(by_topic)}")
        lines.append(f"Skills with cross-topic dependencies: {sum(len(deps) for deps in cross_topic_deps.values())}")
        lines.append(f"Skills needing cross-topic dependencies: {len(missing_deps)}")
        lines.append("")
        
        # List all Grade K skills
        lines.append("## ALL GRADE K SKILLS BY TOPIC")
        lines.append("=" * 100)
        
        for topic in sorted(by_topic.keys()):
            skills = by_topic[topic]
            lines.append(f"\n### {topic} ({len(skills)} skills)")
            lines.append("-" * 80)
            
            for skill in skills:
                lines.append(f"\n{skill['id']}: {skill['skill']}")
                if skill['deps']:
                    lines.append(f"  Dependencies ({len(skill['deps'])}):")
                    for dep in skill['deps']:
                        dep_name = self.all_skills.get(dep, {}).get('skill', 'UNKNOWN')
                        dep_topic = dep.split('.')[0]
                        cross_marker = " [CROSS-TOPIC]" if dep_topic != topic else ""
                        lines.append(f"    - {dep}: {dep_name}{cross_marker}")
                else:
                    lines.append(f"  Dependencies: None (foundational skill)")
        
        lines.append("\n")
        
        # Cross-topic dependency analysis
        lines.append("## EXISTING CROSS-TOPIC DEPENDENCIES")
        lines.append("=" * 100)
        
        if cross_topic_deps:
            for topic in sorted(cross_topic_deps.keys()):
                deps = cross_topic_deps[topic]
                lines.append(f"\n### {topic} ({len(deps)} cross-topic dependencies)")
                
                for dep in deps:
                    lines.append(f"  {dep['skill_id']}: {dep['skill_name']}")
                    lines.append(f"    → Depends on {dep['depends_on']} [{dep['depends_on_topic']}]")
        else:
            lines.append("No cross-topic dependencies found")
        
        lines.append("\n")
        
        # Recommended new dependencies
        lines.append("## RECOMMENDED NEW CROSS-TOPIC DEPENDENCIES")
        lines.append("=" * 100)
        lines.append(f"Found {len(missing_deps)} skills that should add cross-topic dependencies")
        lines.append("")
        
        # Group by rule
        by_rule = defaultdict(list)
        for rec in missing_deps:
            by_rule[rec['rule']].append(rec)
        
        for rule_name in sorted(by_rule.keys()):
            recs = by_rule[rule_name]
            lines.append(f"\n### {rule_name} ({len(recs)} skills)")
            lines.append("-" * 80)
            lines.append(f"Rationale: {recs[0]['rationale']}")
            lines.append("")
            
            for rec in recs[:10]:  # Top 10 per rule
                lines.append(f"{rec['skill_id']}: {rec['skill_name']}")
                lines.append(f"  Keywords found: {', '.join(rec['matched_keywords'])}")
                lines.append(f"  ADD dependency to {rec['missing_topic']}:")
                for dep in rec['suggested_deps']:
                    dep_name = self.grade_k_skills.get(dep, {}).get('skill', 'N/A')
                    lines.append(f"    - Option: {dep} ({dep_name})")
                lines.append("")
        
        lines.append("")
        
        # Specific actionable changes
        lines.append("## ACTIONABLE DEPENDENCY CHANGES")
        lines.append("=" * 100)
        lines.append("Below are specific skills that need dependency updates:")
        lines.append("")
        
        # Group recommendations by skill
        by_skill = defaultdict(list)
        for rec in missing_deps:
            by_skill[rec['skill_id']].append(rec)
        
        for skill_id in sorted(by_skill.keys()):
            skill = self.grade_k_skills[skill_id]
            recs = by_skill[skill_id]
            
            lines.append(f"\n{skill_id}: {skill['skill']}")
            lines.append("-" * 80)
            lines.append(f"Current dependencies: {len(skill['dependencies'])}")
            for dep in skill['dependencies']:
                dep_name = self.all_skills.get(dep, {}).get('skill', 'UNKNOWN')
                lines.append(f"  - {dep} ({dep_name})")
            
            lines.append("")
            lines.append("RECOMMENDED ADDITIONS:")
            
            # Deduplicate recommendations by target topic
            seen_topics = set()
            for rec in recs:
                if rec['missing_topic'] not in seen_topics:
                    seen_topics.add(rec['missing_topic'])
                    lines.append(f"  ADD dependency from {rec['missing_topic']}:")
                    lines.append(f"    Reason: {rec['rationale']}")
                    lines.append(f"    Keywords: {', '.join(rec['matched_keywords'])}")
                    lines.append(f"    Best option: {rec['suggested_deps'][0]}")
                    best_dep = self.grade_k_skills.get(rec['suggested_deps'][0], {})
                    lines.append(f"      {best_dep.get('skill', 'N/A')}")
            
            lines.append("")
        
        lines.append("=" * 100)
        lines.append("END OF ANALYSIS")
        lines.append("=" * 100)
        
        return '\n'.join(lines)

def main():
    analyzer = GradeKAnalyzer('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md')
    
    print("Parsing skills file...")
    analyzer.parse_file()
    
    print(f"Found {len(analyzer.grade_k_skills)} Grade K skills")
    
    print("\nGenerating comprehensive analysis...")
    report = analyzer.analyze_comprehensive()
    
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/grade_k_recommended_changes.md'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\nReport saved to: {output_file}")
    print("\nAnalysis complete!")

if __name__ == '__main__':
    main()
