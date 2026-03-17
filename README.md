# ProjectX

ProjectX is a small Python desktop utility for restaurant/POS spreadsheet support work.

Current progress:

- opens a file picker for `.xlsx` files
- handles the case where no file is selected
- reads an Excel file with `pandas`
- returns a simple multi-line summary of the loaded file structure
- returns a clearer message when the selected file cannot be read as Excel
- includes an initial `pytest` test for the no-file-selected case

Current focus:

- keep improving file-read error handling
- expand the early test setup beyond the first basic case
- prepare for later validation and cleaning rules
