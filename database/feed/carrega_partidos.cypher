//carrega partidos
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///prefeitos_eleitos_pb_2016.csv" AS line fieldterminator ","
MERGE (p:Partido {
        SiglaPartido: line.SIGLA_PARTIDO
        })
ON CREATE SET p.NumeroPartido= line.NUMERO_PARTIDO;