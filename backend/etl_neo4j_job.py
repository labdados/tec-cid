import bonobo
import csv
import gzip
import logging
from neo4j import GraphDatabase
import requests
import time
from bonobo.config import use
from models import Licitacao2
from io import TextIOWrapper
from py2neo import Node, Relationship, Graph, Subgraph



def download_licitacao():
    url = 'https://dados.tce.pb.gov.br/TCE-PB-SAGRES-Licitacao_Esfera_Municipal.txt.gz'
    filename = 'dados/licitacao.txt.gz'

    r = requests.get(url)
    
    with open(filename, 'wb') as f:
        f.write(r.content)

    return filename


def transform_licitacao(filename):
    with TextIOWrapper(gzip.open(filename), newline='\n') as text_file:
        header = text_file.readline().rstrip().split('|')
        for row in text_file:
            licitacao = row.rstrip().replace('\r', '').split('|')
            assert len(licitacao) == 10
            #yield tulicitacao)
            yield dict(zip(header, licitacao))

def write_licitacao_csv(rows):
    csv.wri
    
@use('neo4j_driver')
def load_licitacao_neo4j(*licitacoes, neo4j_driver):
    label = "Licitacao2"
    primary_key = 'uuid'
    #tx = neo4j.begin()
    with neo4j_driver.session() as session:
        tx = session.begin_transaction()
        statement = "MERGE (l:Licitacao {\
            uuid:{uuid}, cd_ugestora:{cd_ugestora}, de_Obs:{de_Obs},\
            de_TipoLicitacao:{de_TipoLicitacao},de_TipoObjeto:{de_TipoObjeto},\
            de_ugestora:{de_ugestora}, dt_Homologacao:{dt_Homologacao},\
            nu_Licitacao:{nu_Licitacao}, tp_Licitacao:{tp_Licitacao},\
            tp_Objeto:{tp_Objeto}, vl_Licitacao:{vl_Licitacao}})"
            
        for lic in licitacoes:
            if lic:
                lic['uuid'] = '-'.join((lic['cd_ugestora'], lic['tp_Licitacao'], lic['nu_Licitacao']))
                lic_node = Node(label, **lic)
                #lic_obj = Licitacao2.wrap(lic_node)
                tx.run(statement, **lic)
                #tx.merge(lic_node, label, primary_key)
                #tx.process()
            else:
                break
            #lic_obj = Licitacao2.wrap(lic_node)
            #tx.merge(lic_node)
            #tx.process()
            #neo4j.merge(lic_node)
        #s = Subgraph(nodes=nodes)
        tx.commit()

@use('neo4j')
def load_licitacao_csv_neo4j(*licitacoes, neo4j):
    with open("database/feed/carrega_licitacao.cypher") as f:
        query = f.read().rstrip("\n")
    neo4j.run(query)

def get_graph(**options):
    """
    This function builds the graph that needs to be executed.

    :return: bonobo.Graph

    """
    graph = bonobo.Graph()
    graph.add_chain(
        download_licitacao,
        transform_licitacao,
        #bonobo.Limit(10000),
        #bonobo.UnpackItems(0),
        bonobo.CsvWriter('dados/licitacao.txt'),
        #bonobo.Limit(1),
        #load_licitacao_csv_neo4j)
        #load_licitacao_neo4j)

    return graph


def get_services(**options):
    """
    This function builds the services dictionary, which is a simple dict of names-to-implementation used by bonobo
    for runtime injection.

    It will be used on top of the defaults provided by bonobo (fs, http, ...). You can override those defaults, or just
    let the framework define them. You can also define your own services and naming is up to you.

    :return: dict
    """
    neo4j = Graph("localhost", user="neo4j", password="password")
    logging.getLogger("neo4j").setLevel(logging.WARNING)
    neo4j.run('CREATE INDEX ON :Licitacao2(uuid)')

    neo4j_driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))
    

    return {'neo4j': neo4j,
            'neo4j_driver': neo4j_driver}


# The __main__ block actually execute the graph.
if __name__ == '__main__':
    parser = bonobo.get_argument_parser()
    with bonobo.parse_args(parser) as options:
        bonobo.run(
            get_graph(**options),
            services=get_services(**options)
        )
        
