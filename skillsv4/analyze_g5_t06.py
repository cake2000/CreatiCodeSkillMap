#!/usr/bin/env python3
"""
Analyze Grade 5 skills to determine which need T06 dependencies added.
Following the same criteria used for Grade 4.
"""

import re

# Decision criteria
NEEDS_T06_KEYWORDS = [
    'build', 'create', 'implement', 'write', 'code', 'program', 'script',
    'design', 'construct', 'develop', 'add', 'spawn', 'configure', 'use',
    'apply', 'combine', 'nest', 'modify', 'update', 'store', 'define',
    'refactor', 'organize', 'attach', 'lock', 'pin', 'control', 'fix',
    'loop', 'conditional', 'variable', 'function', 'game', 'interaction',
    'event', 'broadcast', 'simulate', 'compute', 'track', 'maintain'
]

NO_T06_KEYWORDS = [
    'trace', 'read', 'analyze', 'debug', 'compare', 'describe', 'explain',
    'identify', 'recognize', 'match', 'determine', 'predict', 'label',
    'document', 'choose', 'select', 'distinguish', 'examine', 'flag',
    'highlight', 'list', 'mark'
]

def parse_skills(content):
    """Parse all G5 skills from allskills.md"""
    skills = []

    # Split by skill ID markers
    parts = re.split(r'\n(?=ID: T\d+\.G5\.\d+)', content)

    for part in parts:
        if not part.startswith('ID: T') or '.G5.' not in part:
            continue

        lines = part.split('\n')
        skill_data = {
            'id': '',
            'topic': '',
            'skill': '',
            'description': '',
            'dependencies': [],
            'has_t06': False
        }

        i = 0
        while i < len(lines):
            line = lines[i].strip()

            if line.startswith('ID:'):
                skill_data['id'] = line.replace('ID:', '').strip()
            elif line.startswith('Topic:'):
                skill_data['topic'] = line.replace('Topic:', '').strip()
            elif line.startswith('Skill:'):
                skill_data['skill'] = line.replace('Skill:', '').strip()
            elif line.startswith('Description:'):
                skill_data['description'] = line.replace('Description:', '').strip()
            elif line.startswith('Dependencies:'):
                # Collect all dependency lines
                i += 1
                while i < len(lines) and lines[i].startswith('*'):
                    dep = lines[i].strip()
                    skill_data['dependencies'].append(dep)
                    if 'T06.' in dep:
                        skill_data['has_t06'] = True
                    i += 1
                continue

            i += 1

        if skill_data['id']:
            skills.append(skill_data)

    return skills

def analyze_skill(skill):
    """
    Determine if a skill needs T06 based on Grade 4 criteria:
    - Needs T06: Skills where students BUILD/IMPLEMENT executable code
    - Don't need T06: Skills focused on ANALYSIS/TRACING existing code or pure conceptual understanding
    """
    text = (skill['skill'] + ' ' + skill['description']).lower()

    # Check for explicit indicators
    if 'students trace' in text or 'trace a' in text or 'trace code' in text:
        return False, "Tracing exercise"

    if 'students analyze' in text or 'analyze a' in text or 'analyze code' in text:
        return False, "Analysis exercise"

    if 'students debug' in text and 'fix' not in text[:100]:
        return False, "Debugging analysis only"

    if 'students compare' in text or 'compare two' in text:
        return False, "Comparison exercise"

    if 'students identify' in text or 'students recognize' in text or 'students label' in text:
        return False, "Recognition/identification exercise"

    if 'students match' in text or 'students describe' in text or 'students explain' in text:
        return False, "Conceptual understanding"

    # Check for implementation keywords
    impl_keywords = [
        'students build', 'students create', 'students implement', 'students write',
        'students code', 'students program', 'students script', 'students design',
        'students add', 'students use', 'students apply', 'students combine',
        'students configure', 'students control', 'students spawn', 'students loop',
        'students modify', 'students update', 'students store', 'students define',
        'students compute', 'students simulate', 'students fix', 'students attach',
        'students lock', 'students pin', 'students track', 'students maintain'
    ]

    for keyword in impl_keywords:
        if keyword in text:
            return True, f"Implementation task: {keyword}"

    # Check skill title for strong indicators
    title_lower = skill['skill'].lower()

    if any(word in title_lower for word in ['build', 'create', 'implement', 'write', 'add', 'use', 'apply', 'configure', 'control']):
        # But not if it's analysis
        if not any(word in title_lower for word in ['trace', 'analyze', 'identify', 'recognize', 'describe', 'explain', 'match']):
            return True, "Implementation verb in title"

    # Default to needing T06 for ambiguous cases in programming topics
    topic_code = skill['id'].split('.')[0]
    if topic_code in ['T07', 'T08', 'T09', 'T10', 'T11', 'T12', 'T13', 'T14', 'T15', 'T16', 'T17', 'T18', 'T19', 'T20']:
        # These are programming topics - be more aggressive
        if not any(word in text for word in ['trace', 'analyze', 'read', 'predict', 'examine', 'label', 'describe', 'explain']):
            return True, "Programming topic - likely implementation"

    return False, "No clear implementation indicators"

def determine_t06_type(skill):
    """Determine which T06 dependency to add"""
    text = (skill['skill'] + ' ' + skill['description']).lower()

    # Check for user input/control indicators
    if any(word in text for word in ['key', 'keyboard', 'press', 'user input', 'control', 'player control']):
        return 'T06.G3.02'

    # Default to green flag
    return 'T06.G3.01'

def main():
    with open('allskills.md', 'r') as f:
        content = f.read()

    skills = parse_skills(content)
    print(f"Total G5 skills found: {len(skills)}\n")

    # Categorize skills
    needs_t06 = []
    has_t06 = []
    no_t06_needed = []

    for skill in skills:
        if skill['has_t06']:
            has_t06.append(skill)
        else:
            need, reason = analyze_skill(skill)
            if need:
                t06_type = determine_t06_type(skill)
                needs_t06.append((skill, t06_type, reason))
            else:
                no_t06_needed.append((skill, reason))

    print(f"Skills already with T06: {len(has_t06)}")
    print(f"Skills needing T06 added: {len(needs_t06)}")
    print(f"Skills NOT needing T06: {len(no_t06_needed)}\n")

    # Group by topic
    from collections import defaultdict

    print("="*80)
    print("LIST A: SKILLS NEEDING T06 ({})\n".format(len(needs_t06)))
    print("="*80)

    by_topic = defaultdict(list)
    for skill, t06_type, reason in needs_t06:
        topic_code = skill['id'].split('.')[0]
        by_topic[topic_code].append((skill, t06_type, reason))

    for topic_code in sorted(by_topic.keys()):
        skills_in_topic = by_topic[topic_code]
        print(f"\n{'='*80}")
        print(f"{topic_code}: {len(skills_in_topic)} skills need T06")
        print('='*80)

        for skill, t06_type, reason in skills_in_topic:
            print(f"\nID: {skill['id']}")
            print(f"Skill: {skill['skill']}")
            print(f"Add: {t06_type}")
            print(f"Reason: {reason}")
            desc = skill['description']
            if len(desc) > 200:
                desc = desc[:200] + "..."
            print(f"Description: {desc}")

    print("\n")
    print("="*80)
    print("LIST B: SKILLS NOT NEEDING T06 ({})\n".format(len(no_t06_needed)))
    print("="*80)

    by_topic_no = defaultdict(list)
    for skill, reason in no_t06_needed:
        topic_code = skill['id'].split('.')[0]
        by_topic_no[topic_code].append((skill, reason))

    for topic_code in sorted(by_topic_no.keys()):
        skills_in_topic = by_topic_no[topic_code]
        print(f"\n{topic_code}: {len(skills_in_topic)} skills")
        for skill, reason in skills_in_topic:
            print(f"  - {skill['id']}: {skill['skill']}")
            print(f"    Reason: {reason}")

    print("\n")
    print("="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Total G5 skills: {len(skills)}")
    print(f"Already have T06: {len(has_t06)}")
    print(f"Need T06 added: {len(needs_t06)}")
    print(f"Don't need T06: {len(no_t06_needed)}")
    print()

    # Count T06 types
    t06_g3_01 = sum(1 for _, t06_type, _ in needs_t06 if t06_type == 'T06.G3.01')
    t06_g3_02 = sum(1 for _, t06_type, _ in needs_t06 if t06_type == 'T06.G3.02')
    print(f"T06.G3.01 (green flag): {t06_g3_01}")
    print(f"T06.G3.02 (key press): {t06_g3_02}")

if __name__ == '__main__':
    main()
