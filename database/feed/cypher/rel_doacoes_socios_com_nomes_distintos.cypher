// Foi utilizado o algoritmo de Jaccard para calcular a similaridade dos nomes
// dos sócios doadores que possuem o mesmo CPF e nomes diferentes que são a mesma pessoa.
// Para um relacionamento (Socio)-[:FOI]-(Doador) ser criado, o valor da similaridade dos nomes deverá ser superior a 0.5
MATCH (s:Socio)
WITH s

MATCH (d:Doador)
WHERE s.cpf_cnpj = d.cpf_cnpj AND s.nome <> d.nome AND split(s.nome, ' ')[0] = split(d.nome, ' ')[0]
WITH s, d, toFloat(size(apoc.coll.intersection(split(s.nome, ' '), split(d.nome, ' ')))) / toFloat(size(apoc.coll.union(split(s.nome, ' '), split(d.nome, ' ')))) AS similarity
WHERE similarity > 0.5
WITH s, d

MERGE (s)-[:FOI]->(d);
