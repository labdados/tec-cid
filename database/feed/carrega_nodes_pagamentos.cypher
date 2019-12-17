USING PERIODIC COMMIT 2000
LOAD CSV WITH HEADERS FROM "file:///pagamentos.csv" AS line

CREATE (pag:Pagamento {
	id_empenho: (line.cd_UGestora + line.dt_Ano + line.nu_Empenho),
	numero_parcela: line.nu_Parcela,
	valor_pagto: line.vl_Pagamento,
	data_pagto: date({
		year: toInteger(split(line.dt_pagamento, "/")[2]),
		month: toInteger(split(line.dt_pagamento, "/")[1]),
		day: toInteger(split(line.dt_pagamento, "/")[0])
	}),
	cd_conta: line.cd_Conta,
	desc_ugestora: line.de_ugestora,
	desc_uorcamentaria: line.de_UOrcamentaria,
	numero_agencia: line.cd_agencia,
	numero_cheque: line.nu_Chequepag,
	valor_retencao: toFloat(line.vl_Retencao,
	tipo_conta: line.tp_contabancaria,
	desc_tipo_conta: line.de_contabancaria,
	desc_conta: line.de_conta
})