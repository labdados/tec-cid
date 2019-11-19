import csv
import gzip
import io
import os
import sys
import time

LICITACOES_INPUT_GZ = '../../dados/TCE-PB-Portal-Gestor-Licitacoes_Propostas.txt.gz'
LICITACOES_OUTPUT_CSV = '../../dados/licitacoes_propostas.csv'

EMPENHOS_INPUT_GZ = '../../dados/TCE-PB-SAGRES-Empenhos_Esfera_Municipal.txt.gz'
EMPENHOS_OUTPUT_CSV = '../../dados/empenhos.csv'

PAGAMENTOS_INPUT_GZ = '../../dados/TCE-PB-SAGRES-Pagamentos_Esfera_Municipal.txt.gz'
PAGAMENTOS_OUTPUT_CSV = '../../dados/pagamentos.csv'

LIQUIDACOES_INPUT_GZ = '../../dados/TCE-PB-SAGRES-Liquidacoes_Esfera_Municipal.txt.gz'
LIQUIDACOES_OUTPUT_CSV = '../../dados/liquidacoes.csv'

NUM_LICITACAO_IDX = 1
TIPO_LICITACAO_IDX = 2
TIPO_LICITACAO_EMPENHOS_IDX = 15

ANO_EMPENHO_COL = 2
ANO_EMPENHO_MIN = 2014

PROXIMO_CD_TIPO_LICITACAO = 16

CD_TIPOS_LICITACOES = {
    "Pregão (Eletrônico e Presencial)": 0,
    "Concorrência": 1,
    "Tomada de Preços": 2,
    "Tomada de Preço": 2,
    "Convite": 3,
    "Concurso": 4,
    "Leilão": 5,
    "Dispensa por Valor": 6,
    "Dispensada (Art. 17 - Lei 8.666/93)": 6,
    "Dispensa por outros motivos": 7,
    "Dispensa (Art. 24 - Lei 8.666/93)": 7,
    "Inexigível": 8,
    "Inexigibilidade": 8,
    "Sem Licitação": 9,
    "Pregão Eletrônico": 10,
    "Pregão Presencial": 11,
    "Adesão a Registro de Preço": 12,
    "Adesão a Ata de Registro de Preços": 12,
    "Chamada Pública": 13,
    "RDC - Regime Diferenciado de Contratações Públicas": 14,
    "Licitação da Lei Nº 13.303/2016": 15,
    "Licitação da Lei Nº 13.303/2016 (Art. 29 ou 30)": 15
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

def add_tipo_licitacao(fields, row_num, tipo_licitacao_idx):
    text = ''
    tipo_licitacao = fields[tipo_licitacao_idx]
    if (tipo_licitacao in CD_TIPOS_LICITACOES):
        text = CD_TIPOS_LICITACOES[tipo_licitacao]
    elif row_num == 1:
        text = "cd_tipo_licitacao"
    else:
        print("Adicionando novo tipo de licitacao: {} ({})".format(tipo_licitacao,
                                                                   PROXIMO_CD_TIPO_LICITACAO))
        CD_TIPOS_LICITACOES[tipo_licitacao] = PROXIMO_CD_TIPO_LICITACAO
        PROXIMO_CD_TIPO_LICITACAO += 1

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
                writer.writerow(fields)

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


    input_file = sys.argv[1] if len(sys.argv) > 1 else LIQUIDACOES_INPUT_GZ
    output_file = sys.argv[2] if len(sys.argv) > 2 else LIQUIDACOES_OUTPUT_CSV
    initial_time = time.time()
    print('Writing in ' + LIQUIDACOES_OUTPUT_CSV)

    linhas = 0

    with open(output_file, 'w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)
        for line in extract_liquidacoes(input_file):
            fields = transform_liquidacoes(line)
            if (fields != None):
                writer.writerow(fields)

            else:
                linhas += 1

    print("TOTAL DE LINHAS DEFEITUOSAS: " + str(linhas))
    final_time = time.time()
    total = final_time - initial_time
    print('(written in {:.2f} minutes)'.format(total / 60))