import bonobo
import gzip
import requests
import os
from bonobo.config import use
from io import TextIOWrapper

URL = 'https://dados.tce.pb.gov.br/TCE-PB-Portal-Gestor-Licitacoes_Propostas.txt.gz'
DATA_DIR = '../../dados/'
INPUT_FILE = 'TCE-PB-Portal-Gestor-Licitacoes_Propostas.txt.gz'
OUTPUT_FILE = 'licitacoes_propostas.csv'

@use('fs')
def extract_licitacao(fs):
    r = requests.get(URL)
    with fs.open(INPUT_FILE, 'wb') as f:
        f.write(r.content)
    return INPUT_FILE

@use('fs')
def transform_licitacao(filename, fs):
    file_gz = os.path.join(DATA_DIR, INPUT_FILE)
    with TextIOWrapper(gzip.open(file_gz), newline='\n') as text_file:
        header = text_file.readline().rstrip().split('|')
        for row in text_file:
            licitacao = row.rstrip().replace('\r', '').split('|')
            assert len(licitacao) == 23
            yield dict(zip(header, licitacao))

def get_graph(**options):
    graph = bonobo.Graph()
    graph.add_chain(
        extract_licitacao,
        transform_licitacao,
        bonobo.UnpackItems(0),
        bonobo.CsvWriter(OUTPUT_FILE)
    )
    return graph

def get_services(**options):
    return {'fs': bonobo.open_fs(DATA_DIR)}

if __name__ == '__main__':
    parser = bonobo.get_argument_parser()
    with bonobo.parse_args(parser) as options:
        bonobo.run(
            get_graph(**options),
            services=get_services(**options)
        )
