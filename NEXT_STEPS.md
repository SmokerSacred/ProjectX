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

- export/output now exists in `src/export.py`, but it is not wired into `main.py` yet
- row-level business validation does not exist yet
- export behavior is not tested yet
- tests currently cover read/validation only

## Immediate Next Focus

The next real area of work should be output/export for the `Menu Items` flow.

That likely means:

1. wire `src/export.py` into `main.py` once the workbook-writing and highlight flow is stable
2. test the export flow with a real workbook and confirm the highlight colors/positions in Excel
3. add automated tests around export logic where practical
4. design the export flow so it can later reuse the shared 500-row split rule
5. keep the current export scoped to the default worksheet for `Menu Items`

## Things Future Codex Should Remember

- keep scope on `Menu Items` for now
- do not treat this file like a roadmap; use it for the next practical move
- preserve the user's Codex rules and teaching preferences from `CONTEXT.md`
- keep `ItemGroup` out of the safe trimming list until type handling is explicit
- docs should help the next session move forward, not just repeat other docs
