"""Behavioral checks for review provenance, scope, and legacy compatibility."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('handoff', ROOT / 'skills/cartoon-research-flowchart/scripts/validate_handoff.py')
handoff = importlib.util.module_from_spec(spec)
spec.loader.exec_module(handoff)


class HandoffReviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.package = Path(cls.temp.name) / 'figure'
        shutil.copytree(ROOT / 'examples/bradford', cls.package)
        cls.original = json.loads((cls.package / 'project.json').read_text())

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def sha(self, name):
        return hashlib.sha256((self.package / name).read_bytes()).hexdigest()

    def reviewed(self):
        p = copy.deepcopy(self.original)
        p.update(schema_version=2, style='cartoon', scope='full')
        p['frame']['mode'] = 'native'
        p['approved']['sha256'] = self.sha(p['approved']['file'])
        def record(file):
            return {'file': file, 'sha256': self.sha(file),
                    'fidelity': {'status': 'pass', 'observations': ['Compared the depicted objects and labels to the source.']},
                    'intrinsic': {'status': 'pass', 'observations': ['Inspected shape boundaries, perspective, and scientific relationships.']},
                    'issues': []}
        reference = record(p['approved']['file'])
        assets = []
        for asset in p['assets']:
            r = record(asset['file'])
            r.update(asset_id=asset['id'], reference_sha256=reference['sha256'])
            assets.append(r)
        p['visual_reviews'] = {'reference': reference, 'assets': assets}
        return p

    def check(self, p):
        path = self.package / 'test-project.json'
        path.write_text(json.dumps(p))
        return handoff.validate(path)

    def assert_rejected(self, p, hint):
        result = self.check(p)
        self.assertFalse(result['passed'], result)
        self.assertTrue(any(hint.lower() in e.lower() for e in result['errors']), result['errors'])

    def test_legacy_bradford_remains_valid(self):
        self.assertTrue(self.check(self.original)['passed'])

    def test_reviewed_v2_package_is_valid(self):
        self.assertTrue(self.check(self.reviewed())['passed'])

    def test_alpha_success_cannot_replace_visual_review(self):
        p = self.reviewed()
        del p['visual_reviews']
        self.assert_rejected(p, 'visual review')

    def test_matching_but_intrinsically_wrong_asset_is_rejected(self):
        p = self.reviewed()
        p['visual_reviews']['assets'][0]['intrinsic']['status'] = 'needs_revision'
        self.assert_rejected(p, 'intrinsic')

    def test_plausible_but_drifted_asset_is_rejected(self):
        p = self.reviewed()
        p['visual_reviews']['assets'][0]['fidelity']['status'] = 'needs_revision'
        self.assert_rejected(p, 'fidelity')

    def test_uncertain_source_figure_is_not_ready(self):
        p = self.reviewed()
        p['visual_reviews']['reference']['intrinsic']['status'] = 'uncertain'
        self.assert_rejected(p, 'intrinsic')

    def test_changed_asset_invalidates_old_review(self):
        p = self.reviewed()
        p['visual_reviews']['assets'][0]['sha256'] = '0' * 64
        self.assert_rejected(p, 'review hash')

    def test_review_against_another_reference_is_rejected(self):
        p = self.reviewed()
        p['visual_reviews']['assets'][0]['reference_sha256'] = '0' * 64
        self.assert_rejected(p, 'reference hash')

    def test_blanket_pass_without_observations_is_rejected(self):
        p = self.reviewed()
        p['visual_reviews']['assets'][0]['intrinsic']['observations'] = []
        self.assert_rejected(p, 'observations')

    def test_unresolved_blocker_cannot_be_overruled_by_pass_flags(self):
        p = self.reviewed()
        p['visual_reviews']['assets'][0]['issues'] = [{'severity': 'blocking', 'status': 'open', 'description': 'Impossible intersecting planes'}]
        self.assert_rejected(p, 'blocking')

    def test_asset_review_is_bound_to_exact_file(self):
        p = self.reviewed()
        p['visual_reviews']['assets'][0]['file'] = p['assets'][1]['file']
        self.assert_rejected(p, 'review file')

    def test_malformed_issue_cannot_bypass_review_gate(self):
        p = self.reviewed()
        p['visual_reviews']['assets'][0]['issues'] = ['blocking: open - impossible faces']
        self.assert_rejected(p, 'issue')

    def test_issue_with_unknown_severity_is_rejected(self):
        p = self.reviewed()
        p['visual_reviews']['assets'][0]['issues'] = [{'severity': 'other', 'status': 'open', 'description': 'Ambiguous construction'}]
        self.assert_rejected(p, 'issue')

    def test_sample_scope_needs_no_ppt_or_full_inventory(self):
        p = self.reviewed()
        p.update(scope='sample', stage='samples_ready', style='geometric')
        p.pop('frame')
        p.pop('native_elements')
        p.pop('coverage_review')
        p['occurrences'] = []
        p['assets'] = p['assets'][:2]
        p['visual_reviews']['assets'] = p['visual_reviews']['assets'][:2]
        p['delivery'] = {k: p['delivery'][k] for k in ['contact_sheet', 'prompts_index']}
        self.assertTrue(self.check(p)['passed'], self.check(p))

    def test_geometric_text_placement_frame_is_supported(self):
        p = self.reviewed()
        p['style'] = 'geometric'
        p['frame']['mode'] = 'text-placement'
        self.assertTrue(self.check(p)['passed'])


if __name__ == '__main__':
    unittest.main()
