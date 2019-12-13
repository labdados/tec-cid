USING PERIODIC COMMIT 300
LOAD CSV WITH HEADERS FROM "file:///pagamentos.csv" AS line

MERGE (pag:Pagamento {
	numero_empenho: line.nu_Empenho,
	numero_agencia: line.cd_agencia,
	numero_conta: line.cd_Conta
}) 
ON CREATE SET
	pag.numero_parcela = line.nu_Parcela,
	pag.numero_agencia = line.cd_agencia,
	pag.numero_cheque = line.nu_Chequepag,
	pag.valor_retencao = toFloat(line.vl_Retencao),
	pag.tipo_conta = line.tp_contabancaria,
	pag.desc_tipo_conta= line.de_contabancaria,
	pag.desc_conta = line.de_conta


MERGE (ug:UnidadeGestora {cd_ugestora: line.cd_UGestora})
ON CREATE SET
	ug.nome = line.de_ugestora,
	ug.nome_uorcamentaria = line.de_UOrcamentaria

MERGE (ug)-[transac:REALIZA]->(pag)
ON CREATE SET
	transac.ano = line.dt_Ano,
	transac.valor_pagto = toFloat(line.vl_Pagamento),
	transac.data_pagto = date({
		year: toInteger(split(line.dt_pagamento, "/")[2]),
		month: toInteger(split(line.dt_pagamento, "/")[1]),
		day: toInteger(split(line.dt_pagamento, "/")[0])
	})