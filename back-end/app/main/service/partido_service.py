from ..model.models import Partido
from settings import *
from py2neo import Graph

class Partido_Service:
    
  def __init__(self):
    self.graph = Graph(host=NEO4J_CFG["host"] , port=NEO4J_CFG["port"],user=NEO4J_CFG["user"], password=NEO4J_CFG["passwd"])
  
  def get_partidos(self, pagina, limite):
    skip = limite * (pagina - 1)
    result = Partido.match(self.graph).order_by("_.SiglaPartido").skip(skip).limit(limite)
    nodes = [n.__node__ for n in result]
    return nodes
