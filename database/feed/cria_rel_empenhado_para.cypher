USING PERIODIC COMMIT 10000
LOAD CSV WITH HEADERS FROM "file:///empenhos.csv" AS line

MATCH (emp:Empenho {
	id_empenho: (line.cd_ugestora + SUBSTRING('00', SIZE(line.cd_modalidade_licitacao)) +
				 line.cd_modalidade_licitacao + line.nu_Licitacao + line.nu_Empenho)
})
MATCH (p:Participante)
WHERE (size(p.cpf_cnpj) <= 11 AND p.cpf_cnpj = ('***' + substring(line.cpf_cnpj, 3, 6) + '**')) OR
      (size(p.cpf_cnpj) > 11 AND p.cpf_cnpj = line.cpf_cnpj)

MERGE (emp)-[:EMPENHADO_PARA]->(p);
