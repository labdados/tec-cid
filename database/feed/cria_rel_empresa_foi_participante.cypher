USING PERIODIC COMMIT 3000
LOAD CSV WITH HEADERS FROM "file:///empresa_licitante_pb.csv" as line

MERGE (e:Empresa {cnpj: line.cnpj})
ON CREATE SET
	e.id_matriz_filial = line.identificador_matriz_filial,
	e.razao_social = line.razao_social,
	e.nome_fantasia = line.nome_fantasia,
	e.situacao_cadastral = line.situacao_cadastral,
	e.motivo_situacao_cadastral = line.motivo_situacao_cadastral,
	e.cd_natureza_juridica = line.codigo_natureza_juridica,
	e.data_inicio_atividade = line.data_inicio_atividade,
	e.cnae_fiscal = line.cnae_fiscal,
	e.cep = line.cep,
	e.uf = line.uf,
	e.cd_municipio = line.codigo_municipio,
	e.municipio = line.municipio,
	e.qualificacao_responsavel = line.qualificacao_do_responsavel,
	e.capital_social = line.capital_social,
	e.porte = line.porte,
	e.situacao_especial = line.situacao_especial

MERGE (e)-[:FOI]-(p:Participante {cpf_cnpj: line.cnpj})