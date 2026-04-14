# ProjectX Next Steps

This file is for the next Codex session to know what to work on next without re-reading the whole project.

## Current Working State

The current app flow is:

1. pick an `.xlsx` file
2. read it with `pandas`
3. stop cleanly on read failure
4. validate `Menu Items` headers
5. trim whitespace on the current safe column list
6. run duplicate cleaning
7. print the cleaned data plus duplicate-review rows

What is already working:

- file picker for `.xlsx`
- no-file-selected handling
- Excel read with `pandas`
- clean stop on read failure
- structure validation against `src/validation.py`
- whitespace trimming on the current safe text-column list
- duplicate cleaning and duplicate-review output from `main.py`

What is not finished yet:

- `src/populate.py` is still incomplete
- population/default filling is not wired into the main flow
- row-level business validation does not exist yet
- duplicate handling is not yet surfaced in a final user-friendly output format
- tests currently cover read/validation only

## Immediate Next Focus

The next real area of work should be the population step for `Menu Items`.

That likely means:

1. finish a first usable version of `src/populate.py`
2. make it fill blank cells only
3. preserve values that already exist
4. handle `KitchenPrinter` as a conditional rule instead of a simple fixed default
5. decide what the function should return so later export/highlighting work is still possible

## After Population

Once the first population flow exists, the next likely work is:

1. wire population into `main.py` after cleanup
2. define row-level rules for important fields
3. improve how duplicate-review rows are surfaced
4. expand tests around cleaning and population behavior

## Things Future Codex Should Remember

- keep scope on `Menu Items` for now
- do not treat this file like a roadmap; use it for the next practical move
- preserve the user's Codex rules and teaching preferences from `CONTEXT.md`
- keep `ItemGroup` out of the safe trimming list until type handling is explicit
- docs should help the next session move forward, not just repeat other docs
