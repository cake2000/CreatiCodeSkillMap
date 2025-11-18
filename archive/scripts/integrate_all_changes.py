#!/usr/bin/env python3
"""
Complete Integration Script for CreatiCode K-8 Skill Map
Performs steps 4-8: Integration of all changes and comprehensive validation
"""

import json
from collections import defaultdict
from typing import Dict, List, Set, Tuple
import re

# File paths
CANONICAL_FILE = "skills_k8_ai_complete_WEEK2.json"
FOUNDATIONAL_FILE = "FOUNDATIONAL_41_SKILLS.json"
CREATIVE_FILE = "CREATIVE_SKILLS_3.json"
ACSL_FIXES_FILE = "ACSL_DEPENDENCY_FIXES.json"
OUTPUT_FILE = "skills_k8_ai_complete_FINAL.json"

# Statistics tracking
class IntegrationStats:
    def __init__(self):
        self.original_count = 0
        self.foundational_added = 0
        self.creative_added = 0
        self.acsl_skills_modified = 0
        self.dependencies_fixed = 0
        self.warnings = []
        self.errors = []

    def add_warning(self, msg):
        self.warnings.append(msg)
        print(f"WARNING: {msg}")

    def add_error(self, msg):
        self.errors.append(msg)
        print(f"ERROR: {msg}")

stats = IntegrationStats()
validation_results = {}

def load_json_file(filepath):
    """Load and parse JSON file"""
    print(f"\nLoading {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"  Loaded {len(data) if isinstance(data, list) else 'data'}")
    return data

def skill_sort_key(skill):
    """Generate sort key for skills: topic_id, grade, skill number"""
    topic_match = re.match(r'T(\d+)', skill['topic_id'])
    topic_num = int(topic_match.group(1)) if topic_match else 0

    grade = skill['grade']
    # Convert grade to numeric for sorting
    if isinstance(grade, str):
        if grade == 'K':
            grade_num = 0
        else:
            grade_num = int(grade)
    else:
        grade_num = int(grade)

    # Extract skill number from ID (T##.G#.##)
    skill_match = re.search(r'\.(\d+)$', skill['id'])
    skill_num = int(skill_match.group(1)) if skill_match else 0

    return (topic_num, grade_num, skill_num)

def integrate_foundational_skills(canonical_skills, foundational_skills):
    """Step 4: Integrate 41 foundational block skills"""
    print("\n" + "="*70)
    print("STEP 4: Integrating 41 Foundational Block Skills")
    print("="*70)

    # Create ID lookup for duplicates check
    existing_ids = {skill['id'] for skill in canonical_skills}

    added_count = 0
    duplicate_count = 0

    for skill in foundational_skills:
        skill_id = skill['id']
        if skill_id in existing_ids:
            stats.add_warning(f"Duplicate ID found: {skill_id} - Skipping")
            duplicate_count += 1
        else:
            canonical_skills.append(skill)
            existing_ids.add(skill_id)
            added_count += 1
            print(f"  Added: {skill_id} - {skill['title']}")

    stats.foundational_added = added_count
    print(f"\n✓ Added {added_count} foundational skills")
    if duplicate_count > 0:
        print(f"✗ Skipped {duplicate_count} duplicates")

    return canonical_skills

def integrate_creative_skills(canonical_skills, creative_skills):
    """Step 5: Integrate 3 creative skills"""
    print("\n" + "="*70)
    print("STEP 5: Integrating 3 Creative Skills")
    print("="*70)

    existing_ids = {skill['id'] for skill in canonical_skills}

    added_count = 0
    duplicate_count = 0

    for skill in creative_skills:
        skill_id = skill['id']
        if skill_id in existing_ids:
            stats.add_warning(f"Duplicate ID found: {skill_id} - Skipping")
            duplicate_count += 1
        else:
            canonical_skills.append(skill)
            existing_ids.add(skill_id)
            added_count += 1
            print(f"  Added: {skill_id} - {skill['title']}")

    stats.creative_added = added_count
    print(f"\n✓ Added {added_count} creative skills")
    if duplicate_count > 0:
        print(f"✗ Skipped {duplicate_count} duplicates")

    return canonical_skills

def apply_acsl_cleanup(skills_dict):
    """Step 6: Apply ACSL cleanup to 9 skills"""
    print("\n" + "="*70)
    print("STEP 6: Applying ACSL Cleanup to 9 Skills")
    print("="*70)

    # Part A: Mark 3 skills as competition-only
    print("\nPart A: Marking 3 skills as competition-only")
    competition_skills = {
        "T02.G7.03": "Count and compare steps needed for different algorithms",
        "T01.G6.01": "Efficiency analysis (theoretical)",
        "T04.G6.04": "Pattern efficiency comparison"
    }

    for skill_id, description in competition_skills.items():
        if skill_id in skills_dict:
            skill = skills_dict[skill_id]
            skill['difficulty_track'] = 'competition'
            skill['competition_tags'] = skill.get('competition_tags', [])
            if 'ACSL_junior' not in skill['competition_tags']:
                skill['competition_tags'].append('ACSL_junior')
            skill['optional'] = True
            skill['theoretical_cs'] = True
            skill['age_appropriateness_review'] = '2025-11-17'
            skill['reviewed_by'] = 'ACSL Cleanup'
            print(f"  ✓ Marked {skill_id} as competition-only: {description}")
            stats.acsl_skills_modified += 1
        else:
            stats.add_warning(f"Competition skill not found: {skill_id}")

    # Part B: Reframe 6 skills
    print("\nPart B: Reframing 6 skills for age-appropriateness")

    reframe_updates = {
        "T02.G4.03": {
            "title": "Plan step-by-step before coding",
            "terminology_simplified": "pseudocode → plan step-by-step"
        },
        "T02.G5.03": {
            "title": "Plan your code with steps",
            "terminology_simplified": "pseudocode → plan with steps"
        },
        "T01.G7.02": {
            "title": "Choose the right approach for your problem",
            "terminology_simplified": "algorithm choice → approach choice"
        },
        "T01.G7.04": {
            "title": "Test your code with unusual inputs",
            "terminology_simplified": "analyze correctness → test thoroughly"
        },
        "T02.G7.04": {
            "title": "Debug by following your code step-by-step",
            "terminology_simplified": "trace algorithm → debug step-by-step"
        },
        "T02.G6.03": {
            "title": "Plan complex code with multiple steps",
            "terminology_simplified": "pseudocode with nesting → plan complex code"
        }
    }

    for skill_id, updates in reframe_updates.items():
        if skill_id in skills_dict:
            skill = skills_dict[skill_id]
            old_title = skill['title']
            skill['title'] = updates['title']
            skill['terminology_simplified'] = updates['terminology_simplified']
            skill['age_appropriateness_review'] = '2025-11-17'
            skill['reviewed_by'] = 'ACSL Cleanup'
            print(f"  ✓ Reframed {skill_id}")
            print(f"    Old: {old_title}")
            print(f"    New: {updates['title']}")
            stats.acsl_skills_modified += 1
        else:
            stats.add_warning(f"Reframe skill not found: {skill_id}")

    print(f"\n✓ Modified {stats.acsl_skills_modified} ACSL skills")
    return skills_dict

def update_dependencies(skills_dict, acsl_fixes):
    """Step 7: Update dependencies"""
    print("\n" + "="*70)
    print("STEP 7: Updating Dependencies")
    print("="*70)

    # Part A: Verify new skill dependencies
    print("\nPart A: Verifying new skill dependencies")
    all_skill_ids = set(skills_dict.keys())

    new_skill_ids = [
        'T06.G3.01', 'T06.G3.02', 'T06.G3.03', 'T06.G3.04', 'T06.G3.05',
        'T07.G3.01', 'T07.G3.02', 'T07.G3.03', 'T07.G3.04',
        'T08.G3.01', 'T08.G3.02', 'T08.G3.03', 'T08.G3.04',
        'T10.G3.01', 'T10.G3.02', 'T10.G3.03', 'T10.G3.04', 'T10.G3.05',
        'T05.G3.01', 'T05.G3.02', 'T05.G3.03', 'T05.G3.04', 'T05.G3.05', 'T05.G3.06', 'T05.G3.07',
        'T11.G3.01', 'T11.G3.02', 'T11.G3.03', 'T11.G3.04', 'T11.G3.05', 'T11.G3.06',
        'T12.G3.01', 'T12.G3.02',
        'T09.G3.01', 'T09.G3.02', 'T09.G3.03', 'T09.G3.04', 'T09.G3.05',
        'T13.G3.01', 'T13.G3.02', 'T13.G3.03',
        'T20.G7.05', 'T16.G7.06', 'T05.G6.07'
    ]

    broken_deps = []
    for skill_id in new_skill_ids:
        if skill_id in skills_dict:
            skill = skills_dict[skill_id]
            deps = skill.get('dependencies', [])
            for dep_id in deps:
                if dep_id not in all_skill_ids:
                    broken_deps.append((skill_id, dep_id))
                    stats.add_error(f"Broken dependency: {skill_id} → {dep_id}")

    if not broken_deps:
        print("  ✓ All new skill dependencies are valid")
    else:
        print(f"  ✗ Found {len(broken_deps)} broken dependencies in new skills")

    # Part B: Apply documented dependency fixes
    print("\nPart B: Applying ACSL dependency fixes")

    competition_skills = acsl_fixes.get('competition_only_skills', {})
    fixes_applied = 0

    for comp_skill_id, comp_data in competition_skills.items():
        dependency_fixes = comp_data.get('dependency_fixes_required', [])

        for fix in dependency_fixes:
            skill_id = fix['skill_id']
            action = fix['action']
            rationale = fix['rationale']

            if skill_id in skills_dict:
                skill = skills_dict[skill_id]
                deps = skill.get('dependencies', [])

                if comp_skill_id in deps:
                    deps.remove(comp_skill_id)
                    skill['dependencies'] = deps
                    skill['dependency_count'] = len(deps)
                    print(f"  ✓ Removed {comp_skill_id} from {skill_id}")
                    print(f"    Reason: {rationale}")
                    fixes_applied += 1
                    stats.dependencies_fixed += 1
            else:
                stats.add_warning(f"Dependency fix target not found: {skill_id}")

    print(f"\n✓ Applied {fixes_applied} dependency fixes")

    # Part C: Check for broken dependencies across entire skill map
    print("\nPart C: Scanning for broken dependencies across entire skill map")

    all_broken_deps = []
    for skill_id, skill in skills_dict.items():
        deps = skill.get('dependencies', [])
        for dep_id in deps:
            if dep_id not in all_skill_ids:
                all_broken_deps.append((skill_id, dep_id))

    if all_broken_deps:
        print(f"  ✗ Found {len(all_broken_deps)} broken dependencies:")
        for skill_id, dep_id in all_broken_deps[:10]:  # Show first 10
            print(f"    {skill_id} → {dep_id} (missing)")
            stats.add_error(f"Broken dependency: {skill_id} → {dep_id}")
    else:
        print("  ✓ No broken dependencies found")

    return skills_dict

def validate_skill_map(skills_list, skills_dict):
    """Step 8: Comprehensive validation"""
    print("\n" + "="*70)
    print("STEP 8: Comprehensive Validation")
    print("="*70)

    validation_results['basic'] = validate_basic(skills_list, skills_dict)
    validation_results['fields'] = validate_fields(skills_list)
    validation_results['dependencies'] = validate_dependencies(skills_dict)
    validation_results['quality'] = validate_quality(skills_dict)
    validation_results['statistics'] = calculate_statistics(skills_list)

    return validation_results

def validate_basic(skills_list, skills_dict):
    """Basic validation checks"""
    print("\nA. Basic Validation")
    results = {}

    # Check unique IDs
    ids = [s['id'] for s in skills_list]
    duplicates = [id for id in ids if ids.count(id) > 1]
    unique_duplicates = list(set(duplicates))

    if not unique_duplicates:
        print("  ✓ All skill IDs are unique")
        results['unique_ids'] = True
    else:
        print(f"  ✗ Found {len(unique_duplicates)} duplicate IDs: {unique_duplicates[:5]}")
        results['unique_ids'] = False
        for dup_id in unique_duplicates:
            stats.add_error(f"Duplicate ID: {dup_id}")

    # Check ID format
    invalid_ids = []
    for skill in skills_list:
        skill_id = skill['id']
        if not re.match(r'T\d+\.G[K\d]\.\\d+', skill_id):
            invalid_ids.append(skill_id)

    if not invalid_ids:
        print("  ✓ All skill IDs follow format")
        results['valid_format'] = True
    else:
        print(f"  ✗ Found {len(invalid_ids)} invalid ID formats")
        results['valid_format'] = False

    # Check grades
    valid_grades = ['K', '1', '2', '3', '4', '5', '6', '7', '8', 0, 1, 2, 3, 4, 5, 6, 7, 8]
    invalid_grades = []
    for skill in skills_list:
        grade = skill.get('grade')
        if grade not in valid_grades:
            invalid_grades.append((skill['id'], grade))

    if not invalid_grades:
        print("  ✓ All grades are valid")
        results['valid_grades'] = True
    else:
        print(f"  ✗ Found {len(invalid_grades)} invalid grades")
        results['valid_grades'] = False

    # Check topic IDs
    invalid_topics = []
    for skill in skills_list:
        topic_id = skill.get('topic_id', '')
        if not re.match(r'T\d{2}', topic_id):
            invalid_topics.append((skill['id'], topic_id))

    if not invalid_topics:
        print("  ✓ All topic IDs are valid")
        results['valid_topics'] = True
    else:
        print(f"  ✗ Found {len(invalid_topics)} invalid topic IDs")
        results['valid_topics'] = False

    # Check JSON structure (already validated by loading)
    print("  ✓ JSON structure is valid")
    results['valid_json'] = True

    return results

def validate_fields(skills_list):
    """Field validation checks"""
    print("\nB. Field Validation")
    results = {}

    required_fields = ['id', 'title', 'description', 'grade', 'topic_id']
    missing_fields = []

    for skill in skills_list:
        for field in required_fields:
            if field not in skill or skill[field] is None or skill[field] == '':
                missing_fields.append((skill['id'], field))

    if not missing_fields:
        print("  ✓ All required fields present")
        results['required_fields'] = True
    else:
        print(f"  ✗ Found {len(missing_fields)} missing required fields")
        results['required_fields'] = False

    # Check estimated minutes
    invalid_minutes = []
    for skill in skills_list:
        minutes = skill.get('estimated_minutes')
        if minutes and (minutes < 5 or minutes > 120):
            invalid_minutes.append((skill['id'], minutes))

    if not invalid_minutes:
        print("  ✓ All estimated minutes are reasonable (5-120)")
        results['valid_minutes'] = True
    else:
        print(f"  ✗ Found {len(invalid_minutes)} skills with unreasonable time estimates")
        results['valid_minutes'] = False

    # Check competition tags
    invalid_tags = []
    for skill in skills_list:
        tags = skill.get('competition_tags', [])
        if not isinstance(tags, list):
            invalid_tags.append(skill['id'])

    if not invalid_tags:
        print("  ✓ All competition tags are valid arrays")
        results['valid_tags'] = True
    else:
        print(f"  ✗ Found {len(invalid_tags)} skills with invalid competition tags")
        results['valid_tags'] = False

    return results

def validate_dependencies(skills_dict):
    """Dependency validation checks"""
    print("\nC. Dependency Validation")
    results = {}

    all_ids = set(skills_dict.keys())

    # Check if all dependencies exist
    broken_deps = []
    for skill_id, skill in skills_dict.items():
        deps = skill.get('dependencies', [])
        for dep_id in deps:
            if dep_id not in all_ids:
                broken_deps.append((skill_id, dep_id))

    if not broken_deps:
        print("  ✓ All dependency IDs exist")
        results['deps_exist'] = True
    else:
        print(f"  ✗ Found {len(broken_deps)} broken dependencies")
        results['deps_exist'] = False

    # Check for self-references
    self_refs = []
    for skill_id, skill in skills_dict.items():
        deps = skill.get('dependencies', [])
        if skill_id in deps:
            self_refs.append(skill_id)

    if not self_refs:
        print("  ✓ No self-references found")
        results['no_self_refs'] = True
    else:
        print(f"  ✗ Found {len(self_refs)} self-references")
        results['no_self_refs'] = False

    # Check for forward grade references
    forward_refs = []
    for skill_id, skill in skills_dict.items():
        skill_grade = skill.get('grade')
        deps = skill.get('dependencies', [])
        for dep_id in deps:
            if dep_id in skills_dict:
                dep_grade = skills_dict[dep_id].get('grade')
                # Convert grades to numbers for comparison
                sg = 0 if skill_grade == 'K' else int(skill_grade)
                dg = 0 if dep_grade == 'K' else int(dep_grade)
                if dg > sg:
                    forward_refs.append((skill_id, dep_id))

    if not forward_refs:
        print("  ✓ No forward grade references")
        results['no_forward_refs'] = True
    else:
        print(f"  ✗ Found {len(forward_refs)} forward grade references")
        results['no_forward_refs'] = False

    # Check dependency counts match
    count_mismatches = []
    for skill_id, skill in skills_dict.items():
        deps = skill.get('dependencies', [])
        count = skill.get('dependency_count', 0)
        if len(deps) != count:
            count_mismatches.append((skill_id, len(deps), count))
            # Auto-fix
            skill['dependency_count'] = len(deps)

    if not count_mismatches:
        print("  ✓ All dependency counts match")
        results['counts_match'] = True
    else:
        print(f"  ✓ Fixed {len(count_mismatches)} dependency count mismatches")
        results['counts_match'] = True

    return results

def validate_quality(skills_dict):
    """Quality validation checks"""
    print("\nD. Quality Validation")
    results = {}

    # Check gateway skills
    gateway_missing = []
    for skill_id, skill in skills_dict.items():
        if skill.get('is_gateway') and not isinstance(skill.get('is_gateway'), bool):
            gateway_missing.append(skill_id)

    gateway_count = sum(1 for s in skills_dict.values() if s.get('is_gateway') == True)
    print(f"  ✓ Found {gateway_count} gateway skills")
    results['gateway_count'] = gateway_count

    # Check competition-only skills
    competition_missing = []
    for skill_id, skill in skills_dict.items():
        if skill.get('difficulty_track') == 'competition':
            if 'competition_tags' not in skill or not skill['competition_tags']:
                competition_missing.append(skill_id)

    if not competition_missing:
        print("  ✓ All competition-only skills have competition_tags")
        results['competition_tagged'] = True
    else:
        print(f"  ✗ Found {len(competition_missing)} competition skills without tags")
        results['competition_tagged'] = False

    # Check Grade 3 foundational skills
    g3_foundational = sum(1 for s in skills_dict.values()
                          if s.get('grade') == 3 and s.get('foundational') == True)
    print(f"  ✓ Found {g3_foundational} Grade 3 foundational skills")
    results['g3_foundational'] = g3_foundational

    # Check quality level
    ixl_count = sum(1 for s in skills_dict.values()
                    if s.get('quality_level') == 'IXL_for_coding')
    print(f"  ✓ Found {ixl_count} skills with quality_level: IXL_for_coding")
    results['ixl_count'] = ixl_count

    return results

def calculate_statistics(skills_list):
    """Calculate skill map statistics"""
    print("\nE. Statistical Validation")
    results = {}

    total = len(skills_list)
    print(f"  Total skills: {total}")
    results['total'] = total

    # Skills per grade
    grade_dist = defaultdict(int)
    for skill in skills_list:
        grade = skill.get('grade', 'Unknown')
        grade_dist[grade] += 1

    print("\n  Skills per grade:")
    for grade in ['K', 1, 2, 3, 4, 5, 6, 7, 8]:
        count = grade_dist.get(grade, 0)
        print(f"    Grade {grade}: {count}")
    results['grade_distribution'] = dict(grade_dist)

    # Skills per topic
    topic_dist = defaultdict(int)
    for skill in skills_list:
        topic = skill.get('topic_id', 'Unknown')
        topic_dist[topic] += 1

    print(f"\n  Skills across {len(topic_dist)} topics (showing top 10):")
    sorted_topics = sorted(topic_dist.items(), key=lambda x: x[1], reverse=True)
    for topic, count in sorted_topics[:10]:
        print(f"    {topic}: {count}")
    results['topic_distribution'] = dict(topic_dist)

    # Dependency statistics
    total_deps = sum(len(s.get('dependencies', [])) for s in skills_list)
    avg_deps = total_deps / len(skills_list) if skills_list else 0
    print(f"\n  Total dependencies: {total_deps}")
    print(f"  Average dependencies per skill: {avg_deps:.2f}")
    results['total_dependencies'] = total_deps
    results['avg_dependencies'] = avg_deps

    return results

def write_validation_report(results, stats):
    """Write comprehensive validation report"""
    print("\n" + "="*70)
    print("Writing Validation Report")
    print("="*70)

    report = []
    report.append("# Integration & Validation Report")
    report.append("## CreatiCode K-8 Skill Map - Final Integration\n")
    report.append(f"**Date:** 2025-11-17")
    report.append(f"**Total Skills:** {results['statistics']['total']}\n")

    report.append("## Integration Summary\n")
    report.append(f"- **Original skills:** {stats.original_count}")
    report.append(f"- **Foundational skills added:** {stats.foundational_added}")
    report.append(f"- **Creative skills added:** {stats.creative_added}")
    report.append(f"- **ACSL skills modified:** {stats.acsl_skills_modified}")
    report.append(f"- **Dependencies fixed:** {stats.dependencies_fixed}")
    report.append(f"- **Final total:** {results['statistics']['total']}\n")

    report.append("## Validation Results\n")

    report.append("### A. Basic Validation\n")
    for key, value in results['basic'].items():
        status = "✓ PASS" if value else "✗ FAIL"
        report.append(f"- {key}: {status}")

    report.append("\n### B. Field Validation\n")
    for key, value in results['fields'].items():
        status = "✓ PASS" if value else "✗ FAIL"
        report.append(f"- {key}: {status}")

    report.append("\n### C. Dependency Validation\n")
    for key, value in results['dependencies'].items():
        status = "✓ PASS" if value else "✗ FAIL"
        report.append(f"- {key}: {status}")

    report.append("\n### D. Quality Validation\n")
    report.append(f"- Gateway skills: {results['quality']['gateway_count']}")
    report.append(f"- Grade 3 foundational skills: {results['quality']['g3_foundational']}")
    report.append(f"- IXL quality level skills: {results['quality']['ixl_count']}")

    report.append("\n### E. Statistics\n")
    report.append(f"- Total dependencies: {results['statistics']['total_dependencies']}")
    report.append(f"- Average dependencies per skill: {results['statistics']['avg_dependencies']:.2f}")

    report.append("\n#### Grade Distribution\n")
    for grade in ['K', 1, 2, 3, 4, 5, 6, 7, 8]:
        count = results['statistics']['grade_distribution'].get(grade, 0)
        report.append(f"- Grade {grade}: {count}")

    report.append("\n## Warnings\n")
    if stats.warnings:
        for warning in stats.warnings:
            report.append(f"- {warning}")
    else:
        report.append("No warnings")

    report.append("\n## Errors\n")
    if stats.errors:
        for error in stats.errors:
            report.append(f"- {error}")
    else:
        report.append("No errors")

    report.append("\n## Conclusion\n")
    if not stats.errors:
        report.append("✓ **READY FOR PRODUCTION** - All validation checks passed")
    else:
        report.append(f"✗ **NEEDS ATTENTION** - {len(stats.errors)} errors found")

    with open("INTEGRATION_VALIDATION_REPORT.md", "w", encoding="utf-8") as f:
        f.write("\n".join(report))

    print("✓ Wrote INTEGRATION_VALIDATION_REPORT.md")

def write_changes_summary(stats):
    """Write changes summary"""
    summary = []
    summary.append("# Integration Changes Summary\n")

    summary.append("## Foundational Skills Added (41 skills)\n")
    summary.append("All Grade 3 foundational block skills:")
    foundational_ids = [
        'T06.G3.01', 'T06.G3.02', 'T06.G3.03', 'T06.G3.04', 'T06.G3.05',
        'T07.G3.01', 'T07.G3.02', 'T07.G3.03', 'T07.G3.04',
        'T08.G3.01', 'T08.G3.02', 'T08.G3.03', 'T08.G3.04',
        'T10.G3.01', 'T10.G3.02', 'T10.G3.03', 'T10.G3.04', 'T10.G3.05',
        'T05.G3.01', 'T05.G3.02', 'T05.G3.03', 'T05.G3.04', 'T05.G3.05', 'T05.G3.06', 'T05.G3.07',
        'T11.G3.01', 'T11.G3.02', 'T11.G3.03', 'T11.G3.04', 'T11.G3.05', 'T11.G3.06',
        'T12.G3.01', 'T12.G3.02',
        'T09.G3.01', 'T09.G3.02', 'T09.G3.03', 'T09.G3.04', 'T09.G3.05',
        'T13.G3.01', 'T13.G3.02', 'T13.G3.03'
    ]
    for skill_id in foundational_ids:
        summary.append(f"- {skill_id}")

    summary.append("\n## Creative Skills Added (3 skills)\n")
    creative_ids = ['T20.G7.05', 'T16.G7.06', 'T05.G6.07']
    for skill_id in creative_ids:
        summary.append(f"- {skill_id}")

    summary.append("\n## ACSL Skills Modified (9 skills)\n")
    summary.append("\n### Competition-Only (3 skills)\n")
    summary.append("- T02.G7.03 - Marked competition-only")
    summary.append("- T01.G6.01 - Marked competition-only")
    summary.append("- T04.G6.04 - Marked competition-only")

    summary.append("\n### Reframed (6 skills)\n")
    summary.append("- T02.G4.03 - Title updated for age-appropriateness")
    summary.append("- T02.G5.03 - Title updated for age-appropriateness")
    summary.append("- T01.G7.02 - Title updated for age-appropriateness")
    summary.append("- T01.G7.04 - Title updated for age-appropriateness")
    summary.append("- T02.G7.04 - Title updated for age-appropriateness")
    summary.append("- T02.G6.03 - Title updated for age-appropriateness")

    summary.append(f"\n## Dependencies Updated\n")
    summary.append(f"- Total dependency fixes applied: {stats.dependencies_fixed}")
    summary.append("- Removed competition-only skills from standard track dependencies")

    with open("INTEGRATION_CHANGES_SUMMARY.md", "w", encoding="utf-8") as f:
        f.write("\n".join(summary))

    print("✓ Wrote INTEGRATION_CHANGES_SUMMARY.md")

def write_statistics_json(results):
    """Write machine-readable statistics"""
    stats_output = {
        "total_skills": results['statistics']['total'],
        "grade_distribution": results['statistics']['grade_distribution'],
        "topic_distribution": results['statistics']['topic_distribution'],
        "dependency_stats": {
            "total_dependencies": results['statistics']['total_dependencies'],
            "avg_dependencies": results['statistics']['avg_dependencies']
        },
        "quality_metrics": {
            "gateway_skills": results['quality']['gateway_count'],
            "grade_3_foundational": results['quality']['g3_foundational'],
            "ixl_quality_level": results['quality']['ixl_count']
        }
    }

    with open("FINAL_SKILL_MAP_STATISTICS.json", "w", encoding="utf-8") as f:
        json.dump(stats_output, f, indent=2)

    print("✓ Wrote FINAL_SKILL_MAP_STATISTICS.json")

def write_checklist():
    """Write production readiness checklist"""
    checklist = """# Integration Complete Checklist

## Production Readiness

### Data Integrity
- [ ] All 1,140 original skills preserved
- [ ] 41 foundational skills added successfully
- [ ] 3 creative skills added successfully
- [ ] 9 ACSL skills modified correctly
- [ ] No duplicate skill IDs
- [ ] No data loss occurred

### Validation
- [ ] All skill IDs are unique
- [ ] All skill IDs follow T##.G#.## format
- [ ] All grades are valid (K, 1-8)
- [ ] All topic IDs are valid (T01-T36)
- [ ] JSON structure is valid
- [ ] All required fields present
- [ ] No null values in required fields
- [ ] All dependency IDs exist
- [ ] No self-references in dependencies
- [ ] No forward grade references
- [ ] Dependency counts match arrays
- [ ] Estimated minutes are reasonable (5-120)

### Quality
- [ ] Gateway skills marked correctly
- [ ] Competition-only skills tagged
- [ ] Grade 3 foundational skills marked
- [ ] Quality levels assigned
- [ ] Age-appropriateness reviewed

### Integration Completeness
- [ ] All foundational block skills integrated
- [ ] All creative skills integrated
- [ ] Competition-only skills marked
- [ ] Reframed skills updated
- [ ] Dependencies cleaned up
- [ ] No broken dependencies

## Sign-Off Criteria

**Total Skills:** ~1,193 (expected: 1,140 + 41 + 3 + adjustments)

**Validation:** All checks must PASS

**Errors:** Zero critical errors

**Warnings:** Documented and reviewed

## Rollback Plan

If issues are found:
1. Restore from `skills_k8_ai_complete_WEEK2.json`
2. Review error logs in `INTEGRATION_VALIDATION_REPORT.md`
3. Fix issues and re-run integration

## Next Steps

1. **Review** - Examine validation report for any warnings
2. **Test** - Load skill map in application and verify functionality
3. **Deploy** - Replace canonical file with FINAL version
4. **Monitor** - Watch for any issues in production
5. **Document** - Update changelog and version history

## Files Generated

- `skills_k8_ai_complete_FINAL.json` - New canonical file
- `INTEGRATION_VALIDATION_REPORT.md` - Comprehensive validation results
- `INTEGRATION_CHANGES_SUMMARY.md` - What changed
- `FINAL_SKILL_MAP_STATISTICS.json` - Machine-readable stats
- `INTEGRATION_COMPLETE_CHECKLIST.md` - This checklist

---
**Integration Date:** 2025-11-17
**Reviewer:** [Your Name]
**Status:** [PENDING REVIEW / APPROVED / REJECTED]
"""

    with open("INTEGRATION_COMPLETE_CHECKLIST.md", "w", encoding="utf-8") as f:
        f.write(checklist)

    print("✓ Wrote INTEGRATION_COMPLETE_CHECKLIST.md")

def main():
    """Main integration workflow"""
    print("\n" + "="*70)
    print("CreatiCode K-8 Skill Map - Complete Integration")
    print("Steps 4-8: Integration & Validation")
    print("="*70)

    # Load all files
    canonical_skills = load_json_file(CANONICAL_FILE)
    foundational_skills = load_json_file(FOUNDATIONAL_FILE)
    creative_skills = load_json_file(CREATIVE_FILE)
    acsl_fixes = load_json_file(ACSL_FIXES_FILE)

    stats.original_count = len(canonical_skills)

    # Step 4: Integrate foundational skills
    canonical_skills = integrate_foundational_skills(canonical_skills, foundational_skills)

    # Step 5: Integrate creative skills
    canonical_skills = integrate_creative_skills(canonical_skills, creative_skills)

    # Sort skills by topic, grade, skill number
    print("\nSorting skills by topic_id, grade, skill number...")
    canonical_skills.sort(key=skill_sort_key)
    print("✓ Skills sorted")

    # Create dict for easier lookup
    skills_dict = {skill['id']: skill for skill in canonical_skills}

    # Step 6: Apply ACSL cleanup
    skills_dict = apply_acsl_cleanup(skills_dict)

    # Step 7: Update dependencies
    skills_dict = update_dependencies(skills_dict, acsl_fixes)

    # Convert back to list
    final_skills = [skills_dict[skill_id] for skill_id in sorted(skills_dict.keys(), key=lambda id: skill_sort_key(skills_dict[id]))]

    # Step 8: Validate
    results = validate_skill_map(final_skills, skills_dict)

    # Write output files
    print("\n" + "="*70)
    print("Writing Output Files")
    print("="*70)

    # Write final canonical file
    print(f"\nWriting {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(final_skills, f, indent=2, ensure_ascii=False)
    print(f"✓ Wrote {OUTPUT_FILE} with {len(final_skills)} skills")

    # Write validation report
    write_validation_report(results, stats)

    # Write changes summary
    write_changes_summary(stats)

    # Write statistics
    write_statistics_json(results)

    # Write checklist
    write_checklist()

    # Final summary
    print("\n" + "="*70)
    print("INTEGRATION COMPLETE")
    print("="*70)
    print(f"\n✓ Original skills: {stats.original_count}")
    print(f"✓ Foundational skills added: {stats.foundational_added}")
    print(f"✓ Creative skills added: {stats.creative_added}")
    print(f"✓ ACSL skills modified: {stats.acsl_skills_modified}")
    print(f"✓ Dependencies fixed: {stats.dependencies_fixed}")
    print(f"✓ Final total: {len(final_skills)}")

    if stats.errors:
        print(f"\n⚠ {len(stats.errors)} errors found - review validation report")
    else:
        print(f"\n✓ No errors - READY FOR PRODUCTION")

    if stats.warnings:
        print(f"⚠ {len(stats.warnings)} warnings - review validation report")

    print("\nFiles generated:")
    print(f"  1. {OUTPUT_FILE}")
    print(f"  2. INTEGRATION_VALIDATION_REPORT.md")
    print(f"  3. INTEGRATION_CHANGES_SUMMARY.md")
    print(f"  4. FINAL_SKILL_MAP_STATISTICS.json")
    print(f"  5. INTEGRATION_COMPLETE_CHECKLIST.md")

    print("\n" + "="*70)

if __name__ == "__main__":
    main()
