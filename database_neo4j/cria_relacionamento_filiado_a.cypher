//carrega candidatos
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///receita_2016.txt" AS line fieldterminator ";"
MATCH (p:Partido {
        SiglaPartido: line.SiglaPartido
})
MATCH (c:Candidato {
        CPF: SUBSTRING('00000000000000', SIZE(line.CPFdocandidato)) + line.CPFdocandidato
        })
MERGE (c)-[:FILIADO_A]->(p);

