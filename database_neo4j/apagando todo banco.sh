#!/bin/bash


cat deleta_todos_participantes.cypher | cypher-shell -u neo4j -p tcctcc --format plain
cat deleta_todas_licitacoes.cypher | cypher-shell -u neo4j -p tcctcc --format plain
cat deleta_todos_nos.cypher | cypher-shell -u neo4j -p tcctcc --format plain