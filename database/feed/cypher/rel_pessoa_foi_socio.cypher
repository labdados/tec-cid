MATCH (s:Socio)
WHERE size(s.cpf_cnpj) = 11
WITH s

MERGE (p:Pessoa {cpf: s.cpf_cnpj, nome: s.nome})
WITH s, p

MERGE (p)-[:FOI]-(s);