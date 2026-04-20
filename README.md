# ProjectX

ProjectX is a Python spreadsheet workflow tool for restaurant and POS support work.

The current focus is the `Menu Items` workflow: selecting an Excel file, reading it safely, validating the expected structure, cleaning the data, populating blank defaults, and exporting a processed workbook.

## Current Features

- select an `.xlsx` file through the desktop picker
- read the workbook with `pandas`
- stop cleanly if the file cannot be read
- validate the sheet against the expected `Menu Items` headers
- trim whitespace on the current safe set of text-like columns
- remove exact duplicates by `ItemName` and `Price`
- surface same-name rows that still need review after exact-duplicate cleanup
- fill blank default fields without overwriting existing values
- infer `KitchenPrinter` as `KOT` or `BOT` when that field is blank and `PrintOnKot` is `Yes`
- export a processed Excel file next to the source workbook
- highlight duplicate-review rows and prefilled cells in the exported workbook
- create numbered split workbook copies when the processed export exceeds the 500-row POS limit

## Project Structure

- `main.py`: current entry point for the menu-items flow
- `src/select_file.py`: file selection
- `src/read_file.py`: Excel read logic and error handling
- `src/validation.py`: expected column list and structure validation
- `src/clean_file.py`: whitespace trimming and duplicate cleanup
- `src/populate.py`: blank-only default filling and conditional `KitchenPrinter` handling
- `src/export.py`: processed workbook export and highlight styling
- `global_src/row_limit.py`: shared workbook splitting for oversized exports
- `tests/`: current automated tests
- `CONTEXT.md`: future-Codex handoff context and user rules
- `NEXT_STEPS.md`: immediate next work
- `PROJECT_BLUEPRINT.md`: roadmap and product direction

## Run The App

```powershell
python main.py
```

## Run Tests

```powershell
pytest
```

## Current Status

The project already has the core read -> validate -> trim -> duplicate-clean -> populate -> export flow for `Menu Items`, including workbook highlighting and conditional row-limit splitting.

The next major development area is hardening the current flow with broader real-file testing, better messaging, and practical export tests.
