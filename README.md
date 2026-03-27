# ProjectX

ProjectX is a small Python desktop utility for restaurant and POS spreadsheet support work.

Right now the project is focused on the `Menu Items` module:

- select an `.xlsx` file
- read it safely with `pandas`
- stop cleanly if the file cannot be read
- validate the file against the expected `Menu Items` header list

## Current Entry Point

Run the app:

```powershell
python main.py
```

Run tests:

```powershell
pytest
```

## Current Code Areas

- `main.py`: top-level flow
- `src/select_file.py`: file picker
- `src/read_file.py`: file reading and read errors
- `src/validation.py`: structure validation for `Menu Items`
- `src/clean_file.py`: early duplicate-check stub
- `tests/test_read_file.py`: current read-file tests

## Current Status

- structure validation is wired into the app
- duplicate cleaning is started but not wired in yet
- `read_file()` now returns a DataFrame on success
- the read-file success test is stale and needs updating

## Project Docs

- `README.md`: quick repo overview
- `CONTEXT.md`: Codex handoff context
- `NEXT_STEPS.md`: immediate next work
- `PROJECT_BLUEPRINT.md`: roadmap and longer-term direction
- `DOCS_SUBAGENT.md`: docs-only update rules
