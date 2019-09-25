USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///prefeitos_2016_PB.csv" AS line
MATCH (c:Candidato{
        nome: line.NOME_CANDIDATO
})
MATCH (m:Municipio{
        nome_municipio: line.NOME_MUNICIPIO
})
MERGE (c)-[:GOVERNA]->(m);