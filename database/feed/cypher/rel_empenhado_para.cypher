USING PERIODIC COMMIT 5000
LOAD CSV WITH HEADERS FROM 'file:///empenhos.csv' AS line
WITH line
WHERE size(line.cd_credor) = 14 OR size(line.cd_credor) <= 11

WITH line, CASE WHEN size(line.cd_credor) <= 11 OR (line.cd_credor STARTS WITH '000' AND NOT line.cd_credor STARTS WITH '00000000')
    THEN ('***' + substring(line.cd_credor, size(line.cd_credor) - 8, 6) + '**')
    ELSE line.cd_credor END AS cpf_cnpj_credor

WITH line, cpf_cnpj_credor

MATCH (emp:Empenho {id_empenho: line.id_empenho})
WITH line, cpf_cnpj_credor, emp

MATCH (p:Participante {cpf_cnpj: cpf_cnpj_credor, nome: toUpper(line.no_Credor)})
WITH emp, p

MERGE (emp)-[:EMPENHADO_PARA]-(p);