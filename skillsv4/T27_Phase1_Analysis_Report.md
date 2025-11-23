# T27 (Data Analysis & Storytelling) - Phase 1 Analysis Report

**Analysis Date:** 2025-11-23
**Scope:** Skills T27.GK.01 through T27.G8.04 (lines 16001-16499)
**Total Skills Analyzed:** 54 skills across grades K-8

---

## EXECUTIVE SUMMARY

Topic T27 (Data Analysis & Storytelling) demonstrates strong foundational scaffolding in K-2 with unplugged activities transitioning to computational analysis in G3+. However, several critical issues require attention:

**Critical Findings:**
- 8 HIGH PRIORITY issues requiring immediate fixes
- 6 MEDIUM PRIORITY issues needing attention
- Multiple CreatiCode block categories requiring verification
- Strong dependencies on T10 (Lists & Tables topic) but some gaps in prerequisite coverage

**Strengths:**
- Excellent K-2 unplugged foundation with concrete manipulatives
- Well-structured progression from pictographs → bar charts → data tables
- Strong integration with CreatiCode's data infrastructure (tables, charts, widgets)
- Good ethical considerations (fairness metrics in G7)

---

## HIGH PRIORITY ISSUES

### 1. SKILLS TOO BROAD/COMPLEX NEEDING BREAKDOWN

#### **Issue H1.1: T27.G3.01 - Compute totals and averages from data tables**
**Problem:** Single skill covers 5 different aggregation operations (sum, average, median, minimum, maximum). This is too broad for a single skill, especially since median is taught conceptually separately in T27.G4.02b.

**Specific Issues:**
- Bundles 5 distinct statistical operations into one skill
- Creates confusion: median is introduced here but re-taught conceptually in G4
- Students need separate practice for each aggregation type
- Sum and count are simpler than median/mode; should be separated

**Suggested Fix:**
- **NEW T27.G3.01a:** "Use sum and count aggregations on table columns" - Focus on [sum v] and count operations (simpler aggregations)
- **RENAME T27.G3.01 to T27.G3.01c:** "Use min/max/average aggregations on table columns" - Focus on [average v], [minimum v], [maximum v]
- Keep T27.G4.02b/c for median/mode (more complex statistics)
- Dependencies: Both new skills depend on T27.G3.01b (table creation)

**Impact:** Enables clearer scaffolding; students master simple aggregations before complex ones

---

#### **Issue H1.2: T27.G4.02c - Calculate median and mode using code**
**Problem:** Skill combines built-in median function with custom mode implementation requiring loops and conditionals. The cognitive load mismatch (using vs. implementing) is significant.

**Specific Issues:**
- Median uses built-in block (simple) vs. mode requires custom algorithm (complex)
- Mode calculation needs frequency counting, loops, conditionals, comparison logic
- Skill description doesn't specify the algorithmic complexity difference
- Mode calculation is closer to G6 complexity, not G4

**Suggested Fix:**
- **KEEP T27.G4.02c for median only:** "Calculate median using aggregation blocks"
- **NEW T27.G5.03b:** "Calculate mode by counting frequencies" - Place in G5 where students have stronger loop/conditional skills, similar complexity to T27.G5.01b (GROUP BY)
- Update description to clarify median uses built-in, mode requires custom implementation
- Dependencies: Mode skill should depend on T27.G4.02c (median) + T08.G4.01 (if-else) + T10.G4.01 (list operations)

**Impact:** Separates simple built-in usage from complex algorithm implementation

---

#### **Issue H1.3: T27.G6.01 - Filter table rows using multiple conditions**
**Problem:** Skill description shows two-step manual process (delete + loop) but modern data practice would use proper compound filtering. Too implementation-specific for a conceptual skill.

**Specific Issues:**
- Example given is overly prescriptive (delete rows, then loop)
- Doesn't teach compound conditional logic as a concept
- Implementation-heavy rather than conceptual
- Misses opportunity to teach AND/OR logic in filtering context

**Suggested Fix:**
- **REWRITE description:** "Students implement multi-condition filtering using compound boolean logic (AND/OR operators) in loops. They learn to combine multiple criteria (e.g., level = 'Forest' AND score > 50) and understand the difference between AND (both must be true) and OR (at least one true) filters. Implementation uses iteration with compound conditionals to identify and delete/copy matching rows."
- Add clearer connection to boolean logic (T08 conditionals)
- Keep G6 placement (requires compound conditionals from T08.G4.01+)

**Impact:** Focuses on logical concept rather than specific implementation pattern

---

#### **Issue H1.4: T27.G5.01 - Build a simple interactive dashboard with filter widgets**
**Problem:** Bundles widget event handling + table filtering + chart updates + multiple widget types in single skill. Too broad for first dashboard skill.

**Specific Issues:**
- Covers dropdown menus AND buttons in one skill
- Combines event handling, data filtering, and visualization updates
- No prerequisite for widget creation blocks (add dropdown menu, add button)
- Missing foundation for widget interaction before building dashboard

**Suggested Fix:**
- **NEW T27.G4.05:** "Create basic UI widgets (buttons and dropdowns)" - Add widget creation as standalone skill in G4
  - Description: "Students use 'add button' and 'add dropdown menu' blocks to create UI elements, position them on stage, and understand widget naming for later event handling."
  - Dependencies: T06.G3.01 (basic scripts), T09.G3.01.04 (display concepts)
- **RENAME T27.G5.01 to be more focused:** Keep dashboard skill but simplify to "Build a simple filtered chart with one widget"
- Update description to focus on single widget → single chart connection first
- Dependencies: Add dependency on new T27.G4.05

**Impact:** Provides proper foundation before building interactive dashboards

---

#### **Issue H1.5: T27.G7.01 - Build multi-chart dashboards with linked filters**
**Problem:** Jumps from single-chart filtering (G5) to multi-chart with shared state and event broadcasting. Missing intermediate step of independent multiple charts.

**Specific Issues:**
- Introduces event broadcasting for chart synchronization without prerequisite
- Combines "multiple charts" + "linked filters" + "shared variables" in one skill
- Large conceptual jump from G5 single-chart dashboard
- Missing foundation: creating multiple independent visualizations

**Suggested Fix:**
- **NEW T27.G6.05:** "Create dashboard with multiple independent charts"
  - Description: "Students create 2-3 charts (bar + line, or bar + pie) from the same or different data tables, positioned side-by-side on stage. Charts update independently and are not linked. This builds spatial layout and multi-visualization skills before adding interactivity."
  - Dependencies: T27.G5.02 (correlate two variables), T27.G6.02 (compare groups)
- **KEEP T27.G7.01** but update description to emphasize the "linked" aspect
- Update dependencies: Add T27.G6.05 + T06.G5.01 (broadcast events)

**Impact:** Scaffolds multi-chart creation before adding synchronization complexity

---

### 2. DUPLICATE OR SIGNIFICANTLY OVERLAPPING SKILLS

#### **Issue H2.1: T27.G3.03 vs. T27.G4.02d - Table Filtering Overlap**
**Problem:** Both skills teach table filtering, with significant overlap in content and techniques.

**Skills in Question:**
- **T27.G3.03:** "Use CreatiCode data tables to group and count" - Includes filtering ("delete rows with column [type] of value [desert]")
- **T27.G4.02d:** "Filter table rows by condition" - Dedicated filtering skill with same basic technique plus advanced loop-based filtering

**Specific Issues:**
- G3 skill teaches filtering as part of "group and count" but filtering is the main operation shown
- G4 skill re-teaches the same basic filtering operation
- Creates confusion about when filtering is introduced
- T27.G3.03 should focus on grouping/counting, not filtering

**Suggested Fix:**
- **RENAME T27.G3.03:** "Count rows in filtered tables"
  - **REWRITE description:** "Students use 'row count of table [data v]' to count how many rows exist in a table. They create working tables by copying and filtering original data (e.g., creating a 'forest_only' table), then count rows to answer questions like 'How many forest levels are there?' This separates counting (the new skill) from filtering (taught later)."
  - Remove filtering examples; focus on counting
- **KEEP T27.G4.02d** as the proper introduction to filtering
- Clarify: G3 students use pre-filtered tables or teacher-created tables; G4 students create filters themselves

**Impact:** Eliminates redundancy; clarifies filtering progression

---

#### **Issue H2.2: Statistical Comparison Skills Overlap (T27.G5.02, T27.G6.02, T27.G6.03)**
**Problem:** Three skills with overlapping "compare data" themes but unclear differentiation.

**Skills in Question:**
- **T27.G5.02:** "Correlate two variables visually" - Compare time played vs high score
- **T27.G6.02:** "Compare two groups using data" - Version A vs Version B with statistical comparison
- **T27.G6.03:** "Identify trends and patterns in time-series data" - Multi-week data analysis

**Specific Issues:**
- All three involve comparing datasets or variables
- Differentiation not clear in titles
- G5.02 focuses on RELATIONSHIP (correlation), G6.02 on GROUP DIFFERENCES (comparison), G6.03 on TEMPORAL PATTERNS (trends)
- Need clearer conceptual boundaries

**Suggested Fix:**
- **KEEP all three** but strengthen descriptions to clarify distinctions:
  - **T27.G5.02:** Emphasize "exploring RELATIONSHIPS between two variables" (correlation concept)
  - **T27.G6.02:** Emphasize "STATISTICAL COMPARISON of group means" (hypothesis testing prep)
  - **T27.G6.03:** Emphasize "TEMPORAL PATTERN RECOGNITION" (trend analysis)
- Add cross-references in descriptions to clarify relationships between skills
- Current placement is appropriate (G5→G6 progression)

**Impact:** Clarifies conceptual differences; maintains distinct learning objectives

---

### 3. MISSING ESSENTIAL SKILLS FOR SCAFFOLDING

#### **Issue H3.1: Missing Widget Interaction Foundation (Grade 4)**
**Problem:** Skills jump from basic table operations (G3) to interactive dashboards with widgets (G5) without teaching widget creation or basic event handling.

**Gap Analysis:**
- G3: Students work with tables and charts
- G4: No widget-related skills
- G5: T27.G5.01 suddenly uses widgets with event handlers
- T06 teaches general event handling but not widget-specific events

**Suggested Fix:**
- **NEW T27.G4.05:** "Create basic UI widgets (buttons and dropdowns)"
  - Description: "Students use 'add button' and 'add dropdown menu' blocks to create UI elements on stage. They learn to position widgets using X/Y coordinates, set properties (width, height, labels), and name widgets for later event handling. This introduces the widget creation blocks before using widget events in dashboards."
  - Dependencies: T06.G3.01 (sequences), T09.G3.01.04 (display concepts)
  - Prepares for: T27.G5.01 (interactive dashboards)

**Impact:** Fills critical gap between static charts and interactive dashboards

---

#### **Issue H3.2: Missing Chart Type Selection Skill (Grade 4)**
**Problem:** Students use charts throughout G3-G8 but never explicitly learn when to choose which chart type.

**Gap Analysis:**
- G3: Students create specific chart types (bar, line) but don't learn selection criteria
- G4-G8: Charts are used but type selection is implicit
- No explicit skill teaching: "Use bar charts for categories, line for trends, pie for proportions"

**Suggested Fix:**
- **NEW T27.G4.06:** "Choose appropriate chart types for different data"
  - Description: "Students learn to select chart types based on data characteristics and questions: bar charts for comparing categories (e.g., which class scored highest), line charts for showing change over time (e.g., temperature across days), pie/percentage charts for showing proportions of a whole (e.g., vote distribution). They analyze 3-4 datasets and justify which chart type best answers given questions."
  - Dependencies: T27.G3.04 (side-by-side bar charts), T27.G4.01 (line graphs)
  - Prepares for: Better chart selection in all later grades

**Impact:** Adds explicit data visualization literacy

---

#### **Issue H3.3: Missing Data Quality Concepts (Grade 3)**
**Problem:** T27.G4.03 teaches checking data quality, but students haven't been introduced to what "good data" means.

**Gap Analysis:**
- G3: Students create and populate tables but don't consider data quality
- G4: T27.G4.03 suddenly requires identifying missing entries, duplicates, invalid numbers
- No foundation for understanding data validation

**Suggested Fix:**
- **NEW T27.G3.05:** "Recognize complete vs. incomplete data entries"
  - Description: "Students examine small tables (5-6 rows) and identify which rows have all required information vs. which have missing values (empty cells or placeholder values like -1 or 'unknown'). They learn that analysis requires complete data and practice marking incomplete entries visually. This is a conceptual literacy skill preparing for computational data quality checks."
  - Dependencies: T27.G3.01b (create tables), T27.G3.02 (build statements with evidence)
  - Prepares for: T27.G4.03 (check data quality with code)

**Impact:** Builds data literacy foundation before automated quality checks

---

### 4. INCORRECT GRADE PLACEMENT

#### **Issue H4.1: T27.G4.02 - Calculate percentages from grouped data**
**Problem:** Skill requires division, percentage concepts, and percentage charts - likely too advanced for Grade 4 students without stronger math foundation.

**Evidence:**
- Percentage calculation (15 out of 50 = 30%) requires understanding division and percentage conversion
- Common Core: Percentage formally introduced in Grade 6 (6.RP.A.3c)
- Skill depends on grouped data (categories) + division + percentage interpretation
- G4 students typically work with simpler fractions

**Suggested Fix:**
- **MOVE to Grade 5:** Reposition as **T27.G5.04** (after current G5.03)
- Update dependencies to include stronger math foundations
- Add simpler G4 skill focusing on fractions or simple ratios instead
- **ALTERNATIVE NEW T27.G4.02:** "Calculate simple fractions from grouped data"
  - Description: "Students compute simple fractions (e.g., 3 out of 4 = 3/4) from categorized data and display results as decimal numbers. They understand that fractions represent part-to-whole relationships and can compute proportions without needing percentage conversion."
  - Dependencies: T27.G3.03 (group and count), T09.G3.01.04 (display values)

**Impact:** Aligns with developmental math readiness; maintains progression

---

### 5. INTRA-TOPIC DEPENDENCY VIOLATIONS

#### **Issue H5.1: T27.G4.02 depends on T27.G4.02b (violates ordering)**
**Problem:** T27.G4.02 (calculate percentages) depends on T27.G4.02b (understand median/mode), but the .02 suffix suggests it should come before .02b.

**Dependency Analysis:**
```
T27.G4.02: Calculate percentages from grouped data
└─ Depends on: T27.G4.02b (understand median/mode)

T27.G4.02b: Understand median and mode concepts
└─ Depends on: T27.G3.01, T27.G2.03
```

**Issues:**
- Skill numbering suggests T27.G4.02 comes before T27.G4.02b
- Dependency arrow points backward (T27.G4.02 → T27.G4.02b)
- Conceptually, percentages and median/mode are unrelated topics
- Dependency seems incorrect or skills are misnumbered

**Suggested Fix:**
**Option A (Recommended):** Remove dependency - percentages don't actually require median/mode knowledge
- Remove T27.G4.02b from T27.G4.02's dependencies
- Keep dependency on T27.G3.03 (group and count) which is more relevant

**Option B:** Renumber skills to reflect true sequence
- If dependency is correct, renumber T27.G4.02 to T27.G4.02d (placing it after median/mode skills)

**Recommended:** Option A - the dependency appears spurious

**Impact:** Fixes logical inconsistency in skill sequence

---

#### **Issue H5.2: T27.G4.04b - Sort tables placement and dependencies**
**Problem:** Sorting skill (T27.G4.04b) is placed after caption-writing (T27.G4.04) but depends on filtering (T27.G4.02d). The "b" suffix suggests dependency on T27.G4.04, but description doesn't show that relationship.

**Dependency Analysis:**
```
T27.G4.04: Create narrative captions for charts
└─ No dependency on sorting

T27.G4.04b: Sort tables to organize data
└─ Depends on: T27.G4.02d (filter rows)
└─ No dependency on T27.G4.04
```

**Issues:**
- Naming suggests T27.G4.04b extends/depends on T27.G4.04 (captions), but it doesn't
- Sorting is foundational for many operations (finding medians, top-N analysis)
- Should probably be earlier in G4 sequence, not at the end
- Sorting is more fundamental than caption-writing

**Suggested Fix:**
**RENUMBER:** Change T27.G4.04b → **T27.G4.03b** (place after data quality check, before captions)
- Sorting naturally follows data quality checking (T27.G4.03)
- Sorting enables finding medians (T27.G4.02b mentions sorting is needed)
- Update T27.G4.02b dependencies to include T27.G4.03b (sort before median)
- More logical progression: filter → sort → calculate stats

**Impact:** Improves logical skill sequence; better scaffolding for statistical operations

---

### 6. SKILLS REFERENCING CREATICODE BLOCKS NEEDING VERIFICATION

#### **Issue H6.1: Pivot Table Block (T27.G6.02b)**
**Block Referenced:** `pivot [data v] into [summary v] row groups [grade,gender] columns [score] methods [average]`

**Verification Needed:**
- Does CreatiCode have a native pivot block with this exact syntax?
- If not, does skill need to describe manual pivot implementation using loops?
- Pivot is very advanced operation - is G6 appropriate placement?

**Suggested Action:**
- VERIFY with CreatiCode block library documentation
- If block doesn't exist: Rewrite skill to describe algorithmic pivot implementation OR move to later grade
- If block exists: Add note about when CreatiCode introduced this block (version info)

---

#### **Issue H6.2: Moving Average Block (T27.G7.02b)**
**Block Referenced:** `value from [simple v] moving average window [7] of list [daily_scores v]`

**Verification Needed:**
- Skill says "extract table columns into lists" - is there a block for this conversion?
- Does CreatiCode have built-in moving average function?
- Why does moving average work on lists but not tables directly?

**Issues:**
- Description implies table-to-list conversion is necessary but doesn't teach this conversion
- If conversion is needed, should be a separate skill or prerequisite
- May need dependency on list extraction skill from T10

**Suggested Action:**
- VERIFY block existence and syntax
- ADD prerequisite skill or note about table → list conversion
- Consider adding table-to-list conversion as explicit skill in T10 (Lists & Tables topic)

---

#### **Issue H6.3: Widget Event Blocks (T27.G5.01, T27.G7.01)**
**Blocks Referenced:**
- `add dropdown menu` / `add button`
- `when widget [name v] clicked`
- `when widget [name v] changes`

**Verification Needed:**
- Are these exact block names correct?
- What's the full syntax for add dropdown menu (parameters for options list)?
- Do both clicked and changes events exist for all widget types?

**Suggested Action:**
- VERIFY exact block syntax from CreatiCode documentation
- UPDATE descriptions with complete block signatures including all parameters
- Add notes about which events work with which widget types

---

#### **Issue H6.4: Google Sheets Integration (T27.G7.01b)**
**Blocks Referenced:**
- `read from google sheet: url [URL] sheet name [Sheet1] range [A1:D10] into table [data v]`
- `write into google sheet: url [URL] sheet name [Sheet1] start cell [A1] from table [results v]`

**Verification Needed:**
- Are these blocks currently available in CreatiCode?
- Do they require Google OAuth authentication setup?
- What are the sharing/permission requirements?
- Is this feature available to all users or restricted?

**Issues:**
- Description mentions authentication but doesn't detail the setup process
- OAuth flow may be too complex for G7 students
- May require teacher pre-configuration

**Suggested Action:**
- VERIFY block availability and user requirements
- ADD prerequisite skill about setting up Google Sheets sharing (could be teacher-facing)
- Consider adding simplified version using pre-shared teacher templates

---

#### **Issue H6.5: Chart Drawing Blocks (Multiple Skills)**
**Blocks Referenced:**
- `draw [bar v] chart using columns [classA,classB] from table [scores v]`
- `draw [percentage v] chart using columns [...] from table [...]`
- `draw [line/bar/pie] chart using list [...]`

**Verification Needed:**
- What chart types are available: bar, line, pie, percentage - any others?
- What's the syntax difference between table-based and list-based charts?
- Are column names specified as strings or list of strings?
- What positioning/sizing parameters exist?

**Suggested Action:**
- VERIFY complete chart block family and syntax
- CREATE reference table showing: chart type, data source (list/table), use case
- STANDARDIZE descriptions across all chart-using skills

---

#### **Issue H6.6: Table Aggregation Blocks (T27.G3.01)**
**Blocks Referenced:**
- `[sum v] of column [scores] in table [data v]`
- `[average v] of column [scores] in table [data v]`
- `[median v] of column [scores] in table [data v]`
- `[minimum v] of column [scores] in table [data v]`
- `[maximum v] of column [scores] in table [data v]`

**Verification Needed:**
- Are all five aggregation types available as dropdown options in single block?
- What happens with empty tables or columns with non-numeric data?
- Do these blocks handle missing values (empty cells)?

**Suggested Action:**
- VERIFY all aggregation options exist
- ADD error handling considerations to skill descriptions
- Note data type requirements (numeric columns)

---

#### **Issue H6.7: GROUP BY Operation (T27.G5.01b)**
**Block Referenced:**
- `set table [summary v] to [average v] of column [score] in table [data v] by column [grade]`

**Verification Needed:**
- Is this the actual block syntax?
- What aggregation methods work with GROUP BY?
- Can multiple grouping columns be specified?
- What's the output table structure?

**Issues:**
- This is a very powerful database operation - G5 seems early
- Requires understanding of categorical grouping + aggregation
- Output table structure may be confusing

**Suggested Action:**
- VERIFY block syntax and capabilities
- CONSIDER moving to G6 (closer to pivot table skill complexity)
- ADD visual example of input → output table transformation

---

## MEDIUM PRIORITY ISSUES

### 7. UNCLEAR OR POORLY WORDED SKILL DESCRIPTIONS

#### **Issue M7.1: T27.G3.02 - "Build comparison statements with evidence"**
**Problem:** Title is vague - "build" could mean construct algorithmically or just write. Description clarifies but title misleads.

**Current Description:** "Learners write comparison statements like 'X has more than Y because 15 vs 10' displayed in sprite speech bubbles..."

**Issues:**
- Title doesn't mention speech bubbles or display mechanism
- "Build" suggests construction, but skill is about displaying computed comparisons
- Doesn't indicate this uses sprite say/think blocks

**Suggested Fix:**
**RENAME:** "Display comparison results with computed evidence"
**REWRITE description:** "Students use sprite say/think blocks to display comparison statements that combine text and computed values (e.g., say join ['Team A scored more: '] join [scoreA] join [' vs '] join [scoreB]). They learn to construct messages that show both the conclusion AND the supporting data, reinforcing evidence-based claims."

**Impact:** Clearer learning objective; emphasizes text concatenation skill

---

#### **Issue M7.2: T27.G5.04 - "Present findings using slides or mini reports"**
**Problem:** Skill mentions Google Slides, PowerPoint, OR CreatiCode text widgets - three very different tools with different skill requirements.

**Current Description:** "...using Google Slides, PowerPoint, or text widgets in CreatiCode..."

**Issues:**
- Mixing external tools (Google Slides) with internal CreatiCode features
- External tools require different skill sets (presentation software vs. programming)
- Unclear whether this is a coding skill or presentation skill
- Assessment would vary wildly based on tool choice

**Suggested Fix:**
**OPTION A:** Focus only on CreatiCode implementation
- **RENAME:** "Present findings using text widgets and chart screenshots"
- **REWRITE:** "Students assemble findings presentations within CreatiCode using text widgets for insights, chart blocks for visualizations, and button widgets for navigation. They create 2-3 'slides' (stage views) showing: (1) key chart, (2) main insight, (3) recommendation. This keeps all work in programming environment and practices UI design."

**OPTION B:** Create separate skills
- Keep T27.G5.04 for external presentation tools (less coding focus)
- Add new skill for CreatiCode-native presentations

**Recommended:** Option A (maintains coding focus)

**Impact:** Clarifies scope; maintains consistent tool usage

---

#### **Issue M7.3: T27.G6.04 - "Create structured summaries for AI input"**
**Problem:** Description mentions "XO" (CreatiCode's AI) but doesn't explain the structured format or why specific structure matters for AI.

**Current Description:** "...condense findings into structured text formats (key metric, insight, recommended action) that can be copied into AI assistants like XO..."

**Issues:**
- Doesn't show example of "structured format"
- Unclear what makes a format good for AI input
- "Bridging data analysis with AI prompt engineering" is vague
- Missing concrete success criteria

**Suggested Fix:**
**REWRITE description:** "Students create structured data summaries using a consistent template format: 'METRIC: [value], INSIGHT: [pattern observed], ACTION: [recommendation]'. They learn that AI assistants work better with clearly labeled, concise information rather than narrative paragraphs. Students practice copying their structured summaries into XO's chat interface and comparing AI responses to unstructured vs. structured inputs, understanding how format affects AI interpretation."

**Impact:** Provides concrete format; connects to AI interaction principles

---

#### **Issue M7.4: T27.G7.03 - "Evaluate fairness metrics across user groups"**
**Problem:** "Simple success rates or accuracy metrics" is vague - what specific calculations? How is fairness evaluated?

**Current Description:** "...compute simple success rates or accuracy metrics separately for different user groups..."

**Issues:**
- "Success rates or accuracy" is imprecise
- Doesn't define what constitutes a fairness disparity
- "Discuss any disparities" is not a programming activity
- Missing connection to T25 (AI Ethics) which likely has related content

**Suggested Fix:**
**REWRITE description:** "Students compute success rates (count of successes ÷ total attempts) separately for two or more user groups (e.g., by age range or region) using table filtering and aggregation blocks. They compare rates across groups and identify disparities (e.g., 'Group A: 80% success, Group B: 45% success = 35 percentage point gap'). They document whether differences are small (<10 points), moderate (10-25 points), or large (>25 points) and discuss potential causes, connecting to AI4K12's fairness concepts."
**ADD dependency:** T25.GX.XX (appropriate AI ethics skill from T25)

**Impact:** Provides concrete metrics; connects to ethics framework

---

### 8. SKILLS NEEDING BETTER AGE-APPROPRIATE LANGUAGE

#### **Issue M8.1: T27.G2.03 - "Identify outliers visually in small data sets"**
**Problem:** "Outliers" is technical statistics term not appropriate for Grade 2.

**Current Description:** "...point out which value looks different, explaining why 12 is unusual compared to the others."

**Issues:**
- "Outlier" is formal statistics vocabulary (typically introduced Grade 6+)
- Skill description uses appropriate language ("looks different") but title doesn't match
- G2 students should use everyday language

**Suggested Fix:**
**RENAME:** "Find the value that doesn't fit the pattern"
**REWRITE description:** "Students look at small illustrated datasets like [3, 4, 3, 12] represented as pictures or bars and identify which value is very different from the others. They explain in their own words why 12 doesn't fit the pattern of 3s and 4s. This builds intuition for what will later be called 'outliers' in statistics."

**Impact:** Age-appropriate vocabulary while maintaining concept

---

#### **Issue M8.2: T27.G4.02b - "Understand median and mode concepts"**
**Problem:** For Grade 4, "median" and "mode" are formal terms but description handles this well. However, skill could benefit from everyday analogies.

**Current Description:** Good conceptual explanation but could add concrete contexts.

**Suggested Fix:**
**ENHANCE description (add to existing):** "Students connect these concepts to everyday situations: median is like finding the 'middle kid' when lining up by height, mode is like finding the most popular lunch choice in class. They practice with small datasets (≤10 values) that can be sorted by hand and counted visually."

**Impact:** Adds relatable context; maintains formal vocabulary with scaffolding

---

### 9. UNNECESSARY SAME-GRADE DEPENDENCIES WITHIN T27

#### **Issue M9.1: T27.G4.01 depends on T27.G3.04**
**Problem:** Line graph analysis (T27.G4.01) depends on creating side-by-side bar charts (T27.G3.04). These are different chart types with no clear prerequisite relationship.

**Dependency Analysis:**
```
T27.G4.01: Analyze change over time using line graphs
└─ Depends on: T27.G3.04 (Create side-by-side bar charts for two groups)
```

**Issues:**
- Line graphs and bar charts are independent chart types
- Temporal analysis (line graphs) doesn't require multi-series comparison (side-by-side bars)
- Creates unnecessary sequencing constraint
- Both could be learned independently

**Suggested Fix:**
**REMOVE T27.G3.04 dependency from T27.G4.01**
**REPLACE with more appropriate dependencies:**
- Keep: T08.G3.01, T09.G3.01.04, T09.G3.05, T26.G3.04 (current deps)
- Add: T27.G2.02 (interpret simple line plots) - more relevant prerequisite

**Impact:** Removes unnecessary constraint; allows parallel learning

---

#### **Issue M9.2: T27.G4.04 has redundant dependencies**
**Problem:** Caption-writing skill (T27.G4.04) depends on T27.G4.01 (line graph analysis) but both are same-grade analysis skills that could be learned in either order.

**Dependency Analysis:**
```
T27.G4.04: Create narrative captions for charts
└─ Depends on: T27.G4.01 (Analyze change over time using line graphs)
└─ Also depends on: T06.G3.01, T09.G3.05, T26.G3.04
```

**Issues:**
- Caption writing is a general skill applicable to any chart type
- Doesn't specifically require line graph expertise
- Could write captions for bar charts, pictographs, etc.
- Artificially sequences two parallel G4 skills

**Suggested Fix:**
**OPTION A:** Remove T27.G4.01 dependency, keep only cross-topic deps
**OPTION B:** Keep dependency but broaden to "any chart type from G3 or G4"

**Recommended:** Option A - caption writing doesn't require specific chart type

**Impact:** Allows more flexible learning sequence

---

### 10. SKILLS NOT ALIGNED WITH TOPIC FOCUS

#### **Issue M10.1: T27.G6.04 - AI prompt engineering tangent**
**Problem:** Skill about creating structured summaries for AI input seems to drift from "Data Analysis & Storytelling" into prompt engineering (should be T25 territory).

**Current Description:** "...bridging data analysis with AI prompt engineering..."

**Issues:**
- T25 (AI Perception & Recognition) is the AI-focused topic
- T27 should focus on data storytelling, not AI interaction
- Skill valuable but may be misplaced
- Integration is good, but this feels like T25 content

**Analysis:**
This is a borderline case. The skill DOES involve structuring data findings (T27 focus), but the AI interaction aspect (T25 focus) is prominent.

**Suggested Fix:**
**OPTION A:** Keep in T27 but de-emphasize AI aspect
- Rename: "Create structured data summaries with labeled findings"
- Focus description on structured reporting format
- Mention AI as one application but not primary focus

**OPTION B:** Keep as-is, recognizing cross-topic integration is valuable
- Add clearer dependency on T25 AI skills
- Frame as integration skill that bridges topics

**Recommended:** Option A - maintain T27 focus on data communication

**Impact:** Keeps topic boundaries clearer; maintains integration value

---

## RECOMMENDED NEW SKILLS TO ADD

### For Scaffolding Gaps Identified in HIGH PRIORITY Section:

1. **T27.G3.01a: Use sum and count aggregations on table columns**
   - Placement: Between T27.G3.01b and current T27.G3.01 (renumber to T27.G3.01c)
   - Purpose: Separate simple aggregations from complex ones

2. **T27.G3.05: Recognize complete vs. incomplete data entries**
   - Placement: After T27.G3.04
   - Purpose: Build data quality literacy before G4 quality checks

3. **T27.G4.05: Create basic UI widgets (buttons and dropdowns)**
   - Placement: After T27.G4.04
   - Purpose: Teach widget creation before interactive dashboards

4. **T27.G4.06: Choose appropriate chart types for different data**
   - Placement: After T27.G4.05
   - Purpose: Explicit data visualization literacy

5. **T27.G5.03b: Calculate mode by counting frequencies**
   - Placement: After T27.G5.03 (move from G4)
   - Purpose: Separate complex mode algorithm from simple median block

6. **T27.G6.05: Create dashboard with multiple independent charts**
   - Placement: After T27.G6.04
   - Purpose: Scaffold multi-chart layouts before adding interactivity

### Additional Recommended Skills:

7. **T27.G5.05: Extract table columns into lists for specialized operations**
   - Placement: After T27.G5.01b
   - Purpose: Enable table-to-list conversion needed for moving averages
   - Description: "Students use loops to extract a specific column from a table into a list (e.g., copying all 'score' values into a scores_list). They learn that some operations (like moving averages) work on lists, not tables, requiring conversion. They practice both directions: table column → list, and list → table column."
   - Dependencies: T10.G4.01 (list operations), T27.G5.01b (GROUP BY)

---

## CREATICODE BLOCKS REQUIRING VERIFICATION

### CRITICAL PRIORITY (Core functionality):
1. **Table Operations:**
   - `add column [name] at position (n) to table [table]`
   - `add to table [table]: [value1] [value2] ...`
   - `show table [table]` / `hide table [table]`
   - `delete rows with column [name] of value [v] from table [table]`
   - `row count of table [table]`
   - `item at row (...) column [...] of table [table]`

2. **Aggregation Blocks:**
   - `[sum v] of column [scores] in table [data v]`
   - `[average v] / [median v] / [minimum v] / [maximum v]` (same block?)

3. **Chart Blocks:**
   - `draw [bar v] chart using columns [classA,classB] from table [scores v]`
   - `draw [percentage v] chart using columns [...] from table [...]`
   - Verify all chart types: bar, line, pie, percentage

### HIGH PRIORITY (Advanced features):
4. **Widget Blocks:**
   - `add button [...] at X (...) Y (...) width (...) height (...) as [name]`
   - `add dropdown menu [...]` (need full syntax)
   - `when widget [name v] clicked`
   - `when widget [name v] changes`
   - `value of widget [name v]`

5. **Advanced Table Operations:**
   - `set table [summary v] to [average v] of column [score] in table [data v] by column [grade]` (GROUP BY)
   - `pivot [data v] into [summary v] row groups [...] columns [...] methods [...]`
   - `sort table [data v] by column [score] [large to small v]`

6. **Import/Export:**
   - `export table [table] as [filename]`
   - `import file into table [table]`
   - CSV format handling

### MEDIUM PRIORITY (External integrations):
7. **Google Sheets Integration:**
   - `read from google sheet: url [URL] sheet name [Sheet1] range [A1:D10] into table [data v]`
   - `write into google sheet: url [URL] sheet name [Sheet1] start cell [A1] from table [results v]`
   - Authentication requirements?

8. **Statistical Functions:**
   - `value from [simple v] moving average window [7] of list [daily_scores v]`
   - Requires list input (not table) - confirm this limitation

9. **Table-List Conversion:**
   - Is there a built-in block for extracting table columns to lists?
   - Or must this be done manually with loops?

---

## SUMMARY STATISTICS

### Issue Counts by Priority:
- **HIGH PRIORITY:** 8 issues
  - Skills too broad: 5 issues (H1.1-H1.5)
  - Duplicate skills: 2 issues (H2.1-H2.2)
  - Missing skills: 3 gaps (H3.1-H3.3)
  - Grade placement: 1 issue (H4.1)
  - Dependency violations: 2 issues (H5.1-H5.2)
  - Block verification: 7 categories (H6.1-H6.7)

- **MEDIUM PRIORITY:** 6 issues
  - Unclear descriptions: 4 issues (M7.1-M7.4)
  - Age-appropriate language: 2 issues (M8.1-M8.2)
  - Unnecessary dependencies: 2 issues (M9.1-M9.2)
  - Topic misalignment: 1 issue (M10.1)

### Skills Requiring Changes:
- **Major rewrites:** 5 skills
- **Minor updates:** 8 skills
- **Renumbering:** 3 skills
- **New skills needed:** 7 skills

### Dependency Changes Needed:
- **Remove dependencies:** 4 cases
- **Add dependencies:** 6 cases
- **Modify dependencies:** 3 cases

---

## COMPARISON TO OTHER TOPICS

### T27 Relative Strengths:
1. **Excellent K-2 foundation** - Strong unplugged activities with physical manipulatives
2. **Good integration with CreatiCode features** - Leverages platform-specific data tools
3. **Clear progression** - Visual → statistical → interactive analysis
4. **Ethical considerations** - Fairness metrics in G7 show good integration with AI4K12

### T27 Relative Weaknesses:
1. **Widget introduction gap** - Jumps to interactive dashboards without teaching widgets first
2. **Over-bundled skills** - Several skills try to teach too much at once
3. **Statistical terminology** - Some formal terms introduced too early
4. **External tool inconsistency** - Mixes CreatiCode-native and external tools

### Recommendations Compared to Previous Topics:
- **Similar to T26** - Both have good foundational scaffolding but some advanced skills are over-complex
- **Better than T24** - Fewer dependency violations, clearer progression
- **Room for improvement** - More consistent with block verification needs seen in other topics

---

## NEXT STEPS FOR PHASE 1

### Immediate Actions:
1. **Verify all CreatiCode blocks** - Confirm syntax for 9 block categories listed above
2. **Split over-broad skills** - Implement H1.1, H1.2, H1.4, H1.5 breakdowns
3. **Fix dependency violations** - Address H5.1 and H5.2 sequencing issues
4. **Add missing foundation skills** - Implement NEW skills for H3.1, H3.2, H3.3

### Short-term Actions:
5. **Improve descriptions** - Address M7.1-M7.4 clarity issues
6. **Update age-appropriate language** - Fix M8.1-M8.2 vocabulary
7. **Remove unnecessary dependencies** - Clean up M9.1-M9.2

### Documentation Needed:
8. **Create block reference guide** - Document all T27-specific CreatiCode blocks
9. **Create progression map** - Visual showing K-8 data analysis skill progression
10. **Create assessment examples** - Sample tasks for complex skills (dashboards, GROUP BY, pivot)

---

## APPENDIX: SKILL-BY-SKILL QUICK REFERENCE

### Grade K Skills (3 total) - ✓ STRONG
- T27.GK.01: Sort objects by a rule - **GOOD** unplugged foundation
- T27.GK.02: Compare which group has more - **GOOD** builds on sorting
- T27.GK.03: Read a two-column picture chart - **GOOD** visual literacy

### Grade 1 Skills (3 total) - ✓ STRONG
- T27.G1.01: Build a pictograph from tallies - **GOOD** links T26 to T27
- T27.G1.02: Answer "how many more?" questions - **GOOD** comparative reasoning
- T27.G1.03: Tell a one-sentence story with data - **GOOD** early storytelling

### Grade 2 Skills (4 total) - ⚠ MINOR ISSUES
- T27.G2.01: Create bar charts with axes labels - **GOOD** unplugged to coding bridge
- T27.G2.02: Interpret simple line plots - **GOOD** temporal introduction
- T27.G2.03: Identify outliers visually - **FIX** M8.1 (terminology)
- T27.G2.04: Decide if data answers the question - **GOOD** critical thinking

### Grade 3 Skills (5 total) - ⚠ NEEDS FIXES
- T27.G3.01b: Create and populate data tables - **GOOD** foundation
- T27.G3.01: Compute totals and averages - **SPLIT** (H1.1)
- T27.G3.02: Build comparison statements - **RENAME** (M7.1)
- T27.G3.03: Use tables to group and count - **REWRITE** (H2.1)
- T27.G3.04: Create side-by-side bar charts - **GOOD** multi-series intro
- **MISSING:** T27.G3.05 (data quality awareness)

### Grade 4 Skills (10 total) - ⚠ MAJOR ISSUES
- T27.G4.01: Analyze change over time - **FIX DEP** (M9.1)
- T27.G4.02b: Understand median and mode - **ENHANCE** (M8.2)
- T27.G4.02c: Calculate median and mode - **SPLIT** (H1.2)
- T27.G4.02: Calculate percentages - **MOVE TO G5** (H4.1) + **FIX DEP** (H5.1)
- T27.G4.02d: Filter table rows - **GOOD** (but renumbering affects others)
- T27.G4.03: Check data quality - **GOOD**
- T27.G4.04: Create narrative captions - **FIX DEP** (M9.2)
- T27.G4.04b: Sort tables - **RENUMBER** to T27.G4.03b (H5.2)
- **MISSING:** T27.G4.05 (create widgets)
- **MISSING:** T27.G4.06 (choose chart types)

### Grade 5 Skills (7 total) - ⚠ NEEDS ADDITIONS
- T27.G5.01: Interactive dashboard - **SIMPLIFY** (H1.4)
- T27.G5.01b: GROUP BY operations - **VERIFY BLOCKS**
- T27.G5.02: Correlate two variables - **CLARIFY** (H2.2)
- T27.G5.03: Compare data from sensors - **GOOD**
- T27.G5.04: Present findings - **FOCUS** (M7.2)
- **MISSING:** T27.G5.03b (mode calculation - moved from G4)
- **MISSING:** T27.G5.05 (table to list extraction)
- **ADD FROM G4:** T27.G5.06 (percentages - moved from G4)

### Grade 6 Skills (9 total) - ⚠ VERIFICATION NEEDED
- T27.G6.01: Filter with multiple conditions - **REWRITE** (H1.3)
- T27.G6.01b: VLOOKUP operations - **VERIFY BLOCKS**
- T27.G6.02: Compare two groups - **CLARIFY** (H2.2)
- T27.G6.02b: Pivot tables - **VERIFY BLOCKS** (H6.1)
- T27.G6.03: Identify trends in time-series - **CLARIFY** (H2.2)
- T27.G6.03b: CSV export/import - **VERIFY BLOCKS**
- T27.G6.04: Structured summaries for AI - **REFOCUS** (M10.1, M7.3)
- **MISSING:** T27.G6.05 (multi-chart independent dashboards)

### Grade 7 Skills (7 total) - ⚠ BLOCK VERIFICATION
- T27.G7.01: Multi-chart linked dashboards - **ADD DEP** (H1.5)
- T27.G7.01b: Google Sheets integration - **VERIFY BLOCKS** (H6.4)
- T27.G7.02: Compare predictions to actuals - **GOOD**
- T27.G7.02b: Moving averages - **VERIFY BLOCKS** (H6.2)
- T27.G7.02c: Automate chart updates - **GOOD**
- T27.G7.03: Evaluate fairness metrics - **IMPROVE** (M7.4)
- T27.G7.04: Write findings reports - **GOOD**

### Grade 8 Skills (4 total) - ✓ STRONG (with deps on earlier fixes)
- T27.G8.01: Statistical significance - **GOOD** (advanced concepts)
- T27.G8.02: Automate report generation - **GOOD**
- T27.G8.03: Integrate with AI prompt engineering - **GOOD** integration
- T27.G8.04: Publish data stories - **GOOD** capstone

---

**END OF REPORT**
