# ProjectX

ProjectX is a Python spreadsheet workflow tool for restaurant and POS support work.

The current focus is the `Menu Items` workflow: selecting an Excel file, reading it safely, validating the expected structure, cleaning the data, and preparing for downstream population work.

## Current Features

- select an `.xlsx` file through the desktop picker
- read the workbook with `pandas`
- stop cleanly if the file cannot be read
- validate the sheet against the expected `Menu Items` headers
- trim whitespace on the current safe set of text-like columns
- remove exact duplicates by `ItemName` and `Price`
- surface same-name rows that still need review after exact-duplicate cleanup

## Project Structure

- `main.py`: current entry point for the menu-items flow
- `src/select_file.py`: file selection
- `src/read_file.py`: Excel read logic and error handling
- `src/validation.py`: expected column list and structure validation
- `src/clean_file.py`: whitespace trimming and duplicate cleanup
- `src/populate.py`: early draft of blank-only default filling
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

The project already has the core read -> validate -> trim -> duplicate-clean flow for `Menu Items`.

The next major development area is population logic in [`src/populate.py`](/c:/Users/ADMIN/Documents/ProjectX/src/populate.py#L1), especially blank-only default filling and rule-based handling for fields like `KitchenPrinter`.
