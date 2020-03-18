USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///doacoes_candidatos.csv" AS line

MATCH (p:Participante)
WHERE (size(p.cpf_cnpj) <= 11 AND p.cpf_cnpj = ('***' + substring(line.`CPF/CNPJ do doador`, 3, 6) + '**')) OR
      (size(p.cpf_cnpj) > 11 AND p.cpf_cnpj = line.`CPF/CNPJ do doador`)

MERGE (d:Doador {cpf_cnpj: p.cpf_cnpj})
ON CREATE SET d.nome = p.nome

MERGE (p)-[:FOI]-(d);