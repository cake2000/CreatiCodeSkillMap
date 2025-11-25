import re
import os

source_file = 'skillsv5/allskills.md'
output_file = 'skillsv5/allskillsv6.md'

def parse_skills(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    skills = []
    current_skill = {}
    current_lines = []
    
    for line in lines:
        if line.startswith('ID: '):
            if current_skill:
                current_skill['lines'] = current_lines
                skills.append(current_skill)
            current_skill = {'id': line.strip().split('ID: ')[1].strip()}
            current_lines = [line]
        elif line.startswith('Topic: '):
            current_skill['topic_id'] = line.strip().split('Topic: ')[1].split(' ')[0]
            current_lines.append(line)
        elif line.startswith('Skill: '):
            current_skill['skill_name'] = line.strip().split('Skill: ')[1]
            current_lines.append(line)
        else:
            current_lines.append(line)
            
    if current_skill:
        current_skill['lines'] = current_lines
        skills.append(current_skill)
        
    return skills

def get_grade_val(skill_id):
    parts = skill_id.split('.')
    if len(parts) < 2: return 99
    grade_part = parts[1]
    if grade_part == 'GK': return 0
    if grade_part.startswith('G'):
        try:
            return int(grade_part[1:])
        except:
            return 99
    return 99

def get_sub_id(skill_id):
    parts = skill_id.split('.')
    if len(parts) < 3: return 0
    try:
        val_str = parts[2]
        if len(parts) > 3:
            val_str += '.' + parts[3]
        return float(val_str)
    except:
        return 0

def merge_skills(all_skills):
    t35_skills = [s for s in all_skills if s.get('topic_id') == 'T35']
    t36_skills = [s for s in all_skills if s.get('topic_id') == 'T36']
    other_skills = [s for s in all_skills if s.get('topic_id') not in ['T35', 'T36']]
    
    grade_buckets = {}
    for s in t35_skills + t36_skills:
        g = get_grade_val(s['id'])
        if g not in grade_buckets: grade_buckets[g] = []
        grade_buckets[g].append(s)
        
    sorted_grades = sorted(grade_buckets.keys())
    
    id_mapping = {}
    new_t35_skills = []
    
    for g in sorted_grades:
        g_skills = grade_buckets[g]
        # Separate and sort
        g_t35 = sorted([s for s in g_skills if s['topic_id'] == 'T35'], key=lambda x: get_sub_id(x['id']))
        g_t36 = sorted([s for s in g_skills if s['topic_id'] == 'T36'], key=lambda x: get_sub_id(x['id']))
        
        # Order: T35 then T36 (Impacts/Ethics then Careers/Collaboration)
        # This seems like a reasonable default for "Digital Citizenship" (Ethics first, then Application/Careers)
        ordered = g_t35 + g_t36
            
        for i, skill in enumerate(ordered):
            old_id = skill['id']
            
            grade_str = 'GK' if g == 0 else f'G{g}'
            new_id = f'T35.{grade_str}.{i+1:02d}'
            
            id_mapping[old_id] = new_id
            
            skill['id'] = new_id
            skill['topic_id'] = 'T35'
            
            new_lines = []
            for line in skill['lines']:
                if line.startswith('ID: '):
                    new_lines.append(f'ID: {new_id}\n')
                elif line.startswith('Topic: '):
                    new_lines.append('Topic: T35 – Digital Citizenship\n')
                else:
                    new_lines.append(line)
            skill['lines'] = new_lines
            
            new_t35_skills.append(skill)

    # Ghost parent ID handling
    keys = list(id_mapping.keys())
    for old_id in keys:
        if old_id.endswith('.01'):
            parent_id = old_id[:-3]
            if parent_id not in id_mapping:
                id_mapping[parent_id] = id_mapping[old_id]
                print(f"Mapping parent ghost ID {parent_id} to {id_mapping[old_id]}")

    return other_skills, new_t35_skills, id_mapping

def update_dependencies(skills, id_mapping):
    for skill in skills:
        new_lines = []
        for line in skill['lines']:
            if line.strip().startswith('* T'): 
                match = re.match(r'(\s*\*\s*)(T\d{2}\.G[K\d]\.\d{2}(?:\.\d{2})?)(.*)', line)
                if match:
                    prefix, dep_id, rest = match.groups()
                    if dep_id in id_mapping:
                        new_id = id_mapping[dep_id]
                        new_lines.append(f'{prefix}{new_id}{rest}\n')
                    else:
                        new_lines.append(line)
                else:
                    new_lines.append(line)
            else:
                new_lines.append(line)
        skill['lines'] = new_lines
    return skills

def write_skills(other_skills, new_t35_skills, output_path):
    other_skills.sort(key=lambda x: x['topic_id'])
    
    # T01-T34
    pre_t35 = [s for s in other_skills if int(s['topic_id'][1:]) < 35]
    # T37+ (if any, likely none, but good to be safe)
    post_t36 = [s for s in other_skills if int(s['topic_id'][1:]) > 36]
    
    header = []
    with open(source_file, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('ID: '):
                break
            header.append(line)
            
    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(header)
        
        for s in pre_t35:
            f.writelines(s['lines'])
            f.write('\n')
            
        for s in new_t35_skills:
            f.writelines(s['lines'])
            f.write('\n')
            
        for s in post_t36:
            f.writelines(s['lines'])
            f.write('\n')

def main():
    all_skills = parse_skills(source_file)
    other_skills, new_t35_skills, id_mapping = merge_skills(all_skills)
    
    full_list = other_skills + new_t35_skills
    updated_skills = update_dependencies(full_list, id_mapping)
    
    write_skills(other_skills, new_t35_skills, output_file)
    print(f"Successfully merged T35/T36 and wrote to {output_file}")

if __name__ == '__main__':
    main()
