USING PERIODIC COMMIT 200
LOAD CSV WITH HEADERS FROM "file:///empenhos.csv" AS line

MERGE (emp:Empenho {
	cd_ugestora: line.cd_ugestora,
	numero_licitacao: line.nu_Licitacao,
	numero_empenho: line.nu_Empenho
})
ON CREATE SET
	emp.ano = line.dt_Ano,
	emp.unidade_orcamentaria = line.de_UOrcamentaria,
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
	emp.data = date({
		year: toInteger(split(line.dt_empenho, "/")[2]),
		month: toInteger(split(line.dt_empenho, "/")[1]),
		day: toInteger(split(line.dt_empenho, "/")[0])
	}),		
	emp.historico = line.de_Historico,
	emp.numero_obra = line.nu_Obra,
	emp.fonte_recursos = line.tp_FonteRecursos,
	emp.tipo_recursos = line.de_TipoRecursos


MERGE (ug:UnidadeGestora {cd_ugestora: line.cd_ugestora})
ON CREATE SET
	ug.nome = line.de_ugestora

MERGE (lic:Licitacao {
	cd_ugestora: line.cd_ugestora,
	numero_licitacao: line.nu_Licitacao,
	tipo: line.de_tipolicitacao
})

MERGE (cred:Credor {
	cpf_cnpj: line.cd_credor,
	nome: line.no_Credor
})


MERGE (ug)-[:REALIZA_EMPENHO]->(lic)

MERGE (cred)-[transac:VENCE]->(emp)
ON CREATE SET
	transac.valor = toFloat(line.vl_Empenho)