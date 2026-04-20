from src import select_file, read_file, validation, clean_file, populate, export
from global_src import row_limit
import sys


def main():
    try:
        # Ask the user for an Excel file, then pass that path to the read layer.
        menu_path = select_file.select_file()
        file_output = read_file.read_file(menu_path)

        # Stop before validation if the file could not be read successfully.
        if isinstance(file_output, str):
            print(file_output)
            return


        # Validate the uploaded file structure only after the read step succeeds.
        validation_result = validation.structure_validation(file_output)

        if validation_result is None:
            trimmed_data = clean_file.trim_whitespace(file_output)
            clean_data = clean_file.clean_duplicates(trimmed_data)

            cleaned_data, duplicate_list = clean_data

            populated_data = populate.autofill(cleaned_data)

            prefilled_cells, populated_df = populated_data

            # Export the populated workbook, then reopen it for duplicate/prefilled highlighting.
            export_path = export.export_menu_items(populated_df, menu_path, duplicate_list, prefilled_cells)
            # Only creates split workbooks when the processed file exceeds the 500-row POS limit.
            row_limit.row_split(export_path)

            print(f"Exported file saved to: {export_path}")

    
        else:
            print(validation_result)

    except Exception as e:
        # Catch unexpected pipeline failures so the app exits with a readable message.
        print(f"Something went wrong: {e}")

if __name__ == '__main__':
    main()
