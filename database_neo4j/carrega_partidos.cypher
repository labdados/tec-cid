//carrega partidos
//USING PERIODIC COMMIT
//LOAD CSV WITH HEADERS FROM "file:///receita_2016.txt" AS line fieldterminator ";"
//MERGE (p: {
//        CPF: line.CPFdocandidato
//        })
//ON CREATE SET c.NumCandidato= line.Numerocandidato, c.Nome= line.Nomecandidato, c.SiglaPartido=line.SiglaPartido;