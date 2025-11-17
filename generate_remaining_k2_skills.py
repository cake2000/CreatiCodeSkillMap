#!/usr/bin/env python3
"""
Complete K-2 Skills Generation for Remaining Topics (T25-T35)
Generates skills following the same framework as T01 and T04
"""

import json
import sys

# Load the partial file
with open('skills_k2_redesigned_partial.json', 'r') as f:
    existing_skills = json.load(f)

# Import base functions from generate_k2_skills
sys.path.insert(0, '.')
from generate_k2_skills import create_skill, CSTA_CODES

def create_t25_skills():
    """T25: Data Representation"""
    skills = []

    # Kindergarten - 4 skills
    skills.extend([
        create_skill("T25", "K", 1, "Sort by Color", "Sort objects by single attribute (color)",
                    "sort_categories", "Students sort colored objects into matching color bins, learning data organization by single attribute.",
                    "Drag each toy to the bin with the same color!",
                    {"item_count": 6, "interaction_mode": "drag_to_containers", "visual_theme": "toys", "estimated_time_minutes": 2},
                    {"type": "category_match", "correct_answer": {"red_items": "red_bin", "blue_items": "blue_bin"},
                     "partial_credit": {"enabled": False}, "feedback": {"correct": {"message": "Perfect sorting!", "audio_tts": "Perfect! You sorted all the colors!", "visual_effect": "stars"},
                     "incorrect": {"message": "Try again! Match the colors.", "audio_tts": "Try again! Put each toy in the bin with the same color.", "hint_provided": True}},
                     "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": True}},
                    "NEW K skill - single attribute sorting"),

        create_skill("T25", "K", 2, "Big or Small?", "Sort by size attribute",
                    "sort_categories", "Students sort items into big and small categories, understanding classification by size.",
                    "Put the big things here and the small things there!",
                    {"item_count": 6, "interaction_mode": "drag_to_containers", "visual_theme": "toys", "estimated_time_minutes": 2},
                    {"type": "category_match", "correct_answer": {"big": "big_bin", "small": "small_bin"},
                     "partial_credit": {"enabled": False}, "feedback": {"correct": {"message": "Great! You know big and small!", "audio_tts": "Great! You sorted big and small!", "visual_effect": "stars"},
                     "incorrect": {"message": "Look again. Which are bigger?", "audio_tts": "Look again. Which ones are bigger?", "hint_provided": True}},
                     "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": True}},
                    "NEW K skill - size classification"),

        create_skill("T25", "K", 3, "What Kind Is It?", "Sort by type/category",
                    "sort_categories", "Students sort items by type (animals vs toys vs food), learning categorical classification.",
                    "Put each picture where it belongs!",
                    {"item_count": 6, "interaction_mode": "drag_to_containers", "visual_theme": "mixed", "estimated_time_minutes": 3},
                    {"type": "category_match", "correct_answer": {"animals": "animal_bin", "toys": "toy_bin", "food": "food_bin"},
                     "partial_credit": {"enabled": False}, "feedback": {"correct": {"message": "Perfect! You know the groups!", "audio_tts": "Perfect! You put everything in the right group!", "visual_effect": "confetti"},
                     "incorrect": {"message": "Try again! What kind of thing is it?", "audio_tts": "Try again! Is it an animal, a toy, or food?", "hint_provided": True}},
                     "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": True}},
                    "NEW K skill - type categorization"),

        create_skill("T25", "K", 4, "Count and Compare", "Count items and identify which has more",
                    "click_select", "Students count items in two groups and click on the group with more, introducing quantitative comparison.",
                    "Which group has more? Click on it!",
                    {"item_count": 2, "interaction_mode": "click_items", "visual_theme": "toys", "estimated_time_minutes": 2},
                    {"type": "single_choice", "correct_answer": "larger_group",
                     "partial_credit": {"enabled": False}, "feedback": {"correct": {"message": "Yes! That group has more!", "audio_tts": "Yes! That group has more!", "visual_effect": "stars"},
                     "incorrect": {"message": "Count again! Which has more?", "audio_tts": "Count again! Which group has more?", "hint_provided": True}},
                     "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": False}},
                    "NEW K skill - quantitative comparison")
    ])

    # Grade 1 - 4 skills (redesigned)
    skills.extend([
        create_skill("T25", "1", 1, "Sort by Two Things", "Multi-attribute classification",
                    "sort_categories", "Students sort items considering two attributes (e.g., color AND size), advancing classification skills.",
                    "Sort by color AND size! Put them in the right boxes.",
                    {"item_count": 8, "interaction_mode": "drag_to_containers", "visual_theme": "shapes", "estimated_time_minutes": 4},
                    {"type": "category_match", "correct_answer": {"big_red": "br_box", "big_blue": "bb_box", "small_red": "sr_box", "small_blue": "sb_box"},
                     "partial_credit": {"enabled": False}, "feedback": {"correct": {"message": "Amazing! You sorted by both!", "audio_tts": "Amazing! You sorted by both color and size!", "visual_effect": "confetti"},
                     "incorrect": {"message": "Check the color AND the size!", "audio_tts": "Check both the color and the size!", "hint_provided": True}},
                     "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": True}},
                    "Redesigned from G1.01 - picture-based multi-attribute sorting"),

        create_skill("T25", "1", 2, "More, Less, or Same?", "Compare quantities visually",
                    "click_select", "Students compare groups of items and identify relationships (more, less, same).",
                    "Look at both groups. Are there more, less, or the same? Click your answer!",
                    {"item_count": 3, "interaction_mode": "click_items", "visual_theme": "toys", "estimated_time_minutes": 3},
                    {"type": "single_choice", "correct_answer": "correct_comparison",
                     "partial_credit": {"enabled": False}, "feedback": {"correct": {"message": "Correct! You compared them!", "audio_tts": "Correct! You compared the groups!", "visual_effect": "stars"},
                     "incorrect": {"message": "Count both groups carefully!", "audio_tts": "Count both groups carefully!", "hint_provided": True}},
                     "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": False}},
                    "Redesigned from G1.02 - visual quantitative comparison"),

        create_skill("T25", "1", 3, "Numbers Tell Us Things", "Recognize numeric vs non-numeric data",
                    "sort_categories", "Students sort cards showing numbers vs other information, understanding numeric data.",
                    "Put the number cards in one box and the other cards in the other box!",
                    {"item_count": 8, "interaction_mode": "drag_to_containers", "visual_theme": "data", "estimated_time_minutes": 3},
                    {"type": "category_match", "correct_answer": {"numbers": "number_box", "other": "other_box"},
                     "partial_credit": {"enabled": False}, "feedback": {"correct": {"message": "Great! You know numbers!", "audio_tts": "Great! You sorted the numbers!", "visual_effect": "stars"},
                     "incorrect": {"message": "Which ones are numbers?", "audio_tts": "Which ones show numbers?", "hint_provided": True}},
                     "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": True}},
                    "Redesigned from G1.03 - visual numeric recognition"),

        create_skill("T25", "1", 4, "Make a Picture Chart", "Create simple tally/picture chart",
                    "drag_drop_sequence", "Students drag pictures to create a simple picture chart showing survey results.",
                    "Make a chart! Drag one picture for each person's answer.",
                    {"item_count": 8, "items": ["Picture symbols for chart"], "interaction_mode": "drag_to_slots", "visual_theme": "data", "estimated_time_minutes": 4},
                    {"type": "category_match", "correct_answer": "correct_chart_representation",
                     "partial_credit": {"enabled": False}, "feedback": {"correct": {"message": "Perfect chart!", "audio_tts": "Perfect! Your chart shows the data!", "visual_effect": "confetti"},
                     "incorrect": {"message": "Check how many said each answer!", "audio_tts": "Check how many people said each answer!", "hint_provided": True}},
                     "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": True}},
                    "Redesigned from G1.04 - picture chart creation")
    ])

    # Grade 2 - 5 skills (redesigned with bridge activities)
    skills.extend([
        create_skill("T25", "2", 1, "Number or Not?", "Classify data types",
                    "yes_no_sort", "Students classify various data as numeric or non-numeric, building data type awareness.",
                    "Is it a number? Yes or No?",
                    {"item_count": 8, "interaction_mode": "drag_to_containers", "visual_theme": "data", "estimated_time_minutes": 4},
                    {"type": "binary_classification", "correct_answer": {"numbers": "yes", "other": "no"},
                     "partial_credit": {"enabled": True, "rules": [{"condition": "75% correct", "credit_percentage": 75}]},
                     "feedback": {"correct": {"message": "Excellent! You know data types!", "audio_tts": "Excellent! You know which data is numbers!", "visual_effect": "stars"},
                     "incorrect": {"message": "Think about which ones are numbers!", "audio_tts": "Think about which ones are counting numbers!", "hint_provided": True}},
                     "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": True}},
                    "Redesigned from G2.01 - bridges to data types concept"),

        create_skill("T25", "2", 2, "Make a Variable Box", "Understand variable as storage",
                    "drag_drop_sequence", "Students drag a value into a labeled 'variable box', understanding variables as named storage. Bridges to coding concept.",
                    "Put the score in the Score box! This is like a variable in coding.",
                    {"item_count": 5, "items": ["Value cards to store"], "interaction_mode": "drag_to_slots", "visual_theme": "data", "estimated_time_minutes": 4},
                    {"type": "category_match", "correct_answer": "correct_variable_assignment",
                     "partial_credit": {"enabled": False}, "feedback": {"correct": {"message": "Perfect! That's how variables work!", "audio_tts": "Perfect! Variables in coding work just like that!", "visual_effect": "confetti"},
                     "incorrect": {"message": "Which number goes in which box?", "audio_tts": "Which number goes in which box?", "hint_provided": True}},
                     "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": True}},
                    "Redesigned from G2.02 - bridges to variable concept through pictures"),

        create_skill("T25", "2", 3, "What Can Change? What Stays the Same?", "Identify variable vs constant",
                    "sort_categories", "Students sort data into 'changes' vs 'stays same' categories, understanding variable vs constant concept.",
                    "Sort these: Which ones change? Which stay the same?",
                    {"item_count": 8, "interaction_mode": "drag_to_containers", "visual_theme": "data", "estimated_time_minutes": 4},
                    {"type": "category_match", "correct_answer": {"variables": "changes_bin", "constants": "same_bin"},
                     "partial_credit": {"enabled": True, "rules": [{"condition": "75% correct", "credit_percentage": 75}]},
                     "feedback": {"correct": {"message": "Great thinking!", "audio_tts": "Great! You know what changes and what stays the same!", "visual_effect": "stars"},
                     "incorrect": {"message": "Think about what could be different!", "audio_tts": "Think about what could be different each time!", "hint_provided": True}},
                     "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": True}},
                    "Redesigned from G2.03 - variable vs constant through scenarios"),

        create_skill("T25", "2", 4, "Track the Score!", "Use variable to track changing data",
                    "drag_drop_sequence", "Students update a 'score variable' as events happen, understanding how variables track changing information.",
                    "Update the score after each event! Drag the new score.",
                    {"item_count": 6, "items": ["Score values"], "interaction_mode": "drag_to_slots", "visual_theme": "games", "estimated_time_minutes": 5},
                    {"type": "sequence_order", "correct_answer": ["score1", "score2", "score3", "score4"],
                     "partial_credit": {"enabled": True, "rules": [{"condition": "75% correct", "credit_percentage": 75}]},
                     "feedback": {"correct": {"message": "Perfect! You tracked the score!", "audio_tts": "Perfect! You tracked how the score changed!", "visual_effect": "confetti"},
                     "incorrect": {"message": "Check what happened after each event!", "audio_tts": "Check what happened to the score after each event!", "hint_provided": True}},
                     "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": True}},
                    "Redesigned from G2.04 - variable tracking through game scenario"),

        create_skill("T25", "2", 5, "Make a Simple Table", "Organize data into rows and columns",
                    "drag_drop_sequence", "Students drag data cards into a simple 2-column table, organizing collected data.",
                    "Put the data in the table! Each row is one person.",
                    {"item_count": 8, "items": ["Data cards"], "interaction_mode": "drag_to_slots", "visual_theme": "data", "estimated_time_minutes": 5},
                    {"type": "category_match", "correct_answer": "correct_table_organization",
                     "partial_credit": {"enabled": True, "rules": [{"condition": "75% correct", "credit_percentage": 75}]},
                     "feedback": {"correct": {"message": "Excellent table!", "audio_tts": "Excellent! Your table is organized perfectly!", "visual_effect": "stars"},
                     "incorrect": {"message": "Check which column each data goes in!", "audio_tts": "Check which column each piece of data goes in!", "hint_provided": True}},
                     "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": True}},
                    "Redesigned from G2.05 - table organization")
    ])

    return skills


def create_t26_skills():
    """T26: Data Collection & Organization"""
    skills = []

    # K - 4 skills, G1 - 3 skills, G2 - 4 skills (matching original)
    # (Similar pattern - implementing key skills)

    skills.extend([
        # K.01-04
        create_skill("T26", "K", 1, "Ask and Count", "Collect data by asking yes/no question",
                    "counting_interaction", "Students click to count responses to a simple yes/no question shown in pictures.",
                    "Count how many said YES!",
                    {"item_count": 5, "interaction_mode": "click_items", "visual_theme": "school", "estimated_time_minutes": 2},
                    {"type": "single_choice", "correct_answer": "correct_count",
                     "partial_credit": {"enabled": False}, "feedback": {"correct": {"message": "You counted right!", "audio_tts": "You counted right!", "visual_effect": "stars"},
                     "incorrect": {"message": "Count again!", "audio_tts": "Count again!", "hint_provided": True}},
                     "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": False}},
                    "NEW K skill - basic data collection"),

        create_skill("T26", "K", 2, "Which Has More?", "Compare two data groups",
                    "click_select", "Students compare two groups of collected data and identify which has more.",
                    "Which color did more people pick? Click on it!",
                    {"item_count": 2, "interaction_mode": "click_items", "visual_theme": "data", "estimated_time_minutes": 2},
                    {"type": "single_choice", "correct_answer": "larger_group",
                     "partial_credit": {"enabled": False}, "feedback": {"correct": {"message": "Correct! More people picked that!", "audio_tts": "Correct! More people picked that one!", "visual_effect": "stars"},
                     "incorrect": {"message": "Count both colors!", "audio_tts": "Count both colors!", "hint_provided": True}},
                     "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": False}},
                    "NEW K skill - data comparison"),

        create_skill("T26", "K", 3, "Make a List", "Create list from collected data",
                    "drag_drop_sequence", "Students drag response pictures to make a simple list of answers.",
                    "Make a list! Drag each person's answer.",
                    {"item_count": 4, "items": ["Answer cards"], "interaction_mode": "drag_to_slots", "visual_theme": "data", "estimated_time_minutes": 3},
                    {"type": "sequence_order", "correct_answer": ["item1", "item2", "item3", "item4"],
                     "partial_credit": {"enabled": False}, "feedback": {"correct": {"message": "Great list!", "audio_tts": "Great! You made a list of all the answers!", "visual_effect": "confetti"},
                     "incorrect": {"message": "Put each answer in order!", "audio_tts": "Put each answer in the list!", "hint_provided": True}},
                     "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": True}},
                    "NEW K skill - list making"),

        create_skill("T26", "K", 4, "Take a Survey: Click Your Choice", "Participate in data collection",
                    "click_select", "Students click their answer to a simple survey question, understanding data collection participation.",
                    "What's your favorite? Click on it!",
                    {"item_count": 3, "interaction_mode": "click_items", "visual_theme": "food", "estimated_time_minutes": 2},
                    {"type": "single_choice", "correct_answer": "any_valid_choice",
                     "partial_credit": {"enabled": False}, "feedback": {"correct": {"message": "Thanks for answering!", "audio_tts": "Thanks for answering the survey!", "visual_effect": "stars"},
                     "incorrect": {"message": "", "audio_tts": "", "hint_provided": False}},
                     "retry_logic": {"max_attempts": 1, "show_correct_answer": False, "reset_on_retry": False}},
                    "NEW K skill - survey participation"),

        # G1.01-03
        create_skill("T26", "1", 1, "Ask the Class", "Collect data from multiple responses",
                    "counting_interaction", "Students count responses from a class survey shown visually.",
                    "Count: How many picked each snack?",
                    {"item_count": 8, "interaction_mode": "click_items", "visual_theme": "food", "estimated_time_minutes": 3},
                    {"type": "category_match", "correct_answer": "correct_counts",
                     "partial_credit": {"enabled": False}, "feedback": {"correct": {"message": "Perfect counting!", "audio_tts": "Perfect! You counted all the responses!", "visual_effect": "stars"},
                     "incorrect": {"message": "Count each group carefully!", "audio_tts": "Count each group carefully!", "hint_provided": True}},
                     "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": False}},
                    "Redesigned from G1.01 - visual survey counting"),

        create_skill("T26", "1", 2, "Compare the Data", "Compare multiple data groups",
                    "click_select", "Students compare three groups of data and answer questions about them.",
                    "Which snack got the most votes? Click on it!",
                    {"item_count": 3, "interaction_mode": "click_items", "visual_theme": "data", "estimated_time_minutes": 3},
                    {"type": "single_choice", "correct_answer": "most_popular",
                     "partial_credit": {"enabled": False}, "feedback": {"correct": {"message": "Yes! That got the most!", "audio_tts": "Yes! That snack got the most votes!", "visual_effect": "stars"},
                     "incorrect": {"message": "Count each group!", "audio_tts": "Count how many voted for each snack!", "hint_provided": True}},
                     "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": False}},
                    "Redesigned from G1.02 - data comparison"),

        create_skill("T26", "1", 3, "Make the List", "Organize collected data into list",
                    "drag_drop_sequence", "Students drag data items to organize collected information into a list.",
                    "Put the data in a list! Drag them in order.",
                    {"item_count": 6, "items": ["Data cards"], "interaction_mode": "drag_to_slots", "visual_theme": "data", "estimated_time_minutes": 4},
                    {"type": "sequence_order", "correct_answer": "organized_list",
                     "partial_credit": {"enabled": False}, "feedback": {"correct": {"message": "Great organization!", "audio_tts": "Great! You organized the data in a list!", "visual_effect": "confetti"},
                     "incorrect": {"message": "Check the order!", "audio_tts": "Check if you have all the data!", "hint_provided": True}},
                     "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": True}},
                    "Redesigned from G1.03 - list organization"),

        # G2.01-04
        create_skill("T26", "2", 1, "Collect by Watching", "Observation-based data collection",
                    "counting_interaction", "Students count occurrences in a scene (observation data collection).",
                    "Watch the playground. Count how many kids use each toy!",
                    {"item_count": 10, "interaction_mode": "click_items", "visual_theme": "school", "estimated_time_minutes": 4},
                    {"type": "category_match", "correct_answer": "correct_observation_counts",
                     "partial_credit": {"enabled": True, "rules": [{"condition": "75% correct", "credit_percentage": 75}]},
                     "feedback": {"correct": {"message": "Great observing!", "audio_tts": "Great! You observed and counted carefully!", "visual_effect": "stars"},
                     "incorrect": {"message": "Look carefully at the picture!", "audio_tts": "Look carefully at each part of the picture!", "hint_provided": True}},
                     "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": False}},
                    "Redesigned from G2.01 - observation data collection"),

        create_skill("T26", "2", 2, "Fill the Table", "Organize data into table structure",
                    "drag_drop_sequence", "Students drag data into a simple two-column table.",
                    "Fill in the table! Drag each data piece to the right spot.",
                    {"item_count": 8, "items": ["Data cards"], "interaction_mode": "drag_to_slots", "visual_theme": "data", "estimated_time_minutes": 5},
                    {"type": "category_match", "correct_answer": "correct_table",
                     "partial_credit": {"enabled": True, "rules": [{"condition": "75% correct", "credit_percentage": 75}]},
                     "feedback": {"correct": {"message": "Perfect table!", "audio_tts": "Perfect! Your table is organized well!", "visual_effect": "confetti"},
                     "incorrect": {"message": "Check which column it goes in!", "audio_tts": "Check which column each data goes in!", "hint_provided": True}},
                     "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": True}},
                    "Redesigned from G2.02 - table organization"),

        create_skill("T26", "2", 3, "Survey the Class", "Design and understand survey",
                    "click_select", "Students choose which question would make a good survey for the class.",
                    "Which question is best for a class survey? Click on it!",
                    {"item_count": 3, "interaction_mode": "click_items", "visual_theme": "school", "estimated_time_minutes": 4},
                    {"type": "single_choice", "correct_answer": "good_survey_question",
                     "partial_credit": {"enabled": False}, "feedback": {"correct": {"message": "Great choice!", "audio_tts": "Great! That's a good survey question!", "visual_effect": "stars"},
                     "incorrect": {"message": "Think about what everyone could answer!", "audio_tts": "Think about what question everyone could answer!", "hint_provided": True}},
                     "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": False}},
                    "Redesigned from G2.03 - survey design understanding"),

        create_skill("T26", "2", 4, "Find What's Missing", "Identify incomplete data",
                    "click_select", "Students identify missing or incomplete data in a visual table.",
                    "Look at the table. Click on the missing data!",
                    {"item_count": 8, "interaction_mode": "click_items", "visual_theme": "data", "estimated_time_minutes": 4},
                    {"type": "selection_set", "correct_answer": ["missing_data_cells"],
                     "partial_credit": {"enabled": True, "rules": [{"condition": "75% correct", "credit_percentage": 75}]},
                     "feedback": {"correct": {"message": "You found it!", "audio_tts": "You found all the missing data!", "visual_effect": "stars"},
                     "incorrect": {"message": "Look for empty spots!", "audio_tts": "Look for empty spots or incomplete information!", "hint_provided": True}},
                     "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": False}},
                    "Redesigned from G2.04 - data completeness check")
    ])

    return skills


# Continue with T27, T30, T32, T34, T35...
# (Implementation continues in same pattern)

def create_compact_skills_for_remaining_topics():
    """Create remaining topics T27, T30, T32, T34, T35 in compact form"""
    all_remaining = []

    # T27: Data Analysis - K=4, G1=3, G2=4
    t27_specs = [
        ("K", 1, "Which Pile Has More?", "Visual comparison of quantities", "click_select"),
        ("K", 2, "Count the Pictureseach", "Count and compare picture sets", "counting_interaction"),
        ("K", 3, "Which is Biggest?", "Identify largest group", "click_select"),
        ("K", 4, "Same or Different Amounts?", "Compare for equality", "click_select"),
        ("1", 1, "Read the Picture Chart", "Answer questions from pictograph", "multiple_choice_visual"),
        ("1", 2, "Count Each Group", "Count data in each category", "counting_interaction"),
        ("1", 3, "Which Got the Most?", "Identify mode from visual", "click_select"),
        ("2", 1, "Make a Bar Chart", "Create simple bar chart from data", "drag_drop_sequence"),
        ("2", 2, "Find the Most Popular", "Identify mode/highest count", "click_select"),
        ("2", 3, "More or Fewer?", "Compare data groups", "click_select"),
        ("2", 4, "Add Them All Up", "Find total by adding counts", "multiple_choice_visual"),
    ]

    for grade, num, title, desc, activity in t27_specs:
        all_remaining.append(create_skill(
            "T27", grade, num, title, desc, activity,
            f"Students {desc.lower()} through picture-based interaction.",
            f"{title}!",
            {"item_count": 6 if grade == "K" else 8, "interaction_mode": "click_items" if activity == "click_select" else "drag_to_slots",
             "visual_theme": "data", "estimated_time_minutes": 2 if grade == "K" else 4},
            {"type": "single_choice", "correct_answer": "correct",
             "partial_credit": {"enabled": grade == "2"},
             "feedback": {"correct": {"message": "Great!", "audio_tts": "Great job!", "visual_effect": "stars"},
                         "incorrect": {"message": "Try again!", "audio_tts": "Try again!", "hint_provided": True}},
             "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": False}},
            f"Redesigned for T27.G{grade}.{num:02d}"
        ))

    # T30: Hardware - K=4, G1=4, G2=4
    t30_specs = [
        ("K", 1, "Find the Computer", "Identify computing devices", "click_select"),
        ("K", 2, "What Do We Use It For?", "Match device to use", "match_pairs"),
        ("K", 3, "Is It a Computer?", "Identify computing devices", "yes_no_sort"),
        ("K", 4, "Point to the Screen", "Identify computer parts", "hot_spot_click"),
        ("1", 1, "Match Device to Job", "Match device to purpose", "match_pairs"),
        ("1", 2, "Input or Output?", "Sort input/output devices", "sort_categories"),
        ("1", 3, "Parts of a Computer", "Identify computer components", "hot_spot_click"),
        ("1", 4, "Software Makes It Work", "Match software to device", "match_pairs"),
        ("2", 1, "Choose the Right Tool", "Select appropriate software", "click_select"),
        ("2", 2, "Input to Output", "Understand processing flow", "drag_drop_sequence"),
        ("2", 3, "What Does This Sensor Do?", "Identify sensor purposes", "match_pairs"),
        ("2", 4, "Hardware Plus Software", "Connect hardware and software", "match_pairs"),
    ]

    for grade, num, title, desc, activity in t30_specs:
        all_remaining.append(create_skill(
            "T30", grade, num, title, desc, activity,
            f"Students {desc.lower()} through picture-based interaction.",
            f"{title}!",
            {"item_count": 4 if grade == "K" else 6, "interaction_mode": "click_items",
             "visual_theme": "technology", "estimated_time_minutes": 2 if grade == "K" else 4},
            {"type": "single_choice", "correct_answer": "correct",
             "partial_credit": {"enabled": grade == "2"},
             "feedback": {"correct": {"message": "Correct!", "audio_tts": "Correct!", "visual_effect": "stars"},
                         "incorrect": {"message": "Try again!", "audio_tts": "Try again!", "hint_provided": True}},
             "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": False}},
            f"Redesigned for T30.G{grade}.{num:02d}"
        ))

    # T32: Cybersecurity - K=4, G1=4, G2=4
    t32_specs = [
        ("K", 1, "Private or Not Private?", "Sort personal information", "yes_no_sort"),
        ("K", 2, "Who Can We Tell?", "Identify trusted adults", "click_select"),
        ("K", 3, "Keep Secrets Safe", "Understand privacy", "sort_categories"),
        ("K", 4, "Ask a Grown-Up First", "Identify when to ask adult", "click_select"),
        ("1", 1, "What Should Stay Private?", "Identify PII", "sort_categories"),
        ("1", 2, "Who Can I Trust Online?", "Identify trustworthy people", "click_select"),
        ("1", 3, "Why Passwords Matter", "Understand password purpose", "multiple_choice_visual"),
        ("1", 4, "Spot the Trick", "Identify scam picture", "click_select"),
        ("2", 1, "Keep Information Private", "Privacy practices", "sort_categories"),
        ("2", 2, "Make a Strong Password", "Password creation principles", "click_select"),
        ("2", 3, "Is This Real or Fake?", "Recognize phishing", "click_select"),
        ("2", 4, "Safe Sharing Rules", "Safe online behaviors", "sort_categories"),
    ]

    for grade, num, title, desc, activity in t32_specs:
        all_remaining.append(create_skill(
            "T32", grade, num, title, desc, activity,
            f"Students {desc.lower()} through picture-based scenarios.",
            f"{title}!",
            {"item_count": 5 if grade == "K" else 7, "interaction_mode": "drag_to_containers" if "sort" in activity else "click_items",
             "visual_theme": "digital_citizenship", "estimated_time_minutes": 2 if grade == "K" else 4},
            {"type": "category_match" if "sort" in activity else "single_choice", "correct_answer": "correct",
             "partial_credit": {"enabled": grade == "2"},
             "feedback": {"correct": {"message": "Stay safe!", "audio_tts": "Great! You know how to stay safe!", "visual_effect": "stars"},
                         "incorrect": {"message": "Try again!", "audio_tts": "Try again! Think about staying safe.", "hint_provided": True}},
             "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": True}},
            f"Redesigned for T32.G{grade}.{num:02d}"
        ))

    # T34: History - K=4, G1=4, G2=4
    t34_specs = [
        ("K", 1, "Old or New?", "Sort old vs new technology", "sort_categories"),
        ("K", 2, "Before and After", "Sequence technology evolution", "drag_drop_sequence"),
        ("K", 3, "Match Old to New", "Match old and new versions", "match_pairs"),
        ("K", 4, "How Did People Do It Before?", "Compare past and present", "click_select"),
        ("1", 1, "Technology from Different Places", "Explore diverse contributions", "click_select"),
        ("1", 2, "Life Before and After", "Compare life before/after tech", "sort_categories"),
        ("1", 3, "Name the Inventor", "Match inventor to invention", "match_pairs"),
        ("1", 4, "Draw an Invention", "Identify inventions visually", "click_select"),
        ("2", 1, "How Life Changed", "Compare daily life", "sort_categories"),
        ("2", 2, "What Does It Help Us Do?", "Identify technology purpose", "match_pairs"),
        ("2", 3, "Good and Bad Changes", "Identify impacts", "sort_categories"),
        ("2", 4, "Technology Timeline", "Sequence inventions chronologically", "drag_drop_sequence"),
    ]

    for grade, num, title, desc, activity in t34_specs:
        all_remaining.append(create_skill(
            "T34", grade, num, title, desc, activity,
            f"Students {desc.lower()} through picture-based interaction.",
            f"{title}!",
            {"item_count": 4 if grade == "K" else 6, "interaction_mode": "drag_to_containers" if "sort" in activity else "click_items",
             "visual_theme": "history", "estimated_time_minutes": 2 if grade == "K" else 4},
            {"type": "category_match" if "sort" in activity else "single_choice", "correct_answer": "correct",
             "partial_credit": {"enabled": grade == "2"},
             "feedback": {"correct": {"message": "Great history thinking!", "audio_tts": "Great! You understand how technology changed!", "visual_effect": "stars"},
                         "incorrect": {"message": "Try again!", "audio_tts": "Try again! Think about the past.", "hint_provided": True}},
             "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": True}},
            f"Redesigned for T34.G{grade}.{num:02d}"
        ))

    # T35: Impacts - K=4, G1=4, G2=4
    t35_specs = [
        ("K", 1, "Good or Problem?", "Sort technology effects", "sort_categories"),
        ("K", 2, "Too Much Screen Time?", "Understand balance", "click_select"),
        ("K", 3, "Who Made This Game?", "Recognize human creators", "multiple_choice_visual"),
        ("K", 4, "When to Use It, When Not To", "Appropriate device use", "sort_categories"),
        ("1", 1, "Good and Bad Effects", "List technology impacts", "sort_categories"),
        ("1", 2, "What If I Play Too Long?", "Predict consequences", "click_select"),
        ("1", 3, "People Make Games", "Understand human design", "multiple_choice_visual"),
        ("1", 4, "Device or No Device?", "Decide appropriate use", "click_select"),
        ("2", 1, "Before and After Tech", "Compare life impacts", "sort_categories"),
        ("2", 2, "How Could This Help?", "Brainstorm benefits", "click_select"),
        ("2", 3, "Unexpected Problems", "Identify unintended impacts", "click_select"),
        ("2", 4, "Different Communities, Different Uses", "Understand diverse usage", "match_pairs"),
    ]

    for grade, num, title, desc, activity in t35_specs:
        all_remaining.append(create_skill(
            "T35", grade, num, title, desc, activity,
            f"Students {desc.lower()} through picture-based scenarios.",
            f"{title}!",
            {"item_count": 5 if grade == "K" else 7, "interaction_mode": "drag_to_containers" if "sort" in activity else "click_items",
             "visual_theme": "impacts", "estimated_time_minutes": 2 if grade == "K" else 4},
            {"type": "category_match" if "sort" in activity else "single_choice", "correct_answer": "correct",
             "partial_credit": {"enabled": grade == "2"},
             "feedback": {"correct": {"message": "Great thinking!", "audio_tts": "Great! You understand technology impacts!", "visual_effect": "stars"},
                         "incorrect": {"message": "Try again!", "audio_tts": "Try again! Think about how technology affects us.", "hint_provided": True}},
             "retry_logic": {"max_attempts": 3, "show_correct_answer": True, "reset_on_retry": True}},
            f"Redesigned for T35.G{grade}.{num:02d}"
        ))

    return all_remaining


if __name__ == "__main__":
    print("Generating Remaining K-2 Skills (T25-T35)...")
    print("=" * 60)

    # Generate all remaining skills
    all_skills = []
    all_skills.extend(create_t25_skills())
    all_skills.extend(create_t26_skills())
    all_skills.extend(create_compact_skills_for_remaining_topics())

    # Combine with existing T01 and T04
    all_skills = existing_skills + all_skills

    # Count by topic and grade
    topic_counts = {}
    for skill in all_skills:
        topic = skill['topic_id']
        grade = skill['grade']
        key = f"{topic}_G{grade}"
        topic_counts[key] = topic_counts.get(key, 0) + 1

    print(f"\nTotal skills generated: {len(all_skills)}")
    print("\nBreakdown by Topic and Grade:")
    for topic in ['T01', 'T04', 'T25', 'T26', 'T27', 'T30', 'T32', 'T34', 'T35']:
        k_count = topic_counts.get(f"{topic}_GK", 0)
        g1_count = topic_counts.get(f"{topic}_G1", 0)
        g2_count = topic_counts.get(f"{topic}_G2", 0)
        total = k_count + g1_count + g2_count
        print(f"  {topic}: K={k_count}, G1={g1_count}, G2={g2_count} (Total: {total})")

    # Save complete output
    output_path = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skills_k2_redesigned.json'
    with open(output_path, 'w') as f:
        json.dump(all_skills, f, indent=2)

    print(f"\n✓ Complete redesigned K-2 skills saved to: {output_path}")
    print(f"✓ Total: {len(all_skills)} picture-based K-2 skills")
