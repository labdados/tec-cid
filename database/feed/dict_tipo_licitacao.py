import csv
import operator

CSV_TIPOS_LICITACOES = '../../dados/tipo_licitacao.csv'
TIPO_LICITACAO_IDX = 0
CD_TIPO_LICITACAO_IDX = 1

def get_dictionary(csv_tipos_licitacoes):
    with open(csv_tipos_licitacoes, 'r') as file:
        csv_data = csv.reader(file, delimiter=",")
        next(csv_data) # Skip title line
        dictionary = {}
        for row in csv_data:
            dictionary[row[TIPO_LICITACAO_IDX]] = int(row[CD_TIPO_LICITACAO_IDX])
    return dictionary

def update_csv(csv_tipos_licitacoes, aux_dicionary):
    with open(csv_tipos_licitacoes, 'a') as file:
        csv_data = csv.writer(file, delimiter=",")

        for key in aux_dicionary:
            csv_data.writerow([key, int(aux_dicionary[key])])
        
def get_max_codigo_licitacao(dictionary):
    result = max(dictionary.items(), key=operator.itemgetter(1))[CD_TIPO_LICITACAO_IDX]
    return result