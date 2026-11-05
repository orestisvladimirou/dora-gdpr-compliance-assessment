# 09 — Operational resilience tabletop and open corrective actions

**Training exercise, not a performed resilience test.** The fictional tabletop date, **8 January 2027**, is a scenario date in the future relative to project creation. No actual system, employee, third party or payment service was accessed.

## Six modeled stages

1. **Detect** suspicious payment API behavior and route the alert to the incident lead.
2. **Classify** the event using a complete set of DORA materiality factors, not merely the simplified fields in this portfolio.
3. **Contain** possible metadata exposure while preserving hypothetical evidence.
4. **Evaluate reporting** along two separate DORA and GDPR timelines, consulting the regulator reporting lead and DPO.
5. **Recover** the payment API and customer records service against defined recovery objectives.
6. **Learn and improve** using root cause analysis, management ownership and retrospective risk treatment.

The [step log](../data/resilience_tabletop.csv) clearly distinguishes **ROLE-PLAY ONLY**, **NOT TESTED** and **DRAFT ONLY**. Critically, the restoration step is marked **NOT TESTED**. A tabletop design is not a successful recovery drill or evidence of an achieved RTO/RPO.

## Nine unresolved remediations

The [follow-up register](../data/remediation_followup.csv) carries forward **all nine actions** from the baseline register. Draft new artifacts (e.g., incident packet descriptions and the classification checklist) may demonstrate *documentation progress*, but they do not prove control operation. Each row retains:

- original action and status,
- fictional proposed follow-up,
- the evidence's limitation,
- **Not independently verified** or **NOT TESTED**,
- **Not obtained** sign-off,
- **OPEN - SIMULATED** current status,
- concrete objective evidence needed before a defensible closure.

A real management team would need to authorize risk ownership, prioritization, testing and closure. Here it hasn't.

## Case study limitations

The DORA and GDPR regulatory mappings are educational, selected checkpoints. Neither the exercise nor its automated tests validate full compliance or test a live ICT environment. Actual applicability depends on entity status, authorities, contractual roles and up-to-date regulation. No real regulator report, personal-data breach notice, signed management approval, resilience test or professional audit is claimed.

Sources: https://eur-lex.europa.eu/eli/reg/2022/2554/oj and https://eur-lex.europa.eu/eli/reg/2016/679/oj
