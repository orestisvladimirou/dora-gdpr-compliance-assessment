# 02 — DORA major ICT-related incident assessment

**Simulation only. No competent authority received any report.** All times in UTC and all incident dates in December 2026 are hypothetical.

## Regulatory logic (simplified test model)

For the training scenario, Article 8 of Delegated Regulation (EU) 2024/1772 requires an incident to affect critical services and satisfy **either** the specified malicious unauthorized access/data-loss criterion **or** at least two of the other relevant materiality thresholds. These thresholds include impact on clients/transactions, service downtime, geographical spread, reputational impact, data loss and economic impact. A complete legal decision must examine **all** criteria, thresholds, exceptions and facts—not only the modeled subset here.

| Incident | Critical service? | Selected materiality indicators | Exercise decision |
|---|---|---|---|
| INC-001 | Yes | 12.4% affected clients; 3.5h downtime for critical function; malicious access to customer-data infrastructure | Major (assumed) |
| INC-002 | No | 0.4% clients and 45min internal dashboard disruption | Not major on supplied facts |
| INC-003 | No | Unauthorized email disclosure unrelated to a critical ICT-service disruption | Not major on supplied facts |

The malicious-access indicator is shown separately: Article 9(5)(b) has a specific threshold and should not be conflated with *any* operational IT access event. The scenarios are simplified and not a classifier suitable for live use.

## Incident INC-001 reporting-clock example

- Entity becomes aware of ICT incident: **2026-12-10 09:00 UTC**.
- Fictional major-incident classification: **2026-12-10 11:00 UTC**.
- DORA initial notification deadline, under Delegated Regulation (EU) 2025/301 Article 5(1)(a): as early as possible, **no later than 15:00 UTC** (four hours after classification), and within 24 hours of awareness.
- If classification first occurs after 24 hours, Article 5(2) contains a specific later-classification rule; do not naively apply a deadline that predates classification.
- Intermediate: at the latest 72 hours following **actual** initial notification submission, including where no status changes. Updated intermediates and a final report have separate requirements. The final deadline depends on the intermediate-report timeline; no submission timestamp exists in this repository, so **intermediate/final due dates are intentionally not invented**.

In real reporting, regulatory templates and the specific competent authority's channel must be checked. This exercise performs **no actual submission**.

Source: https://eur-lex.europa.eu/eli/reg_del/2024/1772/oj and https://eur-lex.europa.eu/eli/reg_del/2025/301/oj
