MATCH (p:Participante)-[:Participou]->(l:Licitacao)<-[:Participou]-(p2:Participante)
WHERE p <> p2
RETURN DISTINCT p.NomeParticipante, p2.NomeParticipante, COUNT(l);
