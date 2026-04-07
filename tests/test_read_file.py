from src import read_file


class FakeDataFrame:
    def __init__(self, columns=None):
        self.columns = columns or []


def test_read_file():
    # An empty path should be treated the same as cancelling file selection.
    result = read_file.read_file("")

    assert result == 'No file selected'


def test_file_type(monkeypatch):
    # Simulate pandas failing to read a workbook so the error path stays deterministic.
    def raise_bad_file(*args, **kwargs):
        raise ValueError("cannot parse file")

    monkeypatch.setattr(read_file.pd, "read_excel", raise_bad_file)
    result = read_file.read_file("bad_file.xlsx")

    assert 'Please select an Excel file.' in result


def test_success(monkeypatch):
    # Return a fake DataFrame so we can verify the success path without real Excel support.
    expected_frame = FakeDataFrame(["Name", "Age", "Department"])
    monkeypatch.setattr(read_file.pd, "read_excel", lambda *args, **kwargs: expected_frame)

    result = read_file.read_file("good_file.xlsx")

    assert result is expected_frame
