# Useful Team Utilities for HelloAI

HelloAI could grow from a CSV question-answering app into a collection of
utilities for common spreadsheet tasks. Utilities should present their rules,
show source rows, and let employees review results before acting on them.

| Utility | Example task | Useful output |
|---|---|---|
| Reconcile two files | Compare invoices with payment records | Matched, unmatched, duplicate, and conflicting records |
| Match similar records | Find customer records with slightly different names or addresses | Candidate record pairs, match scores, and reasons |
| Validate data | Check required fields, formats, ranges, and allowed values | Row- and column-specific errors and warnings |
| Find changes | Compare this month's inventory file with last month's | Added, removed, and changed records |
| Summarize and group | Total sales by region or exceptions by supplier | Grouped summaries and notable changes |
| Detect anomalies | Find unusually large amounts or unexpected quantities | Flagged rows for human review |
| Ask questions across files | Ask which suppliers have overdue invoices | Answer with source-file and row references |

## Example: reconciliation workflow

1. Select the columns to compare, such as invoice number. The app can suggest
   candidate columns for the user to confirm.
2. Normalize values using visible, configurable rules, such as trimming spaces
   or standardizing dates.
3. Apply exact or configured fuzzy matching, including business rules such as
   an allowed amount difference or date range.
4. Classify results as **matched**, **possible match**, **unmatched**,
   **duplicate**, or **conflict**.
5. Show the score, matching criteria, and original source rows for each result.
6. Let the user review uncertain cases and export the reconciliation report.

Match scores should represent confidence in a candidate match, not proof that
the records are correct. Keep matching rules explainable and make results
reviewable.
