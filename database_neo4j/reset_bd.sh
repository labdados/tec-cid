#!/bin/bash
killall neo4j
cd /var/lib/neo4j/data/databases
rm -rf graph.db/
neo4j start
