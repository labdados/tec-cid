import sys
import os

import csv

from decouple import config
from py2neo import Graph

import unittest
from neo4j_utils import *

neo4j_utils = Neo4jUtils()


FILE_NAME = '../../dados/empenhos.csv'
CPF_CNPJ_INDEX = 20

class TestParticipanteEmpenhos(unittest.TestCase):

    COUNT_INDEX = 0

    def get_total_participantes(self):
        query = "MATCH (p:Participante) RETURN COUNT(p.cpf_cnpj) AS total"
        result = neo4j_utils.get_query_response(query)
        total_participantes = result[self.COUNT_INDEX]['total']

        return total_participantes

    def comparar_total_participantes(self):
        return self.get_total_participantes() != 0

    def print_warning_message(self, incorrects_cpf_cnpj):
        if (len(incorrects_cpf_cnpj) > 0):
            print("\n[WARNING]: {} CPF(s) / CNPJ(s) não possuía (possuiam) 11 ou 14 caracteres e foram deletados!\n".format(len(incorrects_cpf_cnpj)))
            
            for number, element in enumerate(incorrects_cpf_cnpj):
                print('{}º CPF/CNPJ: {} ({} caracteres)'.format(number+1, element, len(element)))

    def test_total_cpf_cnpj_empenhos_csv(self):
        incorrect_cpf_cnpj = []

        try:
            with open(FILE_NAME, 'r') as csv_file:
                csv_data = csv.reader(csv_file, delimiter=",")
                next(csv_data)

                for row in csv_data:
                    if (len(row[CPF_CNPJ_INDEX]) == 14 or len(row[CPF_CNPJ_INDEX]) == 11):
                        pass

                    else:
                        incorrect_cpf_cnpj.append(row[CPF_CNPJ_INDEX])
  
        except OSError as error:
            print(error)

        self.print_warning_message(incorrect_cpf_cnpj)
        self.assertEqual(len(incorrect_cpf_cnpj), 1)

if __name__ == "__main__":
    tests = unittest.TestLoader().loadTestsFromTestCase(TestParticipanteEmpenhos)
    unittest.TextTestRunner(verbosity=2).run(tests)