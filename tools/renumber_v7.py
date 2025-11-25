import re
import os

source_file = 'skillsv5/allskillsv6.md'
output_file = 'skillsv5/allskillsv7.md'

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
            # Store the full topic line to extract the name later
            current_skill['topic_line'] = line.strip()
            current_lines.append(line)
        else:
            current_lines.append(line)
            
    if current_skill:
        current_skill['lines'] = current_lines
        skills.append(current_skill)
        
    return skills

def get_topic_num(skill_id):
    # T13.GK.01 -> 13
    try:
        return int(skill_id.split('.')[0][1:])
    except:
        return 999

def calculate_new_topic_num(old_num):
    if 1 <= old_num <= 11:
        return old_num
    elif 13 <= old_num <= 32:
        return old_num - 1
    elif old_num == 35:
        return 32
    elif old_num == 33:
        return 33
    elif old_num == 34:
        return 34
    else:
        # Should not happen based on requirements, but keep as is
        return old_num

def get_grade_sort_key(skill_id):
    # Return a tuple for sorting (Topic, Grade, SubID)
    parts = skill_id.split('.')
    topic_num = int(parts[0][1:])
    
    grade_part = parts[1]
    if grade_part == 'GK': grade_val = 0
    elif grade_part.startswith('G'):
        try:
            grade_val = int(grade_part[1:])
        except:
            grade_val = 99
    else:
        grade_val = 99
        
    try:
        # Handle 01 vs 01.01
        sub_str = parts[2]
        if len(parts) > 3:
            sub_str += '.' + parts[3]
        sub_val = float(sub_str)
    except:
        sub_val = 0.0
        
    return (topic_num, grade_val, sub_val)

def process_skills(skills):
    id_map = {}
    
    # First pass: Calculate new IDs and map them
    for skill in skills:
        old_id = skill['id']
        old_topic_num = get_topic_num(old_id)
        new_topic_num = calculate_new_topic_num(old_topic_num)
        
        # Reconstruct ID with new topic number
        # T13.GK.01 -> T12.GK.01
        # parts[0] is T13
        parts = old_id.split('.')
        parts[0] = f'T{new_topic_num:02d}'
        new_id = '.'.join(parts)
        
        id_map[old_id] = new_id
        
        # Store new metadata on skill object
        skill['new_id'] = new_id
        skill['new_topic_num'] = new_topic_num
        
        # Update lines for ID and Topic
        new_lines = []
        for line in skill['lines']:
            if line.startswith('ID: '):
                new_lines.append(f'ID: {new_id}\n')
            elif line.startswith('Topic: '):
                # Regex to replace Txx with Tyy
                # Topic: T13 – Testing -> Topic: T12 – Testing
                # Use the stored topic line to preserve the name part
                old_topic_str = f'T{old_topic_num:02d}'
                new_topic_str = f'T{new_topic_num:02d}'
                new_line = line.replace(old_topic_str, new_topic_str, 1)
                new_lines.append(new_line)
            else:
                new_lines.append(line)
        skill['lines'] = new_lines

    # Handle Ghost IDs (parents)
    # e.g. T13.GK may be ref'd, but only T13.GK.01 exists
    # We need to map T13.GK -> T12.GK
    # Iterate mapping keys
    keys = list(id_map.keys())
    for old_id in keys:
        # If old_id is Txx.Gx.yy
        parts = old_id.split('.')
        # Map Txx.Gx -> Tyy.Gx
        if len(parts) >= 2:
            parent_id = f"{parts[0]}.{parts[1]}"
            if parent_id not in id_map:
                # Calculate new parent ID
                old_top = int(parts[0][1:])
                new_top = calculate_new_topic_num(old_top)
                new_parent_id = f"T{new_top:02d}.{parts[1]}"
                id_map[parent_id] = new_parent_id
                # print(f"Mapped ghost parent {parent_id} -> {new_parent_id}")

    # Second pass: Update dependencies
    for skill in skills:
        new_lines = []
        for line in skill['lines']:
            if line.strip().startswith('* T'):
                match = re.match(r'(\s*\*\s*)(T\d{2}\.G[K\d]\.\d{2}(?:\.\d{2})?)(.*)', line)
                if match:
                    prefix, dep_id, rest = match.groups()
                    
                    # Try exact match
                    if dep_id in id_map:
                        new_dep_id = id_map[dep_id]
                        new_lines.append(f'{prefix}{new_dep_id}{rest}\n')
                    else:
                        # Try parent match? e.g. T13.G4 -> T12.G4
                        # Usually covered by ghost id logic above, but check
                        parts = dep_id.split('.')
                        old_top_num = get_topic_num(dep_id)
                        new_top_num = calculate_new_topic_num(old_top_num)
                        if new_top_num != old_top_num:
                             # It's a topic we are moving, so we must update the ID prefix
                             # even if we didn't map the specific skill (e.g. external ref?)
                             # But safer to rely on map.
                             # If not in map, maybe it's a typo in file?
                             # Let's force update the Txx part if it matches our range
                             new_dep_id = f"T{new_top_num:02d}" + dep_id[3:]
                             new_lines.append(f'{prefix}{new_dep_id}{rest}\n')
                        else:
                             new_lines.append(line)
                else:
                    new_lines.append(line)
            else:
                new_lines.append(line)
        skill['lines'] = new_lines
        
    return skills

def write_skills(skills, output_path):
    # Sort by NEW ID
    skills.sort(key=lambda s: get_grade_sort_key(s['new_id']))
    
    # Header (read from source)
    header = []
    with open(source_file, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('ID: '):
                break
            header.append(line)
            
    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(header)
        for skill in skills:
            f.writelines(skill['lines'])
            f.write('\n')

def main():
    skills = parse_skills(source_file)
    process_skills(skills)
    write_skills(skills, output_file)
    print(f"Successfully renumbered topics and wrote to {output_file}")

if __name__ == '__main__':
    main()
