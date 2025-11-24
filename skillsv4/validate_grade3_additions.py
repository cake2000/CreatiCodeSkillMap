#!/usr/bin/env python3
"""Validate the Grade 3 cross-topic dependency additions"""

import re

def count_dependency_patterns(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Count specific dependency patterns we added
    patterns = {
        "T09.G3.01.01": "Create a new variable with a descriptive name",
        "T08.G3.01": "Use a simple if in a script",
        "T06.G2.03": 'Design a simple "if-then" game rule',
        "T08.G2.03": "Identify which rule applies in a situation",
        "T09.G2.02": "Compare a counter to a target number to trigger an event",
        "T07.G2.01": 'Identify when to use "repeat" vs "do once"',
        "T10.G2.01": "Read and write data to a simple table",
    }
    
    results = {}
    for dep_id, dep_name in patterns.items():
        # Count how many Grade 3 skills depend on this
        pattern = rf'\nID: T\d+\.G3\.[\d.a-z]+\n.*?Dependencies:.*?\* {re.escape(dep_id)}:'
        matches = re.findall(pattern, content, re.DOTALL)
        results[dep_id] = len(matches)
    
    return results

if __name__ == "__main__":
    file_path = "/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md"
    results = count_dependency_patterns(file_path)
    
    print("Grade 3 Cross-Topic Dependency Usage Counts:")
    print("=" * 70)
    
    for dep_id, count in sorted(results.items(), key=lambda x: x[1], reverse=True):
        print(f"{dep_id}: {count} Grade 3 skills")
    
    print("=" * 70)
    print(f"Total: {sum(results.values())} Grade 3 cross-topic dependencies")
