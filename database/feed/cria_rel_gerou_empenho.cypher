USING PERIODIC COMMIT 10000
LOAD CSV WITH HEADERS FROM "file:///empenhos.csv" AS line

MATCH (lic:Licitacao {
    id_licitacao: (line.cd_ugestora + SUBSTRING('00', SIZE(line.cd_modalidade_licitacao)) +
				   line.cd_modalidade_licitacao + line.nu_Licitacao)
})
MATCH (emp:Empenho {
	id_empenho: (line.cd_ugestora + line.dt_Ano + line.nu_Empenho)
})
MERGE (lic)-[:GEROU]->(emp);
