// O score mínimo do fulltext.queryNodes escolhido foi 1.3, 
// após realizarmos comparações manuais entre os sócios que eram doadores 
// e que possuiam uma variação no nome, mas que eram a mesma pessoa.
//
// OBS.: O menor score do sócio doador com nome um pouco diferente mas que é a mesma
// pessoa foi 1.541, já o sócio doador com nome um pouco diferente mas que 
// não é a mesma pessoa foi 0.925

WITH "MATCH (s:Socio) 
    WITH s

    MATCH (d:Doador)
    WHERE s.cpf_cnpj = d.cpf_cnpj AND s.nome <> d.nome
    WITH s, d

    CALL db.index.fulltext.queryNodes('nome_doador', s.nome) YIELD node as doador, score as total
    WHERE total >= 1.3 AND doador.cpf_cnpj = s.cpf_cnpj AND doador.nome <> s.nome

    WITH s, d, doador, total
    RETURN s.nome AS nome_socio, s.cpf_cnpj AS cpf_cnpj_socio, d.nome AS nome_doador, d.cpf_cnpj AS cpf_cnpj_doador" AS query

CALL apoc.export.csv.query(query, "socios_doadores_com_nomes_distintos.csv", {})

YIELD file, nodes, properties, data
RETURN file, nodes, properties, data
