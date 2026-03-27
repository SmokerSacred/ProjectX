# ProjectX Context

This file is for future Codex chats.

Use it to understand what the project is, what code currently does, and how to continue without re-discovering the same context.

## What We Are Building

ProjectX is a spreadsheet workflow tool for restaurant and POS support work.

The intended pattern is:

1. import or select a source workbook
2. read it safely
3. validate that the structure is usable
4. clean and standardize the data
5. prepare or populate a cleaner downstream output file

This will eventually exist across three modules:

- `Menu Items`
- `Inventory Items`
- `Recipes`

Current work is still focused only on `Menu Items`.

## Current App Behavior

The app currently:

- opens a file picker for `.xlsx` files
- returns `"No file selected"` if the picker is cancelled
- reads the chosen file with `pandas`
- returns a DataFrame on successful reads
- exits cleanly if reading fails
- validates the uploaded file against the expected `Menu Items` headers
- reports missing headers clearly

## Current Code Map

- `main.py`: select file -> read file -> validate structure -> print result
- `src/select_file.py`: Tkinter file picker
- `src/read_file.py`: read logic and friendly error messages
- `src/validation.py`: `expected_values` list and structure validation
- `src/clean_file.py`: unfinished duplicate-check function
- `tests/test_read_file.py`: read-file tests, with a stale success test

## Current Source Of Truth

For `Menu Items`, the current header source of truth is [`src/validation.py`](/c:/Users/ADMIN/Documents/ProjectX/src/validation.py#L1).

The current expected columns are:

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
- `HideContactless`
- `IsModifierItem`
- `Inactive`
- `Menu`
- `MenuGroup`
- `MenuSubgroup`
- `ItemGroup`

All of those columns belong to the current menu item files.

## Known Rules And Preferences

Current `Menu Items` rules/preferences from the user:

- trim leading and trailing spaces
- detect or reject duplicate entries
- prefer readable names with spaces, such as `Big Fish` instead of `BigFish`

Current note:

- the spaced-name preference is a formatting preference, not a validation blocker
- `KitchenPrinter` still needs row-level rule confirmation later

## Important Current Reality

- the app only does structure validation right now
- duplicate handling is started but not finished
- docs should follow the code and direct user instructions
- the user prefers small, clear steps and teaching-oriented guidance
- avoid expanding scope beyond the spreadsheet workflow

## Non-Negotiable Codex Rule

- Codex must not change code in the user's code files without the user's clear approval
- without approval, Codex may only add comments in code files
- this rule must not be broken

## Teaching Rules For Codex

- Codex is acting as the user's teacher, not just a fixer
- do not give direct code answers by default
- do not leave the user stranded when they are struggling
- when something is missing in the user's code, explain the relevant syntax, method, or parameter name so the user has something concrete to work with
- if there is a teaching moment, guide the user through it instead of only saying that something is wrong
- give hints that are strong enough to unblock the user while still letting the user make the final coding decision
- it is okay to use simple examples outside the current codebase when that would make the concept easier to understand
- when the user is stuck on a method, explain what commonly goes with it and what each important argument is doing

## If You Update The Project

After meaningful changes, update:

- `README.md` if the repo overview changed
- `CONTEXT.md` if future Codex needs new handoff context
- `NEXT_STEPS.md` if the immediate next move changed
- `PROJECT_BLUEPRINT.md` if roadmap or direction changed
