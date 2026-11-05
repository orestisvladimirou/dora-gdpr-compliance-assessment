#!/usr/bin/env python3
"""Validate the portfolio dashboard and navigation without implying legal compliance."""
import re
from collections import Counter
from pathlib import Path
from urllib.parse import unquote

from validate_project import ROOT, records
from validate_phase2 import validate_phase2, p2_load
from validate_phase3 import validate_phase3, p3_load

def local_links():
    bad=[]
    pattern=re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    for p in ROOT.rglob("*.md"):
        if ".git" in p.parts or "__pycache__" in p.parts:
            continue
        for raw in pattern.findall(p.read_text(encoding="utf-8")):
            value=raw.strip().split(" ",1)[0].strip("<>")
            if not value or value.startswith(("https://","http://","mailto:","#")):
                continue
            loc=unquote(value.split("#",1)[0].split("?",1)[0])
            if loc and not (p.parent/loc).exists():
                bad.append(f"{p.relative_to(ROOT)} -> {loc}")
    assert not bad, "Broken documentation references:\n"+"\n".join(bad)
    return True

def validate_portfolio():
    validate_phase3()
    from csv import DictReader
    path=ROOT/"phase4/data/portfolio_metrics.csv"
    with path.open(newline="",encoding="utf-8") as f:
        metric_rows=list(DictReader(f))
    assert len(metric_rows)==len({r["metric_id"] for r in metric_rows})==20
    m={r["metric_id"]:r for r in metric_rows}
    assert set(m)=={"M"+str(n).zfill(2) for n in range(1,21)}

    incidents=records("data/incident_register.csv")
    obligations=records("data/regulatory_obligations.csv")
    arrangements=records("data/ict_arrangements.csv")
    evidence=records("data/evidence_register.csv")
    actions=records("data/remediation_tracker.csv")
    edge=p2_load("edge_case_decisions.csv")
    clocks=p2_load("timeline_exercises.csv")
    requests=p2_load("evidence_requests.csv")
    packets=p3_load("mock_communication_packets.csv")
    tabletop=p3_load("resilience_tabletop.csv")
    followup=p3_load("remediation_followup.csv")

    values={
        "M01":len(incidents),
        "M02":sum(x["dora_major_expected"]=="Yes" for x in incidents),
        "M03":sum(x["gdpr_authority_notification_expected"]=="Yes" for x in incidents),
        "M04":sum(x["gdpr_subject_communication_expected"]=="Yes" for x in incidents),
        "M05":sum(x["framework"]=="DORA" for x in obligations),
        "M06":sum(x["framework"]=="GDPR" for x in obligations),
        "M07":sum(x["status"]=="Gap" for x in obligations),
        "M08":sum(x["status"]=="Partial" for x in obligations),
        "M09":sum(x["status"]=="Not verified" for x in obligations),
        "M10":len(arrangements),"M11":len(evidence),
        "M12":sum(x["status"]=="Open - fictional" for x in actions),
        "M13":len(edge),"M14":len(clocks),"M15":len(requests),
        "M16":len(packets),"M17":len(tabletop),
        "M18":sum(x["new_status"]=="OPEN - SIMULATED" for x in followup),
        "M19":sum(x["actual_submission"]!="NONE - SIMULATED" for x in packets),
        "M20":sum(x["phase"]=="Service recovery" and x["result"]=="TESTED" for x in tabletop),
    }
    expected=[3,1,2,1,11,8,9,8,2,3,9,9,9,5,9,6,6,9,0,0]
    assert [values["M"+str(i).zfill(2)] for i in range(1,21)]==expected
    for key,count in values.items():
        assert int(m[key]["value"])==count,(key,m[key]["value"],count)
        assert (ROOT/m[key]["source_path"]).is_file(),key
        assert m[key]["indicator"] and m[key]["interpretation"]
    assert len(requests)==9 and all(r["confidence"]=="Not provided - simulation" for r in requests)
    assert all(p["actual_submission"]=="NONE - SIMULATED" and p["review_status"]=="DRAFT - SIMULATED" for p in packets)
    assert all(f["signoff"]=="Not obtained" for f in followup)
    assert len([t for t in tabletop if t["result"]=="NOT TESTED"])==1

    dashboard=(ROOT/"phase4/dashboard.md").read_text(encoding="utf-8")
    assert "NOT VERIFIED REGULATORY COMPLIANCE" in dashboard
    assert "Zero" in dashboard or "zero" in dashboard or "Zero" in dashboard.title()
    assert "Phase 1 has no actual submission" in dashboard
    assert "NOT TESTED" in dashboard
    local_links()
    print("PASS v0.4: 20 dashboard indicators match source, all documentation links resolve, zero actual reports, no recovery assurance.")
    return True

if __name__=="__main__":
    validate_portfolio()
