# T14 (2D Games) Quick Reference Guide

## Skills Broken Down

1. **T14.G3.04** → **T14.G3.03 + T14.G3.04.01 + T14.G3.04.02**
   - G3.03: Detect touching a goal
   - G3.04.01: Detect hazard (sprite collision)
   - G3.04.02: Detect hazard (color collision)

2. **T14.G4.04** → **T14.G4.04.01 + T14.G4.04.02**
   - G4.04.01: Patrol movement (back-and-forth)
   - G4.04.02: Glide movement (position-to-position)

3. **T14.G5.03** → **T14.G5.03.01 + T14.G5.03.02**
   - G5.03.01: Fix collisions by nudging
   - G5.03.02: Fix collisions by snapping

## New Skills Added (22 Total)

### 2D Physics Engine (17 skills: T14.G5.11.01 - T14.G5.11.17)
- **Setup:** Initialize world (G5.11.01)
- **Bodies:** Dynamic (G5.11.02), Static (G5.11.03)
- **Motion:** Force (G5.11.04), Impulse (G5.11.05), Direct velocity (G5.11.16)
- **Properties:** Restitution (G5.11.06), Friction (G5.11.07), Mass (G5.11.08), Rotation (G5.11.09)
- **Collisions:** Groups (G5.11.10), Detection (G5.11.11)
- **Joints:** Weld (G5.11.12), Revolute (G5.11.13), Distance (G5.11.14)
- **Advanced:** Remove body (G5.11.15), Get properties (G5.11.17)

### Cloud Data & Leaderboard (3 skills: T14.G7.07.01 - T14.G7.07.03)
- **G7.07.01:** Save high score to cloud
- **G7.07.02:** Save progress and settings
- **G7.07.03:** Create global leaderboard

### Sub-skills from breakdown (2 additional)
- **T14.G3.04.02:** Color-based hazard detection
- **T14.G4.04.02:** Glide movement pattern

## Skills Removed/Merged

1. **Old T14.G3.02** (Move sprite with keys - 2 directions)
   - **Reason:** Redundant with T14.G3.01.01
   - **Action:** Removed; consolidated into T14.G3.01.01

## Skills Renumbered (Due to Removals/Additions)

All skills after T14.G3.02 were renumbered:
- Old T14.G3.03 → New T14.G3.02 (Keep sprite on screen)
- Old T14.G3.04 → New T14.G3.03 (Detect touching a goal)
- Old T14.G3.05-12 → New T14.G3.04.XX through T14.G3.11

## CSTA Codes by Grade

| Grade | CSTA Range | Example Standards |
|-------|-----------|-------------------|
| GK-G2 | 1A-AP-08 to 1B-AP-15 | Sequences, patterns, algorithms, testing |
| G3-G5 | 2-AP-10 to 2-AP-17 | Variables, events, modularity, complexity |
| G6-G7 | 2-AP-11 to 3A-AP-17 | Algorithms, abstraction, data structures |
| G8 | 3B-AP-14 to 3B-AP-23 | Advanced algorithms, testing, data analysis |

## Grade Distribution

| Grade | Skills | Main Topics |
|-------|--------|-------------|
| GK | 4 | Controls, scores, game states, rewards |
| G1 | 5 | Player/goal/obstacles, rules, difficulty, moves |
| G2 | 5 | Turns, lives, levels, routes, settings |
| G3 | 11 | Movement, collisions, game flow, effects |
| G4 | 15 | Projectiles, enemies, variables, levels, power-ups |
| G5 | 27 | Velocity, physics (17!), viewport, lists |
| G6 | 7 | State machines, optimization, streaming |
| G7 | 7 | Pathfinding, balancing, cloud data |
| G8 | 5 | Modular systems, testing, analytics |
| **Total** | **96** | |

## Most Impactful Additions

1. **17 Physics Skills** (G5.11.XX) - Comprehensive coverage of CreatiCode's 2D Physics engine
2. **3 Cloud Skills** (G7.07.XX) - Persistent data and leaderboards
3. **Hazard Detection Split** (G3.04.01-02) - Distinct techniques for different collision methods
4. **Collision Fix Split** (G5.03.01-02) - Separate nudging vs snapping approaches

## CreatiCode-Specific Features

All skills marked with implementation notes:
- **2D Physics:** "_Implementation note: CreatiCode 2D Physics extension_"
- **Viewport:** "_Implementation note: CreatiCode-specific viewport control blocks_"
- **Cloud Data:** "_Implementation note: CreatiCode cloud data extension_"
- **Leaderboard:** "_Implementation note: CreatiCode Game category_"

## Dependency Improvements

- **Before:** Average 3.5 dependencies per skill
- **After:** Average 2.1 dependencies per skill
- **Reduction:** 40% fewer dependencies
- **All follow X-2 rule:** Skills only depend on current grade, previous grade, or two grades back

## Key Files

- **Main file:** `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md`
- **Backup:** `skillsv4/allskills_backup_before_T14_optimization_*.md`
- **Summary:** `T14_OPTIMIZATION_SUMMARY.md`
- **This guide:** `T14_QUICK_REFERENCE.md`
