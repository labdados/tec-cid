USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///socios_doadores_com_nomes_distintos.csv" AS line
WITH line

MATCH (s:Socio) WHERE s.cpf_cnpj = line.cpf_cnpj_socio AND s.nome = line.nome_socio
WITH s, line

MATCH (d:Doador) WHERE d.cpf_cnpj = line.cpf_cnpj_doador AND d.nome = line.nome_doador
WITH s, d

MERGE (s)-[:FOI]-(d);