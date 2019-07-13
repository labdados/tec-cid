//carrega candidatos
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///receita_2016.txt" AS line fieldterminator ";"
MATCH (p:Partido {
        SiglaPartido: line.SiglaPartido
})
MATCH (c:Candidato {
        CPF: line.CPFdocandidato
        })
MERGE (p)-[:LANÇA]->(c);

