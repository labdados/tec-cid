MATCH (s:Socio)
WITH s

MATCH (d:Doador)
WHERE s.cpf_cnpj = d.cpf_cnpj AND s.nome = d.nome

WITH s, d
MERGE (s)-[:FOI]->(d);