import sys
import unittest
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from validate_phase2 import validate_phase2,p2_load,major_case,plus_calendar_month
from validate_project import utc

class FollowupScenarioTests(unittest.TestCase):
    def test_all_phase2_consistency(self):
        self.assertTrue(validate_phase2())

    def test_special_dora_access_pathway(self):
        cases={x["case_id"]:x for x in p2_load("edge_case_decisions.csv")}
        self.assertEqual(major_case(cases["EDGE-202"]),"Major (scenario)")
        self.assertEqual(major_case(cases["EDGE-205"]),"Requires recurring-incident review")
        self.assertEqual(major_case(cases["EDGE-203"]),"Not major on supplied facts")

    def test_independent_gdpr_notification(self):
        cases={x["case_id"]:x for x in p2_load("edge_case_decisions.csv")}
        self.assertEqual(cases["EDGE-206"]["dora_result"],"Not major on supplied facts")
        self.assertEqual(cases["EDGE-206"]["gdpr_authority"],"Yes")
        self.assertEqual(cases["EDGE-208"]["gdpr_authority"],"No")
        self.assertEqual(cases["EDGE-207"]["gdpr_individuals"],"Yes")

    def test_24h_cap_and_late_classification_rule(self):
        t={x["exercise_id"]:x for x in p2_load("timeline_exercises.csv")}
        self.assertEqual(t["CLK-202"]["calculated_dora_initial_due_utc"],"2026-12-11T16:00:00Z")
        self.assertEqual(t["CLK-203"]["calculated_dora_initial_due_utc"],"2026-12-11T09:00:00Z")

    def test_calendar_month_not_thirty_days(self):
        self.assertEqual(plus_calendar_month(utc("2027-01-31T14:00:00Z")).strftime("%Y-%m-%dT%H:%M:%SZ"),"2027-02-28T14:00:00Z")

    def test_no_notification_is_marked_as_actually_sent(self):
        rows=p2_load("timeline_exercises.csv")
        self.assertTrue(all(x["real_submission_status"]=="NONE - TRAINING" for x in rows))
        self.assertEqual(len(rows),5)

    def test_processor_and_controller_have_separate_awareness(self):
        t={x["exercise_id"]:x for x in p2_load("timeline_exercises.csv")}
        self.assertEqual(t["CLK-205"]["processor_awareness_utc"],"2026-12-10T06:00:00Z")
        self.assertEqual(t["CLK-205"]["controller_breach_awareness_utc"],"2026-12-10T10:00:00Z")
        self.assertEqual(t["CLK-205"]["calculated_gdpr_authority_due_utc"],"2026-12-13T10:00:00Z")

if __name__=="__main__":
    unittest.main()
