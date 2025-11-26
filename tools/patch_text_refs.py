import re

file_path = 'skillsv5/allskillsv7.md'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replacements
replacements = [
    (r'T21 \(Image', 'T20 (Image'),
    (r'T22 \(Chatbots\)', 'T21 (Chatbots)'),
    (r'T23 \(Perception\)', 'T22 (Perception)'),
    (r'T24 \(Coding Assistants\)', 'T23 (Coding Assistants)'),
    (r'T24 \(XO\)', 'T23 (XO)'),
    # Fix naked T21/T22 refs if clear context?
    # "T21 image generation" -> "T20 image generation"
    (r'T21 image generation', 'T20 image generation'),
    (r'T22 chatbot', 'T21 chatbot'),
    (r'T23 perception', 'T22 perception'),
    (r'T24 XO', 'T23 XO'),
    (r'T24 AI practices', 'T23 AI practices'),
    # "T21-T24" range might still exist if missed
    (r'T21-T24', 'T20-T23'),
]

for old, new in replacements:
    content = re.sub(old, new, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
