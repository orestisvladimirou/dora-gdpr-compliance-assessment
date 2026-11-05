#!/usr/bin/env python3
"""Validate fictional regulatory draft communications, tabletop and open remediation."""
import csv
from collections import Counter
from datetime import datetime

from validate_phase2 import validate_phase2
from validate_project import ROOT, records, utc

P3=ROOT/"phase3"/"data"

def p3_load(filename):
    with (P3/filename).open(encoding="utf-8",newline="") as f:
        return list(csv.DictReader(f))

def unique(rows,key,expected):
    keys=[r[key] for r in rows]
    assert len(keys)==len(set(keys))==expected,(key,len(keys))
    return set(keys)

def validate_phase3():
    validate_phase2()
    base={r["incident_id"]:r for r in records("data/incident_register.csv")}
    old_actions={r["action_id"]:r for r in records("data/remediation_tracker.csv")}
    packets=p3_load("mock_communication_packets.csv")
    tabletop=p3_load("resilience_tabletop.csv")
    followup=p3_load("remediation_followup.csv")
    unique(packets,"packet_id",6)
    unique(tabletop,"step_id",6)
    assert unique(followup,"action_id",9)==set(old_actions)
    assert Counter(r["framework"] for r in packets)=={"DORA":3,"GDPR":3}
    assert Counter(r["packet_stage"] for r in packets)=={
        "Initial":1,"Intermediate":1,"Final":1,
        "Authority notification":2,"Individual communication":1
    }
    assert {(r["incident_id"],r["packet_stage"]) for r in packets}=={
        ("INC-001","Initial"),("INC-001","Intermediate"),("INC-001","Final"),
        ("INC-001","Authority notification"),("INC-003","Authority notification"),
        ("INC-001","Individual communication")
    }
    for r in packets:
        assert r["incident_id"] in base
        assert r["review_status"]=="DRAFT - SIMULATED"
        assert r["actual_submission"]=="NONE - SIMULATED"
        assert r["expected_content_scope"] and len(r["key_unknowns"])>18
        assert r["accountable_role"] and r["model_reference"]
        assert utc(r["scenario_preparation_utc"])>=utc(base[r["incident_id"]]["ict_aware_utc"])
        if r["framework"]=="DORA":
            assert base[r["incident_id"]]["dora_major_expected"]=="Yes"
        if r["packet_stage"]=="Authority notification":
            assert base[r["incident_id"]]["gdpr_authority_notification_expected"]=="Yes"
        if r["packet_stage"]=="Individual communication":
            assert base[r["incident_id"]]["gdpr_subject_communication_expected"]=="Yes"
    assert any("No real" in r["key_unknowns"] for r in packets if r["packet_stage"]=="Intermediate")

    assert Counter(r["result"] for r in tabletop)=={
        "ROLE-PLAY ONLY":4,"NOT TESTED":1,"DRAFT ONLY":1
    }
    for r in tabletop:
        assert r["followup_action"] in old_actions
        assert datetime.fromisoformat(r["scenario_date"]).date()>datetime(2026,11,5).date()
        assert r["target_evidence"] and r["limitation"] and r["hypothetical_team_action"]
    restore=[r for r in tabletop if r["phase"]=="Service recovery"]
    assert len(restore)==1 and restore[0]["result"]=="NOT TESTED"

    for row in followup:
        old=old_actions[row["action_id"]]
        assert row["prior_status"]==old["status"]
        assert row["new_status"]=="OPEN - SIMULATED"
        assert row["signoff"]=="Not obtained"
        assert row["verification"] in ("Not independently verified","NOT TESTED")
        assert row["next_evidence_gate"] and row["evidence_type"]
    assert all(r["scenario_status"]=="SIMULATED - NOT REPORTED" for r in base.values())
    print("PASS v0.3: 6 unsubmitted mock communication records, 6 tabletop steps, 9 open follow-ups; zero tested recovery or approvals.")
    return True

if __name__=="__main__":
    validate_phase3()
