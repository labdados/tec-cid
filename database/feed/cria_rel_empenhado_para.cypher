USING PERIODIC COMMIT 10000
LOAD CSV WITH HEADERS FROM "file:///empenhos.csv" AS line
WITH line

MATCH (emp:Empenho {
	id_empenho: (line.cd_ugestora + line.dt_Ano + line.nu_Empenho)
})
WITH emp, line, CASE WHEN line.cd_credor STARTS WITH '000'
					THEN ('***' + substring(line.cd_credor, 6, 6) + '**')
					ELSE line.cd_credor END AS cpf_cnpj_credor
MERGE (p:Participante { cpf_cnpj: cpf_cnpj_credor })
ON CREATE SET p.nome = toUpper(line.no_Credor)
MERGE (emp)-[:EMPENHADO_PARA]->(p);
