USING PERIODIC COMMIT 3000
LOAD CSV WITH HEADERS FROM "file:///socio.csv" as line

MERGE (s:Socio {cpf_cnpj: line.cnpj_cpf_do_socio})
ON CREATE SET
    s.cnpj_empresa = line.cnpj,
    s.id_socio = line.identificador_de_socio,
    s.nome = line.nome_socio,
    s.cd_qualific_socio = line.codigo_qualificacao_socio,
    s.percentual_capital = line.percentual_capital_social,
    s.data_entrada_sociedade = line.data_entrada_sociedade,
    s.cd_pais = line.codigo_pais,
    s.nome_pais = line.nome_pais_socio,
    s.cpf_rep_legal = line.cpf_representante_legal,
    s.nome_rep_legal = line.nome_representante_legal,
    s.cd_qualific_rep_legal = line.codigo_qualificacao_representante_legal


WITH line, s

MATCH (e:Empresa {cnpj: line.cnpj})

MERGE (e)-[:TEM_SOCIO]-(s);