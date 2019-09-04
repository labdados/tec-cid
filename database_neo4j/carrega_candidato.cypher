//carrega candidatos
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///receita_2016.txt" AS line fieldterminator ";"
MERGE (c:Candidato {
        CPF: SUBSTRING('00000000000000', SIZE(line.CPFdocandidato)) + line.CPFdocandidato
        })
ON CREATE SET c.NumCandidato= line.Numerocandidato, c.Nome= line.Nomecandidato, c.SiglaPartido = line.SiglaPartido;