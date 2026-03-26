# ProjectX

ProjectX is a small Python desktop utility for restaurant and POS spreadsheet support work.

The current build is focused on the first working path for the `Menu Items` module: choose an Excel file, read it safely, validate its structure against the expected header set, and stop cleanly when the file cannot be read.

## Current Status

The project can currently:

- open a file picker for `.xlsx` files
- handle the case where no file is selected
- read an Excel file with `pandas`
- stop cleanly when the selected file cannot be read
- validate a successfully read file against the expected `Menu Items` headers
- report which required headers are missing
- return a clearer message when the selected file cannot be read as Excel
- run `pytest` tests for the earlier read-file paths, though the success-path test now needs updating for the DataFrame-based flow

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

- keep the `Menu Items` module moving through one clean working path
- build the next validation/cleaning step after structure validation
- update tests and docs to match the newer DataFrame-based read flow
