//carrega candidatos
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///receita_2016.txt" AS line fieldterminator ";"
MATCH (p:Partido {
        SiglaPartido: line.SiglaPartido
})
MERGE (c:Candidato {
        CPFdocandidato: line.CPFdocandidato
        })
ON CREATE SET c.NumCandidato= line.Numerocandidato, c.Nome= line.Nomecandidato, c.SiglaPartido = line.SiglaPartido
MERGE (p)-[:LANÇA]->(c);

