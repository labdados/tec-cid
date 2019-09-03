#!/bin/bash

cat cria_index_licitacao.cypher | cypher-shell -u neo4j -p neo4jpass --format plain
cat cria_index_participante.cypher | cypher-shell -u neo4j -p neo4jpass --format plain	
cat cria_index_unidade_gestora.cypher | cypher-shell -u neo4j -p neo4jpass --format plain	
cat carrega_unidade_gestora.cypher | cypher-shell -u neo4j -p neo4jpass --format plain
cat carrega_licitacao.cypher | cypher-shell -u neo4j -p neo4jpass --format plain
cat carrega_participante.cypher | cypher-shell -u neo4j -p neo4jpass --format plain
cat carrega_partido.cypher | cypher-shell -u neo4j -p neo4jpass --format plain
cat carrega_candidato.cypher | cypher-shell -u neo4j -p neo4jpass --format plain
cat carrega_municipio.cypher | cypher-shell -u neo4j -p neo4jpass --format plain
cat cria_relacionamento_governa.cypher | cypher-shell -u neo4j -p neo4jpass --format plain
cat cria_relacionamento_lança.cypher | cypher-shell -u neo4j -p neo4jpass --format plain
cat cria_relacionamento_doapara.cypher | cypher-shell -u neo4j -p neo4jpass 