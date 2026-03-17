# ProjectX Blueprint

## 1. What This Project Is

ProjectX is a small Python desktop utility for handling Excel-based POS support work in restaurant environments.

This tool is being built to reduce repetitive manual work done on spreadsheets before that data is ready for POS-related use.

The files handled by this tool are not machine-generated clean exports.
They are typically filled in by humans.

That means the input data may contain:

- inconsistent naming
- blank cells
- extra spaces
- wrong formats
- mixed units
- missing values
- unexpected column names
- manually typed mistakes

Because of that, this project is not just about “reading an Excel file”.
It is about building a workflow that can safely take messy human-filled spreadsheet data and turn it into something usable.

This project is also being used to rebuild the user’s Python skills through a real and useful tool.

So the project has two purposes at the same time:

1. solve real POS spreadsheet work
2. help the user relearn programming by building the solution step by step

---

## 2. What This Project Is Not

ProjectX is not:

- a full POS system
- a restaurant management platform
- an AI assistant
- a voice tool
- a cloud platform
- a complex desktop app
- a general spreadsheet editor

It is a focused utility for file-based spreadsheet preparation and transformation.

---

## 3. Core Problem This Tool Is Solving

In restaurant/POS work, data often comes in Excel sheets prepared by people.
Those sheets may later need to be:

- checked
- cleaned
- standardized
- transformed
- made ready for import or use in another workflow

Doing that manually is slow and repetitive.

The purpose of this program is to create a repeatable process where the user can:

1. choose an Excel file
2. load it safely
3. inspect its structure
4. validate whether it contains the needed data
5. clean or transform the contents
6. produce usable output for the next POS-related step

The long-term goal is not “automation for everything”.
The goal is to automate the specific spreadsheet preparation work that keeps coming up in real restaurant support workflows.

---

## 4. Real-World Assumptions About The Input Files

This project assumes the input files are:

- Excel files, not CSV
- created or filled by humans
- inconsistent in formatting
- not always structured perfectly
- likely to need validation before processing
- likely to have business meaning that matters more than just the raw cell values

This means the program must be built with defensive thinking.

The app should expect things like:

- the file opens but the sheet layout is wrong
- the required columns are missing
- numbers are stored as text
- there are extra unused columns
- headers are spelled differently than expected
- cells contain empty values where real data is needed
- user-selected files may be the wrong file entirely

So reliability and clear error handling are a core requirement, not an optional improvement.

---

## 5. What The Program Needs To Do

Based on current understanding, the program needs to support this general workflow:

### Stage 1: File Intake
The user launches the app and selects an Excel file from the computer.

The program should:

- open a file picker
- allow Excel file selection
- return the selected path
- handle the case where the user cancels

### Stage 2: File Reading
The program reads the selected Excel file successfully.

The program should:

- open the workbook safely
- read the relevant sheet or sheets
- load the data into a structure Python can work with
- fail clearly if the file cannot be read

### Stage 3: Structure Inspection
The program checks what is inside the file.

The program should be able to identify things like:

- sheet names
- row count
- column count
- column headers
- whether expected data appears to exist

### Stage 4: Validation
The program checks whether the file is usable for the intended POS workflow.

This likely includes checking:

- are the required columns present
- are key fields blank
- are the values in a usable format
- is the file shape roughly what is expected

### Stage 5: Cleaning / Standardization
The program prepares the data for reliable processing.

This may include:

- trimming spaces
- normalizing text
- handling blanks
- converting values into the right type
- standardizing headers
- removing irrelevant rows
- fixing predictable formatting issues

### Stage 6: Transformation
The program converts the input into the structure actually needed for POS work.

This is where business logic will matter most.

Examples of this kind of step may include:

- mapping user file columns to expected POS columns
- reformatting units or values
- preparing import-ready output
- generating a cleaner final sheet
- building derived values from the original input

### Stage 7: Output
The program produces usable output.

That output might be:

- a cleaned workbook
- a transformed workbook
- a simplified sheet
- a file ready for another step in the POS workflow
- a status summary explaining success/failure

---

## 6. Current Known Reality

So far, the project direction is still early.

The working idea is clear:
build a small Excel-processing desktop utility for POS-related spreadsheet workflows.

But the exact business transformation rules are not fully locked yet.

That means the project currently has two layers:

### Layer A: Technical Foundation
This includes:

- app launch
- file picker
- file reading
- basic summaries
- error handling

### Layer B: Business Workflow Logic
This includes:

- deciding the exact sheet format being targeted
- identifying required columns
- deciding the cleaning rules
- deciding the transformation rules
- deciding what the final output should look like

Right now, Layer A is underway.
Layer B still needs to be written down properly.

---

## 7. What The User Needs From Codex / ChatGPT

This project is not just about finishing fast.
It is also about learning and retaining understanding.

Because of that, help inside this project must follow these rules.

### Code Ownership
- The user writes the project code.
- Codex should not modify code files unless explicitly told to do so.
- Codex may freely help with planning, documentation(README.md), review, debugging guidance, and explanations.

### Teaching Style
Codex should:

- go one step at a time
- explain the purpose of the next step before giving code
- explain logic and concepts before discussing code structure
- avoid giving full code structure or near-complete implementations unless the user explicitly asks for that level of help
- explain inputs, outputs, and logic clearly
- assume the user may be rusty with Python syntax
- use small examples where useful
- help the user think, not just paste answers

### Default Workflow
When helping with implementation, Codex should usually:

1. explain the next small goal
2. explain how that part should work
3. let the user attempt it
4. review and improve it together

### Session Awareness
- At the start of each new user request, Codex should first check the current project files so it stays aware of the latest state of the codebase.
- Codex should not assume the files are unchanged from the previous message or session.

### What To Avoid
Codex should avoid:

- taking over implementation without permission
- rewriting code silently
- solving everything immediately when the user is trying to learn
- introducing unnecessary complexity
- suggesting extra libraries without a clear reason
- turning the project into something bigger than needed

---

## 8. Build Philosophy

This project should stay:

- small
- useful
- understandable
- modular
- practical

The order of priority is:

1. make it run
2. make it reliable
3. make it understandable
4. make it useful for real work
5. improve convenience later

Clarity is more important than cleverness.
A simple solution that is easy to debug is better than an advanced one that is harder to follow.

---

## 9. Current Scope

The current scope is the early foundation of an Excel-processing utility.

### In Scope Right Now
- launching the app
- selecting an Excel file
- confirming the file path
- reading spreadsheet data
- showing a basic summary
- handling errors clearly
- preparing for later validation and transformation steps

### Not In Scope Right Now
- CSV support
- voice features
- AI assistant features
- advanced UI
- database design
- login systems
- cloud sync
- full POS platform features
- unrelated automation features
- “nice to have” features that distract from the core workflow

---

## 10. Immediate Build Goal

The immediate goal is to get the program into a reliable state where it can:

- launch successfully
- accept an Excel file input
- confirm that a file was selected
- read the spreadsheet successfully
- report useful information about the loaded data
- fail clearly if something goes wrong

This is the minimum base that must be solid before real business processing begins.

---

## 11. Near-Term Milestones

### Milestone 1: Basic App Flow
- app runs
- file picker opens
- user selects a file
- selected file path is returned

### Milestone 2: Excel Reading
- app reads Excel input
- workbook/sheet loads successfully
- basic load summary is shown
- file-read failures are handled cleanly

### Milestone 3: Validation Layer
- required columns can be checked
- missing/invalid structure can be reported
- user gets clear feedback if the file is not usable

### Milestone 4: Cleaning Layer
- text cleanup
- blank handling
- normalization of values
- basic data standardization

### Milestone 5: First Real POS Transformation
- define one exact real-world spreadsheet workflow
- convert input data into the required output structure
- produce usable output from that workflow

### Milestone 6: Better Feedback
- clearer success messages
- clearer failure messages
- easier-to-understand run results

---

## 12. Current Progress

Known current progress:

- `main.py` already calls the file-reading layer after a file is selected
- the app can now read a selected Excel file with pandas
- the app now returns a basic multi-line summary with row count, column count, and column names
- the app now returns a clearer message when an invalid file is selected
- blank values in selected fields are expected and do not prevent a successful read
- `pytest` tests now exist for the no-file-selected case and an invalid-file case
- a success-case test for valid Excel input has been started but is not complete yet
- the project is already split into smaller files instead of one large script
- the next immediate improvement is expanding early automated test coverage

That means the project is already past the absolute start.
The next work should strengthen reliability before adding more logic.

---

## 13. Current Folder Structure

```text
ProjectX/
├── main.py
├── PROJECT_BLUEPRINT.md
└── src/
    ├── read_file.py
    └── select_file.py
