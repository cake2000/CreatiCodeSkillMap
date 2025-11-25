#!/usr/bin/env python3
"""
Generate specific fix recommendations for each Grade 6 skill issue
"""

import json

def load_analysis():
    with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/GRADE6_ANALYSIS_REPORT.json', 'r') as f:
        return json.load(f)

def generate_circular_dependency_fixes():
    """Generate specific fixes for circular dependencies"""
    return [
        {
            "issue_id": "CIRC-001",
            "issue_type": "Circular Dependency",
            "severity": "CRITICAL",
            "cycle": "T07.G6.03 ↔ T07.G6.09",
            "skills_affected": [
                {
                    "id": "T07.G6.03",
                    "name": "Loop-based search in a list"
                },
                {
                    "id": "T07.G6.09",
                    "name": "Use for-each loops to iterate over lists"
                }
            ],
            "fix": {
                "action": "Remove dependency",
                "remove_from": "T07.G6.09",
                "remove_dependency": "T07.G6.03",
                "rationale": "For-each loops are a foundational looping construct. Loop-based search is an application of loops. Students should learn for-each loops BEFORE applying them to search tasks.",
                "natural_order": "T07.G6.09 (for-each) → T07.G6.03 (search application)"
            },
            "validation": "After fix, T07.G6.09 should be reachable from T07.G6.03 but not vice versa"
        },
        {
            "issue_id": "CIRC-002",
            "issue_type": "Circular Dependency",
            "severity": "CRITICAL",
            "cycle": "T07.G6.08 ↔ T07.G6.04",
            "skills_affected": [
                {
                    "id": "T07.G6.04",
                    "name": "Avoid and fix infinite loops"
                },
                {
                    "id": "T07.G6.08",
                    "name": "Use break and continue to control loop flow"
                }
            ],
            "fix": {
                "action": "Remove dependency",
                "remove_from": "T07.G6.08",
                "remove_dependency": "T07.G6.04",
                "rationale": "Students need to understand the problem (infinite loops) before learning the solution (break/continue). Understanding infinite loops doesn't require knowing about break/continue.",
                "natural_order": "T07.G6.04 (understand infinite loops) → T07.G6.08 (use break/continue to fix them)"
            },
            "validation": "After fix, T07.G6.04 should be reachable from T07.G6.08 but not vice versa"
        }
    ]

def generate_missing_dependencies_fixes(analysis):
    """Generate specific dependency additions for skills missing cross-topic deps"""

    fixes = []

    # Mapping of skill patterns to recommended dependencies
    dependency_patterns = {
        'T19': {  # Multiplayer
            'conceptual': {
                'deps': ['T05.G5.01', 'T10.G5.01'],
                'rationale': 'Multiplayer concepts require understanding variables (for state) and events (for networking)'
            },
            'room_management': {
                'deps': ['T05.G5.01', 'T10.G5.01', 'T18.G5.01', 'T08.G5.01'],
                'rationale': 'Room management needs variables, events, UI for room displays, and lists for player management'
            },
            'player_interaction': {
                'deps': ['T05.G5.01', 'T10.G5.01', 'T08.G5.01'],
                'rationale': 'Player interactions need variables for state, events for actions, lists for multiple players'
            },
            'synchronization': {
                'deps': ['T05.G5.01', 'T10.G5.01', 'T08.G5.01'],
                'rationale': 'Synchronization requires variables for shared state, events for updates, lists for data'
            }
        },
        'T22': {  # Game
            'game_mechanics': {
                'deps': ['T05.G5.01', 'T07.G5.01', 'T09.G5.01', 'T10.G5.01', 'T11.G5.01'],
                'rationale': 'Game mechanics need variables (state), conditionals (logic), loops (updates), events (input), motion (movement)'
            }
        },
        'T23': {  # Physics
            'physics_simulation': {
                'deps': ['T11.G5.01', 'T06.G5.01', 'T15.G5.01', 'T05.G5.01', 'T09.G5.01'],
                'rationale': 'Physics needs motion (movement), operators (calculations), sensing (collisions), variables (physics values), loops (updates)'
            }
        },
        'T24': {  # Data
            'data_handling': {
                'deps': ['T08.G5.01', 'T06.G5.01', 'T18.G5.01', 'T05.G5.01'],
                'rationale': 'Data handling needs lists (collections), operators (statistics), UI (visualization), variables (values)'
            }
        },
        'T25': {  # AI
            'ai_concepts': {
                'deps': ['T24.G5.01', 'T08.G5.01', 'T18.G5.01', 'T05.G5.01'],
                'rationale': 'AI needs data concepts, lists (datasets), UI (interaction), variables (model state)'
            }
        },
        'T35': {  # ML
            'ml_concepts': {
                'deps': ['T24.G5.01', 'T25.G5.01', 'T08.G5.01', 'T05.G5.01', 'T06.G5.01'],
                'rationale': 'ML needs data skills, AI foundations, lists (training data), variables, operators (calculations)'
            }
        },
        'T36': {  # Data Science
            'data_science': {
                'deps': ['T24.G5.01', 'T08.G5.01', 'T05.G5.01', 'T06.G5.01', 'T18.G5.01'],
                'rationale': 'Data science needs data handling, lists, variables, operators, UI (visualization)'
            }
        }
    }

    missing_deps = analysis['cross_topic_analysis']['missing_cross_topic_deps']
    all_skills = analysis['all_skills']

    for idx, skill_data in enumerate(missing_deps[:200], 1):  # Process all missing deps
        skill_id = skill_data['skill_id']
        skill_info = all_skills.get(skill_id, {})
        topic = skill_data['topic']

        # Determine pattern based on skill ID and topic
        pattern_key = 'default'
        if topic == 'T19':
            if '.00' in skill_id:
                pattern_key = 'conceptual'
            elif '.01' in skill_id:
                pattern_key = 'room_management'
            elif '.02' in skill_id or '.03' in skill_id:
                pattern_key = 'player_interaction'
            elif '.04' in skill_id or '.05' in skill_id:
                pattern_key = 'synchronization'
            else:
                pattern_key = 'room_management'
        elif topic == 'T22':
            pattern_key = 'game_mechanics'
        elif topic == 'T23':
            pattern_key = 'physics_simulation'
        elif topic == 'T24':
            pattern_key = 'data_handling'
        elif topic == 'T25':
            pattern_key = 'ai_concepts'
        elif topic == 'T35':
            pattern_key = 'ml_concepts'
        elif topic == 'T36':
            pattern_key = 'data_science'

        # Get recommended dependencies
        if topic in dependency_patterns and pattern_key in dependency_patterns[topic]:
            pattern = dependency_patterns[topic][pattern_key]
            deps_to_add = pattern['deps']
            rationale = pattern['rationale']
        else:
            # Default fallback
            deps_to_add = ['T05.G5.01']  # At minimum, add variables
            rationale = 'Basic variables skill as foundation'

        fix = {
            "issue_id": f"MISSING-{idx:03d}",
            "issue_type": "Missing Cross-Topic Dependencies",
            "severity": "MEDIUM-HIGH" if topic in ['T19', 'T22', 'T23', 'T24'] else "MEDIUM",
            "skill_id": skill_id,
            "skill_name": skill_data['skill_name'],
            "topic": topic,
            "current_dependencies": skill_info.get('dependencies', []),
            "missing_from_topics": skill_data['missing_from_topics'],
            "fix": {
                "action": "Add dependencies",
                "add_dependencies": deps_to_add,
                "rationale": rationale,
                "pattern_type": pattern_key
            },
            "validation": f"After fix, {skill_id} should have dependencies from foundational topics: {', '.join(deps_to_add)}"
        }

        fixes.append(fix)

    return fixes

def generate_redundant_dependency_review():
    """Generate review recommendations for redundant dependencies"""

    reviews = [
        {
            "issue_id": "REDUNDANT-REVIEW",
            "issue_type": "Redundant Dependencies Review",
            "severity": "LOW",
            "total_redundant": 191,
            "recommendation": {
                "action": "Manual Review Required",
                "approach": [
                    "Review each redundant dependency case by case",
                    "Evaluate pedagogical value - does it emphasize an important concept?",
                    "Remove if purely transitive with no added meaning",
                    "Keep if it clarifies important prerequisite relationships"
                ],
                "priority_topics": [
                    "T07 (Conditionals) - highest number of redundant deps",
                    "T17 (Functions) - complex dependency chains",
                    "T09 (Loops) - nested prerequisites"
                ]
            },
            "examples": [
                {
                    "skill_id": "T07.G6.03",
                    "redundant_dep": "T08.G4.01",
                    "reachable_via": "T07.G6.09",
                    "recommendation": "REVIEW - May be pedagogically valuable to keep"
                },
                {
                    "skill_id": "T07.G6.08",
                    "redundant_dep": "T07.G5.02",
                    "reachable_via": "T07.G6.03",
                    "recommendation": "CONSIDER REMOVING - Purely transitive"
                }
            ],
            "note": "This is lower priority than fixing circular dependencies and adding missing dependencies"
        }
    ]

    return reviews

def main():
    print("Loading analysis data...")
    analysis = load_analysis()

    print("Generating circular dependency fixes...")
    circular_fixes = generate_circular_dependency_fixes()

    print("Generating missing dependency fixes...")
    missing_fixes = generate_missing_dependencies_fixes(analysis)

    print("Generating redundant dependency review...")
    redundant_review = generate_redundant_dependency_review()

    # Combine all recommendations
    recommendations = {
        "metadata": {
            "generated": "2025-11-24",
            "analysis_version": "1.0",
            "total_issues": len(circular_fixes) + len(missing_fixes) + len(redundant_review)
        },
        "summary": {
            "critical_fixes": len(circular_fixes),
            "missing_dependencies": len(missing_fixes),
            "redundant_reviews": len(redundant_review)
        },
        "fixes": {
            "circular_dependencies": {
                "count": len(circular_fixes),
                "severity": "CRITICAL",
                "priority": 1,
                "fixes": circular_fixes
            },
            "missing_cross_topic_dependencies": {
                "count": len(missing_fixes),
                "severity": "MEDIUM-HIGH",
                "priority": 2,
                "fixes": missing_fixes
            },
            "redundant_dependencies": {
                "count": 191,
                "severity": "LOW",
                "priority": 3,
                "reviews": redundant_review
            }
        },
        "implementation_phases": [
            {
                "phase": 1,
                "name": "Critical Fixes",
                "timeline": "Week 1",
                "items": ["Fix 2 circular dependencies in T07"],
                "issue_ids": ["CIRC-001", "CIRC-002"]
            },
            {
                "phase": 2,
                "name": "High-Priority Dependencies - T19 Multiplayer",
                "timeline": "Week 2",
                "items": ["Add missing dependencies to 62 T19 skills"],
                "issue_ids": [f"MISSING-{i:03d}" for i in range(1, 63)]
            },
            {
                "phase": 3,
                "name": "High-Priority Dependencies - T22/T23",
                "timeline": "Week 3",
                "items": ["Add missing dependencies to T22 (14 skills) and T23 (32 skills)"],
                "issue_ids": []
            },
            {
                "phase": 4,
                "name": "Remaining Dependencies",
                "timeline": "Weeks 4-5",
                "items": ["Complete T24, T25, T35, T36 and other topics"],
                "issue_ids": []
            },
            {
                "phase": 5,
                "name": "Redundant Dependency Review",
                "timeline": "Week 6",
                "items": ["Review and clean up redundant dependencies"],
                "issue_ids": ["REDUNDANT-REVIEW"]
            }
        ]
    }

    # Save recommendations
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/GRADE6_FIX_RECOMMENDATIONS.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(recommendations, f, indent=2, ensure_ascii=False)

    print(f"\n✓ Recommendations saved to {output_file}")
    print(f"\nSummary:")
    print(f"  Critical Fixes (Circular): {len(circular_fixes)}")
    print(f"  Missing Dependencies: {len(missing_fixes)}")
    print(f"  Redundant Reviews: {len(redundant_review)}")
    print(f"\nTotal actionable items: {len(circular_fixes) + len(missing_fixes)}")

    return recommendations

if __name__ == '__main__':
    main()
