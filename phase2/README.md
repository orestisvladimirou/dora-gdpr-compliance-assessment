# Phase 2 — Regulatory decision and timeline exercises

**v0.2 · 5 November 2026 · ENTIRELY FICTIONAL**

The [v0.1 baseline](../README.md) documents three illustrative incident outcomes. This new phase tests harder distinctions without overwriting the original source data or Excel workbook.

- **Nine edge-case decisions:** critical-service qualification, two materiality indicators, special malicious-access pathway, recurrence pending review, GDPR risk versus high risk, and processor/controller duties.
- **Five UTC reporting-clock exercises:** four-hour major classification rule, 24-hour awareness cap, late-classification exception, 72-hour intermediate and GDPR controller deadlines, one-calendar-month DORA final-report example.
- **Nine open evidence requests:** what records would be needed before a real qualified decision.
- **Automated source checks and seven new tests.** All simulated notification times are explicitly *illustrative*, not real submissions.

Read the [classification explanation](docs/06-regulatory-decision-and-evidence.md), [clock exercises](docs/07-separate-clocks.md), [decision register](data/edge_case_decisions.csv), [timeline cases](data/timeline_exercises.csv) and [evidence requests](data/evidence_requests.csv).

Run from repository root:

```sh
python scripts/validate_project.py
python scripts/validate_phase2.py
python -m unittest discover -s tests -v
```

**Important:** The original v0.1 source hashes are preserved in `historical/SOURCE_MANIFEST_v0.1.json`; `Compliance_Assessment_v0.1.xlsx` remains a historical workbook snapshot. These Phase 2 CSVs are *additional* records; the original workbook does not automatically reflect them. Classification logic covers a selected subset of legal criteria and is not suitable for actual compliance decisions.
