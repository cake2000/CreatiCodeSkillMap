import re
import os

source_file = 'skillsv5/allskillsv7.md'
output_file = 'skillsv5/allskillsv7.md' # Overwrite

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

def standardize_verbs(skills):
    # Map ID -> New Title
    updates = {
        'T18.G6.00G': 'Explain Lag and Latency',
        'T09.G6.06.01': 'Explain Variable Persistence across Events',
        'T33.G6.09': 'Compare Cloud Database Collections and Google Sheets',
        'T11.G7.03': 'Explain Encapsulation and Information Hiding',
        'T11.G7.05': 'Identify Helper Blocks',
        'T11.G7.07': 'Analyze Helper Block Structure', 
        'T18.G6.00F': 'Explain Synchronization Mechanisms',
        'T18.G6.00H': 'Explain Role of Game Servers',
        'T18.G6.00I': 'Explain Player Roles',
        'T18.G6.00J': 'Distinguish Display Names from Usernames',
        'T32.G5.06': 'Explain Consent for AI Data Collection',
        'T32.G5.09': 'Demonstrate Encryption Basics (Unplugged)',
        'T32.G6.01.01': 'Analyze Virus and Worm Behavior',
        'T32.G6.01.02': 'Analyze Ransomware Mechanics',
        'T32.G6.01.03': 'Analyze Spyware Risks',
        'T32.G6.01.04': 'Analyze Trojan Horse Tactics',
        'T32.G6.03': 'Explain Network Attacks (DoS, MitM)',
        'T32.G4.03': 'Analyze Data Breaches through Stories',
        'T33.G5.03': 'Explain Risks of Shared URLs',
        'T11.G3.10': 'Distinguish When to Use Custom Blocks vs Loops'
    }
    
    for skill in skills:
        if skill['id'] in updates:
            new_title = updates[skill['id']]
            new_lines = []
            for line in skill['lines']:
                if line.startswith('Skill: '):
                    new_lines.append(f'Skill: {new_title}\n')
                else:
                    new_lines.append(line)
            skill['lines'] = new_lines
            skill['skill_name'] = new_title
            
    return skills

def add_dependencies(skills):
    # Map ID -> List of new dep IDs to ADD
    updates = {
        'T18.G6.00J': ['T32.G2.04'], # Display names -> Public/Private
        'T18.G6.01A': ['T32.G4.01'], # Create game -> DigCit Principles
        'T33.G5.03': ['T32.G2.04'], # Shared URLs -> Public/Private
        'T33.G6.08': ['T32.G5.04'], # Sheet Privacy -> Identify PII
    }
    
    for skill in skills:
        if skill['id'] in updates:
            deps_to_add = updates[skill['id']]
            # Find where dependencies start
            dep_start_idx = -1
            last_dep_idx = -1
            for i, line in enumerate(skill['lines']):
                if line.strip().startswith('Dependencies:'):
                    dep_start_idx = i
                if line.strip().startswith('* T'):
                    last_dep_idx = i
            
            if dep_start_idx != -1:
                insert_pos = last_dep_idx + 1 if last_dep_idx != -1 else dep_start_idx + 1
                for dep_id in deps_to_add:
                    # Check if already exists to avoid dupes
                    exists = any(dep_id in line for line in skill['lines'])
                    if not exists:
                        # Look up skill name for comment? 
                        # Simple version: just ID. 
                        # Actually I should try to find the skill name from all_skills list
                        # But simpler is just ID. The file mostly uses "* ID: Name".
                        # Let's try to get the name.
                        dep_name = get_skill_name(skills, dep_id)
                        skill['lines'].insert(insert_pos, f'* {dep_id}: {dep_name}\n')
                        insert_pos += 1
            else:
                # No dependencies section? Add one at end.
                skill['lines'].append('\nDependencies:\n')
                for dep_id in deps_to_add:
                    dep_name = get_skill_name(skills, dep_id)
                    skill['lines'].append(f'* {dep_id}: {dep_name}\n')
                    
    return skills

def get_skill_name(skills, skill_id):
    for s in skills:
        if s['id'] == skill_id:
            return s['skill_name']
    return "Unknown Skill"

def fix_text_descriptions(skills):
    # Replacements list: (regex, replacement)
    replacements = [
        (r'\(T23-T24\)', '(T22-T23)'),
        (r'using T21/T22 blocks', 'using T20/T21 blocks'),
        (r'T21-T24', 'T20-T23'),
        # Fix specific skill titles if they contain old IDs
        (r'assistance \(T23-T24\)', 'assistance (T22-T23)'),
        (r'generation \(T21-T22\)', 'generation (T20-T21)'),
        (r'assistance \(T23-T24\)', 'assistance (T22-T23)'), 
        # Catch-all for other mentions if safe
        # (r'T35', 'T32'), # Risky if T35 appears in other contexts? But topic is moved.
        # Actually T35 references in text are likely old topic refs.
        # But I won\'t do global T35->T32 text replacement to be safe.
    ]
    
    for skill in skills:
        new_lines = []
        for line in skill['lines']:
            new_line = line
            for pattern, repl in replacements:
                new_line = re.sub(pattern, repl, new_line)
            new_lines.append(new_line)
        skill['lines'] = new_lines
    return skills

def split_capstone(skills):
    # Target: T32.G8.04 "Lead peer workshops on responsible tech use"
    # Split into .01, .02, .03
    
    target_id = 'T32.G8.04'
    target_idx = -1
    for i, s in enumerate(skills):
        if s['id'] == target_id:
            target_idx = i
            break
            
    if target_idx == -1:
        print(f"Could not find {target_id} to split")
        return skills
        
    original_skill = skills[target_idx]
    original_deps = []
    for line in original_skill['lines']:
        if line.strip().startswith('* T'):
            original_deps.append(line)
            
    # Define new skills
    sub1 = {
        'id': 'T32.G8.04.01',
        'topic_id': 'T32',
        'skill_name': 'Design workshop curriculum for responsible tech',
        'lines': [
            '\n',
            'ID: T32.G8.04.01\n',
            'Topic: T32 – Digital Citizenship\n',
            'Skill: Design workshop curriculum for responsible tech\n',
            'Description: Students plan a short lesson (10-15 minutes) to teach younger students a coding concept or tech safety topic (debugging basics, AI safety, online privacy). The plan includes: learning objective, step-by-step instructions, an activity, and how to check understanding. They select the workshop topic (screen balance, kindness, privacy, AI ethics).\n',
            '\n',
            'Dependencies:\n'
        ] + original_deps
    }
    
    sub2 = {
        'id': 'T32.G8.04.02',
        'topic_id': 'T32',
        'skill_name': 'Build interactive workshop tools',
        'lines': [
            '\n',
            'ID: T32.G8.04.02\n',
            'Topic: T32 – Digital Citizenship\n',
            'Skill: Build interactive workshop tools\n',
            'Description: Students design and build interactive teaching tools using widgets and blocks for their workshop. Examples: timer widget for screen balance, scenario simulator for kindness, sorting game for privacy, or bias demo for AI ethics. They also create an assessment component (quiz) to check understanding.\n',
            '\n',
            'Dependencies:\n',
            '* T32.G8.04.01: Design workshop curriculum for responsible tech\n',
            '* T16.G8.01: Build complex multi-widget applications\n'
        ]
    }
    
    sub3 = {
        'id': 'T32.G8.04.03',
        'topic_id': 'T32',
        'skill_name': 'Deliver workshop and iterate',
        'lines': [
            '\n',
            'ID: T32.G8.04.03\n',
            'Topic: T32 – Digital Citizenship\n',
            'Skill: Deliver workshop and iterate\n',
            'Description: Students pilot their workshops with younger grades, delivering the lesson and using their interactive tools. They collect feedback using widget-based surveys and iterate on their tools and lesson plan based on what worked and what didn\'t.\n',
            '\n',
            'Dependencies:\n',
            '* T32.G8.04.02: Build interactive workshop tools\n'
        ]
    }
    
    # Replace original with subs
    skills[target_idx] = sub1
    skills.insert(target_idx + 1, sub2)
    skills.insert(target_idx + 2, sub3)
    
    return skills

def update_refs_to_split_skill(skills):
    # Update dependencies pointing to T32.G8.04 -> T32.G8.04.03
    old_id = 'T32.G8.04'
    new_id = 'T32.G8.04.03'
    new_name = 'Deliver workshop and iterate'
    
    for skill in skills:
        new_lines = []
        for line in skill['lines']:
            if line.strip().startswith(f'* {old_id}'):
                # Replace with new ID
                new_lines.append(f'* {new_id}: {new_name}\n')
            else:
                new_lines.append(line)
        skill['lines'] = new_lines
    return skills

def write_skills(skills, output_path):
    # Write header (manual or grab from first skill?)
    # The first skill (T01) has header lines in its 'lines' in my parser logic?
    # No, parser creates a 'current_skill' when ID is found. 
    # Header lines before first ID are lost in my `parse_skills` function!
    # I need to read and write the header separately.
    
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
            # Ensure spacing between skills (parser keeps newlines usually, but let's be safe)
            # My parser kept full lines including \n. 
            # But inserting new skills might need extra \n.
            # I added \n in sub skill lines.
    
def main():
    skills = parse_skills(source_file)
    
    skills = standardize_verbs(skills)
    skills = add_dependencies(skills)
    skills = fix_text_descriptions(skills)
    skills = split_capstone(skills)
    skills = update_refs_to_split_skill(skills)
    
    write_skills(skills, output_file)
    print(f"Successfully optimized {output_file}")

if __name__ == '__main__':
    main()
