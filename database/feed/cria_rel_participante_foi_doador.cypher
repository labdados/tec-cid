USING PERIODIC COMMIT 10000
LOAD CSV WITH HEADERS FROM "file:///doacoes_candidatos.csv" AS line
WITH line
WHERE size(line.`CPF/CNPJ do doador`) >= 11

MERGE (d:Doador {cpf_cnpj: line.`CPF/CNPJ do doador`})
ON CREATE SET d.nome = line.`Nome do doador`