from py2neo import Graph

def query_from_file(neo4j, cypher_file):
    with open(cypher_file) as f:
        query = f.read().rstrip("\n")
        print(query)
        return neo4j.evaluate(query)

if __name__ == '__main__':
    neo4j = Graph("localhost", user="neo4j", password="password")
    cypher_files = [
        'cria_index_unidade_gestora.cypher',
        'cria_index_municipio.cypher',
        'cria_index_municipio_nome.cypher',
        'cria_index_licitacao.cypher',
        'cria_index_participante.cypher',
        'carrega_licitacoes_propostas.cypher',
        'carrega_municipio.cypher'
    ]
    
    for cypher_file in cypher_files:
        query_from_file(neo4j, cypher_file)