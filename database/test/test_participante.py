import sys
import os
from decouple import config
from py2neo import Graph

from neo4j_utils import *

neo4j_utils = Neo4jUtils()

class TestParticipante():

    COUNT_INDEX = 0

    def comparar_total_participantes(self):
        query = "MATCH (p:Participante) RETURN COUNT(p.cpf_cnpj) AS total"
        result = neo4j_utils.get_query_response(query)
        total_participantes = result[self.COUNT_INDEX]['total']

        return total_participantes != 0