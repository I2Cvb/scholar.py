# -*- coding: utf-8 -*-

from .context import scholar

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_get_paper_reference(self):
        """Retrieve a single article written by Einstein on quantum theory:

            article author: albert einstein
            article phrase: quantum theory
        """

        querier = ScholarQuerier()
        settings = ScholarSettings()
        settings.set_citation_format(ScholarSettings.CITFORM_BIBTEX)

        # querier.apply_settings should be in an assert == ture. when false no internet
        querier.apply_settings(settings)
        query = SearchScholarQuery()
        query.set_author("albert einstein")
        query.set_phrase("quantum theory")
        query.set_num_page_results(1)

        querier.send_query(query)
        citation_export(querier)

if __name__ == '__main__':
    unittest.main()
