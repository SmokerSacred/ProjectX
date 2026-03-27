from src import validation


class FakeColumns(list):
    def to_list(self):
        return list(self)


class FakeDataFrame:
    def __init__(self, columns):
        self.columns = FakeColumns(columns)


def test_structure_validation_success():
    frame = FakeDataFrame(validation.expected_values)

    result = validation.structure_validation(frame)

    assert result == (
        "The file has been uploaded successfully. Please have some patience while we clean up your file"
    )


def test_structure_validation_missing_columns():
    frame = FakeDataFrame(["ItemName", "Description", "Price"])
    expected_missing = [column for column in validation.expected_values if column not in frame.columns]

    result = validation.structure_validation(frame)

    assert result == f"Could not detect the following columns: {expected_missing}"
