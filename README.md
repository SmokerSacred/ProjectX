# ProjectX

ProjectX is a small Python desktop utility for restaurant and POS spreadsheet support work.

The current build is focused on one simple foundation: choose an Excel file, read it safely, and report a basic structural summary before deeper validation or cleaning logic is added.

## Current Status

The project can currently:

- open a file picker for `.xlsx` files
- handle the case where no file is selected
- read an Excel file with `pandas`
- return a simple multi-line summary of row count, column count, and column names
- return a clearer message when the selected file cannot be read as Excel
- run `pytest` tests for the no-file-selected, invalid-file, and valid-file paths

## Project Docs

- `README.md`: quick overview and current entry points
- `CONTEXT.md`: short handoff context for future Codex chats
- `PROJECT_BLUEPRINT.md`: stable project goals, assumptions, and scope
- `NEXT_STEPS.md`: current progress snapshot and recommended next work
- `DOCS_SUBAGENT.md`: rules for a docs-only subagent that updates project documentation

## Run The Project

```powershell
python main.py
```

## Run Tests

```powershell
pytest
```

## Current Focus

- improve file-read error handling without adding unnecessary complexity
- expand early test coverage around summary output and messy spreadsheet inputs
- prepare for a later validation layer for required columns and file structure
