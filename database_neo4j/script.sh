#!/bin/bash
rm /storage/neo4j/import/licitacao.txt
rm /storage/neo4j/import/participante.txt

wget -O licitacao.txt.gz https://dados.tce.pb.gov.br/TCE-PB-SAGRES-Licitacao_Esfera_Municipal.txt.gz;
wget -O participante.txt.gz https://dados.tce.pb.gov.br/TCE-PB-SAGRES-Participantes_Licitacao_Esfera_Municipal.txt.gz;

gunzip licitacao.txt.gz
gunzip participante.txt.gz
sed 's/"/ /g' licitacao.txt >> semaspas.txt
mv semaspas.txt licitacao.txt
mv licitacao.txt /storage/neo4j/import/
mv participante.txt /storage/neo4j/import/

cat cria_index_licitacao.cypher | cypher-shell -u neo4j -p tcctcc --format plain
cat cria_index_participante.cypher | cypher-shell -u neo4j -p tcctcc --format plain
cat carrega_licitacao.cypher | cypher-shell -u neo4j -p tcctcc --format plain
cat carrega_participante.cypher | cypher-shell -u neo4j -p tcctcc --format plain

 
