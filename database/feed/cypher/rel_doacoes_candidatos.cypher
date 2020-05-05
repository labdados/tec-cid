USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///doacoes_candidatos.csv" AS line

MATCH (d:Doador)
WHERE (size(d.cpf_cnpj) <= 11 AND d.cpf_cnpj = ('***' + substring(line.`CPF/CNPJ do doador`, 3, 6) + '**')) OR
      (size(d.cpf_cnpj) > 11 AND d.cpf_cnpj = line.`CPF/CNPJ do doador`)
MATCH (c:Candidato)
WHERE c.id =  line.`Sequencial Candidato`
MERGE (d)-[r:DOOU_PARA { id: line.Linha }]->(c)
ON CREATE SET
        r.valor_receita = toFloat(line.`Valor receita`),
        r.tipo_receita = line.`Tipo receita`,
        r.fonte_recurso = line.`Fonte recurso`,
        r.descricao_receita = line.`Descricao da receita`,
        r.setor_economico_doador = line.`Setor econômico do doador`;