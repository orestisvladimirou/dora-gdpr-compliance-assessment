#!/usr/bin/env python3
"""Validate synthetic DORA/GDPR training records; not legal decision support."""
from pathlib import Path
from datetime import datetime, timedelta, timezone
from collections import Counter
import csv

ROOT=Path(__file__).resolve().parents[1]

def records(path):
    with (ROOT/path).open('r',encoding='utf-8',newline='') as f:
        return list(csv.DictReader(f))

def utc(value):
    if not value:
        return None
    dt=datetime.fromisoformat(value.replace('Z','+00:00'))
    assert dt.tzinfo is not None and dt.utcoffset() == timedelta(), 'Timestamp must be UTC'
    return dt

def fmt(dt):
    return dt.strftime('%Y-%m-%dT%H:%M:%SZ') if dt is not None else ''

def dora_major_simplified(r):
    # This intentionally uses selected thresholds and is NOT a full RTS classifier.
    # Only for fixed fictional examples. Missing criteria may change actual outcomes.
    if r['critical_service'] != 'Yes':
        return False
    client=int(float(r['client_impact_percent'])>10)
    outage=int(float(r['critical_service_outage_hours'])>2)
    geography=int(int(r['cross_border_member_states'])>=2)
    economic=int(float(r['economic_loss_eur'])>100000)
    special_access=(r['successful_malicious_access']=='Yes')
    return special_access or client+outage+geography+economic>=2

def dora_initial_deadline(r):
    if not dora_major_simplified(r):
        return None
    aware=utc(r['ict_aware_utc']);classified=utc(r['classification_utc'])
    assert classified>=aware
    # Art 5(2) exception for classification beyond 24h from awareness.
    if classified>aware+timedelta(hours=24):
        return classified+timedelta(hours=4)
    return min(classified+timedelta(hours=4),aware+timedelta(hours=24))

def gdpr_authority_expected(r):
    return r['personal_data_breach']=='Yes' and r['gdpr_risk_to_individuals']=='Yes'

def gdpr_subject_expected(r):
    return r['personal_data_breach']=='Yes' and r['gdpr_high_risk']=='Yes'

def gdpr_deadline(r):
    if not gdpr_authority_expected(r):
        return None
    return utc(r['gdpr_controller_aware_utc'])+timedelta(hours=72)

def require_unique(rows,key,num):
    vals=[x[key] for x in rows]
    assert len(vals)==len(set(vals))==num,(key,len(vals))
    return set(vals)

def validate():
    incidents=records('data/incident_register.csv')
    obligations=records('data/regulatory_obligations.csv')
    assets=records('data/services_and_assets.csv')
    contracts=records('data/ict_arrangements.csv')
    evidence=records('data/evidence_register.csv')
    actions=records('data/remediation_tracker.csv')
    timeline=records('data/reporting_clock_exercises.csv')
    ids=require_unique(incidents,'incident_id',3)
    obs=require_unique(obligations,'obligation_id',19)
    aids=require_unique(actions,'action_id',9)
    evid=require_unique(evidence,'evidence_id',9)
    require_unique(assets,'asset_id',4)
    require_unique(contracts,'arrangement_id',3)
    assert require_unique(timeline,'incident_id',3)==ids
    assert Counter(x['framework'] for x in obligations)=={'DORA':11,'GDPR':8}
    assert Counter(x['status'] for x in obligations)=={'Gap':9,'Partial':8,'Not verified':2}
    assert Counter(x['dora_major_expected'] for x in incidents)=={'Yes':1,'No':2}
    assert Counter(x['gdpr_authority_notification_expected'] for x in incidents)=={'Yes':2,'No':1}
    assert all(x['scenario_status']=='SIMULATED - NOT REPORTED' for x in incidents)
    for ev in evidence:
        if ev['file']:
            f=ROOT/ev['file'];assert f.is_file(),f
            c=f.read_text(encoding='utf-8').upper()
            assert 'SYNTHETIC' in c and 'FICTIONAL' in c
        else:
            assert ev['assurance_level']=='Missing'
        assert ev['limitations']
    for a in actions:
        assert a['status']=='Open - fictional'
        for ref in a['obligation_refs'].split(';'):
            assert ref in obs,(a['action_id'],ref)
        assert a['acceptance_evidence'] and a['recommended_action']
        assert datetime.fromisoformat(a['target_scenario_date']).date()>datetime(2026,11,5).date()
    for ob in obligations:
        assert ob['evidence_id'] in evid
        assert ob['action_id'] in aids
        assert ob['status'] in ('Gap','Partial','Not verified')
        assert ob['primary_source_url'].startswith('https://eur-lex.europa.eu/')
        assert ob['scope_assumption'] and ob['accountable_role']
    for c in contracts:
        assert c['action_id'] in aids
        assert c['roi_template_status']=='Not official ITS-complete'
        assert c['gdpr_processor_agreement_status']
    by_t={x['incident_id']:x for x in timeline}
    for inc in incidents:
        assert utc(inc['ict_aware_utc']) and utc(inc['classification_utc'])>=utc(inc['ict_aware_utc'])
        assert utc(inc['ict_aware_utc']).date()==datetime.fromisoformat(inc['scenario_date']).date()
        assert inc['dora_major_expected']==('Yes' if dora_major_simplified(inc) else 'No')
        assert inc['gdpr_authority_notification_expected']==('Yes' if gdpr_authority_expected(inc) else 'No')
        assert inc['gdpr_subject_communication_expected']==('Yes' if gdpr_subject_expected(inc) else 'No')
        if inc['personal_data_breach']=='Yes':
            assert utc(inc['gdpr_controller_aware_utc'])
        else:
            assert not inc['gdpr_controller_aware_utc']
        clock=by_t[inc['incident_id']]
        assert clock['dora_initial_deadline_utc']==fmt(dora_initial_deadline(inc))
        assert clock['gdpr_authority_planning_deadline_utc']==fmt(gdpr_deadline(inc))
        assert clock['actual_dora_submission']=='NONE - SIMULATED'
        assert clock['actual_gdpr_submission']=='NONE - SIMULATED'
        if dora_major_simplified(inc):
            assert clock['dora_intermediate_deadline_utc']=='UNKNOWN - AWAIT SUBMISSION'
            assert clock['dora_final_deadline_utc']=='UNKNOWN - AWAIT INTERMEDIATE'
        else:
            assert not clock['dora_intermediate_deadline_utc'] and not clock['dora_final_deadline_utc']
    assert (by_t['INC-001']['dora_initial_deadline_utc'],by_t['INC-001']['gdpr_authority_planning_deadline_utc'])==('2026-12-10T15:00:00Z','2026-12-13T10:45:00Z')
    assert by_t['INC-003']['gdpr_authority_planning_deadline_utc']=='2026-12-15T13:30:00Z'
    print('PASS v0.1: 3 scenarios, 19 mapped obligations, 9 evidence refs, 9 open actions; separate DORA/GDPR clocks; zero actual reports.')
    return True

if __name__=='__main__':
    validate()
