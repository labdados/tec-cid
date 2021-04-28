import io
import os
import unidecode
import csv
import json
import zipfile as zf
import pandas as pd

from zipped_file_utils import ZippedFilesUtils
from headers.json_utils import JsonUtils
from headers.exceptions.missing_attributes_exception import MissingAttributesException

PREFIX = '../../dados/'
ATTRIBUTES_DOACOES_CANDIDATOS = PREFIX + 'attributes_doacoes_candidatos.json'

FINAL_RECEITA_CANDIDATOS_OUTPUT_CSV = '../../dados/doacoes_candidatos.csv'
FINAL_CANDIDATOS_CSV = '../../dados/candidatos.csv'

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
    #Extract and transform candidatos and doacoes_candidados
    zipped_files = ZippedFilesUtils.get_zipped_files_from_key('receita_candidatos')
    for zipped_file in zipped_files:
        final_path = PREFIX + zipped_file.get('output_csv')
        with open(final_path, 'w') as csv_file:
            writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)
            for line in extract_tse(PREFIX + zipped_file.get('input_zip'), zipped_file.get('zip_filename')):
                row = transform_tse(line)
                if (row):
                    writer.writerow(row)

    zipped_file = ZippedFilesUtils.get_zipped_files_from_year(key_name='receita_candidatos', year=2016)
    final_csv_path = PREFIX + zipped_file.get('output_csv')
    doacoes_2016 = pd.read_csv(final_csv_path, converters={'CPF/CNPJ do doador': str})

    zipped_file = ZippedFilesUtils.get_zipped_files_from_year(key_name='receita_candidatos', year=2020)
    final_csv_path = PREFIX + zipped_file.get('output_csv')
    doacoes_2020 = pd.read_csv(final_csv_path, converters={'NR_CPF_CNPJ_DOADOR': str})

    attributes_doacoes = JsonUtils.get_dict_from_json_file(ATTRIBUTES_DOACOES_CANDIDATOS, full_path=False)
    attributes_2016_dict = attributes_doacoes.get('attributes_2016_dict')
    used_attributes_2016_list = attributes_doacoes.get('used_attributes_2016_list')

    doacoes_2016_set = set(used_attributes_2016_list)
    doacoes_2020_set = set(doacoes_2020.columns.to_list())
    if (not doacoes_2016_set.issubset(doacoes_2020_set)):
        raise MissingAttributesException('Atributos de doações que eram de 2020 e eram utilizados para renomear atributos de 2016: ' 
            + str(doacoes_2016_set - doacoes_2020_set))

    doacoes_2016.rename(columns=attributes_2016_dict, inplace=True)
    doacoes_2016['ANO_ELEICAO'] = 2016
    doacoes_2016 = doacoes_2016[used_attributes_2016_list]
    doacoes_final_csv = pd.merge(doacoes_2016, doacoes_2020, how='outer')
    doacoes_final_csv.insert(0, 'LINHA', range(1, len(doacoes_final_csv)+1))

    assert len(doacoes_final_csv) == (len(doacoes_2016) + len(doacoes_2020))
    doacoes_final_csv.to_csv(FINAL_RECEITA_CANDIDATOS_OUTPUT_CSV, sep=';', quoting=csv.QUOTE_NONNUMERIC, index=False)


    # Extract, transform and filter candidatos
    zipped_files = ZippedFilesUtils.get_zipped_files_from_key('candidatos')
    for zipped_file in zipped_files:
        final_path = PREFIX + zipped_file.get('output_csv')
        with open(final_path, 'w') as csv_file:
            writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC, delimiter=";")
            for line in extract_tse(PREFIX + zipped_file.get('input_zip'), zipped_file.get('zip_filename')):
                row = filter_candidatos(transform_tse(line))
                if (row):
                    writer.writerow(row)

    zipped_file = ZippedFilesUtils.get_zipped_files_from_year(key_name='candidatos', year=2016)
    final_csv_path = PREFIX + zipped_file.get('output_csv')
    candidatos_2016 = pd.read_csv(final_csv_path, sep=';')

    zipped_file = ZippedFilesUtils.get_zipped_files_from_year(key_name='candidatos', year=2020)
    final_csv_path = PREFIX + zipped_file.get('output_csv')
    candidatos_2020 = pd.read_csv(final_csv_path, sep=';')

    candidatos_2016 = candidatos_2016.astype({'NM_SOCIAL_CANDIDATO': 'object', 'VR_DESPESA_MAX_CAMPANHA': 'float64'})
    candidatos_2020 = candidatos_2020.astype({'VR_DESPESA_MAX_CAMPANHA': 'float64'})

    candidatos_final_csv = pd.merge(candidatos_2016, candidatos_2020, how='outer')
    assert len(candidatos_final_csv) == (len(candidatos_2016) + len(candidatos_2020))

    candidatos_final_csv.to_csv(FINAL_CANDIDATOS_CSV, sep=';', quoting=csv.QUOTE_NONNUMERIC, index=False)