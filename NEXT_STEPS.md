# ProjectX Next Steps

This file is for the next Codex session to know what to work on next without re-reading the whole project.

## Current Working State

The current `Menu Items` app flow is:

1. pick an `.xlsx` file
2. read it with `pandas`
3. stop cleanly on read failure
4. validate `Menu Items` headers
5. trim whitespace on the current safe column list
6. run duplicate cleaning
7. run blank-only population/default filling
8. export the processed workbook
9. highlight duplicate-review rows and prefilled cells
10. split the workbook only if it exceeds the 500-row POS limit
11. print the saved export path

What is already working:

- file picker for `.xlsx`
- no-file-selected handling
- Excel read with `pandas`
- clean stop on read failure
- structure validation against `src/validation.py`
- whitespace trimming on the current safe text-column list
- duplicate cleaning
- population/default filling from `main.py`
- export/output from `src/export.py`
- duplicate-row and prefilled-cell highlighting in the exported workbook
- conditional workbook splitting from `global_src/row_limit.py`
- top-level error handling in `main.py`

What is not finished yet:

- row-level business validation does not exist yet
- export behavior is only manually tested right now
- tests currently cover read/validation only

## Immediate Next Focus

The next real area of work should be hardening and testing the current `Menu Items` flow rather than adding new core pipeline steps.

That likely means:

1. test the export and split flow with more real client files
2. refine `KitchenPrinter` logic if `MenuGroup` needs to be used as a fallback
3. improve read/export messaging where user-facing wording is still rough
4. add automated tests around export logic where practical
5. keep the current export scoped to the default worksheet for `Menu Items`

## Things Future Codex Should Remember

- keep scope on `Menu Items` for now
- do not treat this file like a roadmap; use it for the next practical move
- preserve the user's Codex rules and teaching preferences from `CONTEXT.md`
- keep `ItemGroup` out of the safe trimming list until type handling is explicit
- docs should help the next session move forward, not just repeat other docs
