import pandas as pd

cols_defaults = {
    #"CanApplyDiscount", "AutoApplySameDiscountOnModifier", "IsRateInclusive", "PrintOnReceipt", "PrintOnKot"
    "Yes": ["CanApplyDiscount", "AutoApplySameDiscountOnModifier", "IsRateInclusive", "PrintOnReceipt", "PrintOnKot"],
    "No": ["IsOpenPrice", "AskQuantity", "ExcludeFromTopSellingItems", "PrintOnLabel", "SoldByWeight", "HideContactless", "IsModifierItem", "Inactive"],
    0 : ["Cost", "MaxPrice", "MinPrice", "InventoryCount"],
    "Sales Tax" : ["TaxGroup"],          
    }

def autofill(df):
    filled_vals = []

    for default_value, columns in cols_defaults.items():
        for column in columns:
            # Skip optional/newer columns that may not exist in older client files.
            if column not in df.columns:
                continue

            # Split the current column into blank cells we should fill and pre-filled
            # cells we should remember for later highlighting/export behavior.
            blank_mask = df[column].isnull() | (df[column].astype(str).str.strip() == "")
            filled_mask = ~blank_mask

            for idx in df.index[filled_mask]:
                filled_vals.append((idx, column, df.at[idx, column]))

            # Blank-heavy Yes/No text columns can be inferred as float by pandas, so
            # make them object-compatible before assigning string defaults.
            if isinstance(default_value, str):
                df[column] = df[column].astype("object")

            df.loc[blank_mask, column] = default_value

    # KitchenPrinter needs its own pass because the value depends on other columns,
    # not just a single fixed default.
    if 'KitchenPrinter' in df.columns:
        # Blank-heavy printer columns can be inferred as float, so make the column
        # object-compatible before assigning text values like KOT or BOT.
        df['KitchenPrinter'] = df['KitchenPrinter'].astype("object")

        KitchenPrinter_BlankMask = df['KitchenPrinter'].isnull() | (df['KitchenPrinter'].astype(str).str.strip() == "")
        KitchenPrinter_FilledMask = ~KitchenPrinter_BlankMask

        for idx in df.index[KitchenPrinter_FilledMask]:
            filled_vals.append((idx, 'KitchenPrinter', df.at[idx, 'KitchenPrinter']))

        for idx in df.index[KitchenPrinter_BlankMask]:
            # Only assign a kitchen printer when KOT printing is enabled for that row.
            if df.at[idx, "PrintOnKot"] == "Yes":
                if isinstance(df.at[idx, "Category"], str) and df.at[idx, "Category"].lower() == "food":
                    df.loc[idx, "KitchenPrinter"] = "KOT"
                elif isinstance(df.at[idx, "Category"], str) and df.at[idx, "Category"].lower() == "beverage":
                    df.loc[idx, "KitchenPrinter"] = "BOT"

    return filled_vals, df
