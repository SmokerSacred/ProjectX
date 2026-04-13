import pandas as pd
cols_defaults = {
    "Yes": ["CanApplyDiscount", "AutoApplySameDiscountOnModifier", "IsRateInclusive", "PrintOnReceipt", "PrintOnKot"],
    "No": ["IsOpenPrice", "AskQuantity", "ExcludeFromTopSellingItems", "PrintOnLabel", "SoldByWeight", "HideContactless", "IsModifierItem", "Inactive"],
    0 : ["Cost", "MaxPrice", "MinPrice", "InventoryCount"],
    "Sales Tax" : ["TaxGroup"],
    #"KOT/BOT" : ['KitchenPrinter']           
    }

def autofill(df):
    Filled_Vals = []

    for default_value, columns in cols_defaults.items():
        for column in columns:
          blank_mask = df[column].isnull() | df[column].astype(str).str.strip() == ""


        return