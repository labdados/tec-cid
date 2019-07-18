#!/bin/bash

# if env variables do not exist, use default values
${NEO4J_DIR_IMPORT:="../import"}
${NEO4J_USERNAME:="neo4j"}
${NEO4J_PASSWORD:="neo4j"}

curl -o $NEO4J_DIR_IMPORT/licitacao.txt.gz https://dados.tce.pb.gov.br/TCE-PB-SAGRES-Licitacao_Esfera_Municipal.txt.gz
curl -o $NEO4J_DIR_IMPORT/participante.txt.gz https://dados.tce.pb.gov.br/TCE-PB-SAGRES-Propostas_Licitacao_Esfera_Municipal.txt.gz

mv $NEO4J_DIR_IMPORT/licitacao.txt $NEO4J_DIR_IMPORT/licitacao.txt.bkp
mv $NEO4J_DIR_IMPORT/participante.txt $NEO4J_DIR_IMPORT/participante.txt.bkp

gunzip $NEO4J_DIR_IMPORT/licitacao.txt.gz
gunzip $NEO4J_DIR_IMPORT/participante.txt.gz

sed -i -e 's/"/ /g' -e 's/\r//g' $NEO4J_DIR_IMPORT/licitacao.txt 

cypher-shell -u $NEO4J_USERNAME -p $NEO4J_PASSWORD < cria_index_licitacao.cypher
cypher-shell -u $NEO4J_USERNAME -p $NEO4J_PASSWORD < cria_index_participante.cypher
cypher-shell -u $NEO4J_USERNAME -p $NEO4J_PASSWORD < cria_index_unidade_gestora.cypher
cypher-shell -u $NEO4J_USERNAME -p $NEO4J_PASSWORD < carrega_unidade_gestora.cypher
cypher-shell -u $NEO4J_USERNAME -p $NEO4J_PASSWORD < carrega_licitacao.cypher
cypher-shell -u $NEO4J_USERNAME -p $NEO4J_PASSWORD < carrega_participante.cypher
