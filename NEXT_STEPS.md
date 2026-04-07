# ProjectX Next Steps

This file is for the next Codex session to know what to do next.

## Current Working State

Working now:

- file picker for `.xlsx`
- no-file-selected handling
- Excel read with `pandas`
- clean stop on read failure
- `Menu Items` structure validation against `src/validation.py`
- duplicate detection after structure validation
- duplicate-cleaning output from `main.py`

Not done yet:

- wiring trimming into the app flow
- deciding how to handle `ItemGroup` during trimming without triggering pandas string errors
- row-level validation beyond headers
- deciding whether duplicate handling should also be surfaced separately from the cleaned output

## Immediate Next Task

Decide where trimming should enter the cleaning flow.

That likely means:

1. decide whether trimming should happen before or after duplicate cleanup
2. confirm whether duplicate rows should be reported separately from the cleaned output
3. keep `ItemGroup` out of the safe trimming list until type handling is explicit
4. wire the trimming helper into the app flow
5. keep the flow scoped to `Menu Items`

## After That

Next likely work:

1. wire in trimming of leading and trailing spaces with column-type awareness
2. confirm row-level rules for `KitchenPrinter`
3. begin blank-cell validation for important fields
4. update or expand tests once the flow settles

## Things To Remember

- all columns in `src/validation.py` are part of the real menu item files
- keep scope on `Menu Items`
- do small changes, not big rewrites
- prefer clarity over cleverness
