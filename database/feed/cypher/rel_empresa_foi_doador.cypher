MATCH (e:Empresa)
WITH e

MATCH (d:Doador)
WHERE e.cnpj = d.cpf_cnpj
WITH e, d

MERGE (e)-[:FOI]-(d);