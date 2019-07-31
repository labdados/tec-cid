from ..model.models import Participante
from py2neo import Graph
import config as cfg

class Participante_Service:

	def __init__(self):
		self.graph = Graph(host=cfg.NEO4J_CFG["host"] , http_port=cfg.NEO4J_CFG["http_port"], https_port=cfg.NEO4J_CFG["https_port"] , bolt_port=cfg.NEO4J_CFG["bolt_port"], user=cfg.NEO4J_CFG["user"], password=cfg.NEO4J_CFG["passwd"])

		self.count_part = 0

	def get_participantes(self, pagina, itens):
	    skip = itens * (pagina - 1)
	    result = Participante.match(self.graph).order_by("_.NomeParticipante").skip(skip).limit(itens)

	    self.count_part = len(Participante.match(self.graph))

	    nodes = [n.__node__ for n in result]
	    nodes.append(self.secao_de_links_participantes(pagina, itens))
	    return nodes

	# Busca participante pelo cpf ou cnpj
	def get_participante_por_codigo(self, codigo):
	    result = Participante.match(self.graph).where("_.ChaveParticipante = '{}'".format(codigo))
	    nodes = [n.__node__ for n in result]
	    return nodes