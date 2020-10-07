LOAD CSV WITH HEADERS FROM 'file:///cnep.csv' AS line
FIELDTERMINATOR ';'
WITH line
WHERE size(line.`CPF OU CNPJ DO SANCIONADO`) = 14

MATCH (e:Empresa {cnpj: line.`CPF OU CNPJ DO SANCIONADO`})
WITH line, e

WITH line, e, CASE WHEN line.`DATA INÍCIO SANÇÃO` <> ''
    THEN date({
        year: toInteger(split(line.`DATA INÍCIO SANÇÃO`, "/")[2]),
        month: toInteger(split(line.`DATA INÍCIO SANÇÃO`,"/")[1]),
        day: toInteger(split(line.`DATA INÍCIO SANÇÃO`,"/")[0])
    })
    ELSE line.`DATA INÍCIO SANÇÃO` END AS data_inicio_sancao

WITH line, e, data_inicio_sancao, CASE WHEN line.`DATA FINAL SANÇÃO` <> ''
	THEN date({
    	year: toInteger(split(line.`DATA FINAL SANÇÃO`, "/")[2]),
        month: toInteger(split(line.`DATA FINAL SANÇÃO`, "/")[1]),
        day: toInteger(split(line.`DATA FINAL SANÇÃO`, "/")[0])
    })
    ELSE line.`DATA FINAL SANÇÃO` END AS data_final_sancao

WITH line, e, data_inicio_sancao, data_final_sancao
MERGE (s:Sancao {
	cadastro: 'CNEP',
    tipo_sancao: line.`TIPO SANÇÃO`,
    data_inicio: data_inicio_sancao,
   	data_final: data_final_sancao
})

WITH e, s
MERGE (e)-[:TEM]->(s);