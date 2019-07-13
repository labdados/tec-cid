//carrega partidos
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///prefeito_sem_acento.csv" AS line fieldterminator ","
MERGE (p:Partido {
        SiglaPartido: line.SIGLA_PARTIDO
        })
ON CREATE SET p.NumeroPartido= line.NUMERO_PARTIDO;