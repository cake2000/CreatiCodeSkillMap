import os

def optimize_t10():
    file_path = 'skillsv6/allskills.md'
    
    # Read original file
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    # Find start of T10
    start_idx = -1
    for i, line in enumerate(lines):
        if line.startswith('## T10 – Lists & Tables'):
            start_idx = i
            break
    
    if start_idx == -1:
        print("Error: Could not find start of T10")
        return

    # Find start of T11
    end_idx = -1
    for i, line in enumerate(lines):
        if i > start_idx and line.startswith('# T11 – Functions & Organization'):
            end_idx = i
            break
            
    if end_idx == -1:
        print("Error: Could not find start of T11")
        # Fallback: search for T11.GK.01 context if header changed
        for i, line in enumerate(lines):
             if i > start_idx and 'ID: T11.GK.01' in line:
                 # Walk back to find the header or separator
                 end_idx = i - 20 # Approx
                 # Search forward from there for the # T11 header
                 for j in range(end_idx, i):
                     if lines[j].startswith('# T11 –'):
                         end_idx = j
                         break
                 break
    
    if end_idx == -1:
        print("Critical Error: Could not find end of T10 section")
        return

    print(f"Replacing lines {start_idx} to {end_idx}")

    # Read new content parts
    new_content = ""
    for i in range(1, 5):
        with open(f't10_new_part{i}.md', 'r') as f:
            new_content += f.read()
            new_content += "\n\n"

    # Add separator
    new_content += "---\n\n"

    # Construct new file content
    final_lines = lines[:start_idx] + [new_content] + lines[end_idx:]
    
    # Write back
    with open(file_path, 'w') as f:
        f.writelines(final_lines)
    
    print("Successfully optimized T10 in skillsv6/allskills.md")

if __name__ == '__main__':
    optimize_t10()
