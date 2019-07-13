#!/bin/bash
cat deleta_todos_nos.cypher | cypher-shell -u neo4j -p tcctcc --format plain
rm /storage/neo4j/import/licitacao.txt
rm /storage/neo4j/import/participante.txt

wget -O licitacao.txt.gz https://dados.tce.pb.gov.br/TCE-PB-SAGRES-Licitacao_Esfera_Municipal.txt.gz;
wget -O participante.txt.gz https://dados.tce.pb.gov.br/TCE-PB-SAGRES-Propostas_Licitacao_Esfera_Municipal.txt.gz;

gunzip licitacao.txt.gz
gunzip participante.txt.gz
sed -i 's/"/ /g' licitacao.txt 
sed -i "s/\r//g" licitacao.txt
mv licitacao.txt /storage/neo4j/import/
mv participante.txt /storage/neo4j/import/

cat carrega_unidade_gestora.cypher | cypher-shell -u neo4j -p tcctcc --format plain
cat carrega_licitacao.cypher | cypher-shell -u neo4j -p tcctcc --format plain
cat carrega_participante.cypher | cypher-shell -u neo4j -p tcctcc --format plain

 
