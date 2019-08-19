#/bin/bash

# First argument is the neo4j container name or id. If empty, use default value
NEO4J_CONTAINER_NAME=${1:-teccid-neo4j}

docker exec -u neo4j -w /feed $NEO4J_CONTAINER_NAME /bin/bash ./feed_neo4j.sh
