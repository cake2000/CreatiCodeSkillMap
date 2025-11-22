# T12 Quick Fixes Required - Executive Summary

## CRITICAL ISSUES FOUND: 3

### 🔴 ISSUE 1: Custom Block Syntax is WRONG
**Skills:** T12.G3.05, T12.G4.02, T12.G4.03, T12.G4.05

**Problem:** Skills say "use the define block and call block" - This is INCORRECT

**CreatiCode Reality:**
- `define (block name)` is ONE syntax construct (not a separate "define block")
- `call block name` is the call syntax (not a separate "call block")
- Students don't "use the define block" - they create a custom block using define syntax

**Example Fix for T12.G3.05:**
```
OLD: "create a custom block using the 'define' block and call it using the 'call' block"
NEW: "create custom blocks using define syntax (e.g., define (draw square)) and call them using call syntax (e.g., call draw square)"
```

---

### 🔴 ISSUE 2: Parameter Syntax is WRONG
**Skills:** T12.G4.05

**Problem:** Description confuses definition syntax, argument references, and calling syntax

**CreatiCode Reality:**
- **Define with params:** `define (draw polygon (sides) (size))` ← params in parentheses
- **Use inside:** `(argument (sides))` ← reference the parameter value
- **Call with args:** `call draw polygon [4] [100]` ← args in square brackets

**Fix:**
```
OLD: "use the 'argument' block inside the definition and pass values when calling the block (e.g., 'draw polygon [sides] [size]')"

NEW: "create custom blocks that accept parameters by including them in the definition signature (e.g., define (draw polygon (sides) (size))). Inside the block, use (argument (sides)) to reference parameter values. When calling, pass values using square brackets: call draw polygon [4] [100]."
```

---

### 🔴 ISSUE 3: Return Value Syntax is WRONG
**Skills:** T12.G5.05

**Problem:** Says "call them using 'report [block name]'" - INCORRECT

**CreatiCode Reality:**
- **Inside definition:** `return [VALUE]` ← returns a value
- **Call reporter block:** `report block-name [args]` ← NOT "report [block name]"
- Must use full signature with arguments

**Fix:**
```
OLD: "call them using 'report [block name]'"
NEW: "call them using 'report block-name [args]' (e.g., report calculate distance [100] [200])"
```

---

## HIGH PRIORITY ISSUES: 3

### ⚠️ ISSUE 4: G3.01 Too Advanced for First Comment
**Skills:** T12.G3.01

**Problem:** First commenting skill asks students to explain "blocks that are not immediately obvious"

**Fix:** Simplify to labeling/simple explanations
```
OLD: "add their first comment explaining a block that is not immediately obvious in purpose"
NEW: "add simple comments that label or explain parts of their script (e.g., '// Move the cat' or '// Check if score > 10')"
```

---

### ⚠️ ISSUE 5: Header Comment Uses Wrong Syntax
**Skills:** T12.G3.02

**Problem:** Example uses "# " but CreatiCode uses "// "

**Fix:**
```
OLD: "e.g., '# When the green flag is clicked...'"
NEW: "e.g., '// Game initialization: sets lives to 3, resets score, shows start screen'"
```

---

### ⚠️ ISSUE 6: External Documentation Too Vague
**Skills:** T12.G5.01

**Problem:** "external documentation" could mean many things

**Fix:** Specify CreatiCode's Project Instructions feature
```
OLD: "using CreatiCode's project notes or instructions feature"
NEW: "using CreatiCode's Project Instructions feature that explains: (1) what the project does, (2) how to use it (controls/interactions), and (3) what the main features are"
```

---

## COMPLETE FIX LIST

### Files to Update: `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md`

### Critical Fixes (Do First):

**T12.G3.05 - Create and use a simple custom block**
```yaml
OLD Description: "Students learn to create a custom block using the 'define' block and call it using the 'call' block. They create a simple custom block with a descriptive name (e.g., 'draw square') that groups 3-5 related blocks, then call it from their main script. This introduces the concept of reusable code modules."

NEW Description: "Students learn to create custom blocks using CreatiCode's define syntax and call them using call syntax. In the My Blocks category, they create a simple custom block with a descriptive, action-based name (e.g., define (draw square)) that groups 3-5 related blocks, then call it from their main script using call draw square. This introduces the concept of reusable code modules."
```

**T12.G4.05 - Add input parameters to a custom block**
```yaml
OLD Description: "Students create custom blocks that accept input parameters using the 'define' block with parameter placeholders. They learn to use the 'argument' block inside the definition and pass values when calling the block (e.g., 'draw polygon [sides] [size]')."

NEW Description: "Students create custom blocks that accept input parameters by including them in the definition signature (e.g., define (draw polygon (sides) (size))). Inside the custom block, they use (argument (sides)) and (argument (size)) to reference parameter values. When calling the block, they pass values using square brackets: call draw polygon [4] [100]."
```

**T12.G5.05 - Use return values in custom blocks**
```yaml
OLD Description: "Students create custom reporter blocks that return values using the 'return' block inside a custom block definition, and call them using 'report [block name]'. They learn when to use reporter blocks vs. stack blocks (e.g., 'calculate distance' returns a number vs. 'move to target' performs an action)."

NEW Description: "Students create custom reporter blocks that return values using 'return [VALUE]' inside the definition, and call them using 'report block-name [args]'. They learn when to use reporter blocks vs. stack blocks (e.g., report calculate distance [100] [200] returns a number vs. call move to target performs an action)."
```

---

### High Priority Fixes (Do Next):

**T12.G3.01 - Add a comment to explain a block in a script**
```yaml
OLD Description: "Students use the comment block (// [text]) to add their first comment explaining a block that is not immediately obvious in purpose (e.g., a simple loop or condition). This gateway skill introduces the concept of documenting code for others to understand using CreatiCode's comment feature."

NEW Description: "Students use the comment block (// [text]) from the My Blocks category to add simple comments that label or explain parts of their script (e.g., '// Move the cat' or '// Check if score > 10'). This introduces the concept of documenting code for others to understand."
```

**T12.G3.02 - Create a header comment for a script**
```yaml
OLD Description: "Students add a comment block at the very top of a script that summarizes its purpose, triggering event, and role in the larger program (e.g., '# When the green flag is clicked, initialize the game: set lives to 3, reset score, show the start screen'). This is a first step toward external documentation."

NEW Description: "Students add a comment block (// [text]) at the beginning of a script, right after the hat block, that summarizes the script's purpose and role in the larger program (e.g., '// Game initialization: sets lives to 3, resets score, shows start screen'). This is a first step toward systematic documentation."
```

**T12.G5.01 - Write a project description explaining what the program does**
```yaml
OLD Description: "Students write a clear project description (using CreatiCode's project notes or instructions feature) that explains: what the project does, how to use it (controls/interactions), and what the main features are. This is the first experience with external documentation for users."

NEW Description: "Students write a clear project description using CreatiCode's Project Instructions feature that explains: (1) what the project does, (2) how to use it (controls/interactions), and (3) what the main features are. This user-facing documentation helps others understand the project without reading the code."
```

---

## WHY THESE FIXES MATTER

### 1. **Accuracy**: Students will learn correct CreatiCode syntax
   - Currently, skills teach incorrect mental models
   - Students would be confused when they try to "use the define block"

### 2. **Clarity**: Examples will match actual block syntax
   - `define (name)` vs "the define block"
   - `// comment` vs "# comment"

### 3. **Scaffolding**: First commenting skill is gentler
   - Label first, explain later
   - Matches how teachers actually introduce comments

### 4. **Specificity**: Clear artifacts for assessment
   - "Project Instructions feature" (specific)
   - Not "project notes or instructions" (vague)

---

## VALIDATION

All fixes have been validated against:
- ✅ `/media/binyu/USB2/ScratchCopilot/blockdes8.txt` (CreatiCode block definitions)
- ✅ Actual block syntax from procedures_definition, procedures_call, procedures_argument, procedures_return, procedures_comment
- ✅ Phase 1 dependency analysis (no new violations introduced)
- ✅ Grade level appropriateness (no changes to grade placement)

---

## NEXT STEPS

1. Review and approve these fixes
2. Update `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md`
3. Run validation to ensure no syntax errors
4. Consider Medium Priority fixes in T12_CREATICODE_ACCURACY_ANALYSIS.md for further polish

**Total Skills Updated:** 6 out of 36 T12 skills (16.7%)
**Impact:** CRITICAL - These skills are foundational to all custom block usage
