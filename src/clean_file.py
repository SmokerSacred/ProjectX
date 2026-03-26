import pandas as pd


def clean_duplicates(df):
    detected_duplicates = df.duplicated(subset=['ItemName', 'Price'])

