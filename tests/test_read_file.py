from src import read_file

def test_read_file():
    # An empty path should be treated the same as cancelling file selection.
    result = read_file.read_file("")

    assert result == 'No file selected'
