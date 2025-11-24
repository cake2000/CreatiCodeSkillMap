#!/usr/bin/env python3
"""
Improved Grade K skills analysis with better parsing and more accurate dependency analysis.
"""

import re
from collections import defaultdict
from typing import Dict, List, Set, Tuple

def parse_skills_file(filepath: str) -> Dict[str, Dict]:
    """Parse the allskills.md file and extract all skills with their metadata."""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    skills = {}

    # Find all skill blocks using ID as marker
    pattern = r'ID:\s*(T\d+\.[A-Z]+\.\d+)\s*\nTopic:\s*([^\n]+)\s*\nSkill:\s*([^\n]+)\s*\nDescription:\s*([^\n]+(?:\n(?!ID:|Dependencies:)[^\n]+)*)'

    matches = re.finditer(pattern, content, re.MULTILINE)

    for match in matches:
        skill_id = match.group(1).strip()
        topic = match.group(2).strip()
        skill_name = match.group(3).strip()
        description = match.group(4).strip()

        # Find dependencies for this skill
        # Look for Dependencies section after this skill ID
        start_pos = match.end()
        # Find next ID or end of file
        next_id_match = re.search(r'\nID:', content[start_pos:])
        if next_id_match:
            skill_content = content[start_pos:start_pos + next_id_match.start()]
        else:
            skill_content = content[start_pos:]

        # Extract dependencies
        dependencies = []
        dep_section = re.search(r'Dependencies:\s*\n((?:\*[^\n]+\n?)+)', skill_content)
        if dep_section:
            dep_text = dep_section.group(1)
            dep_ids = re.findall(r'(T\d+\.[A-Z]+\.\d+)', dep_text)
            dependencies = dep_ids

        skills[skill_id] = {
            'id': skill_id,
            'topic': topic,
            'skill': skill_name,
            'description': description,
            'dependencies': dependencies
        }

    return skills

def extract_grade_k_skills(skills: Dict[str, Dict]) -> Dict[str, Dict]:
    """Extract only Grade K skills."""
    return {sid: data for sid, data in skills.items() if '.GK.' in sid}

def analyze_x_minus_2_violations(gk_skills: Dict[str, Dict], all_skills: Dict[str, Dict]) -> List[Dict]:
    """Find Grade K skills that depend on non-Grade K skills (X-2 rule violations)."""
    violations = []

    for skill_id, skill_data in gk_skills.items():
        for dep_id in skill_data['dependencies']:
            if '.GK.' not in dep_id:
                violations.append({
                    'skill_id': skill_id,
                    'skill_name': skill_data['skill'],
                    'dependency_id': dep_id,
                    'dependency_name': all_skills.get(dep_id, {}).get('skill', 'UNKNOWN'),
                    'violation_type': 'X-2 rule violation'
                })

    return violations

def find_meaningful_missing_deps(gk_skills: Dict[str, Dict]) -> List[Dict]:
    """Identify meaningful missing cross-topic dependencies."""
    suggestions = []

    # Game skills that might need event/loop dependencies
    game_skills = ['T14.GK.01', 'T14.GK.02', 'T14.GK.03']
    for skill_id in game_skills:
        if skill_id in gk_skills:
            skill = gk_skills[skill_id]
            # Check if they have event dependencies
            has_event_dep = any('T06.' in dep for dep in skill['dependencies'])
            if not has_event_dep:
                # T14.GK.01 already has T06.GK.01, others might need it
                if skill_id in ['T14.GK.02', 'T14.GK.03']:
                    suggestions.append({
                        'skill_id': skill_id,
                        'skill_name': skill['skill'],
                        'missing_topic': 'T06 (Events)',
                        'reason': 'Game interaction requires understanding of events',
                        'priority': 'Medium'
                    })

    # T01.GK.08 (counting) might benefit from T04.GK.01 (patterns) since it's already dependent
    if 'T01.GK.08' in gk_skills:
        skill = gk_skills['T01.GK.08']
        # It already depends on T01.GK.07 which depends on T04.GK.01, so this is fine

    # Check T26 (data collection) - it should have solid foundations
    data_collection_skill = 'T26.GK.02'
    if data_collection_skill in gk_skills:
        skill = gk_skills[data_collection_skill]
        # Already has T26.GK.01, T01.GK.07, T04.GK.01 - good coverage

    # T08.GK.01 is about conditionals but is foundational - might want T01.GK.04 (picking what makes sense)
    if 'T08.GK.01' in gk_skills:
        skill = gk_skills['T08.GK.01']
        has_t01_dep = any('T01.' in dep for dep in skill['dependencies'])
        if not has_t01_dep:
            suggestions.append({
                'skill_id': 'T08.GK.01',
                'skill_name': skill['skill'],
                'missing_topic': 'T01 (Algorithms)',
                'reason': 'Understanding conditional rules benefits from algorithm sequencing (e.g., T01.GK.04)',
                'priority': 'Medium'
            })

    # T13.GK.02 has T01.GK.01, T13.GK.01 - might benefit from T01.GK.05 (fixing order)
    if 'T13.GK.02' in gk_skills:
        skill = gk_skills['T13.GK.02']
        # Check if it has T01.GK.05 (move wrong picture)
        if 'T01.GK.05' not in skill['dependencies']:
            suggestions.append({
                'skill_id': 'T13.GK.02',
                'skill_name': skill['skill'],
                'missing_topic': 'T01.GK.05',
                'reason': 'Fixing/debugging benefits from understanding how to fix sequencing errors',
                'priority': 'Low'
            })

    return suggestions

def detect_circular_dependencies(gk_skills: Dict[str, Dict]) -> List[Dict]:
    """Detect circular dependencies among Grade K skills."""
    circles = []
    visited_cycles = set()

    def has_cycle(start: str, current: str, path: List[str], visited: Set[str]) -> bool:
        if current == start and len(path) > 1:
            # Found a cycle
            cycle_tuple = tuple(sorted(path))
            if cycle_tuple not in visited_cycles:
                visited_cycles.add(cycle_tuple)
                circles.append({
                    'cycle': path.copy(),
                    'description': f"{' -> '.join(path)} -> {start}"
                })
            return True

        if current in visited:
            return False

        visited.add(current)

        if current in gk_skills:
            for dep in gk_skills[current]['dependencies']:
                if dep in gk_skills:  # Only check GK dependencies
                    if has_cycle(start, dep, path + [dep], visited.copy()):
                        return True

        return False

    for skill_id in gk_skills:
        has_cycle(skill_id, skill_id, [skill_id], set())

    return circles

def find_redundant_transitive_deps(gk_skills: Dict[str, Dict]) -> List[Dict]:
    """Find truly redundant transitive dependencies."""
    redundant = []

    def get_all_descendants(skill_id: str, visited: Set[str] = None) -> Set[str]:
        """Get all transitive dependencies of a skill."""
        if visited is None:
            visited = set()
        if skill_id in visited or skill_id not in gk_skills:
            return set()

        visited.add(skill_id)
        descendants = set()

        for dep in gk_skills[skill_id]['dependencies']:
            if dep in gk_skills:
                descendants.add(dep)
                descendants.update(get_all_descendants(dep, visited.copy()))

        return descendants

    for skill_id, skill_data in gk_skills.items():
        direct_deps = [d for d in skill_data['dependencies'] if d in gk_skills]

        if len(direct_deps) < 2:
            continue

        # Check if any direct dependency is reachable through another
        for dep in direct_deps:
            # Get descendants of all other direct deps
            other_deps = [d for d in direct_deps if d != dep]
            reachable_from = []

            for other_dep in other_deps:
                if dep in get_all_descendants(other_dep):
                    reachable_from.append(other_dep)

            if reachable_from:
                redundant.append({
                    'skill_id': skill_id,
                    'skill_name': skill_data['skill'],
                    'redundant_dep': dep,
                    'reachable_via': reachable_from,
                    'recommendation': f"Remove {dep} from {skill_id} (reachable via {', '.join(reachable_from)})"
                })

    return redundant

def find_overlapping_skills(gk_skills: Dict[str, Dict]) -> List[Dict]:
    """Find skills with very similar descriptions across different topics."""
    overlaps = []
    skill_list = list(gk_skills.items())

    for i, (id1, data1) in enumerate(skill_list):
        for id2, data2 in skill_list[i+1:]:
            # Skip same topic
            topic1 = id1.split('.')[0]
            topic2 = id2.split('.')[0]
            if topic1 == topic2:
                continue

            # Check skill names for similarity
            name1 = data1['skill'].lower()
            name2 = data2['skill'].lower()

            # Look for key phrase overlaps
            if 'count' in name1 and 'count' in name2:
                overlaps.append({
                    'skill1_id': id1,
                    'skill1_name': data1['skill'],
                    'skill2_id': id2,
                    'skill2_name': data2['skill'],
                    'similarity': 'Both involve counting',
                    'note': 'May be intentionally different contexts'
                })
            elif 'match' in name1 and 'match' in name2:
                overlaps.append({
                    'skill1_id': id1,
                    'skill1_name': data1['skill'],
                    'skill2_id': id2,
                    'skill2_name': data2['skill'],
                    'similarity': 'Both involve matching',
                    'note': 'May be intentionally different contexts'
                })
            elif 'order' in name1 and 'order' in name2:
                overlaps.append({
                    'skill1_id': id1,
                    'skill1_name': data1['skill'],
                    'skill2_id': id2,
                    'skill2_name': data2['skill'],
                    'similarity': 'Both involve ordering',
                    'note': 'May be intentionally different contexts'
                })

            # Check for very similar names
            words1 = set(name1.split())
            words2 = set(name2.split())
            common = words1 & words2
            total = words1 | words2

            if len(common) >= 3 and len(common) / len(total) > 0.6:
                overlaps.append({
                    'skill1_id': id1,
                    'skill1_name': data1['skill'],
                    'skill2_id': id2,
                    'skill2_name': data2['skill'],
                    'similarity': f"{len(common)}/{len(total)} words in common",
                    'note': 'High textual similarity - review needed'
                })

    return overlaps

def check_scaffolding(gk_skills: Dict[str, Dict]) -> List[Dict]:
    """Verify that complex skills have sufficient prerequisites."""
    issues = []

    # More refined complexity detection
    for skill_id, skill_data in gk_skills.items():
        text_to_check = skill_data['skill'].lower()

        # True complexity indicators for kindergarten
        true_complexity = ['fix', 'debug', 'wrong', 'missing', 'replace', 'change']
        is_truly_complex = any(keyword in text_to_check for keyword in true_complexity)

        gk_deps = [d for d in skill_data['dependencies'] if d in gk_skills]

        if is_truly_complex and len(gk_deps) == 0:
            issues.append({
                'skill_id': skill_id,
                'skill_name': skill_data['skill'],
                'issue': 'Complex skill with no Grade K dependencies',
                'complexity_indicators': [k for k in true_complexity if k in text_to_check],
                'recommendation': 'Add prerequisite dependencies for sequencing/ordering'
            })

        # Check for "identify" or "match" skills that are truly foundational vs complex
        if any(word in text_to_check for word in ['identify', 'match', 'spot', 'recognize']):
            # These are only issues if they seem to require prior knowledge
            if len(gk_deps) == 0 and skill_id.split('.')[2] != '01':
                # Not the first skill in topic, probably should have deps
                context_words = ['ai', 'computing', 'device', 'tech', 'data']
                if any(word in text_to_check for word in context_words):
                    issues.append({
                        'skill_id': skill_id,
                        'skill_name': skill_data['skill'],
                        'issue': 'Recognition skill with no dependencies (may need foundational skills)',
                        'complexity_indicators': ['context-specific recognition'],
                        'recommendation': 'Consider if basic matching/sorting skills should be prerequisites'
                    })

    return issues

def analyze_topic_coverage(gk_skills: Dict[str, Dict]) -> Dict:
    """Analyze which topics have Grade K skills and their interconnections."""
    topic_info = defaultdict(lambda: {'count': 0, 'skills': [], 'incoming_deps': set(), 'outgoing_deps': set()})

    for skill_id, skill_data in gk_skills.items():
        topic = skill_id.split('.')[0]
        topic_info[topic]['count'] += 1
        topic_info[topic]['skills'].append(skill_id)

        for dep in skill_data['dependencies']:
            if dep in gk_skills:
                dep_topic = dep.split('.')[0]
                if dep_topic != topic:
                    topic_info[topic]['outgoing_deps'].add(dep_topic)
                    topic_info[dep_topic]['incoming_deps'].add(topic)

    return dict(topic_info)

def main():
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("Parsing skills file...")
    all_skills = parse_skills_file(filepath)
    print(f"Total skills parsed: {len(all_skills)}")

    print("\nExtracting Grade K skills...")
    gk_skills = extract_grade_k_skills(all_skills)
    print(f"Total Grade K skills: {len(gk_skills)}")

    # Group by topic
    by_topic = defaultdict(list)
    for skill_id in sorted(gk_skills.keys()):
        topic = skill_id.split('.')[0]
        by_topic[topic].append(skill_id)

    print(f"\nGrade K skills across {len(by_topic)} topics:")
    for topic in sorted(by_topic.keys()):
        print(f"  {topic}: {len(by_topic[topic])} skills")

    print("\n" + "="*80)
    print("ANALYSIS PHASE")
    print("="*80)

    print("\n1. Analyzing X-2 rule violations...")
    violations = analyze_x_minus_2_violations(gk_skills, all_skills)
    print(f"   Found {len(violations)} violations")

    print("\n2. Finding meaningful missing cross-topic dependencies...")
    missing_deps = find_meaningful_missing_deps(gk_skills)
    print(f"   Found {len(missing_deps)} potential missing dependencies")

    print("\n3. Detecting circular dependencies...")
    circles = detect_circular_dependencies(gk_skills)
    print(f"   Found {len(circles)} circular dependencies")

    print("\n4. Finding redundant transitive dependencies...")
    redundant = find_redundant_transitive_deps(gk_skills)
    print(f"   Found {len(redundant)} redundant dependencies")

    print("\n5. Finding overlapping skills...")
    overlaps = find_overlapping_skills(gk_skills)
    print(f"   Found {len(overlaps)} potential overlaps")

    print("\n6. Checking scaffolding...")
    scaffolding_issues = check_scaffolding(gk_skills)
    print(f"   Found {len(scaffolding_issues)} scaffolding issues")

    print("\n7. Analyzing topic coverage...")
    topic_coverage = analyze_topic_coverage(gk_skills)

    # Generate report
    print("\n\nGenerating detailed report...")
    report = generate_report(gk_skills, by_topic, violations, missing_deps, circles,
                           redundant, overlaps, scaffolding_issues, topic_coverage, all_skills)

    output_path = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/grade_k_phase2_analysis.md'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"Report written to: {output_path}")

def generate_report(gk_skills, by_topic, violations, missing_deps, circles,
                   redundant, overlaps, scaffolding_issues, topic_coverage, all_skills) -> str:
    """Generate the markdown report."""

    report = []
    report.append("# Grade K Skills - Phase 2 Dependency Analysis\n")
    report.append(f"**Generated**: 2025-11-24\n")
    report.append(f"**Total Grade K Skills Analyzed**: {len(gk_skills)}\n")
    report.append(f"**Topics with Grade K Coverage**: {len(by_topic)}\n")

    # Executive Summary
    report.append("\n## Executive Summary\n")
    report.append(f"- **X-2 Rule Violations**: {len(violations)} violations found")
    report.append(f"- **Missing Cross-Topic Dependencies**: {len(missing_deps)} meaningful gaps identified")
    report.append(f"- **Circular Dependencies**: {len(circles)} cycles detected")
    report.append(f"- **Redundant Dependencies**: {len(redundant)} transitive redundancies")
    report.append(f"- **Overlapping Skills**: {len(overlaps)} potential duplicates")
    report.append(f"- **Scaffolding Issues**: {len(scaffolding_issues)} complex skills needing review\n")

    # Topic Coverage Analysis
    report.append("\n## Topic Coverage Analysis\n")
    report.append("Cross-topic dependency relationships at Grade K level:\n")

    for topic in sorted(topic_coverage.keys()):
        info = topic_coverage[topic]
        report.append(f"\n### {topic}")
        report.append(f"- Skills: {info['count']}")
        if info['outgoing_deps']:
            report.append(f"- Depends on topics: {', '.join(sorted(info['outgoing_deps']))}")
        if info['incoming_deps']:
            report.append(f"- Depended upon by: {', '.join(sorted(info['incoming_deps']))}")

    # Grade K Skills by Topic
    report.append("\n\n## Complete List of Grade K Skills\n")

    for topic in sorted(by_topic.keys()):
        if by_topic[topic]:
            first_skill = gk_skills[by_topic[topic][0]]
            topic_name = first_skill['topic']
            report.append(f"\n### {topic}: {topic_name}\n")

            for skill_id in by_topic[topic]:
                skill_data = gk_skills[skill_id]
                report.append(f"\n**{skill_id}**: {skill_data['skill']}")

                if skill_data['dependencies']:
                    # Separate GK and non-GK dependencies
                    gk_deps = [d for d in skill_data['dependencies'] if '.GK.' in d]
                    non_gk_deps = [d for d in skill_data['dependencies'] if '.GK.' not in d]

                    if gk_deps:
                        report.append(f"  - GK Dependencies: {', '.join(gk_deps)}")
                    if non_gk_deps:
                        report.append(f"  - ⚠️ NON-GK Dependencies: {', '.join(non_gk_deps)} (X-2 VIOLATION)")
                else:
                    report.append(f"  - Dependencies: None (foundational skill)")

    # X-2 Rule Violations
    report.append("\n\n## 1. X-2 Rule Violations\n")
    report.append("**Rule**: Grade K skills should only depend on other Grade K skills.\n")

    if violations:
        report.append(f"\n⚠️ **CRITICAL**: Found {len(violations)} violations\n")
        for v in violations:
            report.append(f"\n### {v['skill_id']}: {v['skill_name']}")
            report.append(f"- **Invalid Dependency**: {v['dependency_id']} ({v['dependency_name']})")
            report.append(f"- **Action Required**: Remove this dependency or replace with equivalent GK skill")
    else:
        report.append("\n✅ **PASS**: No X-2 rule violations found.\n")

    # Missing Cross-Topic Dependencies
    report.append("\n\n## 2. Missing Cross-Topic Dependencies\n")

    if missing_deps:
        report.append(f"\nFound {len(missing_deps)} skills that may benefit from additional dependencies:\n")
        for m in missing_deps:
            report.append(f"\n### {m['skill_id']}: {m['skill_name']}")
            report.append(f"- **Suggested Addition**: {m['missing_topic']}")
            report.append(f"- **Rationale**: {m['reason']}")
            report.append(f"- **Priority**: {m['priority']}")
    else:
        report.append("\n✅ No missing cross-topic dependencies identified.\n")

    # Circular Dependencies
    report.append("\n\n## 3. Circular Dependencies\n")

    if circles:
        report.append(f"\n⚠️ **CRITICAL**: Found {len(circles)} circular dependency chains:\n")
        for c in circles:
            report.append(f"\n- **Cycle**: {c['description']}")
            report.append(f"  - **Action Required**: Break the cycle by removing one dependency link")
    else:
        report.append("\n✅ **PASS**: No circular dependencies detected. Dependency graph is acyclic.\n")

    # Redundant Dependencies
    report.append("\n\n## 4. Redundant Transitive Dependencies\n")

    if redundant:
        report.append(f"\nFound {len(redundant)} redundant direct dependencies:\n")
        for r in redundant:
            report.append(f"\n### {r['skill_id']}: {r['skill_name']}")
            report.append(f"- **Redundant Dependency**: {r['redundant_dep']}")
            report.append(f"- **Already Reachable Via**: {', '.join(r['reachable_via'])}")
            report.append(f"- **Recommendation**: {r['recommendation']}")
    else:
        report.append("\n✅ No redundant transitive dependencies found.\n")

    # Overlapping Skills
    report.append("\n\n## 5. Overlapping Skills Across Topics\n")

    if overlaps:
        report.append(f"\nFound {len(overlaps)} pairs of skills with similar characteristics:\n")
        for o in overlaps:
            report.append(f"\n### Potential Overlap")
            report.append(f"- **Skill 1**: {o['skill1_id']} - {o['skill1_name']}")
            report.append(f"- **Skill 2**: {o['skill2_id']} - {o['skill2_name']}")
            report.append(f"- **Similarity**: {o['similarity']}")
            report.append(f"- **Note**: {o.get('note', 'Review for potential consolidation')}")
    else:
        report.append("\n✅ No significant skill overlaps detected.\n")

    # Scaffolding Issues
    report.append("\n\n## 6. Scaffolding Analysis\n")

    if scaffolding_issues:
        report.append(f"\nFound {len(scaffolding_issues)} skills that may need additional scaffolding:\n")
        for s in scaffolding_issues:
            report.append(f"\n### {s['skill_id']}: {s['skill_name']}")
            report.append(f"- **Issue**: {s['issue']}")
            report.append(f"- **Indicators**: {', '.join(s['complexity_indicators'])}")
            report.append(f"- **Recommendation**: {s['recommendation']}")
    else:
        report.append("\n✅ All complex skills have appropriate scaffolding.\n")

    # Detailed Recommendations
    report.append("\n\n## Recommended Actions (Prioritized)\n")

    if violations or circles:
        report.append("\n### 🔴 HIGH PRIORITY - Critical Issues\n")
        if violations:
            report.append(f"\n1. **Fix X-2 Rule Violations** ({len(violations)} violations)")
            report.append("   - These prevent the curriculum from meeting grade-level constraints")
            for v in violations:
                report.append(f"   - Remove {v['dependency_id']} from {v['skill_id']}")
        if circles:
            report.append(f"\n2. **Break Circular Dependencies** ({len(circles)} cycles)")
            report.append("   - These create impossible learning sequences")
            for c in circles:
                report.append(f"   - {c['description']}")

    if missing_deps or redundant:
        report.append("\n### 🟡 MEDIUM PRIORITY - Optimization Opportunities\n")
        if missing_deps:
            report.append(f"\n3. **Consider Adding Cross-Topic Dependencies** ({len(missing_deps)} suggestions)")
            for m in missing_deps:
                if m['priority'] == 'Medium':
                    report.append(f"   - {m['skill_id']}: Add {m['missing_topic']}")
        if redundant:
            report.append(f"\n4. **Remove Redundant Dependencies** ({len(redundant)} redundancies)")
            for r in redundant:
                report.append(f"   - {r['recommendation']}")

    if overlaps or scaffolding_issues:
        report.append("\n### 🟢 LOW PRIORITY - Refinements\n")
        if overlaps:
            report.append(f"\n5. **Review Overlapping Skills** ({len(overlaps)} overlaps)")
            report.append("   - Verify these are intentionally separate or consolidate")
        if scaffolding_issues:
            report.append(f"\n6. **Review Scaffolding** ({len(scaffolding_issues)} skills)")
            report.append("   - Consider if additional prerequisites would help learners")

    # Conclusion
    report.append("\n\n## Conclusion\n")

    if not violations and not circles:
        report.append("\n✅ **Grade K skills meet core dependency requirements**. ")
        report.append("The dependency graph is valid (acyclic with no cross-grade violations).\n")
    else:
        report.append("\n⚠️ **Action required**: Fix critical violations before release.\n")

    if redundant or missing_deps:
        report.append("\nOptional improvements can be made to streamline dependencies and add helpful cross-topic connections.\n")

    report.append("\nThis analysis examined all 36 topics for Grade K coverage and found K-level skills in ")
    report.append(f"{len(by_topic)} topics, creating a foundation for early learners.\n")

    return '\n'.join(report)

if __name__ == '__main__':
    main()
