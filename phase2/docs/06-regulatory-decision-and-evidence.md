# 06 — Regulatory classification and evidence traceability (fictional Phase 2)

**SIMULATED EXERCISE, not legal or operational advice.** All nine EDGE cases are invented and take place in a hypothetical December 2026 review. No real reporting or regulatory conclusions have been reached.

## DORA: classification logic

For this educational exercise, [Commission Delegated Regulation (EU) 2024/1772](https://eur-lex.europa.eu/eli/reg_del/2024/1772/oj), Articles 8–9, provides the major classification architecture: an affected critical service plus either (a) the specific successful malicious unauthorized access/data-loss pathway in Article 9(5)(b) or (b) two or more other materiality thresholds. This simplified model explicitly tests the client and critical-service downtime thresholds and accepts fictional flags for other criteria, **but it is not a full RTS implementation**.

| Case | Input scenario | Example exercise conclusion |
| --- | --- | --- |
| EDGE-201 | Critical service; clients and downtime both exceed assumed thresholds | Major |
| EDGE-202 | Critical service; successful malicious unauthorized access potentially causing data loss | Major |
| EDGE-203 | Critical service; only one documented materiality threshold | Not major *on supplied facts* |
| EDGE-204 | Noncritical tool; two assumed thresholds | Not major *if service scope assumption holds* |
| EDGE-205 | Two incidents with apparently shared root cause within six months | **Further recurrence review**; not automatically major |

Article 8(2) has extra recurrence conditions and exceptions for some entities. Mere repetition or a similar alert is not proof the conditions are met. No real enterprise classification should rely on this subset of criteria without actual affected-service and materiality evidence.

## GDPR: independent risk and high-risk tests

Under GDPR Article 33, authority notification is generally needed for a personal-data breach unless it is unlikely to result in risk to individuals; it is due without undue delay and, where feasible, within 72 hours of the controller becoming aware. Under Article 34, **high-risk** breaches generally also trigger direct communication to individuals, subject to exceptions and the actual facts.

The matrix explicitly distinguishes:
- **EDGE-206**: risk present but high risk not established — authority notification assumed, no individual communication assumed.
- **EDGE-207**: high risk — authority and individual communication *provisionally* assumed, with Article 34 exceptions still needing review.
- **EDGE-208**: breach with no likely risk on assumed facts — document the incident but don't presume an authority notice.
- **EDGE-209**: processor-to-controller notification must occur without undue delay; controller's own awareness is separately evaluated.

A GDPR breach can exist without a DORA-major ICT incident. A DORA-major outage does not itself establish a personal-data breach.

## Evidence and governance

The [nine open evidence requests](../data/evidence_requests.csv) map each case to the factual records an ICT lead, DPO, procurement team or management would need to review. All evidence requests are **not provided — simulation**. No regulatory authority, supervisory country, final applicability gate, DPO opinion, manager signature or notification receipt is claimed.

Official sources:
- https://eur-lex.europa.eu/eli/reg_del/2024/1772/oj
- https://eur-lex.europa.eu/eli/reg/2016/679/oj
- https://www.edpb.europa.eu/topics/security-data-breaches/personal-data-breaches_en
