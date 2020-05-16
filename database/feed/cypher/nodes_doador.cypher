USING PERIODIC COMMIT 10000
LOAD CSV WITH HEADERS FROM "file:///doacoes_candidatos.csv" AS line
WITH line
WHERE size(line.`CPF/CNPJ do doador`) >= 11 and toUpper(line.`Nome do doador (Receita Federal)`) <> ''

WITH line, CASE WHEN size(line.`CPF/CNPJ do doador`) <= 11 OR (line.`CPF/CNPJ do doador` STARTS WITH '000' AND NOT line.`CPF/CNPJ do doador` STARTS WITH '00000000')
    THEN ('***' + substring(line.`CPF/CNPJ do doador`, size(line.`CPF/CNPJ do doador`) - 8, 6) + '**')
    ELSE line.`CPF/CNPJ do doador` END AS cpf_cnpj_doador

WITH line, cpf_cnpj_doador

MERGE (d:Doador {cpf_cnpj: cpf_cnpj_doador, nome: toUpper(line.`Nome do doador (Receita Federal)`)});