import sys
import unittest
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from validate_portfolio import validate_portfolio,local_links

class PortfolioQualityTests(unittest.TestCase):
    def test_integrated_dashboard(self):
        self.assertTrue(validate_portfolio())

    def test_document_navigation(self):
        self.assertTrue(local_links())

    def test_no_real_certification_claims_in_dashboard(self):
        text=(Path(__file__).resolve().parents[1]/"phase4/dashboard.md").read_text(encoding="utf-8")
        self.assertIn("NOT VERIFIED REGULATORY COMPLIANCE",text)
        self.assertIn("NOT TESTED",text)

    def test_portfolio_has_no_actual_submission(self):
        from validate_phase3 import p3_load
        self.assertTrue(all(x["actual_submission"]=="NONE - SIMULATED" for x in p3_load("mock_communication_packets.csv")))

if __name__=="__main__":
    unittest.main()
