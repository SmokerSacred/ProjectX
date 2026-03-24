import pandas as pd

def read_file(menu_path):
     # Stop early if the user closes the file picker without choosing a file.
     if not menu_path : 
        return 'No file selected'
     else:
        try:
            # Read the selected workbook into a pandas DataFrame.
            df = pd.read_excel(menu_path)
            # Build a simple structural summary of the loaded sheet.

            row_count = df.shape[0]
            column_count = df.shape[1]
            column_names = df.columns.to_list()

            return f'The number of Rows: {row_count} \nThe number of Columns: {column_count} \nColumn names are: {column_names}'
            
        except Exception as e:
           # Return a user-facing message instead of crashing on a bad file.
           return f'Please select an Excel file. {e}'
