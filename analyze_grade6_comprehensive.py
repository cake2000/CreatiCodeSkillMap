#!/usr/bin/env python3
"""
Comprehensive Grade 6 Skills Analysis
Extracts and analyzes ALL Grade 6 skills from all 36 topics
"""

import re
import json
from collections import defaultdict
from typing import Dict, List, Set, Tuple

def parse_allskills_file(filepath: str) -> Dict:
    """Parse the allskills.md file and extract all skills with their dependencies"""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by skill ID patterns (T##.G#.##)
    skill_pattern = r'\nID: (T\d+\.G[K\d]+\.\d+)\n'
    parts = re.split(skill_pattern, content)

    all_skills = {}
    current_id = None

    for i, part in enumerate(parts):
        if i == 0:
            continue  # Skip header

        if i % 2 == 1:  # This is a skill ID
            current_id = part.strip()
        else:  # This is the skill content
            if current_id:
                skill_data = parse_skill_block(current_id, part)
                all_skills[current_id] = skill_data

    return all_skills

def parse_skill_block(skill_id: str, content: str) -> Dict:
    """Parse a single skill block to extract all relevant information"""

    lines = content.strip().split('\n')
    skill_data = {
        'id': skill_id,
        'topic': '',
        'skill_name': '',
        'description': '',
        'dependencies': [],
        'grade': extract_grade_from_id(skill_id)
    }

    current_section = None

    for line in lines:
        line = line.strip()

        if line.startswith('Topic:'):
            skill_data['topic'] = line.replace('Topic:', '').strip()
        elif line.startswith('Skill:'):
            skill_data['skill_name'] = line.replace('Skill:', '').strip()
        elif line.startswith('Description:'):
            skill_data['description'] = line.replace('Description:', '').strip()
            current_section = 'description'
        elif line.startswith('Dependencies:'):
            current_section = 'dependencies'
        elif line.startswith('*') and current_section == 'dependencies':
            # Extract dependency ID
            dep_match = re.search(r'(T\d+\.G[K\d]+\.\d+)', line)
            if dep_match:
                skill_data['dependencies'].append(dep_match.group(1))
        elif current_section == 'description' and line and not line.startswith('ID:'):
            skill_data['description'] += ' ' + line

    return skill_data

def extract_grade_from_id(skill_id: str) -> int:
    """Extract grade number from skill ID (e.g., T01.G6.01 -> 6)"""
    match = re.search(r'\.G([K\d]+)\.', skill_id)
    if match:
        grade_str = match.group(1)
        if grade_str == 'K':
            return 0
        return int(grade_str)
    return -1

def extract_topic_number(skill_id: str) -> int:
    """Extract topic number from skill ID (e.g., T01.G6.01 -> 1)"""
    match = re.search(r'T(\d+)\.', skill_id)
    if match:
        return int(match.group(1))
    return -1

def check_x_minus_2_rule(skill_grade: int, dep_grade: int) -> bool:
    """Check if dependency violates X-2 rule (can only depend on X-2, X-1, X grades)"""
    if skill_grade == 6:
        return dep_grade >= 4  # Grade 6 can depend on 4, 5, 6
    return False  # Not checking other grades in this analysis

def analyze_grade6_skills(all_skills: Dict) -> Dict:
    """Comprehensive analysis of all Grade 6 skills"""

    # Filter Grade 6 skills
    grade6_skills = {k: v for k, v in all_skills.items() if v['grade'] == 6}

    # Organize by topic
    skills_by_topic = defaultdict(list)
    for skill_id, skill_data in grade6_skills.items():
        topic_num = extract_topic_number(skill_id)
        skills_by_topic[topic_num].append({
            'id': skill_id,
            'skill_name': skill_data['skill_name'],
            'description': skill_data['description'][:200] + '...' if len(skill_data['description']) > 200 else skill_data['description'],
            'dependencies': skill_data['dependencies']
        })

    # Analyze each Grade 6 skill
    analysis_results = {
        'total_grade6_skills': len(grade6_skills),
        'topics_with_grade6': len(skills_by_topic),
        'skills_by_topic': {},
        'violations': {
            'x_minus_2_violations': [],
            'potential_circular': [],
            'missing_cross_topic': [],
            'unnecessary_transitive': []
        },
        'recommendations': {}
    }

    # Analyze each skill
    for topic_num in sorted(skills_by_topic.keys()):
        topic_key = f"T{topic_num:02d}"
        analysis_results['skills_by_topic'][topic_key] = {
            'skills': skills_by_topic[topic_num],
            'count': len(skills_by_topic[topic_num])
        }

        for skill_info in skills_by_topic[topic_num]:
            skill_id = skill_info['id']
            skill_data = grade6_skills[skill_id]

            # Analyze dependencies
            dep_analysis = analyze_dependencies(
                skill_id,
                skill_data,
                all_skills,
                grade6_skills
            )

            # Store recommendations
            if dep_analysis['issues'] or dep_analysis['recommendations']:
                analysis_results['recommendations'][skill_id] = {
                    'skill_name': skill_data['skill_name'],
                    'current_deps': skill_data['dependencies'],
                    'issues': dep_analysis['issues'],
                    'add_dependencies': dep_analysis['add_dependencies'],
                    'remove_dependencies': dep_analysis['remove_dependencies'],
                    'rationale': dep_analysis['rationale']
                }

            # Collect violations
            for issue in dep_analysis['issues']:
                if 'X-2 rule' in issue:
                    analysis_results['violations']['x_minus_2_violations'].append({
                        'skill_id': skill_id,
                        'issue': issue
                    })
                elif 'circular' in issue.lower():
                    analysis_results['violations']['potential_circular'].append({
                        'skill_id': skill_id,
                        'issue': issue
                    })
                elif 'missing' in issue.lower():
                    analysis_results['violations']['missing_cross_topic'].append({
                        'skill_id': skill_id,
                        'issue': issue
                    })

    return analysis_results

def analyze_dependencies(skill_id: str, skill_data: Dict, all_skills: Dict, grade6_skills: Dict) -> Dict:
    """Analyze dependencies for a single Grade 6 skill"""

    result = {
        'issues': [],
        'recommendations': [],
        'add_dependencies': [],
        'remove_dependencies': [],
        'rationale': []
    }

    skill_grade = skill_data['grade']
    skill_name = skill_data['skill_name'].lower()
    skill_desc = skill_data['description'].lower()
    current_deps = skill_data['dependencies']
    skill_topic = extract_topic_number(skill_id)

    # Check X-2 rule violations
    for dep_id in current_deps:
        if dep_id in all_skills:
            dep_grade = all_skills[dep_id]['grade']
            if dep_grade < 4:  # Grade 6 should only depend on 4, 5, 6
                result['issues'].append(
                    f"X-2 rule violation: depends on {dep_id} (grade {dep_grade}), should be >= grade 4"
                )
                result['remove_dependencies'].append({
                    'dep_id': dep_id,
                    'reason': f"Grade {dep_grade} violates X-2 rule for grade 6"
                })

    # Check for missing cross-topic dependencies based on skill content
    potential_cross_topic = find_potential_cross_topic_deps(
        skill_id, skill_name, skill_desc, skill_topic, all_skills
    )

    for pot_dep in potential_cross_topic:
        if pot_dep['dep_id'] not in current_deps:
            result['add_dependencies'].append(pot_dep)
            result['recommendations'].append(
                f"Consider adding {pot_dep['dep_id']}: {pot_dep['reason']}"
            )

    # Check for transitive redundancy
    transitive_deps = find_transitive_dependencies(skill_id, current_deps, all_skills)
    for trans_dep in transitive_deps:
        if trans_dep in current_deps:
            # This is potentially redundant
            result['rationale'].append(
                f"{trans_dep} might be transitive (check if truly redundant)"
            )

    # Check for circular dependencies
    circular = check_circular_dependencies(skill_id, current_deps, all_skills)
    if circular:
        result['issues'].append(f"Potential circular dependency: {circular}")

    return result

def find_potential_cross_topic_deps(skill_id: str, skill_name: str, skill_desc: str,
                                   skill_topic: int, all_skills: Dict) -> List[Dict]:
    """Find potential cross-topic dependencies based on skill content"""

    suggestions = []

    # Define keyword patterns for cross-topic dependencies
    patterns = {
        # Game-related skills need loops, variables, events
        'game': {
            'keywords': ['game', 'score', 'level', 'player', 'enemy', 'collision', 'win', 'lose'],
            'needed_topics': {
                2: ['loop', 'repeat'],  # Topic 2: Loops
                3: ['variable', 'counter', 'score'],  # Topic 3: Variables
                7: ['event', 'click', 'key press'],  # Topic 7: Events
                10: ['motion', 'move', 'glide'],  # Topic 10: Motion
            }
        },
        # AI/ML skills need data structures, logic
        'ai': {
            'keywords': ['ai', 'machine learning', 'classify', 'train', 'model', 'predict', 'pattern recognition'],
            'needed_topics': {
                5: ['list', 'data', 'collection'],  # Topic 5: Data structures
                4: ['condition', 'logic', 'if'],  # Topic 4: Conditionals
                3: ['variable', 'data'],  # Topic 3: Variables
            }
        },
        # Animation skills need motion, timing, events
        'animation': {
            'keywords': ['animate', 'animation', 'tween', 'morph', 'transition', 'sequence'],
            'needed_topics': {
                10: ['motion', 'move', 'glide'],  # Topic 10: Motion
                7: ['event', 'timing'],  # Topic 7: Events
                2: ['loop', 'repeat'],  # Topic 2: Loops
            }
        },
        # Physics/simulation needs math, variables
        'physics': {
            'keywords': ['physics', 'gravity', 'force', 'velocity', 'acceleration', 'collision'],
            'needed_topics': {
                3: ['variable', 'calculate'],  # Topic 3: Variables
                6: ['operator', 'math', 'calculate'],  # Topic 6: Operators
                10: ['motion', 'position'],  # Topic 10: Motion
            }
        },
        # Data visualization needs lists, operators
        'data_viz': {
            'keywords': ['chart', 'graph', 'visualize', 'plot', 'display data'],
            'needed_topics': {
                5: ['list', 'data', 'array'],  # Topic 5: Data structures
                6: ['operator', 'calculate'],  # Topic 6: Operators
                11: ['draw', 'pen'],  # Topic 11: Drawing/Pen
            }
        },
        # Complex drawing needs pen, operators, loops
        'drawing': {
            'keywords': ['draw', 'pen', 'stamp', 'shape', 'pattern', 'geometric'],
            'needed_topics': {
                11: ['pen', 'draw', 'stamp'],  # Topic 11: Drawing/Pen
                2: ['loop', 'repeat'],  # Topic 2: Loops
                6: ['operator', 'math'],  # Topic 6: Operators
            }
        },
        # Sensing/interaction needs events, conditionals
        'sensing': {
            'keywords': ['sense', 'detect', 'touch', 'distance', 'color', 'ask', 'answer'],
            'needed_topics': {
                12: ['sense', 'detect', 'ask'],  # Topic 12: Sensing
                7: ['event', 'when'],  # Topic 7: Events
                4: ['condition', 'if'],  # Topic 4: Conditionals
            }
        },
        # Cloning/spawning needs events, variables
        'cloning': {
            'keywords': ['clone', 'spawn', 'create', 'delete', 'instance'],
            'needed_topics': {
                13: ['clone', 'create'],  # Topic 13: Cloning
                7: ['event', 'when'],  # Topic 7: Events
                3: ['variable'],  # Topic 3: Variables
            }
        },
    }

    combined_text = skill_name + ' ' + skill_desc

    # Check each pattern category
    for category, pattern_data in patterns.items():
        # Check if skill matches any keywords
        if any(kw in combined_text for kw in pattern_data['keywords']):
            # Suggest dependencies from needed topics
            for needed_topic, topic_keywords in pattern_data['needed_topics'].items():
                if needed_topic != skill_topic:  # Cross-topic only
                    # Find high-grade skills from that topic
                    topic_skills = find_skills_from_topic(needed_topic, [4, 5, 6], all_skills)
                    for topic_skill in topic_skills:
                        topic_skill_name = all_skills[topic_skill]['skill_name'].lower()
                        topic_skill_desc = all_skills[topic_skill]['description'].lower()
                        topic_combined = topic_skill_name + ' ' + topic_skill_desc

                        # Check if topic skill matches the needed keywords
                        if any(tkw in topic_combined for tkw in topic_keywords):
                            suggestions.append({
                                'dep_id': topic_skill,
                                'reason': f"{category.replace('_', ' ').title()} skill needs {needed_topic} concepts",
                                'confidence': 'medium'
                            })
                            break  # Only suggest one per topic

    # Remove duplicates
    seen = set()
    unique_suggestions = []
    for sugg in suggestions:
        if sugg['dep_id'] not in seen:
            seen.add(sugg['dep_id'])
            unique_suggestions.append(sugg)

    return unique_suggestions[:5]  # Limit to top 5 suggestions

def find_skills_from_topic(topic_num: int, grades: List[int], all_skills: Dict) -> List[str]:
    """Find skills from a specific topic with specific grades"""
    results = []
    topic_prefix = f"T{topic_num:02d}"

    for skill_id, skill_data in all_skills.items():
        if skill_id.startswith(topic_prefix) and skill_data['grade'] in grades:
            results.append(skill_id)

    return sorted(results, key=lambda x: all_skills[x]['grade'], reverse=True)[:3]

def find_transitive_dependencies(skill_id: str, deps: List[str], all_skills: Dict) -> Set[str]:
    """Find transitive dependencies (dependencies of dependencies)"""
    transitive = set()

    for dep in deps:
        if dep in all_skills:
            dep_deps = all_skills[dep]['dependencies']
            transitive.update(dep_deps)

    return transitive

def check_circular_dependencies(skill_id: str, deps: List[str], all_skills: Dict,
                               visited: Set[str] = None) -> str:
    """Check for circular dependencies"""
    if visited is None:
        visited = set()

    if skill_id in visited:
        return f"Circular: {skill_id}"

    visited.add(skill_id)

    for dep in deps:
        if dep in all_skills:
            dep_deps = all_skills[dep]['dependencies']
            circular = check_circular_dependencies(dep, dep_deps, all_skills, visited.copy())
            if circular:
                return circular

    return ""

def generate_summary_stats(analysis: Dict) -> Dict:
    """Generate summary statistics"""
    return {
        'total_grade6_skills': analysis['total_grade6_skills'],
        'topics_with_grade6': analysis['topics_with_grade6'],
        'total_x_minus_2_violations': len(analysis['violations']['x_minus_2_violations']),
        'total_circular_issues': len(analysis['violations']['potential_circular']),
        'skills_needing_updates': len(analysis['recommendations']),
        'topics_breakdown': {
            topic: data['count']
            for topic, data in analysis['skills_by_topic'].items()
        }
    }

def main():
    print("Starting comprehensive Grade 6 analysis...")
    print("=" * 80)

    # Parse the file
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'
    print(f"Parsing {filepath}...")
    all_skills = parse_allskills_file(filepath)
    print(f"Total skills parsed: {len(all_skills)}")

    # Analyze Grade 6 skills
    print("\nAnalyzing all Grade 6 skills...")
    analysis = analyze_grade6_skills(all_skills)

    # Generate summary
    summary = generate_summary_stats(analysis)

    # Print summary
    print("\n" + "=" * 80)
    print("SUMMARY STATISTICS")
    print("=" * 80)
    print(f"Total Grade 6 skills found: {summary['total_grade6_skills']}")
    print(f"Topics with Grade 6 skills: {summary['topics_with_grade6']}")
    print(f"X-2 rule violations: {summary['total_x_minus_2_violations']}")
    print(f"Potential circular dependencies: {summary['total_circular_issues']}")
    print(f"Skills needing updates: {summary['skills_needing_updates']}")

    print("\nGrade 6 skills by topic:")
    for topic, count in sorted(summary['topics_breakdown'].items()):
        print(f"  {topic}: {count} skills")

    # Save full analysis
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/GRADE6_COMPREHENSIVE_ANALYSIS.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({
            'summary': summary,
            'full_analysis': analysis
        }, f, indent=2)

    print(f"\nFull analysis saved to: {output_file}")

    # Generate readable report
    report_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/GRADE6_ANALYSIS_REPORT.md'
    generate_markdown_report(analysis, summary, report_file)
    print(f"Readable report saved to: {report_file}")

    print("\nAnalysis complete!")

def generate_markdown_report(analysis: Dict, summary: Dict, output_file: str):
    """Generate a readable markdown report"""

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Grade 6 Skills - Comprehensive Analysis Report\n\n")
        f.write("## Executive Summary\n\n")
        f.write(f"- **Total Grade 6 Skills**: {summary['total_grade6_skills']}\n")
        f.write(f"- **Topics with Grade 6 Skills**: {summary['topics_with_grade6']}\n")
        f.write(f"- **X-2 Rule Violations**: {summary['total_x_minus_2_violations']}\n")
        f.write(f"- **Skills Needing Updates**: {summary['skills_needing_updates']}\n\n")

        f.write("## Grade 6 Skills Distribution by Topic\n\n")
        for topic, count in sorted(summary['topics_breakdown'].items()):
            f.write(f"- **{topic}**: {count} skills\n")

        f.write("\n## Detailed Analysis by Topic\n\n")

        for topic in sorted(analysis['skills_by_topic'].keys()):
            topic_data = analysis['skills_by_topic'][topic]
            f.write(f"### {topic} ({topic_data['count']} skills)\n\n")

            for skill in topic_data['skills']:
                skill_id = skill['id']
                f.write(f"#### {skill_id}\n")
                f.write(f"**Skill**: {skill['skill_name']}\n\n")
                f.write(f"**Description**: {skill['description']}\n\n")
                f.write(f"**Current Dependencies**: {len(skill['dependencies'])}\n")

                if skill['dependencies']:
                    for dep in skill['dependencies']:
                        f.write(f"  - {dep}\n")
                else:
                    f.write("  - None\n")

                # Add recommendations if any
                if skill_id in analysis['recommendations']:
                    rec = analysis['recommendations'][skill_id]

                    if rec['issues']:
                        f.write("\n**Issues Found**:\n")
                        for issue in rec['issues']:
                            f.write(f"  - {issue}\n")

                    if rec['add_dependencies']:
                        f.write("\n**Recommended Additions**:\n")
                        for add_dep in rec['add_dependencies']:
                            f.write(f"  - {add_dep['dep_id']}: {add_dep['reason']}\n")

                    if rec['remove_dependencies']:
                        f.write("\n**Recommended Removals**:\n")
                        for rem_dep in rec['remove_dependencies']:
                            f.write(f"  - {rem_dep['dep_id']}: {rem_dep['reason']}\n")

                f.write("\n---\n\n")

        f.write("\n## X-2 Rule Violations\n\n")
        if analysis['violations']['x_minus_2_violations']:
            for violation in analysis['violations']['x_minus_2_violations']:
                f.write(f"- **{violation['skill_id']}**: {violation['issue']}\n")
        else:
            f.write("No X-2 rule violations found.\n")

        f.write("\n## Recommendations Summary\n\n")
        f.write(f"Total skills with recommendations: {len(analysis['recommendations'])}\n\n")

        for skill_id, rec in sorted(analysis['recommendations'].items()):
            f.write(f"### {skill_id}: {rec['skill_name']}\n")
            f.write(f"- Current dependencies: {len(rec['current_deps'])}\n")
            f.write(f"- Issues: {len(rec['issues'])}\n")
            f.write(f"- Additions suggested: {len(rec['add_dependencies'])}\n")
            f.write(f"- Removals suggested: {len(rec['remove_dependencies'])}\n\n")

if __name__ == '__main__':
    main()
