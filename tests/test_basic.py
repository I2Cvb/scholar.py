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

    def test_get_cluster(self):
        """Retrieve the articles that reference Albert Einstein's quantum theory paper:
        """
       cluster-id=8174092782678430881
       # siktodo

    def test_get_library(self):
        """Retrieve the articles from a library id:
        """
       # siktodo
       # library url example https://scholar.google.fr/scholar?scilib=1024&hl=en&as_sdt=0,5

if __name__ == '__main__':
    unittest.main()
