#!/usr/bin/env python3
"""
Analyze T06-T13 Programming Core Skills and Add Dependencies
"""

import json
import re
from collections import defaultdict

def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(data, filepath):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

def get_skill_by_id(skills, skill_id):
    for skill in skills:
        if skill['id'] == skill_id:
            return skill
    return None

def get_skills_by_topic_grade(skills, topic, grade):
    return [s for s in skills if s.get('topic_id') == topic and s.get('grade') == grade]

def analyze_dependencies():
    print("Loading skills...")
    t06_t13_skills = load_json('/tmp/skills_T06_T13.json')
    t01_t05_deps = load_json('/media/binyu/USB2/dev/CreatiCodeSkillMap/dependencies_T01_T05.json')
    all_skills = load_json('/media/binyu/USB2/dev/CreatiCodeSkillMap/skills_enriched.json')

    print(f"Loaded {len(t06_t13_skills)} skills from T06-T13")
    print(f"Loaded {len(t01_t05_deps)} dependency records from T01-T05")

    # Organize skills by topic
    skills_by_topic = defaultdict(list)
    for skill in t06_t13_skills:
        skills_by_topic[skill['topic_id']].append(skill)

    # Sort by grade within each topic
    for topic in skills_by_topic:
        skills_by_topic[topic].sort(key=lambda s: (s['grade'], s['id']))

    print("\nSkills per topic:")
    for topic in ['T06', 'T07', 'T08', 'T09', 'T10', 'T11', 'T12', 'T13']:
        count = len(skills_by_topic.get(topic, []))
        print(f"  {topic}: {count} skills")

    # Create dependency mappings
    dependencies = []
    gateway_skills = []
    quality_issues_summary = defaultdict(list)

    print("\n" + "="*80)
    print("ANALYZING DEPENDENCIES BY TOPIC")
    print("="*80)

    # T06: Events & Sequencing - FOUNDATION
    print("\n### T06: Events & Sequencing in Programs")
    print("This is the GATEWAY topic - enables all actual programming\n")

    for skill in skills_by_topic.get('T06', []):
        deps, cross_deps, notes, gateway, issues = analyze_T06_skill(skill, all_skills)
        dependencies.append({
            'id': skill['id'],
            'dependencies': deps,
            'cross_domain_dependencies': cross_deps,
            'notes': notes,
            'grade_level_ok': len(issues) == 0,
            'quality_issues': issues,
            'gateway_skill': gateway
        })
        if gateway:
            gateway_skills.append(skill['id'])
        for issue in issues:
            quality_issues_summary[issue].append(skill['id'])

    # T07: Loops & Repetition
    print("\n### T07: Loops & Repetition")
    print("Depends on: T06 (events), T04 (patterns), T01 (repetition)\n")

    for skill in skills_by_topic.get('T07', []):
        deps, cross_deps, notes, gateway, issues = analyze_T07_skill(skill, all_skills, skills_by_topic)
        dependencies.append({
            'id': skill['id'],
            'dependencies': deps,
            'cross_domain_dependencies': cross_deps,
            'notes': notes,
            'grade_level_ok': len(issues) == 0,
            'quality_issues': issues,
            'gateway_skill': gateway
        })
        if gateway:
            gateway_skills.append(skill['id'])
        for issue in issues:
            quality_issues_summary[issue].append(skill['id'])

    # T08: Conditionals & Logic
    print("\n### T08: Conditionals & Logic")
    print("Depends on: T06 (events), T01 (if/then thinking)\n")

    for skill in skills_by_topic.get('T08', []):
        deps, cross_deps, notes, gateway, issues = analyze_T08_skill(skill, all_skills, skills_by_topic)
        dependencies.append({
            'id': skill['id'],
            'dependencies': deps,
            'cross_domain_dependencies': cross_deps,
            'notes': notes,
            'grade_level_ok': len(issues) == 0,
            'quality_issues': issues,
            'gateway_skill': gateway
        })
        if gateway:
            gateway_skills.append(skill['id'])
        for issue in issues:
            quality_issues_summary[issue].append(skill['id'])

    # T09: Variables & Expressions
    print("\n### T09: Variables & Expressions")
    print("Depends on: T06 (events), used BY many topics\n")

    for skill in skills_by_topic.get('T09', []):
        deps, cross_deps, notes, gateway, issues = analyze_T09_skill(skill, all_skills, skills_by_topic)
        dependencies.append({
            'id': skill['id'],
            'dependencies': deps,
            'cross_domain_dependencies': cross_deps,
            'notes': notes,
            'grade_level_ok': len(issues) == 0,
            'quality_issues': issues,
            'gateway_skill': gateway
        })
        if gateway:
            gateway_skills.append(skill['id'])
        for issue in issues:
            quality_issues_summary[issue].append(skill['id'])

    # T10: Lists, Tables & Structured Data
    print("\n### T10: Lists, Tables & Structured Data")
    print("Depends on: T09 (variables), T07 (loops for iteration)\n")

    for skill in skills_by_topic.get('T10', []):
        deps, cross_deps, notes, gateway, issues = analyze_T10_skill(skill, all_skills, skills_by_topic)
        dependencies.append({
            'id': skill['id'],
            'dependencies': deps,
            'cross_domain_dependencies': cross_deps,
            'notes': notes,
            'grade_level_ok': len(issues) == 0,
            'quality_issues': issues,
            'gateway_skill': gateway
        })
        if gateway:
            gateway_skills.append(skill['id'])
        for issue in issues:
            quality_issues_summary[issue].append(skill['id'])

    # T11: Functions & Modularization
    print("\n### T11: Functions & Modularization")
    print("Depends on: T06 (events), T03 (decomposition), T09 (parameters)\n")

    for skill in skills_by_topic.get('T11', []):
        deps, cross_deps, notes, gateway, issues = analyze_T11_skill(skill, all_skills, skills_by_topic)
        dependencies.append({
            'id': skill['id'],
            'dependencies': deps,
            'cross_domain_dependencies': cross_deps,
            'notes': notes,
            'grade_level_ok': len(issues) == 0,
            'quality_issues': issues,
            'gateway_skill': gateway
        })
        if gateway:
            gateway_skills.append(skill['id'])
        for issue in issues:
            quality_issues_summary[issue].append(skill['id'])

    # T12: Program Organization, Style & Readability
    print("\n### T12: Program Organization, Style & Readability")
    print("Depends on: T03 (decomposition), T11 (functions)\n")

    for skill in skills_by_topic.get('T12', []):
        deps, cross_deps, notes, gateway, issues = analyze_T12_skill(skill, all_skills, skills_by_topic)
        dependencies.append({
            'id': skill['id'],
            'dependencies': deps,
            'cross_domain_dependencies': cross_deps,
            'notes': notes,
            'grade_level_ok': len(issues) == 0,
            'quality_issues': issues,
            'gateway_skill': gateway
        })
        if gateway:
            gateway_skills.append(skill['id'])
        for issue in issues:
            quality_issues_summary[issue].append(skill['id'])

    # T13: Testing, Debugging & Error Handling
    print("\n### T13: Testing, Debugging & Error Handling")
    print("Depends on: T02 (tracing), works with all programming constructs\n")

    for skill in skills_by_topic.get('T13', []):
        deps, cross_deps, notes, gateway, issues = analyze_T13_skill(skill, all_skills, skills_by_topic)
        dependencies.append({
            'id': skill['id'],
            'dependencies': deps,
            'cross_domain_dependencies': cross_deps,
            'notes': notes,
            'grade_level_ok': len(issues) == 0,
            'quality_issues': issues,
            'gateway_skill': gateway
        })
        if gateway:
            gateway_skills.append(skill['id'])
        for issue in issues:
            quality_issues_summary[issue].append(skill['id'])

    # Save results
    print("\n" + "="*80)
    print("SAVING RESULTS")
    print("="*80)

    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/dependencies_T06_T13.json'
    save_json(dependencies, output_file)
    print(f"\nSaved {len(dependencies)} dependency records to: {output_file}")

    # Print summary
    print("\n" + "="*80)
    print("SUMMARY STATISTICS")
    print("="*80)
    print(f"\nTotal skills analyzed: {len(dependencies)}")
    print(f"Gateway skills identified: {len(gateway_skills)}")
    print(f"Skills with quality issues: {sum(len(v) for v in quality_issues_summary.values())}")

    if gateway_skills:
        print(f"\nGateway Skills ({len(gateway_skills)}):")
        for gw in gateway_skills[:20]:  # Show first 20
            print(f"  - {gw}")
        if len(gateway_skills) > 20:
            print(f"  ... and {len(gateway_skills) - 20} more")

    if quality_issues_summary:
        print(f"\nQuality Issues by Type:")
        for issue_type, skills in quality_issues_summary.items():
            print(f"  {issue_type}: {len(skills)} skills")

    return dependencies, gateway_skills, quality_issues_summary


# Topic-specific analysis functions

def analyze_T06_skill(skill, all_skills):
    """T06: Events & Sequencing - GATEWAY to programming"""
    grade = skill['grade']
    skill_id = skill['id']
    title = skill['title'].lower()

    deps = []
    cross_deps = []
    notes = ""
    gateway = False
    issues = []

    # Grade 1: Foundational
    if grade == 1:
        if 'G1.01' in skill_id:
            notes = "Foundational - first exposure to events in programming"
            gateway = True
        else:
            deps.append('T06.G1.01')
            notes = "Builds on basic event understanding"

    # Grade 2: Event sequencing
    elif grade == 2:
        deps.append(f'T06.G{grade-1}.01')  # Previous grade foundation
        cross_deps.append('T01.G2.01')  # Algorithm understanding
        if 'broadcast' in title or 'message' in title:
            notes = "Introduces communication between sprites via events"
        else:
            notes = "Extends event understanding with sequencing"

    # Grade 3+: Events + other constructs
    elif grade >= 3:
        deps.append(f'T06.G{grade-1}.01')
        cross_deps.append(f'T01.G{grade}.01')

        # Gateway skills - basic coding with events
        if grade == 3 and 'G3.01' in skill_id:
            gateway = True
            notes = "GATEWAY: Transition from unplugged to actual coding with events"
        elif 'loop' in title:
            cross_deps.append(f'T07.G{grade}.01' if grade <= 8 else 'T07.G8.01')
            notes = "Combines events with loops"
        elif 'condition' in title or 'if' in title:
            cross_deps.append(f'T08.G{grade}.01' if grade <= 8 else 'T08.G8.01')
            notes = "Combines events with conditionals"
        elif 'variable' in title:
            cross_deps.append(f'T09.G{grade}.01' if grade <= 8 else 'T09.G8.01')
            notes = "Combines events with variables"
        else:
            notes = f"Event programming at grade {grade} level"

    return deps, cross_deps, notes, gateway, issues


def analyze_T07_skill(skill, all_skills, skills_by_topic):
    """T07: Loops & Repetition"""
    grade = skill['grade']
    skill_id = skill['id']
    title = skill['title'].lower()

    deps = []
    cross_deps = []
    notes = ""
    gateway = False
    issues = []

    # All loops depend on events
    cross_deps.append(f'T06.G{max(1, grade-1)}.01')

    # Grade 1-2: Conceptual (might not exist)
    if grade <= 2:
        cross_deps.append(f'T01.G{grade}.02')  # Algorithm repetition
        cross_deps.append('T04.G1.01')  # Pattern recognition
        notes = "Conceptual understanding of repetition"

    # Grade 3: Introduction to actual loops
    elif grade == 3:
        if 'G3.01' in skill_id:
            cross_deps.append('T01.G2.02')  # Algorithm with repeat
            cross_deps.append('T04.G2.01')  # Patterns
            notes = "GATEWAY: First actual coding with loops (repeat blocks)"
            gateway = True
        else:
            deps.append('T07.G3.01')
            cross_deps.append('T01.G3.03')
            notes = "Extends basic loop understanding"

    # Grade 4+
    else:
        deps.append(f'T07.G{grade-1}.01')

        if 'nested' in title:
            deps.append(f'T07.G{max(3, grade-1)}.01')  # Need basic loops
            notes = "Nested loops require solid understanding of basic loops"
        elif 'list' in title or 'array' in title or 'iterate' in title:
            cross_deps.append(f'T10.G{min(grade, 8)}.01')
            notes = "Loop iteration over lists requires list knowledge"
        elif 'variable' in title or 'counter' in title:
            cross_deps.append(f'T09.G{min(grade, 8)}.01')
            notes = "Loop counters require variable understanding"
        elif 'condition' in title or 'while' in title or 'until' in title:
            cross_deps.append(f'T08.G{min(grade, 8)}.01')
            notes = "Conditional loops combine loops and conditionals"
            if grade >= 5:
                gateway = True  # While loops are gateway to more advanced programming
        else:
            notes = f"Loop skills at grade {grade} level"

    return deps, cross_deps, notes, gateway, issues


def analyze_T08_skill(skill, all_skills, skills_by_topic):
    """T08: Conditionals & Logic"""
    grade = skill['grade']
    skill_id = skill['id']
    title = skill['title'].lower()

    deps = []
    cross_deps = []
    notes = ""
    gateway = False
    issues = []

    # All conditionals depend on events
    cross_deps.append(f'T06.G{max(1, grade-1)}.01')

    # Grade 1-2: Conceptual
    if grade <= 2:
        cross_deps.append(f'T01.G{grade}.01')  # If/then thinking
        notes = "Conceptual understanding of conditional logic"

    # Grade 3: Introduction to actual conditionals
    elif grade == 3:
        if 'G3.01' in skill_id:
            cross_deps.append('T01.G2.01')  # Algorithm with if/then
            notes = "GATEWAY: First actual coding with conditionals (if blocks)"
            gateway = True
        else:
            deps.append('T08.G3.01')
            cross_deps.append('T01.G3.02')
            notes = "Extends basic conditional understanding"

    # Grade 4+
    else:
        deps.append(f'T08.G{grade-1}.01')

        if 'nested' in title or 'complex' in title:
            deps.append(f'T08.G{max(3, grade-1)}.01')
            notes = "Nested conditionals require solid conditional understanding"
        elif 'else if' in title or 'multiple' in title:
            deps.append(f'T08.G{max(3, grade-1)}.01')
            notes = "Multiple branches extend basic if/else"
        elif 'and' in title or 'or' in title or 'not' in title or 'boolean' in title:
            deps.append(f'T08.G{max(3, grade-1)}.01')
            notes = "Boolean logic requires basic conditional understanding"
            if grade >= 5:
                gateway = True  # Boolean logic is gateway to complex conditions
        elif 'loop' in title:
            cross_deps.append(f'T07.G{min(grade, 8)}.01')
            notes = "Conditionals in loops combine both concepts"
        elif 'variable' in title:
            cross_deps.append(f'T09.G{min(grade, 8)}.01')
            notes = "Conditional logic with variables"
        else:
            notes = f"Conditional logic at grade {grade} level"

    return deps, cross_deps, notes, gateway, issues


def analyze_T09_skill(skill, all_skills, skills_by_topic):
    """T09: Variables & Expressions"""
    grade = skill['grade']
    skill_id = skill['id']
    title = skill['title'].lower()

    deps = []
    cross_deps = []
    notes = ""
    gateway = False
    issues = []

    # All variables depend on events (can't code without events)
    cross_deps.append(f'T06.G{max(1, grade-1)}.01')

    # Grade 1-2: Conceptual (counters in algorithms)
    if grade <= 2:
        cross_deps.append(f'T01.G{grade}.01')
        notes = "Conceptual understanding of storing and changing values"

    # Grade 3: Introduction to actual variables
    elif grade == 3:
        if 'G3.01' in skill_id:
            cross_deps.append('T01.G2.01')
            notes = "GATEWAY: First actual variables in code"
            gateway = True
        else:
            deps.append('T09.G3.01')
            notes = "Extends basic variable understanding"

    # Grade 4+
    else:
        deps.append(f'T09.G{grade-1}.01')

        if 'expression' in title or 'math' in title or 'calculation' in title:
            deps.append(f'T09.G{max(3, grade-1)}.01')
            notes = "Expressions build on basic variable use"
        elif 'string' in title or 'text' in title:
            deps.append(f'T09.G{max(3, grade-1)}.01')
            notes = "String variables extend numeric variables"
        elif 'scope' in title or 'local' in title or 'global' in title:
            cross_deps.append(f'T11.G{min(grade, 8)}.01')
            notes = "Variable scope requires function understanding"
        elif 'list' in title or 'array' in title:
            cross_deps.append(f'T10.G{min(grade, 8)}.01')
            notes = "Variables in lists/arrays"
        else:
            notes = f"Variable skills at grade {grade} level"
            if grade == 4 and 'G4.01' in skill_id:
                gateway = True  # Core variable manipulation

    return deps, cross_deps, notes, gateway, issues


def analyze_T10_skill(skill, all_skills, skills_by_topic):
    """T10: Lists, Tables & Structured Data"""
    grade = skill['grade']
    skill_id = skill['id']
    title = skill['title'].lower()

    deps = []
    cross_deps = []
    notes = ""
    gateway = False
    issues = []

    # Lists depend on variables (they're variable containers)
    cross_deps.append(f'T09.G{max(3, grade-1)}.01')
    # And events for coding
    cross_deps.append(f'T06.G{max(3, grade-1)}.01')

    # Grade 3-4: Introduction to lists
    if grade <= 4:
        if 'G3.01' in skill_id or 'G4.01' in skill_id:
            notes = "Introduction to list data structures"
            if 'G4.01' in skill_id:
                gateway = True
        else:
            deps.append(f'T10.G{grade}.01' if 'G3' not in skill_id else 'T10.G3.01')
            notes = "Extends list understanding"

    # Grade 5+
    else:
        deps.append(f'T10.G{grade-1}.01')

        if 'iterate' in title or 'loop' in title or 'for each' in title:
            cross_deps.append(f'T07.G{min(grade, 8)}.01')
            notes = "Iterating through lists requires loop understanding"
        elif '2d' in title or 'table' in title or 'grid' in title or 'matrix' in title:
            deps.append(f'T10.G{max(4, grade-1)}.01')
            notes = "2D arrays/tables build on 1D lists"
        elif 'search' in title or 'find' in title:
            cross_deps.append(f'T07.G{min(grade, 8)}.01')
            notes = "Searching lists typically uses loops"
        elif 'sort' in title:
            cross_deps.append(f'T07.G{min(grade, 8)}.01')
            cross_deps.append(f'T08.G{min(grade, 8)}.01')
            notes = "Sorting requires loops and conditionals"
        else:
            notes = f"List/data structure skills at grade {grade} level"

    return deps, cross_deps, notes, gateway, issues


def analyze_T11_skill(skill, all_skills, skills_by_topic):
    """T11: Functions & Modularization"""
    grade = skill['grade']
    skill_id = skill['id']
    title = skill['title'].lower()

    deps = []
    cross_deps = []
    notes = ""
    gateway = False
    issues = []

    # Functions depend on events and decomposition
    cross_deps.append(f'T06.G{max(3, grade-1)}.01')
    cross_deps.append(f'T03.G{min(grade, 8)}.01')

    # Grade 3-4: Introduction to custom blocks/functions
    if grade <= 4:
        if 'G3.01' in skill_id or 'G4.01' in skill_id:
            notes = "Introduction to custom blocks (functions)"
            if 'G4.01' in skill_id:
                gateway = True
        else:
            deps.append(f'T11.G{grade}.01' if 'G3' not in skill_id else 'T11.G3.01')
            notes = "Extends function understanding"

    # Grade 5+
    else:
        deps.append(f'T11.G{grade-1}.01')

        if 'parameter' in title or 'argument' in title or 'input' in title:
            cross_deps.append(f'T09.G{min(grade, 8)}.01')
            notes = "Function parameters require variable understanding"
            if grade >= 5:
                gateway = True
        elif 'return' in title or 'output' in title:
            deps.append(f'T11.G{max(4, grade-1)}.01')
            cross_deps.append(f'T09.G{min(grade, 8)}.01')
            notes = "Return values extend parameterized functions"
        elif 'recursive' in title or 'recursion' in title:
            deps.append(f'T11.G{max(5, grade-1)}.01')
            notes = "Recursion is advanced function concept"
        elif 'library' in title or 'module' in title:
            deps.append(f'T11.G{max(5, grade-1)}.01')
            cross_deps.append(f'T12.G{min(grade, 8)}.01')
            notes = "Libraries/modules combine functions with organization"
        else:
            notes = f"Function skills at grade {grade} level"

    return deps, cross_deps, notes, gateway, issues


def analyze_T12_skill(skill, all_skills, skills_by_topic):
    """T12: Program Organization, Style & Readability"""
    grade = skill['grade']
    skill_id = skill['id']
    title = skill['title'].lower()

    deps = []
    cross_deps = []
    notes = ""
    gateway = False
    issues = []

    # Organization depends on decomposition
    cross_deps.append(f'T03.G{min(grade, 8)}.01')

    # Also depends on having written code
    cross_deps.append(f'T06.G{max(3, grade-1)}.01')

    # Grade 3-4: Basic organization
    if grade <= 4:
        if 'comment' in title or 'name' in title:
            notes = "Basic code documentation and naming"
        else:
            notes = "Introduction to code organization"

    # Grade 5+
    else:
        deps.append(f'T12.G{grade-1}.01') if grade > 5 else None

        if 'function' in title or 'module' in title or 'block' in title:
            cross_deps.append(f'T11.G{min(grade, 8)}.01')
            notes = "Organizing code with functions/modules"
        elif 'refactor' in title:
            cross_deps.append(f'T11.G{min(grade, 8)}.01')
            notes = "Refactoring requires understanding functions and structure"
        elif 'style' in title or 'convention' in title:
            notes = "Code style and conventions"
        else:
            notes = f"Code organization at grade {grade} level"

    # Remove None from deps
    deps = [d for d in deps if d]

    return deps, cross_deps, notes, gateway, issues


def analyze_T13_skill(skill, all_skills, skills_by_topic):
    """T13: Testing, Debugging & Error Handling"""
    grade = skill['grade']
    skill_id = skill['id']
    title = skill['title'].lower()

    deps = []
    cross_deps = []
    notes = ""
    gateway = False
    issues = []

    # Testing depends on tracing
    cross_deps.append(f'T02.G{min(grade, 8)}.01')

    # And having code to test
    cross_deps.append(f'T06.G{max(3, grade-1)}.01')

    # Grade 3-4: Basic debugging
    if grade <= 4:
        if 'G3.01' in skill_id or 'G4.01' in skill_id:
            notes = "Introduction to debugging and testing"
            if 'G3.01' in skill_id:
                gateway = True  # First debugging is gateway
        else:
            deps.append(f'T13.G{grade}.01' if 'G3' not in skill_id else 'T13.G3.01')
            notes = "Extends debugging skills"

    # Grade 5+
    else:
        deps.append(f'T13.G{grade-1}.01')

        if 'test case' in title or 'test plan' in title:
            cross_deps.append(f'T03.G{min(grade, 8)}.01')
            notes = "Test planning requires decomposition"
        elif 'edge case' in title or 'boundary' in title:
            notes = "Advanced testing with edge cases"
        elif 'systematic' in title or 'strategy' in title:
            notes = "Systematic debugging strategies"
        elif 'error handling' in title or 'exception' in title or 'try' in title:
            notes = "Error handling is advanced debugging"
        else:
            notes = f"Testing/debugging at grade {grade} level"

    return deps, cross_deps, notes, gateway, issues


if __name__ == '__main__':
    analyze_dependencies()
