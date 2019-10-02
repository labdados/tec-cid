from ..model.participante import Participante
from app.main import db

class ParticipanteService:

	def __init__(self):
		self.count_part = 0

	def get_participantes(self, pagina, itens):
		skip = itens * (pagina - 1)
		
		result = Participante.match(db).order_by("_.nome").skip(skip).limit(itens)
		
		self.count_part = len(Participante.match(db))
		
		nodes = [n.__node__ for n in result]
		
		return nodes

	# Busca participante pelo cpf ou cnpj
	def get_participante(self, cpf_cnpj):
	    result = Participante.match(db).where("_.cpf_cnpj = '{}'".format(cpf_cnpj))
	    nodes = [n.__node__ for n in result]
	    return nodes