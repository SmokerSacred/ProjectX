# ProjectX Context

This file is the fastest way to hand ProjectX context to Codex in a new chat.

## Project Purpose

ProjectX is a small Python desktop utility for restaurant and POS spreadsheet support work.

The goal is to take messy human-filled Excel files and move toward a repeatable workflow for:

- selecting a workbook
- reading it safely
- checking whether the structure is usable
- cleaning or standardizing data later
- preparing the data for downstream POS-related work

The broader workflow is not limited to one file type. The user expects the system to be built in three modules over time:

- `Menu Items`
- `Inventory Items`
- `Recipes`

The menu item template is only the first confirmed input type, and current work should stay focused on that module until its validation flow is in a good place.

## Current Architecture

- `main.py` drives the top-level flow
- `src/select_file.py` opens the Excel file picker
- `src/read_file.py` handles the no-file case and reads Excel data with `pandas`
- `src/validation.py` is the start of the `Menu Items` structure-validation layer
- `tests/test_read_file.py` covers the current read-file behavior with `pytest`

## Current Behavior

Right now the project can:

- open a file picker limited to `.xlsx`
- return `"No file selected"` if the picker is cancelled
- read a selected Excel file with `pandas`
- return a `pandas` DataFrame on a successful read
- return a friendly invalid-file message when a fake or unreadable Excel file is selected
- validate the uploaded `Menu Items` file structure against the fixed expected header list
- report the exact missing headers when structure validation fails

Current implementation note:

- `main.py` now stops cleanly if file reading fails before validation runs
- `src/validation.py` compares uploaded headers against the fixed `Menu Items` header list
- the next likely step is content-level validation or cleaning after structure validation

## Current Constraints

- the project is intentionally small and learning-oriented
- clarity is preferred over cleverness
- reliability comes before convenience features
- business validation rules are not fully defined yet
- code changes should stay incremental and easy to understand

## Known Template

The current real-world validation target is a menu item Excel template shared by the user on March 24, 2026.

Observed sheet details:

- workbook has one sheet named `Sheet1`
- header row currently contains 30 columns
- sample data exists in the file, so the template is usable as both a structure reference and a realistic validation example

Current known header set:

- `ItemName`
- `Description`
- `AlternateName`
- `VariantName`
- `Category`
- `SubCategory`
- `Type`
- `Barcode`
- `BarControllerCode`
- `Sku`
- `IntegrationCode`
- `Price`
- `Cost`
- `IsOpenPrice`
- `MaxPrice`
- `MinPrice`
- `AskQuantity`
- `CanApplyDiscount`
- `AutoApplySameDiscountOnModifier`
- `IsRateInclusive`
- `TaxGroup`
- `PrintOnReceipt`
- `ExcludeFromTopSellingItems`
- `PrintOnKot`
- `KitchenPrinter`
- `PrintOnLabel`
- `InventoryCount`
- `SoldByWeight`
- `CaptainPrinter`
- `LabelPrinter`

User-confirmed optional fields so far:

- `Description`
- `AlternateName`
- `VariantName`
- `Type`
- `Barcode`
- `BarControllerCode`
- `Sku`
- `IntegrationCode`
- `CaptainPrinter`
- `LabelPrinter`

Validation note:

- `ItemGroup` was mentioned by the user as optional, but it does not appear in the current template header list
- `KitchenPrinter` is conditional
- the user initially described `KitchenPrinter` as required only if `PrintOnKot` is set to `No`
- the sample rows in the template show `PrintOnKot = Yes` together with `KitchenPrinter = KOT`, so this rule still needs confirmation before it is enforced in code

## Menu Items Rules

For the current `Menu Items` module, the user has identified these business rules and preferences:

- no leading or trailing empty space in values
- no duplicate entries
- prefer title-style naming with spaces between words, such as `Big Fish` instead of `BigFish`

Formatting note:

- the `Big Fish` preference is currently a formatting preference, not a validation blocker

Future todo, not current priority:

- if the uploaded file only contains a smaller core set such as item name, price, category, and subcategory, the system may later auto-populate the other default-style fields such as `Yes`, `No`, and `0`
- the project may later accept non-Excel input formats

## Workflow Direction

The user's current mental model is:

- data will be scraped or imported from one source file
- that imported data will be cleaned or standardized
- the cleaned data will populate a separate output copy or template file
- this overall pattern will later exist across three modules: `Menu Items`, `Inventory Items`, and `Recipes`

This means the project is moving toward a multi-module spreadsheet workflow rather than a single-file checker.

## Working Style

When helping on this project:

- prefer small steps over large rewrites
- review the current code before suggesting changes
- explain logic clearly when teaching is useful
- guide by default instead of providing direct code immediately
- only give direct code when the user explicitly asks for it
- when the user is stuck, explain the solution path more like a teacher instead of only describing what is wrong
- give more concrete guided hints when the user does not yet know what to write next
- when there are multiple valid approaches, offer a few concrete options and explain why one may fit better
- when the user is blocked on syntax or library usage, name the relevant methods or parameters so the user has something real to work with
- avoid broad feature expansion outside the spreadsheet workflow
- treat the docs as a running record of real progress, not aspirational plans

## Useful Commands

```powershell
python main.py
pytest
```

## Documentation Update Rule

If the project changes meaningfully, update:

- `README.md` for the quick overview if user-facing behavior changed
- `CONTEXT.md` for new-chat handoff context
- `NEXT_STEPS.md` for the current snapshot and immediate next work
