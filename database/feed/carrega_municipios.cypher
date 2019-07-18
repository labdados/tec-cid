//carrega municipios
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///jurisdicionado.csv" AS line fieldterminator ","
MATCH (u:UnidadeGestora { 
        CodUnidadeGest: line.codigo_sagres
        })
MERGE (m:Municipio {
        codigo_sagres: line.codigo_sagres
        })
ON CREATE SET m.municipio_importacao= line.municipio_importacao
CREATE (m)-[:POSSUI]->(u);