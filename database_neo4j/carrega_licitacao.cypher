//carrega licitacoes
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///licitacao.txt" AS line fieldterminator "|"
MATCH (u:UnidadeGestora { 
      CodUnidadeGest: line.cd_ugestora,         
      NomeUnidadeGest: line.de_ugestora
       })
MERGE (l:Licitacao{
        CodUnidadeGest: line.cd_ugestora,
        CodLicitacao: line.nu_Licitacao,
        CodTipoLicitacao: line.tp_Licitacao
})
ON CREATE SET l.TipoLicitacao = line.de_TipoLicitacao, 
        l.Data = line.dt_Homologacao,
        l.CodObj = line.tp_Objeto, 
        l.NomeObg = line.de_TipoObjeto, 
        l.Valor = line.vl_Licitacao, 
        l.Obs = line.de_Obs
CREATE (u)-[:REALIZOU]->(l);

