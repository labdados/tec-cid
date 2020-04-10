import sys
from decouple import config
from etl_utils import query_from_file
from py2neo import Graph

if __name__ == '__main__':
    user = sys.argv[1] if len(sys.argv) > 1 else config('NEO4J_USER', default='neo4j')
    password = sys.argv[2] if len(sys.argv) > 2 else config('NEO4J_PASSWORD', default='password')
    
    neo4j = Graph("localhost", user=user, password=password)
    cypher_files = [
        'cria_index_empresa_cnpj.cypher',
        'cria_index_socio.cypher',
        'carrega_nodes_empresas.cypher',
        'carrega_nodes_socios.cypher',
        'cria_rel_empresa_foi_participante.cypher',
        'cria_rel_empresa_tem_socio.cypher',
        'carrega_doacoes_socios.cypher'
    ]
    
    for cypher_file in cypher_files:
        query_from_file(neo4j, cypher_file)