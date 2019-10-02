from etl_utils import query_from_file
from py2neo import Graph

if __name__ == '__main__':
    neo4j = Graph("localhost", user="neo4j", password="password")
    cypher_files = [
        'cria_index_candidato.cypher',
        'cria_index_partido.cypher',
        'carrega_candidatos.cypher',
        'carrega_doacoes_candidatos.cypher']
    
    for cypher_file in cypher_files:
        query_from_file(neo4j, cypher_file)