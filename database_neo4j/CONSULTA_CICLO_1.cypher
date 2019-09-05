match p=(x:Participante)<-[:RECEBEU_PROPOSTA_DE]-(:Licitacao)<-[:REALIZOU]-(:UnidadeGestora)<-[POSSUI]-(:Municipio)<-[:GOVERNA]-(:Candidato)<-[:DOA_PARA]-(x:Participante) return COUNT(p)
