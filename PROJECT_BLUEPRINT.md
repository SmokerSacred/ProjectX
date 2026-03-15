# Project Blueprint

## Purpose

Build a small Python desktop utility that helps with POS-related file and data automation for restaurant work.

The goal is to reduce repetitive manual work while rebuilding programming skill through a real, useful project.

## Core Build Philosophy

This project should stay:

- small
- useful
- understandable

We build the working core first, then improve it later.

## Collaboration Rules

These rules define how coding help should work in this project.

### Code Ownership

- The user writes the project code.
- Codex should not change code files unless the user explicitly gives permission.
- Codex does have free rein over documentation, blueprint updates, and code comments.

### How Codex Should Help

- break problems into smaller steps
- explain what each part is doing
- guide the user toward writing the code themselves
- avoid rushing straight to the final answer
- support learning and understanding, not just speed

### Default Approach

When helping with code, Codex should:

1. explain the goal of the next small step
2. help the user think through inputs, outputs, and logic
3. let the user attempt the code
4. review and explain improvements if needed

### What To Avoid

Codex should avoid:

- taking over implementation without permission
- solving the whole problem immediately when the user is trying to learn
- making code changes silently
- turning the project into fake progress by doing all the thinking for the user

## Phase 1 Scope

Phase 1 is a simple app that can:

1. let the user choose an input file
2. read that file successfully
3. prepare the data for POS-related processing
4. produce usable output

## Not In Scope Right Now

These are intentionally out of scope for now:

- voice features
- AI assistant features
- advanced UI
- full POS platform features
- random extra libraries that do not support the core workflow

## Immediate Goal

Get the project into a reliable state where it can:

- launch successfully
- accept a file input
- confirm that the file was selected
- read spreadsheet data successfully

## Near-Term Milestones

### Milestone 1: Basic App Flow

- app runs
- file picker opens
- user selects a file
- selected file path is returned

### Milestone 2: File Reading

- app reads Excel or CSV input
- basic validation is added
- errors are handled clearly

Current progress:

- `main.py` now calls the file-reading layer after a file is selected
- the app prints a basic load summary with row and column information
- the next improvement should be safer error handling around failed reads

### Milestone 3: POS Processing Logic

- identify required columns
- clean values
- transform the data into the needed structure
- generate final output

### Milestone 4: Simple Interface Improvements

- status messages
- clearer buttons or prompts
- export confirmation

## Current Folder Structure

```text
ProjectX/
├── main.py
├── PROJECT_BLUEPRINT.md
└── src/
    ├── read_file.py
    └── select_file.py
```

## File Responsibilities

### `main.py`

The app entry point.

Responsibilities:

- start the basic app flow
- call helper modules
- show or print results while the project is still simple

### `src/select_file.py`

File selection logic.

Responsibilities:

- open the file picker
- limit the selectable file types when needed
- return the chosen file path

### `src/read_file.py`

File reading logic.

Responsibilities:

- load selected files into Python
- handle spreadsheet-reading logic
- return the loaded data for later processing

## Development Rules

When adding new features, ask:

1. Does this help the real POS workflow?
2. Is this needed now, or is it a distraction?
3. Can the code stay easy to understand?

If the answer is no, do not add it yet.

## Next Recommended Build Steps

1. Add error handling if the selected file cannot be opened or parsed.
2. Decide the exact POS file format and required columns.
3. Build the first real transformation step.
4. Add clearer status messages for success and failure.
5. Expand output handling after the processing rules are defined.
