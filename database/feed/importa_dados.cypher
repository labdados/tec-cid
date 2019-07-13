USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///dados/licitacao.txt" AS line fieldterminator "|"
create (:Licitação {CodUnidadeGest: line.cd_ugestora, NomeUnidadeGest: line.de_ugestora, CodLicitacao: line.nu_Licitacao, CodTipoLicitacao: line.tp_Licitacao, TipoLicitacao: line.de_TipoLicitacao, Data: line.dt_Homologacao, CodObj: line.tp_Objeto, NomeObg: line.de_TipoObjeto, Valor: line.vl_Licitacao, Obs: line.de_Obs})

USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///dados/participante.txt" AS line fieldterminator "|"
create (:Participante {pCodUnidadeGest: line.cd_ugestora, pNome: line.de_ugestora,pCodLicitacao: line.nu_licitacao,pCodTipoLicitacao:line.tp_licitacao,pNomeTipo:line.de_tipolicitacao,ChaveParticipante:line.nu_cpfcnpj,NomeParticipante:line.no_participante})


MATCH (participante:Participante)
MERGE (licitacao:Licitação {CodLicitacao: participante.pCodLicitacao, CodTipoLicitacao: participante.pCodTipoLicitacao, CodUnidadeGest: participante.pCodUnidadeGest})
MERGE (participante)-[r:Participou]->(licitacao)
RETURN participante.pNome
