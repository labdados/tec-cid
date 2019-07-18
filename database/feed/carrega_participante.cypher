//carrega participante
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///participante.txt" AS line fieldterminator "|"
MATCH (l:Licitacao { 
        CodUnidadeGest: line.cd_ugestora,
        CodLicitacao: line.nu_licitacao,
        CodTipoLicitacao:line.tp_licitacao
        })
MERGE (p:Participante{ChaveParticipante: line.nu_cpfcnpj})
ON CREATE SET p.NomeParticipante = line.no_proponente
CREATE (l)-[:RECEBEU_PROPOSTA_DE{
        CodUnidadeGest: line.cd_ugestora,
        CodLicitacao: line.nu_licitacao,
        CodTipoLicitacao:line.tp_licitacao,
        QuantidadeOferdada: line.qt_ofertada, 
        ValorOfertado: line.vl_ofertado
}]->(p);
