match p=(x:Participante)-[:DOA_PARA]->(c1:Candidato)-[:FILIADO_A]->(:Partido)<-[:FILIADO_A]-(c2:Candidato)-[:GOVERNA]->(:Municipio)-[:POSSUI]->(:UnidadeGestora)-[:REALIZOU]->(:Licitacao)-[:RECEBEU_PROPOSTA_DE]->(x:Participante)
where c1 <> c2
return p