#!/bin/bash

# if env variables do not exist, use default values
IMPORT_DATA_DIR=${IMPORT_DATA_DIR:-"../../dados"}

echo $IMPORT_DATA_DIR

mkdir -p $IMPORT_DATA_DIR

cd $IMPORT_DATA_DIR

curl -o prestacao_2016.zip.tmp http://agencia.tse.jus.br/estatistica/sead/odsele/prestacao_contas/prestacao_contas_relatorio_financeiro_2016.zip
curl -o prefeitos_2016_PB.csv.tmp https://raw.githubusercontent.com/StewenAscari/tcc-licitacoes-doacoes/master/dados/prefeitos_eleitos_pb_2016.csv

if [ -f "receitas_2016_PB.txt" ]; then
    mv receitas_2016_PB.txt receitas_2016_PB.txt.bkp
fi

if [ -f "prefeitos_2016_PB.csv" ]; then
    mv prefeitos_2016_PB.csv prefeitos_2016_PB.csv.bkp
fi

# retirando acentos
iconv -f UTF8 -t ASCII//TRANSLIT < prefeitos_2016_PB.csv.tmp > prefeitos_2016_PB.csv

unzip -p prestacao_2016.zip.tmp receitas_candidatos_relatorio_financeiro_2016_PB.txt > receitas_2016_PB.txt_1.tmp
iconv --from latin1 --to-code utf-8 receitas_2016_PB.txt_1.tmp > receitas_2016_PB.txt_2.tmp
iconv -f UTF8 -t ASCII//TRANSLIT < receitas_2016_PB.txt_2.tmp > receitas_2016_PB.txt_3.tmp
sed -e '1s/\///g' -e '1s/ //g' -e 's/"//g' receitas_2016_PB.txt_3.tmp > receitas_2016_PB.txt

rm prestacao_2016.zip.tmp prefeitos_2016_PB.csv.tmp receitas_2016_PB.txt_?.tmp