import re
import os

source_file = 'skillsv4/allskills.md'
output_file = 'skillsv5/allskills.md'

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
    # Extract grade from ID (e.g. T11.GK.01 -> 0, T11.G1.01 -> 1)
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
    # Extract sub ID for sorting within grade (e.g. T11.GK.01 -> 1)
    parts = skill_id.split('.')
    if len(parts) < 3: return 0
    try:
        # Convert last part(s) to a float for sorting
        # e.g. 01 -> 1.0, 01.01 -> 1.01
        val_str = parts[2]
        if len(parts) > 3:
            val_str += '.' + parts[3]
        return float(val_str)
    except:
        return 0

def merge_skills(all_skills):
    t11_skills = [s for s in all_skills if s.get('topic_id') == 'T11']
    t12_skills = [s for s in all_skills if s.get('topic_id') == 'T12']
    other_skills = [s for s in all_skills if s.get('topic_id') not in ['T11', 'T12']]
    
    # Group by grade
    grade_buckets = {}
    for s in t11_skills + t12_skills:
        g = get_grade_val(s['id'])
        if g not in grade_buckets: grade_buckets[g] = []
        grade_buckets[g].append(s)
        
    # Sort and merge within grades
    sorted_grades = sorted(grade_buckets.keys())
    
    id_mapping = {}
    new_t11_skills = []
    
    for g in sorted_grades:
        g_skills = grade_buckets[g]
        # Separate T11 and T12 for this grade
        g_t11 = sorted([s for s in g_skills if s['topic_id'] == 'T11'], key=lambda x: get_sub_id(x['id']))
        g_t12 = sorted([s for s in g_skills if s['topic_id'] == 'T12'], key=lambda x: get_sub_id(x['id']))
        
        # Heuristic: K-3: T12 then T11, 4-8: T11 then T12
        if g <= 3:
            ordered = g_t12 + g_t11
        else:
            ordered = g_t11 + g_t12
            
        # Renumber
        for i, skill in enumerate(ordered):
            old_id = skill['id']
            
            # Construct new ID
            grade_str = 'GK' if g == 0 else f'G{g}'
            new_id = f'T11.{grade_str}.{i+1:02d}'
            
            id_mapping[old_id] = new_id
            
            # Update skill object
            skill['id'] = new_id
            skill['topic_id'] = 'T11'
            
            # Update ID line in content
            new_lines = []
            for line in skill['lines']:
                if line.startswith('ID: '):
                    new_lines.append(f'ID: {new_id}\n')
                elif line.startswith('Topic: '):
                    new_lines.append('Topic: T11 – Functions & Organization\n') 
                else:
                    new_lines.append(line)
            skill['lines'] = new_lines
            
            new_t11_skills.append(skill)

    # Fix for "Parent" IDs in dependencies (e.g. T12.G3.05 -> T12.G3.05.01's new ID)
    keys = list(id_mapping.keys())
    for old_id in keys:
        # If old_id looks like T12.GX.YY.01
        if old_id.endswith('.01'):
            parent_id = old_id[:-3] # Remove .01
            if parent_id not in id_mapping:
                id_mapping[parent_id] = id_mapping[old_id]
                print(f"Mapping parent ghost ID {parent_id} to {id_mapping[old_id]}")

    return other_skills, new_t11_skills, id_mapping

def update_dependencies(skills, id_mapping):
    for skill in skills:
        new_lines = []
        for line in skill['lines']:
            if line.strip().startswith('* T'): 
                # Regex to capture the ID part specifically
                # Matches * TXX.G... up to end of line or colon
                match = re.match(r'(\s*\*\s*)(T\d{2}\.G[K\d]\.\d{2}(?:\.\d{2})?)(.*)', line)
                if match:
                    prefix, dep_id, rest = match.groups()
                    if dep_id in id_mapping:
                        new_id = id_mapping[dep_id]
                        new_lines.append(f'{prefix}{new_id}{rest}\n')
                    else:
                        # Fallback: Check if it's a T12 ID that wasn't mapped?
                        if dep_id.startswith('T12'):
                            # Try simple heuristic if not in map? No, relied on parent mapping
                            new_lines.append(line) 
                        else:
                            new_lines.append(line)
                else:
                    new_lines.append(line)
            else:
                new_lines.append(line)
        skill['lines'] = new_lines
    return skills

def write_skills(other_skills, t11_skills, output_path):
    # Sort other skills by Topic ID
    other_skills.sort(key=lambda x: x['topic_id'])
    
    pre_t11 = [s for s in other_skills if int(s['topic_id'][1:]) < 11]
    post_t11 = [s for s in other_skills if int(s['topic_id'][1:]) > 12] 
    
    # Header
    header = []
    with open(source_file, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('ID: '):
                break
            header.append(line)
            
    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(header)
        
        for s in pre_t11:
            f.writelines(s['lines'])
            f.write('\n') 
            
        for s in t11_skills:
            f.writelines(s['lines'])
            f.write('\n')
            
        for s in post_t11:
            f.writelines(s['lines'])
            f.write('\n')

def main():
    all_skills = parse_skills(source_file)
    other_skills, new_t11_skills, id_mapping = merge_skills(all_skills)
    
    full_list = other_skills + new_t11_skills
    updated_skills = update_dependencies(full_list, id_mapping)
    
    write_skills(other_skills, new_t11_skills, output_file)
    print(f"Successfully merged T11/T12 and wrote to {output_file}")

if __name__ == '__main__':
    main()