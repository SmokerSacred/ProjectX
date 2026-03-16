# ProjectX

ProjectX is a small Python desktop utility for restaurant/POS spreadsheet support work.

Current progress:

- opens a file picker for `.xlsx` files
- handles the case where no file is selected
- reads an Excel file with `pandas`
- prints a small preview of the loaded data with `df.head()`

Current focus:

- strengthen file-read error handling
- move from raw preview output into clearer file summaries
- prepare for later validation and cleaning rules
