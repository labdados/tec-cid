LOAD CSV WITH HEADERS FROM 'file:///cepim.csv' AS line
FIELDTERMINATOR ';'
WITH line
WHERE size(line.`CNPJ ENTIDADE`) = 14

MATCH (e:Empresa {cnpj: line.`CNPJ ENTIDADE`})
WITH e, line

MERGE (s:Sancao {
	cadastro: 'CEPIM',
    motivo_impedimento: line.`MOTIVO DO IMPEDIMENTO`
})

WITH e, s
MERGE (e)-[:TEM]->(s);