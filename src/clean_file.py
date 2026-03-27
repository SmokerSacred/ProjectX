color = 'blue'

def clean_duplicates(df):
    exact_duplicates_removed = df.drop_duplicates(subset=['ItemName', 'Price'], keep='first')

    dirty_duplicate_rows = exact_duplicates_removed[exact_duplicates_removed.duplicated(subset=['ItemName'], keep=False)]
    
    if dirty_duplicate_rows.empty:
        pass
    elif dirty_duplicate_rows.isin(exact_duplicates_removed):
        exact_duplicates_removed.style.apply({color})





    