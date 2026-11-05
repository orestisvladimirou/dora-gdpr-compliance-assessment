# Phase 3 — Mock regulatory communications and resilience tabletop

**v0.3 · Entirely fictional educational exercise. No reports, notifications or data-subject communications were sent.**

This phase continues from [the Phase 2 decision and clock exercises](../phase2/README.md) without changing the v0.1 historical case files.

| Deliverable | Size | Assurance limitation |
| --- | ---: | --- |
| [Mock communication inventory](data/mock_communication_packets.csv) | 6 | Drafts only: three DORA report stages, two GDPR authority cases, one high-risk subject communication |
| [Resilience tabletop](data/resilience_tabletop.csv) | 6 steps | Pure role play; **no live recovery test** |
| [Remediation follow-up](data/remediation_followup.csv) | 9 actions | All remain **OPEN - SIMULATED**; no signoffs |
| [Automated crosschecks](../scripts/validate_phase3.py) | Validator | Ensures draft reports cannot be mistaken for sent reports |

Read [the communication preparation notes](docs/08-mock-communication-preparation.md) and [the resilience/remediation rehearsal](docs/09-tabletop-and-corrective-action.md).

```sh
python scripts/validate_project.py
python scripts/validate_phase2.py
python scripts/validate_phase3.py
python -m unittest discover -s tests -v
```

The original v0.1 Excel workbook remains a baseline **snapshot**. No role-play outcome constitutes legal advice, operational recovery assurance, regulator communication, DORA compliance or GDPR compliance. All scenarios are hypothetical December 2026 or January 2027 events.
