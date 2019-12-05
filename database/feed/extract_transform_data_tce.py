import csv
import gzip
import io
import os
import sys
import hashlib
import time
from dict_tipo_licitacao import get_dictionary, update_csv, get_max_codigo_licitacao

LICITACOES_INPUT_GZ = '../../dados/TCE-PB-Portal-Gestor-Licitacoes_Propostas.txt.gz'
LICITACOES_OUTPUT_CSV = '../../dados/licitacoes_propostas.csv'

EMPENHOS_INPUT_GZ = '../../dados/TCE-PB-SAGRES-Empenhos_Esfera_Municipal.txt.gz'
EMPENHOS_OUTPUT_CSV = '../../dados/empenhos.csv'

PAGAMENTOS_INPUT_GZ = '../../dados/TCE-PB-SAGRES-Pagamentos_Esfera_Municipal.txt.gz'
PAGAMENTOS_OUTPUT_CSV = '../../dados/pagamentos.csv'

CSV_TIPOS_LICITACOES = '../../dados/tipo_licitacao.csv'

NUM_LICITACAO_IDX = 1
TIPO_LICITACAO_IDX = 2
TIPO_LICITACAO_EMPENHOS_IDX = 15

ANO_EMPENHO_COL = 2
ANO_EMPENHO_MIN = 2014

CD_UGESTORA_IDX = 0
DT_ANO_IDX = 2
DESC_UORCAMENTARIA_IDX = 3
NUMERO_EMPENHO_IDX = 17

CD_TIPOS_LICITACOES = get_dictionary(CSV_TIPOS_LICITACOES)

# Retorna o maior código do dicionário e incrementa uma unidade = próximo código
PROXIMO_CD_TIPO_LICITACAO = get_max_codigo_licitacao(CD_TIPOS_LICITACOES) + 1

CD_TIPOS_LICITACOES_AUX = {}

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


def add_id_hash(fields, row_num, id_hash):
    if (row_num == 1):
        fields.append("id_empenho")
        return fields
    fields.append(id_hash)
    return fields

def add_tipo_licitacao(fields, row_num, tipo_licitacao_idx):
    text = ''
    tipo_licitacao = fields[tipo_licitacao_idx]
    if (tipo_licitacao in CD_TIPOS_LICITACOES):
        text = CD_TIPOS_LICITACOES[tipo_licitacao]
    elif row_num == 1:
        text = "cd_tipo_licitacao"
    else:
        PROXIMO_CD_TIPO_LICITACAO = get_max_codigo_licitacao(CD_TIPOS_LICITACOES) + 1
        CD_TIPOS_LICITACOES_AUX[tipo_licitacao] = PROXIMO_CD_TIPO_LICITACAO

        print("Adicionando novo tipo de licitacao: {} ({})".format(tipo_licitacao,
                                                                   PROXIMO_CD_TIPO_LICITACAO))
        CD_TIPOS_LICITACOES[tipo_licitacao] = PROXIMO_CD_TIPO_LICITACAO
        text = CD_TIPOS_LICITACOES[tipo_licitacao]

    fields.append(text)
    return fields

def extract_empenhos(input_gz):
    with io.TextIOWrapper(gzip.GzipFile(input_gz)) as text_file:
        for line in text_file:
            yield line

def get_id_hash(id):
    result = hashlib.md5(id.encode())
    return result.hexdigest()

def transform_empenhos(line):
    fields = line.rstrip().replace('\r', '').replace('\\', '').split('|')
    fields = [x if x != 'NULL' else '' for x in fields]
    return fields if (len(fields) == 26) else None

def filter_empenhos(line, line_no):
    return line if line_no == 1 or (line and int(line[ANO_EMPENHO_COL]) >= ANO_EMPENHO_MIN) else ''

def extract_pagamentos(input_gz):
    with io.TextIOWrapper(gzip.GzipFile(input_gz)) as text_file:
        for line in text_file:
            yield line

def transform_pagamentos(line):
    fields = line.rstrip().replace('\r', '').split('|')
    fields = [x if x != 'NULL' else '' for x in fields]
    assert len(fields) == 15
    return fields

def extract_liquidacoes(input_gz):
    with io.TextIOWrapper(gzip.GzipFile(input_gz)) as text_file:
        for line in text_file:
            yield line

def transform_liquidacoes(line):
    fields = line.rstrip().replace('\r', '').split('|')
    fields = [x if x != 'NULL' and x != '-' else '' for x in fields]
    return fields if (len(fields) == 17) else None


if __name__ == '__main__':
    input_file = sys.argv[1] if len(sys.argv) > 1 else LICITACOES_INPUT_GZ
    output_file = sys.argv[2] if len(sys.argv) > 2 else LICITACOES_OUTPUT_CSV

    initial_time = time.time()

    print('Writing in ' + LICITACOES_OUTPUT_CSV)
    with open(output_file, 'w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)
        row_num = 0
        for line in extract_licitacao(input_file):
            row_num += 1
            fields = transform_licitacao(line)
            fields = add_tipo_licitacao(
                fields, row_num, TIPO_LICITACAO_IDX)
            writer.writerow(fields)

    final_time = time.time()
    total = final_time - initial_time
    print('(written in {:.2f} minutes)'.format(total / 60))

    input_file = sys.argv[1] if len(sys.argv) > 1 else EMPENHOS_INPUT_GZ
    output_file = sys.argv[2] if len(sys.argv) > 2 else EMPENHOS_OUTPUT_CSV

    initial_time = time.time()

    print('Writing in ' + EMPENHOS_OUTPUT_CSV)
    with open(output_file, 'w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)
        row_num = 0
        for line in extract_empenhos(input_file):
            row_num += 1
            fields = filter_empenhos(transform_empenhos(line), row_num)
            if fields:
                fields = add_tipo_licitacao(
                    fields, row_num, TIPO_LICITACAO_EMPENHOS_IDX)
                id_empenho = fields[CD_UGESTORA_IDX] + fields[DT_ANO_IDX] + fields[DESC_UORCAMENTARIA_IDX] + fields[NUMERO_EMPENHO_IDX]
                fields = add_id_hash(fields, row_num, get_id_hash(id_empenho))
                writer.writerow(fields)

    # Atualiza o arquivo tipo_licitacao.csv, caso tenha novos tipos
    if (len(CD_TIPOS_LICITACOES_AUX) > 1): update_csv(CSV_TIPOS_LICITACOES, CD_TIPOS_LICITACOES_AUX)
    
    final_time = time.time()
    total = final_time - initial_time
    print('(written in {:.2f} minutes)'.format(total / 60))

    input_file = sys.argv[1] if len(sys.argv) > 1 else PAGAMENTOS_INPUT_GZ
    output_file = sys.argv[2] if len(sys.argv) > 2 else PAGAMENTOS_OUTPUT_CSV

    initial_time = time.time()

    print('Writing in ' + PAGAMENTOS_OUTPUT_CSV)
    with open(output_file, 'w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)
        for line in extract_pagamentos(input_file):
            fields = transform_pagamentos(line)
            writer.writerow(fields)

    final_time = time.time()
    total = final_time - initial_time
    print('(written in {:.2f} minutes)'.format(total / 60))