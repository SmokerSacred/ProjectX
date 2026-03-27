expected_values = ["ItemName", "Description", "AlternateName", "VariantName", "Category", "SubCategory", "Type", "Barcode", "BarControllerCode", "Sku", "IntegrationCode", "Price", "Cost", "IsOpenPrice", "MaxPrice", "MinPrice", "AskQuantity", "CanApplyDiscount", "AutoApplySameDiscountOnModifier", "IsRateInclusive", "TaxGroup", "PrintOnReceipt", "ExcludeFromTopSellingItems", "PrintOnKot", "KitchenPrinter", "PrintOnLabel", "InventoryCount", "SoldByWeight", "CaptainPrinter", "LabelPrinter", "HideContactless", "IsModifierItem", "Inactive", "Menu", "MenuGroup", "MenuSubgroup", "ItemGroup"] 

def structure_validation(df):
    column_headers = df.columns.to_list()

    missing_values = []

    # Collect every expected header that is missing from the uploaded file.
    for i in expected_values:
        if i not in column_headers:
            missing_values.append(i)

    if not missing_values:
        return None
    else:
        return f'Could not detect the following columns: {missing_values}'
