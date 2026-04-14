# ProjectX Blueprint

This file describes the intended direction of ProjectX.

It should explain the product vision, module progression, and future work shape without turning into a running status report or a copy of Codex instructions.

## Project Goal

Build a practical spreadsheet workflow tool for restaurant and POS support work.

The goal is to reduce repetitive manual cleanup by taking messy source spreadsheets and moving them toward a reliable downstream output workflow.

## Long-Term Workflow

The intended end-to-end flow is:

1. choose or import a source file
2. read it safely
3. validate structure
4. validate row-level business rules
5. clean and standardize values
6. transform the data into the required shape
7. populate or produce an output file for downstream use

## Planned Modules

ProjectX is expected to grow in this order:

1. `Menu Items`
2. `Inventory Items`
3. `Recipes`

The project should fully establish the workflow in `Menu Items` first, then reuse the lessons and structure in the later modules.

## Menu Items Progression

The intended progression for the current module is:

1. stable file selection and reading
2. structure validation against the required template
3. trimming and normalization
4. duplicate detection and duplicate reporting
5. row-level business validation
6. cleaned-output preparation
7. template or downstream-file population

## Product Direction

ProjectX is not meant to be only a checker.

The intended real-world use is:

- data may be scraped or exported from one source
- that data should be cleaned and standardized
- the cleaned result should help populate a more controlled destination file

For `Menu Items`, the downstream population direction should favor:

- preserving values that already exist
- filling blank cells only
- handling rule-based fields like `KitchenPrinter` separately from simple fixed defaults

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

## Scope Boundaries

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

- `README.md`: repo overview and how to run the project
- `CONTEXT.md`: Codex handoff context, user rules, and documentation/teaching guidance
- `NEXT_STEPS.md`: immediate next practical work
- `PROJECT_BLUEPRINT.md`: roadmap and intended direction
