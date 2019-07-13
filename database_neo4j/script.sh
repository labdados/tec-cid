#!/bin/bash
storage=/storage/neo4j/import/

rm $storage/licitacao.txt
rm $storage/participante.txt
rm $storage/receita_2016.txt
rm $storage/prefeito_sem_acento.csv

wget -O licitacao.txt.gz https://dados.tce.pb.gov.br/TCE-PB-SAGRES-Licitacao_Esfera_Municipal.txt.gz;
wget -O participante.txt.gz https://dados.tce.pb.gov.br/TCE-PB-SAGRES-Propostas_Licitacao_Esfera_Municipal.txt.gz;
wget -O grande.zip http://agencia.tse.jus.br/estatistica/sead/odsele/prestacao_contas/prestacao_contas_relatorio_financeiro_2016.zip;
wget -O prefeitos_eleitos_pb_2016.csv https://raw.githubusercontent.com/StewenAscari/tcc-licitacoes-doacoes/master/dados/prefeitos_eleitos_pb_2016.csv;

gunzip licitacao.txt.gz
gunzip participante.txt.gz
unzip -p grande.zip receitas_candidatos_relatorio_financeiro_2016_PB.txt > receita.txt
iconv -f UTF8 -t ASCII//TRANSLIT < prefeitos_eleitos_pb_2016.csv > prefeito_sem_acento.csv
iconv --from latin1 --to-code utf-8 receita.txt > receitas.txt
iconv -f UTF8 -t ASCII//TRANSLIT < receitas.txt > receita_2016.txt
sed -i '1s/\///g' receita_2016.txt
sed -i '1s/ //g' receita_2016.txt
sed -i 's/"//g' receita_2016.txt
sed -i 's/"/ /g' licitacao.txt 
sed -i "s/\r//g" licitacao.txt

rm -rf receita.txt
rm -rf receitas.txt
rm -rf grande.zip
rm -rf prefeitos_eleitos_pb_2016.csv

mv prefeito_sem_acento.csv $storage
mv receita_2016.txt $storage
mv licitacao.txt $storage
mv participante.txt $storage

cat cria_index_licitacao.cypher | cypher-shell -u neo4j -p tcctcc --format plain
cat cria_index_participante.cypher | cypher-shell -u neo4j -p tcctcc --format plain	
cat cria_index_unidade_gestora.cypher | cypher-shell -u neo4j -p tcctcc --format plain	
cat carrega_unidade_gestora.cypher | cypher-shell -u neo4j -p tcctcc --format plain
cat carrega_licitacao.cypher | cypher-shell -u neo4j -p tcctcc --format plain
cat carrega_participante.cypher | cypher-shell -u neo4j -p tcctcc --format plain
cat carrega_partido.cypher | cypher-shell -u neo4j -p tcctcc --format plain
cat carrega_candidato.cypher | cypher-shell -u neo4j -p tcctcc --format plain
cat carrega_municipio.cypher | cypher-shell -u neo4j -p tcctcc --format plain
cat cria_relacionamento_governa.cypher | cypher-shell -u neo4j -p tcctcc --format plain
cat cria_relacionamento_lança.cypher | cypher-shell -u neo4j -p tcctcc --format plain
cat cria_relacionamento_doapara.cypher | cypher-shell -u neo4j -p tcctcc --format plain