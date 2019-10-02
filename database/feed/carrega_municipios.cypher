//carrega municipios
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///localidade.csv" AS line
WITH line
WHERE line.uf = "Paraíba"

MERGE (m:Municipio { id: line.id })
ON CREATE SET
    m.uf = line.uf,
    m.nome = toUpper(line.nome),
    m.mesoregiao = line.mesoregiao,
    m.microregiao = line.microregiao,
    m.codigo_ibge = line.codigo_ibge,
    m.codigo_siaf = line.codigo_siaf,
    m.link_ibge = line.link_ibge,
    m.bandeira = line.bandeira,
    m.brasao = line.brasao,
    m.link_wikipedia = line.link_wikipedia,
    m.esfera = line.esfera,
    m.cancelled = line.cancelled

WITH m
MATCH (ug:UnidadeGestora)
WHERE m.nome = ug.municipio
MERGE (ug)-[:PERTENCE_A]->(m);