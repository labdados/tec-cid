#!/bin/bash

# if env variables do not exist, use default values
NEO4J_DIR_IMPORT=${NEO4J_DIR_IMPORT:-"../import"}

echo $NEO4J_DIR_IMPORT

mkdir -p $NEO4J_DIR_IMPORT

cd $NEO4J_DIR_IMPORT

curl -o prestacao_2016.zip http://agencia.tse.jus.br/estatistica/sead/odsele/prestacao_contas/prestacao_contas_relatorio_financeiro_2016.zip
curl -o prefeitos_eleitos_pb_2016_com_acento.csv https://raw.githubusercontent.com/StewenAscari/tcc-licitacoes-doacoes/master/dados/prefeitos_eleitos_pb_2016.csv

if [ -f "$NEO4J_DIR_IMPORT/receitas_2016_PB.txt" ]; then
    mv $NEO4J_DIR_IMPORT/receitas_2016_PB.txt $NEO4J_DIR_IMPORT/receitas_2016_PB.txt.bkp
fi

if [ -f "$NEO4J_DIR_IMPORT/prefeitos_2016_PB.csv" ]; then
    mv $NEO4J_DIR_IMPORT/prefeitos_2016_PB.csv $NEO4J_DIR_IMPORT/prefeitos_2016_PB.csv.bkp
fi

unzip -p prestacao_2016.zip receitas_candidatos_relatorio_financeiro_2016_PB.txt > receitas_2016_PB_latin1.txt
iconv -f UTF8 -t ASCII//TRANSLIT < prefeitos_eleitos_pb_2016_com_acento.csv > prefeitos_2016_PB.csv
iconv --from latin1 --to-code utf-8 receitas_2016_PB_latin1.txt > receitas_2016_PB_com_acento.txt
iconv -f UTF8 -t ASCII//TRANSLIT < receitas_2016_PB_com_acento.txt > receitas_2016_PB.txt
sed -e  '1s/\///g' -e '1s/ //g' -e 's/"//g' -i .sed receitas_2016_PB.txt

rm prestacao_2016.zip receitas_2016_PB_latin1.txt receitas_2016_PB_com_acento.txt
