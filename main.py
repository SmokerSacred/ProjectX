from src import select_file, read_file

# Ask the user for an Excel file, then pass that path to the read layer.
menu_path = select_file.select_file()
file_output = read_file.read_file(menu_path)

# Print either the preview data or a clear status/error message.
print(file_output)
