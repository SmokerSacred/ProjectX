values_to_trim = ["ItemName", "Category", "SubCategory", "Menu", "MenuGroup", "MenuSubgroup"]

def clean_duplicates(df):
    # First pass: remove rows that are true duplicates of the same item at the same price.
    exact_duplicates_removed = df.drop_duplicates(subset=['ItemName', 'Price'], keep='first')

    # Reset the surviving row numbers so later export/highlight logic points to the
    # correct Excel rows after exact duplicates are removed.
    exact_duplicates_removed.reset_index(drop=True, inplace=True)


    # Second pass: keep track of rows that still share an item name after exact duplicates
    # are removed. These are the "dirty duplicates" where the name matches but the pricing
    # does not, so they should be reviewed or highlighted later during export
    dirty_duplicate_rows = exact_duplicates_removed[exact_duplicates_removed.duplicated(subset=['ItemName'], keep=False)]

    # Return the cleaned data plus the rows that need special handling downstream.
    return exact_duplicates_removed, dirty_duplicate_rows


def trim_whitespace(df):
    # Trim only existing columns, and only for values that are actually strings.
    # Optional or blank-heavy columns like SubCategory can be inferred as float by
    # pandas, so raw `.str.strip()` across the whole Series is not always safe.
    for i in values_to_trim:
        if i in df.columns:
            df[i] = df[i].apply(lambda value: value.strip() if isinstance(value, str) else value)

    # Return the same DataFrame so later cleaning steps can keep chaining.
    return df
