import sys
from decouple import config
from etl_utils import query_from_file
from py2neo import Graph

if __name__ == '__main__':
    user = 'neo4j'
    password = 'password'
    
    neo4j = Graph("localhost", user=user, password=password)
    cypher_files = [
        'cria_index_unidade_gestora.cypher',
        'cria_index_municipio.cypher',
        'cria_index_municipio_nome.cypher',
        'cria_index_licitacao.cypher',
        'cria_index_participante.cypher',
        'cria_index_empenho.cypher',
        #'cria_index_empenho_uorcamentaria.cypher',
        #'cria_index_credor.cypher',
        'carrega_licitacoes_propostas.cypher',
        'carrega_municipios.cypher',
        'carrega_nodes_empenhos.cypher',
        'cria_rel_gerou_empenho.cypher',
        'cria_rel_empenhado_para.cypher'
        #'carrega_pagamentos.cypher'
    ]
    
    for cypher_file in cypher_files:
        query_from_file(neo4j, cypher_file)