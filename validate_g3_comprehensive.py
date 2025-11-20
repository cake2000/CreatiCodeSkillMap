#!/usr/bin/env python3
"""
Comprehensive validation of Grade 3 skills after transitive dependency removal.
"""

import re
import json
from collections import defaultdict

def parse_markdown_skills(file_path):
    """Parse the markdown file and extract all skills."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by skill blocks (ID: ...)
    skill_blocks = re.split(r'\n\n(?=ID: )', content)

    skills = []
    for block in skill_blocks:
        if not block.strip() or not block.startswith('ID:'):
            continue

        # Extract ID
        id_match = re.search(r'ID:\s+([^\n]+)', block)
        if not id_match:
            continue
        skill_id = id_match.group(1).strip()

        # Extract grade from ID (e.g., T01.G3.01 -> 3, T01.GK.01 -> 0)
        grade_match = re.search(r'\.G(\d+|K)\.', skill_id)
        if not grade_match:
            continue

        grade_str = grade_match.group(1)
        if grade_str == 'K':
            grade = 0
        else:
            grade = int(grade_str)

        # Extract topic
        topic_match = re.search(r'Topic:\s+([^\n]+)', block)
        topic = topic_match.group(1).strip() if topic_match else ""

        # Extract skill title
        skill_match = re.search(r'Skill:\s+([^\n]+)', block)
        title = skill_match.group(1).strip() if skill_match else ""

        # Extract description
        desc_match = re.search(r'Description:\s+(.+?)(?=\n\nDependencies:|$)', block, re.DOTALL)
        description = desc_match.group(1).strip() if desc_match else ""

        # Extract dependencies
        dependencies = []
        deps_section = re.search(r'Dependencies:\s*\n((?:\*[^\n]+\n?)+)', block, re.DOTALL)
        if deps_section:
            dep_lines = deps_section.group(1).strip().split('\n')
            for line in dep_lines:
                # Match: * T01.GK.01: Put pictures in order...
                dep_match = re.search(r'\*\s+([^:]+):', line)
                if dep_match:
                    dependencies.append(dep_match.group(1).strip())

        skills.append({
            'id': skill_id,
            'title': title,
            'topic': topic,
            'grade': grade,
            'dependencies': dependencies,
            'description': description
        })

    return skills

def validate_g3_skills(skills):
    """Perform comprehensive validation of Grade 3 skills."""

    # Create skill lookup
    skill_map = {s['id']: s for s in skills}

    # Separate by grade
    g3_skills = [s for s in skills if s['grade'] == 3]

    print("=" * 80)
    print("GRADE 3 SKILLS COMPREHENSIVE VALIDATION REPORT")
    print("=" * 80)
    print()

    # 1. Basic counts
    print(f"Total skills in file: {len(skills)}")
    print(f"Grade 3 skills found: {len(g3_skills)}")
    print()

    # Track issues
    issues = []
    warnings = []

    # 2. Data integrity checks
    print("-" * 80)
    print("DATA INTEGRITY CHECKS")
    print("-" * 80)

    missing_title = [s for s in g3_skills if not s['title']]
    missing_desc = [s for s in g3_skills if not s['description']]

    print(f"Skills with missing titles: {len(missing_title)}")
    if missing_title:
        issues.append(f"Missing titles: {[s['id'] for s in missing_title]}")
        for s in missing_title[:5]:
            print(f"  - {s['id']}")

    print(f"Skills with missing descriptions: {len(missing_desc)}")
    if missing_desc:
        issues.append(f"Missing descriptions: {[s['id'] for s in missing_desc]}")
        for s in missing_desc[:5]:
            print(f"  - {s['id']}")

    # Check for duplicates
    id_counts = defaultdict(int)
    for s in g3_skills:
        id_counts[s['id']] += 1

    duplicates = {k: v for k, v in id_counts.items() if v > 1}
    print(f"Duplicate skill IDs: {len(duplicates)}")
    if duplicates:
        issues.append(f"Duplicate IDs found: {duplicates}")

    print()

    # 3. Dependency validation
    print("-" * 80)
    print("DEPENDENCY VALIDATION")
    print("-" * 80)

    empty_deps = []
    invalid_deps = []
    out_of_order_deps = []
    suspicious_low_deps = []

    for skill in g3_skills:
        skill_id = skill['id']
        deps = skill['dependencies']

        # Empty dependencies check
        if not deps:
            empty_deps.append(skill_id)

        # Low dependency count (potential over-removal)
        if len(deps) == 1:
            suspicious_low_deps.append((skill_id, len(deps)))

        # Check each dependency
        for dep in deps:
            # Invalid dependency (doesn't exist)
            if dep not in skill_map:
                invalid_deps.append((skill_id, dep))
                continue

            dep_skill = skill_map[dep]

            # Out of order dependency (G3 depending on G4+)
            if dep_skill['grade'] > 3:
                out_of_order_deps.append((skill_id, dep, dep_skill['grade']))

    print(f"Skills with empty dependencies: {len(empty_deps)}")
    if empty_deps:
        print(f"  First 10: {empty_deps[:10]}")
        warnings.append(f"{len(empty_deps)} skills have empty dependencies")

    print(f"Skills with invalid dependencies: {len(invalid_deps)}")
    if invalid_deps:
        issues.append(f"Invalid dependencies: {invalid_deps[:5]}")
        for skill_id, dep in invalid_deps[:5]:
            print(f"  - Skill {skill_id} depends on non-existent {dep}")

    print(f"Skills with out-of-order dependencies (G3->G4+): {len(out_of_order_deps)}")
    if out_of_order_deps:
        issues.append(f"Out-of-order dependencies: {out_of_order_deps[:5]}")
        for skill_id, dep, dep_grade in out_of_order_deps[:5]:
            print(f"  - Skill {skill_id} depends on G{dep_grade} skill {dep}")

    print(f"Skills with only 1 dependency: {len(suspicious_low_deps)}")
    if suspicious_low_deps and len(suspicious_low_deps) > 20:
        print(f"  First 10: {suspicious_low_deps[:10]}")
        warnings.append(f"{len(suspicious_low_deps)} skills have only 1 dependency")

    print()

    # 4. Transitive dependency detection
    print("-" * 80)
    print("TRANSITIVE DEPENDENCY ANALYSIS")
    print("-" * 80)

    transitive_issues = []
    for skill in g3_skills:
        skill_id = skill['id']
        direct_deps = set(skill['dependencies'])

        if len(direct_deps) < 2:
            continue

        # For each direct dependency, check if any of our other direct deps
        # are also dependencies of this dep
        for dep in direct_deps:
            if dep not in skill_map:
                continue

            # Get dependencies of this dependency
            dep_deps = set(skill_map[dep]['dependencies'])

            # Check if any of our other direct deps are in dep's dependencies
            other_direct_deps = direct_deps - {dep}
            overlap = other_direct_deps.intersection(dep_deps)
            if overlap:
                transitive_issues.append((skill_id, dep, list(overlap)))

    print(f"Skills with potential transitive dependencies: {len(transitive_issues)}")
    if transitive_issues:
        print(f"  First 10 examples:")
        for skill_id, through_dep, redundant in transitive_issues[:10]:
            print(f"    Skill {skill_id}: {redundant} may be transitive through {through_dep}")
        if len(transitive_issues) > 50:
            issues.append(f"{len(transitive_issues)} potential transitive dependencies remain")
        else:
            warnings.append(f"{len(transitive_issues)} potential transitive dependencies remain (acceptable)")
    else:
        print("  EXCELLENT: No obvious transitive dependencies detected!")

    print()

    # 5. Dependency statistics
    print("-" * 80)
    print("DEPENDENCY STATISTICS")
    print("-" * 80)

    dep_counts = [len(s['dependencies']) for s in g3_skills]
    if dep_counts:
        print(f"Total G3 skills: {len(g3_skills)}")
        print(f"Average dependencies per skill: {sum(dep_counts)/len(dep_counts):.2f}")
        print(f"Min dependencies: {min(dep_counts)}")
        print(f"Max dependencies: {max(dep_counts)}")
        print(f"Median dependencies: {sorted(dep_counts)[len(dep_counts)//2]}")

        # Distribution
        dist = defaultdict(int)
        for count in dep_counts:
            dist[count] += 1

        print("\nDependency count distribution:")
        for count in sorted(dist.keys())[:15]:
            bar = '#' * (dist[count] // 2)
            print(f"  {count:2d} deps: {dist[count]:3d} skills {bar}")

    print()

    # 6. Sample validation (spot checks)
    print("-" * 80)
    print("SPOT CHECK VALIDATION")
    print("-" * 80)

    # Check a few specific skills across different topics
    sample_skills = g3_skills[::30][:5]  # Every 30th skill, up to 5
    print(f"Examining sample of {len(sample_skills)} G3 skills:")
    for s in sample_skills:
        print(f"\n  Skill: {s['id']}")
        print(f"  Title: {s['title'][:60]}...")
        print(f"  Dependencies ({len(s['dependencies'])}): {s['dependencies'][:3]}")

    print()

    # 7. Final assessment
    print("=" * 80)
    print("FINAL ASSESSMENT")
    print("=" * 80)

    critical_issues = len([i for i in issues if 'Invalid' in str(i) or 'Out-of-order' in str(i) or 'Duplicate' in str(i)])

    if critical_issues > 0:
        status = "FAIL"
        print(f"STATUS: {status}")
        print(f"Critical issues found: {critical_issues}")
    elif len(issues) > 0:
        status = "PASS WITH WARNINGS"
        print(f"STATUS: {status}")
        print(f"Non-critical issues: {len(issues)}")
    else:
        status = "PASS"
        print(f"STATUS: {status}")
        print("All validation checks passed!")

    print()
    print(f"Total critical issues: {critical_issues}")
    print(f"Total warnings: {len(warnings)}")
    print(f"Total issues logged: {len(issues)}")

    if issues:
        print("\nISSUES SUMMARY:")
        for i, issue in enumerate(issues[:20], 1):
            issue_str = str(issue)[:200]
            print(f"  {i}. {issue_str}")

    if warnings:
        print("\nWARNINGS SUMMARY:")
        for i, warning in enumerate(warnings[:20], 1):
            print(f"  {i}. {warning}")

    print()
    print("=" * 80)
    print("IMPROVEMENTS ACHIEVED")
    print("=" * 80)
    print(f"Skills validated: {len(g3_skills)}")
    print(f"Data integrity: {'PASS' if not missing_title and not missing_desc else 'FAIL'}")
    print(f"Dependency validity: {'PASS' if not invalid_deps else 'FAIL'}")
    print(f"No out-of-order deps: {'PASS' if not out_of_order_deps else 'FAIL'}")
    print(f"Transitive deps status: {len(transitive_issues)} remaining (goal: < 50)")

    # Quality metrics
    avg_deps = sum(dep_counts) / len(dep_counts) if dep_counts else 0
    print(f"Average dependencies: {avg_deps:.2f} (target: 2-4)")
    print(f"Skills with 0 deps: {len(empty_deps)}")
    print(f"Skills with 1 dep: {len(suspicious_low_deps)}")

    # Return summary
    return {
        'status': status,
        'total_g3_skills': len(g3_skills),
        'critical_issues': critical_issues,
        'warnings': len(warnings),
        'transitive_deps_remaining': len(transitive_issues),
        'empty_deps': len(empty_deps),
        'invalid_deps': len(invalid_deps),
        'out_of_order_deps': len(out_of_order_deps),
        'avg_dependencies': avg_deps
    }

if __name__ == "__main__":
    file_path = "/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md"

    print("Parsing skills file...")
    skills = parse_markdown_skills(file_path)
    print(f"Parsed {len(skills)} skills total")
    print()

    result = validate_g3_skills(skills)

    print()
    print("=" * 80)
    print("VALIDATION COMPLETE")
    print("=" * 80)
    print(f"Final Status: {result['status']}")
    print(f"G3 Skills Validated: {result['total_g3_skills']}")
    print(f"Critical Issues: {result['critical_issues']}")
    print(f"Warnings: {result['warnings']}")
