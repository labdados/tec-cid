MATCH (participante:Participante)
MERGE (licitacao:Licitação {CodLicitacao: participante.pCodLicitacao, CodTipoLicitacao: participante.pCodTipoLicitacao, CodUnidadeGest: participante.pCodUnidadeGest})
MERGE (participante)-[r:Participou]->(licitacao)
RETURN participante.pNome
