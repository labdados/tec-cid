import sys
from decouple import config
from etl_utils import query_from_file
from py2neo import Graph

import traceback
import datetime

PREFIX = 'cypher/'

def get_time():
    now = datetime.datetime.now()
    hours = now.hour
    minutes = now.minute
    seconds = now.second

    return '{}h:{}m:{}s'.format(hours, minutes, seconds)

if __name__ == '__main__':
    start_time = '[START TIME load_data_tce]: ' + get_time()
    
    user = sys.argv[1] if len(sys.argv) > 1 else config('NEO4J_USER', default='neo4j')
    password = sys.argv[2] if len(sys.argv) > 2 else config('NEO4J_PASSWORD', default='password')
    
    neo4j = Graph("localhost", user=user, password=password)
    cypher_files = [
        'index_unidade_gestora.cypher',
        'index_municipio.cypher',
        'index_municipio_nome.cypher',
        'index_licitacao.cypher',
        'index_participante.cypher',
        'index_empenho.cypher',
        'index_empenho_uorcamentaria.cypher',

        #'index_pagamento_id_empenho.cypher',
        #'index_pagamento_valor.cypher',
        #'index_pagamento_data.cypher',
        #'index_pagamento_ugestora.cypher',

        'rel_licitacoes_propostas.cypher',
        'nodes_municipios.cypher',
        'nodes_empenhos.cypher',
        'nodes_participantes.cypher',
        'rel_gerou_empenho.cypher',
        'rel_empenhado_para.cypher'

        #'deleta_rel_gerou_pagamento.cypher',
        #'deleta_pagamentos.cypher',
        #'nodes_pagamentos.cypher',
        #'rel_gerou_pagamento.cypher'
    ]

    try:
        for cypher_file in cypher_files:
            query_from_file(neo4j, PREFIX + cypher_file)

    finally:
        finish_time = '[FINISH TIME load_data_tce]: ' + get_time()

        print(start_time)
        print(finish_time)