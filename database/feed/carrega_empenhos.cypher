USING PERIODIC COMMIT 50000
LOAD CSV WITH HEADERS FROM "file:///empenhos.csv" AS line

MERGE (emp:Empenho {
	cd_ugestora: line.cd_ugestora,
	numero_empenho: line.nu_Empenho,
	unidade_orcamentaria: line.de_UOrcamentaria,
	ano: line.dt_Ano
})
ON CREATE SET
	emp.funcao = line.de_Funcao,
	emp.sub_funcao = line.de_Subfuncao,
	emp.programa = line.de_Programa,
	emp.acao = line.de_Acao,
	emp.categoria_economica = line.de_CatEconomica,
	emp.natureza_despesa = line.de_NatDespesa,
	emp.modalidade = line.de_Modalidade,
	emp.cd_elemento = line.cd_elemento,
	emp.nome_elemento = line.de_Elemento,
	emp.cd_subelemento = line.cd_subelemento,
	emp.nome_subelemento = line.de_subelemento,
	emp.historico = line.de_Historico,
	emp.numero_obra = line.nu_Obra,
	emp.fonte_recursos = line.tp_FonteRecursos,
	emp.tipo_recursos = line.de_TipoRecursos,
	emp.nome_ugestora = line.de_ugestora,
	emp.data = date({
		year: toInteger(split(line.dt_empenho, "/")[2]),
		month: toInteger(split(line.dt_empenho, "/")[1]),
		day: toInteger(split(line.dt_empenho, "/")[0])
	}),
	emp.valor = toFloat(line.vl_Empenho)

MERGE (cred:Credor {
	cpf_cnpj: line.cd_credor,
	nome: line.no_Credor
})

MATCH (lic:Licitacao)
WHERE lic.numero_licitacao = line.nu_Licitacao AND
	  lic.cd_modalidade = toString(line.cd_modalidade_licitacao) AND
	  lic.cd_ugestora = line.cd_ugestora

MERGE (lic)-[:GEROU]->(emp)-[:EMPENHADO_PARA]->(cred)
