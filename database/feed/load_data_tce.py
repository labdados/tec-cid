import sys
from decouple import config
from etl_utils import query_from_file
from py2neo import Graph

import traceback
import datetime

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
        'cria_index_unidade_gestora.cypher',
        'cria_index_municipio.cypher',
        'cria_index_municipio_nome.cypher',
        'cria_index_licitacao.cypher',
        'cria_index_participante.cypher',
        'cria_index_empenho.cypher',
        'cria_index_empenho_uorcamentaria.cypher',

        #'cria_index_pagamento_id_empenho.cypher',
        #'cria_index_pagamento_valor.cypher',
        #'cria_index_pagamento_data.cypher',
        #'cria_index_pagamento_ugestora.cypher',

        'carrega_licitacoes_propostas.cypher',
        'carrega_municipios.cypher',
        'carrega_nodes_empenhos.cypher',
        'carrega_nodes_participantes.cypher',
        'cria_rel_gerou_empenho.cypher',
        'cria_rel_empenhado_para.cypher'

        #'deleta_rel_gerou_pagamento.cypher',
        #'deleta_pagamentos.cypher',
        #'carrega_nodes_pagamentos.cypher',
        #'cria_rel_gerou_pagamento.cypher'
    ]

    try:
        for cypher_file in cypher_files:
            query_from_file(neo4j, cypher_file)

    except Exception as exception:
        print(exception)
        print(traceback.format_exc())

    finally:
        finish_time = '[FINISH TIME load_data_tce]: ' + get_time()

        print(start_time)
        print(finish_time)