//carrega candidatos
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///receita_2016.txt" AS line fieldterminator ";"
MATCH (p:Participante { 
        ChaveParticipante: toInteger(line.CPFCNPJdodoador)
        })
MERGE (c:Candidato {
        CPF: line.CPFdocandidato
        })
ON CREATE SET c.NumCandidato= line.Numerocandidato, c.Nome= line.Nomecandidato, c.SiglaPartido = line.SiglaPartido
MERGE (p)-[:DOA_PARA{
        ValorDoado: line.Valorreceita
}]->(c);