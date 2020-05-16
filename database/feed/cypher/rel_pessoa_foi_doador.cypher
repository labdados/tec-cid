MATCH (d:Doador)
WHERE size(d.cpf_cnpj) = 11
WITH d

MERGE (p:Pessoa {cpf: d.cpf_cnpj, nome: d.nome})
WITH d, p

MERGE (p)-[:FOI]-(d);