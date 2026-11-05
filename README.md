# DORA & GDPR Compliance Assessment — Fictional EU Financial Services Exercise

**Independent cybersecurity governance portfolio project · v0.3 · 5 November 2026**

> **ENTIRELY SYNTHETIC.** Aurora Payment Services (fictional), suppliers, incidents, controls, employees, information, decisions, reports and evidence are invented. No regulatory report was sent, no actual organization was assessed, and this project is **not an attestation of DORA or GDPR compliance, legal advice, or employment experience**.

## Purpose

This case study trains the **regulatory decision and evidence workflow** an information security/governance role might support at an EU financial entity. It is distinct from a general supplier-risk model or an ISO 27001 ISMS gap assessment: the core deliverables are **two independent incident-reporting assessments** (DORA and GDPR), a mapped obligation register, fictional ICT contractual arrangements, evidence gaps and documented remediation.

The organization is *assumed* to be an in-scope EU payment institution for teaching purposes. Neither its legal status, supervisory authority nor jurisdictional reporting channel is verified. The incident scenarios are set in **December 2026**, deliberately later than the package creation date; they are hypothetical future events, not historical facts.

## Contents

| File | Function |
|---|---|
| [`data/incident_register.csv`](data/incident_register.csv) | Three invented incidents, critical-service data, personal-data assessment and different reporting decisions |
| [`data/regulatory_obligations.csv`](data/regulatory_obligations.csv) | 19 DORA/GDPR obligation checkpoints with status, evidence and remediation owner |
| [`data/services_and_assets.csv`](data/services_and_assets.csv) | Fictional critical services and information assets |
| [`data/ict_arrangements.csv`](data/ict_arrangements.csv) | Three fictional ICT arrangements; **not** the official DORA ITS register |
| [`data/evidence_register.csv`](data/evidence_register.csv) | Synthetic or missing evidence with assurance limitations |
| [`data/remediation_tracker.csv`](data/remediation_tracker.csv) | Nine open actions; none approved or completed |
| [`docs/01-scenario-and-scope.md`](docs/01-scenario-and-scope.md) | Assumed business, criticality, roles and boundaries |
| [`docs/02-dora-classification-and-reporting.md`](docs/02-dora-classification-and-reporting.md) | DORA major-incident decision and clocks |
| [`docs/03-gdpr-breach-triage.md`](docs/03-gdpr-breach-triage.md) | GDPR reportability, rights/freedoms risk and independent clock |
| [`docs/04-executive-report.md`](docs/04-executive-report.md) | Management-facing recommendations and unresolved legal gates |
| [`docs/05-regulatory-sources.md`](docs/05-regulatory-sources.md) | Official source links, scope and limitations |
| [`scripts/validate_project.py`](scripts/validate_project.py) | Automated cross-file and reporting-clock consistency validation |
| [`Compliance_Assessment_v0.1.xlsx`](Compliance_Assessment_v0.1.xlsx) | Editable executive dashboard and source registers |

## Phase 2 — Extended regulatory decision exercises (v0.2)

The [Phase 2 dossier](phase2/README.md) contains **nine additional DORA/GDPR classification scenarios**, five explicitly fictional notification-clock exercises and nine evidence requests. Cases cover the special DORA malicious-access threshold, recurrence needing review, two materiality thresholds, the 24-hour awareness cap, post-24-hour major classification, intermediate/final deadlines, and the distinction between the GDPR processor's notice and the controller's 72-hour awareness clock.

All hypothetical submission timestamps are **training examples**, not real regulatory notices. The v0.1 baseline and workbook remain intact; the workbook is a historical snapshot rather than a live Phase 2 dashboard.

## Phase 3 — Draft reporting packets and tabletop (v0.3)

The [Phase 3 dossier](phase3/README.md) includes **six draft communication records** (three DORA report stages, two GDPR supervisory-authority notices and one assumed high-risk individual communication), six **tabletop-only** resilience steps and a follow-up register covering all nine original corrective actions. Every notification is marked **NONE - SIMULATED**; the recovery step is **NOT TESTED**, and all nine corrective actions remain open and unapproved.

The historical v0.1 data, baseline Excel workbook and original decisions remain unchanged. The Phase 2 and Phase 3 datasets are separate **future-dated fictional exercises**, not actual incidents or filings.

## Three contrasting scenarios

| Scenario | DORA major? | GDPR personal-data breach authority notification? | Why (assumed facts) |
|---|---|---|---|
| INC-001 — payment API compromise and outage | **Yes** | **Yes** | Critical service + 12.4% customer impact and 3.5-hour outage; documented personal-data exposure potentially harmful to individuals |
| INC-002 — minor internal dashboard slowdown | **No** | **No** | Not critical service, short disruption, no personal-data breach found |
| INC-003 — mistakenly disclosed contact export | **No** | **Yes** | Personal-data breach presenting risk; does not affect a critical ICT service |

Classifications are simplified exercises that depend on facts and require expert verification. DORA uses its detailed classification regulation; these scenarios **do not replace the full decision criteria**. A notification decision is not evidence that a report was actually filed.

## Run checks

```bash
python scripts/validate_project.py
python scripts/validate_phase2.py
python scripts/validate_phase3.py
python -m unittest discover -s tests -v
```

No external Python libraries are required to validate the CSV source data. Excel is a separate **v0.1 snapshot**, not a regulatory submission template and not automatically synchronized with the CSV files.

## Implementation roadmap

- **Phase 1 (v0.1):** Fictional organization, obligation and evidence registers, three incident comparisons, reportability checks and workbook.
- **Phase 2 (v0.2): Completed** nine classification scenarios, five illustrative timelines, nine evidence requests and new automated tests.
- **Phase 3 (v0.3): Completed** draft regulatory communication preparation, resilience tabletop design and nine clearly open simulated corrective-action follow-ups.
- **Final:** Review clarity, documentation, automated checks, potential sensitive information and portfolio suitability before publication.

Keep the eventual GitHub repository **private throughout development**. Publish only after manual owner review and explicit approval.
