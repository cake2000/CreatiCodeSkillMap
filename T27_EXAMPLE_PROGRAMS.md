# T27 Data Analysis & Visualization - Example Programs

## Example 1: Creating and Visualizing a Simple Dataset

**Goal**: Create a table with student data and visualize it as a chart

```
when green flag clicked
    // Create table structure
    delete all columns from table [students v]
    add column [name] at position (1) to table [students v]
    add column [score] at position (2) to table [students v]

    // Add data rows
    add to table [students v]: [Alice] [85] [] [] [] [] [] [] [] [] [] []
    add to table [students v]: [Bob] [92] [] [] [] [] [] [] [] [] [] []
    add to table [students v]: [Charlie] [78] [] [] [] [] [] [] [] [] [] []
    add to table [students v]: [Diana] [95] [] [] [] [] [] [] [] [] [] []

    // Display table on stage
    show table [students v]

    // Create visualization
    draw [bar v] chart using columns [score] from table [students v] x (200) y (150) width (200) height (200)
```

---

## Example 2: Data Analysis - Computing Statistics

**Goal**: Calculate average, min, and max scores

```
when green flag clicked
    set [average_score v] to [average v] of column [score] in table [students v]
    set [min_score v] to [smallest v] of column [score] in table [students v]
    set [max_score v] to [largest v] of column [score] in table [students v]

    say (join [Average: ] [average_score]) for (2) seconds
    say (join [Min: ] [min_score]) for (2) seconds
    say (join [Max: ] [max_score]) for (2) seconds
```

---

## Example 3: Filtering and Searching Data

**Goal**: Find students with scores above 90

```
when green flag clicked
    set [search_row v] to (1)

    repeat until [search_row] > [row count of table [students v]]
        set [current_score v] to item at row [search_row] column [score] of table [students v]

        if [current_score] > [90] then
            set [student_name v] to item at row [search_row] column [name] of table [students v]
            say (join [High scorer: ] [student_name])
        end

        change [search_row v] by (1)
    end
```

---

## Example 4: GROUP BY Aggregation

**Goal**: Calculate average score by gender

```
when green flag clicked
    // Setup: t1 has columns: name, gender, score

    // Create summary table with GROUP BY
    set table [summary v] to [average v] of column [score] in table [t1 v] by column [gender]

    // Now summary table has:
    // Column 1: gender values (M, F, etc.)
    // Column 2: average scores for each gender

    show snapshot of table [summary v] from row (1) to (10) with style [style1 v] [#1E54B6FF]
```

**Result** (if data exists):
```
gender | score
-------|------
M      | 94
F      | 99
```

---

## Example 5: Pivot Table Analysis

**Goal**: Analyze scores by both gender and grade level

```
when green flag clicked
    // Setup: t1 has columns: name, gender, grade, score

    // Create pivot table
    pivot [t1 v] into [summary v] row groups [gender,grade] columns [score] methods [average]

    // Result: summary table shows average scores grouped by gender and grade

    show snapshot of table [summary v] from row (1) to (20) with style [style2 v] [#FF6B6BFF]
```

**Result**:
```
gender | grade | score
-------|-------|-------
M      | 9     | 88.5
M      | 10    | 92.0
F      | 9     | 91.5
F      | 10    | 96.0
```

---

## Example 6: Data Sorting

**Goal**: Sort students by score (highest to lowest)

```
when green flag clicked
    // Sort in descending order (large to small)
    sort table [students v] by column [score] [large to small v]

    // Display sorted results
    show table [students v]
```

---

## Example 7: Lookup Operation (VLOOKUP)

**Goal**: Find a student's score by name

```
when green flag clicked
    set [search_name v] to [Alice]

    set [found_score v] to item in column [score] of [students v] where column [name] equals [search_name]

    if [found_score] = [0] then
        say [Student not found]
    else
        say (join [Score for Alice: ] [found_score])
    end
```

---

## Example 8: Creating Multiple Chart Types

**Goal**: Visualize same data in different ways

```
when green flag clicked
    // Line chart - showing trend
    draw [line v] chart using columns [score] from table [students v] x (100) y (100) width (150) height (150)

    wait (3) seconds

    // Bar chart - comparing values
    draw [bar v] chart using columns [score] from table [students v] x (300) y (100) width (150) height (150)

    wait (3) seconds

    // Pie chart - showing composition
    draw [pie v] chart using category [name] and value [score] from table [students v] x (200) y (300) width (150) height (150)
```

---

## Example 9: Data Import and Processing

**Goal**: Import CSV, clean, and visualize

```
when green flag clicked
    // Import from file
    import file into table [raw_data v]

    // Delete rows with missing data
    delete rows with column [score] of value [] from table [raw_data v]

    // Sort by score
    sort table [raw_data v] by column [score] [large to small v]

    // Visualize top 10
    show snapshot of table [raw_data v] from row (1) to (10) with style [style1 v] [#1E54B6FF]

    // Export cleaned data
    export table [raw_data v] as [cleaned_scores]
```

---

## Example 10: Google Sheets Integration

**Goal**: Read from Google Sheet, process, and write results back

```
when green flag clicked
    // Read data from Google Sheet
    read from google sheet: url [https://docs.google.com/spreadsheets/d/ABC123...] sheet name [data] range [A1:D100] into table [imported_data v]

    // Process: Calculate average score
    set [avg_score v] to [average v] of column [score] in table [imported_data v]

    // Create summary table
    set table [summary v] to [average v] of column [score] in table [imported_data v] by column [category]

    // Write results back to Google Sheet
    write into google sheet: url [https://docs.google.com/spreadsheets/d/ABC123...] sheet name [results] starting cell [A1] from table [summary v]
```

---

## Example 11: Cloud Database Operations

**Goal**: Query cloud database, modify data, and save

```
when green flag clicked
    // Fetch students with score > 80 from cloud
    fetch from collection [students v] into table [filtered_students v] where <cond (field [score]) [gt v] [80]> limit (100) sort by (field [name]) [1 v] () [1 v]

    // Update a score
    replace item at row (1) column [score] of table [filtered_students v] with [98]

    // Save back to cloud database
    update collection [students v] from table [filtered_students v]
```

---

## Example 12: Multi-Step Data Analysis Workflow

**Goal**: Complete data science workflow

```
when green flag clicked
    // Step 1: Load data
    read from google sheet: url [https://docs.google.com/spreadsheets/d/...] sheet name [raw] range [A1:E500] into table [raw_data v]

    // Step 2: Clean data
    delete rows with column [age] of value [] from table [raw_data v]
    sort table [raw_data v] by column [age] [small to large v]

    // Step 3: Analyze
    set [avg_age v] to [average v] of column [age] in table [raw_data v]
    set table [by_category v] to [average v] of column [age] in table [raw_data v] by column [category]

    // Step 4: Visualize
    draw [bar v] chart using columns [age] from table [by_category v] x (240) y (180) width (300) height (250)

    // Step 5: Export
    export table [by_category v] as [analysis_results]
    write into google sheet: url [https://docs.google.com/spreadsheets/d/...] sheet name [summary] starting cell [A1] from table [by_category v]
```

---

## Example 13: Row-by-Row Data Transformation

**Goal**: Apply formula to each row

```
when green flag clicked
    // Assume table has: quantity, unit_price, total

    repeat (row count of table [orders v])
        set [qty v] to item at row [counter] column [quantity] of table [orders v]
        set [price v] to item at row [counter] column [unit_price] of table [orders v]

        set [total_price v] to [qty] * [price]

        replace item at row [counter] column [total] of table [orders v] with [total_price]

        change [counter v] by (1)
    end
```

---

## Example 14: Progress Bar Visualization

**Goal**: Show data upload progress

```
when green flag clicked
    add progress bar as (0) out of total (100) at x (240) y (180) width (400) height (40) color [#4CAF50FF] background [#EEEEEE FF] border width (2) color [#000000FF] as [upload_progress]

    repeat (100)
        change [upload_progress v] by (1)

        // Simulate work
        wait (0.1) seconds
    end

    say [Upload complete!]
```

---

## Example 15: Table Copy and Append for Report Generation

**Goal**: Combine multiple data sources into single report

```
when green flag clicked
    // Copy department A data
    copy table [dept_a_data v] into [combined_report v]

    // Append department B data
    append table [dept_b_data v] to [combined_report v]

    // Append department C data
    append table [dept_c_data v] to [combined_report v]

    // Sort combined report by date
    sort table [combined_report v] by column [date] [large to small v]

    // Display and export
    show snapshot of table [combined_report v] from row (1) to (50) with style [style3 v] [#2196F3FF]
    export table [combined_report v] as [monthly_report]
```

---

## Example 16: Moving Average for Trend Analysis

**Goal**: Calculate moving average of stock prices

```
when green flag clicked
    // prices list: [100, 102, 101, 105, 107, 106, 108, ...]

    set [moving_avg_list v] to value from [simple v] moving average window [7] of list [prices v]

    // moving_avg_list now contains smoothed trend
    // Can be used for visualization
    draw [line v] chart using list [moving_avg_list v] x (240) y (180) width (300) height (200)
```

---

## Example 17: Conditional Row Deletion

**Goal**: Remove outliers or invalid data

```
when green flag clicked
    // Delete all rows where score is 0 (invalid)
    delete rows with column [score] of value [0] from table [raw_scores v]

    // Delete all rows where age is less than 18
    set [temp_age v] to (1)

    repeat until [temp_age] > [row count of table [raw_scores v]]
        set [current_age v] to item at row [temp_age] column [age] of table [raw_scores v]

        if [current_age] < [18] then
            delete row [temp_age] of table [raw_scores v]
        end

        change [temp_age v] by (1)
    end
```

---

## Example 18: Database In-Place Update

**Goal**: Update multiple records at once in cloud database

```
when green flag clicked
    // Mark all orders for customer "John Smith" as processed
    update collection [orders v] in-place where <cond (field [customer_name]) [eq v] [John Smith]> set (field [status]) to (processed) set (field [processed_date]) to (12/15/2024) set () to () set () to ()
```

---

## Example 19: Percentage Chart for Composition

**Goal**: Show budget allocation

```
when green flag clicked
    // Create budget data
    delete all columns from table [budget v]
    add column [category] at position (1) to table [budget v]
    add column [amount] at position (2) to table [budget v]

    add to table [budget v]: [Salary] [50000] [] [] [] [] [] [] [] [] [] []
    add to table [budget v]: [Rent] [15000] [] [] [] [] [] [] [] [] [] []
    add to table [budget v]: [Equipment] [10000] [] [] [] [] [] [] [] [] [] []
    add to table [budget v]: [Other] [5000] [] [] [] [] [] [] [] [] [] []

    // Visualize as percentage chart
    draw [percentage v] chart using category [category] and value [amount] from table [budget v] x (240) y (180) width (300) height (300)
```

---

## Example 20: Database with Complex WHERE Conditions

**Goal**: Advanced filtering with multiple conditions

```
when green flag clicked
    // Fetch high-value orders from recent dates
    fetch from collection [orders v] into table [high_value_orders v] where <cond (<cond (field [total]) [gt v] [1000]> and <cond (field [date]) [gt v] [2024-01-01]>)> limit (50) sort by (field [total]) [-1 v] () [1 v]

    show snapshot of table [high_value_orders v] from row (1) to (20) with style [style4 v] [#FF9800FF]
```

---

**Note**: These examples demonstrate the breadth of data operations available. Actual block syntax in CreatiCode may have slight variations. Always refer to official documentation for exact syntax.
