import sys
import os
import csv
import io
from decouple import config
from py2neo import Graph
import gzip

import datetime
import logging
from logging.config import dictConfig

from log_utils.log_utils import LogUtils


CNPJ_INDEX = 0
TAMANHO_CPF = 11
TAMANHO_CNPJ = 14

HEADER = ["cnpj","identificador_matriz_filial","razao_social","nome_fantasia","situacao_cadastral","data_situacao_cadastral","motivo_situacao_cadastral","nome_cidade_exterior","codigo_natureza_juridica","data_inicio_atividade","cnae_fiscal","descricao_tipo_logradouro","logradouro","numero","complemento","bairro","cep","uf","codigo_municipio","municipio","ddd_telefone_1","ddd_telefone_2","ddd_fax","qualificacao_do_responsavel","capital_social","porte","opcao_pelo_simples","data_opcao_pelo_simples","data_exclusao_do_simples","opcao_pelo_mei","situacao_especial","data_situacao_especial"]
TAMANHO_HEADER = len(HEADER) #32

EMPRESA_CSV_GZ = "../../dados/empresa.csv.gz"
EMPRESA_CSV = "../../dados/empresa.csv"


def get_summary(set_participantes):
    cpfs = cnpjs = erros = total = 0

    for p in participantes:
        if (len(p) == TAMANHO_CPF):
            cpfs += 1

        elif (len(p) == TAMANHO_CNPJ):
            cnpjs += 1

        else:
            logging.warning(f'TAMANHO DO CPF / CNPJ INCORRETO: {len(p)}')
            erros += 1

        total += 1

    logging.info('SUMMARY \n\nCPFs: {} \nCNPJs: {} \nERRORS: {} \n\nTOTAL: {}'.format(cpfs, cnpjs, erros, total))


def get_query_response(neo4j: Graph, query):
    return neo4j.run(query).data()

def get_set_cpf_cnpj_participantes(neo4j: Graph, query):
    participantes = get_query_response(neo4j, query)
    aux = [p['p.cpf_cnpj'] for p in participantes]

    return set(aux)

def get_set_cpf_cnpj_doadores(neo4j: Graph, query):
    doadores = get_query_response(neo4j, query)
    aux = [d['d.cpf_cnpj'] for d in doadores]

    return set(aux)

def extract_empresas(input_gz):
    with io.TextIOWrapper(gzip.GzipFile(input_gz)) as csv_file:
        for line in csv_file:
            yield line

def transform_empresas(line):
    for fields in csv.reader([line], delimiter=","):
        assert len(fields) == TAMANHO_HEADER
        return fields

def get_cnpj(line):
    for fields in csv.reader([line], delimiter=","):
        return fields[CNPJ_INDEX]

def get_time():
    now = datetime.datetime.now()
    hours = now.hour
    minutes = now.minute
    seconds = now.second

    return  '{}h:{}m:{}s'.format(hours, minutes, seconds)

def assert_max_size(old_size, new_size):
    assert new_size > old_size

def is_subset(set_a, set_b):
    assert set_a.issubset(set_b) == True

if __name__ == '__main__':
    dictConfig(LogUtils.get_updated_dict_config())

    start_time = '[START extract empresas]: ' + get_time()

    user = sys.argv[1] if len(sys.argv) > 1 else config(
        'NEO4J_USER', default='neo4j')
    password = sys.argv[2] if len(sys.argv) > 2 else config(
        'NEO4J_PASSWORD', default='password')

    neo4j = Graph("localhost", user=user, password=password)

    query_participantes = "MATCH (p:Participante) WHERE size(p.cpf_cnpj) = 14 RETURN p.cpf_cnpj;"
    query_doadores = "MATCH (d:Doador) WHERE size(d.cpf_cnpj) = 14 RETURN d.cpf_cnpj;"

    participantes = get_set_cpf_cnpj_participantes(neo4j, query_participantes)
    doadores = get_set_cpf_cnpj_doadores(neo4j, query_doadores)

    empresas = participantes
    old_size = len(empresas)

    empresas.update(doadores)
    new_size = len(empresas)

    assert_max_size(old_size, new_size)
    is_subset(doadores, empresas)

    get_summary(participantes)

    # Removendo CNPJs inválidos
    if ('' in participantes):
        participantes.remove('')

    if ('0013670772812' in participantes):
        participantes.remove('0013670772812')

    with open(EMPRESA_CSV, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(HEADER)

        for line in extract_empresas(EMPRESA_CSV_GZ):
            cnpj = get_cnpj(line)

            if (cnpj in empresas):
                writer.writerow(transform_empresas(line))

    finish_time = '[FINISH extract empresas]: ' + get_time()

    logging.info(start_time)
    logging.info(finish_time)