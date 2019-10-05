from ..model.unidade_gestora import UnidadeGestora
from app.main import db

class UnidadeGestoraService:

	def get_unidades_gestoras(self, nome_municipio):
            result = ''
            if nome_municipio:
                result = UnidadeGestora.match(db).where("_.municipio = '{}' AND _.nome_esfera_jurisdicionado = 'Municipal'".format(nome_municipio.upper()))
            else:
                result = UnidadeGestora.match(db).where("_.nome_esfera_jurisdicionado = 'Municipal'")
            
            nodes = [n.__node__ for n in result]
            return nodes
