import sys
import os
from decouple import config
from py2neo import Graph

import unittest

from neo4j_utils import Neo4jUtils
from assert_utils import *

from test_participante import *
from test_socio import *
from test_sancao import *

neo4j_utils = Neo4jUtils()
assert_utils = AssertUtils()

test_participante_empenhos = TestParticipanteEmpenhos()
test_socio = TestSocio()
test_sancao = TestSancao()

class TestEmpresa(unittest.TestCase):

    COUNT_INDEX = 0

    @classmethod
    def comparar_total_empresas(self):
        query = "MATCH (e:Empresa) RETURN COUNT(e.cnpj) AS total;"
        result = neo4j_utils.get_query_response(query)
        total_empresas = result[self.COUNT_INDEX]['total']

        return total_empresas != 0

    @classmethod
    def assert_empresas(self):
        total_empresas = self.comparar_total_empresas()

        if (not total_empresas): 
            raise unittest.SkipTest("O total de empresas não pode ser zero!")

    @classmethod
    def assert_empresas_e_participantes(self):
        self.assert_empresas()
        total_participantes = test_participante_empenhos.comparar_total_participantes()

        if (not total_participantes):
            raise unittest.SkipTest("O total de participantes não pode ser zero!")

    @classmethod
    def assert_empresas_e_socios(self):
        self.assert_empresas()
        total_socios = test_socio.comparar_total_socios()

        if (not total_socios):
            raise unittest.SkipTest("O total de sócios não pode ser zero!")

    @classmethod
    def assert_empresas_e_sancoes(self):
        self.assert_empresas()
        total_sancoes = test_sancao.comparar_total_sancoes()

        if (not total_sancoes):
            raise unittest.SkipTest("O total de sanções não pode ser zero!")
    
    def test_participacao_licitacao(self):
        self.assert_empresas_e_participantes()
        query = "MATCH x=(e:Empresa)-[:FOI]-(p:Participante) RETURN e.cnpj, p.cpf_cnpj;"
        atributoA = "e.cnpj"
        atributoB = "p.cpf_cnpj"

        assert_utils.test_assert_equal(neo4j_utils, query, atributoA, atributoB)

    def test_empresa_tem_socio(self):
        self.assert_empresas_e_socios()
        query = "MATCH x=(e:Empresa)-[:TEM_SOCIO]-(s:Socio) RETURN e.cnpj, s.cnpj_empresa;"
        atributoA = "e.cnpj"
        atributoB = "s.cnpj_empresa"

        assert_utils.test_assert_equal(neo4j_utils, query, atributoA, atributoB)

    def test_empresas_com_sancoes(self):
        self.assert_empresas_e_sancoes()
        query = "MATCH x=(e:Empresa)-[:TEM]-(s:Sancao) RETURN COUNT(x) AS total;"
        result = neo4j_utils.get_query_response(query)
        total = result[self.COUNT_INDEX]['total']

        self.assertTrue(total != 0)


if __name__ == "__main__":
    tests = unittest.TestLoader().loadTestsFromTestCase(TestEmpresa)
    unittest.TextTestRunner(verbosity=2).run(tests)