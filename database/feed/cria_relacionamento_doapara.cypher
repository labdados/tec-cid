//carrega candidatos
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///receitas_2016_PB.txt" AS line fieldterminator ";"
MATCH (p:Participante { 
        cpf_cnpj_proponente: line.CPFCNPJdodoador
        })
MATCH (c:Candidato {
        CPF: line.CPFdocandidato
        })
MERGE (p)-[:DOA_PARA{
        ValorDoado: line.Valorreceita
}]->(c);