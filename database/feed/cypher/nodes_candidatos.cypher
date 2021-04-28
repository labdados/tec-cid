USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///candidatos.csv" AS line
FIELDTERMINATOR ';'

MERGE (cand:Candidato { id: line.SQ_CANDIDATO })
ON CREATE SET 
        cand.cpf = line.NR_CPF_CANDIDATO,
        cand.cd_eleicao = line.CD_ELEICAO,
        cand.tipo_eleicao = line.CD_TIPO_ELEICAO,
        cand.ano_eleicao = toInteger(line.ANO_ELEICAO),
        cand.uf = line.SG_UF,
        cand.municipio = line.NM_UE,
        cand.unidade_estadual = line.SG_UE,
        cand.nome = line.NM_CANDIDATO,
        cand.nome_urna = line.NM_URNA_CANDIDATO,
        cand.numero = line.NR_CANDIDATO,
        cand.sigla_partido = line.SG_PARTIDO,
        cand.coligacao = line.DS_COMPOSICAO_COLIGACAO,
        cand.cargo = line.DS_CARGO,
        cand.situacao = line.DS_SIT_TOT_TURNO,
        cand.data_nascimento = line.DT_NASCIMENTO,
        cand.titulo_eleitoral = line.NR_TITULO_ELEITORAL_CANDIDATO,
        cand.genero = line.DS_GENERO,
        cand.grau_instrucao = line.DS_GRAU_INSTRUCAO,
        cand.raca = line.DS_COR_RACA,
        cand.ocupacao = line.DS_OCUPACAO

MERGE (part:Partido { sigla: line.SG_PARTIDO })
ON CREATE SET
        part.numero = line.NR_PARTIDO,
        part.nome = line.NM_PARTIDO

MERGE (cand)-[:FILIADO_A]->(part)

WITH cand
WHERE cand.situacao = "ELEITO" and cand.cargo = "PREFEITO"
MATCH (mun:Municipio)
WHERE mun.nome = cand.municipio
MERGE (cand)-[:GOVERNA]->(mun);