# ProjectX Next Steps

## Purpose

This file is the short-term progress tracker for ProjectX.

Use it to answer three things quickly:

- what currently works
- what still feels rough
- what the next small step should be

## Current Working State

The project currently:

- opens a file picker for `.xlsx` files
- returns `"No file selected"` if the picker is cancelled
- passes the selected file path into the file-reading layer
- reads an Excel file with `pandas`
- returns a summary with row count, column count, and column names
- returns a clearer invalid-file message when a fake or unreadable Excel file is selected
- prints the returned message in `main.py`
- has `pytest` coverage for the no-file-selected, invalid-file, and valid-file cases

## Current File Roles

- `main.py`: top-level app flow
- `src/select_file.py`: Excel file selection
- `src/read_file.py`: no-file checks and Excel reading
- `tests/test_read_file.py`: read-file behavior tests

## Current Notes

The project is still in an early learning-oriented stage.

Known rough edges:

- `read_file()` returns plain strings for both success and failure paths
- the invalid-file message still includes raw exception text
- automated test coverage is still small

## Immediate Next Step

Strengthen the tests around the file-reading layer before adding more business logic.

The next best tests are:

- a test that locks down the exact summary format
- a test with blank values that still loads successfully
- a test with unexpected columns so behavior is documented before validation rules exist

## After That

Once the tests are a little stronger, the next likely improvements are:

1. make file-read error messages cleaner
2. make the return behavior more consistent
3. begin basic validation for required columns

## Update Rule

Review this file after any meaningful code change or project checkpoint.

When updating it, keep it factual:

- what changed
- what currently works
- what the next step is
- what is intentionally still unfinished
