# 07 — Separate clocks and reporting escalation (fictional Phase 2)

**Every timestamp is an illustrative simulated event, NOT an actual regulator submission.** These exercises model hypothetical future events in December 2026. All timestamps are UTC; the competent authority and reporting template are intentionally unspecified.

## DORA timeline assumptions

Under [Delegated Regulation (EU) 2025/301 Article 5](https://eur-lex.europa.eu/eli/reg_del/2025/301/oj):

- The initial report for a major incident is due as early as possible, no later than **4 hours after major classification** and no later than **24 hours after ICT awareness**.
- When major classification occurs **after 24 hours of ICT awareness**, Article 5(2) provides a special 4-hours-after-classification requirement.
- An intermediate report is due no later than **72 hours after the initial report is submitted**; additional intermediate updates may be required.
- A final report is due no later than **one calendar month after the intermediate report or latest updated intermediate report**, whichever applies. The scenarios assume no subsequent updated intermediate.
- If reporting is impossible on time, different regulator notification and reasons requirements apply. This exercise **does not** model them or suggest that late reporting is acceptable.

| Exercise | ICT awareness | Major classification | Initial deadline | Illustrative first report | Intermediate deadline |
| --- | --- | --- | --- | --- | --- |
| CLK-201 | 10 Dec 09:00 | 10 Dec 11:00 | 10 Dec 15:00 | 10 Dec 14:00 | 13 Dec 14:00 |
| CLK-202 | 10 Dec 09:00 | 11 Dec 12:00 (>24h) | **11 Dec 16:00** | 11 Dec 15:30 | 14 Dec 15:30 |
| CLK-203 | 10 Dec 09:00 | 11 Dec 07:30 (<24h) | **11 Dec 09:00** | 11 Dec 08:45 | 14 Dec 08:45 |

**Important difference from Phase 1:** The baseline source register intentionally leaves intermediate/final deadlines *unknown* without actual submissions. Phase 2 uses **explicitly fabricated illustrative submission times** to demonstrate calculation; it does not retroactively claim submissions in Phase 1.

## GDPR and processor clock

Under GDPR Article 33, the controller documents when it became aware of a qualifying personal-data breach. Illustrative 72-hour planning deadlines follow this awareness, not the DORA ICT detection timestamp. An appointed processor alerts the controller **without undue delay**; the GDPR does not set a numeric 72-hour processor-to-controller limit.

- **CLK-204:** GDPR-only scenario, controller aware 12 Dec 13:30; 72-hour planning deadline 15 Dec 13:30.
- **CLK-205:** processor aware 10 Dec 06:00; hypothetical processor notice 09:00; controller becomes aware 10:00; 72-hour planning deadline 13 Dec 10:00.

Individual communications under Article 34 are assessed separately from authority notification. The relevant authority, language, cross-border lead authority and any legal exceptions require professional verification.

## Correct use

These calculations illustrate **deadline arithmetic only**, not regulatory sufficiency. Always check whether a factual awareness/classification threshold was actually reached, whether a report is mandatory, and whether the reporting route and prescribed content are correct.

See the [clock dataset](../data/timeline_exercises.csv) and the [automated cross-checks](../../scripts/validate_phase2.py).

Official sources:
- https://eur-lex.europa.eu/eli/reg_del/2025/301/oj
- https://eur-lex.europa.eu/eli/reg/2016/679/oj
- https://www.edpb.europa.eu/documents/guideline/guidelines-92022-on-personal-data-breach-notification-under-gdpr_en
