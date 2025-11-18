#!/usr/bin/env python3
import json
import os
from pathlib import Path
from datetime import datetime

def analyze_skill_files():
    base_path = Path('/media/binyu/USB2/dev/CreatiCodeSkillMap')

    # Find all JSON files
    all_json = sorted(base_path.glob('*.json'))

    # Filter for skill-related files
    skill_files = []
    for f in all_json:
        if 'skill' in f.name.lower():
            skill_files.append(f)

    results = []

    for file_path in skill_files:
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)

            # Count skills
            if isinstance(data, list):
                count = len(data)
            elif isinstance(data, dict):
                # Check if it's a dict of skills
                if 'skills' in data:
                    count = len(data['skills'])
                else:
                    count = len(data)
            else:
                count = 'N/A'

            # Get file stats
            stat = os.stat(file_path)
            size_mb = stat.st_size / (1024 * 1024)
            modified = datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M')

            results.append({
                'filename': file_path.name,
                'count': count,
                'size_mb': size_mb,
                'modified': modified,
                'path': str(file_path)
            })

        except Exception as e:
            results.append({
                'filename': file_path.name,
                'count': f'ERROR: {str(e)[:50]}',
                'size_mb': os.stat(file_path).st_size / (1024 * 1024),
                'modified': datetime.fromtimestamp(os.stat(file_path).st_mtime).strftime('%Y-%m-%d %H:%M'),
                'path': str(file_path)
            })

    # Sort by filename
    results.sort(key=lambda x: x['filename'])

    # Print results
    print(f"{'Filename':<60} {'Count':>8} {'Size(MB)':>10} {'Modified':>18}")
    print("=" * 100)

    for r in results:
        count_str = str(r['count']) if isinstance(r['count'], int) else r['count']
        print(f"{r['filename']:<60} {count_str:>8} {r['size_mb']:>10.2f} {r['modified']:>18}")

    print("\n" + "=" * 100)
    print(f"Total skill-related JSON files: {len(results)}")

    # Write to JSON for further processing
    with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/skill_file_analysis.json', 'w') as f:
        json.dump(results, f, indent=2)

    print("\nDetailed analysis saved to: skill_file_analysis.json")

if __name__ == '__main__':
    analyze_skill_files()
