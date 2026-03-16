from tkinter import filedialog

def select_file():
    # Open a file picker that only allows Excel workbook selection.
    selected_file = filedialog.askopenfilename(
        filetypes = [("Excel File", "*.xlsx")]
        )
    return selected_file
