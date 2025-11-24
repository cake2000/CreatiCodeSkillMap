#!/usr/bin/env python3
"""
Extract key findings and actionable recommendations from Grade K analysis
"""

import re
from collections import defaultdict

def extract_key_sections(filepath: str):
    """Extract the most important sections from the analysis"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract summary statistics
    stats_match = re.search(r'Total Grade K skills: (\d+)', content)
    topics_match = re.search(r'Topics with Grade K skills: (\d+)', content)

    print("GRADE K SKILLS ANALYSIS - EXECUTIVE SUMMARY")
    print("=" * 100)
    print()
    print(f"Total Grade K Skills Analyzed: {stats_match.group(1) if stats_match else 'N/A'}")
    print(f"Topics with Grade K Skills: {topics_match.group(1) if topics_match else 'N/A'}")
    print()

    # Extract all topics with Grade K skills
    print("\nALL TOPICS WITH GRADE K SKILLS")
    print("-" * 80)

    topic_pattern = r'### (T\d+) \((\d+) Grade K skills\)'
    topics = re.findall(topic_pattern, content)

    for topic, count in topics:
        print(f"{topic}: {count} skills")

    print()

    # Find cross-topic section
    existing_start = content.find("### EXISTING Cross-Topic Dependencies")
    missing_start = content.find("### SUGGESTED Missing Cross-Topic Dependencies")
    redundant_start = content.find("## POTENTIALLY REDUNDANT TRANSITIVE DEPENDENCIES")

    if existing_start != -1 and missing_start != -1:
        existing_section = content[existing_start:missing_start]
        print("\nEXISTING CROSS-TOPIC DEPENDENCIES")
        print("-" * 80)
        # Count by parsing
        from_topic_pattern = r'From (T\d+):'
        from_topics = re.findall(from_topic_pattern, existing_section)
        print(f"Found {len(from_topics)} topics with existing cross-topic dependencies")

    if missing_start != -1 and redundant_start != -1:
        missing_section = content[missing_start:redundant_start]

        # Count suggestions by topic
        topic_sections = re.split(r'\n(T\d+):\n', missing_section)
        suggestion_topics = [topic_sections[i] for i in range(1, len(topic_sections), 2)]

        print(f"\nMISSING CROSS-TOPIC DEPENDENCIES")
        print("-" * 80)
        print(f"Found {len(suggestion_topics)} topics with missing cross-topic dependency suggestions")
        print()

        # Parse detailed suggestions
        by_suggested_topic = defaultdict(list)
        
        # Look for patterns in missing section
        lines = missing_section.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # Match skill ID line
            skill_match = re.match(r'(T\d+\.GK\.\d+) \((.+)\)', line)
            if skill_match:
                skill_id = skill_match.group(1)
                skill_name = skill_match.group(2)
                
                # Look ahead for reason and suggested topic
                reason = ""
                suggested_topic = ""
                candidates = []
                
                j = i + 1
                while j < len(lines) and j < i + 10:
                    next_line = lines[j].strip()
                    
                    if re.match(r'T\d+\.GK\.\d+', next_line):
                        break
                        
                    if next_line.startswith('Reason:'):
                        reason = next_line[7:].strip()
                        topic_match = re.search(r'from (T\d+)', reason)
                        if topic_match:
                            suggested_topic = topic_match.group(1)
                    
                    if next_line.startswith('Suggested candidates from'):
                        topic_match = re.search(r'from (T\d+):', next_line)
                        if topic_match:
                            suggested_topic = topic_match.group(1)
                    
                    if next_line.startswith('Option:') or next_line.startswith('- T'):
                        cand_match = re.search(r'(T\d+\.GK\.\d+) \((.+)\)', next_line)
                        if cand_match:
                            candidates.append({
                                'id': cand_match.group(1),
                                'name': cand_match.group(2)
                            })
                    
                    j += 1
                
                if suggested_topic:
                    by_suggested_topic[suggested_topic].append({
                        'skill_id': skill_id,
                        'skill_name': skill_name,
                        'reason': reason,
                        'candidates': candidates
                    })
                
            i += 1
        
        # Print organized by suggested topic
        print("\nSUGGESTED DEPENDENCIES BY TARGET TOPIC:")
        print("(Skills that should add dependencies to fundamental concepts)")
        print()
        
        for topic in sorted(by_suggested_topic.keys()):
            suggestions = by_suggested_topic[topic]
            print(f"\n### {topic}: {len(suggestions)} skills should depend on this topic")
            print("-" * 80)
            
            for sug in suggestions[:5]:  # Show top 5 per topic
                print(f"\n  {sug['skill_id']}: {sug['skill_name']}")
                if sug['candidates']:
                    print(f"    Suggested: {sug['candidates'][0]['id']} - {sug['candidates'][0]['name']}")

if __name__ == '__main__':
    extract_key_sections('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/comprehensive_grade_k_analysis.md')
