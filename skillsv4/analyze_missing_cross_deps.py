#!/usr/bin/env python3
"""
Enhanced Grade 7 Analysis: Missing Cross-Topic Dependencies
Identifies skills that SHOULD have cross-topic dependencies based on content analysis
"""

import json
import re
from collections import defaultdict

def load_skills(filepath):
    """Load skills from JSON file"""
    with open(filepath, 'r') as f:
        data = json.load(f)
        return data.get('skills', [])

def extract_dep_id(dep_string):
    """Extract skill ID from dependency string"""
    if ':' in dep_string:
        return dep_string.split(':')[0].strip()
    return dep_string.strip()

def extract_grade_from_id(skill_id):
    """Extract grade number from skill ID"""
    if '.G' in skill_id:
        parts = skill_id.split('.G')
        if len(parts) > 1:
            grade_str = parts[1].split('.')[0]
            return int(grade_str) if grade_str.isdigit() else None
    return None

def extract_topic_from_id(skill_id):
    """Extract topic number from skill ID"""
    if skill_id.startswith('T') and '.' in skill_id:
        topic_str = skill_id.split('.')[0][1:]
        return int(topic_str) if topic_str.isdigit() else None
    return None

def get_skill_keywords(skill):
    """Extract important keywords from skill name and description"""
    text = f"{skill.get('skill', '')} {skill.get('description', '')}".lower()

    # Remove common words
    stop_words = {'a', 'an', 'the', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by',
                  'from', 'using', 'use', 'that', 'this', 'is', 'are', 'and', 'or'}

    words = re.findall(r'\b\w+\b', text)
    keywords = [w for w in words if len(w) > 3 and w not in stop_words]

    return set(keywords)

def analyze_missing_dependencies(skills):
    """Find skills that should depend on other topics but don't"""

    # Topic domains - skills that commonly need dependencies from these topics
    foundational_topics = {
        6: 'Events & Sequences',
        7: 'Loops',
        8: 'Conditions & Logic',
        9: 'Variables & Expressions',
        10: 'Lists & Tables',
        11: 'Functions & Procedures'
    }

    missing_deps = []

    # Build topic keyword index
    topic_keywords = defaultdict(lambda: defaultdict(set))
    for skill in skills:
        if extract_grade_from_id(skill['id']) == 7:
            topic = extract_topic_from_id(skill['id'])
            keywords = get_skill_keywords(skill)
            topic_keywords[topic][skill['id']] = keywords

    for skill in skills:
        skill_id = skill['id']
        if extract_grade_from_id(skill_id) != 7:
            continue

        skill_topic = extract_topic_from_id(skill_id)
        skill_name = skill.get('skill', '')
        skill_desc = skill.get('description', '')

        # Get current dependencies
        current_deps = set()
        for dep_string in skill.get('dependencies', []):
            dep = extract_dep_id(dep_string)
            dep_topic = extract_topic_from_id(dep)
            if dep_topic:
                current_deps.add(dep_topic)

        # Check for indicators of missing foundational dependencies
        text = f"{skill_name} {skill_desc}".lower()

        missing = []

        # Check for variables/expressions (Topic 9)
        if 9 not in current_deps and skill_topic != 9:
            if any(kw in text for kw in ['variable', 'expression', 'calculate', 'formula', 'math', 'arithmetic']):
                missing.append({
                    'topic': 9,
                    'topic_name': 'Variables & Expressions',
                    'reason': 'Uses variables, expressions, or calculations'
                })

        # Check for conditions/logic (Topic 8)
        if 8 not in current_deps and skill_topic != 8:
            if any(kw in text for kw in ['condition', 'if', 'logic', 'boolean', 'compare', 'check']):
                missing.append({
                    'topic': 8,
                    'topic_name': 'Conditions & Logic',
                    'reason': 'Uses conditional logic or comparisons'
                })

        # Check for loops (Topic 7)
        if 7 not in current_deps and skill_topic != 7:
            if any(kw in text for kw in ['loop', 'repeat', 'iterate', 'each item']):
                missing.append({
                    'topic': 7,
                    'topic_name': 'Loops',
                    'reason': 'Uses iteration or repetition'
                })

        # Check for lists/tables (Topic 10)
        if 10 not in current_deps and skill_topic != 10:
            if any(kw in text for kw in ['list', 'table', 'array', 'data', 'dataset', 'collection']):
                missing.append({
                    'topic': 10,
                    'topic_name': 'Lists & Tables',
                    'reason': 'Works with data structures'
                })

        # Check for events (Topic 6)
        if 6 not in current_deps and skill_topic != 6:
            if any(kw in text for kw in ['event', 'broadcast', 'message', 'trigger', 'signal']):
                missing.append({
                    'topic': 6,
                    'topic_name': 'Events & Sequences',
                    'reason': 'Uses event-driven programming'
                })

        # Check for functions (Topic 11)
        if 11 not in current_deps and skill_topic != 11:
            if any(kw in text for kw in ['function', 'procedure', 'reusable', 'modular']):
                missing.append({
                    'topic': 11,
                    'topic_name': 'Functions & Procedures',
                    'reason': 'Uses functions or modular design'
                })

        if missing:
            missing_deps.append({
                'skill_id': skill_id,
                'skill_name': skill_name,
                'skill_topic': skill_topic,
                'missing_topics': missing
            })

    return missing_deps

def analyze_topic_coherence(skills):
    """Check if topics are well-defined or have overlapping concerns"""

    topic_skills = defaultdict(list)

    for skill in skills:
        if extract_grade_from_id(skill['id']) == 7:
            topic = extract_topic_from_id(skill['id'])
            topic_skills[topic].append({
                'id': skill['id'],
                'name': skill.get('skill', ''),
                'keywords': get_skill_keywords(skill)
            })

    # Find topics with unusual cross-dependencies
    unusual_patterns = []

    for skill in skills:
        skill_id = skill['id']
        if extract_grade_from_id(skill_id) != 7:
            continue

        skill_topic = extract_topic_from_id(skill_id)

        deps = skill.get('dependencies', [])
        dep_topics = set()
        for dep_string in deps:
            dep = extract_dep_id(dep_string)
            dep_topic = extract_topic_from_id(dep)
            if dep_topic and dep_topic != skill_topic:
                dep_topics.add(dep_topic)

        # If a skill has many cross-topic deps, it might be misplaced
        if len(dep_topics) >= 4:
            unusual_patterns.append({
                'skill_id': skill_id,
                'skill_name': skill.get('skill', ''),
                'topic': skill_topic,
                'cross_topic_count': len(dep_topics),
                'dep_topics': sorted(dep_topics)
            })

    return unusual_patterns

def generate_enhanced_report(skills, output_file):
    """Generate enhanced analysis report"""

    print("Analyzing missing cross-topic dependencies...")
    missing_deps = analyze_missing_dependencies(skills)

    print("Analyzing topic coherence...")
    unusual_patterns = analyze_topic_coherence(skills)

    # Group missing deps by topic
    by_missing_topic = defaultdict(list)
    for item in missing_deps:
        for missing in item['missing_topics']:
            by_missing_topic[missing['topic']].append({
                'skill_id': item['skill_id'],
                'skill_name': item['skill_name'],
                'skill_topic': item['skill_topic'],
                'reason': missing['reason']
            })

    with open(output_file, 'w') as f:
        f.write("# Grade 7 Missing Cross-Topic Dependencies Analysis\n\n")

        f.write("## Executive Summary\n\n")
        f.write(f"- **Skills Analyzed**: {len([s for s in skills if extract_grade_from_id(s['id']) == 7])}\n")
        f.write(f"- **Skills with Potentially Missing Dependencies**: {len(missing_deps)}\n")
        f.write(f"- **Skills with Unusual Cross-Topic Patterns**: {len(unusual_patterns)}\n\n")

        # Missing dependencies by target topic
        f.write("## 1. Missing Dependencies by Target Topic\n\n")
        f.write("These are foundational topics that skills should depend on but don't.\n\n")

        topic_names = {
            6: 'Events & Sequences',
            7: 'Loops',
            8: 'Conditions & Logic',
            9: 'Variables & Expressions',
            10: 'Lists & Tables',
            11: 'Functions & Procedures'
        }

        for topic in sorted(by_missing_topic.keys()):
            items = by_missing_topic[topic]
            f.write(f"### Topic {topic}: {topic_names.get(topic, 'Unknown')}\n\n")
            f.write(f"**{len(items)} skills may need dependencies on this topic:**\n\n")

            for item in items[:15]:  # Show top 15
                f.write(f"#### {item['skill_id']}: {item['skill_name']}\n")
                f.write(f"- **Current Topic**: Topic {item['skill_topic']}\n")
                f.write(f"- **Reason**: {item['reason']}\n")
                f.write(f"- **Recommendation**: Review if this skill uses Topic {topic} concepts\n\n")

            if len(items) > 15:
                f.write(f"_...and {len(items) - 15} more skills_\n\n")

        # Unusual patterns
        f.write("## 2. Skills with Unusual Cross-Topic Dependencies\n\n")
        f.write("Skills that depend on 4+ different topics may be too complex or misplaced.\n\n")

        if unusual_patterns:
            for pattern in unusual_patterns:
                f.write(f"### {pattern['skill_id']}: {pattern['skill_name']}\n")
                f.write(f"- **Topic**: Topic {pattern['topic']}\n")
                f.write(f"- **Cross-Topic Dependencies**: {pattern['cross_topic_count']} topics\n")
                f.write(f"- **Depends on Topics**: {', '.join(map(str, pattern['dep_topics']))}\n")
                f.write(f"- **Recommendation**: Consider if this skill should be broken down or moved\n\n")
        else:
            f.write("No unusual patterns detected.\n\n")

        # Recommendations
        f.write("## 3. Specific Recommendations\n\n")

        f.write("### Add Missing Foundational Dependencies\n\n")
        f.write("Many skills use foundational concepts (variables, conditions, loops, lists) ")
        f.write("but don't explicitly depend on them. Consider adding these dependencies:\n\n")

        for topic in sorted(by_missing_topic.keys()):
            count = len(by_missing_topic[topic])
            f.write(f"- **Topic {topic} ({topic_names.get(topic)})**: {count} skills may need this dependency\n")

        f.write("\n### Review Complex Skills\n\n")
        if unusual_patterns:
            f.write(f"Review {len(unusual_patterns)} skills with many cross-topic dependencies. ")
            f.write("Consider breaking them into smaller skills or adding intermediate prerequisites.\n\n")

        f.write("## 4. Priority Actions\n\n")
        f.write("1. **High Priority**: Add missing dependencies to foundational topics (8, 9) for computational thinking skills\n")
        f.write("2. **Medium Priority**: Add missing dependencies to data structure topics (10) for data-heavy skills\n")
        f.write("3. **Low Priority**: Review skills with many cross-topic dependencies for potential restructuring\n")

    print(f"Enhanced report generated: {output_file}")

def main():
    input_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/GRADE7_SKILLS.json'
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/GRADE7_MISSING_CROSS_DEPS.md'

    print(f"Loading skills from {input_file}...")
    skills = load_skills(input_file)
    print(f"Loaded {len(skills)} skills")

    print("\nPerforming enhanced dependency analysis...")
    generate_enhanced_report(skills, output_file)

    print("\nAnalysis complete!")

if __name__ == '__main__':
    main()
