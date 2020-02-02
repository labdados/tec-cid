USING PERIODIC COMMIT 2000
LOAD CSV WITH HEADERS FROM "file:///empresa.csv.gz" as line

MATCH (p:Participante)
		WHERE (p.cpf_cnpj = line.cnpj)
MERGE (e:Empresa {cnpj: line.cnpj})
ON CREATE SET
	e.id_matriz_filial = toInteger(line.identificador_matriz_filial),
	e.razao_social = line.razao_social,
	e.nome_fantasia = line.nome_fantasia,
	e.situacao_cadastral = line.situacao_cadastral,
	e.data_situacao_cadastral =  line.data_situacao_cadastral,
	e.motivo_situacao_cadastral = line.motivo_situacao_cadastral,
	e.nome_cidade_exterior = line.nome_cidade_exterior,
	e.cd_natureza_juridica = toInteger(line.codigo_natureza_juridica),
	e.data_inicio_atividade = date({
		year: toInteger(split(line.data_inicio_atividade, "-")[0]),
		month: toInteger(split(line.data_inicio_atividade, "-")[1]),
		day: toInteger(split(line.data_inicio_atividade, "-")[2])
	}),
	e.cnae_fiscal = toInteger(line.cnae_fiscal),
	e.desc_tipo_logradouro = line.descricao_tipo_logradouro,
	e.logradouro = line.logradouro,
	e.numero = line.numero,
	e.complemento = line.complemento,
	e.bairro = line.bairro,
	e.cep = toInteger(line.cep),
	e.uf = line.uf,
	e.cd_municipio = line.codigo_municipio,
	e.municipio = line.municipio,
	e.ddd_telefone_1 = line.ddd_telefone_1,
	e.ddd_telefone_2 = line.ddd_telefone_2,
	e.ddd_fax = line.ddd_fax,
	e.qualificacao_responsavel = line.qualificacao_do_responsavel,
	e.capital_social = line.capital_social,
	e.porte = line.porte,
	e.opcao_pelo_simples = line.opcao_pelo_simples,
	e.data_opcao_pelo_simples = line.data_opcao_pelo_simples,
	e.data_exclusao_pelo_simples = line.data_exclusao_pelo_simples,
	e.opcao_pelo_mei = line.opcao_pelo_mei,
	e.situacao_especial = line.situacao_especial,
	e.data_situacao_especial = line.data_situacao_especial

WITH p, e
MERGE (e)-[:FOI]-(p)