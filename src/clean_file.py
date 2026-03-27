def clean_duplicates(df):
    exact_duplicates_removed = df.drop_duplicates(subset=['ItemName', 'Price'], keep='first')

    dirty_duplicate_rows = exact_duplicates_removed[exact_duplicates_removed.duplicated(subset=['ItemName'], keep=False)]
    
    return exact_duplicates_removed, dirty_duplicate_rows




    