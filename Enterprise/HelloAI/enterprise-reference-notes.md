# HelloAI Enterprise Reference Notes

This file collects monetization ideas, pilot measures, and implementation
cautions for reference, along with a suggested initial feature set. It is
separate from the use-case and utility lists.

## Important distinction

The current app answers questions using keyword-matched CSV rows. It does not
currently compare two CSV files, reconcile records, or validate matches.
Those capabilities would need to be implemented as data-processing features.
AI can help interpret instructions and explain results, but should not be the
sole decision-maker for financial or operational reconciliation.

## Straightforward ways to monetize

- **Paid pilot:** Charge for setup and a short trial using one team's approved
  CSVs.
- **Setup and integration:** Charge to configure datasets, deployment,
  branding, and onboarding.
- **Per-team subscription:** Charge a monthly fee for access, support, and an
  agreed usage level.
- **Managed service:** Charge recurring fees to prepare and maintain CSV data
  sources on an agreed schedule.
- **Premium tier:** Offer private deployment, access controls, auditability,
  and support after those capabilities are implemented.

A simple starting offer is to configure HelloAI for one team and a small set
of approved CSVs, run a pilot, and measure time saved on common questions.

## Benefits to measure in a pilot

Track:

- Average time to answer common questions.
- How often employees need a colleague's help to find information.
- Employee ratings of answer usefulness.
- The rate of unsupported or missed answers.

Use the results to help the client decide whether a broader rollout is
worthwhile.

## Important before selling it as an enterprise tool

The current app is a prototype. It does not yet provide features such as user
authentication, role-based access, or persistent managed datasets. Its search
uses keyword overlap, so it can miss synonyms or ambiguous questions.

When a model API key is configured, questions and matching rows are sent to
the selected AI provider. Confirm the client's data-sharing requirements
before using business data.

Before wider deployment, assess access controls, data handling, audit history,
dataset management, search quality, operational support, and the client's
security and compliance requirements.

## Suggested first release

Start with exact-key reconciliation, duplicate detection, configurable amount
and date tolerances, and CSV export. Add fuzzy matching and AI-generated
explanations after the deterministic results are tested against representative
data.
