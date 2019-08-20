#!/bin/bash

# if env variables do not exist, use default values
NEO4J_DIR_IMPORT=${NEO4J_DIR_IMPORT:-"../import"}

echo $NEO4J_DIR_IMPORT

mkdir -p $NEO4J_DIR_IMPORT

cd $NEO4J_DIR_IMPORT

curl -o licitacao.txt.gz https://dados.tce.pb.gov.br/TCE-PB-SAGRES-Licitacao_Esfera_Municipal.txt.gz
curl -o participante.txt.gz https://dados.tce.pb.gov.br/TCE-PB-SAGRES-Propostas_Licitacao_Esfera_Municipal.txt.gz

if [ -f "licitacao.txt" ]; then
    mv licitacao.txt licitacao.txt.bkp
fi
    
if [ -f "participante.txt" ]; then
    mv participante.txt participante.txt.bkp
fi

gunzip licitacao.txt.gz
gunzip participante.txt.gz
sed -i .sed -e 's/"/ /g' -e "s/\r//g" licitacao.txt 

