USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///doacoes_candidatos.csv" AS line

MATCH (p:Participante)
WHERE (size(p.cpf_cnpj) <= 11 AND p.cpf_cnpj = ('***' + substring(line.`CPF/CNPJ do doador`, 3, 6) + '**')) OR
      (size(p.cpf_cnpj) > 11 AND p.cpf_cnpj = line.`CPF/CNPJ do doador`)
MATCH (c:Candidato)
WHERE c.cpf =  line.`CPF do candidato` AND c.cd_eleicao = line.`Cód. Eleição`
MERGE (p)-[d:DOOU_PARA { id: line.Linha }]->(c)
ON CREATE SET
        d.valor_receita = toFloat(line.`Valor receita`),
        d.tipo_receita = line.`Tipo receita`,
        d.fonte_recurso = line.`Fonte recurso`,
        d.descricao_receita = line.`Descricao da receita`,
        d.setor_economico_doador = line.`Setor econômico do doador`;