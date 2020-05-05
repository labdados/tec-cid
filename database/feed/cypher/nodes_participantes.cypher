USING PERIODIC COMMIT 10000
LOAD CSV WITH HEADERS FROM "file:///empenhos.csv" AS line
WITH line
WHERE size(line.cd_credor) = 14 OR size(line.cd_credor) <= 11

WITH line, CASE WHEN size(line.cd_credor) <= 11 OR (line.cd_credor STARTS WITH '000' AND NOT line.cd_credor STARTS WITH '00000000')
    THEN ('***' + substring(line.cd_credor, size(line.cd_credor) - 8, 6) + '**')
    ELSE line.cd_credor END AS cpf_cnpj_credor

WITH line, cpf_cnpj_credor

MERGE (p:Participante { cpf_cnpj: cpf_cnpj_credor })
ON CREATE SET p.nome = toUpper(line.no_Credor);