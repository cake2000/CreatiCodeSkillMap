#!/usr/bin/env python3
"""
Verify that all G3 transitive fixes were applied correctly to allskills.md
"""

import json
import re

def load_json_fixes(json_path):
    """Load the fixes from JSON file"""
    with open(json_path, 'r') as f:
        return json.load(f)

def load_markdown_file(md_path):
    """Load the markdown file"""
    with open(md_path, 'r') as f:
        return f.read()

def verify_fixes(content, fixes):
    """Verify all fixes were applied correctly"""
    stats = {
        'total_fixes': len(fixes),
        'verified': 0,
        'failed': [],
        'warnings': []
    }

    for fix in fixes:
        skill_id = fix['skill_id']
        expected_deps = fix['final_deps']
        removed_deps = fix['remove_deps']

        # Find the skill section
        skill_pattern = rf'ID: {re.escape(skill_id)}\n.*?\nDependencies:\n((?:\* [^\n]+\n)*)'

        match = re.search(skill_pattern, content, re.DOTALL)

        if not match:
            stats['failed'].append({
                'skill_id': skill_id,
                'issue': 'Skill or dependencies section not found'
            })
            continue

        # Extract the dependencies block
        deps_block = match.group(1).strip()

        # Parse dependency IDs
        actual_deps = []
        if deps_block:
            for line in deps_block.split('\n'):
                if line.startswith('* '):
                    dep_id_match = re.match(r'\* ([^:]+):', line)
                    if dep_id_match:
                        actual_deps.append(dep_id_match.group(1))

        # Verify the dependencies match expected
        if sorted(actual_deps) == sorted(expected_deps):
            stats['verified'] += 1

            # Also check that removed deps are truly gone
            for removed in removed_deps:
                if removed in actual_deps:
                    stats['warnings'].append({
                        'skill_id': skill_id,
                        'warning': f'Removed dependency {removed} still present'
                    })
        else:
            stats['failed'].append({
                'skill_id': skill_id,
                'issue': f'Dependencies mismatch',
                'expected': expected_deps,
                'actual': actual_deps
            })

    return stats

def check_file_format(content):
    """Check that the file format is still valid"""
    issues = []

    # Check for basic structure
    skill_count = len(re.findall(r'^ID: T\d+\.G\d+\.\d+', content, re.MULTILINE))

    # Check for dependency sections
    deps_sections = len(re.findall(r'^Dependencies:', content, re.MULTILINE))

    print(f"\nFile Format Check:")
    print(f"  Total skills found: {skill_count}")
    print(f"  Dependency sections: {deps_sections}")

    # Look for any malformed dependency lines
    malformed = re.findall(r'\* [^:]+:[^\n]{200,}', content)
    if malformed:
        issues.append(f"Found {len(malformed)} potentially malformed dependency lines")

    return issues

def print_report(stats, format_issues):
    """Print the detailed verification report"""
    print("\n" + "="*80)
    print("G3 TRANSITIVE FIXES VERIFICATION REPORT")
    print("="*80)

    print(f"\nTotal fixes verified: {stats['total_fixes']}")
    print(f"Successfully verified: {stats['verified']}")
    print(f"Failed verification: {len(stats['failed'])}")
    print(f"Warnings: {len(stats['warnings'])}")

    if stats['failed']:
        print("\n" + "-"*80)
        print("FAILED VERIFICATIONS:")
        print("-"*80)
        for failure in stats['failed']:
            print(f"\nSkill: {failure['skill_id']}")
            print(f"  Issue: {failure['issue']}")
            if 'expected' in failure:
                print(f"  Expected: {', '.join(failure['expected']) if failure['expected'] else '[]'}")
                print(f"  Actual: {', '.join(failure['actual']) if failure['actual'] else '[]'}")

    if stats['warnings']:
        print("\n" + "-"*80)
        print("WARNINGS:")
        print("-"*80)
        for warning in stats['warnings']:
            print(f"  {warning['skill_id']}: {warning['warning']}")

    if format_issues:
        print("\n" + "-"*80)
        print("FORMAT ISSUES:")
        print("-"*80)
        for issue in format_issues:
            print(f"  - {issue}")

    print("\n" + "="*80)
    if stats['verified'] == stats['total_fixes'] and not stats['warnings'] and not format_issues:
        print("SUCCESS: All fixes verified correctly!")
    else:
        print("REVIEW NEEDED: Some issues found")
    print("="*80 + "\n")

def main():
    json_path = '/media/binyu/USB2/dev/CreatiCodeSkillMap/G3_TRANSITIVE_FIXES.json'
    md_path = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("Loading fixes from JSON...")
    fixes = load_json_fixes(json_path)

    print(f"Loading allskills.md...")
    content = load_markdown_file(md_path)

    print(f"Verifying {len(fixes)} fixes...")
    stats = verify_fixes(content, fixes)

    print("Checking file format...")
    format_issues = check_file_format(content)

    print_report(stats, format_issues)

if __name__ == '__main__':
    main()
