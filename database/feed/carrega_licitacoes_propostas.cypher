USING PERIODIC COMMIT 10000
LOAD CSV WITH HEADERS FROM "file:///licitacoes_propostas.csv" AS line

MERGE (ug:UnidadeGestora { cd_ugestora: line.cd_ugestora })
ON CREATE SET 
        ug.nome = line.nome_jurisdicionado,
        ug.municipio = toUpper(line.nome_municipio),
        ug.jurisdicionado_id = line.jurisdicionado_id,
        ug.nome_tipo_jurisdicionado = line.nome_tipo_jurisdicionado,
        ug.nome_tipo_administracao_jurisdicionado = line.nome_tipo_administracao_jurisdicionado,
        ug.nome_esfera_jurisdicionado = line.nome_esfera_jurisdicionado

MERGE (lic:Licitacao {
        id_licitacao: (line.cd_ugestora + SUBSTRING('00', SIZE(line.cd_modalidade_licitacao)) +
		        line.cd_modalidade_licitacao + line.numero_licitacao)
})
ON CREATE SET
        lic.cd_ugestora = line.cd_ugestora,
        lic.cd_modalidade = line.cd_modalidade_licitacao,
        lic.numero_licitacao = line.numero_licitacao,
        lic.modalidade = line.nome_modalidade_licitacao,
        lic.objeto = line.objeto_licitacao,
        lic.valor_estimado = toFloat(line.valor_estimado_licitacao),
        lic.valor_licitado = toFloat(line.valor_licitado_licitacao),
        lic.data_homologacao = date({
                year: toInteger(split(line.data_homologacao_licitacao, "/")[2]),
                month: toInteger(split(line.data_homologacao_licitacao, "/")[1]),
                day: toInteger(split(line.data_homologacao_licitacao, "/")[0])
        }),
        lic.ano_homologacao = toInteger(line.ano_homologacao_licitacao),
        lic.situacao_fracassada = line.situacao_fracassada_licitacao,
        lic.nome_estagio_processual = line.nome_estagio_processual_licitacao,
        lic.nome_setor_atual = line.nome_setor_atual_licitacao,
        lic.url = line.url

MERGE (ug)-[:REALIZOU]->(lic)

MERGE (p:Participante{cpf_cnpj: line.cpf_cnpj_proponente})
ON CREATE SET p.nome = toUpper(line.nome_proponente)

MERGE (p)-[prop:FEZ_PROPOSTA_EM]->(lic)
ON CREATE SET
        prop.valor = toFloat(line.valor_proposta),
        prop.situacao = line.situacao_proposta;