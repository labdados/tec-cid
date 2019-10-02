#!/bin/bash

# if env variables do not exist, use default values
NEO4J_USERNAME=${NEO4J_USERNAME:-"neo4j"}
NEO4J_PASSWORD=${NEO4J_PASSWORD:-"neo4jpass"}

echo $NEO4J_USERNAME/$NEO4J_PASSWORD

cypher-shell -u $NEO4J_USERNAME -p $NEO4J_PASSWORD < cria_index_licitacao.cypher
cypher-shell -u $NEO4J_USERNAME -p $NEO4J_PASSWORD < cria_index_participante.cypher
cypher-shell -u $NEO4J_USERNAME -p $NEO4J_PASSWORD < cria_index_unidade_gestora.cypher
cypher-shell -u $NEO4J_USERNAME -p $NEO4J_PASSWORD < carrega_licitacao_proposta.cypher
cypher-shell -u $NEO4J_USERNAME -p $NEO4J_PASSWORD < carrega_partido.cypher
cypher-shell -u $NEO4J_USERNAME -p $NEO4J_PASSWORD < carrega_candidato.cypher
cypher-shell -u $NEO4J_USERNAME -p $NEO4J_PASSWORD < carrega_municipio.cypher
cypher-shell -u $NEO4J_USERNAME -p $NEO4J_PASSWORD < cria_relacionamento_governa.cypher 
cypher-shell -u $NEO4J_USERNAME -p $NEO4J_PASSWORD < cria_relacionamento_lança.cypher
cypher-shell -u $NEO4J_USERNAME -p $NEO4J_PASSWORD < cria_relacionamento_doapara.cypher

