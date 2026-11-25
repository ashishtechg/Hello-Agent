# Hello Agent Business Requirements

## Document purpose

This document describes the current Hello Agent product baseline: its users,
business purpose, supported behavior, and known boundaries. It is not a
specification for enterprise features that have not been implemented.

## Product summary

Hello Agent is a web application for asking natural-language questions about
tabular data in CSV files. A user selects the bundled example datasets,
uploads CSV files, or uses both. The application searches for rows with words
that overlap the question and asks a configured language model to form an
answer from those rows.

## Users and business need

### Primary users

- Employees who need to look up information in one or more CSV files.
- Teams that maintain or receive data as CSV exports.
- Developers or operators who configure and run the frontend and backend.

### Business need

Users need a simpler way to find relevant information in CSV data than
manually scanning or filtering tables. Hello Agent offers a chat-style
interface for this lookup workflow.

## Business goals

- Let users ask questions about selected CSV data in plain language.
- Reduce the effort required to locate relevant rows in small CSV datasets.
- Provide a readable response grounded in rows found by the application.
- Support an easy local demonstration using bundled sample datasets.

## In-scope capabilities

1. Provide a Streamlit chat interface.
2. Let users optionally include the bundled sample datasets. This option is
   enabled by default in the frontend.
3. Let users upload multiple CSV files, up to 10 files per request.
4. Accept valid, non-empty UTF-8 CSV files up to 5 MB and 10,000 data rows
   each.
5. Replace a bundled sample dataset when an uploaded file has the same
   filename.
6. Require at least one available dataset, from uploads or enabled samples,
   before answering.
7. Search rows using keyword overlap between the question and row column names
   and values. Return at most 40 ranked rows to the agent.
8. Use a configured OpenAI-compatible model through the backend to compose an
   answer using matching rows.
9. Return the exact no-match response
   `I could not find this information in the uploaded files.` when no rows
   match or the retrieved information is insufficient.
10. Display the answer in the chat interface. The API response also includes
    filenames used and the total row count.
11. Display backend validation, HTTP, and connection errors to the user.

## User workflow

1. Open the Streamlit application.
2. Keep the example datasets enabled, upload one or more CSV files, or do
   both.
3. Enter a question about the selected data.
4. The frontend submits the question and selected data to the FastAPI backend.
5. The backend validates and loads the data, finds relevant rows, and uses the
   configured model to prepare an answer when rows match.
6. Read the answer in the chat interface.

## Business rules and constraints

- Each question is answered independently. Previous chat messages are shown
  in the frontend but are not sent as context with the next question.
- Search is based on keyword overlap, not semantic similarity. Different
  wording, synonyms, or ambiguous questions may not find the intended rows.
- Only up to 40 ranked matching rows are supplied to the agent.
- The model is instructed to answer only from returned rows and treat CSV
  contents as data, not instructions. Model output may still be incomplete or
  incorrect and should be checked when accuracy is important.
- CSV uploads are processed for the request and are not persisted in a
  database by the application.
- If an API key is configured, the question and matching rows are sent from
  the backend to the configured model provider.
- A model API key is required to answer questions. Supported configuration
  includes OpenRouter or OpenAI-compatible API settings.

## Out of scope in the current baseline

The current application does not provide:

- Authentication, user accounts, or role-based access control.
- Persistent dataset storage, dataset administration, or scheduled imports.
- Reconciliation or comparison of two CSVs, fuzzy record matching, or
  configurable business-rule validation across records.
- Semantic search, guaranteed citations to individual rows, or guaranteed
  factual correctness.
- Audit trails, organization-wide usage analytics, or production service
  objectives.

## Acceptance criteria for the current baseline

- A user can ask a question when at least one sample or uploaded dataset is
  available.
- The frontend sends the current question and selected uploads to the
  configured backend.
- Valid CSV inputs within the documented limits are available to the
  question-answering flow.
- Invalid or missing data, blank questions, unavailable backend, and backend
  failures are reported rather than shown as successful answers.
- Matching questions produce a readable response based on retrieved rows;
  unmatched questions use the specified no-match response.
- The application does not send earlier chat messages as context for later
  questions.
