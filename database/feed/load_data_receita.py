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
        'index_empresa_cnpj.cypher',
        'index_socio.cypher',
        'nodes_empresas.cypher',
        'nodes_socios.cypher',
        'rel_empresa_foi_participante.cypher',
        'rel_empresa_tem_socio.cypher',
        'export_doacoes_socios_com_nomes_distintos.cypher',
        'rel_doacoes_socios_com_nomes_iguais.cypher',
        'rel_doacoes_socios_com_nomes_distintos.cypher'
    ]
    
    for cypher_file in cypher_files:
        query_from_file(neo4j, PREFIX + cypher_file)