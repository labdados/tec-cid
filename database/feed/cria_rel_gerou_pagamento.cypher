USING PERIODIC COMMIT 2000
LOAD CSV WITH HEADERS FROM "file:///pagamentos.csv" AS line
WITH line


MATCH (emp:Empenho {
    id_empenho: (line.cd_UGestora + line.dt_Ano + line.nu_Empenho)
})-[:EMPENHADO_PARA]-(part:Participante)

MATCH (pag:Pagamento {
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

WITH emp, pag, part
CREATE (emp)-[:GEROU]-(pag)-[:PARA]-(part);