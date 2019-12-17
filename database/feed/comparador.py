import csv
import collections

FILE_NAME = "../../dados/pagamentos.csv"

# A princípio, identificam unicamente um Pagamento
CD_UGESTORA_IDX = 0
DT_ANO_IDX = 2
NU_EMPENHO_IDX = 4
NU_PARCELA_IDX = 5
VL_PAGAMENTO_IDX = 6
DT_PAGAMENTO_IDX = 7
CD_CONTA_IDX = 8
#NU_CHEQUE_IDX = 10
#VL_RETENCAO_IDX = 11

with open(FILE_NAME, 'r') as file:
    csv_data = csv.reader(file, delimiter=',')
    next(csv_data)

    count = collections.Counter()
    '''
    Removidos
        row[VL_RETENCAO_IDX]
        row[NU_CHEQUE_IDX]
    #pagto = row[CD_UGESTORA_IDX] + row[DT_ANO_IDX] + row[NU_EMPENHO_IDX] + row[NU_PARCELA_IDX] + row[VL_PAGAMENTO_IDX] + row[DT_PAGAMENTO_IDX] + row[CD_CONTA_IDX] + row[NU_CHEQUE_IDX] + row[VL_RETENCAO_IDX]
    '''
    for row in csv_data:
        pagto = row[CD_UGESTORA_IDX] + row[DT_ANO_IDX] + row[NU_EMPENHO_IDX] + row[NU_PARCELA_IDX] + row[VL_PAGAMENTO_IDX] + row[DT_PAGAMENTO_IDX] + row[CD_CONTA_IDX]
        count[pagto] += 1

    total = 0
    for pagtos, nb in count.items():
        if (nb > 1):
            total += 1
            print(pagtos, ' is a duplicate payment', ' seen ', str(nb), ' times')

    print('Total: ', total)