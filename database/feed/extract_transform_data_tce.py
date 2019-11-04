import csv
import gzip
import io
import os
import sys


LICITACOES_INPUT_GZ = '../../dados/TCE-PB-Portal-Gestor-Licitacoes_Propostas.txt.gz'
LICITACOES_OUTPUT_CSV = '../../dados/licitacoes_propostas.csv'

EMPENHOS_INPUT_GZ = '../../dados/TCE-PB-SAGRES-Empenhos_Esfera_Municipal.txt.gz'
EMPENHOS_OUTPUT_CSV = '../../dados/empenhos.csv'

PAGAMENTOS_INPUT_GZ = '../../dados/TCE-PB-SAGRES-Pagamentos_Esfera_Municipal.txt.gz'
PAGAMENTOS_OUTPUT_GZ = '../../dados/pagamentos.csv'

NUM_LICITACAO_IDX = 1
MODALIDADE_IDX = 2

CD_MODALIDADES = {
    "Pregão (Eletrônico e Presencial)": 0,
    "Concorrência": 1,
    "Tomada de Preço": 2,
    "Convite": 3,
    "Concurso": 4,
    "Leilão": 5,
    "Dispensada (Art. 17 - Lei 8.666/93)": 6,
    "Dispensa (Art. 24 - Lei 8.666/93)": 7,
    "Inexigibilidade": 8,
    "Sem Licitação": 9,
    "Pregão Eletrônico": 10,
    "Pregão Presencial": 11,
    "Adesão a Ata de Registro de Preços": 12,
    "Chamada Pública": 13,
    "RDC - Regime Diferenciado de Contratações Públicas": 14,
    "Licitação da Lei Nº 13.303/2016": 15,
    "Licitação da Lei Nº 13.303/2016 (Art. 29 ou 30)": 16
}

def extract_licitacao(input_gz):
    with io.TextIOWrapper(gzip.GzipFile(input_gz)) as text_file:
        for line in text_file:
            yield line

def transform_licitacao(line):
    fields = line.rstrip().replace('\r', '').split('|')
    fields = [x if x != 'NULL' else '' for x in fields]
    fields[NUM_LICITACAO_IDX] = fields[NUM_LICITACAO_IDX].replace('/', '')
    assert len(fields) == 23
    return fields

def add_codigo_modalidade(fields, row_num):
    text = ''
    modalidade = fields[MODALIDADE_IDX]
    if row_num == 1:
        text = "cd_modalidade_licitacao"
    elif modalidade in CD_MODALIDADES:
        text = CD_MODALIDADES[modalidade]
    fields.append(text)
    return fields

def extract_empenhos(input_gz):
    with io.TextIOWrapper(gzip.GzipFile(input_gz)) as text_file:
        for line in text_file:
            yield line

def transform_empenhos(line):
    fields = line.rstrip().replace('\r', '').replace('\\', '').split('|')
    fields = [x if x != 'NULL' else '' for x in fields]
    return fields if (len(fields) == 26) else None

def extract_pagamentos(input_gz):
    with io.TextIOWrapper(gzip.GzipFile(input_gz)) as text_file:
        for line in text_file:
            yield line

def transform_pagamentos(line):
    fields = line.rstrip().replace('\r', '').split('|')
    fields = [x if x != 'NULL' else '' for x in fields]
    assert len(fields) == 15
    return fields

if __name__ == '__main__':
    input_file = sys.argv[1] if len(sys.argv) > 1 else LICITACOES_INPUT_GZ
    output_file = sys.argv[2] if len(sys.argv) > 2 else LICITACOES_OUTPUT_CSV

    print('Writing in ' + LICITACOES_OUTPUT_CSV)
    with open(output_file, 'w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)
        row_num = 0
        for line in extract_licitacao(input_file):
            row_num += 1
            fields = transform_licitacao(line)
            fields = add_codigo_modalidade(fields, row_num)
            writer.writerow(fields)


    input_file = sys.argv[1] if len(sys.argv) > 1 else EMPENHOS_INPUT_GZ
    output_file = sys.argv[2] if len(sys.argv) > 2 else EMPENHOS_OUTPUT_CSV

    print('Writing in ' + EMPENHOS_OUTPUT_CSV)
    with open(output_file, 'w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)
        for line in extract_empenhos(input_file):
            fields = transform_empenhos(line)
            if (fields != None): writer.writerow(fields)


    input_file = sys.argv[1] if len(sys.argv) > 1 else PAGAMENTOS_INPUT_GZ
    output_file = sys.argv[2] if len(sys.argv) > 2 else PAGAMENTOS_OUTPUT_GZ

    print('Writing in ' + PAGAMENTOS_OUTPUT_GZ)
    with open(output_file, 'w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)
        for line in extract_pagamentos(input_file):
            fields = transform_pagamentos(line)
            writer.writerow(fields)