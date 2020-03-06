import csv
import io
import gzip

EMPRESA_LICITANTE_PB_CSV = "../../dados/empresa_licitante_pb.csv"
SOCIO_CSV_GZ = "../../dados/socio.csv.gz"
SOCIO_CSV = "../../dados/socio.csv"

HEADER = ['cnpj', 'identificador_de_socio', 'nome_socio', 'cnpj_cpf_do_socio', 'codigo_qualificacao_socio', 'percentual_capital_social', 'data_entrada_sociedade', 'codigo_pais', 'nome_pais_socio', 'cpf_representante_legal', 'nome_representante_legal', 'codigo_qualificacao_representante_legal']

CNPJ_INDEX = 0
TAMANHO_HEADER = 12


def extract_socios(input_gz):
    with io.TextIOWrapper(gzip.GzipFile(input_gz)) as csv_file:
        for line in csv_file:
            yield line

def transform_socios(line):
    for fields in csv.reader([line], delimiter=","):
        assert len(fields) == TAMANHO_HEADER
        return fields

def get_cnpj_socio(line):
    for fields in csv.reader([line], delimiter=","):
        return fields[CNPJ_INDEX]

def get_cnpjs_empresas(empresa_csv):
    with open(empresa_csv, 'r') as csv_file:
        reader = csv.reader(csv_file)

        # Pula o header
        next(reader)

        cnpj_empresas = set()
        for line in reader:
            cnpj_empresas.add(line[CNPJ_INDEX])

    return cnpj_empresas

def write_socios(socio_csv_gz, socio_csv, set_cnpj):
    with open(socio_csv, 'w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(HEADER)

        for line in extract_socios(socio_csv_gz):
            cpnj = get_cnpj_socio(line)

            if (cpnj in set_cnpj):
                writer.writerow(transform_socios(line))


if __name__ == '__main__':
    cnpj_empresas = get_cnpjs_empresas(EMPRESA_LICITANTE_PB_CSV)
    
    write_socios(SOCIO_CSV_GZ, SOCIO_CSV, cnpj_empresas)