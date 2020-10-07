import unittest

class AssertUtils(unittest.TestCase):

    def test_assert_equal(self, neo4j_utils, query, attributeA, attributeB):
        results = neo4j_utils.get_query_response(query)

        for item in results:
            self.assertEqual(item[attributeA], item[attributeB])