import unittest

import json

from wrappers.report.ReportWrapper import ReportWrapper


example_reports_dir_path = 'wrappers/report/example_reports/'

example_reports = {}

with open(example_reports_dir_path + 'unkeyed.json', 'r') as f:
    example_reports['unkeyed'] = json.loads(f.read())

with open(example_reports_dir_path + 'keyed.json', 'r') as f:
    example_reports['keyed'] = json.loads(f.read())


class TestWrappeeProperty(unittest.TestCase):
    def test_unkeyed(self):
        wrappee = example_reports['unkeyed']
        report = ReportWrapper(wrappee)
        self.assertIs(report.wrappee, wrappee)

    def test_keyed(self):
        wrappee = example_reports['keyed']
        report = ReportWrapper(wrappee)
        self.assertIs(report.wrappee, wrappee['report'])


class TestResultsGetter(unittest.TestCase):
    def test_unkeyed(self):
        report = ReportWrapper(example_reports['unkeyed'])
        results = report.results
        # just check one results value
        self.assertEqual(results.search.hits[0].hsps[0].hit_from, 1250)

    def test_keyed(self):
        report = ReportWrapper(example_reports['keyed'])
        results = report.results
        # just check one results value
        self.assertEqual(results.search.hits[0].hsps[0].query_to, 195)
