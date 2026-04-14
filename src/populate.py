import pandas as pd
cols_defaults = {
    "Yes": ["CanApplyDiscount", "AutoApplySameDiscountOnModifier", "IsRateInclusive", "PrintOnReceipt", "PrintOnKot"],
    "No": ["IsOpenPrice", "AskQuantity", "ExcludeFromTopSellingItems", "PrintOnLabel", "SoldByWeight", "HideContactless", "IsModifierItem", "Inactive"],
    0 : ["Cost", "MaxPrice", "MinPrice", "InventoryCount"],
    "Sales Tax" : ["TaxGroup"],
    #"KOT/BOT" : ['KitchenPrinter']           
    }

def autofill(df):
    filled_vals = []

    for default_value, columns in cols_defaults.items():
        for column in columns:
            blank_mask = df[column].isnull() | (df[column].astype(str).str.strip() == "")
            filled_mask = ~blank_mask

            for idx in df.index[filled_mask]:
                filled_vals.append((idx, column, df.at[idx, column]))

            df.loc[blank_mask, column] = default_value

    for j in df["PrintOnKot"]:
        if j == "Yes":
            for i in df["Category"]:
                if i == "FOOD" or i == "Food" or i == "food":
                    df.loc[idx, "KitchenPrinter"] = "KOT"
                elif i == "BEVERAGE" or i == "Beverage" or i == "beverage":
                    df.loc[idx, "KitchenPrinter"] = "BOT"

    return filled_vals, df