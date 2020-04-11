import sys
import os
from decouple import config
from py2neo import Graph

from neo4j_utils import *

neo4j_utils = Neo4jUtils()
class TestDoador():

    COUNT_INDEX = 0

    def comparar_total_doadores(self):
        query = "MATCH (d:Doador) RETURN COUNT(d.cpf_cnpj) AS total"
        result = neo4j_utils.get_query_response(query)
        total_doadores = result[self.COUNT_INDEX]['total']

        return total_doadores != 0