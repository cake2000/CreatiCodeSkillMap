# Grade 1 Cross-Topic Dependency Analysis - Actionable Fixes

**Analysis Date:** 2024-11-24

**Total Grade 1 Skills:** 112

**Total Issues Found:** 9

## Issue Summary

| Severity | Count |
|----------|-------|
| HIGH | 6 |
| MEDIUM | 3 |

## Issues by Type

- **GAME_NEEDS_EVENTS**: 3 issues
- **GAME_NEEDS_VARIABLES**: 3 issues
- **TRANSITIVE_REDUNDANT**: 3 issues

---

## HIGH Priority Issues (6)

### 1. T14.G1.01

**Topic:** T14 – 2D Games

**Skill:** Identify the player, goal, and obstacles

**Description:** In a labeled picture of a game level (maze, platformer, or board game), students point to and name: (1) the controllable character (marked with an arrow or labeled 'YOU'), (2) the goal object or location (flag, door, finish line), and (3) hazards that should be avoided (spikes, enemies, water). _CST...

**Current Dependencies:** T01.GK.03, T14.GK.03

**Issue Type:** GAME_NEEDS_EVENTS

**Reason:** Interactive game needs Events (T6)


### 2. T14.G1.01

**Topic:** T14 – 2D Games

**Skill:** Identify the player, goal, and obstacles

**Description:** In a labeled picture of a game level (maze, platformer, or board game), students point to and name: (1) the controllable character (marked with an arrow or labeled 'YOU'), (2) the goal object or location (flag, door, finish line), and (3) hazards that should be avoided (spikes, enemies, water). _CST...

**Current Dependencies:** T01.GK.03, T14.GK.03

**Issue Type:** GAME_NEEDS_VARIABLES

**Reason:** Game with scoring needs Variables (T9)


### 3. T14.G1.04

**Topic:** T14 – 2D Games

**Skill:** Predict the best next move

**Description:** Given a short rule and a partially played level, students pick which control card (up, down, left, right, jump) keeps the player safe and moving toward the goal. _CSTA: 1B-AP-12.__...

**Current Dependencies:** T14.G1.01, T14.GK.01

**Issue Type:** GAME_NEEDS_EVENTS

**Reason:** Interactive game needs Events (T6)


### 4. T16.G1.01

**Topic:** T16 – User Interfaces

**Skill:** Match interface elements to their purpose (unplugged)

**Description:** Given pictures of interface elements (button, slider, text box, picture) and pictures of purposes (click to start, move to change volume, type your name, look at photo), draw lines connecting each element to its purpose....

**Current Dependencies:** None

**Issue Type:** GAME_NEEDS_EVENTS

**Reason:** Interactive game needs Events (T6)


### 5. T28.G1.03

**Topic:** T28 – Chance & Simulations: K–8 Skill List

**Skill:** Recognize when games use chance

**Description:** Students identify chance elements in simple games by pointing to parts of the game that involve randomness (dice, spinners, shuffled cards, drawing from a bag). They explain in simple words why these elements make the game unpredictable....

**Current Dependencies:** T28.G1.02, T01.G1.10

**Issue Type:** GAME_NEEDS_VARIABLES

**Reason:** Game with scoring needs Variables (T9)


### 6. T29.G1.02

**Topic:** T29 – Text Data & NLP Foundations

**Skill:** Count words in a sentence

**Description:** Given simple sentences written on strips, students count how many words are in each sentence by pointing to each word, distinguishing between letters and words....

**Current Dependencies:** T29.GK.03

**Issue Type:** GAME_NEEDS_VARIABLES

**Reason:** Game with scoring needs Variables (T9)



---

## MEDIUM Priority Issues (3)

### 1. T10.G1.01

**Topic:** T10 – Lists & Tables

**Skill:** Sort items using two rules

**Description:** Students sort 6-8 items into groups using two attributes (e.g., "big red shapes" vs "small blue shapes"), understanding that items can belong to groups based on multiple properties....

**Current Dependencies:** T10.GK.01, T10.GK.04

**Issue Type:** TRANSITIVE_REDUNDANT

**Reason:** T10.GK.01 is direct dep of T10.GK.04 (same topic)

**Redundant Dependency:** `T10.GK.01`

**Keep Instead:** `T10.GK.04`


### 2. T24.G1.02

**Topic:** T24 – XO & Generative AI Practices

**Skill:** Compare AI answers to expected answers

**Description:** Students ask a simple question (e.g., "What color is the sky?") and compare the AI's answer to what they know. They discuss when AI gives good answers and when it might be wrong....

**Current Dependencies:** T24.GK.01, T24.GK.03

**Issue Type:** TRANSITIVE_REDUNDANT

**Reason:** T24.GK.01 is direct dep of T24.GK.03 (same topic)

**Redundant Dependency:** `T24.GK.01`

**Keep Instead:** `T24.GK.03`


### 3. T24.G1.03

**Topic:** T24 – XO & Generative AI Practices

**Skill:** Understand AI needs clear instructions

**Description:** Students see examples of unclear instructions and their confusing results. They practice making instructions clearer by adding details like color, size, or action....

**Current Dependencies:** T24.GK.03, T24.G1.02

**Issue Type:** TRANSITIVE_REDUNDANT

**Reason:** T24.GK.03 is direct dep of T24.G1.02 (same topic)

**Redundant Dependency:** `T24.GK.03`

**Keep Instead:** `T24.G1.02`


