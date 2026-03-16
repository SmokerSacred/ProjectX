import pandas as pd

def read_file(menu_path):
     # Stop early if the user closes the file picker without choosing a file.
     if not menu_path : 
        return 'No file selected'
     else:
        try:
            # Read the selected workbook into a pandas DataFrame.
            df = pd.read_excel(menu_path)
            # Show a small preview so we can confirm the file loaded correctly.
            return df.head()
        except:
            return 'An unexpected error occurred'
