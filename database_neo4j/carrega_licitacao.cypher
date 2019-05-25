//carrega licitação
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///licitacao.txt" AS line fieldterminator "|"
create (:Licitacao {CodUnidadeGest: line.cd_ugestora, NomeUnidadeGest: line.de_ugestora, CodLicitacao: line.nu_Licitacao, CodTipoLicitacao: line.tp_Licitacao, TipoLicitacao: line.de_TipoLicitacao, Data: line.dt_Homologacao, CodObj: line.tp_Objeto, NomeObg: line.de_TipoObjeto, Valor: line.vl_Licitacao, Obs: line.de_Obs});
