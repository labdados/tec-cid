USING PERIODIC COMMIT 10000
LOAD CSV WITH HEADERS FROM "file:///empenhos.csv" AS line

MATCH (lic:Licitacao {
    id_licitacao: (line.cd_ugestora + SUBSTRING('00', SIZE(line.cd_tipo_licitacao)) +
				   line.cd_tipo_licitacao + line.nu_Licitacao)
})
MATCH (emp:Empenho {
	id_empenho: line.id_empenho
})
MERGE (lic)-[:GEROU]->(emp);
