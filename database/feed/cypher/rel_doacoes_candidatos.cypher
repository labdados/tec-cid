USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///doacoes_candidatos.csv" AS line
FIELDTERMINATOR ';'
WITH line

MATCH (d:Doador)
WHERE ((size(d.cpf_cnpj) <= 11 AND d.cpf_cnpj = ('***' + substring(line.NR_CPF_CNPJ_DOADOR, 3, 6) + '**')) OR
      (size(d.cpf_cnpj) > 11 AND d.cpf_cnpj = line.NR_CPF_CNPJ_DOADOR)) AND d.nome = toUpper(line.NM_DOADOR_RFB)

WITH line, d

MATCH (c:Candidato)
WHERE c.id = line.SQ_CANDIDATO

WITH line, d, c

MERGE (d)-[r:DOOU_PARA { id: line.LINHA }]->(c)
ON CREATE SET
        r.id = toInteger(r.id),
        r.valor_receita = toFloat(line.VR_RECEITA),
        r.tipo_receita = line.DS_ORIGEM_RECEITA,
        r.fonte_recurso = line.DS_FONTE_RECEITA,
        r.descricao_receita = line.DS_RECEITA,
        r.setor_economico_doador = line.DS_CNAE_DOADOR;