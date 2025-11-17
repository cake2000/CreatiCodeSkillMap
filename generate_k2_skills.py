#!/usr/bin/env python3
"""
K-2 Picture-Based Skills Generator
Redesigns K-2 skills for high-priority topics following developmentally appropriate framework
"""

import json
from typing import List, Dict, Any

# CSTA alignment mapping (simplified)
CSTA_CODES = {
    'T01': {'K': '1A-AP-08', '1': '1A-AP-08', '2': '1A-AP-11'},
    'T04': {'K': '1A-AP-08', '1': '1A-AP-08', '2': '1A-AP-14'},
    'T25': {'K': '1A-DA-05', '1': '1A-DA-05', '2': '1A-DA-06'},
    'T26': {'K': '1A-DA-05', '1': '1A-DA-05', '2': '1A-DA-06'},
    'T27': {'K': '1A-DA-07', '1': '1A-DA-07', '2': '1A-DA-07'},
    'T30': {'K': '1A-CS-01', '1': '1A-CS-01', '2': '1A-CS-02'},
    'T32': {'K': '1A-NI-04', '1': '1A-NI-04', '2': '1A-NI-04'},
    'T34': {'K': '1A-IC-16', '1': '1A-IC-16', '2': '1A-IC-18'},
    'T35': {'K': '1A-IC-17', '1': '1A-IC-17', '2': '1A-IC-18'},
}

def create_skill(topic_id: str, grade: str, skill_num: int,
                 title: str, short_name: str, activity_type: str,
                 description_teacher: str, student_prompt: str,
                 interaction_details: Dict, auto_grade_rules: Dict,
                 notes_redesign: str = "") -> Dict[str, Any]:
    """Create a skill dictionary following K-2 format specification"""

    skill_id = f"{topic_id}.G{grade}.{skill_num:02d}"
    csta_code = CSTA_CODES.get(topic_id, {}).get(grade, '1A-AP-08')

    return {
        "id": skill_id,
        "title": title,
        "short_name": short_name,
        "topic_id": topic_id,
        "grade": grade,
        "skill_type": "picture_based_digital",
        "activity_type": activity_type,
        "description_teacher": description_teacher,
        "student_prompt": student_prompt,
        "student_prompt_audio": {
            "tts_text": student_prompt,
            "voice_settings": {
                "speed": "normal",
                "voice_type": "child_friendly"
            }
        },
        "interaction_details": interaction_details,
        "auto_grade_rules": auto_grade_rules,
        "accessibility": {
            "audio_support": True,
            "keyboard_navigable": True,
            "screen_reader_compatible": True,
            "touch_target_size": "extra_large" if grade == "K" else "large",
            "color_blind_safe": True,
            "high_contrast_mode": True,
            "language_support": ["en"]
        },
        "dependencies": [],
        "csta_code": csta_code,
        "notes_redesign": notes_redesign
    }

def create_t01_skills() -> List[Dict]:
    """T01: Everyday Algorithms & Step-by-Step Thinking"""
    skills = []

    # Kindergarten (NEW - 4 skills)
    skills.append(create_skill(
        "T01", "K", 1,
        "Help the Puppy Get Ready for Bed",
        "Sequence 3 bedtime routine steps",
        "drag_drop_sequence",
        "Students practice sequencing by arranging 3 pictures of a puppy's bedtime routine in logical order. This builds foundational understanding of algorithms as ordered steps.",
        "Put the pictures in order to help the puppy get ready for bed!",
        {
            "item_count": 3,
            "items": ["Brush teeth", "Put on pajamas", "Get in bed"],
            "interaction_mode": "drag_to_slots",
            "visual_theme": "animals_pets",
            "estimated_time_minutes": 2,
            "randomization": {"enabled": True, "randomize_positions": True}
        },
        {
            "type": "sequence_order",
            "correct_answer": ["pajamas", "brush", "bed"],
            "partial_credit": {"enabled": False},
            "feedback": {
                "correct": {"message": "Great job! The puppy is ready for bed!", "audio_tts": "Great job! The puppy is ready for bed!", "visual_effect": "stars"},
                "incorrect": {"message": "Try again! What does the puppy do first?", "audio_tts": "Try again! Think about what the puppy does first.", "hint_provided": True, "hint_text": "We put on pajamas before brushing teeth!"}
            },
            "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": True}
        },
        "NEW K skill - picture-based sequencing activity"
    ))

    skills.append(create_skill(
        "T01", "K", 2,
        "Making a Sandwich: What's the Right Order?",
        "Sequence 3 sandwich-making steps",
        "drag_drop_sequence",
        "Students arrange pictures showing how to make a sandwich in the correct order, reinforcing the concept that steps must follow a logical sequence.",
        "Drag the pictures to show how to make a sandwich!",
        {
            "item_count": 3,
            "items": ["Get bread", "Add peanut butter", "Put bread together"],
            "interaction_mode": "drag_to_slots",
            "visual_theme": "food_cooking",
            "estimated_time_minutes": 2,
            "randomization": {"enabled": True, "randomize_positions": True}
        },
        {
            "type": "sequence_order",
            "correct_answer": ["bread", "peanut_butter", "close"],
            "partial_credit": {"enabled": False},
            "feedback": {
                "correct": {"message": "Yummy! You made a perfect sandwich!", "audio_tts": "Yummy! You made a perfect sandwich!", "visual_effect": "confetti"},
                "incorrect": {"message": "Not quite! What do we need first?", "audio_tts": "Not quite! What do we need first to make a sandwich?", "hint_provided": True, "hint_text": "We need bread before we can add anything!"}
            },
            "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": True}
        },
        "NEW K skill - everyday algorithm with familiar task"
    ))

    skills.append(create_skill(
        "T01", "K", 3,
        "Getting Dressed: Morning Routine",
        "Sequence 3 getting dressed steps",
        "drag_drop_sequence",
        "Students sequence pictures of getting dressed, understanding that some actions must come before others (underwear before pants!).",
        "Put the pictures in order to get dressed for school!",
        {
            "item_count": 3,
            "items": ["Put on underwear", "Put on pants", "Put on shoes"],
            "interaction_mode": "drag_to_slots",
            "visual_theme": "home_family",
            "estimated_time_minutes": 2,
            "randomization": {"enabled": True, "randomize_positions": True}
        },
        {
            "type": "sequence_order",
            "correct_answer": ["underwear", "pants", "shoes"],
            "partial_credit": {"enabled": False},
            "feedback": {
                "correct": {"message": "Perfect! Now you're ready for school!", "audio_tts": "Perfect! Now you're ready for school!", "visual_effect": "stars"},
                "incorrect": {"message": "Try again! What goes on first?", "audio_tts": "Try again! Think about what we put on first.", "hint_provided": True, "hint_text": "Underwear goes on before pants!"}
            },
            "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": True}
        },
        "NEW K skill - logical sequencing with clear dependencies"
    ))

    skills.append(create_skill(
        "T01", "K", 4,
        "Washing Hands: Do It Right!",
        "Sequence 3 handwashing steps",
        "drag_drop_sequence",
        "Students arrange pictures showing proper handwashing steps, connecting algorithms to health routines.",
        "Show the right way to wash your hands!",
        {
            "item_count": 3,
            "items": ["Turn on water", "Use soap", "Dry hands"],
            "interaction_mode": "drag_to_slots",
            "visual_theme": "home_family",
            "estimated_time_minutes": 2,
            "randomization": {"enabled": True, "randomize_positions": True}
        },
        {
            "type": "sequence_order",
            "correct_answer": ["water", "soap", "dry"],
            "partial_credit": {"enabled": False},
            "feedback": {
                "correct": {"message": "Great! Your hands are clean!", "audio_tts": "Great! Your hands are clean and healthy!", "visual_effect": "stars"},
                "incorrect": {"message": "Try again! What do we do first?", "audio_tts": "Try again! What do we do first when washing hands?", "hint_provided": True, "hint_text": "We need water before we can use soap!"}
            },
            "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": True}
        },
        "NEW K skill - health-related algorithm"
    ))

    # Grade 1 (REDESIGN - 4 skills)
    skills.append(create_skill(
        "T01", "1", 1,
        "Plant a Seed: Steps in Order",
        "Sequence 4-5 planting steps",
        "drag_drop_sequence",
        "Students arrange pictures showing how to plant a seed in the correct order, building on K sequencing with more steps and complexity.",
        "Put the pictures in order to plant a seed!",
        {
            "item_count": 5,
            "items": ["Get a pot", "Add soil", "Make hole", "Put seed in", "Water it"],
            "interaction_mode": "drag_to_slots",
            "visual_theme": "nature_weather",
            "estimated_time_minutes": 3,
            "randomization": {"enabled": True, "randomize_positions": True}
        },
        {
            "type": "sequence_order",
            "correct_answer": ["pot", "soil", "hole", "seed", "water"],
            "partial_credit": {"enabled": False},
            "feedback": {
                "correct": {"message": "Perfect! Your seed will grow into a plant!", "audio_tts": "Perfect! Your seed will grow into a beautiful plant!", "visual_effect": "confetti"},
                "incorrect": {"message": "Not quite! Think about what you need first.", "audio_tts": "Not quite! Think about what you need before you can plant.", "hint_provided": True, "hint_text": "You need a pot before you can add soil!"}
            },
            "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": True}
        },
        "Redesigned from coding-heavy G1.01 to picture-based sequencing"
    ))

    skills.append(create_skill(
        "T01", "1", 2,
        "What Happens Next? Story Sequence",
        "Predict next step in 4-picture sequence",
        "multiple_choice_visual",
        "Students view a 3-picture sequence and predict what comes next from visual choices, practicing algorithmic prediction.",
        "Look at the story. What happens next?",
        {
            "item_count": 4,
            "interaction_mode": "click_items",
            "visual_theme": "animals_pets",
            "estimated_time_minutes": 3,
            "randomization": {"enabled": True, "randomize_items": True}
        },
        {
            "type": "single_choice",
            "correct_answer": "option_correct",
            "partial_credit": {"enabled": False},
            "feedback": {
                "correct": {"message": "Yes! That's what happens next!", "audio_tts": "Yes! That's what happens next in the story!", "visual_effect": "stars"},
                "incorrect": {"message": "Try again! Look at what the cat is doing.", "audio_tts": "Try again! Look carefully at what the cat is doing.", "hint_provided": True, "hint_text": "The cat is walking toward something!"}
            },
            "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": False}
        },
        "Redesigned from G1.02 (trace algorithm) to visual prediction"
    ))

    skills.append(create_skill(
        "T01", "1", 3,
        "Find the Missing Step",
        "Identify missing step in sequence",
        "click_select",
        "Students identify which step is missing from a sequence, building debugging skills through picture-based problem solving.",
        "One picture is missing! Click on what's missing from the steps.",
        {
            "item_count": 6,
            "interaction_mode": "click_items",
            "visual_theme": "food_cooking",
            "estimated_time_minutes": 4,
            "randomization": {"enabled": True, "randomize_positions": True}
        },
        {
            "type": "selection_set",
            "correct_answer": ["missing_step"],
            "partial_credit": {"enabled": False},
            "feedback": {
                "correct": {"message": "Great! You found the missing step!", "audio_tts": "Great! You found the missing step!", "visual_effect": "stars"},
                "incorrect": {"message": "Not quite! Look at all the steps carefully.", "audio_tts": "Not quite! Look at all the steps to see what's missing.", "hint_provided": True, "hint_text": "What do we do after mixing but before baking?"}
            },
            "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": False}
        },
        "Redesigned from G1.03 (identify incorrect steps) to visual debugging"
    ))

    skills.append(create_skill(
        "T01", "1", 4,
        "Two Ways to Do It: Which is Better?",
        "Compare two visual sequences",
        "click_select",
        "Students compare two different sequences for the same task and identify which one works better or is more efficient.",
        "Look at both ways. Which way works better? Click on it!",
        {
            "item_count": 2,
            "interaction_mode": "click_items",
            "visual_theme": "home_family",
            "estimated_time_minutes": 4,
            "randomization": {"enabled": False}
        },
        {
            "type": "single_choice",
            "correct_answer": "better_sequence",
            "partial_credit": {"enabled": False},
            "feedback": {
                "correct": {"message": "Yes! That way works better!", "audio_tts": "Yes! That way works better and is easier!", "visual_effect": "confetti"},
                "incorrect": {"message": "Look again. Which way has all the steps?", "audio_tts": "Look again. Which way has all the steps we need?", "hint_provided": True, "hint_text": "Count the steps in each way!"}
            },
            "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": False}
        },
        "Redesigned from G1.04 (compare algorithms) to visual comparison"
    ))

    # Grade 2 (REDESIGN - 4 skills with bridge activities)
    skills.append(create_skill(
        "T01", "2", 1,
        "Choose the Path: If-Then Decisions",
        "Sequence with conditional choices",
        "click_select",
        "Students follow a sequence that includes an if-then decision, clicking on the correct path based on a condition. Bridges to conditional logic.",
        "The robot needs to go around the puddle. Click to show the right path!",
        {
            "item_count": 8,
            "interaction_mode": "tap_sequence",
            "visual_theme": "technology",
            "estimated_time_minutes": 4,
            "randomization": {"enabled": True, "randomize_items": True}
        },
        {
            "type": "sequence_order",
            "correct_answer": ["forward", "check", "turn_if_puddle", "forward", "forward"],
            "partial_credit": {"enabled": False},
            "feedback": {
                "correct": {"message": "Perfect! The robot stayed dry!", "audio_tts": "Perfect! You helped the robot go around the puddle!", "visual_effect": "stars"},
                "incorrect": {"message": "Try again! What should the robot do when it sees the puddle?", "audio_tts": "Try again! What should the robot do when it sees the puddle?", "hint_provided": True, "hint_text": "The robot needs to turn when it sees a puddle!"}
            },
            "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": True}
        },
        "Redesigned from G2.01 (write if-then) to picture-based conditional"
    ))

    skills.append(create_skill(
        "T01", "2", 2,
        "Patterns that Repeat: Can You See It?",
        "Identify repeating sequences",
        "click_select",
        "Students identify which part of a visual sequence repeats multiple times, building foundation for loop concepts through pattern recognition.",
        "Which part repeats over and over? Click on it!",
        {
            "item_count": 12,
            "interaction_mode": "click_items",
            "visual_theme": "patterns",
            "estimated_time_minutes": 4,
            "randomization": {"enabled": True, "randomize_items": True}
        },
        {
            "type": "selection_set",
            "correct_answer": ["repeating_unit"],
            "partial_credit": {"enabled": False},
            "feedback": {
                "correct": {"message": "Yes! That pattern repeats!", "audio_tts": "Yes! You found the pattern that repeats over and over!", "visual_effect": "stars"},
                "incorrect": {"message": "Look again. What do you see more than once?", "audio_tts": "Look again. What do you see happening more than once?", "hint_provided": True, "hint_text": "Find the steps that happen again and again!"}
            },
            "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": False}
        },
        "Redesigned from G2.02 (repeat statement) to visual pattern identification bridging to loops"
    ))

    skills.append(create_skill(
        "T01", "2", 3,
        "Follow the Steps: What Does It Make?",
        "Trace sequence to predict outcome",
        "multiple_choice_visual",
        "Students follow a 6-8 step visual sequence and predict the final result from picture choices.",
        "Follow all the steps. What will you make?",
        {
            "item_count": 4,
            "interaction_mode": "click_items",
            "visual_theme": "food_cooking",
            "estimated_time_minutes": 5,
            "randomization": {"enabled": True, "randomize_items": True}
        },
        {
            "type": "single_choice",
            "correct_answer": "final_product",
            "partial_credit": {"enabled": False},
            "feedback": {
                "correct": {"message": "Correct! That's what the steps make!", "audio_tts": "Correct! If you follow all the steps, you make that!", "visual_effect": "confetti"},
                "incorrect": {"message": "Try again! Follow each step carefully.", "audio_tts": "Try again! Follow each step carefully to see what you make.", "hint_provided": True, "hint_text": "Look at what you're adding in each step!"}
            },
            "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": False}
        },
        "Redesigned from G2.03 (trace with branching) to outcome prediction"
    ))

    skills.append(create_skill(
        "T01", "2", 4,
        "Guide the Robot Through the Maze",
        "Navigate path with directional choices",
        "path_tracing",
        "Students click directional arrows to guide a robot through a simple maze, applying sequential thinking in a problem-solving context.",
        "Click the arrows to guide the robot to the star!",
        {
            "item_count": 8,
            "interaction_mode": "tap_sequence",
            "visual_theme": "technology",
            "estimated_time_minutes": 5,
            "randomization": {"enabled": True, "randomize_items": False}
        },
        {
            "type": "sequence_order",
            "correct_answer": ["forward", "forward", "right", "forward", "left", "forward"],
            "partial_credit": {"enabled": True, "rules": [{"condition": "75% correct", "credit_percentage": 75}]},
            "feedback": {
                "correct": {"message": "Amazing! The robot reached the star!", "audio_tts": "Amazing! You guided the robot to the star!", "visual_effect": "confetti"},
                "incorrect": {"message": "Not quite! Try a different path.", "audio_tts": "Not quite! Try a different path to reach the star.", "hint_provided": True, "hint_text": "The robot needs to go around the walls!"}
            },
            "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": True}
        },
        "Redesigned from G2.04 (unplugged maze) to interactive digital navigation"
    ))

    return skills


def create_t04_skills() -> List[Dict]:
    """T04: Patterns & Reusable Solutions"""
    skills = []

    # Kindergarten (NEW - 4 skills)
    skills.append(create_skill(
        "T04", "K", 1,
        "Animal Pattern: What Comes Next?",
        "Complete simple AB pattern",
        "pattern_complete",
        "Students identify and complete a simple AB pattern using animal pictures, building pattern recognition skills that underpin algorithmic thinking.",
        "Look at the pattern. What comes next?",
        {
            "item_count": 3,
            "interaction_mode": "click_items",
            "visual_theme": "animals_pets",
            "estimated_time_minutes": 2,
            "randomization": {"enabled": True, "randomize_items": True, "item_pool_size": 6}
        },
        {
            "type": "pattern_completion",
            "correct_answer": "next_in_pattern",
            "partial_credit": {"enabled": False},
            "feedback": {
                "correct": {"message": "Perfect! You found the pattern!", "audio_tts": "Perfect! You found what comes next in the pattern!", "visual_effect": "stars"},
                "incorrect": {"message": "Try again! Look at what repeats.", "audio_tts": "Try again! Look at which animals repeat.", "hint_provided": True, "hint_text": "Dog, cat, dog, cat... what comes next?"}
            },
            "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": False}
        },
        "NEW K skill - AB pattern recognition"
    ))

    skills.append(create_skill(
        "T04", "K", 2,
        "Color Pattern: Red, Blue, Red, Blue",
        "Complete AB color pattern",
        "pattern_complete",
        "Students complete a simple color pattern, reinforcing pattern recognition with a different attribute (color).",
        "What color comes next in the pattern?",
        {
            "item_count": 3,
            "interaction_mode": "click_items",
            "visual_theme": "colors_shapes",
            "estimated_time_minutes": 2,
            "randomization": {"enabled": True, "randomize_items": True, "item_pool_size": 4}
        },
        {
            "type": "pattern_completion",
            "correct_answer": "next_color",
            "partial_credit": {"enabled": False},
            "feedback": {
                "correct": {"message": "Great! You know the pattern!", "audio_tts": "Great! You know which color comes next!", "visual_effect": "stars"},
                "incorrect": {"message": "Look again! What color repeats?", "audio_tts": "Look again! What color repeats over and over?", "hint_provided": True, "hint_text": "Red, blue, red, blue... what's next?"}
            },
            "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": False}
        },
        "NEW K skill - AB pattern with colors"
    ))

    skills.append(create_skill(
        "T04", "K", 3,
        "Shape Pattern: Circle, Square, Circle",
        "Complete AB shape pattern",
        "pattern_complete",
        "Students complete a shape pattern, applying pattern recognition to geometric attributes.",
        "What shape comes next?",
        {
            "item_count": 3,
            "interaction_mode": "click_items",
            "visual_theme": "colors_shapes",
            "estimated_time_minutes": 2,
            "randomization": {"enabled": True, "randomize_items": True, "item_pool_size": 5}
        },
        {
            "type": "pattern_completion",
            "correct_answer": "next_shape",
            "partial_credit": {"enabled": False},
            "feedback": {
                "correct": {"message": "Yes! You found the next shape!", "audio_tts": "Yes! You found which shape comes next!", "visual_effect": "confetti"},
                "incorrect": {"message": "Try again! Look at the shapes.", "audio_tts": "Try again! Look carefully at the shapes.", "hint_provided": True, "hint_text": "Circle, square, circle, square... what's next?"}
            },
            "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": False}
        },
        "NEW K skill - AB pattern with shapes"
    ))

    skills.append(create_skill(
        "T04", "K", 4,
        "Big-Small Pattern",
        "Complete AB size pattern",
        "pattern_complete",
        "Students complete a pattern based on size attribute (big-small), expanding pattern understanding.",
        "What size comes next? Big or small?",
        {
            "item_count": 3,
            "interaction_mode": "click_items",
            "visual_theme": "colors_shapes",
            "estimated_time_minutes": 2,
            "randomization": {"enabled": True, "randomize_items": True}
        },
        {
            "type": "pattern_completion",
            "correct_answer": "next_size",
            "partial_credit": {"enabled": False},
            "feedback": {
                "correct": {"message": "Perfect! You know big and small!", "audio_tts": "Perfect! You found which size comes next!", "visual_effect": "stars"},
                "incorrect": {"message": "Try again! Big or small?", "audio_tts": "Try again! Is the next one big or small?", "hint_provided": True, "hint_text": "Big, small, big, small... what's next?"}
            },
            "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": False}
        },
        "NEW K skill - AB pattern with size"
    ))

    # Grade 1 (REDESIGN - 4 skills)
    skills.append(create_skill(
        "T04", "1", 1,
        "Find the Repeating Part",
        "Identify repeating unit in ABC pattern",
        "click_select",
        "Students identify which sequence of items repeats in a longer pattern, building awareness of reusable units.",
        "Click on the part that repeats over and over!",
        {
            "item_count": 12,
            "interaction_mode": "click_items",
            "visual_theme": "patterns",
            "estimated_time_minutes": 3,
            "randomization": {"enabled": True, "randomize_items": True}
        },
        {
            "type": "selection_set",
            "correct_answer": ["repeating_unit"],
            "partial_credit": {"enabled": False},
            "feedback": {
                "correct": {"message": "Great! You found what repeats!", "audio_tts": "Great! You found the part that repeats!", "visual_effect": "stars"},
                "incorrect": {"message": "Try again! What do you see more than once?", "audio_tts": "Try again! What group do you see more than once?", "hint_provided": True, "hint_text": "Look for a group of items that happens again and again!"}
            },
            "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": False}
        },
        "Redesigned from G1.01 (find repeated blocks) to visual pattern recognition"
    ))

    skills.append(create_skill(
        "T04", "1", 2,
        "Story Pattern Match",
        "Match repeating story to pattern",
        "match_pairs",
        "Students match pictures showing a repeating story sequence to the visual pattern it creates.",
        "Match each story to its pattern!",
        {
            "item_count": 4,
            "interaction_mode": "drag_to_match",
            "visual_theme": "stories",
            "estimated_time_minutes": 4,
            "randomization": {"enabled": True, "randomize_positions": True}
        },
        {
            "type": "pair_match",
            "correct_answer": {"story1": "pattern1", "story2": "pattern2", "story3": "pattern3", "story4": "pattern4"},
            "partial_credit": {"enabled": False},
            "feedback": {
                "correct": {"message": "Perfect matching!", "audio_tts": "Perfect! You matched all the stories to their patterns!", "visual_effect": "confetti"},
                "incorrect": {"message": "Try again! Look at what repeats in each story.", "audio_tts": "Try again! Look at what repeats in each story.", "hint_provided": True, "hint_text": "Find the part of the story that happens over and over!"}
            },
            "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": True}
        },
        "Redesigned from G1.02 (match picture story to code) to pattern matching"
    ))

    skills.append(create_skill(
        "T04", "1", 3,
        "Template Time: Which Ones Are the Same?",
        "Identify items following same template",
        "click_select",
        "Students identify which pictures follow the same basic structure/template, building understanding of reusable solutions.",
        "Click on all the pictures that are made the same way!",
        {
            "item_count": 8,
            "interaction_mode": "click_items",
            "visual_theme": "patterns",
            "estimated_time_minutes": 4,
            "randomization": {"enabled": True, "randomize_positions": True}
        },
        {
            "type": "selection_set",
            "correct_answer": ["same_template_items"],
            "partial_credit": {"enabled": False},
            "feedback": {
                "correct": {"message": "Yes! They're all made the same way!", "audio_tts": "Yes! All those pictures follow the same pattern!", "visual_effect": "stars"},
                "incorrect": {"message": "Look again! Which ones have the same structure?", "audio_tts": "Look again! Which ones have the same structure or design?", "hint_provided": True, "hint_text": "Look at how the colors and shapes are arranged!"}
            },
            "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": False}
        },
        "Redesigned from G1.03 (recognize template) to visual template identification"
    ))

    skills.append(create_skill(
        "T04", "1", 4,
        "Make Your Own Pattern",
        "Create repeating pattern by arranging items",
        "drag_drop_sequence",
        "Students create their own repeating pattern by dragging items into slots, applying pattern knowledge creatively.",
        "Make a pattern that repeats! Drag the items.",
        {
            "item_count": 6,
            "items": ["Choose 2-3 different items to repeat"],
            "interaction_mode": "drag_to_slots",
            "visual_theme": "colors_shapes",
            "estimated_time_minutes": 4,
            "randomization": {"enabled": False}
        },
        {
            "type": "pattern_completion",
            "correct_answer": "valid_repeating_pattern",
            "partial_credit": {"enabled": False},
            "feedback": {
                "correct": {"message": "Great pattern! It repeats perfectly!", "audio_tts": "Great! Your pattern repeats over and over!", "visual_effect": "confetti"},
                "incorrect": {"message": "Almost! Make sure your pattern repeats.", "audio_tts": "Almost! Make sure the same group repeats over and over.", "hint_provided": True, "hint_text": "Pick a group and repeat it at least two times!"}
            },
            "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": True}
        },
        "Redesigned from G1.04 (build repeating script) to visual pattern creation"
    ))

    # Grade 2 (REDESIGN - 4 skills)
    skills.append(create_skill(
        "T04", "2", 1,
        "Find All the Patterns",
        "Identify multiple repeating sections",
        "click_select",
        "Students identify all the different patterns that repeat in a complex visual sequence, building advanced pattern recognition.",
        "This picture has patterns! Click on all the parts that repeat.",
        {
            "item_count": 12,
            "interaction_mode": "click_items",
            "visual_theme": "patterns",
            "estimated_time_minutes": 5,
            "randomization": {"enabled": True, "randomize_items": True}
        },
        {
            "type": "selection_set",
            "correct_answer": ["all_repeating_units"],
            "partial_credit": {"enabled": True, "rules": [{"condition": "75% correct", "credit_percentage": 75}]},
            "feedback": {
                "correct": {"message": "Amazing! You found all the patterns!", "audio_tts": "Amazing! You found all the parts that repeat!", "visual_effect": "confetti"},
                "incorrect": {"message": "Good start! Are there more patterns?", "audio_tts": "Good start! Look again - are there more patterns?", "hint_provided": True, "hint_text": "Look for different groups that repeat!"}
            },
            "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": False}
        },
        "Redesigned from G2.01 (identify repeating sections) to complex pattern identification"
    ))

    skills.append(create_skill(
        "T04", "2", 2,
        "Short-Cut the Repeat: Circle It Once",
        "Identify what to repeat instead of showing multiple times",
        "click_select",
        "Students identify the core unit that could be repeated instead of showing it many times, bridging to loop concept.",
        "These steps happen 3 times! Circle just one group that repeats.",
        {
            "item_count": 12,
            "interaction_mode": "click_items",
            "visual_theme": "patterns",
            "estimated_time_minutes": 4,
            "difficulty_parameters": {"visual_complexity": "medium"},
            "randomization": {"enabled": True}
        },
        {
            "type": "selection_set",
            "correct_answer": ["repeating_unit"],
            "partial_credit": {"enabled": False},
            "feedback": {
                "correct": {"message": "Perfect! That's what repeats!", "audio_tts": "Perfect! Instead of showing it 3 times, we could just say repeat this!", "visual_effect": "stars"},
                "incorrect": {"message": "Try again! Find what happens over and over.", "audio_tts": "Try again! Find the group that happens over and over.", "hint_provided": True, "hint_text": "Look for the same steps happening again and again!"}
            },
            "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": False}
        },
        "Redesigned from G2.02 (replace with loop) - bridges to loop concept through visual shortcut"
    ))

    skills.append(create_skill(
        "T04", "2", 3,
        "Customize the Template",
        "Modify template while keeping structure",
        "drag_drop_sequence",
        "Students start with a template pattern and customize it by changing specific elements while keeping the overall structure, understanding templates as reusable frameworks.",
        "Change the colors but keep the same pattern!",
        {
            "item_count": 6,
            "interaction_mode": "drag_to_slots",
            "visual_theme": "patterns",
            "estimated_time_minutes": 5,
            "randomization": {"enabled": False}
        },
        {
            "type": "pattern_completion",
            "correct_answer": "valid_customized_pattern",
            "partial_credit": {"enabled": True, "rules": [{"condition": "structure preserved", "credit_percentage": 80}]},
            "feedback": {
                "correct": {"message": "Great! You kept the pattern but made it your own!", "audio_tts": "Great! You kept the same pattern but changed the colors!", "visual_effect": "confetti"},
                "incorrect": {"message": "Almost! Keep the same repeating structure.", "audio_tts": "Almost! Remember to keep the same repeating structure.", "hint_provided": True, "hint_text": "The pattern should still be ABC ABC, just with different items!"}
            },
            "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": True}
        },
        "Redesigned from G2.03 (use template project) to visual template customization"
    ))

    skills.append(create_skill(
        "T04", "2", 4,
        "Pattern Prediction: What Will It Make?",
        "Predict result of repeating pattern",
        "multiple_choice_visual",
        "Students view a small repeating pattern and predict what it will look like when repeated many times, building mental model of iteration.",
        "If we repeat this pattern 5 times, what will it look like?",
        {
            "item_count": 4,
            "interaction_mode": "click_items",
            "visual_theme": "patterns",
            "estimated_time_minutes": 5,
            "randomization": {"enabled": True, "randomize_items": True}
        },
        {
            "type": "single_choice",
            "correct_answer": "repeated_result",
            "partial_credit": {"enabled": False},
            "feedback": {
                "correct": {"message": "Correct! That's what it makes!", "audio_tts": "Correct! When you repeat the pattern, it makes that!", "visual_effect": "stars"},
                "incorrect": {"message": "Try again! Count how many times it repeats.", "audio_tts": "Try again! Count how many times the pattern repeats.", "hint_provided": True, "hint_text": "The pattern ABC repeated 5 times makes ABCABCABCABCABC!"}
            },
            "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": False}
        },
        "Redesigned from G2.04 (predict pattern output) to visual iteration prediction"
    ))

    return skills


# Continue with remaining topics...
# Due to length constraints, I'll create the remaining topics in the same systematic way

def create_all_k2_skills() -> List[Dict]:
    """Generate all K-2 redesigned skills for 9 high-priority topics"""
    all_skills = []

    # Add T01 and T04
    all_skills.extend(create_t01_skills())
    all_skills.extend(create_t04_skills())

    # Add remaining topics (T25, T26, T27, T30, T32, T34, T35)
    # Each following the same pattern: K=4 new skills, G1=3-4 redesigned, G2=4-5 redesigned

    # For brevity, I'll create compact versions of remaining topics
    # In production, each would have full detailed specifications like T01 and T04

    return all_skills


if __name__ == "__main__":
    print("Generating K-2 Picture-Based Skills...")
    print("=" * 60)

    # Generate skills
    skills = create_all_k2_skills()

    # Count by topic and grade
    topic_counts = {}
    for skill in skills:
        topic = skill['topic_id']
        grade = skill['grade']
        key = f"{topic}_G{grade}"
        topic_counts[key] = topic_counts.get(key, 0) + 1

    print(f"\nGenerated {len(skills)} skills so far (T01 and T04 complete)")
    print("\nBreakdown:")
    for key in sorted(topic_counts.keys()):
        print(f"  {key}: {topic_counts[key]} skills")

    # Save partial output
    output_path = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skills_k2_redesigned_partial.json'
    with open(output_path, 'w') as f:
        json.dump(skills, f, indent=2)

    print(f"\nPartial output saved to: {output_path}")
    print("\nNote: This is T01 and T04. Remaining 7 topics to be completed.")
