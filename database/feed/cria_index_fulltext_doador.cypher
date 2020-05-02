WITH 1 AS ignored
WHERE NOT apoc.schema.node.indexExists("Doador", ["nome", "cpf_cnpj"])

CALL db.index.fulltext.createNodeIndex("nome_doador", ["Doador"], ["nome", "cpf_cnpj"])
RETURN true