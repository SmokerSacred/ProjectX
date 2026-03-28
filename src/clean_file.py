def clean_duplicates(df):
    # First pass: remove rows that are true duplicates of the same item at the same price.
    exact_duplicates_removed = df.drop_duplicates(subset=['ItemName', 'Price'], keep='first')

    # Second pass: keep track of rows that still share an item name after exact duplicates
    # are removed. These are the "dirty duplicates" where the name matches but the pricing
    # does not, so they should be reviewed or highlighted later during export
    dirty_duplicate_rows = exact_duplicates_removed[exact_duplicates_removed.duplicated(subset=['ItemName'], keep=False)]

    # Return the cleaned data plus the rows that need special handling downstream.
    return exact_duplicates_removed, dirty_duplicate_rows

values_to_trim = ["ItemName", "Description", "AlternateName", "VariantName", "Category", "SubCategory", "Type", "Barcode", "BarControllerCode", "IsOpenPrice", "AskQuantity", "CanApplyDiscount", "AutoApplySameDiscountOnModifier", "IsRateInclusive", "TaxGroup", "PrintOnReceipt", "ExcludeFromTopSellingItems", "PrintOnKot", "KitchenPrinter", "PrintOnLabel", "SoldByWeight", "CaptainPrinter", "LabelPrinter", "HideContactless", "IsModifierItem", "Inactive", "Menu", "MenuGroup", "MenuSubgroup", "ItemGroup"]

def trim_whitespace():
    None
