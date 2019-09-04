//carrega candidatos
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///receita_2016.txt" AS line fieldterminator ";"
MATCH (p:Participante { 
        ChaveParticipante: SUBSTRING('00000000000000', SIZE(line.CPFCNPJdodoador)) + line.CPFCNPJdodoador
        })
MATCH (c:Candidato {
        CPF: SUBSTRING('00000000000000', SIZE(line.CPFdocandidato)) + line.CPFdocandidato
        })
MERGE (p)-[:DOA_PARA{
        ValorDoado: line.Valorreceita
}]->(c);