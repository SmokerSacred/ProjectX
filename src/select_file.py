from tkinter import filedialog

def select_file():
    selected_file = filedialog.askopenfilename(
        filetypes = [("Excel File", "*.xlsx")]
        )
    return selected_file
