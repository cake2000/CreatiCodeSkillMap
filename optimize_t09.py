import os

def optimize_t09():
    file_path = 'skillsv6/allskills.md'
    content_path = 't09_content.txt'
    
    with open(file_path, 'r') as f:
        lines = f.readlines()
        
    with open(content_path, 'r') as f:
        new_t09_content = f.read()
        
    start_index = -1
    end_index = -1
    
    for i, line in enumerate(lines):
        if line.strip().startswith('# T09'):
            start_index = i
            print(f"Found T09 at line {i}: {line.strip()}")
            break
            
    if start_index != -1:
        # Search for T10 starting from T09
        for i in range(start_index + 1, len(lines)):
            if lines[i].strip().startswith('# T10'):
                end_index = i
                print(f"Found T10 at line {i}: {lines[i].strip()}")
                break
    
    if start_index == -1:
        print('Error: Could not find T09 start')
        return
        
    if end_index == -1:
        print('Error: Could not find T10 start')
        return

    if not new_t09_content.endswith('\n'):
        new_t09_content += '\n'

    # We replace everything from start_index to end_index (exclusive)
    new_lines = lines[:start_index]
    new_lines.append(new_t09_content)
    new_lines.extend(lines[end_index:])
    
    with open(file_path, 'w') as f:
        f.writelines(new_lines)
        
    print(f"Optimized T09 in {file_path}")

if __name__ == "__main__":
    optimize_t09()
