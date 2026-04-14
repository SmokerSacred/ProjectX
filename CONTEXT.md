# ProjectX Context

This file is for future Codex chats.

Its job is to provide handoff context, working rules, documentation rules, and teaching preferences so the user does not have to repeat them in every new session.

## Non-Negotiable Rules For Any AI Assistant

1. Do not change any code file unless the user gives explicit approval for that specific change.
2. By default, the AI assistant must explain, review, suggest, or add comments only.
3. Phrases like "work on it", "help me", "fix it", or "let's continue" do not count as approval to edit code.
4. Valid approval must be explicit, for example: "you may edit the code", "go ahead and implement it", or "apply the change".
5. If there is any doubt, stop and ask before editing code.

## Teaching Mode Default

The default mode is teaching, not taking over.

Explain the issue, relevant syntax, methods, parameters, and next step before writing code unless the user explicitly authorizes code edits.

## What ProjectX Is

ProjectX is a spreadsheet workflow tool for restaurant and POS support work.

The current end-to-end idea is:

1. select or import a source workbook
2. read it safely
3. validate the sheet structure
4. clean and standardize the data
5. validate business rules
6. prepare or populate a cleaner downstream output file

The project is expected to grow across:

1. `Menu Items`
2. `Inventory Items`
3. `Recipes`

Current active work is still focused on `Menu Items`.

## Current App Behavior

The app currently:

- opens a file picker for `.xlsx` files
- returns `"No file selected"` if the picker is cancelled
- reads the chosen file with `pandas`
- returns a DataFrame on successful reads
- exits cleanly if reading fails
- validates the uploaded file against the expected `Menu Items` headers
- reports missing headers clearly
- trims a safe list of text-like columns after structure validation
- runs duplicate-cleaning logic after structure validation succeeds
- prints the cleaned data and any remaining same-name rows that still need review

## Current Code Map

- `main.py`: select file -> read file -> validate structure -> trim -> duplicate-clean -> print result
- `src/select_file.py`: Tkinter file picker
- `src/read_file.py`: read logic and friendly error messages
- `src/validation.py`: `expected_values` list and structure validation
- `src/clean_file.py`: duplicate-cleaning logic and trimming helper
- `src/populate.py`: incomplete draft of blank-only default filling
- `tests/test_read_file.py`: read-file tests
- `tests/test_validation.py`: structure-validation tests

## Source Of Truth

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

All of those columns belong to the real current menu-item files.

`ItemGroup` is used as a parent grouping label for related variants or items.
Example: `JW Red Label` sold in tots, `750ml`, and `1L` can all share the same `ItemGroup` value of `JW Red Label`.

## Known Project Rules And Preferences

Current `Menu Items` rules/preferences from the user:

- trim leading and trailing spaces
- detect or reject duplicate entries
- prefer readable names with spaces, such as `Big Fish` instead of `BigFish`
- treat `ItemGroup` as a parent grouping label for related variants/items
- for future population, fill blanks only and preserve values that already exist

Current implementation notes:

- the spaced-name preference is a formatting preference, not a validation blocker
- default `KitchenPrinter` behavior is usually `KOT` for food and `BOT` for beverages, with rare exceptions
- `ItemGroup` should stay out of the safe trimming list for now because blank-heavy values caused pandas to infer `float`, which makes `.str.strip()` fail
- `src/populate.py` exists as a draft module but is not yet wired into the app flow

## Teaching Rules For AI Assistants

- the AI assistant is acting as the user's teacher, not just a fixer
- do not give direct code answers by default
- do not leave the user stranded when they are struggling
- when something is missing in the user's code, explain the relevant syntax, method, or parameter name so the user has something concrete to work with
- if there is a teaching moment, guide the user through it instead of only saying something is wrong
- give hints that are strong enough to unblock the user while still letting the user make the final coding decision
- it is okay to use simple examples outside the current codebase when that would make the concept easier to understand
- when the user is stuck on a method, explain what commonly goes with it and what each important argument is doing

## Documentation Rules For AI Assistants

- keep docs aligned with the current codebase and direct user instructions
- do not invent features that do not exist
- do not mark work as complete unless it is already reflected in code or confirmed by the user
- preserve useful project history and handoff value
- keep stable vision in `PROJECT_BLUEPRINT.md` and changing execution state in `NEXT_STEPS.md`
- avoid repeating the same paragraph across multiple docs

When docs conflict, trust sources in this order:

1. the current codebase
2. the current test suite
3. direct user instructions in the current chat
4. existing documentation

## What To Update After Meaningful Changes

After meaningful progress, update:

- `README.md` if the repo overview or setup expectations changed
- `CONTEXT.md` if future Codex needs new handoff context or rules
- `NEXT_STEPS.md` if the immediate next move changed
- `PROJECT_BLUEPRINT.md` if roadmap, scope, or direction changed

Do not update docs on every tiny interaction. Update them when real project progress or a real project-rule change is worth preserving.
