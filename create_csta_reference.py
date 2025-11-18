#!/usr/bin/env python3
"""
Create a comprehensive CSTA Standards Reference document
organized for easy lookup and curriculum alignment.
"""
import json

# Load extracted standards
with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/csta_standards_extracted.json', 'r') as f:
    data = json.load(f)

standards = data['standards']
topic_areas = data['topic_areas']
by_topic_grade = data['by_topic_grade']

# Generate markdown document
md = """# CSTA K-8 Standards Reference

**Generated:** 2025-11-17
**Source:** CSTA PreK-12 Computer Science Standards Draft 2.0
**Scope:** Kindergarten through Grade 8 (Elementary K-5, Middle School 6-8)

## Overview

This reference organizes all **{total} K-8 CSTA standards** by:
- **5 Topic Areas**: Algorithms & Design, Programming, Data & Analysis, Systems & Security, Computing & Society
- **7 Grade Levels**: K, 1, 2, 3, 4, 5, and 6-8 (Middle School)

Each standard follows this naming convention:
- **Grade Band**: `EK` (PreK-K), `E1`-`E5` (Grades 1-5), `MS` (Middle School 6-8)
- **Topic Area**: `ALG`, `PRO`, `DAA`, `SAS`, `CAS`
- **Subtopic**: Two-letter code (e.g., `AF` = Algorithm Fundamentals)
- **Number**: Sequential number within topic area

**Example**: `E3-PRO-PF-01` = Elementary Grade 3, Programming, Programming Fundamentals, Standard 01

---

## Table of Contents

1. [Algorithms and Design (ALG)](#algorithms-and-design-alg) - {alg_count} standards
2. [Programming (PRO)](#programming-pro) - {pro_count} standards
3. [Data and Analysis (DAA)](#data-and-analysis-daa) - {daa_count} standards
4. [Systems and Security (SAS)](#systems-and-security-sas) - {sas_count} standards
5. [Computing and Society (CAS)](#computing-and-society-cas) - {cas_count} standards

---

""".format(
    total=len(standards),
    alg_count=sum(len(by_topic_grade['ALG'][g]) for g in by_topic_grade['ALG']),
    pro_count=sum(len(by_topic_grade['PRO'][g]) for g in by_topic_grade['PRO']),
    daa_count=sum(len(by_topic_grade['DAA'][g]) for g in by_topic_grade['DAA']),
    sas_count=sum(len(by_topic_grade['SAS'][g]) for g in by_topic_grade['SAS']),
    cas_count=sum(len(by_topic_grade['CAS'][g]) for g in by_topic_grade['CAS'])
)

# Generate each topic area section
for topic_code in ['ALG', 'PRO', 'DAA', 'SAS', 'CAS']:
    topic_name = topic_areas[topic_code]['name']
    topic_standards = by_topic_grade[topic_code]

    md += f"## {topic_name} ({topic_code})\n\n"

    # Get subtopics for this topic area
    subtopics = topic_areas[topic_code]['subtopics']

    # Organize by subtopic
    by_subtopic = {}
    for grade in ['EK', 'E1', 'E2', 'E3', 'E4', 'E5', 'MS']:
        for std in topic_standards[grade]:
            if std['subtopic'] not in by_subtopic:
                by_subtopic[std['subtopic']] = {
                    'name': std['subtopic_name'],
                    'standards': []
                }
            by_subtopic[std['subtopic']]['standards'].append(std)

    # Write each subtopic
    for subtopic_code, subtopic_data in sorted(by_subtopic.items()):
        md += f"### {subtopic_data['name']} ({topic_code}-{subtopic_code})\n\n"

        # Group by grade
        by_grade = {'K': [], '1': [], '2': [], '3': [], '4': [], '5': [], '6-8': []}
        for std in subtopic_data['standards']:
            by_grade[std['grade_level']].append(std)

        # Write standards by grade
        for grade_level in ['K', '1', '2', '3', '4', '5', '6-8']:
            if by_grade[grade_level]:
                grade_display = f"Grade {grade_level}" if grade_level != '6-8' else "Grades 6-8"
                md += f"**{grade_display}:**\n\n"
                for std in sorted(by_grade[grade_level], key=lambda x: x['code']):
                    md += f"- **{std['code']}**: {std['description']}\n"
                md += "\n"

        md += "---\n\n"

# Add quick reference table
md += """## Quick Reference: Standards by Grade Level

### Kindergarten (K)

| Topic Area | Count | Codes |
|------------|-------|-------|
"""

grade_summary = {}
for grade in ['K', '1', '2', '3', '4', '5', '6-8']:
    grade_summary[grade] = {}
    for topic_code in ['ALG', 'PRO', 'DAA', 'SAS', 'CAS']:
        grade_key = 'EK' if grade == 'K' else f'E{grade}' if grade != '6-8' else 'MS'
        stds = by_topic_grade[topic_code][grade_key]
        grade_summary[grade][topic_code] = {
            'count': len(stds),
            'codes': [s['code'] for s in stds]
        }

for topic_code in ['ALG', 'PRO', 'DAA', 'SAS', 'CAS']:
    count = grade_summary['K'][topic_code]['count']
    codes = ', '.join(grade_summary['K'][topic_code]['codes'])
    md += f"| {topic_areas[topic_code]['name']} | {count} | {codes} |\n"

md += "\n"

# Add other grades
for grade in ['1', '2', '3', '4', '5', '6-8']:
    grade_display = f"Grade {grade}" if grade != '6-8' else "Grades 6-8 (Middle School)"
    md += f"### {grade_display}\n\n"
    md += "| Topic Area | Count | Sample Codes |\n"
    md += "|------------|-------|-------------|\n"

    for topic_code in ['ALG', 'PRO', 'DAA', 'SAS', 'CAS']:
        count = grade_summary[grade][topic_code]['count']
        codes = grade_summary[grade][topic_code]['codes'][:3]
        code_str = ', '.join(codes)
        if len(grade_summary[grade][topic_code]['codes']) > 3:
            code_str += ', ...'
        md += f"| {topic_areas[topic_code]['name']} | {count} | {code_str} |\n"

    md += "\n"

# Add mapping guide
md += """---

## CreatiCode Topic to CSTA Topic Area Mapping

This mapping helps identify which CSTA standards apply to each CreatiCode topic:

| CreatiCode Domain | CreatiCode Topics | Primary CSTA Topic Area | Secondary CSTA Areas |
|-------------------|-------------------|-------------------------|---------------------|
| D1: Algorithms & Design | T01-T05 | ALG (Algorithms and Design) | PRO (for implementation) |
| D2: Programming Core | T06-T13 | PRO (Programming) | ALG (for algorithm design) |
| D3: Applications & AI | T14-T24 | PRO, DAA (for AI/data) | CAS (for AI ethics/society) |
| D4: Data & Analysis | T25-T29 | DAA (Data and Analysis) | PRO (for data processing code) |
| D5: Systems & Society | T30-T36 | SAS, CAS | All (cross-cutting) |

### Detailed Topic Mappings

**T01: Algorithms (Sequencing, Planning, Algorithms)** → `ALG-AF` (Algorithm Fundamentals)

**T02: Abstraction & Models** → `ALG-PS` (Problem Solving - decomposition), `PRO-PD` (Program Development)

**T03: Decomposition** → `ALG-PS` (Problem Solving)

**T04: Pattern Recognition** → `ALG-AF`, `ALG-PS`

**T05: Design & Human-Computer Interaction** → `ALG-HD` (Human-Centered Design)

**T06: Events** → `PRO-PF` (Programming Fundamentals)

**T07: Loops** → `PRO-PF` (Programming Fundamentals)

**T08: Conditionals** → `PRO-PF` (Programming Fundamentals)

**T09: Variables & Expressions** → `PRO-DH` (Data Handling)

**T10: Lists & Arrays** → `PRO-DH` (Data Handling)

**T11: Functions & Procedures** → `PRO-PD` (Program Development - modularity)

**T12: Organization & Modularity** → `PRO-PD` (Program Development)

**T13: Debugging & Testing** → `PRO-TR` (Testing and Refining Code)

**T14: 2D Games** → `PRO-PF`, `PRO-PD`, `ALG-AF` (game algorithms)

**T15: Animation & Storytelling** → `PRO-PF`, `CAS-ET` (creative technologies)

**T16: UI & Widgets** → `ALG-HD` (Human-Centered Design), `PRO-PF`

**T17: Physics Simulations** → `PRO-PF`, `ALG-AF` (simulation algorithms)

**T18: 3D Graphics & Spatial Reasoning** → `PRO-PF`, `ALG-AF`

**T19: Multiplayer & Networking** → `SAS-NW` (Networks), `PRO-PF`

**T20: Algorithmic Art & Creative Coding** → `PRO-PF`, `ALG-AF`

**T21: AI Media Tools & Creative Assets** → `DAA-IM` (AI impacts), `CAS-ET` (emerging tech)

**T22: AI Chatbots & Information Apps** → `DAA-IM`, `PRO-PF`, `CAS-ET`

**T23: AI Voice, Vision & Gesture** → `DAA-IM`, `SAS-HW` (sensors), `CAS-ET`

**T24: XO & AI-Supported Coding** → `PRO-PD` (AI tools), `CAS-ET`, `DAA-IM`

**T25: Data Representation & Types** → `DAA-DF` (Data Fundamentals)

**T26: Data Collection & Measurement** → `DAA-DF` (Data Fundamentals)

**T27: Data Analysis & Visualization** → `DAA-DI` (Data Investigations)

**T28: Probability & Sampling** → `DAA-DI` (Data Investigations)

**T29: Text Analysis & NLP** → `DAA-DI`, `DAA-IM` (AI/ML)

**T30: Hardware & Devices** → `SAS-HW` (Hardware and Software)

**T31: Internet & Networks** → `SAS-NW` (Networks)

**T32: Privacy & Cybersecurity** → `SAS-SC` (Security)

**T33: APIs & Cloud Services** → `SAS-HW`, `SAS-NW`

**T34: History of Computing** → `CAS-HC` (History of Computing)

**T35: Impacts of Computing, Games & AI** → `SAS-IM`, `DAA-IM`, `ALG-IM`, `CAS-ET`

**T36: Ethics, Careers, Collaboration** → `CAS-CE` (Career Exploration), All `IM` subtopics (Ethics)

---

## Using This Reference

**For Curriculum Developers:**
1. Identify which CreatiCode topics you're teaching
2. Look up the corresponding CSTA topic areas above
3. Find the grade-appropriate standards in the sections above
4. Map specific skills to specific standards

**For Standards Alignment:**
1. Start with the grade level you're targeting
2. Review all standards for that grade in relevant topic areas
3. Map each CreatiCode skill to 1-3 CSTA standards
4. Verify full coverage across all CSTA topic areas

**For Assessment:**
1. Use CSTA standards as learning objectives
2. Design auto-gradable activities that demonstrate standard mastery
3. Track student progress across all K-8 standards

---

**Document Version:** 1.0
**Last Updated:** 2025-11-17
**Standards Source:** CSTA PreK-12 CS Standards Draft 2.0 (2025)
"""

# Write to file
with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/CSTA_STANDARDS_REFERENCE.md', 'w') as f:
    f.write(md)

print("Created CSTA_STANDARDS_REFERENCE.md")
print(f"Total standards documented: {len(standards)}")
print(f"Document length: {len(md)} characters, {len(md.split())} words")
