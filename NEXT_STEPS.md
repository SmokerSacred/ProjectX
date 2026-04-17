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
8. print the populated data

What is already working:

- file picker for `.xlsx`
- no-file-selected handling
- Excel read with `pandas`
- clean stop on read failure
- structure validation against `src/validation.py`
- whitespace trimming on the current safe text-column list
- duplicate cleaning
- population/default filling from `main.py`

What is not finished yet:

- export/output to Excel does not exist yet
- row-level business validation does not exist yet
- duplicate and autofill reference points are not yet applied as highlights in the exported workbook
- tests currently cover read/validation only

## Immediate Next Focus

The next real area of work should be output/export for the `Menu Items` flow.

That likely means:

1. decide what the exported `Menu Items` workbook should contain
2. use `duplicate_list` as reference data to highlight the entire duplicate-review row with a constant duplicate color
3. use `filled_vals` as reference data to highlight only the specific recorded cells with a separate constant color
4. design the export flow so it can later reuse the shared 500-row split rule
5. add tests around cleaning/population before or alongside export work

## Things Future Codex Should Remember

- keep scope on `Menu Items` for now
- do not treat this file like a roadmap; use it for the next practical move
- preserve the user's Codex rules and teaching preferences from `CONTEXT.md`
- keep `ItemGroup` out of the safe trimming list until type handling is explicit
- docs should help the next session move forward, not just repeat other docs
