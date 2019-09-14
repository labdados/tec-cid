from ..model.participante import Participante
from app.main.__init_ import db

class Participante_Service:

	def __init__(self):
		self.count_part = 0

	def get_participantes(self, pagina, itens):
		skip = itens * (pagina - 1)
		
		result = Participante.match(db).order_by("_.NomeParticipante").skip(skip).limit(itens)
		
		self.count_part = len(Participante.match(db))
		
		nodes = [n.__node__ for n in result]
		
		return nodes

	# Busca participante pelo cpf ou cnpj
	def get_participante_por_codigo(self, codigo):
	    result = Participante.match(db).where("_.ChaveParticipante = '{}'".format(codigo))
	    nodes = [n.__node__ for n in result]
	    return nodes