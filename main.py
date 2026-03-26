from src import select_file, read_file, validation
import sys

# Ask the user for an Excel file, then pass that path to the read layer.
menu_path = select_file.select_file()
file_output = read_file.read_file(menu_path)

# Stop before validation if the file could not be read successfully.
if isinstance(file_output, str):
    sys.exit(file_output)

# Validate the uploaded file structure only after the read step succeeds.
file_validation = validation.structure_validation(file_output)

# Print either the preview data or a clear status/error message.
print(file_validation)
