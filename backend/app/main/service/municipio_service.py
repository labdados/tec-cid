from ..model.models import Municipio
from settings import *
from py2neo import Graph

class Municipio_Service:
    
    def __init__(self):
        self.graph = Graph(host=NEO4J_CFG["host"] , port=NEO4J_CFG["port"],user=NEO4J_CFG["user"], password=NEO4J_CFG["passwd"])

    def get_municipios(self, pagina, limite):
        skip = limite * (pagina - 1)
        result = Municipio.match(self.graph).skip(skip).limit(limite)
        nodes = [n.__node__ for n in result]
        return nodes