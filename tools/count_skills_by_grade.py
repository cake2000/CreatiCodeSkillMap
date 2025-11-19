import re
from collections import defaultdict, Counter
from pathlib import Path


SKILLS_DIR = Path(__file__).resolve().parents[1] / "skillsv4"

ID_PATTERN = re.compile(r"\b(T\d{2})\.G([A-Z]?[0-8])\.(\d{2})\b")


def normalize_grade(grade_code: str) -> str:
    """
    Normalize grade codes like 'K', 'GK', '1', '2', ..., '8' into a common label.
    We treat:
      GK or K -> 'K'
      0, 1, 2, ..., 8 -> themselves as strings.
    """
    g = grade_code.upper().lstrip("G")
    if g in {"K", "0"}:
        return "K"
    return g


def main() -> None:
    topic_grade_counts: dict[str, Counter] = {}
    global_counts: Counter = Counter()

    for path in sorted(SKILLS_DIR.glob("skills_T*.md")):
        topic_counts: Counter = Counter()
        text = path.read_text(encoding="utf-8", errors="ignore")
        for match in ID_PATTERN.finditer(text):
            topic_id, grade_code, _ = match.groups()
            grade = normalize_grade(grade_code)
            topic_counts[grade] += 1
            global_counts[grade] += 1
        topic_grade_counts[path.name] = topic_counts

    # Print per-topic breakdown
    print("Per-topic skill counts by grade (K–8):")
    print("-------------------------------------")
    grades_order = ["K", "1", "2", "3", "4", "5", "6", "7", "8"]

    for fname, counts in sorted(topic_grade_counts.items()):
        if not counts:
            continue
        line_parts = [fname]
        for g in grades_order:
            n = counts.get(g, 0)
            if n:
                line_parts.append(f"{g}:{n}")
        print("  " + "  ".join(line_parts))

    # Print global totals
    print("\nGlobal skill counts by grade (all topics):")
    print("-----------------------------------------")
    for g in grades_order:
        n = global_counts.get(g, 0)
        print(f"  Grade {g}: {n}")


if __name__ == "__main__":
    main()

