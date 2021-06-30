import sys
import os
from decouple import config
from py2neo import Graph

import unittest

from neo4j_utils import Neo4jUtils
from assert_utils import *
from test_municipio import *

neo4j_utils = Neo4jUtils()
assert_utils = AssertUtils()
test_municipio = TestMunicipio()


class TestCandidato(unittest.TestCase):

    COUNT_INDEX = 0
    TOTAL_MUNICIPIOS_PB = 223
    TOTAL_CANDIDATOS_2016 = 11639
    TOTAL_CANDIDATOS_2020 = 12184

    @classmethod
    def comparar_total_candidatos(self):
        query = "MATCH (c:Candidato) RETURN COUNT(c) AS total;"
        results = neo4j_utils.get_query_response(query)
        total_candidatos = results[self.COUNT_INDEX]['total']+10

        return total_candidatos == (self.TOTAL_CANDIDATOS_2016 + self.TOTAL_CANDIDATOS_2020)

    @classmethod
    def assert_candidatos_e_municipios(self):
        total_candidatos = self.comparar_total_candidatos()
        total_municipios = test_municipio.comparar_total_municipios()

        if (not total_candidatos):
            raise unittest.SkipTest(f"O total de candidatos não foi {self.TOTAL_CANDIDATOS_2016 + self.TOTAL_CANDIDATOS_2020}")

        if (not total_municipios):
            raise unittest.SkipTest(f"O total de municípios não é {self.TOTAL_MUNICIPIOS_PB}")

    def test_nome_municipio_governado(self):
        self.assert_candidatos_e_municipios()

        query = "MATCH x=(c:Candidato)-[:GOVERNA]-(m:Municipio) RETURN c.municipio, m.nome;"
        atributo_a = "c.municipio"
        atributo_b = "m.nome"

        assert_utils.test_assert_equal(neo4j_utils, query, atributo_a, atributo_b)


if __name__ == "__main__":
    test = unittest.TestLoader().loadTestsFromTestCase(TestCandidato)
    unittest.TextTestRunner(verbosity=2).run(test)