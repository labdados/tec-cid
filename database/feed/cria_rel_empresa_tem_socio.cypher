MATCH (e:Empresa), (s:Socio) WHERE e.cnpj = s.cnpj_empresa
WITH e, s
MERGE (e)-[:TEM_SOCIO]-(s);