required_values = ["ItemName", "Description", "AlternateName", "VariantName", "Category", "SubCategory", "Type", "Barcode", "BarControllerCode", "Sku", "IntegrationCode", "Price", "Cost", "IsOpenPrice", "MaxPrice", "MinPrice", "AskQuantity", "CanApplyDiscount", "AutoApplySameDiscountOnModifier", "IsRateInclusive", "TaxGroup", "PrintOnReceipt", "ExcludeFromTopSellingItems", "PrintOnKot", "KitchenPrinter", "PrintOnLabel", "InventoryCount", "SoldByWeight", "CaptainPrinter", "LabelPrinter", "HideContactless", "IsModifierItem", "Menu", "MenuGroup", "MenuSubgroup", "ItemGroup"]
optional_values = ["Inactive"]

def structure_validation(df):
    column_headers = df.columns.to_list()

    missing_values = []

    # Collect only truly required headers. Some newer template fields, like Inactive,
    # should be accepted when present without failing older client files that lack them.
    for i in required_values:
        if i not in column_headers:
            missing_values.append(i)

    if not missing_values:
        return None
    else:
        return f'Could not detect the following columns: {missing_values}'
