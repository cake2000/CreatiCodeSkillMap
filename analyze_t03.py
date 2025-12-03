import re

def parse_skills(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    skills = {}
    current_skill = None
    
    # Regex for Skill ID
    id_pattern = re.compile(r'^ID:\s*(T03\.[^ \n]+)')
    # Regex for Dependencies
    dep_pattern = re.compile(r'^\*\s*(T03\.[^: \n]+)')
    
    lines = content.split('\n')
    for line in lines:
        id_match = id_pattern.match(line)
        if id_match:
            if current_skill:
                skills[current_skill['id']] = current_skill
            current_skill = {
                'id': id_match.group(1),
                'grade': id_match.group(1).split('.')[1],
                'desc': '',
                'deps': [],
                'content': line
            }
        elif current_skill:
            current_skill['content'] += '\n' + line
            dep_match = dep_pattern.match(line.strip())
            if dep_match:
                current_skill['deps'].append(dep_match.group(1))
            
            if line.strip().startswith('Description:'):
                current_skill['desc'] = line.strip()

    if current_skill:
        skills[current_skill['id']] = current_skill
        
    return skills

def get_grade_value(grade_str):
    if grade_str == 'GK': return 0
    if grade_str.startswith('G'): return int(grade_str[1:])
    return -1

def check_t03(skills):
    issues = []
    
    for sk_id, skill in skills.items():
        grade_val = get_grade_value(skill['grade'])
        
        # 1. Check Dependencies (X-2 Rule)
        for dep_id in skill['deps']:
            if dep_id not in skills: continue # Skip if not in T03 (or typo) 
            
            dep_grade = skills[dep_id]['grade']
            dep_grade_val = get_grade_value(dep_grade)
            
            # Rule: dep must be >= grade - 2
            # Allowed: X, X-1, X-2
            # So if grade is 5, allowed deps are 5, 4, 3.
            # 5 - 2 = 3. So dep_grade_val must be >= 3.
            
            if dep_grade_val < grade_val - 2:
                issues.append(f"X-2 Violation: {sk_id} ({skill['grade']}) depends on {dep_id} ({dep_grade})")

        # 2. Check Content Appropriateness
        desc_lower = skill['desc'].lower() + skill['content'].lower()
        
        if grade_val <= 2: # K-2
            keywords = ['picture', 'card', 'visual', 'unplugged', 'image', 'photo', 'draw']
            if not any(k in desc_lower for k in keywords):
                issues.append(f"K-2 Content: {sk_id} might need visual/picture keywords.")
        
        if grade_val >= 3: # 3-8
            keywords = ['code', 'block', 'script', 'sprite', 'project', 'program', 'debug', 'algorithm', 'variable', 'list', 'loop', 'feature', 'module', 'component', 'design', 'plan', 'architecture']
            if not any(k in desc_lower for k in keywords):
                issues.append(f"G3+ Content: {sk_id} might need coding keywords.")

    return issues

skills = parse_skills('skillsv6/allskills.md')
issues = check_t03(skills)

print(f"Found {len(issues)} issues.")
for i in issues:
    print(i)
