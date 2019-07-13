//carrega unidade gestora
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///licitacao.txt" AS line fieldterminator "|"
MERGE (u:UnidadeGestora {
        CodUnidadeGest: line.cd_ugestora
        })
ON CREATE SET u.NomeUnidadeGest = line.de_ugestora;