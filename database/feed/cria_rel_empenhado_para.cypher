USING PERIODIC COMMIT 10000
LOAD CSV WITH HEADERS FROM "file:///empenhos.csv" AS line

MATCH (emp:Empenho {
	id_empenho: (line.cd_ugestora + line.dt_Ano + line.nu_Empenho)
})
WITH emp, line, CASE WHEN line.cpf_cnpj STARTS WITH '000' THEN ('***' + substring(line.cpf_cnpj, 6, 6) + '**')
										 ELSE line.cpf_cnpj END AS line_cpf_cnpj
WHERE line_cpf_cnpj <> NULL
MERGE (p:Participante { cpf_cnpj: line_cpf_cnpj })
ON CREATE SET p.nome = toUpper(line.no_Credor)
MERGE (emp)-[:EMPENHADO_PARA]->(p);
