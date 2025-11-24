#!/usr/bin/env python3
"""Fix circular dependency in T09.G4.02.01"""

import re

filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix T09.G4.02.01 - remove self-dependency
pattern = r'(ID: T09\.G4\.02\.01\nTopic: T09 – Variables & Expressions\nSkill: Use division \(\/\) in expressions\nDescription:.*?\n\nDependencies:\n)\* T09\.G4\.02\.01: Use division \(\/\) in expressions\n'

replacement = r'\1'

content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed circular dependency in T09.G4.02.01")
