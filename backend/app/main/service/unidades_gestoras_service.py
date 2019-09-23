from ..model.unidade_gestora import UnidadeGestora
from app.main import db

class UnidadeGestoraService:

	def get_unidades_e_codigos(self):
            result = UnidadeGestora.match(db)
            nodes = [n.__node__ for n in result]
            return nodes