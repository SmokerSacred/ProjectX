import pandas as pd

def read_file(menu_path):
     # Stop early if the user closes the file picker without choosing a file.
     if not menu_path : 
        return 'No file selected'
     else:
        try:
            # Read the selected workbook and return the DataFrame for later validation.
            df = pd.read_excel(menu_path)
            return df
            
        except Exception as e:
           # Return a user-facing message instead of crashing on a bad file.
           return f'Please select an Excel file. {e}'
