import csv

CSV_TIPOS_LICITACOES = '../../dados/tipo_licitacao.csv'
TIPO_LICITACAO_IDX = 0
CD_TIPO_LICITACAO_IDX = 1


def get_dictionary(csv_file):
    with open(csv_file, 'r') as file:
        csv_data = csv.reader(file, delimiter=",")

        # Skip title line
        next(csv_data)
        dictionary = {}
        for row in csv_data:
            dictionary[row[TIPO_LICITACAO_IDX]] = row[CD_TIPO_LICITACAO_IDX]
    return dictionary


res = get_dictionary(CSV_TIPOS_LICITACOES)
print(res)