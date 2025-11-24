#!/usr/bin/env python3
"""
Comprehensive analyzer for Grade 3 cross-topic dependencies in Topics T25-T36
"""

import re

def extract_all_skills_by_grade(filename):
    """Extract ALL skills organized by grade"""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by skill ID pattern
    skill_blocks = re.split(r'\n(?=ID: T\d+\.)', content)

    all_skills = {}
    grade3_skills = []

    for block in skill_blocks:
        if not block.strip() or not block.startswith('ID: '):
            continue

        lines = block.split('\n')
        skill = {
            'id': '',
            'topic': '',
            'skill_name': '',
            'description': '',
            'dependencies': [],
            'raw': block
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
                dep_line = line[2:]  # Remove '* '
                if ':' in dep_line:
                    dep_id = dep_line.split(':')[0].strip()
                    skill['dependencies'].append(dep_id)
            elif in_dependencies and not line.startswith('* ') and line:
                in_dependencies = False

        if skill['id']:
            all_skills[skill['id']] = skill

            # Check if it's a Grade 3 skill in T25-T36
            if '.G3.' in skill['id']:
                try:
                    topic_num = int(skill['id'].split('.')[0][1:])
                    if 25 <= topic_num <= 36:
                        grade3_skills.append(skill)
                except:
                    pass

    return all_skills, grade3_skills

def get_grade_from_skill_id(skill_id):
    """Extract grade from skill ID (GK, G1, G2, G3, G4, G5)"""
    if '.GK.' in skill_id:
        return 'GK'
    match = re.search(r'\.G(\d+)\.', skill_id)
    if match:
        return f'G{match.group(1)}'
    return None

def analyze_cross_topic_dependencies(all_skills, grade3_skills):
    """Analyze Grade 3 skills for missing cross-topic dependencies"""
    recommendations = []

    for skill in grade3_skills:
        skill_id = skill['id']
        description = (skill['description'] + ' ' + skill['skill_name']).lower()
        current_deps = set(skill['dependencies'])

        missing = []

        # Get current topic
        current_topic = skill_id.split('.')[0]

        # Check for various cross-topic dependencies

        # T07 - Loops/Repetition
        loop_patterns = [
            r'\brepeat\b', r'\bloop\b', r'\bforever\b', r'\btimes\b',
            r'\buntil\b', r'\bwhile\b', r'\bfor each\b', r'\biterat',
            r'\bmultiple times\b', r'\brepetition\b'
        ]
        if any(re.search(pattern, description) for pattern in loop_patterns):
            has_loop_dep = any(dep.startswith('T07.') for dep in current_deps)
            if not has_loop_dep and current_topic != 'T07':
                # Find appropriate T07 dependency
                suggested = "T07.G2.01 or T07.G3.01"
                missing.append({
                    'topic': 'T07',
                    'name': 'Loops/Repetition',
                    'suggested': suggested,
                    'reason': 'Uses loops or repetition'
                })

        # T08 - Conditionals
        conditional_patterns = [
            r'\bif\b', r'\bwhen\b', r'\bcheck\b', r'\bcondition\b',
            r'\bchoose\b', r'\bdecide\b', r'\bcompare\b', r'\belse\b',
            r'\bgreater than\b', r'\bless than\b', r'\bequal\b'
        ]
        if any(re.search(pattern, description) for pattern in conditional_patterns):
            has_cond_dep = any(dep.startswith('T08.') for dep in current_deps)
            if not has_cond_dep and current_topic != 'T08':
                suggested = "T08.G2.01 or T08.G3.01"
                missing.append({
                    'topic': 'T08',
                    'name': 'Conditionals',
                    'suggested': suggested,
                    'reason': 'Uses conditionals/decisions'
                })

        # T09 - Variables
        variable_patterns = [
            r'\bvariable\b', r'\bstore\b', r'\bsave\b', r'\bvalue\b',
            r'\bscore\b', r'\bcounter\b', r'\btrack\b', r'\bset.*to\b',
            r'\bchange.*by\b'
        ]
        if any(re.search(pattern, description) for pattern in variable_patterns):
            has_var_dep = any(dep.startswith('T09.') for dep in current_deps)
            if not has_var_dep and current_topic != 'T09':
                suggested = "T09.G2.01 or T09.G3.01"
                missing.append({
                    'topic': 'T09',
                    'name': 'Variables',
                    'suggested': suggested,
                    'reason': 'Uses variables or data storage'
                })

        # T10 - Lists
        list_patterns = [
            r'\blist\b', r'\barray\b', r'\bcollection\b', r'\bdataset\b',
            r'\bitems?\b', r'\badd.*to.*list\b', r'\bremove.*from.*list\b'
        ]
        if any(re.search(pattern, description) for pattern in list_patterns):
            has_list_dep = any(dep.startswith('T10.') for dep in current_deps)
            if not has_list_dep and current_topic != 'T10':
                suggested = "T10.G2.01 or T10.G3.01"
                missing.append({
                    'topic': 'T10',
                    'name': 'Lists',
                    'suggested': suggested,
                    'reason': 'Uses lists or collections'
                })

        # T06 - Events
        event_patterns = [
            r'\bevent\b', r'\btrigger\b', r'\bwhen clicked\b', r'\bwhen pressed\b',
            r'\bbroadcast\b', r'\bmessage\b', r'\bgreen flag\b', r'\bkey press\b'
        ]
        if any(re.search(pattern, description) for pattern in event_patterns):
            has_event_dep = any(dep.startswith('T06.') for dep in current_deps)
            if not has_event_dep and current_topic != 'T06':
                suggested = "T06.G2.01 or T06.G3.01"
                missing.append({
                    'topic': 'T06',
                    'name': 'Events',
                    'suggested': suggested,
                    'reason': 'Uses events or triggers'
                })

        # T11 - Random
        random_patterns = [
            r'\brandom\b', r'\bchance\b', r'\bprobability\b', r'\bpick\b'
        ]
        if any(re.search(pattern, description) for pattern in random_patterns):
            has_random_dep = any(dep.startswith('T11.') for dep in current_deps)
            if not has_random_dep and current_topic != 'T11':
                suggested = "T11.G2.01 or T11.G3.01"
                missing.append({
                    'topic': 'T11',
                    'name': 'Random',
                    'suggested': suggested,
                    'reason': 'Uses random values'
                })

        # T01 - Algorithms/Sequences
        algo_patterns = [
            r'\bsequence\b', r'\bsteps\b', r'\border\b', r'\balgorithm\b',
            r'\bprocedure\b', r'\binstruction\b'
        ]
        if any(re.search(pattern, description) for pattern in algo_patterns):
            has_algo_dep = any(dep.startswith('T01.') for dep in current_deps)
            if not has_algo_dep and current_topic != 'T01':
                suggested = "T01.G2.01 or T01.G3.01"
                missing.append({
                    'topic': 'T01',
                    'name': 'Algorithms',
                    'suggested': suggested,
                    'reason': 'Uses algorithms or sequences'
                })

        # T04 - User Interface
        ui_patterns = [
            r'\bbutton\b', r'\bclick\b', r'\binput\b', r'\buser\b',
            r'\binterface\b', r'\bdisplay\b', r'\bshow\b', r'\bask\b',
            r'\banswer\b', r'\bsprite\b', r'\bstage\b'
        ]
        if any(re.search(pattern, description) for pattern in ui_patterns):
            has_ui_dep = any(dep.startswith('T04.') for dep in current_deps)
            if not has_ui_dep and current_topic != 'T04':
                suggested = "T04.G2.01 or T04.G3.01"
                missing.append({
                    'topic': 'T04',
                    'name': 'User Interface',
                    'suggested': suggested,
                    'reason': 'Uses UI elements or interaction'
                })

        # T05 - Functions/Procedures
        func_patterns = [
            r'\bfunction\b', r'\bprocedure\b', r'\bcustom block\b',
            r'\bdefine\b', r'\breuse\b', r'\bcall\b'
        ]
        if any(re.search(pattern, description) for pattern in func_patterns):
            has_func_dep = any(dep.startswith('T05.') for dep in current_deps)
            if not has_func_dep and current_topic != 'T05':
                suggested = "T05.G2.01 or T05.G3.01"
                missing.append({
                    'topic': 'T05',
                    'name': 'Functions',
                    'suggested': suggested,
                    'reason': 'Uses functions or custom blocks'
                })

        # Check for dependencies on grades higher than G3 (X-2 rule violation)
        invalid_deps = []
        for dep_id in current_deps:
            dep_grade = get_grade_from_skill_id(dep_id)
            if dep_grade and dep_grade in ['G4', 'G5']:
                invalid_deps.append({
                    'dep_id': dep_id,
                    'dep_grade': dep_grade,
                    'reason': f'Grade 3 skill depends on {dep_grade} skill (violates X-2 rule)'
                })

        if missing or invalid_deps:
            recommendations.append({
                'skill': skill,
                'missing': missing,
                'invalid': invalid_deps
            })

    return recommendations

def main():
    filename = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("Extracting all skills...")
    all_skills, grade3_skills = extract_all_skills_by_grade(filename)
    print(f"Total skills in database: {len(all_skills)}")
    print(f"Grade 3 skills in T25-T36: {len(grade3_skills)}")

    # Group by topic
    by_topic = {}
    for skill in grade3_skills:
        topic = skill['id'].split('.')[0]
        if topic not in by_topic:
            by_topic[topic] = []
        by_topic[topic].append(skill)

    print("\nSkills by topic:")
    for topic in sorted(by_topic.keys()):
        print(f"  {topic}: {len(by_topic[topic])} skills")

    print("\nAnalyzing cross-topic dependencies...")
    recommendations = analyze_cross_topic_dependencies(all_skills, grade3_skills)

    print(f"\n{'='*100}")
    print("GRADE 3 (T25-T36) MISSING CROSS-TOPIC DEPENDENCIES ANALYSIS")
    print(f"{'='*100}\n")

    if not recommendations:
        print("No issues found - all dependencies look good!")
    else:
        for rec in recommendations:
            skill = rec['skill']
            print(f"\nSKILL_ID: {skill['id']}")
            print(f"SKILL_NAME: {skill['skill_name']}")
            print(f"TOPIC: {skill['topic']}")
            print(f"CURRENT_DEPS: {len(skill['dependencies'])} dependencies")

            if rec['invalid']:
                print("\n  INVALID DEPENDENCIES (X-2 Rule Violations):")
                for inv in rec['invalid']:
                    print(f"    REMOVE: {inv['dep_id']} ({inv['dep_grade']})")
                    print(f"    REASON: {inv['reason']}")

            if rec['missing']:
                print("\n  MISSING DEPENDENCIES:")
                for miss in rec['missing']:
                    print(f"    ADD DEPENDENCY: {miss['topic']} - {miss['name']}")
                    print(f"    SUGGESTED: {miss['suggested']}")
                    print(f"    REASON: {miss['reason']}")

            # Show snippet of description
            desc = skill['description']
            if len(desc) > 200:
                desc = desc[:200] + "..."
            print(f"\n  DESCRIPTION: {desc}")
            print(f"\n  {'-'*100}")

    # Save detailed report
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/grade3_t25_t36_detailed_analysis.txt'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("GRADE 3 (T25-T36) CROSS-TOPIC DEPENDENCY ANALYSIS\n")
        f.write("="*100 + "\n\n")

        f.write(f"Total Grade 3 skills analyzed: {len(grade3_skills)}\n")
        f.write(f"Skills with issues: {len(recommendations)}\n\n")

        for rec in recommendations:
            skill = rec['skill']
            f.write(f"\nSKILL_ID: {skill['id']}\n")
            f.write(f"SKILL_NAME: {skill['skill_name']}\n")

            if rec['invalid']:
                for inv in rec['invalid']:
                    f.write(f"REMOVE DEPENDENCY: {inv['dep_id']}\n")
                    f.write(f"REASON: {inv['reason']}\n")

            if rec['missing']:
                for miss in rec['missing']:
                    f.write(f"ADD DEPENDENCY: {miss['suggested']}\n")
                    f.write(f"REASON: {miss['reason']}\n")

            f.write("\n")

    print(f"\n{'='*100}")
    print(f"\nDetailed analysis saved to: {output_file}")
    print(f"\nSummary:")
    print(f"  Total Grade 3 skills analyzed: {len(grade3_skills)}")
    print(f"  Skills with dependency issues: {len(recommendations)}")
    print(f"  Percentage needing updates: {len(recommendations)/len(grade3_skills)*100:.1f}%")

if __name__ == '__main__':
    main()
