#!/bin/bash

# if env variables do not exist, use default values
IMPORT_DATA_DIR=${IMPORT_DATA_DIR:-"../../dados"}

echo $IMPORT_DATA_DIR

mkdir -p $IMPORT_DATA_DIR

cd $IMPORT_DATA_DIR

curl -o licitacao.txt.gz https://dados.tce.pb.gov.br/TCE-PB-SAGRES-Licitacao_Esfera_Municipal.txt.gz
curl -o propostas.txt.gz https://dados.tce.pb.gov.br/TCE-PB-SAGRES-Propostas_Licitacao_Esfera_Municipal.txt.gz

if [ -f "licitacao.txt" ]; then
    mv licitacao.txt licitacao.txt.bkp
fi
    
if [ -f "propostas.txt" ]; then
    mv propostas.txt propostas.txt.bkp
fi

gunzip licitacao.txt.gz
gunzip propostas.txt.gz
sed -i".tmp" -e 's/"/ /g' -e "s/\r//g" licitacao.txt
 
 rm licitacao.txt.tmp