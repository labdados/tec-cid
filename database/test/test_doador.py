import unittest

from neo4j_utils import Neo4jUtils
from assert_utils import AssertUtils
from test_candidato import TestCandidato

neo4j_utils = Neo4jUtils()
assert_utils = AssertUtils()
test_candidatos = TestCandidato()

class TestDoador(unittest.TestCase):

    COUNT_INDEX = 0

    def comparar_total_doadores(self):
        query = "MATCH (d:Doador) RETURN COUNT(d.cpf_cnpj) AS total"
        result = neo4j_utils.get_query_response(query)
        total_doadores = result[self.COUNT_INDEX]['total']

        return total_doadores != 0
    
    def assert_total_doadores_e_candidatos(self):
        total_candidatos = test_candidatos.comparar_total_candidatos()
        total_doadores = self.comparar_total_doadores()

        if (not total_candidatos):
            raise unittest.SkipTest("O total de candidatos de 2016 não é 11639.")

        if (not total_doadores):
            raise unittest.SkipTest("O total de doadores não pode ser zero!")


    def test_doadores_que_nao_doaram_para_candidatos(self):
        self.assert_total_doadores_e_candidatos()

        query = "MATCH (d:Doador) WHERE NOT (:Doador)-[:DOOU_PARA]-(:Candidato) RETURN COUNT(d) AS total;"
        result = neo4j_utils.get_query_response(query)
        total = result[self.COUNT_INDEX]['total']

        self.assertTrue(total == 0)


if __name__ == "__main__":
    test = unittest.TestLoader().loadTestsFromTestCase(TestDoador)
    unittest.TextTestRunner(verbosity=2).run(test)