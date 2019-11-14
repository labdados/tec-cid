USING PERIODIC COMMIT 10000
LOAD CSV WITH HEADERS FROM "file:///empenhos.csv" AS line

MATCH (emp:Empenho {
	id_empenho: (line.cd_ugestora + line.dt_Ano + line.nu_Empenho)
})
WITH emp, line.no_Credor AS line_no_Credor,
	 CASE WHEN line.cpf_cnpj STARTS WITH '000' THEN ('***' + substring(line.cpf_cnpj, 6, 6) + '**')
										 ELSE line.cpf_cnpj AS line_cpf_cnpj
WHERE line_cpf_cnpj <> NULL
MERGE (p:Participante { cpf_cnpj: line_cpf_cnpj })
ON CREATE SET p.nome = toUpper(line_no_Credor),
 p.credor = TRUE
ON UPDATE SET p.credor = TRUE
MERGE (emp)-[:EMPENHADO_PARA]->(p);
