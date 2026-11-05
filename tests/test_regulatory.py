import unittest,sys
from pathlib import Path
from datetime import timedelta
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from validate_project import validate,records,utc,dora_major_simplified,dora_initial_deadline,gdpr_deadline,gdpr_authority_expected,gdpr_subject_expected

class FictionalComplianceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data={r['incident_id']:r for r in records('data/incident_register.csv')}

    def test_all_records(self):
        self.assertTrue(validate())

    def test_major_ict_plus_personal_data(self):
        r=self.data['INC-001']
        self.assertTrue(dora_major_simplified(r))
        self.assertTrue(gdpr_authority_expected(r))
        self.assertTrue(gdpr_subject_expected(r))

    def test_minor_ict_not_assumed_breach(self):
        r=self.data['INC-002']
        self.assertFalse(dora_major_simplified(r))
        self.assertFalse(gdpr_authority_expected(r))
        self.assertIsNone(dora_initial_deadline(r))
        self.assertIsNone(gdpr_deadline(r))

    def test_privacy_breach_separate_from_dora(self):
        r=self.data['INC-003']
        self.assertFalse(dora_major_simplified(r))
        self.assertTrue(gdpr_authority_expected(r))
        self.assertFalse(gdpr_subject_expected(r))

    def test_different_awareness_clocks(self):
        r=self.data['INC-001']
        self.assertNotEqual(r['ict_aware_utc'],r['gdpr_controller_aware_utc'])
        self.assertEqual((dora_initial_deadline(r)-utc(r['classification_utc'])),timedelta(hours=4))
        self.assertEqual((gdpr_deadline(r)-utc(r['gdpr_controller_aware_utc'])),timedelta(hours=72))

    def test_late_major_classification_exception(self):
        r=dict(self.data['INC-001'],classification_utc='2026-12-11T12:00:00Z')
        self.assertEqual(dora_initial_deadline(r)-utc(r['classification_utc']),timedelta(hours=4))

    def test_dont_confuse_status_with_sent_notification(self):
        rows=records('data/reporting_clock_exercises.csv')
        self.assertEqual(len(rows),3)
        self.assertTrue(all(x['actual_dora_submission']=='NONE - SIMULATED' for x in rows))
        self.assertTrue(all(x['actual_gdpr_submission']=='NONE - SIMULATED' for x in rows))

if __name__=='__main__':unittest.main()
