import csv
import io
import os
import unidecode
import zipfile as zf

PRESTACAO_INPUT_ZIP = '../../dados/prestacao_contas_2016.zip'
RECEITA_ZIP_FILENAME = 'receitas_candidatos_2016_PB.txt'
RECEITA_OUTPUT_CSV = '../../dados/doacoes_candidatos.csv'

CANDIDATOS_INPUT_ZIP = '../../dados/consulta_cand_2016.zip'
CANDIDATOS_ZIP_FILENAME = 'consulta_cand_2016_PB.csv'
CANDIDATOS_OUTPUT_CSV = '../../dados/candidatos.csv'
CANDIDATOS_SIT_TOT_COL = 53
CANDIDATOS_SIT_TOT_EXCLUDE = ['2º TURNO', '#NULO#', '']

def extract_tse(zip_file, file_to_decompress):
    zip_file = zf.ZipFile(zip_file)
    with io.TextIOWrapper(zip_file.open(file_to_decompress), encoding="latin1") as text_file:
        for line in text_file:
            yield line

def transform_tse(line, n_fields=None):
    #line = unidecode.unidecode(line).replace('#NULO', '')
    for fields in csv.reader([line], delimiter=";"):
        fields = ['' if f.startswith('#NULO') else f for f in fields]
        if n_fields:
            assert len(fields) == n_fields
        return fields

def filter_candidatos(row):
    return '' if row[CANDIDATOS_SIT_TOT_COL] in CANDIDATOS_SIT_TOT_EXCLUDE else row

if __name__ == '__main__':
    # Extract and transform receitas
    with open(RECEITA_OUTPUT_CSV, 'w') as csv_file:
         row_num = 0
         writer = csv.writer(csv_file)
         for line in extract_tse(PRESTACAO_INPUT_ZIP, RECEITA_ZIP_FILENAME):
            row = transform_tse(line, n_fields=35)
            if row_num == 0:
                row.insert(0, 'Linha')
            else:
                row.insert(0, row_num)
            
            writer.writerow(row)
            row_num += 1

    # Extract, transform and filter candidatos
    with open(CANDIDATOS_OUTPUT_CSV, 'w') as csv_file:
         row_num = 0
         writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)
         for line in extract_tse(CANDIDATOS_INPUT_ZIP, CANDIDATOS_ZIP_FILENAME):
            row = filter_candidatos(transform_tse(line, n_fields=58))
            writer.writerow(row)