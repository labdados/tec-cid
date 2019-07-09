//carrega municipios
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///jurisdicionado.csv" AS line fieldterminator ","
MATCH (u:UnidadeGestora { 
        CodUnidadeGest: line.codigo_sagres
        })
MERGE (m:Municipio {
        Codigo: line.codigo_sagres
        })
ON CREATE SET m.Nome= line.municipio_importacao
CREATE (m)-[:POSSUI]->(u);