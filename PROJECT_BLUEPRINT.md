# ProjectX Blueprint

## What This Project Is

ProjectX is a small Python desktop utility for handling Excel-based POS support work in restaurant environments.

The tool is being built to reduce repetitive spreadsheet cleanup and preparation work before the data is ready for downstream POS-related use.

The input files are expected to be human-filled spreadsheets rather than perfectly structured exports, so the project is centered on defensive handling rather than ideal inputs.

This project also supports rebuilding the user's Python skills through a practical real-world tool, so clarity and learning value matter alongside functionality.

## What This Project Is Not

ProjectX is not:

- a full POS system
- a restaurant management platform
- a cloud platform
- a general spreadsheet editor
- a broad automation suite

It is a focused utility for file-based spreadsheet preparation and transformation.

## Core Problem

Restaurant and POS support work often involves Excel sheets prepared by people.

Those sheets may need to be:

- checked
- cleaned
- standardized
- transformed
- prepared for another workflow

Doing that manually is repetitive and error-prone.

The long-term goal is to create a repeatable process where the user can:

1. choose an Excel file
2. load it safely
3. inspect its structure
4. validate whether it contains the needed data
5. clean or transform the contents
6. produce usable output for the next POS-related step

## Real-World Assumptions

This project assumes the input files are:

- Excel files, not CSV
- created or filled by humans
- inconsistent in formatting
- imperfectly structured
- likely to need validation before processing
- likely to contain business meaning that matters more than raw cell values

Because of that, the program should expect issues like:

- the wrong file being selected
- required columns missing
- headers spelled differently than expected
- numbers stored as text
- blank cells in important fields
- extra irrelevant columns

Reliability and clear error handling are core requirements, not optional polish.

## Expected Workflow

### Stage 1: File Intake

The app launches and the user selects an Excel file.

### Stage 2: File Reading

The program reads the workbook safely and fails clearly if it cannot.

### Stage 3: Structure Inspection

The program reports what is inside the file, such as row count, column count, and headers.

### Stage 4: Validation

The program checks whether the file is usable for the intended workflow.

### Stage 5: Cleaning And Standardization

The program prepares the data for reliable downstream use.

### Stage 6: Transformation

The program converts the spreadsheet into the structure actually needed for POS work.

### Stage 7: Output

The program produces a usable result, such as a cleaned workbook, transformed workbook, or status summary.

## Current Development Reality

The project currently has two layers:

### Layer A: Technical Foundation

This includes:

- app launch
- file picker
- file reading
- basic summaries
- error handling
- tests around early behavior

### Layer B: Business Workflow Logic

This includes:

- deciding the exact spreadsheet format being targeted
- defining required columns
- defining cleaning rules
- defining transformation rules
- defining the final output shape

Layer A is underway.
Layer B still needs to be written down more precisely as the real workflow becomes clearer.

## Working Rules For Codex

When helping on this project, Codex should:

- stay aware of the current repository state before giving advice
- prefer small, understandable steps
- explain logic clearly when the user is learning
- avoid unnecessary complexity
- avoid expanding scope beyond the spreadsheet workflow

Unless explicitly asked otherwise, documentation help should stay accurate to the current code and project direction.

## Build Philosophy

This project should stay:

- small
- useful
- understandable
- modular
- practical

Order of priority:

1. make it run
2. make it reliable
3. make it understandable
4. make it useful for real work
5. improve convenience later

Clarity is more important than cleverness.
A simple solution that is easy to debug is better than an advanced one that is harder to follow.

## Scope Guardrails

### In Scope Right Now

- launching the app
- selecting an Excel file
- confirming the selected path
- reading spreadsheet data
- showing a basic summary
- handling errors clearly
- preparing for later validation and transformation steps

### Not In Scope Right Now

- CSV support
- voice features
- AI assistant features inside the app
- advanced UI
- database design
- login systems
- cloud sync
- unrelated automation features

## Documentation Structure

Use the project docs like this:

- `README.md`: stable quick overview
- `CONTEXT.md`: fast handoff for new Codex chats
- `NEXT_STEPS.md`: live progress and immediate next work
- `DOCS_SUBAGENT.md`: instructions for docs-only delegation
