import sys
import os
from decouple import config
from py2neo import Graph

import unittest

from neo4j_utils import Neo4jUtils
from assert_utils import *

neo4j_utils = Neo4jUtils()
assert_utils = AssertUtils()


class TestUnidadeGestora(unittest.TestCase):

    COUNT_INDEX = 0

    @classmethod
    def comparar_total_unidades_gestoras(self):
        query = "MATCH (ug:UnidadeGestora) RETURN COUNT(ug.cd_ugestora) AS total;"
        results = neo4j_utils.get_query_response(query)
        total_unidades = results[self.COUNT_INDEX]['total']

        return total_unidades > 0

    @classmethod
    def assert_total_unidades_gestoras(self):
        total_unidades = self.comparar_total_unidades_gestoras()

        if (not total_unidades):
            raise unittest.SkipTest("O total de Unidades Gestoras não é 627")

    def test_unidade_gestora_pertence_a_municipio(self):
        self.assert_total_unidades_gestoras()

        query = "MATCH x=(ug:UnidadeGestora)-[:PERTENCE_A]-(m:Municipio) RETURN ug.municipio, m.nome;"
        atributoA = "ug.municipio"
        atributoB = "m.nome"

        assert_utils.test_assert_equal(neo4j_utils, query, atributoA, atributoB)


if __name__ == "__main__":
    test = unittest.TestLoader().loadTestsFromTestCase(TestUnidadeGestora)
    unittest.TextTestRunner(verbosity=2).run(test)