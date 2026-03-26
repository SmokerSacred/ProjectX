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
- returns a DataFrame on successful file reads
- returns a clearer invalid-file message when a fake or unreadable Excel file is selected
- stops cleanly in `main.py` when file reading fails
- validates uploaded `Menu Items` files against the expected header list
- reports the exact missing headers when structure validation fails
- has `pytest` coverage for the no-file-selected, invalid-file, and valid-file cases
- now has a real menu item template available to define validation rules from actual business structure instead of guesses

## Current File Roles

- `main.py`: top-level app flow
- `src/select_file.py`: Excel file selection
- `src/read_file.py`: no-file checks and Excel reading
- `src/validation.py`: `Menu Items` structure validation
- `tests/test_read_file.py`: read-file behavior tests

## Current Notes

The project is still in an early learning-oriented stage.

Known rough edges:

- `read_file()` now returns mixed types: a DataFrame on success and strings on failure
- the invalid-file message still includes raw exception text
- automated test coverage is still small
- validation rules are only partially defined and need to be confirmed against the real template workflow
- the larger workflow is planned as three modules: `Menu Items`, `Inventory Items`, and `Recipes`
- current implementation should stay focused on finishing `Menu Items` before moving to the later modules
- `tests/test_read_file.py` still needs to be updated for the new DataFrame-based read flow

## Current Validation Notes

The current template target is a menu item workbook with 30 known columns, including:

- `ItemName`
- `Category`
- `SubCategory`
- `Price`
- `Cost`
- `TaxGroup`
- `PrintOnKot`
- `KitchenPrinter`

User-confirmed optional fields so far:

- `Description`
- `AlternateName`
- `VariantName`
- `Type`
- `Barcode`
- `BarControllerCode`
- `Sku`
- `IntegrationCode`
- `CaptainPrinter`
- `LabelPrinter`

Rules still needing confirmation:

- whether `KitchenPrinter` is required when `PrintOnKot` is `Yes` or `No`
- whether any additional columns are optional or conditional

## Menu Items Todo Notes

Known `Menu Items` goals beyond basic structure validation:

- trim leading and trailing spaces from values
- detect or reject duplicate entries
- encourage readable spaced naming such as `Big Fish` instead of `BigFish`

Future ideas, not current priority:

- support files that only provide a smaller core field set and auto-populate default-style values such as `Yes`, `No`, and `0`
- eventually accept non-Excel file formats

## Immediate Next Step

Move from structure validation into the next `Menu Items` validation or cleaning step.

The best first step is:

- choose the next concrete rule after structure validation
- likely candidates are duplicate detection or trimming leading and trailing spaces
- update the outdated read-file success test to match the new return type
- keep the next change scoped to `Menu Items` only

This should be done in a way that can later support the other planned modules, but without expanding scope beyond `Menu Items` right now.

## After That

Once the next `Menu Items` validation step exists, the next likely improvements are:

1. confirm conditional field rules such as `KitchenPrinter`
2. begin blank-cell validation for non-optional fields
3. make file-read and validation messages cleaner and more consistent

## Update Rule

Review this file after any meaningful code change or project checkpoint.

When updating it, keep it factual:

- what changed
- what currently works
- what the next step is
- what is intentionally still unfinished
