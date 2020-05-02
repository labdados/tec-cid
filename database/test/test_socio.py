import sys
import os
from decouple import config
from py2neo import Graph

import unittest

from neo4j_utils import *
from assert_utils import *
from test_doador import *


neo4j_utils = Neo4jUtils()
assert_utils = AssertUtils()
test_doador = TestDoador()

class TestSocio(unittest.TestCase):

    COUNT_INDEX = 0

    @classmethod
    def comparar_total_socios(self):
        query = "MATCH (s:Socio) RETURN COUNT(s.cpf_cnpj) AS total;"
        result = neo4j_utils.get_query_response(query)
        total_socios = result[self.COUNT_INDEX]['total']

        return total_socios != 0

    @classmethod
    def assert_socios_e_doadores(self):
        total_socios = self.comparar_total_socios()
        total_doadores = test_doador.comparar_total_doadores()

        if (not total_socios):
            raise unittest.SkipTest("O total de sócios não pode ser zero!")

        if (not total_doadores):
            raise unittest.SkipTest("O total de doadores não pode ser zero!")

    def test_quantidade_de_socios_doadores(self):
        self.assert_socios_e_doadores()

        query = "MATCH x=(s:Socio)-[:FOI]-(d:Doador) RETURN COUNT(x) as total;"
        result = neo4j_utils.get_query_response(query)
        total_relacionamentos = result[self.COUNT_INDEX]['total']

        self.assertTrue(total_relacionamentos > 0)

    def test_socio_foi_doador(self):
        self.assert_socios_e_doadores()

        query = "MATCH x=(s:Socio)-[:FOI]-(d:Doador) RETURN s.cpf_cnpj, d.cpf_cnpj;"
        atributoA = "s.cpf_cnpj"
        atributoB = "d.cpf_cnpj"

        assert_utils.test_assert_equal(neo4j_utils, query, atributoA, atributoB)


if __name__ == "__main__":
    test = unittest.TestLoader().loadTestsFromTestCase(TestSocio)
    unittest.TextTestRunner(verbosity=2).run(test)