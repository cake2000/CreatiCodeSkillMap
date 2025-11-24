#!/usr/bin/env python3
"""
Comprehensive Grade K Skills Extractor and Analyzer
Extracts ALL Grade K skills and performs dependency analysis
"""

import re
import json
from collections import defaultdict

def extract_grade_k_skills(filepath):
    """Extract all Grade K skills from allskills.md"""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    grade_k_skills = []

    # Extract ALL skills with ID T##.GK.##
    # Each skill starts with "ID: T##.GK.##"
    skill_pattern = r'ID:\s+(T\d+\.GK\.\d+)(.*?)(?=\nID:\s+T\d+\.|^# T\d+|\Z)'
    skills = re.finditer(skill_pattern, content, re.DOTALL | re.MULTILINE)

    for skill_match in skills:
        skill_id = skill_match.group(1)
        skill_content = skill_match.group(2)

        # Extract topic ID from skill ID
        topic_match = re.match(r'(T\d+)\.GK\.\d+', skill_id)
        topic_id = topic_match.group(1) if topic_match else "Unknown"

        skill_data = {
            'id': skill_id,
            'topic_id': topic_id,
            'topic_name': '',
            'title': '',
            'description': '',
            'dependencies': [],
            'csta_codes': [],
            'ai4k12': None
        }

        # Extract Topic line
        topic_pattern = r'Topic:\s+(T\d+)\s+[–-]\s+(.+?)(?=\n)'
        topic_match = re.search(topic_pattern, skill_content)
        if topic_match:
            skill_data['topic_name'] = topic_match.group(2).strip()

        # Extract Skill (title) line
        skill_title_pattern = r'Skill:\s+(.+?)(?=\n)'
        skill_title_match = re.search(skill_title_pattern, skill_content)
        if skill_title_match:
            skill_data['title'] = skill_title_match.group(1).strip()

        # Extract Description
        desc_pattern = r'Description:\s+(.+?)(?=\n(?:Dependencies:|CSTA:|AI4K12:|\n\n|$))'
        desc_match = re.search(desc_pattern, skill_content, re.DOTALL)
        if desc_match:
            skill_data['description'] = desc_match.group(1).strip()

        # Extract Dependencies (list format with asterisks)
        dep_section_pattern = r'Dependencies:(.*?)(?=\n(?:CSTA:|AI4K12:|\n\n|ID:|\Z))'
        dep_section_match = re.search(dep_section_pattern, skill_content, re.DOTALL)
        if dep_section_match:
            dep_section = dep_section_match.group(1)
            # Extract each dependency line starting with *
            dep_lines = re.findall(r'\*\s+(T\d+\.G[KX\d]+\.\d+(?:\.\d+)?)', dep_section)
            skill_data['dependencies'] = dep_lines

        # Extract CSTA codes
        csta_pattern = r'CSTA:\s*([^\n]+)'
        csta_match = re.search(csta_pattern, skill_content)
        if csta_match:
            csta_str = csta_match.group(1).strip()
            # Split by comma or semicolon
            csta_codes = [c.strip() for c in re.split(r'[,;]', csta_str) if c.strip()]
            skill_data['csta_codes'] = csta_codes

        # Extract AI4K12
        ai_pattern = r'AI4K12:\s*(.+?)(?=\n|$)'
        ai_match = re.search(ai_pattern, skill_content)
        if ai_match:
            skill_data['ai4k12'] = ai_match.group(1).strip()

        grade_k_skills.append(skill_data)

    return grade_k_skills

def analyze_dependencies(skills):
    """Analyze dependency patterns and violations"""

    analysis = {
        'total_skills': len(skills),
        'skills_by_topic': defaultdict(list),
        'dependency_violations': [],
        'missing_cross_topic_deps': [],
        'dependency_stats': {
            'no_deps': 0,
            'with_deps': 0,
            'avg_deps': 0
        }
    }

    # Group by topic
    for skill in skills:
        analysis['skills_by_topic'][skill['topic_id']].append(skill)

    # Analyze each skill
    total_deps = 0
    for skill in skills:
        deps = skill['dependencies']

        if not deps:
            analysis['dependency_stats']['no_deps'] += 1
        else:
            analysis['dependency_stats']['with_deps'] += 1
            total_deps += len(deps)

            # Check for violations (Grade K should only depend on Grade K)
            for dep in deps:
                # Parse dependency grade
                dep_match = re.match(r'T\d+\.G([KX\d]+)\.\d+', dep)
                if dep_match:
                    dep_grade = dep_match.group(1)
                    if dep_grade != 'K':
                        analysis['dependency_violations'].append({
                            'skill_id': skill['id'],
                            'skill_title': skill['title'],
                            'invalid_dependency': dep,
                            'issue': f"Grade K skill depends on Grade {dep_grade} skill"
                        })

    if analysis['dependency_stats']['with_deps'] > 0:
        analysis['dependency_stats']['avg_deps'] = total_deps / analysis['dependency_stats']['with_deps']

    return analysis

def generate_report(skills, analysis, output_file):
    """Generate comprehensive markdown report"""

    report = []
    report.append("# COMPREHENSIVE GRADE K SKILLS ANALYSIS")
    report.append(f"\nGenerated: 2025-11-24")
    report.append(f"\n## Executive Summary\n")
    report.append(f"- **Total Grade K Skills Found:** {analysis['total_skills']}")
    report.append(f"- **Topics with Grade K Skills:** {len(analysis['skills_by_topic'])}")
    report.append(f"- **Skills with Dependencies:** {analysis['dependency_stats']['with_deps']}")
    report.append(f"- **Skills without Dependencies:** {analysis['dependency_stats']['no_deps']}")
    report.append(f"- **Average Dependencies per Skill (when >0):** {analysis['dependency_stats']['avg_deps']:.2f}")
    report.append(f"- **Dependency Violations Found:** {len(analysis['dependency_violations'])}")

    # List all topics with Grade K skills
    report.append(f"\n## Topics with Grade K Skills\n")
    for topic_id in sorted(analysis['skills_by_topic'].keys()):
        topic_skills = analysis['skills_by_topic'][topic_id]
        topic_name = topic_skills[0]['topic_name'] if topic_skills else "Unknown"
        report.append(f"- **{topic_id}**: {topic_name} ({len(topic_skills)} skills)")

    # Detailed skill listing by topic
    report.append(f"\n## All Grade K Skills by Topic\n")

    for topic_id in sorted(analysis['skills_by_topic'].keys()):
        topic_skills = analysis['skills_by_topic'][topic_id]
        topic_name = topic_skills[0]['topic_name'] if topic_skills else "Unknown"

        report.append(f"\n### {topic_id}: {topic_name}\n")

        for skill in sorted(topic_skills, key=lambda x: x['id']):
            report.append(f"\n#### {skill['id']}: {skill['title']}\n")
            report.append(f"**Description:** {skill['description']}\n")
            report.append(f"**Dependencies:** {', '.join(skill['dependencies']) if skill['dependencies'] else 'None'}\n")
            report.append(f"**CSTA Codes:** {', '.join(skill['csta_codes']) if skill['csta_codes'] else 'None'}\n")
            if skill['ai4k12']:
                report.append(f"**AI4K12:** {skill['ai4k12']}\n")

    # Dependency violations
    if analysis['dependency_violations']:
        report.append(f"\n## DEPENDENCY VIOLATIONS (Grade K depending on other grades)\n")
        for violation in analysis['dependency_violations']:
            report.append(f"\n### {violation['skill_id']}: {violation['skill_title']}")
            report.append(f"- **Invalid Dependency:** {violation['invalid_dependency']}")
            report.append(f"- **Issue:** {violation['issue']}\n")
    else:
        report.append(f"\n## Dependency Violations\n")
        report.append("✅ No violations found. All Grade K skills only depend on other Grade K skills.\n")

    # Skills with no dependencies (potential issues)
    report.append(f"\n## Skills with No Dependencies (Foundational Skills)\n")
    for topic_id in sorted(analysis['skills_by_topic'].keys()):
        topic_skills = [s for s in analysis['skills_by_topic'][topic_id] if not s['dependencies']]
        if topic_skills:
            report.append(f"\n### {topic_id}: {topic_skills[0]['topic_name']}\n")
            for skill in sorted(topic_skills, key=lambda x: x['id']):
                report.append(f"- **{skill['id']}**: {skill['title']}")

    # Write report
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report))

    print(f"Report written to: {output_file}")
    print(f"Total Grade K skills found: {analysis['total_skills']}")
    print(f"Topics covered: {len(analysis['skills_by_topic'])}")
    print(f"Dependency violations: {len(analysis['dependency_violations'])}")

def main():
    input_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/GRADE_K_COMPREHENSIVE_ANALYSIS.md'
    json_output = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/grade_k_skills.json'

    print("Extracting Grade K skills...")
    skills = extract_grade_k_skills(input_file)

    print(f"Found {len(skills)} Grade K skills")

    print("Analyzing dependencies...")
    analysis = analyze_dependencies(skills)

    print("Generating report...")
    generate_report(skills, analysis, output_file)

    # Save JSON
    with open(json_output, 'w', encoding='utf-8') as f:
        json.dump(skills, f, indent=2, ensure_ascii=False)
    print(f"JSON data written to: {json_output}")

if __name__ == '__main__':
    main()
