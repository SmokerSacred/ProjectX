from src import read_file
import pandas as pd

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


def test_success(tmp_path):
    # Create a real temporary Excel file so the success path can be tested safely.
    good_file = tmp_path / "good_file.xlsx"

    data = {
        'Name': ['Mustafa', 'Payal', 'imtiyaz', 'idris', 'Huzeifa'],
        'Age' : ['22', '26', '78', '55', '49'],
        'Department' : ['Support', 'Support', 'Bigboss', 'smallboss1', 'smallboss2']
    }

    clean_data = pd.DataFrame(data)

    clean_data.to_excel(good_file, index=False)

    row_count = clean_data.shape[0]
    column_count = clean_data.shape[1]
    column_names = clean_data.columns.to_list()


    result = read_file.read_file(str(good_file))
    assert f'The number of Rows: {row_count} \nThe number of Columns: {column_count} \nColumn names are: {column_names}' in result





