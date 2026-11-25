## Assignment checklist: design, develop, and test a production-ready Hello Agent

Use the checklist as a project brief. Learners should mark an item complete
only when its acceptance evidence can be demonstrated or reviewed. Adapt the
choices to the organization's data, security, and deployment requirements.

| Done | Phase | Checklist item | Evidence / acceptance criteria |
|---|---|---|---|
| [ ] | Design | Define users, supported questions, data owners, and out-of-scope uses. | Product brief names target users, use cases, data boundaries, and a human escalation path. |
| [ ] | Design | Define the data contract for CSV input. | Documented required/optional columns, encoding, null handling, size/row limits, duplicate-file behavior, and validation rules. |
| [ ] | Design | Choose a retrieval strategy appropriate to the corpus. | Decision record compares the current keyword matcher with alternatives; retrieval behavior is tested against representative paraphrases and ambiguous queries. |
| [ ] | Design | Specify response and evidence requirements. | Response contract includes no-match behavior, uncertainty, source file/row citations, and rules for numeric calculations. |
| [ ] | Design | Complete privacy, threat, and risk reviews. | Data-flow and threat models identify uploads, model-provider transfer, prompt injection, access boundaries, retention, and mitigations. |
| [ ] | Design | Set measurable service objectives and operating limits. | Approved latency, availability, throughput, cost, upload limits, timeout, and rate-limit targets. |
| [ ] | Develop | Implement robust CSV validation and resource limits. | Invalid encoding, malformed CSV, empty files, excessive rows/bytes/files, duplicate headers, and hostile inputs return clear, safe errors. |
| [ ] | Develop | Add authentication, authorization, and transport security. | Only authorized users can access the application and permitted datasets; secrets and traffic are protected. |
| [ ] | Develop | Protect and govern uploaded data. | Retention/deletion, encryption, malware/content handling as applicable, provider disclosure, and data-minimization policies are implemented and documented. |
| [ ] | Develop | Harden model instructions and tool permissions. | Agent has least-privilege tools; untrusted CSV cells are treated as data; no arbitrary code execution; provider/model settings are controlled. |
| [ ] | Develop | Make answers inspectable and useful. | Answers include traceable sources, distinguish source facts from calculations, and provide a safe fallback or escalation when evidence is insufficient. |
| [ ] | Develop | Add operational observability. | Structured logs, request IDs, latency/error metrics, provider status, and cost/usage tracking are available without logging secrets or unnecessary sensitive data. |
| [ ] | Develop | Package and deploy reproducibly. | Pinned/reviewed dependencies, separate configuration, health/readiness checks, deployment instructions, and rollback procedure are documented. |
| [ ] | Test | Add unit tests for parsing, matching, and answer boundaries. | Tests cover normal data, no matches, paraphrases, ambiguous terms, missing values, numeric fields, and row ranking/limits. |
| [ ] | Test | Add API and frontend integration tests. | Tests cover single/multiple uploads, samples, same-name replacement, invalid uploads, API errors, timeouts, and response rendering. |
| [ ] | Test | Build a representative answer-quality evaluation set. | Curated questions have expected source rows, acceptable answers, and no-answer cases; retrieval and answer quality meet agreed thresholds. |
| [ ] | Test | Test adversarial and privacy scenarios. | Prompt-injection-like cell content, oversized files, malformed requests, unauthorized access, secret exposure, and sensitive-data handling are checked. |
| [ ] | Test | Run performance, resilience, and cost tests. | Load tests meet objectives; provider failure, rate limits, retries, timeouts, and graceful degradation behave as specified. |
| [ ] | Test | Validate production release and ongoing ownership. | Release checklist, monitoring alerts, incident/runbook, data/model change review, owner, and recurring evaluation schedule are in place. |
