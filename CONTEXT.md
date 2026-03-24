# ProjectX Context

This file is the fastest way to hand ProjectX context to Codex in a new chat.

## Project Purpose

ProjectX is a small Python desktop utility for restaurant and POS spreadsheet support work.

The goal is to take messy human-filled Excel files and move toward a repeatable workflow for:

- selecting a workbook
- reading it safely
- checking whether the structure is usable
- cleaning or standardizing data later
- preparing the data for downstream POS-related work

## Current Architecture

- `main.py` drives the top-level flow
- `src/select_file.py` opens the Excel file picker
- `src/read_file.py` handles the no-file case and reads Excel data with `pandas`
- `tests/test_read_file.py` covers the current read-file behavior with `pytest`

## Current Behavior

Right now the project can:

- open a file picker limited to `.xlsx`
- return `"No file selected"` if the picker is cancelled
- read a selected Excel file with `pandas`
- return a text summary containing row count, column count, and column names
- return a friendly invalid-file message when a fake or unreadable Excel file is selected

## Current Constraints

- the project is intentionally small and learning-oriented
- clarity is preferred over cleverness
- reliability comes before convenience features
- business validation rules are not fully defined yet
- code changes should stay incremental and easy to understand

## Working Style

When helping on this project:

- prefer small steps over large rewrites
- explain logic clearly when teaching is useful
- avoid broad feature expansion outside the spreadsheet workflow
- treat the docs as a running record of real progress, not aspirational plans

## Useful Commands

```powershell
python main.py
pytest
```

## Documentation Update Rule

If the project changes meaningfully, update:

- `README.md` for the quick overview if user-facing behavior changed
- `CONTEXT.md` for new-chat handoff context
- `NEXT_STEPS.md` for the current snapshot and immediate next work
