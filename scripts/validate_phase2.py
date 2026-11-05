#!/usr/bin/env python3
"""Cross-check fictional v0.2 DORA/GDPR decision, evidence and reporting exercises.

This educational model is NOT a legal rules engine or valid reporting interface.
"""
import calendar
import csv
from collections import Counter
from datetime import timedelta
from pathlib import Path

from validate_project import ROOT, records, utc, fmt, validate

P2=ROOT/"phase2"/"data"

def p2_load(name):
    with (P2/name).open(encoding="utf-8",newline="") as f:
        return list(csv.DictReader(f))

def plus_calendar_month(value):
    month = 1 if value.month == 12 else value.month + 1
    year = value.year + (1 if value.month == 12 else 0)
    day = min(value.day,calendar.monthrange(year,month)[1])
    return value.replace(year=year,month=month,day=day)

def major_case(r):
    if r["recurring_requires_individual_assessment"]=="Yes":
        return "Requires recurring-incident review"
    critical=r["critical_service"]=="Yes"
    thresholds=sum(r[x]=="Yes" for x in ("client_threshold","downtime_threshold"))
    thresholds+=int(r["other_threshold_count"])
    if critical and (r["malicious_access_data_loss_threshold"]=="Yes" or thresholds>=2):
        return "Major (scenario)"
    return "Not major on supplied facts"

def validate_phase2():
    validate()
    cases=p2_load("edge_case_decisions.csv")
    clocks=p2_load("timeline_exercises.csv")
    requests=p2_load("evidence_requests.csv")
    assert len(cases)==len({c["case_id"] for c in cases})==9
    assert len(clocks)==len({c["exercise_id"] for c in clocks})==5
    assert len(requests)==len({r["request_id"] for r in requests})==9
    case_by={c["case_id"]:c for c in cases}
    clock_by={c["exercise_id"]:c for c in clocks}
    assert set(case_by)=={"EDGE-"+str(x) for x in range(201,210)}
    assert set(clock_by)=={"CLK-"+str(x) for x in range(201,206)}
    assert Counter(c["dora_result"] for c in cases)=={
        "Major (scenario)":2,
        "Not major on supplied facts":6,
        "Requires recurring-incident review":1
    }
    for c in cases:
        assert all(c[k] in ("Yes","No") for k in ("critical_service","client_threshold",
              "downtime_threshold","malicious_access_data_loss_threshold",
              "recurring_requires_individual_assessment","personal_data_breach",
              "risk_to_people","high_risk_to_people","gdpr_authority","gdpr_individuals"))
        assert int(c["other_threshold_count"])>=0
        assert c["dora_result"]==major_case(c),c["case_id"]
        breach=c["personal_data_breach"]=="Yes"
        risk=c["risk_to_people"]=="Yes"
        high=c["high_risk_to_people"]=="Yes"
        assert not (high and not risk),c["case_id"]
        assert not (risk and not breach),c["case_id"]
        assert c["gdpr_authority"]==("Yes" if breach and risk else "No")
        assert c["gdpr_individuals"]==("Yes" if breach and high else "No")
        assert len(c["decision_limit"])>=30
    assert case_by["EDGE-205"]["dora_result"]=="Requires recurring-incident review"
    assert case_by["EDGE-202"]["dora_result"]=="Major (scenario)"
    assert case_by["EDGE-208"]["personal_data_breach"]=="Yes" and case_by["EDGE-208"]["gdpr_authority"]=="No"

    for row in clocks:
        case=case_by[row["edge_case_id"]]
        assert row["real_submission_status"]=="NONE - TRAINING"
        fields=("illustrative_dora_initial_sent_utc","illustrative_dora_intermediate_sent_utc",
                "illustrative_gdpr_authority_sent_utc","illustrative_processor_notice_utc")
        if case["dora_result"]=="Major (scenario)":
            aware=utc(row["entity_ict_awareness_utc"])
            classified=utc(row["major_classification_utc"])
            assert aware and classified and classified>=aware
            due=(classified+timedelta(hours=4) if classified>aware+timedelta(hours=24)
                 else min(classified+timedelta(hours=4),aware+timedelta(hours=24)))
            assert row["calculated_dora_initial_due_utc"]==fmt(due)
            first=utc(row["illustrative_dora_initial_sent_utc"])
            assert first and classified<=first<=due
            intermediate_due=first+timedelta(hours=72)
            assert row["calculated_dora_intermediate_due_utc"]==fmt(intermediate_due)
            intermediate=utc(row["illustrative_dora_intermediate_sent_utc"])
            assert intermediate and first<=intermediate<=intermediate_due
            assert row["calculated_dora_final_due_utc"]==fmt(plus_calendar_month(intermediate))
        else:
            assert not any(row[k] for k in (
                "entity_ict_awareness_utc","major_classification_utc","calculated_dora_initial_due_utc",
                "illustrative_dora_initial_sent_utc","calculated_dora_intermediate_due_utc",
                "illustrative_dora_intermediate_sent_utc","calculated_dora_final_due_utc"))
        if case["gdpr_authority"]=="Yes":
            controller_aware=utc(row["controller_breach_awareness_utc"])
            assert controller_aware
            due=controller_aware+timedelta(hours=72)
            assert row["calculated_gdpr_authority_due_utc"]==fmt(due)
            illustrative=utc(row["illustrative_gdpr_authority_sent_utc"])
            assert illustrative and controller_aware<=illustrative<=due
        else:
            assert not row["controller_breach_awareness_utc"] and not row["calculated_gdpr_authority_due_utc"]
            assert not row["illustrative_gdpr_authority_sent_utc"]
        if row["processor_awareness_utc"]:
            assert row["edge_case_id"]=="EDGE-209"
            p=utc(row["processor_awareness_utc"])
            n=utc(row["illustrative_processor_notice_utc"])
            c=utc(row["controller_breach_awareness_utc"])
            assert p<=n<=c
        else:
            assert not row["illustrative_processor_notice_utc"]
        assert "simulation" not in row["exercise_note"].lower() or "TRAINING" in row["real_submission_status"]
    assert (clock_by["CLK-201"]["calculated_dora_intermediate_due_utc"],
            clock_by["CLK-201"]["calculated_dora_final_due_utc"])==(
                "2026-12-13T14:00:00Z","2027-01-13T12:00:00Z")
    assert clock_by["CLK-202"]["calculated_dora_initial_due_utc"]=="2026-12-11T16:00:00Z"
    assert clock_by["CLK-203"]["calculated_dora_initial_due_utc"]=="2026-12-11T09:00:00Z"
    assert clock_by["CLK-205"]["calculated_gdpr_authority_due_utc"]=="2026-12-13T10:00:00Z"
    known=set(case_by)|set(clock_by)|{r["incident_id"] for r in records("data/incident_register.csv")}
    for r in requests:
        assert r["confidence"]=="Not provided - simulation"
        assert r["requested_objective_evidence"] and len(r["decision_gate"])>20
        assert r["evidence_owner"] and r["regulatory_refs"]
        for ident in r["scenario_refs"].split(";"):
            assert ident in known, (r["request_id"],ident)
    print("PASS v0.2: nine independent scenario gates, five training-only timelines, nine open evidence requests; no real reports.")
    return True

if __name__=="__main__":
    validate_phase2()
