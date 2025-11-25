#!/usr/bin/env python3
"""
Script to replace T09 section in allskills.md with content from T09_replacement_ready.txt
"""

def replace_t09_section(allskills_path, replacement_path):
    """
    Replace T09 section in allskills.md with content from replacement file.

    Returns: (success, line_count_diff, message)
    """
    # Read the replacement content
    try:
        with open(replacement_path, 'r', encoding='utf-8') as f:
            replacement_content = f.read()
        replacement_lines = replacement_content.count('\n')
        print(f"Replacement content loaded: {replacement_lines} lines")
    except Exception as e:
        return False, 0, f"Failed to read replacement file: {e}"

    # Read the original file
    try:
        with open(allskills_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        total_lines = len(lines)
        print(f"Original file loaded: {total_lines} lines")
    except Exception as e:
        return False, 0, f"Failed to read allskills.md: {e}"

    # Find T09 start line (containing "ID: T09.GK.01")
    t09_start = None
    for i, line in enumerate(lines):
        if "ID: T09.GK.01" in line:
            t09_start = i
            print(f"T09 start found at line {i + 1}: {line.strip()}")
            break

    if t09_start is None:
        return False, 0, "Could not find T09 start marker (ID: T09.GK.01)"

    # Find T10 start line (containing "ID: T10.GK.01")
    t10_start = None
    for i in range(t09_start + 1, len(lines)):
        line = lines[i]
        if "ID: T10.GK.01" in line:
            t10_start = i
            print(f"T10 start found at line {i + 1}: {line.strip()}")
            break

    if t10_start is None:
        return False, 0, "Could not find T10 start marker (ID: T10.GK.01)"

    # Calculate the section to replace
    # T09 section is from t09_start (inclusive) to t10_start (exclusive)
    t09_end = t10_start
    original_t09_lines = t09_end - t09_start
    print(f"T09 section spans lines {t09_start + 1} to {t09_end} ({original_t09_lines} lines)")

    # Build the new file content
    # Keep everything before T09
    new_content = ''.join(lines[:t09_start])

    # Add the replacement content
    new_content += replacement_content

    # Ensure proper spacing before T10 (2 blank lines)
    if not replacement_content.endswith('\n\n\n'):
        # Count trailing newlines in replacement
        trailing_newlines = len(replacement_content) - len(replacement_content.rstrip('\n'))
        if trailing_newlines == 0:
            new_content += '\n\n\n'
        elif trailing_newlines == 1:
            new_content += '\n\n'
        elif trailing_newlines == 2:
            new_content += '\n'

    # Add everything from T10 onwards
    new_content += ''.join(lines[t10_start:])

    # Write the new content back
    try:
        with open(allskills_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        new_total_lines = new_content.count('\n')
        line_diff = new_total_lines - total_lines
        print(f"File written successfully")
        print(f"New total lines: {new_total_lines}")
        print(f"Line count difference: {line_diff:+d}")
        return True, line_diff, "Replacement successful"
    except Exception as e:
        return False, 0, f"Failed to write file: {e}"


if __name__ == "__main__":
    allskills_path = "/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md"
    replacement_path = "/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/T09_replacement_ready.txt"

    success, line_diff, message = replace_t09_section(allskills_path, replacement_path)

    print("\n" + "=" * 60)
    if success:
        print(f"✓ SUCCESS: {message}")
        print(f"  Line count change: {line_diff:+d} lines")
    else:
        print(f"✗ FAILED: {message}")
        exit(1)
