# DORA & GDPR Compliance — Executive Portfolio Dashboard

> **FICTIONAL EU FINANCIAL-SERVICES CASE STUDY, NOT LEGAL ADVICE, NOT VERIFIED REGULATORY COMPLIANCE.**  
> Aurora Payment Services, all incidents, suppliers, records, proposed actions and reporting decisions are invented. The incident/event dates in December 2026 and the tabletop on 8 January 2027 are hypothetical future scenario dates. No reports, contacts, regulator submissions, system tests or management approvals occurred.

## Executive overview

| Dimension | Simulated result | Limitation |
| --- | ---: | --- |
| DORA-major ICT incidents in initial cases | **1 of 3** | Simplified subset of criteria, not a live classifier |
| GDPR authority notification cases | **2 of 3** | Independent rights-and-freedoms risk assessment |
| GDPR individual communication cases | **1 of 3** | High-risk assumption, with Article 34 exceptions unresolved |
| Regulatory checkpoints mapped | **19** (11 DORA, 8 GDPR) | Selected obligations only |
| Checkpoint status | **9 Gap · 8 Partial · 2 Not verified** | Training observations, **not** official noncompliance findings |
| ICT arrangements | **3** | Not an ITS-compliant DORA register |
| Risk/remediation actions | **9 open** | None approved or independently closed |
| DORA/GDPR edge decisions | **9** | Includes one deliberately unresolved recurrence case |
| Reporting-clock exercises | **5** | Any populated report timestamp is explicitly fictitious |
| Draft regulatory communication records | **6** | **Zero real submissions** |
| Resilience tabletop steps | **6** | **Zero demonstrated service restores** |

## The three core incidents

| Case | DORA major? | GDPR supervisory authority? | Communicate to individuals? |
| --- | --- | --- | --- |
| INC-001: payment API compromise and customer metadata exposure | Assumed **Yes** | Assumed **Yes** | Provisionally **Yes** |
| INC-002: internal dashboard slowdown | **No** on given facts | **No** | **No** |
| INC-003: mistakenly shared contact export | **No** on given facts | Assumed **Yes** | **No** on given facts |

These determinations are deliberately independent. An ICT incident is not necessarily a personal-data breach, and a personal-data breach is not automatically a DORA-major incident.

## Timing decisions — separate regulatory clocks

| Reporting obligation | Assumed trigger | General planning approach |
| --- | --- | --- |
| DORA initial major-ICT notification | Major classification **and** awareness of ICT incident | As soon as possible; four hours from major classification, with a 24-hour awareness ceiling except the late-classification rule |
| DORA intermediate report | Actual initial notification submission | Within 72 hours after that submission |
| DORA final report | Latest intermediate report, where applicable | No later than one calendar month after the applicable intermediate submission |
| GDPR supervisory authority | Controller awareness of a reportable personal-data breach | Without undue delay; where feasible within 72 hours |
| GDPR affected individuals | Likely high risk to rights and freedoms | Without undue delay, subject to Article 34 exceptions |

**Phase 1 has no actual submission timestamps**, so its intermediate/final reporting deadlines correctly remain unknown. Phase 2 introduces **hypothetical illustrative submissions**, labeled as exercises, to teach arithmetic without inventing actual notices. For DORA exceptions and detailed forms, review the current implementing regulations and competent authority instructions.

[Review the five clock examples](../phase2/data/timeline_exercises.csv) · [Read the DORA/GDPR reporting analysis](../phase2/docs/07-separate-clocks.md)

## Readiness gaps and evidence

The **19 checkpoints** are split into nine modeled gaps, eight partial observations and two without verification. The source register records owners and regulatory URLs. The nine evidence register entries are synthetic or explicitly missing. The nine corrective actions remain **open** even after later documentation exercises.

The fictional resilience tabletop includes no restoration test: documentation of a proposed recovery step is not evidence that a critical payment service meets RTO/RPO goals. Similarly, building a mock notification packet does not satisfy a real regulator reporting requirement.

[Obligation register](../data/regulatory_obligations.csv) · [Open remediation register](../data/remediation_tracker.csv) · [Phase 3 follow-up](../phase3/data/remediation_followup.csv)

## Decision and management priorities

1. Validate whether the organization is truly in DORA's scope, what functions are critical, which EU supervisory authority applies, and what official incident templates/communication channels are required.
2. Establish DORA major-incident classification procedures against **all** thresholds and recurrence conditions, with legal/compliance and risk-owner approval.
3. Distinguish ICT detection, major classification, controller awareness, processor escalation, and each submitted reporting stage.
4. Complete an appropriate ICT third-party **register of information**, contractual control review, RoPA and case-by-case DPIA screening where relevant.
5. Perform a witnessed resilience/recovery exercise and independently verify remediation before any closure or risk acceptance.
6. Document GDPR notification decisions, risk-to-individuals analysis and any high-risk subject communication, regardless of whether an authority notification ultimately becomes necessary.

## Portfolio integrity

The [quality review](docs/final-quality-review.md) describes what has been verified and what remains unproven. [Machine-readable indicator definitions](data/portfolio_metrics.csv) are checked against the underlying source CSVs.

The original [v0.1 workbook](../Compliance_Assessment_v0.1.xlsx) is a baseline snapshot, not a live dashboard or submission form. The v0.2 and v0.3 cases are recorded in separate folders. All source documents avoid real account details and do not claim certifications, paid audits or actual regulatory filings.

## Reproduce automated consistency checks

```sh
python scripts/validate_project.py
python scripts/validate_phase2.py
python scripts/validate_phase3.py
python scripts/validate_portfolio.py
python scripts/validate_manifest.py
python -m unittest discover -s tests -v
```

These tests check arithmetic, provenance and consistency, **not** actual compliance with DORA/GDPR. The source materials are independent paraphrases and summaries; a real assessment needs up-to-date official law, supervisory guidance and documented operating evidence.
