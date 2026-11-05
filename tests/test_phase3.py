import sys
import unittest
from collections import Counter
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from validate_phase3 import validate_phase3,p3_load

class Phase3RegulatoryExerciseTests(unittest.TestCase):
    def test_all_cross_checks(self):
        self.assertTrue(validate_phase3())

    def test_no_real_regulatory_reports(self):
        self.assertTrue(all(r["actual_submission"]=="NONE - SIMULATED"
                            for r in p3_load("mock_communication_packets.csv")))

    def test_separate_gdpr_and_dora_packets(self):
        rows=p3_load("mock_communication_packets.csv")
        self.assertEqual(Counter(r["framework"] for r in rows),{"DORA":3,"GDPR":3})
        self.assertEqual(len([r for r in rows if r["packet_stage"]=="Authority notification"]),2)

    def test_no_false_restoration_assurance(self):
        rows=p3_load("resilience_tabletop.csv")
        self.assertEqual([r["result"] for r in rows if r["phase"]=="Service recovery"],["NOT TESTED"])

    def test_all_actions_stay_open_without_signoff(self):
        rows=p3_load("remediation_followup.csv")
        self.assertEqual(len(rows),9)
        self.assertTrue(all(r["signoff"]=="Not obtained" and
                            r["new_status"]=="OPEN - SIMULATED" for r in rows))

if __name__=="__main__":
    unittest.main()
