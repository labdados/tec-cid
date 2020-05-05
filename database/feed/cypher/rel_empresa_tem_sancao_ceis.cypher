LOAD CSV WITH HEADERS FROM 'file:///ceis.csv' AS line
FIELDTERMINATOR ';'
WITH line
WHERE size(line.`CPF OU CNPJ DO SANCIONADO`) = 14

MATCH (e:Empresa {cnpj: line.`CPF OU CNPJ DO SANCIONADO`})
WITH e, line

WITH line, e, CASE WHEN line.`DATA FINAL SANÇÃO` <> ''
	THEN date({
    	year: toInteger(split(line.`DATA FINAL SANÇÃO`, "/")[2]),
        month: toInteger(split(line.`DATA FINAL SANÇÃO`, "/")[1]),
        day: toInteger(split(line.`DATA FINAL SANÇÃO`, "/")[0])
    })
    ELSE line.`DATA FINAL SANÇÃO` END AS data_final_sancao

WITH line, e, data_final_sancao
MERGE (s:Sancao {
	cadastro: 'CEIS',
    tipo_sancao: line.`TIPO SANÇÃO`,
    data_inicio: line.`DATA INÍCIO SANÇÃO`,
   	data_final: data_final_sancao
})

WITH e, s
MERGE (e)-[:TEM]-(s);