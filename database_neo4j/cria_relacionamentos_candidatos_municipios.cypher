USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///prefeitos_eleitos_pb_2016.csv" AS line fieldterminator ","
MATCH (c:Candidato { 
        Nome: line.codigo_sagres
        })