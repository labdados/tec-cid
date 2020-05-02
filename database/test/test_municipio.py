import sys
import os
from decouple import config
from py2neo import Graph

from neo4j_utils import *

neo4j_utils = Neo4jUtils()

class TestMunicipio():

    COUNT_INDEX = 0
    TOTAL_MUNICIPIOS_PB = 223

    def comparar_total_municipios(self):
        query = "MATCH (m:Municipio) RETURN COUNT(m.id) AS total"
        results = neo4j_utils.get_query_response(query)
        total_municipios = results[self.COUNT_INDEX]['total']

        return total_municipios == self.TOTAL_MUNICIPIOS_PB