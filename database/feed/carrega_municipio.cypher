//carrega municipios
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///jurisdicionado_sem_acento.csv" AS line fieldterminator ","
MATCH (u:UnidadeGestora { 
        cd_ugestora: line.CODIGO_SAGRES
        })
MERGE (m:Municipio {
        codigo_sagres: line.CODIGO_SAGRES
        })
ON CREATE SET m.nome_municipio = line.MUNICIPIO_IMPORTACAO
MERGE (m)-[:POSSUI]->(u);