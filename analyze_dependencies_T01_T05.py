#!/usr/bin/env python3
"""
Analyze dependencies for Topics T01-T05 (Algorithms & Design domain)
"""
import json
from collections import defaultdict

def load_skills():
    """Load T01-T05 skills from the extracted file"""
    with open('t01_t05_skills.json', 'r') as f:
        return json.load(f)

def get_grade_num(skill_id):
    """Extract numeric grade from skill ID (e.g., T01.G1.01 -> 1)"""
    parts = skill_id.split('.')
    return int(parts[1][1:])  # Extract number from G1, G2, etc.

def analyze_dependencies(skills):
    """Analyze and add dependencies to each skill"""
    # Organize skills by topic and grade for easy lookup
    skills_by_topic_grade = defaultdict(lambda: defaultdict(list))
    skills_dict = {}

    for skill in skills:
        topic = skill['topic_id']
        grade = get_grade_num(skill['id'])
        skills_by_topic_grade[topic][grade].append(skill)
        skills_dict[skill['id']] = skill

    results = []

    # Process each skill
    for skill in sorted(skills, key=lambda s: (s['topic_id'], get_grade_num(s['id']), s['id'])):
        skill_id = skill['id']
        topic = skill['topic_id']
        grade = get_grade_num(skill_id)
        title = skill['title']
        description = skill['description']

        dependencies = []
        notes = ""
        grade_level_ok = True
        quality_issues = []

        # T01: Everyday Algorithms
        if topic == 'T01':
            if grade == 1:
                # Grade 1 - foundational, minimal dependencies
                if 'G1.01' in skill_id:
                    notes = "Foundational skill - recognizing sequences in daily activities"
                elif 'G1.02' in skill_id:
                    dependencies = ['T01.G1.01']
                    notes = "Builds on sequence recognition to create simple step-by-step instructions"
                elif 'G1.03' in skill_id:
                    dependencies = ['T01.G1.02']
                    notes = "Applies instruction creation to storytelling context"
                elif 'G1.04' in skill_id:
                    dependencies = ['T01.G1.02']
                    notes = "Applies sequential thinking to everyday tasks"

            elif grade == 2:
                # Grade 2 - builds on G1 foundations
                if 'G2.01' in skill_id:
                    dependencies = ['T01.G1.02']
                    notes = "Extends simple instructions to more detailed algorithm writing"
                elif 'G2.02' in skill_id:
                    dependencies = ['T01.G2.01']
                    notes = "Adds precision and clarity to algorithm writing"
                elif 'G2.03' in skill_id:
                    dependencies = ['T01.G2.01']
                    notes = "Introduces ordering and sequencing of algorithm steps"
                elif 'G2.04' in skill_id:
                    dependencies = ['T01.G2.01', 'T01.G1.04']
                    notes = "Applies algorithm creation to real-world tasks"

            elif grade == 3:
                # Grade 3 - introduces debugging and refinement
                if 'G3.01' in skill_id:
                    dependencies = ['T01.G2.02']
                    notes = "Introduces error detection in algorithms"
                elif 'G3.02' in skill_id:
                    dependencies = ['T01.G3.01']
                    notes = "Adds error correction to debugging skills"
                elif 'G3.03' in skill_id:
                    dependencies = ['T01.G2.03']
                    notes = "Introduces comparison of different algorithmic approaches"
                elif 'G3.04' in skill_id:
                    dependencies = ['T01.G2.01', 'T02.G3.01']
                    notes = "Applies algorithms in block coding context (cross-topic with T02)"

            elif grade == 4:
                # Grade 4 - efficiency and optimization
                if 'G4.01' in skill_id:
                    dependencies = ['T01.G3.03']
                    notes = "Introduces efficiency concepts in algorithm comparison"
                elif 'G4.02' in skill_id:
                    dependencies = ['T01.G4.01']
                    notes = "Applies efficiency analysis to algorithm selection"
                elif 'G4.03' in skill_id:
                    dependencies = ['T01.G3.02', 'T01.G4.01']
                    notes = "Combines debugging with efficiency improvement"
                elif 'G4.04' in skill_id:
                    dependencies = ['T01.G4.02', 'T03.G4.01']
                    notes = "Applies algorithmic thinking with decomposition (cross-topic with T03)"

            elif grade == 5:
                # Grade 5 - complex algorithms and planning
                if 'G5.01' in skill_id:
                    dependencies = ['T01.G4.02']
                    notes = "Extends to multi-step algorithms with efficiency considerations"
                elif 'G5.02' in skill_id:
                    dependencies = ['T01.G5.01']
                    notes = "Adds planning and pseudocode to algorithm design"
                elif 'G5.03' in skill_id:
                    dependencies = ['T01.G4.03']
                    notes = "Introduces systematic testing of algorithms"
                elif 'G5.04' in skill_id:
                    dependencies = ['T01.G5.02', 'T03.G5.01']
                    notes = "Combines algorithm design with decomposition strategies"

            elif grade == 6:
                # Grade 6 - algorithm types and analysis
                if 'G6.01' in skill_id:
                    dependencies = ['T01.G5.01']
                    notes = "Introduces different algorithm types (search, sort)"
                elif 'G6.02' in skill_id:
                    dependencies = ['T01.G6.01']
                    notes = "Compares algorithm types for different problems"
                elif 'G6.03' in skill_id:
                    dependencies = ['T01.G5.03']
                    notes = "Extends testing to include edge cases and boundary conditions"
                elif 'G6.04' in skill_id:
                    dependencies = ['T01.G6.02', 'T04.G6.01']
                    notes = "Combines algorithm selection with pattern recognition"

            elif grade == 7:
                # Grade 7 - algorithm complexity and recursion
                if 'G7.01' in skill_id:
                    dependencies = ['T01.G6.01']
                    notes = "Introduces more complex algorithm types including recursion"
                elif 'G7.02' in skill_id:
                    dependencies = ['T01.G6.02', 'T01.G7.01']
                    notes = "Analyzes time and space complexity of algorithms"
                elif 'G7.03' in skill_id:
                    dependencies = ['T01.G7.02']
                    notes = "Optimizes algorithms based on complexity analysis"
                elif 'G7.04' in skill_id:
                    dependencies = ['T01.G7.02', 'T04.G7.01']
                    notes = "Applies algorithmic thinking to complex problem-solving"

            elif grade == 8:
                # Grade 8 - advanced algorithms
                if 'G8.01' in skill_id:
                    dependencies = ['T01.G7.01']
                    notes = "Explores advanced algorithmic techniques"
                elif 'G8.02' in skill_id:
                    dependencies = ['T01.G7.03', 'T01.G8.01']
                    notes = "Designs efficient algorithms for complex problems"
                elif 'G8.03' in skill_id:
                    dependencies = ['T01.G8.02']
                    notes = "Evaluates algorithm trade-offs (time vs space, accuracy vs speed)"
                elif 'G8.04' in skill_id:
                    dependencies = ['T01.G8.02', 'T03.G8.01']
                    notes = "Applies advanced algorithms to real-world computational problems"

        # T02: Representing and Tracing Programs
        elif topic == 'T02':
            if grade == 1:
                if 'G1.01' in skill_id:
                    notes = "Foundational - following simple visual directions"
                elif 'G1.02' in skill_id:
                    dependencies = ['T02.G1.01']
                    notes = "Extends following directions to multi-step sequences"
                elif 'G1.03' in skill_id:
                    dependencies = ['T02.G1.02', 'T01.G1.01']
                    notes = "Connects visual sequences to algorithmic thinking"
                elif 'G1.04' in skill_id:
                    dependencies = ['T02.G1.02']
                    notes = "Applies sequence following to physical movement"

            elif grade == 2:
                if 'G2.01' in skill_id:
                    dependencies = ['T02.G1.03']
                    notes = "Introduces basic visual programming concepts"
                elif 'G2.02' in skill_id:
                    dependencies = ['T02.G2.01']
                    notes = "Adds predicting outcomes to program understanding"
                elif 'G2.03' in skill_id:
                    dependencies = ['T02.G2.01']
                    notes = "Introduces tracing program execution"
                elif 'G2.04' in skill_id:
                    dependencies = ['T02.G2.03', 'T01.G2.01']
                    notes = "Combines tracing with algorithm understanding"

            elif grade == 3:
                if 'G3.01' in skill_id:
                    dependencies = ['T02.G2.01']
                    notes = "Introduces block-based programming"
                elif 'G3.02' in skill_id:
                    dependencies = ['T02.G3.01']
                    notes = "Adds reading and interpreting block code"
                elif 'G3.03' in skill_id:
                    dependencies = ['T02.G3.02', 'T02.G2.03']
                    notes = "Extends tracing to block-based programs"
                elif 'G3.04' in skill_id:
                    dependencies = ['T02.G3.03', 'T01.G3.01']
                    notes = "Applies tracing to debug programs"

            elif grade == 4:
                if 'G4.01' in skill_id:
                    dependencies = ['T02.G3.02']
                    notes = "Deepens understanding of block code structure"
                elif 'G4.02' in skill_id:
                    dependencies = ['T02.G4.01']
                    notes = "Introduces translating between representations"
                elif 'G4.03' in skill_id:
                    dependencies = ['T02.G3.03']
                    notes = "Extends tracing to more complex programs"
                elif 'G4.04' in skill_id:
                    dependencies = ['T02.G4.03', 'T01.G4.01']
                    notes = "Uses tracing to analyze program efficiency"

            elif grade == 5:
                if 'G5.01' in skill_id:
                    dependencies = ['T02.G4.02']
                    notes = "Introduces multiple programming representations"
                elif 'G5.02' in skill_id:
                    dependencies = ['T02.G5.01']
                    notes = "Converts between visual and text-based code"
                elif 'G5.03' in skill_id:
                    dependencies = ['T02.G4.03']
                    notes = "Traces programs with multiple control flows"
                elif 'G5.04' in skill_id:
                    dependencies = ['T02.G5.03', 'T01.G5.03']
                    notes = "Combines tracing with systematic testing"

            elif grade == 6:
                if 'G6.01' in skill_id:
                    dependencies = ['T02.G5.02']
                    notes = "Understands different programming paradigms"
                elif 'G6.02' in skill_id:
                    dependencies = ['T02.G6.01']
                    notes = "Compares programming representations and paradigms"
                elif 'G6.03' in skill_id:
                    dependencies = ['T02.G5.03']
                    notes = "Traces programs with complex state changes"
                elif 'G6.04' in skill_id:
                    dependencies = ['T02.G6.03', 'T01.G6.03']
                    notes = "Uses tracing for comprehensive testing"

            elif grade == 7:
                if 'G7.01' in skill_id:
                    dependencies = ['T02.G6.01']
                    notes = "Analyzes programming language features"
                elif 'G7.02' in skill_id:
                    dependencies = ['T02.G7.01']
                    notes = "Evaluates trade-offs between programming approaches"
                elif 'G7.03' in skill_id:
                    dependencies = ['T02.G6.03']
                    notes = "Traces programs with advanced control structures"
                elif 'G7.04' in skill_id:
                    dependencies = ['T02.G7.03', 'T01.G7.02']
                    notes = "Uses tracing for performance analysis"

            elif grade == 8:
                if 'G8.01' in skill_id:
                    dependencies = ['T02.G7.01']
                    notes = "Masters multiple programming paradigms"
                elif 'G8.02' in skill_id:
                    dependencies = ['T02.G8.01']
                    notes = "Selects optimal programming representation for problems"
                elif 'G8.03' in skill_id:
                    dependencies = ['T02.G7.03']
                    notes = "Traces complex programs with advanced features"
                elif 'G8.04' in skill_id:
                    dependencies = ['T02.G8.03', 'T01.G8.02']
                    notes = "Integrates tracing with algorithm design"

        # T03: Decomposition
        elif topic == 'T03':
            if grade == 1:
                if 'G1.01' in skill_id:
                    notes = "Foundational - breaking simple tasks into steps"
                elif 'G1.02' in skill_id:
                    dependencies = ['T03.G1.01']
                    notes = "Applies decomposition to familiar activities"
                elif 'G1.03' in skill_id:
                    dependencies = ['T03.G1.01', 'T01.G1.01']
                    notes = "Connects part-to-whole thinking with sequences"
                elif 'G1.04' in skill_id:
                    dependencies = ['T03.G1.02']
                    notes = "Applies decomposition to simple problems"

            elif grade == 2:
                if 'G2.01' in skill_id:
                    dependencies = ['T03.G1.04']
                    notes = "Extends decomposition to more complex tasks"
                elif 'G2.02' in skill_id:
                    dependencies = ['T03.G2.01']
                    notes = "Introduces organizing sub-tasks"
                elif 'G2.03' in skill_id:
                    dependencies = ['T03.G2.01', 'T01.G2.01']
                    notes = "Combines decomposition with algorithm design"
                elif 'G2.04' in skill_id:
                    dependencies = ['T03.G2.02']
                    notes = "Applies systematic decomposition to problems"

            elif grade == 3:
                if 'G3.01' in skill_id:
                    dependencies = ['T03.G2.04']
                    notes = "Introduces identifying sub-problems"
                elif 'G3.02' in skill_id:
                    dependencies = ['T03.G3.01']
                    notes = "Adds solving sub-problems independently"
                elif 'G3.03' in skill_id:
                    dependencies = ['T03.G3.02']
                    notes = "Introduces combining solutions from sub-problems"
                elif 'G3.04' in skill_id:
                    dependencies = ['T03.G3.03', 'T02.G3.01']
                    notes = "Applies decomposition in programming context"

            elif grade == 4:
                if 'G4.01' in skill_id:
                    dependencies = ['T03.G3.01']
                    notes = "Deepens sub-problem identification skills"
                elif 'G4.02' in skill_id:
                    dependencies = ['T03.G4.01']
                    notes = "Introduces hierarchical decomposition"
                elif 'G4.03' in skill_id:
                    dependencies = ['T03.G3.03']
                    notes = "Manages relationships between sub-problems"
                elif 'G4.04' in skill_id:
                    dependencies = ['T03.G4.02', 'T02.G4.01']
                    notes = "Applies structured decomposition in programs"

            elif grade == 5:
                if 'G5.01' in skill_id:
                    dependencies = ['T03.G4.02']
                    notes = "Masters multi-level decomposition"
                elif 'G5.02' in skill_id:
                    dependencies = ['T03.G5.01']
                    notes = "Introduces modular problem-solving"
                elif 'G5.03' in skill_id:
                    dependencies = ['T03.G5.02']
                    notes = "Plans decomposition strategies before solving"
                elif 'G5.04' in skill_id:
                    dependencies = ['T03.G5.03', 'T01.G5.02']
                    notes = "Integrates decomposition with algorithm planning"

            elif grade == 6:
                if 'G6.01' in skill_id:
                    dependencies = ['T03.G5.02']
                    notes = "Introduces functional decomposition"
                elif 'G6.02' in skill_id:
                    dependencies = ['T03.G6.01']
                    notes = "Designs reusable modules and components"
                elif 'G6.03' in skill_id:
                    dependencies = ['T03.G6.02']
                    notes = "Manages dependencies between modules"
                elif 'G6.04' in skill_id:
                    dependencies = ['T03.G6.03', 'T02.G6.01']
                    notes = "Applies modular design in programming"

            elif grade == 7:
                if 'G7.01' in skill_id:
                    dependencies = ['T03.G6.02']
                    notes = "Introduces object-oriented decomposition concepts"
                elif 'G7.02' in skill_id:
                    dependencies = ['T03.G7.01']
                    notes = "Designs systems with multiple interacting components"
                elif 'G7.03' in skill_id:
                    dependencies = ['T03.G7.02']
                    notes = "Analyzes decomposition trade-offs"
                elif 'G7.04' in skill_id:
                    dependencies = ['T03.G7.03', 'T01.G7.02']
                    notes = "Optimizes decomposition for efficiency"

            elif grade == 8:
                if 'G8.01' in skill_id:
                    dependencies = ['T03.G7.01']
                    notes = "Masters advanced decomposition techniques"
                elif 'G8.02' in skill_id:
                    dependencies = ['T03.G8.01']
                    notes = "Applies design patterns and architectural principles"
                elif 'G8.03' in skill_id:
                    dependencies = ['T03.G8.02']
                    notes = "Evaluates and refactors decomposition strategies"
                elif 'G8.04' in skill_id:
                    dependencies = ['T03.G8.03', 'T01.G8.02']
                    notes = "Designs scalable, maintainable systems"

        # T04: Patterns
        elif topic == 'T04':
            if grade == 1:
                if 'G1.01' in skill_id:
                    notes = "Foundational - recognizing simple repeating patterns"
                elif 'G1.02' in skill_id:
                    dependencies = ['T04.G1.01']
                    notes = "Extends patterns to visual and audio sequences"
                elif 'G1.03' in skill_id:
                    dependencies = ['T04.G1.01']
                    notes = "Introduces predicting pattern continuation"
                elif 'G1.04' in skill_id:
                    dependencies = ['T04.G1.02', 'T01.G1.01']
                    notes = "Connects patterns to sequences and algorithms"

            elif grade == 2:
                if 'G2.01' in skill_id:
                    dependencies = ['T04.G1.03']
                    notes = "Introduces creating original patterns"
                elif 'G2.02' in skill_id:
                    dependencies = ['T04.G2.01']
                    notes = "Extends patterns to different contexts"
                elif 'G2.03' in skill_id:
                    dependencies = ['T04.G1.01']
                    notes = "Introduces describing pattern rules"
                elif 'G2.04' in skill_id:
                    dependencies = ['T04.G2.03', 'T01.G2.01']
                    notes = "Connects patterns to algorithmic steps"

            elif grade == 3:
                if 'G3.01' in skill_id:
                    dependencies = ['T04.G2.03']
                    notes = "Introduces identifying different pattern types"
                elif 'G3.02' in skill_id:
                    dependencies = ['T04.G3.01']
                    notes = "Analyzes pattern structure and rules"
                elif 'G3.03' in skill_id:
                    dependencies = ['T04.G2.01']
                    notes = "Creates patterns following specific rules"
                elif 'G3.04' in skill_id:
                    dependencies = ['T04.G3.02', 'T02.G3.01']
                    notes = "Applies patterns in block programming"

            elif grade == 4:
                if 'G4.01' in skill_id:
                    dependencies = ['T04.G3.02']
                    notes = "Introduces patterns in data and information"
                elif 'G4.02' in skill_id:
                    dependencies = ['T04.G4.01']
                    notes = "Uses patterns to make predictions"
                elif 'G4.03' in skill_id:
                    dependencies = ['T04.G3.03']
                    notes = "Creates complex, nested patterns"
                elif 'G4.04' in skill_id:
                    dependencies = ['T04.G4.02', 'T03.G4.01']
                    notes = "Applies pattern recognition to problem decomposition"

            elif grade == 5:
                if 'G5.01' in skill_id:
                    dependencies = ['T04.G4.01']
                    notes = "Introduces computational patterns and structures"
                elif 'G5.02' in skill_id:
                    dependencies = ['T04.G5.01']
                    notes = "Identifies patterns in algorithms and programs"
                elif 'G5.03' in skill_id:
                    dependencies = ['T04.G5.02']
                    notes = "Abstracts patterns into reusable solutions"
                elif 'G5.04' in skill_id:
                    dependencies = ['T04.G5.03', 'T03.G5.02']
                    notes = "Combines pattern abstraction with modular design"

            elif grade == 6:
                if 'G6.01' in skill_id:
                    dependencies = ['T04.G5.03']
                    notes = "Introduces algorithmic patterns and templates"
                elif 'G6.02' in skill_id:
                    dependencies = ['T04.G6.01']
                    notes = "Applies design patterns to solve common problems"
                elif 'G6.03' in skill_id:
                    dependencies = ['T04.G6.02']
                    notes = "Adapts patterns to different contexts"
                elif 'G6.04' in skill_id:
                    dependencies = ['T04.G6.03', 'T01.G6.02']
                    notes = "Selects appropriate patterns for algorithms"

            elif grade == 7:
                if 'G7.01' in skill_id:
                    dependencies = ['T04.G6.02']
                    notes = "Introduces advanced design patterns"
                elif 'G7.02' in skill_id:
                    dependencies = ['T04.G7.01']
                    notes = "Analyzes pattern trade-offs and applications"
                elif 'G7.03' in skill_id:
                    dependencies = ['T04.G7.02']
                    notes = "Combines multiple patterns in solutions"
                elif 'G7.04' in skill_id:
                    dependencies = ['T04.G7.03', 'T03.G7.02']
                    notes = "Designs pattern-based system architectures"

            elif grade == 8:
                if 'G8.01' in skill_id:
                    dependencies = ['T04.G7.01']
                    notes = "Masters software design patterns"
                elif 'G8.02' in skill_id:
                    dependencies = ['T04.G8.01']
                    notes = "Creates custom patterns for specific domains"
                elif 'G8.03' in skill_id:
                    dependencies = ['T04.G8.02']
                    notes = "Evaluates pattern effectiveness and appropriateness"
                elif 'G8.04' in skill_id:
                    dependencies = ['T04.G8.03', 'T03.G8.02']
                    notes = "Applies patterns in large-scale system design"

        # T05: Human-Centered Design
        elif topic == 'T05':
            if grade == 1:
                if 'G1.01' in skill_id:
                    notes = "Foundational - understanding user needs"
                elif 'G1.02' in skill_id:
                    dependencies = ['T05.G1.01']
                    notes = "Introduces expressing preferences and choices"
                elif 'G1.03' in skill_id:
                    dependencies = ['T05.G1.01']
                    notes = "Introduces observing how others use things"
                elif 'G1.04' in skill_id:
                    dependencies = ['T05.G1.02', 'T01.G1.02']
                    notes = "Applies user thinking to simple design tasks"

            elif grade == 2:
                if 'G2.01' in skill_id:
                    dependencies = ['T05.G1.03']
                    notes = "Introduces asking users questions"
                elif 'G2.02' in skill_id:
                    dependencies = ['T05.G2.01']
                    notes = "Uses feedback to improve designs"
                elif 'G2.03' in skill_id:
                    dependencies = ['T05.G1.04']
                    notes = "Introduces thinking about different user types"
                elif 'G2.04' in skill_id:
                    dependencies = ['T05.G2.02', 'T01.G2.04']
                    notes = "Applies user-centered thinking to practical tasks"

            elif grade == 3:
                if 'G3.01' in skill_id:
                    dependencies = ['T05.G2.01']
                    notes = "Introduces structured user research"
                elif 'G3.02' in skill_id:
                    dependencies = ['T05.G3.01']
                    notes = "Identifies user problems and needs"
                elif 'G3.03' in skill_id:
                    dependencies = ['T05.G2.02']
                    notes = "Introduces iterative design and testing"
                elif 'G3.04' in skill_id:
                    dependencies = ['T05.G3.03', 'T02.G3.01']
                    notes = "Applies user-centered design to programs"

            elif grade == 4:
                if 'G4.01' in skill_id:
                    dependencies = ['T05.G3.02']
                    notes = "Introduces empathy in design"
                elif 'G4.02' in skill_id:
                    dependencies = ['T05.G4.01']
                    notes = "Designs for diverse user groups"
                elif 'G4.03' in skill_id:
                    dependencies = ['T05.G3.03']
                    notes = "Develops systematic testing with users"
                elif 'G4.04' in skill_id:
                    dependencies = ['T05.G4.03', 'T03.G4.01']
                    notes = "Combines user research with problem decomposition"

            elif grade == 5:
                if 'G5.01' in skill_id:
                    dependencies = ['T05.G4.02']
                    notes = "Introduces accessibility in design"
                elif 'G5.02' in skill_id:
                    dependencies = ['T05.G5.01']
                    notes = "Designs inclusive solutions"
                elif 'G5.03' in skill_id:
                    dependencies = ['T05.G4.03']
                    notes = "Introduces usability testing methods"
                elif 'G5.04' in skill_id:
                    dependencies = ['T05.G5.03', 'T01.G5.02']
                    notes = "Integrates user testing into design process"

            elif grade == 6:
                if 'G6.01' in skill_id:
                    dependencies = ['T05.G5.02']
                    notes = "Introduces user experience (UX) principles"
                elif 'G6.02' in skill_id:
                    dependencies = ['T05.G6.01']
                    notes = "Applies UX design to interfaces"
                elif 'G6.03' in skill_id:
                    dependencies = ['T05.G5.03']
                    notes = "Conducts comprehensive usability studies"
                elif 'G6.04' in skill_id:
                    dependencies = ['T05.G6.03', 'T04.G6.02']
                    notes = "Combines UX patterns with design principles"

            elif grade == 7:
                if 'G7.01' in skill_id:
                    dependencies = ['T05.G6.01']
                    notes = "Introduces advanced UX concepts"
                elif 'G7.02' in skill_id:
                    dependencies = ['T05.G7.01']
                    notes = "Designs for complex user journeys"
                elif 'G7.03' in skill_id:
                    dependencies = ['T05.G6.03']
                    notes = "Analyzes usability metrics and data"
                elif 'G7.04' in skill_id:
                    dependencies = ['T05.G7.03', 'T03.G7.02']
                    notes = "Integrates UX into system design"

            elif grade == 8:
                if 'G8.01' in skill_id:
                    dependencies = ['T05.G7.01']
                    notes = "Masters UX design methodologies"
                elif 'G8.02' in skill_id:
                    dependencies = ['T05.G8.01']
                    notes = "Designs complete user experiences"
                elif 'G8.03' in skill_id:
                    dependencies = ['T05.G7.03']
                    notes = "Evaluates and optimizes user experiences"
                elif 'G8.04' in skill_id:
                    dependencies = ['T05.G8.03', 'T03.G8.02']
                    notes = "Leads user-centered design projects"

        # Validate dependencies don't reference future grades
        for dep_id in dependencies:
            if dep_id in skills_dict:
                dep_grade = get_grade_num(dep_id)
                if dep_grade > grade:
                    grade_level_ok = False
                    quality_issues.append(f"Grade level conflict: depends on {dep_id} which is grade {dep_grade}")

        # Check for quality issues based on skill content
        # This is a simplified check - real analysis would be more sophisticated
        if len(title) < 10:
            quality_issues.append("Title may be too brief")
        if len(description) < 30:
            quality_issues.append("Description may be too brief")
        if len(title) > 150:
            quality_issues.append("Title may be too long/complex")

        result = {
            "id": skill_id,
            "title": title,
            "topic": topic,
            "grade": grade,
            "dependencies": dependencies,
            "notes": notes,
            "grade_level_ok": grade_level_ok,
            "quality_issues": quality_issues
        }

        results.append(result)

    return results

def generate_summary(results):
    """Generate summary statistics and findings"""
    summary = {
        "total_skills": len(results),
        "by_topic": {},
        "by_grade": defaultdict(int),
        "grade_conflicts": [],
        "quality_issues_count": 0,
        "dependency_stats": {
            "no_dependencies": 0,
            "within_topic_only": 0,
            "cross_topic": 0,
            "avg_dependencies": 0
        }
    }

    total_deps = 0

    for result in results:
        topic = result['topic']
        grade = result['grade']

        if topic not in summary['by_topic']:
            summary['by_topic'][topic] = 0
        summary['by_topic'][topic] += 1
        summary['by_grade'][grade] += 1

        if not result['grade_level_ok']:
            summary['grade_conflicts'].append(result['id'])

        if result['quality_issues']:
            summary['quality_issues_count'] += len(result['quality_issues'])

        # Analyze dependencies
        deps = result['dependencies']
        total_deps += len(deps)

        if not deps:
            summary['dependency_stats']['no_dependencies'] += 1
        else:
            has_cross_topic = any(d.split('.')[0] != topic for d in deps)
            if has_cross_topic:
                summary['dependency_stats']['cross_topic'] += 1
            else:
                summary['dependency_stats']['within_topic_only'] += 1

    summary['dependency_stats']['avg_dependencies'] = total_deps / len(results)

    return summary

def main():
    print("Loading skills...")
    skills = load_skills()

    print(f"Analyzing {len(skills)} skills from T01-T05...")
    results = analyze_dependencies(skills)

    print("Generating summary...")
    summary = generate_summary(results)

    # Save results
    with open('dependencies_T01_T05.json', 'w') as f:
        json.dump(results, f, indent=2)

    with open('dependencies_T01_T05_summary.json', 'w') as f:
        json.dump(summary, f, indent=2)

    print("\n=== ANALYSIS COMPLETE ===\n")
    print(f"Total skills analyzed: {summary['total_skills']}")
    print(f"\nSkills by topic:")
    for topic, count in sorted(summary['by_topic'].items()):
        print(f"  {topic}: {count}")

    print(f"\nSkills by grade:")
    for grade in sorted(summary['by_grade'].keys()):
        print(f"  Grade {grade}: {summary['by_grade'][grade]}")

    print(f"\nDependency Statistics:")
    print(f"  No dependencies: {summary['dependency_stats']['no_dependencies']}")
    print(f"  Within-topic only: {summary['dependency_stats']['within_topic_only']}")
    print(f"  Cross-topic: {summary['dependency_stats']['cross_topic']}")
    print(f"  Average dependencies per skill: {summary['dependency_stats']['avg_dependencies']:.2f}")

    print(f"\nGrade-level conflicts: {len(summary['grade_conflicts'])}")
    if summary['grade_conflicts']:
        print("  Skills with conflicts:", ', '.join(summary['grade_conflicts'][:10]))

    print(f"\nTotal quality issues flagged: {summary['quality_issues_count']}")

    print("\nFiles created:")
    print("  - dependencies_T01_T05.json")
    print("  - dependencies_T01_T05_summary.json")

if __name__ == '__main__':
    main()
