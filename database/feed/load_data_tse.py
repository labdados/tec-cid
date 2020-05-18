import sys
from decouple import config
from etl_utils import query_from_file
from py2neo import Graph

PREFIX = 'cypher/'

if __name__ == '__main__':
    user = sys.argv[1] if len(sys.argv) > 1 else config('NEO4J_USER', default='neo4j')
    password = sys.argv[2] if len(sys.argv) > 2 else config('NEO4J_PASSWORD', default='password')
    
    neo4j = Graph("localhost", user=user, password=password)
    cypher_files = [
        'index_candidato.cypher',
        'index_partido.cypher',
        'index_doador.cypher',
        'index_fulltext_doador.cypher',
        'index_pessoa.cypher',
        'nodes_candidatos.cypher',
        'nodes_doador.cypher',
        'rel_doacoes_candidatos.cypher',
        'rel_pessoa_foi_participante.cypher',
        'rel_pessoa_foi_doador.cypher',
        'rel_pessoa_foi_candidato.cypher',
    ]
    
    for cypher_file in cypher_files:
        query_from_file(neo4j, PREFIX + cypher_file)
