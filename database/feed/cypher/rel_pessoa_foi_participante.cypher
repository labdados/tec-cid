MATCH (part:Participante)
WHERE size(part.cpf_cnpj) = 11
WITH part

MERGE (p:Pessoa {cpf: part.cpf_cnpj, nome: part.nome})
WITH part, p

MERGE (p)-[:FOI]-(part);