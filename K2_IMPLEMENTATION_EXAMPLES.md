# K-2 Picture-Based Skills: Implementation Examples

## Overview
This document provides detailed examples showing how to redesign coding-heavy skills into picture-based, developmentally appropriate activities for K-2 students.

---

## Example 1: Sequencing Algorithm Steps

### Original Concept (Coding-Heavy)
**Topic**: T01 - Everyday Algorithms (Grade 1)
**Original Skill**: "Write code blocks to make character brush teeth"
- Student drags coding blocks: `moveToSink()`, `turnOnWater()`, `pickUpToothbrush()`, etc.
- Requires understanding of code syntax and block-based programming
- Text-heavy instructions
- Abstract representation

### Redesigned Picture-Based Version

#### Complete Specification

```json
{
  "id": "T01.G1.03",
  "title": "Help Leo Get Ready for Bed",
  "short_name": "Sequence 4 bedtime routine steps",
  "topic_id": "T01",
  "grade": "1",
  "skill_type": "picture_based_digital",
  "activity_type": "drag_drop_sequence",
  "description_teacher": "Students practice sequencing by arranging 4 pictures showing a child's bedtime routine in logical order. This builds understanding that algorithms are ordered steps. Students must consider dependencies (can't put on pajamas over clothes, must brush teeth after dinner, etc.).",
  "student_prompt": "Put the pictures in order to help Leo get ready for bed!",
  "student_prompt_audio": {
    "tts_text": "Put the pictures in order to help Leo get ready for bed!",
    "voice_settings": {
      "speed": "normal",
      "voice_type": "child_friendly"
    }
  },
  "interaction_details": {
    "item_count": 4,
    "interaction_mode": "drag_to_slots",
    "visual_theme": "home_family",
    "estimated_time_minutes": 3,
    "randomization": {
      "enabled": true,
      "randomize_positions": true,
      "randomize_items": false
    }
  },
  "auto_grade_rules": {
    "type": "sequence_order",
    "correct_answer": ["eat_dinner", "brush_teeth", "put_on_pajamas", "get_in_bed"],
    "partial_credit": {
      "enabled": false
    },
    "feedback": {
      "correct": {
        "message": "Perfect! You helped Leo get ready for bed!",
        "audio_tts": "Perfect! You helped Leo get ready for bed!",
        "visual_effect": "stars"
      },
      "incorrect": {
        "attempt_1": {
          "message": "Not quite! Think about what Leo does first.",
          "audio_tts": "Not quite! Think about what Leo does first after dinner.",
          "hint_provided": true,
          "hint_text": "What should Leo do right after eating dinner?"
        },
        "attempt_2": {
          "message": "Keep trying! What needs to happen before getting in bed?",
          "audio_tts": "Keep trying! Think about all the things that happen before Leo gets in bed.",
          "hint_provided": true,
          "hint_text": "Leo needs to brush teeth and change clothes. Which comes first?"
        },
        "attempt_3": {
          "message": "Let's see the correct order together!",
          "show_correct_answer": true,
          "audio_tts": "Let's look at the correct order together. First Leo eats dinner, then brushes teeth, then puts on pajamas, and finally gets in bed!"
        }
      }
    },
    "retry_logic": {
      "max_attempts": 3,
      "show_correct_answer": true,
      "reset_on_retry": true
    }
  },
  "accessibility": {
    "audio_support": true,
    "keyboard_navigable": true,
    "screen_reader_compatible": true,
    "touch_target_size": "extra_large",
    "color_blind_safe": true,
    "high_contrast_mode": true,
    "language_support": ["en", "es"]
  },
  "dependencies": [],
  "csta_code": "1A-AP-08",
  "additional_metadata": {
    "tags": ["sequencing", "daily_routines", "bedtime", "algorithms"],
    "learning_objectives": [
      "Arrange steps in logical order",
      "Understand that algorithms require specific sequences",
      "Identify dependencies between steps"
    ],
    "common_misconceptions": [
      "Students may put pajamas before brushing teeth (personal preference vs. common practice)",
      "May not understand that order matters for some steps"
    ],
    "differentiation_notes": {
      "scaffolding": "Use 3 items instead of 4, or show first step already placed",
      "extension": "Ask: 'What else could Leo do before bed?' or use 5-6 steps"
    }
  }
}
```

#### Visual Mockup Description

**Screen Layout:**
```
┌─────────────────────────────────────────────────────────┐
│  [Speaker Icon] Put the pictures in order to help      │
│                 Leo get ready for bed!                  │
├─────────────────────────────────────────────────────────┤
│                                                         │
│   Numbered Slots (Target Area):                        │
│   ┌───────┐  ┌───────┐  ┌───────┐  ┌───────┐         │
│   │   1   │  │   2   │  │   3   │  │   4   │         │
│   │ [DROP]│  │ [DROP]│  │ [DROP]│  │ [DROP]│         │
│   └───────┘  └───────┘  └───────┘  └───────┘         │
│                                                         │
│   Draggable Items (Source Area - shuffled):           │
│   ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐   │
│   │  [img]  │ │  [img]  │ │  [img]  │ │  [img]  │   │
│   │ Pajamas │ │  Brush  │ │ Dinner  │ │   Bed   │   │
│   └─────────┘ └─────────┘ └─────────┘ └─────────┘   │
│                                                         │
│               [Check My Answer] Button                  │
└─────────────────────────────────────────────────────────┘
```

**Images:**
1. **Dinner**: Leo sitting at table eating dinner (fork, plate with food, smile)
2. **Brush teeth**: Leo at sink brushing teeth (toothbrush, toothpaste, mirror)
3. **Pajamas**: Leo putting on or wearing pajamas (PJs with stars, happy)
4. **Bed**: Leo in bed under covers (pillow, blanket, teddy bear)

**Visual Style:**
- Cartoon illustration style
- Diverse child character (gender-neutral name "Leo", medium skin tone)
- Bright, warm colors
- Clear, uncluttered backgrounds (bathroom, bedroom, dining room)
- 150x150px images minimum
- High contrast borders on items and slots

#### Student Experience Walkthrough

**Step 1: Introduction**
- Screen loads with audio automatically playing: "Put the pictures in order to help Leo get ready for bed!"
- Student sees 4 numbered empty slots at top
- Student sees 4 shuffled picture cards below (in random order each time)

**Step 2: Interaction**
- Student taps/clicks on first picture (e.g., "Brush teeth")
- Picture highlights (blue border glow)
- Student drags it toward slot #1
- Slot #1 highlights as picture approaches (green outline)
- Student drops picture into slot #1
- Picture snaps into place with satisfying click sound
- Student repeats for remaining 3 pictures

**Step 3: Submission**
- Student clicks "Check My Answer" button
- Button glows, brief pause (1 second)

**Scenario A - Correct Answer:**
- ✅ All 4 slots light up green with checkmarks
- ⭐ Stars and confetti animation
- 🎵 Happy "success" chime plays
- 💬 Text appears: "Perfect! You helped Leo get ready for bed!"
- 🔊 Audio narration: "Perfect! You helped Leo get ready for bed!"
- ➡️ "Next Skill" button appears

**Scenario B - Incorrect Answer (1st attempt):**
- ❌ Slots shake gently (not harsh)
- 💬 Encouraging message appears: "Not quite! Think about what Leo does first."
- 🔊 Audio: "Not quite! Think about what Leo does first after dinner."
- 💡 Hint appears: "What should Leo do right after eating dinner?"
- 🔄 "Try Again" button appears
- Student can rearrange items and resubmit

**Scenario C - Incorrect Answer (2nd attempt):**
- ❌ Gentle shake again
- 💬 "Keep trying! What needs to happen before getting in bed?"
- 🔊 Audio with more specific hint
- 💡 More detailed hint shown
- Student gets one more attempt

**Scenario D - Incorrect Answer (3rd attempt):**
- 📺 Animation shows correct sequence:
  - Items slide into correct positions one by one
  - Each step is narrated: "First Leo eats dinner, then brushes teeth..."
- ✅ Green checkmarks appear on each in sequence
- 💬 "Let's see the correct order together!"
- ➡️ "Try a New One" button to get fresh randomized version

#### Teacher Notes

**Learning Objective**:
Students will understand that algorithms are precise sequences of steps where order matters.

**What to Look For:**
- Can students identify the logical first step (dinner)?
- Do they understand dependencies (must brush teeth before bed)?
- Are they using trial-and-error or logical thinking?

**Common Student Approaches:**
- **Random guessing**: Place items randomly, check, adjust based on feedback
- **Personal experience**: Use their own bedtime routine (may vary by family)
- **Partial logic**: Get first/last correct but struggle with middle steps
- **Pattern recognition**: After feedback, identify which specific steps are wrong

**Differentiation:**
- **Struggling students**:
  - Reduce to 3 steps
  - Show first step already placed ("Leo eats dinner first, now what?")
  - Provide visual clues (numbers on images, timeline graphic)
- **Advanced students**:
  - Increase to 5-6 steps (add "take bath", "read story")
  - Mix in a distractor image that doesn't belong
  - Ask them to explain WHY order matters for each step

**Extensions:**
- Have students draw/photograph their own bedtime routine
- Create a class book with everyone's routines
- Discuss: "Does everyone do these in the same order? Why or why not?"

---

## Example 2: Sorting by Categories (Input/Output)

### Original Concept (Coding-Heavy)
**Topic**: T30 - Hardware (Grade 2)
**Original Skill**: "Identify input and output devices, write code to use them"
- Student writes code: `input = keyboard.readKey()`
- Requires understanding of programming concepts
- Abstract terminology (input/output/device)
- Text-based interface

### Redesigned Picture-Based Version

#### Complete Specification

```json
{
  "id": "T30.G2.02",
  "title": "Computer Helpers: Inputs and Outputs",
  "short_name": "Sort devices as inputs or outputs",
  "topic_id": "T30",
  "grade": "2",
  "skill_type": "picture_based_digital",
  "activity_type": "sort_categories",
  "description_teacher": "Students sort 8 computing devices into two categories: Input (devices that send information TO the computer) and Output (devices that get information FROM the computer). This builds foundational understanding of computer systems and information flow.",
  "student_prompt": "Sort the computer parts! Inputs send information to the computer. Outputs get information from the computer.",
  "student_prompt_audio": {
    "tts_text": "Sort the computer parts! Inputs send information TO the computer. Outputs get information FROM the computer. Drag each picture to the correct box!",
    "voice_settings": {
      "speed": "normal",
      "voice_type": "child_friendly"
    }
  },
  "interaction_details": {
    "item_count": 8,
    "interaction_mode": "drag_to_containers",
    "visual_theme": "technology_devices",
    "estimated_time_minutes": 4,
    "randomization": {
      "enabled": true,
      "randomize_positions": true,
      "randomize_items": false
    }
  },
  "auto_grade_rules": {
    "type": "category_match",
    "correct_answer": {
      "keyboard": "input",
      "mouse": "input",
      "microphone": "input",
      "camera": "input",
      "monitor": "output",
      "speakers": "output",
      "printer": "output",
      "headphones": "output"
    },
    "partial_credit": {
      "enabled": true,
      "rules": [
        {
          "condition": "75% correct (6 of 8)",
          "credit_percentage": 70,
          "feedback": "Almost perfect! Just check a couple more."
        }
      ]
    },
    "feedback": {
      "correct": {
        "message": "Excellent! You sorted all the inputs and outputs!",
        "audio_tts": "Excellent! You sorted all the inputs and outputs correctly!",
        "visual_effect": "checkmarks"
      },
      "incorrect": {
        "attempt_1": {
          "message": "Some are in the wrong group. Check each one carefully!",
          "audio_tts": "Some are in the wrong group. Think about whether each device sends information TO the computer or gets information FROM the computer.",
          "hint_provided": true,
          "hint_text": "Does a keyboard send information to the computer, or get information from it?"
        },
        "attempt_2": {
          "message": "Keep going! Remember: inputs send TO, outputs get FROM.",
          "audio_tts": "Keep going! Remember: input devices send information TO the computer. Output devices get information FROM the computer.",
          "hint_provided": true,
          "hint_text": "Think about what you do with each device. Do you use it to tell the computer something, or does it show you something?"
        },
        "attempt_3": {
          "message": "Let's learn about inputs and outputs together!",
          "show_correct_answer": true,
          "audio_tts": "Let's learn together! Watch where each device goes and why."
        }
      }
    },
    "retry_logic": {
      "max_attempts": 3,
      "show_correct_answer": true,
      "reset_on_retry": false
    }
  },
  "accessibility": {
    "audio_support": true,
    "keyboard_navigable": true,
    "screen_reader_compatible": true,
    "touch_target_size": "large",
    "color_blind_safe": true,
    "high_contrast_mode": true,
    "language_support": ["en", "es"]
  },
  "dependencies": ["T30.G2.01"],
  "csta_code": "1A-CS-01",
  "additional_metadata": {
    "tags": ["hardware", "input_output", "devices", "computers", "sorting"],
    "learning_objectives": [
      "Identify common input and output devices",
      "Understand that inputs send information TO computers",
      "Understand that outputs send information FROM computers",
      "Classify devices by their function"
    ],
    "common_misconceptions": [
      "Thinking monitors are inputs because you look at them (they output information)",
      "Thinking microphones are outputs because sound comes out of speakers",
      "Confusion with devices like touchscreens that are both input and output"
    ],
    "differentiation_notes": {
      "scaffolding": "Use 6 items (3 inputs, 3 outputs) instead of 8; show one example in each category already sorted",
      "extension": "Add 'both' category for touchscreen devices; ask students to name other inputs/outputs not shown"
    },
    "home_school_notes": "Look around your home together! Can you find inputs and outputs? What about the TV remote (input) or the TV screen (output)?"
  }
}
```

#### Visual Mockup Description

**Screen Layout:**
```
┌──────────────────────────────────────────────────────────────┐
│  [Speaker] Sort the computer parts!                          │
│  Inputs send TO the computer. Outputs get FROM the computer. │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────────────┐     ┌──────────────────────┐     │
│  │   INPUT DEVICES      │     │   OUTPUT DEVICES     │     │
│  │   ─────────────      │     │   ──────────────     │     │
│  │   [Sends TO          │     │   [Gets FROM         │     │
│  │    Computer Icon]    │     │    Computer Icon]    │     │
│  │                      │     │                      │     │
│  │  [Drop zone for      │     │  [Drop zone for      │     │
│  │   input devices]     │     │   output devices]    │     │
│  │                      │     │                      │     │
│  └──────────────────────┘     └──────────────────────┘     │
│                                                              │
│  Devices to Sort (shuffled in center):                     │
│  ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐ │
│  │[KB]│ │[MS]│ │[MN]│ │[SP]│ │[PR]│ │[CM]│ │[MC]│ │[HP]│ │
│  └────┘ └────┘ └────┘ └────┘ └────┘ └────┘ └────┘ └────┘ │
│                                                              │
│                   [Check My Answer]                          │
└──────────────────────────────────────────────────────────────┘
```

**Container Visual Design:**
- **INPUT container**: Blue background, icon showing arrow pointing TO computer
- **OUTPUT container**: Green background, icon showing arrow pointing FROM computer
- Containers grow to accommodate items dragged into them
- Show count: "3 items" updates as items added

**Device Images** (120x120px):
1. **Keyboard** - with labeled keys, modern style
2. **Mouse** - wireless mouse, recognizable shape
3. **Microphone** - desktop or handheld mic, clear icon
4. **Camera** - webcam style, lens visible
5. **Monitor** - computer screen showing colorful image
6. **Speakers** - desktop speakers, sound waves icon
7. **Printer** - with paper coming out
8. **Headphones** - over-ear style, recognizable shape

**Visual Style:**
- Consistent icon style across all devices
- Clear, simple representations
- Labels under each image (e.g., "Keyboard", "Monitor")
- High contrast colors
- Friendly, not intimidating

#### Student Experience Walkthrough

**Step 1: Introduction**
- Audio plays: "Sort the computer parts! Inputs send information TO the computer. Outputs get information FROM the computer. Drag each picture to the correct box!"
- Student sees two large, clearly labeled containers
- Student sees 8 device pictures in center (randomized order)

**Step 2: Exploration**
- Student can tap/click any device to hear its name: "Keyboard", "Monitor", etc.
- Student can tap containers to re-hear definitions
- No pressure, no timer

**Step 3: Sorting**
- Student drags keyboard toward INPUT container
- Container highlights (blue glow) as item approaches
- Student drops keyboard
- Keyboard slides into container with satisfying "plop" sound
- Label appears: "Keyboard" inside INPUT container
- Container shows "1 item"
- Student continues sorting all 8 devices

**Step 4: Checking Work**
- Student reviews their sorting
- Can drag items between containers if they change their mind
- Clicks "Check My Answer"

**Scenario A - All Correct:**
- ✅ Both containers light up green
- ⭐ Checkmarks appear over each correctly sorted item
- 🎵 Success sound
- 💬 "Excellent! You sorted all the inputs and outputs!"
- 🔊 Audio narration
- ➡️ "Next Skill" button

**Scenario B - Partially Correct (6/8 correct):**
- ✅ Correctly sorted items get green checkmarks
- ❌ Incorrect items shake gently in their current container
- 💬 "Almost perfect! Just check a couple more."
- 🔊 Audio: "You got most of them! Think again about the ones that are shaking."
- 💡 Hint: "Does a keyboard send information TO the computer, or get information FROM it?"
- Student can move just the incorrect items and recheck

**Scenario C - Several Incorrect (3rd attempt):**
- 📺 Animation shows correct sorting:
  - Incorrect items slide to correct containers one by one
  - Each is narrated: "The keyboard is an INPUT because you use it to type information TO the computer..."
- ✅ All items end in correct containers with explanations
- 💬 "Let's learn about inputs and outputs together!"
- ➡️ "Try a New One" for fresh practice

#### Teacher Notes

**Learning Objective:**
Students will classify devices as inputs (sending information TO computer) or outputs (receiving information FROM computer).

**Pre-Lesson Discussion:**
- "When you type on a keyboard, where does that information go?" (TO the computer)
- "When you see a picture on the screen, where did it come from?" (FROM the computer)
- Act it out: Student pretends to be computer, teacher uses "input devices" to send info

**What to Look For:**
- Do students understand directional flow (TO vs. FROM)?
- Are they thinking about device function?
- Do they use context clues (speaking into mic = input)?

**Common Student Errors:**
1. **Microphone sorted as output**: Students confuse it with speakers because both involve sound
   - **Teacher support**: "Do you talk INTO the mic (sending to computer) or does the mic talk to YOU?"

2. **Monitor sorted as input**: Students look at it so think they're "inputting" their vision
   - **Teacher support**: "Does information go FROM your eyes TO the computer, or FROM the computer TO your eyes?"

3. **Printer confusion**: May think it's input because you put paper in
   - **Teacher support**: "Does the printer send information TO the computer, or does the computer send information TO the printer?"

**Differentiation:**
- **Struggling**: Start with 4 devices (2 obvious inputs like keyboard/mouse, 2 obvious outputs like monitor/speakers)
- **Advanced**: Add "BOTH" category and include touchscreen, microphone-headset combo

**Real-World Connections:**
- Game controllers (input)
- Smart speakers like Alexa (both!)
- TV (output), TV remote (input)

**Assessment:**
Look for students who can:
- Explain WHY a device is input or output (not just memorize)
- Apply concept to new devices not in the activity
- Use correct directional language (TO, FROM)

---

## Example 3: Pattern Recognition

### Original Concept (Coding-Heavy)
**Topic**: T04 - Patterns (Kindergarten)
**Original Skill**: "Create a repeating pattern using code blocks"
- Student writes: `repeat 3 times: { circle, square }`
- Requires understanding loops and block syntax
- Abstract representation

### Redesigned Picture-Based Version

#### Complete Specification

```json
{
  "id": "T04.GK.02",
  "title": "What Comes Next? Color Patterns",
  "short_name": "Complete simple AB color patterns",
  "topic_id": "T04",
  "grade": "K",
  "skill_type": "picture_based_digital",
  "activity_type": "pattern_complete",
  "description_teacher": "Students identify and complete simple AB color patterns by selecting the next item in the sequence. This foundational pattern recognition skill prepares students for understanding repetition in algorithms.",
  "student_prompt": "What comes next in the pattern?",
  "student_prompt_audio": {
    "tts_text": "What comes next in the pattern? Look at the colors and find what should go in the empty box!",
    "voice_settings": {
      "speed": "slow",
      "voice_type": "child_friendly"
    }
  },
  "interaction_details": {
    "item_count": 6,
    "interaction_mode": "click_items",
    "visual_theme": "colors_shapes",
    "estimated_time_minutes": 2,
    "randomization": {
      "enabled": true,
      "randomize_positions": false,
      "randomize_items": true,
      "item_pool_size": 12
    },
    "difficulty_parameters": {
      "distractor_count": 2,
      "similarity_level": "low"
    }
  },
  "auto_grade_rules": {
    "type": "pattern_completion",
    "correct_answer": "blue_circle",
    "partial_credit": {
      "enabled": false
    },
    "feedback": {
      "correct": {
        "message": "Yes! Blue circle comes next!",
        "audio_tts": "Yes! The blue circle comes next! You found the pattern!",
        "visual_effect": "pattern_animates"
      },
      "incorrect": {
        "attempt_1": {
          "message": "Not quite! Look at the pattern again.",
          "audio_tts": "Not quite! Look at the colors. What pattern do you see? Red, blue, red, blue...",
          "hint_provided": true,
          "hint_text": "Say the colors out loud: Red, blue, red, blue, red... what comes next?"
        },
        "attempt_2": {
          "message": "Try again! Watch the pattern.",
          "audio_tts": "Try again! Let's say it together: Red, blue, red, blue, red, and then...?",
          "hint_provided": true,
          "hint_text": "The pattern goes: red, blue, red, blue. It repeats!",
          "visual_hint": true,
          "visual_hint_type": "animate_pattern_sequence"
        },
        "attempt_3": {
          "message": "The blue circle comes next!",
          "show_correct_answer": true,
          "audio_tts": "The blue circle comes next! See? Red, blue, red, blue, red, blue! The pattern repeats!",
          "visual_hint_type": "show_and_animate_answer"
        }
      }
    },
    "retry_logic": {
      "max_attempts": 3,
      "show_correct_answer": true,
      "reset_on_retry": false
    }
  },
  "accessibility": {
    "audio_support": true,
    "keyboard_navigable": true,
    "screen_reader_compatible": true,
    "touch_target_size": "extra_large",
    "color_blind_safe": false,
    "high_contrast_mode": true,
    "language_support": ["en", "es"],
    "note": "Color-blind safety achieved through shape + color combinations"
  },
  "dependencies": [],
  "csta_code": "1A-AP-08",
  "additional_metadata": {
    "tags": ["patterns", "colors", "sequencing", "prediction", "repetition"],
    "learning_objectives": [
      "Identify simple repeating patterns",
      "Predict what comes next in a sequence",
      "Understand that patterns repeat"
    ],
    "common_misconceptions": [
      "Choosing based on preference (\"I like red\") rather than pattern logic",
      "Not seeing the repetition (treating each item as random)",
      "Focusing on shape instead of color (if both vary)"
    ],
    "differentiation_notes": {
      "scaffolding": "Use physical manipulatives first; animate the pattern before asking; use only 4 items instead of 6",
      "extension": "Use ABB or AAB patterns; use 2 attributes (color AND shape); create longer patterns"
    },
    "home_school_notes": "Practice finding patterns everywhere: clothing stripes, food on plate, toys in a row!"
  }
}
```

#### Visual Mockup Description

**Screen Layout:**
```
┌─────────────────────────────────────────────────────┐
│  [Speaker] What comes next in the pattern?         │
├─────────────────────────────────────────────────────┤
│                                                     │
│  The Pattern:                                       │
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ │
│  │ ●RED│ │●BLUE│ │ ●RED│ │●BLUE│ │ ●RED│ │  ?  │ │
│  └─────┘ └─────┘ └─────┘ └─────┘ └─────┘ └─────┘ │
│                                    [Question mark] │
│                                                     │
│  Click the answer:                                 │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐        │
│  │          │  │          │  │          │        │
│  │  ● BLUE  │  │  ● RED   │  │ ● GREEN  │        │
│  │  (large) │  │  (large) │  │  (large) │        │
│  └──────────┘  └──────────┘  └──────────┘        │
│   [Option 1]    [Option 2]    [Option 3]         │
│                                                     │
│              [Submit Answer]                        │
└─────────────────────────────────────────────────────┘
```

**Visual Elements:**
- **Pattern row**: 5 filled circles + 1 empty box with question mark
- **Circles**: Large (80px diameter), solid color, simple style
- **Empty box**: Dashed border, question mark, same size as circles
- **Answer choices**: 3 large circles (150px), clearly spaced
- **Colors**: Bright, saturated primary colors
- **Animation** (on load): Pattern circles appear one by one, left to right, with "pop" sound

**Pattern Variations** (randomized from pool):
- Version A: Red, Blue, Red, Blue, Red, ? (Blue)
- Version B: Yellow, Green, Yellow, Green, Yellow, ? (Green)
- Version C: Blue, Red, Blue, Red, Blue, ? (Red)
- Version D: Green, Yellow, Green, Yellow, Green, ? (Yellow)

**Distractors:**
- Always include correct answer + 1 color from pattern + 1 color not in pattern
- Randomize position of correct answer among choices

#### Student Experience Walkthrough

**Step 1: Pattern Introduction**
- Screen loads with animation
- Circles appear one by one: "Pop! Pop! Pop! Pop! Pop!"
- Audio: "What comes next in the pattern? Look at the colors and find what should go in the empty box!"
- Student can tap speaker icon to replay

**Step 2: Pattern Observation**
- Student looks at: Red, Blue, Red, Blue, Red, ?
- Student might say pattern out loud (encouraged)
- Pattern can be animated again: circles pulse in sequence showing repetition

**Step 3: Making a Choice**
- Student sees 3 large circle options:
  - Blue circle (correct)
  - Red circle (distractor from pattern)
  - Green circle (distractor not in pattern)
- Student taps blue circle
- Blue circle highlights (yellow border glow)
- Student taps "Submit Answer" (or auto-submits if designed that way)

**Step 4: Feedback - Correct**
- ✅ Selected blue circle jumps into the empty box
- 🎬 Full pattern animates: circles light up in sequence showing repetition
  - "Red, blue, red, blue, red, blue!" with each lighting up
- ⭐ Stars burst from pattern
- 🎵 Happy jingle plays
- 💬 "Yes! Blue circle comes next!"
- 🔊 Audio: "Yes! The blue circle comes next! You found the pattern!"
- 👍 "You did it!" celebration image (smiling child, thumbs up)
- ➡️ "Next Pattern" button

**Step 5: Feedback - Incorrect (choosing red)**
- ❌ Selected red circle shakes "no"
- Pattern stays incomplete
- 💬 "Not quite! Look at the pattern again."
- 🔊 Audio: "Not quite! Look at the colors. What pattern do you see? Red, blue, red, blue..."
- 💡 Hint appears: "Say the colors out loud: Red, blue, red, blue, red... what comes next?"
- 🎬 Pattern animates: circles pulse in order (red, blue, red, blue, red) with audio narration
- Student choice is cleared; can choose again
- "Try Again" button

**Step 6: If Still Incorrect (2nd attempt)**
- 🎬 More explicit animation:
  - First two circles (red, blue) bracket together: "This is the pattern!"
  - Next two circles (red, blue) bracket: "It repeats!"
  - Fifth circle (red) pulses: "Red again..."
  - Empty box pulses: "So what comes next?"
- 💡 Stronger hint: "The pattern goes: red, blue, red, blue. It repeats!"
- Student tries again

**Step 7: If Still Incorrect (3rd attempt)**
- 🎬 Correct answer (blue circle) slides into empty box automatically
- ✅ Full pattern shown: Red, Blue, Red, Blue, Red, Blue
- Pattern animates with bracketing showing repetition
- 💬 "The blue circle comes next! See? Red, blue, red, blue, red, blue! The pattern repeats!"
- 🔊 Full audio explanation
- ➡️ "Try a New Pattern" button (generates new random pattern)

#### Teacher Notes

**Learning Objective:**
Students will identify repeating elements in a pattern and predict what comes next.

**Pre-Activity:**
- Practice patterns with physical objects: blocks, beads, toys
- Have students create their own patterns
- Say patterns out loud together
- Clap patterns (clap, stomp, clap, stomp...)

**What to Look For:**
- Can student identify the repeating unit (red-blue)?
- Do they understand "repeats" means it happens again?
- Are they using logic or guessing?
- Can they verbalize the pattern?

**Common Student Responses:**

1. **Random Guessing**: Clicks any color, switches quickly
   - **Support**: "Stop and look. Tell me what colors you see. Say them out loud."

2. **Personal Preference**: "I like green!" (chooses green even though not in pattern)
   - **Support**: "Green is nice! But what color is in the pattern? Look only at these colors."

3. **Partial Understanding**: Gets first unit (red-blue) but doesn't continue pattern
   - **Support**: "You're right, it goes red, blue! And then what? It starts again!"

4. **Correct but Can't Explain**: Chooses correctly but says "I don't know why"
   - **Extend**: "You got it! Can you show me where the pattern repeats?"

**Scaffolding:**
- Use only 4 items (red, blue, red, ?)
- Physically bracket the repeating unit before asking
- Use familiar patterns (apple, orange, apple, orange from snack time)
- Provide physical manipulatives alongside digital

**Extension:**
- ABB patterns (red, blue, blue, red, blue, blue, red, ?, ?)
- AAB patterns (red, red, blue, red, red, blue, red, ?, ?)
- Two-attribute patterns (big red, small blue, big red, small blue...)
- Student creates their own pattern for a friend

**Assessment:**
Student demonstrates understanding when they can:
- Choose correct next item consistently
- Explain WHY that item comes next ("Because the pattern goes red, blue, and it repeats!")
- Create their own simple AB pattern
- Find patterns in the world around them

**Cross-Curricular Connections:**
- Math: Number patterns, counting by 2s
- Music: Rhythm patterns, verse-chorus repetition
- Art: Patterns in design, symmetry
- Nature: Stripes on animals, leaf arrangements

---

## Example 4: Sorting with Binary Classification

### Original Concept (Coding-Heavy)
**Topic**: T32 - Cybersecurity (Grade 1)
**Original Skill**: "Write conditional code to identify safe/unsafe online behaviors"
- Student writes: `if (behavior.isSafe()) { allowIt(); }`
- Requires understanding conditionals and boolean logic
- Abstract syntax

### Redesigned Picture-Based Version

#### Complete Specification

```json
{
  "id": "T32.G1.01",
  "title": "Is It Safe Online? Yes or No",
  "short_name": "Identify safe vs. unsafe online behaviors",
  "topic_id": "T32",
  "grade": "1",
  "skill_type": "picture_based_digital",
  "activity_type": "yes_no_sort",
  "description_teacher": "Students view 6 pictures showing different online behaviors and sort them into Safe (appropriate) or Unsafe (not appropriate). This introduces basic digital citizenship concepts in a concrete, visual way appropriate for Grade 1.",
  "student_prompt": "Is it safe to do this online? Drag each picture to Yes (safe) or No (not safe).",
  "student_prompt_audio": {
    "tts_text": "Is it safe to do this online? Look at each picture. Drag it to Yes if it's safe, or No if it's not safe.",
    "voice_settings": {
      "speed": "normal",
      "voice_type": "child_friendly"
    }
  },
  "interaction_details": {
    "item_count": 6,
    "interaction_mode": "drag_to_containers",
    "visual_theme": "technology_devices",
    "estimated_time_minutes": 4,
    "randomization": {
      "enabled": true,
      "randomize_positions": true,
      "randomize_items": true,
      "item_pool_size": 12
    }
  },
  "auto_grade_rules": {
    "type": "binary_classification",
    "correct_answer": {
      "share_full_name": "no",
      "ask_adult_for_help": "yes",
      "share_address": "no",
      "use_nice_words": "yes",
      "click_unknown_links": "no",
      "tell_teacher_problem": "yes"
    },
    "partial_credit": {
      "enabled": false
    },
    "feedback": {
      "correct": {
        "message": "Great job! You know how to be safe online!",
        "audio_tts": "Great job! You know how to be safe online!",
        "visual_effect": "checkmarks"
      },
      "incorrect": {
        "attempt_1": {
          "message": "Some need to be moved. Think about staying safe!",
          "audio_tts": "Some pictures are in the wrong group. Think carefully about which things keep you safe online.",
          "hint_provided": true,
          "hint_text": "Should you share your address online?"
        },
        "attempt_2": {
          "message": "Keep trying! Remember to ask an adult if you're not sure.",
          "audio_tts": "Keep trying! Remember, asking an adult for help is always safe!",
          "hint_provided": true,
          "hint_text": "Asking for help is safe. Sharing personal information is not safe."
        },
        "attempt_3": {
          "message": "Let's learn about being safe online!",
          "show_correct_answer": true,
          "audio_tts": "Let's learn together! I'll show you which things are safe and which are not safe online."
        }
      }
    },
    "retry_logic": {
      "max_attempts": 3,
      "show_correct_answer": true,
      "reset_on_retry": false
    }
  },
  "accessibility": {
    "audio_support": true,
    "keyboard_navigable": true,
    "screen_reader_compatible": true,
    "touch_target_size": "large",
    "color_blind_safe": true,
    "high_contrast_mode": true,
    "language_support": ["en", "es"]
  },
  "dependencies": [],
  "csta_code": "1A-IC-18",
  "additional_metadata": {
    "tags": ["digital_citizenship", "safety", "online_behavior", "cybersecurity", "privacy"],
    "learning_objectives": [
      "Identify safe online behaviors",
      "Recognize that personal information should be kept private",
      "Understand the importance of asking adults for help online",
      "Practice making safe choices in digital environments"
    ],
    "common_misconceptions": [
      "Thinking it's OK to share first name only (still personal info in this context)",
      "Not understanding what 'personal information' means",
      "Assuming all websites/links are safe",
      "Thinking they should solve all problems themselves without asking adults"
    ],
    "differentiation_notes": {
      "scaffolding": "Use 4 items (2 safe, 2 unsafe) with very obvious examples; discuss each scenario before sorting",
      "extension": "Add nuance: 'Safe with parent permission' category; discuss WHY each is safe/unsafe"
    },
    "home_school_notes": "Practice these rules at home! Make a family plan for safe internet use together."
  }
}
```

#### Visual Mockup Description

**Screen Layout:**
```
┌─────────────────────────────────────────────────────────┐
│  [Speaker] Is it safe to do this online?               │
│  Drag each picture to Yes (safe) or No (not safe).     │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌─────────────────────┐   ┌─────────────────────┐   │
│  │    YES - SAFE ✓     │   │   NO - NOT SAFE ✗   │   │
│  │    ───────────      │   │   ──────────────    │   │
│  │  [Green background] │   │  [Red background]   │   │
│  │  [Smiling face]     │   │  [Stop hand symbol] │   │
│  │                     │   │                     │   │
│  │  [Drop zone]        │   │  [Drop zone]        │   │
│  │                     │   │                     │   │
│  └─────────────────────┘   └─────────────────────┘   │
│                                                         │
│  Pictures to Sort:                                     │
│  ┌────────┐ ┌────────┐ ┌────────┐                    │
│  │[Image1]│ │[Image2]│ │[Image3]│                    │
│  │ Label  │ │ Label  │ │ Label  │                    │
│  └────────┘ └────────┘ └────────┘                    │
│  ┌────────┐ ┌────────┐ ┌────────┐                    │
│  │[Image4]│ │[Image5]│ │[Image6]│                    │
│  │ Label  │ │ Label  │ │ Label  │                    │
│  └────────┘ └────────┘ └────────┘                    │
│                                                         │
│              [Check My Answer]                          │
└─────────────────────────────────────────────────────────┘
```

**Container Design:**
- **YES - SAFE**:
  - Green background (light green, not harsh)
  - Large green checkmark icon
  - Smiling, friendly icon
  - Label: "YES - SAFE ✓"

- **NO - NOT SAFE**:
  - Red background (soft red, not alarming)
  - Stop hand symbol (not scary, clear)
  - Label: "NO - NOT SAFE ✗"

**Scenario Images** (120x120px, cartoon style, diverse children):

**SAFE Behaviors:**
1. **Ask Adult for Help**: Child raising hand to adult nearby at computer
   - Label: "Ask an adult"
2. **Use Nice Words**: Speech bubble with "Great job!" and smiley face
   - Label: "Be kind online"
3. **Tell Teacher Problem**: Child talking to teacher, pointing at screen
   - Label: "Tell a teacher"

**UNSAFE Behaviors:**
4. **Share Full Name**: Screen showing "My name is [Full Name]" being typed
   - Label: "Share my full name"
5. **Share Address**: Screen showing "I live at [Address]" being typed
   - Label: "Share my address"
6. **Click Unknown Links**: Cursor hovering over suspicious pop-up/link
   - Label: "Click any link"

**Visual Style:**
- Simple, clear illustrations
- Diverse child characters
- Not scary or overly serious
- Recognizable computer/tablet screens in images
- Consistent cartoon style

#### Student Experience Walkthrough

**Step 1: Introduction**
- Audio: "Is it safe to do this online? Look at each picture. Drag it to Yes if it's safe, or No if it's not safe."
- Student sees two large containers (YES/NO)
- Student sees 6 picture cards to sort

**Step 2: Examining Pictures**
- Student can tap each picture to hear description:
  - Taps "Ask an adult" card
  - Audio: "This shows asking an adult for help."
- Student thinks about whether this is safe

**Step 3: Sorting**
- Student drags "Ask an adult" toward YES container
- YES container highlights green
- Card drops in with positive sound
- Card remains visible inside YES container
- Student continues with remaining 5 cards

**Step 4: Checking Answer (All Correct)**
- Student clicks "Check My Answer"
- ✅ Both containers flash green
- All cards in YES show green checkmarks
- All cards in NO show red X's (confirming correct placement)
- ⭐ Stars and celebration
- 💬 "Great job! You know how to be safe online!"
- 🔊 Audio praise
- ➡️ "Next Skill" button

**Step 5: Checking Answer (Some Incorrect)**
- Example: Student put "Share my full name" in YES (incorrect)
- ❌ That card shakes in YES container
- 💬 "Some need to be moved. Think about staying safe!"
- 🔊 Audio: "Some pictures are in the wrong group. Think carefully..."
- 💡 Hint: "Should you share your address online?"
- Student can drag shaking card(s) to other container
- "Try Again" button

**Step 6: Second Attempt Still Incorrect**
- More specific hint provided
- 💡 "Asking for help is safe. Sharing personal information is not safe."
- 🎬 Optional: Categories pulse (YES glows green, NO glows red) to reinforce
- Student tries again

**Step 7: Show Answer (3rd Attempt)**
- 🎬 Animation shows correct sorting:
  - "Ask an adult" slides to YES: ✓ "Asking for help keeps you safe!"
  - "Share my full name" slides to NO: ✗ "Don't share your name with strangers online."
  - (Continues for each card with brief explanation)
- 💬 "Let's learn about being safe online!"
- 🔊 Each card is explained as it moves to correct container
- ➡️ "Try Another Set" (new random selection of 6 from pool of 12)

#### Teacher Notes

**Learning Objective:**
Students will identify safe and unsafe online behaviors, with focus on privacy and seeking adult help.

**Pre-Lesson Discussion:**
- "What does 'online' mean?" (on the computer/tablet/internet)
- "Who helps keep you safe at home? At school?" (adults)
- "What is personal information?" (name, address, phone, age, school)
- "Why do we keep some information private?" (stranger danger applies online too)

**Context Setting:**
This skill should be part of broader digital citizenship curriculum:
- Previous lesson: "What is the internet?"
- This lesson: "Staying safe online"
- Next lesson: "Being kind online"

**What to Look For:**
- Can students identify what "personal information" means?
- Do they understand adults are helpers (not obstacles)?
- Are they applying real-world safety rules to online context?
- Do they understand "stranger danger" applies online?

**Common Student Responses:**

1. **"But I have friends online!"**
   - **Clarify**: "Are they friends you know in real life, or people you've only met online? There's a difference!"

2. **"My mom is right here, so it's safe to share my address."**
   - **Clarify**: "Great that mom is there! But once you type it online, lots of people can see it. Better to ask mom first."

3. **Confusion about "nice words" being online-specific**
   - **Clarify**: "We use nice words everywhere - in person AND online!"

4. **Thinking they shouldn't tell adults about problems**
   - **Emphasize**: "Telling an adult is ALWAYS the right choice if something feels wrong or confusing!"

**Differentiation:**

**Struggling Students:**
- Use 4 scenarios (2 obviously safe, 2 obviously unsafe)
- Discuss each scenario as a class first, then have students sort
- Use physical cards before digital version
- Pair with peer mentor

**Advanced Students:**
- Add "Safe WITH adult permission" third category
- Discuss nuance: "When might it be OK to share your name?" (with parent, on school website, etc.)
- Have student generate their own safe/unsafe scenarios
- Role-play: Student teaches younger sibling about online safety

**English Language Learners:**
- Pre-teach vocabulary: safe, unsafe, personal information, adult, private
- Use visuals heavily (already picture-based)
- Pair with bilingual peer if possible
- Provide word bank with pictures

**Students with Special Needs:**
- Use physical manipulatives first
- Simplify to 2-4 scenarios
- Use social story: "I stay safe online" narrative
- Repeat with consistency for rule internalization

**Extensions:**

1. **Class Safety Rules Poster**: Students create visual rules for computer lab
2. **Role Play**: Act out scenarios (what would you do if...)
3. **Family Conversation**: Take-home sheet for family internet safety plan
4. **Story Time**: Read book about online safety (e.g., "Chicken Clicking" by Jeanne Willis)
5. **Guest Speaker**: Invite police officer or librarian to discuss online safety

**Assessment:**
Student demonstrates understanding when they can:
- Correctly identify 5-6 scenarios as safe/unsafe
- Explain WHY something is safe or unsafe
- Apply rules to new scenarios not practiced
- State the rule: "I don't share personal information online" and "I ask an adult for help"

**Parent Communication:**
Send home note explaining what was learned and how families can reinforce:
- Review family rules for internet use
- Discuss what "personal information" means
- Remind child to always ask adult before sharing online
- Keep computers in common family areas when possible

**Cross-Curricular Connections:**
- **Social-Emotional Learning**: Making safe choices, asking for help
- **Reading**: Following rules, understanding consequences
- **Health**: Personal safety, stranger danger

**Resources for Teachers:**
- Common Sense Media (digital citizenship curriculum)
- NetSmartz (online safety education from NCMEC)
- Be Internet Awesome (Google's internet safety program)

---

## Example 5: Path Navigation (Computational Thinking)

### Original Concept (Coding-Heavy)
**Topic**: T01 - Everyday Algorithms (Grade 2)
**Original Skill**: "Write directional commands (forward, turn left, turn right) to navigate maze"
- Student writes: `forward(3); turnLeft(); forward(2);`
- Requires understanding commands and spatial reasoning together
- Syntax-focused

### Redesigned Picture-Based Version

#### Complete Specification

```json
{
  "id": "T01.G2.05",
  "title": "Help the Robot Get Home",
  "short_name": "Navigate simple grid paths with directional clicks",
  "topic_id": "T01",
  "grade": "2",
  "skill_type": "light_coding_prep",
  "activity_type": "path_tracing",
  "description_teacher": "Students guide a robot through a 5x5 grid from start to goal by clicking directional arrows. This prepares students for algorithmic thinking and introduces the concept of precise step-by-step instructions without requiring code syntax.",
  "student_prompt": "Help the robot get home! Click the arrows to move the robot to the house.",
  "student_prompt_audio": {
    "tts_text": "Help the robot get home! Click the arrows to tell the robot which way to move. Get the robot to the house!",
    "voice_settings": {
      "speed": "normal",
      "voice_type": "child_friendly"
    }
  },
  "interaction_details": {
    "item_count": 4,
    "interaction_mode": "click_items",
    "visual_theme": "transportation",
    "estimated_time_minutes": 5,
    "randomization": {
      "enabled": true,
      "randomize_positions": false,
      "randomize_items": true,
      "item_pool_size": 8
    },
    "difficulty_parameters": {
      "grid_size": "5x5",
      "obstacles": 2,
      "path_length": "6-8 moves"
    }
  },
  "auto_grade_rules": {
    "type": "location_accuracy",
    "correct_answer": {
      "goal_reached": true,
      "path_valid": true,
      "obstacle_avoided": true
    },
    "partial_credit": {
      "enabled": true,
      "rules": [
        {
          "condition": "Reached goal but hit obstacle",
          "credit_percentage": 50,
          "feedback": "You got there, but watch out for obstacles!"
        }
      ]
    },
    "feedback": {
      "correct": {
        "message": "The robot made it home! Great directions!",
        "audio_tts": "The robot made it home! You gave great directions!",
        "visual_effect": "robot_celebration"
      },
      "incorrect": {
        "attempt_1": {
          "message": "The robot didn't make it. Try a different path!",
          "audio_tts": "The robot didn't make it home yet. Try giving different directions!",
          "hint_provided": true,
          "hint_text": "Which direction should the robot go first?"
        },
        "attempt_2": {
          "message": "Keep trying! Plan your path before clicking.",
          "audio_tts": "Keep trying! Look at where the house is. Plan your path before you click the arrows.",
          "hint_provided": true,
          "hint_text": "The robot needs to go right, then up. Can you find that path?",
          "visual_hint": true,
          "visual_hint_type": "show_goal_direction"
        },
        "attempt_3": {
          "message": "Let me show you one way to get home!",
          "show_correct_answer": true,
          "audio_tts": "Let me show you one way the robot can get home! Watch the path.",
          "visual_hint_type": "animate_solution_path"
        }
      }
    },
    "retry_logic": {
      "max_attempts": 3,
      "show_correct_answer": true,
      "reset_on_retry": true
    }
  },
  "accessibility": {
    "audio_support": true,
    "keyboard_navigable": true,
    "screen_reader_compatible": true,
    "touch_target_size": "large",
    "color_blind_safe": true,
    "high_contrast_mode": true,
    "language_support": ["en", "es"]
  },
  "dependencies": ["T01.G2.03"],
  "csta_code": "1A-AP-11",
  "additional_metadata": {
    "tags": ["algorithms", "sequencing", "spatial_reasoning", "directions", "problem_solving"],
    "learning_objectives": [
      "Give step-by-step directions to reach a goal",
      "Use spatial reasoning to plan a path",
      "Understand that order of steps matters",
      "Recognize that there may be multiple correct solutions"
    ],
    "common_misconceptions": [
      "Thinking robot can move diagonally (only up/down/left/right)",
      "Not planning ahead, just trying random directions",
      "Confusion between left/right from robot's perspective vs. their own",
      "Thinking robot can jump over obstacles"
    ],
    "differentiation_notes": {
      "scaffolding": "Use 3x3 grid, no obstacles, shorter path; show first step already done; use physical robot on floor mat first",
      "extension": "Larger grid (6x6), more obstacles, require shortest path, introduce 'turn' concept, use cardinal directions (north/south/east/west)"
    },
    "home_school_notes": "Play 'Robot' at home! One person gives directions, another follows them exactly. Take turns!"
  }
}
```

(Content continues with visual mockup, walkthrough, and teacher notes - following same detailed format as previous examples)

---

## Summary Table: Redesign Principles

| Original (Coding-Heavy) | Redesigned (Picture-Based) |
|------------------------|----------------------------|
| Write code blocks | Drag pictures to slots |
| Syntax required | No syntax needed |
| Text-heavy | Picture-primary, minimal text |
| Abstract representation | Concrete, familiar contexts |
| Typing/spelling needed | Click, drag, tap only |
| Sequential coding logic | Visual sequencing |
| Variables and functions | Patterns and sorting |
| Boolean conditions | Binary choices (Yes/No) |
| Loops as code | Patterns as repetition |
| Debugging code | Trial and error with hints |

---

## Key Design Principles Demonstrated

1. **Developmentally Appropriate**: All examples match cognitive stage (concrete operational)
2. **Picture-First**: Images carry the primary content, words support
3. **Audio Support**: Every example includes comprehensive audio narration
4. **Auto-Gradable**: Clear, objective correctness criteria
5. **Encouraging Feedback**: Positive language, progressive hints, show answer after attempts
6. **Accessibility**: Large touch targets, keyboard nav, screen reader support
7. **Engagement**: Friendly characters, meaningful contexts, celebration of success
8. **Cultural Responsiveness**: Diverse representation, inclusive scenarios
9. **Appropriate Time**: 2-5 minutes per skill by grade
10. **Real-World Connections**: Skills relate to students' daily experiences

---

**Document Version**: 1.0
**Last Updated**: 2025
**Maintained by**: CreatiCode Curriculum Team
