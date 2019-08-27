MATCH (participante:Participante)
MERGE (licitacao:Licitacao {CodLicitacao: participante.pCodLicitacao, CodTipoLicitacao: participante.pCodTipoLicitacao, CodUnidadeGest: participante.pCodUnidadeGest})
MERGE (participante)-[r:Participou]->(licitacao)
RETURN participante.pNome;
