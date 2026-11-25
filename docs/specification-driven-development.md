# Specification-Driven Development

## What it is

Specification-driven development (SDD) is a way of building software in
which a clear, testable specification guides implementation and verification.
The team agrees on the intended behavior before or alongside writing code,
then uses the specification to make design choices, create tests, and review
the finished change.

The specification is a practical source of shared understanding, not a
replacement for engineering judgment. It should be specific enough to guide
implementation while remaining easy to update when requirements change.

## Why use it

- Align product, engineering, and users on what a feature should do.
- Identify edge cases and constraints before they become production bugs.
- Turn expectations into repeatable acceptance tests.
- Make changes easier to review and maintain.
- Keep intended behavior distinct from implementation details.

## A lightweight SDD workflow

1. **Describe the problem.** Identify the user, their task, and why the
   current workflow is insufficient.
2. **Define scope.** State what the change includes and explicitly excludes.
3. **Write requirements.** Use clear, uniquely identifiable statements. Mark
   whether each is functional, quality-related, or a constraint.
4. **Specify examples and edge cases.** Include normal, invalid, boundary,
   and failure scenarios.
5. **Define acceptance criteria.** Make each criterion observable and
   verifiable, preferably with concrete input and expected output.
6. **Design the solution.** Choose the smallest suitable implementation and
   identify affected interfaces and data.
7. **Derive tests from the specification.** Map each requirement to one or
   more tests before or during implementation.
8. **Implement and verify.** Make the change, run targeted tests and relevant
   checks, and compare actual behavior with the acceptance criteria.
9. **Update the specification.** If the approved behavior changes, revise the
   spec, tests, and related documentation together.

## What a feature specification should contain

- Problem statement and intended users.
- Goals, non-goals, and assumptions.
- Functional requirements and relevant quality requirements.
- User flows, API contracts, data formats, and limits where applicable.
- Error handling and edge cases.
- Acceptance criteria and their corresponding tests.
- Security, privacy, and operational considerations appropriate to the
  feature.
- Open questions and decisions that need stakeholder input.

## Hello Agent example: rejecting an invalid CSV

### Problem

Users need clear feedback when an uploaded file cannot be used as a CSV.

### Requirement

**CSV-VAL-01:** The backend must reject uploaded files that are empty or
cannot be parsed as a valid UTF-8 CSV and must return an actionable client
error. The file must not be used to generate an answer.

### Acceptance examples

| Input | Expected behavior |
|---|---|
| Valid, non-empty UTF-8 CSV within size and row limits | Load it and make its rows available to the question-answering flow |
| Empty file | Reject the request with a clear error identifying that the file is empty |
| Malformed CSV or invalid encoding | Reject the request with a clear CSV validation error |
| File larger than the configured maximum | Reject the request with a clear size-limit error |

### Derived verification

Tests should exercise each input above and assert both the HTTP outcome and
the error detail. An integration test should also verify that rejected
uploads do not result in a model-generated answer. This ties the user-facing
requirement to observable system behavior without prescribing every internal
implementation detail.

## Keeping specifications useful

- Prefer concise requirements with one testable behavior each.
- Use stable IDs when requirements need traceability across code and tests.
- Avoid describing a feature as complete until its acceptance criteria pass.
- Separate current behavior from desired future behavior.
- Avoid duplicating details that already have a maintained source of truth;
  link to the relevant API, architecture, or operational documentation.
- Review specifications when assumptions, data handling, or user workflows
  change.

For the current product baseline, see the
[Hello Agent business requirements](business-requirements.md) and
[technical architecture](architecture.md).
