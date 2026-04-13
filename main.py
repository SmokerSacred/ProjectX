from src import select_file, read_file, validation, clean_file, populate
import sys

# Ask the user for an Excel file, then pass that path to the read layer.
menu_path = select_file.select_file()
file_output = read_file.read_file(menu_path)

# Stop before validation if the file could not be read successfully.
if isinstance(file_output, str):
    sys.exit(file_output)

# Validate the uploaded file structure only after the read step succeeds.
validation_result = validation.structure_validation(file_output)

if validation_result is None:
    trimmed_data = clean_file.trim_whitespace(file_output)
    clean_data = clean_file.clean_duplicates(trimmed_data)
    # Print the cleaned data plus any same-name rows that still need review.
    print(clean_data)

else:
    print(validation_result)
