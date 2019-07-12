import os
from decouple import config

NEO4J_CFG = {
    'host': config('NEO4J_HOST', default='localhost'),
    'port': config('NEO4J_PORT', cast=int, default='7687'),
    'user': config('NEO4J_USER', default='neo4j'),
    'passwd': config('NEO4J_PASSWORD', default='neo4j')

}
