import sys
import os
from decouple import config
from py2neo import Graph

import unittest

from neo4j_utils import *
from assert_utils import *
from test_municipio import *

neo4j_utils = Neo4jUtils()
assert_utils = AssertUtils()
test_municipio = TestMunicipio()


class TestCandidato(unittest.TestCase):

    COUNT_INDEX = 0
    TOTAL_CANDIDATOS_2016 = 11639

    @classmethod
    def comparar_total_candidatos(self):
        query = "MATCH (c:Candidato) RETURN COUNT(c) AS total;"
        results = neo4j_utils.get_query_response(query)
        total_candidatos = results[self.COUNT_INDEX]['total']

        return total_candidatos == self.TOTAL_CANDIDATOS_2016

    @classmethod
    def assert_candidatos_e_municipios(self):
        total_candidatos = self.comparar_total_candidatos()
        total_municipios = test_municipio.comparar_total_municipios()

        if (not total_candidatos):
            raise unittest.SkipTest("O total de candidatos não é 11639.")

        if (not total_municipios):
            raise unittest.SkipTest("O total de municípios não é 223.")

    def test_nome_municipio_governado(self):
        self.assert_candidatos_e_municipios()

        query = "MATCH x=(c:Candidato)-[:GOVERNA]-(m:Municipio) RETURN c.municipio, m.nome;"
        atributoA = "c.municipio"
        atributoB = "m.nome"

        assert_utils.test_assert_equal(neo4j_utils, query, atributoA, atributoB)


if __name__ == "__main__":
    test = unittest.TestLoader().loadTestsFromTestCase(TestCandidato)
    unittest.TextTestRunner(verbosity=2).run(test)