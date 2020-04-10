MATCH (s:Socio), (d:Doador) WHERE s.cpf_cnpj = d.cpf_cnpj
WITH s, d
MERGE (s)-[:FOI]-(d);