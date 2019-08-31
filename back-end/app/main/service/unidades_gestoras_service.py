from ..model.models import UnidadeGestora
from settings import *
from py2neo import Graph

class Unidade_Gestora_Service:
	def __init__(self):
		self.graph = Graph(host=NEO4J_CFG["host"] , port=NEO4J_CFG["port"],
                           user=NEO4J_CFG["user"], password=NEO4J_CFG["passwd"])

	def get_unidades_e_codigos(self):
                result = UnidadeGestora.match(self.graph)
                nodes = [n.__node__ for n in result]
                return nodes