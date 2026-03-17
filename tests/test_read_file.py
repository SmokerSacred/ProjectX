from src import read_file

def test_read_file():
    # An empty path should be treated the same as cancelling file selection.
    result = read_file.read_file("")

    assert result == 'No file selected'

def test_file_type(tmp_path):
    # Create a temporary fake .xlsx file so the error path can be tested safely.
    bad_file = tmp_path / 'bad_file.xlsx'
    bad_file.write_text("this is not a real excel file")

    result = read_file.read_file(str(bad_file))

    assert 'Please select an Excel file.' in result
