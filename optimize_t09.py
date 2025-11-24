#!/usr/bin/env python3
"""
Optimize T09 skills in allskills.md according to the analysis
"""

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.readlines()

def write_file(path, lines):
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(lines)

def find_skill_boundaries(lines):
    """Find start and end indices for T09 section"""
    start_idx = None
    end_idx = None

    for i, line in enumerate(lines):
        if line.startswith('ID: T09.GK.01'):
            start_idx = i
        elif line.startswith('ID: T10.GK.01') and start_idx is not None:
            end_idx = i
            break

    return start_idx, end_idx

def extract_skill(lines, start_idx):
    """Extract a single skill from lines starting at start_idx"""
    skill_lines = []
    i = start_idx
    while i < len(lines):
        line = lines[i]
        skill_lines.append(line)

        # Check if next line starts a new skill
        if i + 1 < len(lines) and lines[i + 1].startswith('ID: '):
            break
        i += 1

    return skill_lines

def optimize_t09(input_path, output_path):
    print("Reading allskills.md...")
    lines = read_file(input_path)

    print("Finding T09 boundaries...")
    t09_start, t09_end = find_skill_boundaries(lines)
    print(f"T09 starts at line {t09_start}, ends at line {t09_end}")

    # Extract parts
    before_t09 = lines[:t09_start]
    t09_section = lines[t09_start:t09_end]
    after_t09 = lines[t09_end:]

    print(f"T09 has {len(t09_section)} lines")

    # Build optimized T09 section
    optimized_t09 = []

    # Parse T09 into individual skills
    skills = {}
    current_id = None
    current_skill = []

    for line in t09_section:
        if line.startswith('ID: T09.'):
            if current_id:
                skills[current_id] = current_skill
            current_id = line.strip().replace('ID: ', '')
            current_skill = [line]
        else:
            current_skill.append(line)

    # Add last skill
    if current_id:
        skills[current_id] = current_skill

    print(f"Parsed {len(skills)} T09 skills")

    # Now apply optimizations
    optimized_skills = {}
    changes = []

    # Process each skill and apply transformations
    for skill_id, skill_lines in skills.items():
        # Apply specific optimizations based on skill ID
        if skill_id == 'T09.G3.02':
            # Split into change and reduce blocks
            changes.append(f"SPLIT: {skill_id} -> T09.G3.02 (change) + T09.G3.02.01 (reduce)")
            optimized_skills[skill_id] = create_g3_02_change(skill_lines)
            optimized_skills['T09.G3.02.01'] = create_g3_02_reduce()

        elif skill_id == 'T09.G3.06':
            # Fix dependencies - move earlier, change dependency
            changes.append(f"FIX DEPS: {skill_id} - changed to depend on G3.01.02 instead of G3.02")
            optimized_skills[skill_id] = fix_g3_06_deps(skill_lines)

        elif skill_id == 'T09.G4.01':
            # Split into + and -
            changes.append(f"SPLIT: {skill_id} -> T09.G4.01 (+) + T09.G4.01.01 (-)")
            optimized_skills[skill_id] = create_g4_01_addition(skill_lines)
            optimized_skills['T09.G4.01.01'] = create_g4_01_subtraction()

        elif skill_id == 'T09.G4.02':
            # Split into * and /
            changes.append(f"SPLIT: {skill_id} -> T09.G4.02 (*) + T09.G4.02.01 (/)")
            optimized_skills[skill_id] = create_g4_02_multiplication(skill_lines)
            optimized_skills['T09.G4.02.01'] = create_g4_02_division()

        elif skill_id == 'T09.G4.05':
            # Add missing dependencies
            changes.append(f"FIX DEPS: {skill_id} - added T09.G3.01.04 and T09.G3.02")
            optimized_skills[skill_id] = fix_g4_05_deps(skill_lines)

        elif skill_id == 'T09.G4.06':
            # Split into 4 skills for comparison operators
            changes.append(f"SPLIT: {skill_id} -> 4 skills for comparison operators")
            optimized_skills[skill_id] = create_g4_06_basic_compare(skill_lines)
            optimized_skills['T09.G4.06.01'] = create_g4_06_greater()
            optimized_skills['T09.G4.06.02'] = create_g4_06_not_equal()
            optimized_skills['T09.G4.06.03'] = create_g4_06_gte_lte()

        elif skill_id == 'T09.G6.04':
            # Split into length and case conversion
            changes.append(f"SPLIT: {skill_id} -> T09.G6.04 (length) + T09.G6.04.01 (case)")
            optimized_skills[skill_id] = create_g6_04_length(skill_lines)
            optimized_skills['T09.G6.04.01'] = create_g6_04_case()

        elif skill_id == 'T09.G6.05':
            # Split into position and substring
            changes.append(f"SPLIT: {skill_id} -> T09.G6.05 (position) + T09.G6.05.01 (substring)")
            optimized_skills[skill_id] = create_g6_05_position(skill_lines)
            optimized_skills['T09.G6.05.01'] = create_g6_05_substring()

        elif skill_id == 'T09.G7.01.01':
            # Split into 3 skills for math functions
            changes.append(f"SPLIT: {skill_id} -> 3 skills for math functions")
            optimized_skills[skill_id] = create_g7_01_01_rounding(skill_lines)
            optimized_skills['T09.G7.01.02'] = create_g7_01_02_abs()
            optimized_skills['T09.G7.01.03'] = create_g7_01_03_sqrt()

        else:
            # Keep as is (but may need dependency updates)
            optimized_skills[skill_id] = skill_lines

    # Add new skills
    changes.append("ADD: T09.G3.01.05 - Variable reporter blocks")
    optimized_skills['T09.G3.01.05'] = create_g3_01_05_reporter()

    changes.append("ADD: T09.G5.03.01 - Multi-input join")
    optimized_skills['T09.G5.03.01'] = create_g5_03_01_multi_join()

    # Now update dependencies in all skills that reference split skills
    optimized_skills = update_all_dependencies(optimized_skills)

    # Sort skills by ID to maintain order
    sorted_ids = sorted(optimized_skills.keys(), key=lambda x: skill_sort_key(x))

    # Rebuild optimized T09 section
    for skill_id in sorted_ids:
        optimized_t09.extend(optimized_skills[skill_id])

    # Write output
    print(f"Writing optimized file to {output_path}...")
    result = before_t09 + optimized_t09 + after_t09
    write_file(output_path, result)

    print(f"\n=== OPTIMIZATION COMPLETE ===")
    print(f"Total changes: {len(changes)}")
    print(f"Original skills: {len(skills)}")
    print(f"Optimized skills: {len(optimized_skills)}")
    print(f"\nChanges made:")
    for change in changes:
        print(f"  - {change}")

    return changes

def skill_sort_key(skill_id):
    """Generate sort key for skill IDs"""
    # Extract parts: T09.GK.01 -> (9, 'K', 0, 1, 0, 0)
    # Extract parts: T09.G3.01.02 -> (9, 3, 1, 2, 0, 0)
    import re
    match = re.match(r'T(\d+)\.G([K\d])\.(\d+)(?:\.(\d+))?(?:\.(\d+))?', skill_id)
    if not match:
        return (99, 99, 99, 99, 99, 99)

    topic = int(match.group(1))
    grade = match.group(2)
    grade_num = -1 if grade == 'K' else int(grade)
    part1 = int(match.group(3))
    part2 = int(match.group(4)) if match.group(4) else 0
    part3 = int(match.group(5)) if match.group(5) else 0

    return (topic, grade_num, part1, part2, part3)

# Skill creation functions
def create_g3_02_change(original_lines):
    """Split G3.02 - keep change block, remove reduce"""
    return [
        "ID: T09.G3.02\n",
        "Topic: T09 – Variables & Expressions\n",
        "Skill: Use change block to increase a variable\n",
        "Description: Students use `change [variable] by (amount)` to increase a variable by arbitrary amounts (e.g., change score by 10, change lives by 5). They understand that \"change\" adds to the current value. This extends the basic increment-by-1 pattern (G3.01.03) to arbitrary positive amounts.\n",
        "\n",
        "Dependencies:\n",
        "* T09.G3.01.04: Display variable value on stage using the variable monitor\n",
        "\n",
        "\n"
    ]

def create_g3_02_reduce():
    """Create new G3.02.01 for reduce block"""
    return [
        "ID: T09.G3.02.01\n",
        "Topic: T09 – Variables & Expressions\n",
        "Skill: Use reduce block to decrease a variable\n",
        "Description: Students use `reduce [variable] by (amount)` to decrease a variable by arbitrary amounts (e.g., reduce lives by 1, reduce health by 10). They understand that \"reduce\" subtracts from the current value, which is the opposite of \"change\". This provides an intuitive way to decrement variables.\n",
        "\n",
        "Dependencies:\n",
        "* T09.G3.02: Use change block to increase a variable\n",
        "\n",
        "\n"
    ]

def fix_g3_06_deps(original_lines):
    """Fix G3.06 dependencies - should depend on G3.01.02, not G3.02"""
    new_lines = []
    in_deps = False
    for line in original_lines:
        if line.startswith('Dependencies:'):
            in_deps = True
            new_lines.append(line)
        elif in_deps and line.startswith('* T09.G3.02'):
            # Replace with correct dependency
            new_lines.append('* T09.G3.01.02: Set a variable to an initial value at program start\n')
            in_deps = False
        else:
            new_lines.append(line)
    return new_lines

def create_g3_01_05_reporter():
    """Create new G3.01.05 for variable reporter blocks"""
    return [
        "ID: T09.G3.01.05\n",
        "Topic: T09 – Variables & Expressions\n",
        "Skill: Use variable reporter blocks in other blocks\n",
        "Description: Students drag the round [variable] reporter block into other blocks to use the variable's value (e.g., \"say [score]\" or \"move [speed] steps\"). They understand that the variable reporter provides the current value and can be used anywhere a number input is needed. This is the foundation for using variables in expressions.\n",
        "\n",
        "Dependencies:\n",
        "* T09.G3.01.04: Display variable value on stage using the variable monitor\n",
        "\n",
        "\n"
    ]

def create_g4_01_addition(original_lines):
    """Split G4.01 - keep addition only"""
    return [
        "ID: T09.G4.01\n",
        "Topic: T09 – Variables & Expressions\n",
        "Skill: Use addition (+) in variable expressions\n",
        "Description: Students use the + operator block to create expressions that add values, such as \"set total to score + bonus\" or \"set sum to a + b\". They understand that the + operator combines two values into a sum and can be used with variables, literals, or other expressions.\n",
        "\n",
        "Dependencies:\n",
        "* T09.G3.06: Copy one variable's value to another variable\n",
        "* T09.G3.05: Trace code with variables to predict outcomes\n",
        "\n",
        "\n"
    ]

def create_g4_01_subtraction():
    """Create new G4.01.01 for subtraction"""
    return [
        "ID: T09.G4.01.01\n",
        "Topic: T09 – Variables & Expressions\n",
        "Skill: Use subtraction (-) in variable expressions\n",
        "Description: Students use the - operator block to create expressions that subtract values, such as \"set remaining to total - used\" or \"set difference to a - b\". They understand that the - operator finds the difference between two values and can compute negative results.\n",
        "\n",
        "Dependencies:\n",
        "* T09.G4.01: Use addition (+) in variable expressions\n",
        "\n",
        "\n"
    ]

def create_g4_02_multiplication(original_lines):
    """Split G4.02 - keep multiplication only"""
    return [
        "ID: T09.G4.02\n",
        "Topic: T09 – Variables & Expressions\n",
        "Skill: Use multiplication (*) in expressions\n",
        "Description: Students use the * operator to create expressions that multiply values, such as \"set total to lives * 100\" or \"set area to width * height\". They understand that multiplication scales one value by another.\n",
        "\n",
        "Dependencies:\n",
        "* T09.G4.01.01: Use subtraction (-) in variable expressions\n",
        "\n",
        "\n"
    ]

def create_g4_02_division():
    """Create new G4.02.01 for division"""
    return [
        "ID: T09.G4.02.01\n",
        "Topic: T09 – Variables & Expressions\n",
        "Skill: Use division (/) in expressions\n",
        "Description: Students use the / operator to create expressions that divide values, such as \"set average to sum / count\" or \"set half to total / 2\". They understand that division splits one value by another and may produce decimal results.\n",
        "\n",
        "Dependencies:\n",
        "* T09.G4.02: Use multiplication (*) in expressions\n",
        "\n",
        "\n"
    ]

def fix_g4_05_deps(original_lines):
    """Add missing dependencies to G4.05"""
    new_lines = []
    deps_added = False
    for line in original_lines:
        new_lines.append(line)
        if line.startswith('Dependencies:') and not deps_added:
            # Add missing dependencies after the Dependencies: line
            new_lines.append('* T09.G3.01.04: Display variable value on stage using the variable monitor\n')
            new_lines.append('* T09.G3.02: Use change block to increase a variable\n')
            deps_added = True
    return new_lines

def create_g4_06_basic_compare(original_lines):
    """Split G4.06 - basic comparisons (= and <)"""
    return [
        "ID: T09.G4.06\n",
        "Topic: T09 – Variables & Expressions\n",
        "Skill: Use basic comparison operators (=, <) in conditionals\n",
        "Description: Students use the equals (=) and less than (<) operators in conditionals to compare values. Examples: \"if score = 10\", \"if lives < 3\". They understand that comparisons evaluate to true/false and control program flow. These are the most intuitive comparisons for beginners.\n",
        "\n",
        "Dependencies:\n",
        "* T09.G3.03: Use a variable in a simple conditional (if block)\n",
        "* T09.G3.05: Trace code with variables to predict outcomes\n",
        "\n",
        "\n"
    ]

def create_g4_06_greater():
    """Create G4.06.01 for greater than"""
    return [
        "ID: T09.G4.06.01\n",
        "Topic: T09 – Variables & Expressions\n",
        "Skill: Use greater than (>) operator in conditionals\n",
        "Description: Students use the greater than (>) operator to check if one value exceeds another. Examples: \"if score > 100\", \"if health > 0\". They understand that > is the opposite of < and when to use each.\n",
        "\n",
        "Dependencies:\n",
        "* T09.G4.06: Use basic comparison operators (=, <) in conditionals\n",
        "\n",
        "\n"
    ]

def create_g4_06_not_equal():
    """Create G4.06.02 for not equal"""
    return [
        "ID: T09.G4.06.02\n",
        "Topic: T09 – Variables & Expressions\n",
        "Skill: Use not equal (≠) operator in conditionals\n",
        "Description: Students use the not equal (≠) operator to check if values are different. Examples: \"if lives ≠ 0\", \"if answer ≠ correct\". They understand that ≠ is the opposite of = and when checking for difference is useful.\n",
        "\n",
        "Dependencies:\n",
        "* T09.G4.06: Use basic comparison operators (=, <) in conditionals\n",
        "\n",
        "\n"
    ]

def create_g4_06_gte_lte():
    """Create G4.06.03 for >= and <="""
    return [
        "ID: T09.G4.06.03\n",
        "Topic: T09 – Variables & Expressions\n",
        "Skill: Use greater-or-equal (≥) and less-or-equal (≤) operators\n",
        "Description: Students use >= and <= operators for inclusive comparisons. Examples: \"if score >= 100\" (at least 100), \"if health <= 20\" (at most 20). They understand these include the boundary value unlike > and <, which is important for \"at least\" and \"at most\" conditions.\n",
        "\n",
        "Dependencies:\n",
        "* T09.G4.06.01: Use greater than (>) operator in conditionals\n",
        "\n",
        "\n"
    ]

def create_g6_04_length(original_lines):
    """Split G6.04 - keep length only"""
    return [
        "ID: T09.G6.04\n",
        "Topic: T09 – Variables & Expressions\n",
        "Skill: Use string length operator\n",
        "Description: Students use `length of [string]` to get the character count of text. They apply this to validate input (e.g., check password length) or process text. Example: \"if length of [name] > 10\".\n",
        "\n",
        "Dependencies:\n",
        "* T09.G5.03: Join strings using concatenation\n",
        "\n",
        "\n"
    ]

def create_g6_04_case():
    """Create G6.04.01 for case conversion"""
    return [
        "ID: T09.G6.04.01\n",
        "Topic: T09 – Variables & Expressions\n",
        "Skill: Use case conversion (uppercase/lowercase) operators\n",
        "Description: Students use `[CASE v] of text [T]` blocks to convert text to uppercase or lowercase. They apply this for formatting output or case-insensitive comparisons. Examples: uppercase for shouting effects, lowercase for normalizing user input.\n",
        "\n",
        "Dependencies:\n",
        "* T09.G6.04: Use string length operator\n",
        "\n",
        "\n"
    ]

def create_g6_05_position(original_lines):
    """Split G6.05 - keep position only"""
    return [
        "ID: T09.G6.05\n",
        "Topic: T09 – Variables & Expressions\n",
        "Skill: Use position operator to find substrings\n",
        "Description: Students use `position of [search] in [text]` to find where a substring appears (returns position number, or 0 if not found). They apply this for text searching and validation. Example: check if email contains \"@\".\n",
        "\n",
        "Dependencies:\n",
        "* T09.G6.04.01: Use case conversion (uppercase/lowercase) operators\n",
        "\n",
        "\n"
    ]

def create_g6_05_substring():
    """Create G6.05.01 for substring extraction"""
    return [
        "ID: T09.G6.05.01\n",
        "Topic: T09 – Variables & Expressions\n",
        "Skill: Use substring operator to extract text portions\n",
        "Description: Students use `substring of [text] from position (start) to (end)` to extract parts of strings. They apply this for text parsing, extracting initials, or getting file extensions. Example: extract first name from full name.\n",
        "\n",
        "Dependencies:\n",
        "* T09.G6.05: Use position operator to find substrings\n",
        "\n",
        "\n"
    ]

def create_g7_01_01_rounding(original_lines):
    """Split G7.01.01 - keep rounding functions only"""
    return [
        "ID: T09.G7.01.01\n",
        "Topic: T09 – Variables & Expressions\n",
        "Skill: Use rounding functions (round, floor, ceiling) in expressions\n",
        "Description: Students use rounding functions to convert decimals to integers: round() rounds to nearest, floor() rounds down, ceiling() rounds up. They understand when each is appropriate. Examples: \"set rounded_score to round(score)\" for display, \"set pages to ceiling(items / 10)\" for pagination.\n",
        "\n",
        "Dependencies:\n",
        "* T09.G6.03: Use exponents (^) in expressions\n",
        "\n",
        "\n"
    ]

def create_g7_01_02_abs():
    """Create G7.01.02 for absolute value"""
    return [
        "ID: T09.G7.01.02\n",
        "Topic: T09 – Variables & Expressions\n",
        "Skill: Use absolute value (abs) function in expressions\n",
        "Description: Students use the abs() function to get the magnitude of a number without regard to sign (removes negative signs). They apply this for distance calculations, error magnitudes, or ensuring positive values. Example: \"set distance to abs(x1 - x2)\".\n",
        "\n",
        "Dependencies:\n",
        "* T09.G7.01.01: Use rounding functions (round, floor, ceiling) in expressions\n",
        "\n",
        "\n"
    ]

def create_g7_01_03_sqrt():
    """Create G7.01.03 for square root"""
    return [
        "ID: T09.G7.01.03\n",
        "Topic: T09 – Variables & Expressions\n",
        "Skill: Use square root (sqrt) function in expressions\n",
        "Description: Students use the sqrt() function to find square roots in calculations. They apply this for distance formulas (Pythagorean theorem), scaling, or inverse of squaring operations. Example: \"set distance to sqrt((x2-x1)^2 + (y2-y1)^2)\".\n",
        "\n",
        "Dependencies:\n",
        "* T09.G7.01.02: Use absolute value (abs) function in expressions\n",
        "\n",
        "\n"
    ]

def create_g5_03_01_multi_join():
    """Create new G5.03.01 for multi-input join"""
    return [
        "ID: T09.G5.03.01\n",
        "Topic: T09 – Variables & Expressions\n",
        "Skill: Use multi-input join with separator\n",
        "Description: Students use the advanced join block `join [T1] [T2] [T3] [T4] [T5] [T6] with [SEPARATOR]` to combine multiple strings with a separator between them. They apply this for creating CSV data, formatted lists, or comma-separated values. Example: join names with \", \" to create \"Alice, Bob, Carol\".\n",
        "\n",
        "Dependencies:\n",
        "* T09.G5.03: Join strings using concatenation\n",
        "\n",
        "\n"
    ]

def update_all_dependencies(skills):
    """Update dependencies in all skills to reference new split skills"""
    updated = {}

    # Map old skill IDs to new ones for dependency updates
    dep_mapping = {
        'T09.G4.01': ['T09.G4.01', 'T09.G4.01.01'],  # If depends on old G4.01, keep dependency on G4.01 (addition)
        'T09.G4.02': ['T09.G4.02', 'T09.G4.02.01'],  # If depends on old G4.02, now depends on G4.02.01 (both * and /)
        'T09.G4.06': ['T09.G4.06', 'T09.G4.06.01', 'T09.G4.06.02', 'T09.G4.06.03'],  # Depends on all comparison ops
        'T09.G6.04': ['T09.G6.04', 'T09.G6.04.01'],
        'T09.G6.05': ['T09.G6.05', 'T09.G6.05.01'],
        'T09.G7.01.01': ['T09.G7.01.01', 'T09.G7.01.02', 'T09.G7.01.03']
    }

    for skill_id, skill_lines in skills.items():
        new_lines = []
        for line in skill_lines:
            # Check if this is a dependency line that needs updating
            if line.startswith('* T09.G4.02:') and 'T09.G4.02' in dep_mapping:
                # Change dependency on old G4.02 to G4.02.01 (both ops)
                new_lines.append('* T09.G4.02.01: Use division (/) in expressions\n')
            elif line.startswith('* T09.G4.06:') and skill_id not in ['T09.G4.06.01', 'T09.G4.06.02', 'T09.G4.06.03']:
                # For skills depending on old G4.06, update to depend on all comparison operators
                # But only update if it's not one of the split skills
                new_lines.append('* T09.G4.06.03: Use greater-or-equal (≥) and less-or-equal (≤) operators\n')
            elif line.startswith('* T09.G6.04:') and skill_id not in ['T09.G6.04.01']:
                new_lines.append('* T09.G6.04.01: Use case conversion (uppercase/lowercase) operators\n')
            elif line.startswith('* T09.G6.05:') and skill_id not in ['T09.G6.05.01']:
                new_lines.append('* T09.G6.05.01: Use substring operator to extract text portions\n')
            elif line.startswith('* T09.G7.01.01:') and skill_id not in ['T09.G7.01.02', 'T09.G7.01.03']:
                new_lines.append('* T09.G7.01.03: Use square root (sqrt) function in expressions\n')
            else:
                new_lines.append(line)

        updated[skill_id] = new_lines

    return updated

if __name__ == '__main__':
    input_path = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'
    output_path = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    changes = optimize_t09(input_path, output_path)

    # Write changes to summary file
    with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/T09_optimization_changes.txt', 'w') as f:
        f.write("T09 Optimization Changes\n")
        f.write("=" * 50 + "\n\n")
        for change in changes:
            f.write(f"{change}\n")
