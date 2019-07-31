from ..model.models import UnidadeGestora
import config as cfg
from py2neo import Graph

class Unidade_Gestora_Service:
	def __init__(self):
		self.graph = Graph(host=cfg.NEO4J_CFG["host"] , http_port=cfg.NEO4J_CFG["http_port"], https_port=cfg.NEO4J_CFG["https_port"] , bolt_port=cfg.NEO4J_CFG["bolt_port"], user=cfg.NEO4J_CFG["user"], password=cfg.NEO4J_CFG["passwd"])

	def get_unidades_e_codigos(self):
                result = UnidadeGestora.match(self.graph)
                nodes = [n.__node__ for n in result]
                return nodes