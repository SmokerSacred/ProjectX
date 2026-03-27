# ProjectX Blueprint

This file is the roadmap for ProjectX.

It should describe where the project is going, not repeat the current status line by line.

## Project Goal

Build a small, practical spreadsheet workflow tool for restaurant and POS support work.

The tool should reduce repetitive manual cleanup by taking messy source spreadsheets and moving them toward a reliable, reusable output workflow.

## Long-Term Workflow

The intended end-to-end flow is:

1. choose or import a source file
2. read it safely
3. validate structure
4. validate row-level business rules
5. clean and standardize values
6. transform the data into the needed shape
7. populate or produce an output file for downstream use

## Planned Modules

The project is expected to grow in three modules:

1. `Menu Items`
2. `Inventory Items`
3. `Recipes`

The build order should stay:

1. finish `Menu Items`
2. move to `Inventory Items`
3. move to `Recipes`

## Menu Items Roadmap

The `Menu Items` module is the current focus.

Planned progression:

1. stable file selection and reading
2. structure validation against the expected template
3. duplicate detection
4. trimming and normalization
5. row-level business validation
6. cleaned output preparation
7. template/output population

## Business Direction

The project is not meant to be only a checker.

The intended use is:

- data may be scraped or imported from one source
- that data should be cleaned and standardized
- the cleaned result should help populate a more controlled destination file

## Design Principles

ProjectX should stay:

- small
- reliable
- understandable
- modular
- useful for real work

Priority order:

1. make it run
2. make it reliable
3. make it understandable
4. make it useful
5. add convenience later

## Scope Guardrails

In scope:

- spreadsheet intake
- validation
- cleaning
- transformation
- output preparation for the POS workflow

Out of scope for now:

- CSV support
- advanced UI
- cloud features
- login systems
- unrelated automation

## Documentation Roles

- `README.md`: repo overview
- `CONTEXT.md`: handoff context for Codex
- `NEXT_STEPS.md`: immediate next work
- `PROJECT_BLUEPRINT.md`: roadmap and intended direction

## Codex Guardrail

- Codex must not change code in the user's code files without clear user approval
- if approval has not been given, Codex may only add comments inside code files
- this is a hard rule for future Codex sessions

## Teaching Guardrail

- Codex should teach by guiding, not by taking over
- Codex should not give direct code answers unless the user clearly asks for them
- Codex should not stop at saying there is an error; it should explain the missing concept, syntax, method, or parameter that the user likely needs next
- Codex should give concrete hints when the user is stuck, while still leaving the final implementation decision to the user
- Codex may use simple outside examples when they help explain a coding idea more clearly
