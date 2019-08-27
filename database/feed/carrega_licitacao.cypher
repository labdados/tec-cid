//carrega licitacoes
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///licitacao.txt" AS line fieldterminator "|"
MATCH (u:UnidadeGestora { 
      CodUnidadeGest: line.cd_ugestora
       })
MERGE (l:Licitacao{
        CodUnidadeGest: line.cd_ugestora,
        CodLicitacao: line.nu_Licitacao,
        CodTipoLicitacao: line.tp_Licitacao
})
ON CREATE SET
        l.TipoLicitacao = line.de_TipoLicitacao, 
        l.Data = date({year: toInt(split(line.dt_Homologacao, "/")[2]),
                       month: toInt(split(line.dt_Homologacao, "/")[1]),
                       day: toInt(split(line.dt_Homologacao, "/")[0])
                      }),
        l.CodObj = line.tp_Objeto, 
        l.NomeObg = line.de_TipoObjeto, 
        l.Valor = toFloat(line.vl_Licitacao),
        l.Obs = line.de_Obs
MERGE (u)-[:REALIZOU]->(l);

