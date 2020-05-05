MATCH (e:Empresa), (p:Participante) WHERE e.cnpj = p.cpf_cnpj
WITH e, p
MERGE (e)-[:FOI]-(p);