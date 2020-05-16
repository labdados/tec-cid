MATCH (c:Candidato)
WITH c 

MERGE (p:Pessoa {cpf: '***' + substring(c.cpf, 3, 6) + '**', nome: c.nome})
WITH c, p

MERGE (p)-[:FOI]-(c);