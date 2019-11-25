import sys
from decouple import config
from etl_utils import query_from_file
from py2neo import Graph

if __name__ == '__main__':
    user = sys.argv[1] if len(sys.argv) > 1 else config('NEO4J_USER', default='neo4j')
    password = sys.argv[2] if len(sys.argv) > 2 else config('NEO4J_PASSWORD', default='password')
    
    neo4j = Graph("localhost", user=user, password=password)
    cypher_files = [
        'cria_index_unidade_gestora.cypher',
        'cria_index_municipio.cypher',
        'cria_index_municipio_nome.cypher',
        'cria_index_licitacao.cypher',
        'cria_index_participante.cypher',
        'cria_index_empenho.cypher',
        'cria_index_valor_pagamento.cypher',
        'cria_index_id_empenho_pagamento.cypher',
        ##'cria_index_empenho_uorcamentaria.cypher',
        ##'cria_index_credor.cypher',
        'carrega_licitacoes_propostas.cypher',
        'carrega_municipios.cypher',
        'carrega_nodes_empenhos.cypher',
        'cria_rel_gerou_empenho.cypher',
        'cria_rel_empenhado_para.cypher',
        'carrega_nodes_pagamentos.cypher',
        'cria_rel_gerou_pagamento.cypher'
    ]
    
    for cypher_file in cypher_files:
        query_from_file(neo4j, cypher_file)