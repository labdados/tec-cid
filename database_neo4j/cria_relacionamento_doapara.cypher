//carrega candidatos
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///receita_2016.txt" AS line fieldterminator ";"
MATCH (p:Participante { 
        ChaveParticipante: toInteger(line.CPFCNPJdodoador)
        })
MATCH (c:Candidato {
        CPF: toInteger(line.CPFdocandidato)
        })
MERGE (p)-[:DOA_PARA{
        ValorDoado: line.Valorreceita
}]->(c);