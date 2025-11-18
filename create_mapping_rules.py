#!/usr/bin/env python3
"""
Create comprehensive mapping rules from CreatiCode topics to CSTA standards.
This includes both automated rule-based mappings and manual assignments.
"""
import json

# Load CSTA standards
with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/csta_standards_extracted.json', 'r') as f:
    csta_data = json.load(f)

# Load skills to analyze existing patterns
with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/skills_k8_ai_complete.json', 'r') as f:
    skills = json.load(f)

# Create comprehensive mapping rules
# Structure: topic_id -> grade_range -> primary/secondary CSTA codes

mapping_rules = {
    "metadata": {
        "version": "1.0",
        "created": "2025-11-17",
        "description": "Mapping rules from CreatiCode K-8 topics to CSTA standards",
        "usage": "Apply grade-specific rules first, then fall back to topic-level defaults"
    },

    "topic_mappings": {
        # D1: Algorithms & Design (T01-T05)
        "T01": {
            "name": "Algorithms (Sequencing, Planning, Algorithms)",
            "primary_csta_area": "ALG-AF",
            "secondary_csta_areas": ["PRO-PF"],
            "grade_mappings": {
                "K": ["EK-ALG-AF-01"],
                "1": ["E1-ALG-AF-01"],
                "2": ["E2-ALG-AF-01"],
                "3": ["E3-ALG-AF-01", "E3-PRO-PF-01"],
                "4": ["E4-ALG-AF-01", "E4-PRO-PF-01"],
                "5": ["E5-ALG-AF-01", "E5-PRO-PF-01"],
                "6": ["MS-ALG-AF-01", "MS-ALG-AF-02", "MS-PRO-PF-01"],
                "7": ["MS-ALG-AF-01", "MS-ALG-AF-02", "MS-PRO-PF-02"],
                "8": ["MS-ALG-AF-01", "MS-ALG-AF-02", "MS-PRO-PF-03"]
            }
        },

        "T02": {
            "name": "Abstraction & Models",
            "primary_csta_area": "ALG-PS",
            "secondary_csta_areas": ["PRO-PD"],
            "grade_mappings": {
                "K": ["EK-ALG-PS-03"],
                "1": ["E1-ALG-PS-03"],
                "2": ["E2-ALG-PS-03"],
                "3": ["E3-ALG-PS-03"],
                "4": ["E4-ALG-PS-03"],
                "5": ["E5-ALG-PS-03"],
                "6": ["MS-ALG-PS-05", "MS-ALG-PS-07"],
                "7": ["MS-ALG-PS-06", "MS-ALG-PS-07"],
                "8": ["MS-ALG-PS-05", "MS-ALG-PS-06", "MS-ALG-PS-07"]
            }
        },

        "T03": {
            "name": "Decomposition",
            "primary_csta_area": "ALG-PS",
            "secondary_csta_areas": ["PRO-PD"],
            "grade_mappings": {
                "K": ["EK-ALG-PS-03"],
                "1": ["E1-ALG-PS-03"],
                "2": ["E2-ALG-PS-03"],
                "3": ["E3-ALG-PS-03"],
                "4": ["E4-ALG-PS-03"],
                "5": ["E5-ALG-PS-03"],
                "6": ["MS-ALG-PS-05", "MS-PRO-PD-08"],
                "7": ["MS-ALG-PS-06", "MS-PRO-PD-08"],
                "8": ["MS-ALG-PS-07", "MS-PRO-PD-08"]
            }
        },

        "T04": {
            "name": "Pattern Recognition",
            "primary_csta_area": "ALG-AF",
            "secondary_csta_areas": ["ALG-PS"],
            "grade_mappings": {
                "K": ["EK-ALG-AF-01", "EK-ALG-PS-03"],
                "1": ["E1-ALG-AF-01"],
                "2": ["E2-ALG-AF-01", "E2-ALG-PS-03"],
                "3": ["E3-ALG-AF-01"],
                "4": ["E4-ALG-AF-01", "E4-ALG-PS-03"],
                "5": ["E5-ALG-AF-01", "E5-ALG-PS-03"],
                "6": ["MS-ALG-AF-01", "MS-ALG-PS-05"],
                "7": ["MS-ALG-AF-02", "MS-ALG-PS-06"],
                "8": ["MS-ALG-AF-01", "MS-ALG-PS-07"]
            }
        },

        "T05": {
            "name": "Design & Human-Computer Interaction",
            "primary_csta_area": "ALG-HD",
            "secondary_csta_areas": ["SAS-HW"],
            "grade_mappings": {
                "K": ["EK-ALG-HD-02"],
                "1": ["E1-ALG-HD-02", "E1-SAS-HW-01"],
                "2": ["E2-ALG-HD-02", "E2-SAS-HW-01"],
                "3": ["E3-ALG-HD-02"],
                "4": ["E4-ALG-HD-02"],
                "5": ["E5-ALG-HD-02"],
                "6": ["MS-ALG-HD-03"],
                "7": ["MS-ALG-HD-03", "MS-ALG-HD-04"],
                "8": ["MS-ALG-HD-04"]
            }
        },

        # D2: Programming Core (T06-T13)
        "T06": {
            "name": "Events",
            "primary_csta_area": "PRO-PF",
            "secondary_csta_areas": [],
            "grade_mappings": {
                "K": [],  # Picture-based pre-skill
                "1": [],  # Picture-based pre-skill
                "2": ["E2-PRO-PF-01"],  # Bridge skill
                "3": ["E3-PRO-PF-01"],
                "4": ["E4-PRO-PF-01"],
                "5": ["E5-PRO-PF-01"],
                "6": ["MS-PRO-PF-01", "MS-PRO-PF-02"],
                "7": ["MS-PRO-PF-01", "MS-PRO-PF-02"],
                "8": ["MS-PRO-PF-01", "MS-PRO-PF-03"]
            }
        },

        "T07": {
            "name": "Loops",
            "primary_csta_area": "PRO-PF",
            "secondary_csta_areas": ["ALG-AF"],
            "grade_mappings": {
                "K": ["EK-PRO-PF-02"],  # Picture-based iteration concept
                "1": ["E1-PRO-PF-01"],  # Includes iteration
                "2": ["E2-PRO-PF-01", "E2-ALG-PS-03"],  # Iteration in code + recognizing repetition
                "3": ["E3-PRO-PF-01"],
                "4": ["E4-PRO-PF-01"],
                "5": ["E5-PRO-PF-01"],
                "6": ["MS-PRO-PF-01", "MS-PRO-DH-06"],  # Loops + iteration over collections
                "7": ["MS-PRO-PF-02", "MS-PRO-DH-06"],
                "8": ["MS-PRO-PF-03", "MS-PRO-DH-06"]
            }
        },

        "T08": {
            "name": "Conditionals",
            "primary_csta_area": "PRO-PF",
            "secondary_csta_areas": ["ALG-AF"],
            "grade_mappings": {
                "K": [],
                "1": [],
                "2": ["E2-PRO-PF-01"],  # Bridge: includes selection
                "3": ["E3-PRO-PF-01", "E3-PRO-TR-03"],  # Selection + debugging
                "4": ["E4-PRO-PF-01", "E4-PRO-TR-03"],
                "5": ["E5-PRO-PF-01"],
                "6": ["MS-PRO-PF-01", "MS-PRO-PF-02"],
                "7": ["MS-PRO-PF-02"],
                "8": ["MS-PRO-PF-03"]
            }
        },

        "T09": {
            "name": "Variables & Expressions",
            "primary_csta_area": "PRO-DH",
            "secondary_csta_areas": ["PRO-PF"],
            "grade_mappings": {
                "K": [],
                "1": ["E1-PRO-DH-02"],  # Identifying variables in daily life
                "2": ["E2-PRO-DH-02"],  # Labeling variables, constant vs changing
                "3": ["E3-PRO-DH-02", "E3-PRO-PF-01"],  # Identifying and using variables
                "4": ["E4-PRO-DH-02", "E4-PRO-PF-01"],  # Tracing data flow
                "5": ["E5-PRO-DH-02", "E5-PRO-PF-01"],  # Different types of variables
                "6": ["MS-PRO-DH-04", "MS-PRO-DH-05"],  # Data structures and types
                "7": ["MS-PRO-DH-05"],
                "8": ["MS-PRO-DH-04", "MS-PRO-DH-05"]
            }
        },

        "T10": {
            "name": "Lists & Arrays",
            "primary_csta_area": "PRO-DH",
            "secondary_csta_areas": ["DAA-DF"],
            "grade_mappings": {
                "K": [],
                "1": [],
                "2": ["E2-PRO-DH-02"],  # Collections concept
                "3": ["E3-PRO-DH-02"],
                "4": ["E4-PRO-DH-02"],
                "5": ["E5-PRO-DH-02"],
                "6": ["MS-PRO-DH-04", "MS-PRO-DH-06"],  # Collection types + iteration
                "7": ["MS-PRO-DH-04", "MS-PRO-DH-06"],
                "8": ["MS-PRO-DH-04", "MS-PRO-DH-06"]
            }
        },

        "T11": {
            "name": "Functions & Procedures",
            "primary_csta_area": "PRO-PD",
            "secondary_csta_areas": ["ALG-PS"],
            "grade_mappings": {
                "K": [],
                "1": [],
                "2": [],
                "3": [],
                "4": [],
                "5": [],
                "6": ["MS-PRO-PD-08"],  # Create modular programs
                "7": ["MS-PRO-PD-08"],
                "8": ["MS-PRO-PD-08"]
            }
        },

        "T12": {
            "name": "Organization & Modularity",
            "primary_csta_area": "PRO-PD",
            "secondary_csta_areas": ["PRO-PM"],
            "grade_mappings": {
                "K": [],
                "1": [],
                "2": ["E2-PRO-PM-04"],  # Document steps
                "3": ["E3-PRO-PM-05"],  # Articulate function of code
                "4": ["E4-PRO-PM-05"],  # Document with comments
                "5": ["E5-PRO-PM-05"],  # External documentation
                "6": ["MS-PRO-PD-08", "MS-PRO-PM-16"],  # Modular programs + documentation
                "7": ["MS-PRO-PD-08", "MS-PRO-PM-16"],
                "8": ["MS-PRO-PD-08", "MS-PRO-PM-16"]
            }
        },

        "T13": {
            "name": "Debugging & Testing",
            "primary_csta_area": "PRO-TR",
            "secondary_csta_areas": [],
            "grade_mappings": {
                "K": ["EK-PRO-TR-04"],  # Identify errors
                "1": ["E1-PRO-TR-03"],  # Debug sequence and events
                "2": ["E2-PRO-TR-03"],  # Debug iteration
                "3": ["E3-PRO-TR-03", "E3-PRO-TR-04"],  # Debug selection + create alternatives
                "4": ["E4-PRO-TR-03", "E4-PRO-TR-04"],
                "5": ["E5-PRO-TR-03", "E5-PRO-TR-04"],  # Systematic debugging
                "6": ["MS-PRO-TR-11", "MS-PRO-TR-12"],  # Test, debug, document
                "7": ["MS-PRO-TR-11", "MS-PRO-TR-12"],
                "8": ["MS-PRO-TR-11", "MS-PRO-TR-13"]  # AI-generated code accuracy
            }
        },

        # D3: Applications & AI (T14-T24)
        "T14": {
            "name": "2D Games",
            "primary_csta_area": "PRO-PF",
            "secondary_csta_areas": ["ALG-AF", "PRO-PD"],
            "grade_mappings": {
                "K": [],
                "1": [],
                "2": ["E2-PRO-PF-01"],  # Bridge
                "3": ["E3-PRO-PF-01", "E3-ALG-AF-01"],
                "4": ["E4-PRO-PF-01", "E4-ALG-AF-01"],
                "5": ["E5-PRO-PF-01", "E5-ALG-AF-01"],
                "6": ["MS-PRO-PF-02", "MS-ALG-AF-01", "MS-PRO-PD-08"],
                "7": ["MS-PRO-PF-02", "MS-ALG-AF-02", "MS-PRO-PD-08"],
                "8": ["MS-PRO-PF-03", "MS-ALG-AF-01", "MS-PRO-PD-08"]
            }
        },

        "T15": {
            "name": "Animation & Storytelling",
            "primary_csta_area": "PRO-PF",
            "secondary_csta_areas": ["CAS-ET"],
            "grade_mappings": {
                "K": [],
                "1": [],
                "2": [],
                "3": ["E3-PRO-PF-01"],
                "4": ["E4-PRO-PF-01"],
                "5": ["E5-PRO-PF-01"],
                "6": ["MS-PRO-PF-02", "MS-CAS-ET-04"],
                "7": ["MS-PRO-PF-02", "MS-CAS-ET-05"],
                "8": ["MS-PRO-PF-03", "MS-CAS-ET-06"]
            }
        },

        "T16": {
            "name": "UI & Widgets",
            "primary_csta_area": "ALG-HD",
            "secondary_csta_areas": ["PRO-PF"],
            "grade_mappings": {
                "K": [],
                "1": [],
                "2": [],
                "3": ["E3-ALG-HD-02", "E3-PRO-PF-01"],
                "4": ["E4-ALG-HD-02", "E4-PRO-PF-01"],
                "5": ["E5-ALG-HD-02", "E5-PRO-PF-01"],
                "6": ["MS-ALG-HD-03", "MS-PRO-PF-02"],
                "7": ["MS-ALG-HD-04", "MS-PRO-PF-02"],
                "8": ["MS-ALG-HD-04", "MS-PRO-PF-03"]
            }
        },

        "T17": {
            "name": "Physics Simulations",
            "primary_csta_area": "PRO-PF",
            "secondary_csta_areas": ["ALG-AF"],
            "grade_mappings": {
                "K": [],
                "1": [],
                "2": [],
                "3": ["E3-PRO-PF-01"],
                "4": ["E4-PRO-PF-01", "E4-ALG-AF-01"],
                "5": ["E5-PRO-PF-01", "E5-ALG-AF-01"],
                "6": ["MS-PRO-PF-02", "MS-ALG-AF-01"],
                "7": ["MS-PRO-PF-02", "MS-ALG-AF-02"],
                "8": ["MS-PRO-PF-03", "MS-ALG-AF-02"]
            }
        },

        "T18": {
            "name": "3D Graphics & Spatial Reasoning",
            "primary_csta_area": "PRO-PF",
            "secondary_csta_areas": ["ALG-PS"],
            "grade_mappings": {
                "K": [],
                "1": [],
                "2": [],
                "3": ["E3-PRO-PF-01"],
                "4": ["E4-PRO-PF-01"],
                "5": ["E5-PRO-PF-01", "E5-ALG-PS-03"],
                "6": ["MS-PRO-PF-02", "MS-ALG-PS-05"],
                "7": ["MS-PRO-PF-02", "MS-ALG-PS-06"],
                "8": ["MS-PRO-PF-03", "MS-ALG-PS-07"]
            }
        },

        "T19": {
            "name": "Multiplayer & Networking",
            "primary_csta_area": "SAS-NW",
            "secondary_csta_areas": ["PRO-PF"],
            "grade_mappings": {
                "K": [],
                "1": [],
                "2": [],
                "3": ["E3-SAS-NW-02"],
                "4": ["E4-SAS-NW-02"],
                "5": ["E5-SAS-NW-02"],
                "6": ["MS-SAS-NW-04", "MS-SAS-NW-06"],
                "7": ["MS-SAS-NW-05", "MS-SAS-NW-06"],
                "8": ["MS-SAS-NW-05", "MS-SAS-NW-06"]
            }
        },

        "T20": {
            "name": "Algorithmic Art & Creative Coding",
            "primary_csta_area": "PRO-PF",
            "secondary_csta_areas": ["ALG-AF"],
            "grade_mappings": {
                "K": ["EK-PRO-PF-02"],
                "1": ["E1-PRO-PF-01"],
                "2": ["E2-PRO-PF-01"],
                "3": ["E3-PRO-PF-01", "E3-ALG-AF-01"],
                "4": ["E4-PRO-PF-01", "E4-ALG-AF-01"],
                "5": ["E5-PRO-PF-01", "E5-ALG-AF-01"],
                "6": ["MS-PRO-PF-02", "MS-ALG-AF-01"],
                "7": ["MS-PRO-PF-02", "MS-ALG-AF-02"],
                "8": ["MS-PRO-PF-03", "MS-ALG-AF-01"]
            }
        },

        "T21": {
            "name": "AI Media Tools & Creative Assets",
            "primary_csta_area": "CAS-ET",
            "secondary_csta_areas": ["DAA-IM", "ALG-IM"],
            "grade_mappings": {
                "K": [],
                "1": [],
                "2": ["E2-CAS-ET-02"],
                "3": ["E3-CAS-ET-02", "E3-DAA-DI-04"],  # AI models evolve with data
                "4": ["E4-CAS-ET-02", "E4-DAA-DI-03"],  # Training data properties
                "5": ["E5-CAS-ET-02", "E5-DAA-DI-03"],  # Train AI models
                "6": ["MS-CAS-ET-04", "MS-DAA-IM-15"],  # AI design + impacts
                "7": ["MS-CAS-ET-05", "MS-DAA-IM-15"],
                "8": ["MS-CAS-ET-06", "MS-DAA-IM-15"]
            }
        },

        "T22": {
            "name": "AI Chatbots & Information Apps",
            "primary_csta_area": "CAS-ET",
            "secondary_csta_areas": ["DAA-IM", "PRO-PF"],
            "grade_mappings": {
                "K": [],
                "1": [],
                "2": [],
                "3": ["E3-CAS-ET-02"],
                "4": ["E4-CAS-ET-02"],
                "5": ["E5-CAS-ET-02"],
                "6": ["MS-CAS-ET-05", "MS-DAA-IM-15"],
                "7": ["MS-CAS-ET-06", "MS-DAA-IM-15", "MS-PRO-PF-02"],
                "8": ["MS-CAS-ET-07", "MS-DAA-IM-15", "MS-PRO-PF-03"]
            }
        },

        "T23": {
            "name": "AI Voice, Vision & Gesture Interfaces",
            "primary_csta_area": "SAS-HW",
            "secondary_csta_areas": ["CAS-ET", "DAA-IM"],
            "grade_mappings": {
                "K": ["EK-SAS-HW-01"],  # Sensing concepts
                "1": ["E1-SAS-HW-01"],
                "2": ["E2-SAS-HW-01"],
                "3": ["E3-SAS-HW-01"],  # Sensors in environment
                "4": ["E4-SAS-HW-01"],
                "5": ["E5-SAS-HW-01"],
                "6": ["MS-SAS-HW-01", "MS-CAS-ET-05"],
                "7": ["MS-SAS-HW-02", "MS-CAS-ET-06", "MS-DAA-IM-15"],
                "8": ["MS-SAS-HW-03", "MS-CAS-ET-07", "MS-DAA-IM-15"]
            }
        },

        "T24": {
            "name": "XO & AI-Supported Coding Practices",
            "primary_csta_area": "PRO-PD",
            "secondary_csta_areas": ["CAS-ET", "PRO-TR"],
            "grade_mappings": {
                "K": [],
                "1": [],
                "2": [],
                "3": [],
                "4": [],
                "5": [],
                "6": ["MS-PRO-PD-09", "MS-PRO-TR-13"],  # Tools + AI code accuracy
                "7": ["MS-PRO-PD-09", "MS-PRO-TR-13", "MS-CAS-ET-05"],
                "8": ["MS-PRO-PD-09", "MS-PRO-TR-13", "MS-CAS-ET-07"]
            }
        },

        # D4: Data & Analysis (T25-T29)
        "T25": {
            "name": "Data Representation & Types",
            "primary_csta_area": "DAA-DF",
            "secondary_csta_areas": [],
            "grade_mappings": {
                "K": ["EK-DAA-DF-01"],
                "1": ["E1-DAA-DF-01"],
                "2": ["E2-DAA-DF-01"],
                "3": ["E3-DAA-DF-01", "E3-DAA-DF-02"],
                "4": ["E4-DAA-DF-01"],
                "5": ["E5-DAA-DF-01"],
                "6": ["MS-DAA-DF-01", "MS-DAA-DF-03"],
                "7": ["MS-DAA-DF-02", "MS-DAA-DF-04"],
                "8": ["MS-DAA-DF-03", "MS-DAA-DF-04"]
            }
        },

        "T26": {
            "name": "Data Collection & Measurement",
            "primary_csta_area": "DAA-DF",
            "secondary_csta_areas": ["DAA-DI"],
            "grade_mappings": {
                "K": ["EK-DAA-DF-01"],
                "1": ["E1-DAA-DI-02"],  # Investigate questions with data
                "2": ["E2-DAA-DF-01"],
                "3": ["E3-DAA-DF-01"],
                "4": ["E4-DAA-DI-02"],  # Multiple attributes
                "5": ["E5-DAA-DF-01"],
                "6": ["MS-DAA-DF-03", "MS-DAA-DI-08"],
                "7": ["MS-DAA-DF-04", "MS-DAA-DI-09"],
                "8": ["MS-DAA-DF-03", "MS-DAA-DI-08"]
            }
        },

        "T27": {
            "name": "Data Analysis & Visualization",
            "primary_csta_area": "DAA-DI",
            "secondary_csta_areas": ["DAA-DP"],
            "grade_mappings": {
                "K": ["EK-DAA-DI-02"],
                "1": ["E1-DAA-DI-02"],
                "2": ["E2-DAA-DI-02"],  # Different representations
                "3": ["E3-DAA-DI-03"],  # Create visualization + narrative
                "4": ["E4-DAA-DI-02"],
                "5": ["E5-DAA-DI-02"],  # Analyze variability
                "6": ["MS-DAA-DI-09", "MS-DAA-DI-10"],  # Relationships + visualizations
                "7": ["MS-DAA-DP-05", "MS-DAA-DI-10", "MS-DAA-DI-12"],
                "8": ["MS-DAA-DP-07", "MS-DAA-DI-11", "MS-DAA-DI-12"]
            }
        },

        "T28": {
            "name": "Probability & Sampling",
            "primary_csta_area": "DAA-DI",
            "secondary_csta_areas": ["DAA-IM"],
            "grade_mappings": {
                "K": ["EK-DAA-DI-03"],  # Patterns for predictions
                "1": ["E1-DAA-DI-03"],  # Patterns for classification
                "2": ["E2-DAA-DI-03"],  # How computers learn from patterns
                "3": ["E3-DAA-DI-04"],  # AI models evolve
                "4": ["E4-DAA-DI-03"],  # Training data properties
                "5": ["E5-DAA-DI-02", "E5-DAA-DI-03"],  # Variability + train models
                "6": ["MS-DAA-DI-08", "MS-DAA-DI-09"],
                "7": ["MS-DAA-DI-09", "MS-DAA-DI-11"],
                "8": ["MS-DAA-DI-08", "MS-DAA-DI-12"]
            }
        },

        "T29": {
            "name": "Text Analysis & NLP",
            "primary_csta_area": "DAA-DP",
            "secondary_csta_areas": ["DAA-IM", "CAS-ET"],
            "grade_mappings": {
                "K": [],
                "1": [],
                "2": [],
                "3": [],
                "4": [],
                "5": [],
                "6": ["MS-DAA-DP-05", "MS-DAA-IM-15"],
                "7": ["MS-DAA-DP-06", "MS-DAA-IM-15", "MS-CAS-ET-05"],
                "8": ["MS-DAA-DP-07", "MS-DAA-IM-15", "MS-CAS-ET-07"]
            }
        },

        # D5: Systems & Society (T30-T36)
        "T30": {
            "name": "Hardware & Devices",
            "primary_csta_area": "SAS-HW",
            "secondary_csta_areas": [],
            "grade_mappings": {
                "K": ["EK-SAS-HW-01"],
                "1": ["E1-SAS-HW-01"],
                "2": ["E2-SAS-HW-01"],
                "3": ["E3-SAS-HW-01"],
                "4": ["E4-SAS-HW-01"],
                "5": ["E5-SAS-HW-01"],
                "6": ["MS-SAS-HW-01", "MS-SAS-HW-02"],
                "7": ["MS-SAS-HW-02", "MS-SAS-HW-03"],
                "8": ["MS-SAS-HW-01", "MS-SAS-HW-03"]
            }
        },

        "T31": {
            "name": "Internet & Networks",
            "primary_csta_area": "SAS-NW",
            "secondary_csta_areas": [],
            "grade_mappings": {
                "K": [],
                "1": [],
                "2": [],
                "3": ["E3-SAS-NW-02"],
                "4": ["E4-SAS-NW-02"],
                "5": ["E5-SAS-NW-02"],
                "6": ["MS-SAS-NW-04", "MS-SAS-NW-05"],
                "7": ["MS-SAS-NW-05", "MS-SAS-NW-06"],
                "8": ["MS-SAS-NW-04", "MS-SAS-NW-06"]
            }
        },

        "T32": {
            "name": "Privacy & Cybersecurity",
            "primary_csta_area": "SAS-SC",
            "secondary_csta_areas": [],
            "grade_mappings": {
                "K": ["EK-SAS-SC-02"],
                "1": ["E1-SAS-SC-02"],
                "2": ["E2-SAS-SC-02"],
                "3": ["E3-SAS-SC-03"],
                "4": ["E4-SAS-SC-03"],
                "5": ["E5-SAS-SC-03"],
                "6": ["MS-SAS-SC-07", "MS-SAS-SC-08"],
                "7": ["MS-SAS-SC-09", "MS-SAS-SC-10"],
                "8": ["MS-SAS-SC-07", "MS-SAS-SC-09"]
            }
        },

        "T33": {
            "name": "APIs & Cloud Services",
            "primary_csta_area": "SAS-NW",
            "secondary_csta_areas": ["SAS-HW"],
            "grade_mappings": {
                "K": [],
                "1": [],
                "2": [],
                "3": [],
                "4": [],
                "5": [],
                "6": ["MS-SAS-NW-05", "MS-SAS-HW-02"],
                "7": ["MS-SAS-NW-06", "MS-SAS-HW-02"],
                "8": ["MS-SAS-NW-05", "MS-SAS-HW-03"]
            }
        },

        "T34": {
            "name": "History of Computing",
            "primary_csta_area": "CAS-HC",
            "secondary_csta_areas": [],
            "grade_mappings": {
                "K": ["EK-CAS-HC-01"],
                "1": ["E1-CAS-HC-01"],
                "2": ["E2-CAS-HC-01"],
                "3": ["E3-CAS-HC-01"],
                "4": ["E4-CAS-HC-01"],
                "5": ["E5-CAS-HC-01"],
                "6": ["MS-CAS-HC-01", "MS-CAS-HC-02"],
                "7": ["MS-CAS-HC-02", "MS-CAS-HC-03"],
                "8": ["MS-CAS-HC-01", "MS-CAS-HC-03"]
            }
        },

        "T35": {
            "name": "Impacts of Computing, Games & AI",
            "primary_csta_area": "SAS-IM",
            "secondary_csta_areas": ["DAA-IM", "ALG-IM"],
            "grade_mappings": {
                "K": ["EK-SAS-IM-03", "EK-ALG-IM-04"],
                "1": ["E1-SAS-IM-03", "E1-ALG-IM-04"],
                "2": ["E2-SAS-IM-03", "E2-ALG-IM-04"],
                "3": ["E3-SAS-IM-04", "E3-ALG-IM-04"],
                "4": ["E4-SAS-IM-04", "E4-ALG-IM-04"],
                "5": ["E5-SAS-IM-04", "E5-ALG-IM-04"],
                "6": ["MS-SAS-IM-11", "MS-ALG-IM-08", "MS-DAA-IM-15"],
                "7": ["MS-SAS-IM-12", "MS-ALG-IM-09", "MS-DAA-IM-15"],
                "8": ["MS-SAS-IM-11", "MS-ALG-IM-08", "MS-DAA-IM-15"]
            }
        },

        "T36": {
            "name": "Ethics, Careers, Collaboration & Communication",
            "primary_csta_area": "CAS-CE",
            "secondary_csta_areas": ["PRO-PM", "ALG-IM", "DAA-IM"],
            "grade_mappings": {
                "K": ["EK-CAS-CE-03"],
                "1": ["E1-CAS-CE-03"],
                "2": ["E2-CAS-CE-03", "E2-PRO-PM-04"],
                "3": ["E3-CAS-CE-03", "E3-PRO-PM-06"],
                "4": ["E4-CAS-CE-03", "E4-PRO-PM-06"],
                "5": ["E5-CAS-CE-03", "E5-PRO-PM-06"],
                "6": ["MS-CAS-CE-08", "MS-PRO-PM-15", "MS-CAS-CE-10"],
                "7": ["MS-CAS-CE-09", "MS-PRO-PM-16", "MS-CAS-CE-11"],
                "8": ["MS-CAS-CE-08", "MS-PRO-PM-15", "MS-CAS-CE-10"]
            }
        }
    }
}

# Save mapping rules
with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/TOPIC_TO_CSTA_MAPPING_RULES.json', 'w') as f:
    json.dump(mapping_rules, f, indent=2)

print("Created TOPIC_TO_CSTA_MAPPING_RULES.json")

# Generate summary statistics
total_topics = len(mapping_rules['topic_mappings'])
topics_with_k2_mappings = 0
topics_with_coding_mappings = 0

for topic_id, topic_data in mapping_rules['topic_mappings'].items():
    has_k2 = any(len(topic_data['grade_mappings'].get(str(g), [])) > 0 for g in ['K', '1', '2'])
    has_coding = any(len(topic_data['grade_mappings'].get(str(g), [])) > 0 for g in ['3', '4', '5', '6', '7', '8'])

    if has_k2:
        topics_with_k2_mappings += 1
    if has_coding:
        topics_with_coding_mappings += 1

print(f"\n=== Mapping Rules Summary ===")
print(f"Total topics mapped: {total_topics}")
print(f"Topics with K-2 mappings: {topics_with_k2_mappings}")
print(f"Topics with G3-8 mappings: {topics_with_coding_mappings}")
print(f"\nRules file ready for automated skill assignment!")
