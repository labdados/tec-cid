import os
from decouple import config
NEO4J_CFG = {
    'host': config('HOST_NAME', default='localhost'),
    'http_port': config('HTTP_PORT', cast=int, default='7474'),
    'https_port': config('HTTPS_PORT', cast=int, default='7473'),
    'bolt_port': config('BOLT_PORT', cast=int, default='7687'),
    'user': config('USER', default='neo4j'),
    'passwd': config('PASSWORD', default='neo4j')

}
