//carrega candidatos
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///receitas_2016_PB.txt" AS line fieldterminator ";"
MATCH (p:Partido {
        SiglaPartido: line.SiglaPartido
})
MATCH (c:Candidato {
        CPF: line.CPFdocandidato
        })
MERGE (p)-[:FILIADO_A]->(c);

