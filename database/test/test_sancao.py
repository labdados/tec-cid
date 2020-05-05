import sys
import os
from decouple import config
from py2neo import Graph

import unittest

from neo4j_utils import *
from assert_utils import *

neo4j_utils = Neo4jUtils()
assert_utils = AssertUtils()

class TestSancao():

    COUNT_INDEX = 0

    @classmethod
    def comparar_total_sancoes(self):
        query = "MATCH (s:Sancao) RETURN COUNT(s) AS total;"
        result = neo4j_utils.get_query_response(query)
        total_sancoes = result[self.COUNT_INDEX]['total']

        return total_sancoes != 0