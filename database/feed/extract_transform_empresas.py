import sys
import os
import csv
import io
from decouple import config
from py2neo import Graph
import gzip

CNPJ_INDEX = 0
TAMANHO_CPF = 11
TAMANHO_CNPJ = 14

HEADER = ["cnpj","identificador_matriz_filial","razao_social","nome_fantasia","situacao_cadastral","data_situacao_cadastral","motivo_situacao_cadastral","nome_cidade_exterior","codigo_natureza_juridica","data_inicio_atividade","cnae_fiscal","descricao_tipo_logradouro","logradouro","numero","complemento","bairro","cep","uf","codigo_municipio","municipio","ddd_telefone_1","ddd_telefone_2","ddd_fax","qualificacao_do_responsavel","capital_social","porte","opcao_pelo_simples","data_opcao_pelo_simples","data_exclusao_do_simples","opcao_pelo_mei","situacao_especial","data_situacao_especial"]

EMPRESA_CSV_GZ = "../../dados/empresa.csv.gz"
EMPRESA_LICITANTE_PB_CSV = "../../dados/empresa_licitante_pb.csv"


def get_summary(set_participantes):
    cpfs = cnpjs = erros = total = 0

    for p in participantes:
        if (len(p) == TAMANHO_CPF):
            cpfs += 1

        elif (len(p) == TAMANHO_CNPJ):
            cnpjs += 1

        else:
            print('TAMANHO DO CPF / CNPJ INCORRETO: ', len(p))
            erros += 1

        total += 1

    print('SUMMARY \n\nCPFs: {} \nCNPJs: {} \nERRORS: {} \n\nTOTAL: {}'.format(cpfs, cnpjs, erros, total))


def get_query_response(neo4j: Graph, query):
    return neo4j.run(query).data()

def get_set_cpf_cnpj(neo4j: Graph, query):
    participantes = get_query_response(neo4j, query)
    aux = [p['p.cpf_cnpj'] for p in participantes]

    return set(aux)

def extract_empresas(input_gz):
    with io.TextIOWrapper(gzip.GzipFile(input_gz)) as csv_file:
        for line in csv_file:
            yield line

def transform_empresas(line):
    fields = line.replace('\n', '').split(',')
    return fields

def get_cnpj(line):
    for fields in csv.reader([line], delimiter=","):
        return fields[CNPJ_INDEX]


if __name__ == '__main__':
    user = sys.argv[1] if len(sys.argv) > 1 else config(
        'NEO4J_USER', default='neo4j')
    password = sys.argv[2] if len(sys.argv) > 2 else config(
        'NEO4J_PASSWORD', default='password')

    neo4j = Graph("localhost", user=user, password=password)

    query = "MATCH (p:Participante) RETURN p.cpf_cnpj;"

    participantes = get_set_cpf_cnpj(neo4j, query)

    get_summary(participantes)

    # Removendo CNPJs inválidos
    participantes.remove('')
    participantes.remove('0013670772812')

    with open(EMPRESA_LICITANTE_PB_CSV, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(HEADER)

        for line in extract_empresas(EMPRESA_CSV_GZ):
            cnpj = get_cnpj(line)

            if (cnpj in participantes):
                writer.writerow(transform_empresas(line))