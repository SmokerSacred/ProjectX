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

Not done yet:

- trimming values
- row-level validation beyond headers
- deciding whether duplicate handling should only report or also remove duplicates

## Immediate Next Task

Decide the next cleaning step after duplicate detection.

That likely means:

1. decide whether value trimming should happen before any later duplicate removal logic
2. confirm whether duplicates should only be reported or automatically cleaned
3. begin trimming leading and trailing spaces
4. keep the flow scoped to `Menu Items`

## After That

Next likely work:

1. trim leading and trailing spaces
2. confirm row-level rules for `KitchenPrinter`
3. begin blank-cell validation for important fields
4. update or expand tests once the flow settles

## Things To Remember

- all columns in `src/validation.py` are part of the real menu item files
- keep scope on `Menu Items`
- do small changes, not big rewrites
- prefer clarity over cleverness
