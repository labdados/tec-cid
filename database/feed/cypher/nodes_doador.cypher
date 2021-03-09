USING PERIODIC COMMIT 10000
LOAD CSV WITH HEADERS FROM "file:///doacoes_candidatos.csv" AS line
FIELDTERMINATOR ';'
WITH line
WHERE size(line.NR_CPF_CNPJ_DOADOR) >= 11 and toUpper(line.NM_DOADOR_RFB) <> ''

WITH line, CASE WHEN size(line.NR_CPF_CNPJ_DOADOR) <= 11 OR (line.NR_CPF_CNPJ_DOADOR STARTS WITH '000' AND NOT line.NR_CPF_CNPJ_DOADOR STARTS WITH '00000000')
    THEN ('***' + substring(line.NR_CPF_CNPJ_DOADOR, size(line.NR_CPF_CNPJ_DOADOR) - 8, 6) + '**')
    ELSE line.NR_CPF_CNPJ_DOADOR END AS cpf_cnpj_doador

WITH line, cpf_cnpj_doador

MERGE (d:Doador {cpf_cnpj: cpf_cnpj_doador, nome: toUpper(line.NM_DOADOR_RFB)});