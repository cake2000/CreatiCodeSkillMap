#!/usr/bin/env python3
"""
Final analyzer for Grade 3 cross-topic dependencies in Topics T25-T36
Provides SPECIFIC skill IDs to add as dependencies
"""

import re

def extract_all_skills(filename):
    """Extract ALL skills"""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    skill_blocks = re.split(r'\n(?=ID: T\d+\.)', content)

    all_skills = {}

    for block in skill_blocks:
        if not block.strip() or not block.startswith('ID: '):
            continue

        lines = block.split('\n')
        skill = {
            'id': '',
            'topic': '',
            'skill_name': '',
            'description': '',
            'dependencies': []
        }

        in_dependencies = False

        for line in lines:
            line = line.strip()

            if line.startswith('ID: '):
                skill['id'] = line.replace('ID: ', '').strip()
            elif line.startswith('Topic: '):
                skill['topic'] = line.replace('Topic: ', '').strip()
            elif line.startswith('Skill: '):
                skill['skill_name'] = line.replace('Skill: ', '').strip()
            elif line.startswith('Description: '):
                skill['description'] = line.replace('Description: ', '').strip()
            elif line.startswith('Dependencies:'):
                in_dependencies = True
            elif in_dependencies and line.startswith('* '):
                dep_line = line[2:]
                if ':' in dep_line:
                    dep_id = dep_line.split(':')[0].strip()
                    skill['dependencies'].append(dep_id)
            elif in_dependencies and not line.startswith('* ') and line:
                in_dependencies = False

        if skill['id']:
            all_skills[skill['id']] = skill

    return all_skills

def find_appropriate_dependency(all_skills, topic_prefix, max_grade='G3'):
    """Find the most appropriate skill from a topic at or below max_grade"""
    grade_order = ['GK', 'G1', 'G2', 'G3']
    max_grade_idx = grade_order.index(max_grade)

    # Try to find skills at each grade level, preferring lower grades
    for grade in grade_order[:max_grade_idx + 1]:
        # Look for foundational skills
        for skill_id, skill in all_skills.items():
            if skill_id.startswith(f'{topic_prefix}.{grade}.'):
                # Prefer early skills (01, 02, etc.)
                if re.search(r'\.0[12]$', skill_id):
                    return skill_id, skill['skill_name']

    # If no foundational skill found, return any skill from that topic
    for grade in grade_order[:max_grade_idx + 1]:
        for skill_id, skill in all_skills.items():
            if skill_id.startswith(f'{topic_prefix}.{grade}.'):
                return skill_id, skill['skill_name']

    return None, None

def analyze_with_specific_deps(all_skills):
    """Analyze Grade 3 T25-T36 skills with specific dependency recommendations"""
    recommendations = []

    # Filter Grade 3 skills from T25-T36
    grade3_skills = []
    for skill_id, skill in all_skills.items():
        if '.G3.' in skill_id:
            try:
                topic_num = int(skill_id.split('.')[0][1:])
                if 25 <= topic_num <= 36:
                    grade3_skills.append(skill)
            except:
                pass

    for skill in grade3_skills:
        skill_id = skill['id']
        description = (skill['description'] + ' ' + skill['skill_name']).lower()
        current_deps = set(skill['dependencies'])
        current_topic = skill_id.split('.')[0]

        missing = []

        # Check for each type of cross-topic dependency
        checks = [
            {
                'patterns': [r'\brepeat\b', r'\bloop\b', r'\bforever\b', r'\btimes\b', r'\buntil\b', r'\bwhile\b', r'\bfor each\b', r'\biterat'],
                'topic': 'T07',
                'name': 'Loops/Repetition'
            },
            {
                'patterns': [r'\bif\b', r'\bwhen\b', r'\bcheck\b', r'\bcondition\b', r'\bchoose\b', r'\bdecide\b', r'\bcompare\b', r'\belse\b', r'\bgreater\b', r'\bless\b', r'\bequal'],
                'topic': 'T08',
                'name': 'Conditionals'
            },
            {
                'patterns': [r'\bvariable\b', r'\bstore\b', r'\bsave\b', r'\bvalue\b', r'\bscore\b', r'\bcounter\b', r'\btrack\b', r'\bset.*to\b', r'\bchange.*by\b'],
                'topic': 'T09',
                'name': 'Variables'
            },
            {
                'patterns': [r'\blist\b', r'\barray\b', r'\bcollection\b', r'\bdataset\b', r'\bitems?\b', r'\badd.*to.*list\b'],
                'topic': 'T10',
                'name': 'Lists'
            },
            {
                'patterns': [r'\bevent\b', r'\btrigger\b', r'\bwhen clicked\b', r'\bwhen pressed\b', r'\bbroadcast\b', r'\bmessage\b', r'\bgreen flag\b'],
                'topic': 'T06',
                'name': 'Events'
            },
            {
                'patterns': [r'\brandom\b', r'\bchance\b', r'\bprobability\b', r'\bpick\b'],
                'topic': 'T11',
                'name': 'Random'
            },
            {
                'patterns': [r'\bsequence\b', r'\bsteps\b', r'\border\b', r'\balgorithm\b', r'\bprocedure\b'],
                'topic': 'T01',
                'name': 'Algorithms'
            },
            {
                'patterns': [r'\bbutton\b', r'\bclick\b', r'\binput\b', r'\buser\b', r'\binterface\b', r'\bdisplay\b', r'\bshow\b', r'\bask\b', r'\banswer\b', r'\bsprite\b', r'\bstage\b', r'\bwidget\b'],
                'topic': 'T04',
                'name': 'User Interface'
            },
            {
                'patterns': [r'\bfunction\b', r'\bprocedure\b', r'\bcustom block\b', r'\bdefine\b', r'\breuse\b'],
                'topic': 'T05',
                'name': 'Functions'
            }
        ]

        for check in checks:
            if any(re.search(pattern, description) for pattern in check['patterns']):
                has_dep = any(dep.startswith(f"{check['topic']}.") for dep in current_deps)
                if not has_dep and current_topic != check['topic']:
                    dep_id, dep_name = find_appropriate_dependency(all_skills, check['topic'], 'G3')
                    if dep_id:
                        missing.append({
                            'topic': check['topic'],
                            'name': check['name'],
                            'dep_id': dep_id,
                            'dep_name': dep_name
                        })

        if missing:
            recommendations.append({
                'skill': skill,
                'missing': missing
            })

    return recommendations, len(grade3_skills)

def main():
    filename = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("Loading all skills...")
    all_skills = extract_all_skills(filename)
    print(f"Loaded {len(all_skills)} skills")

    print("\nAnalyzing Grade 3 T25-T36 cross-topic dependencies...")
    recommendations, total_skills = analyze_with_specific_deps(all_skills)

    # Output in requested format
    print(f"\n{'='*100}")
    print("GRADE 3 (T25-T36) MISSING CROSS-TOPIC DEPENDENCIES")
    print(f"{'='*100}\n")

    for rec in recommendations:
        skill = rec['skill']
        print(f"SKILL_ID: {skill['id']}")
        print(f"CURRENT_SKILL_NAME: {skill['skill_name']}")

        for miss in rec['missing']:
            print(f"ADD DEPENDENCY: {miss['dep_id']}: {miss['dep_name']}")
            print(f"REASON: Skill uses {miss['name'].lower()} concepts")

        print()

    # Save formatted recommendations
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/grade3_t25_t36_final_recommendations.txt'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("GRADE 3 (T25-T36) MISSING CROSS-TOPIC DEPENDENCIES\n")
        f.write("="*100 + "\n")
        f.write(f"Format: SKILL_ID → ADD DEPENDENCY → REASON\n")
        f.write("="*100 + "\n\n")

        for rec in recommendations:
            skill = rec['skill']
            f.write(f"SKILL_ID: {skill['id']}\n")
            f.write(f"CURRENT_SKILL_NAME: {skill['skill_name']}\n")

            for miss in rec['missing']:
                f.write(f"ADD DEPENDENCY: {miss['dep_id']}: {miss['dep_name']}\n")
                f.write(f"REASON: Skill uses {miss['name'].lower()} concepts\n")

            f.write("\n")

    print(f"{'='*100}")
    print(f"\nSummary:")
    print(f"  Total Grade 3 T25-T36 skills: {total_skills}")
    print(f"  Skills needing new dependencies: {len(recommendations)}")
    print(f"  Coverage: {len(recommendations)/total_skills*100:.1f}% need updates")
    print(f"\nRecommendations saved to: {output_file}")

if __name__ == '__main__':
    main()
