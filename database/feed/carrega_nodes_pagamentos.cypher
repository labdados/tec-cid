USING PERIODIC COMMIT 2000
LOAD CSV WITH HEADERS FROM "file:///pagamentos.csv" AS line

MERGE (pag:Pagamento {
	id_empenho: (line.cd_UGestora + line.dt_Ano + line.nu_Empenho),
	numero_parcela: line.nu_Parcela,
	valor_pagto: line.vl_Pagamento,
	data_pagto: date({
		year: toInteger(split(line.dt_pagamento, "/")[2]),
		month: toInteger(split(line.dt_pagamento, "/")[1]),
		day: toInteger(split(line.dt_pagamento, "/")[0])
	}),
	cd_conta: line.cd_Conta
}) 
ON CREATE SET
	pag.desc_ugestora = line.de_ugestora,
	pag.desc_uorcamentaria = line.de_UOrcamentaria,
	pag.numero_agencia = line.cd_agencia,
	pag.numero_cheque = line.nu_Chequepag,
	pag.valor_retencao = toFloat(line.vl_Retencao),
	pag.tipo_conta = line.tp_contabancaria,
	pag.desc_tipo_conta= line.de_contabancaria,
	pag.desc_conta = line.de_conta