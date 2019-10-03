from ..model.unidade_gestora import UnidadeGestora
from app.main import db

class UnidadeGestoraService:

	def get_unidades_gestoras(self):
            result = UnidadeGestora.match(db).where("_.nome_esfera_jurisdicionado = 'Municipal'")
            nodes = [n.__node__ for n in result]
            return nodes