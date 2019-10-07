from ..model.models import UnidadeGestora
from app.main import db
from ..model.models import Municipio

class UnidadeGestoraService:

	def get_unidades_gestoras(self, nome_municipio, id_municipio):
            result = ''
            if nome_municipio:
                result = UnidadeGestora.match(db).where("_.municipio = '{}' AND _.nome_esfera_jurisdicionado = 'Municipal'".format(nome_municipio.upper()))
            elif id_municipio:
                mun = Municipio.match(db).where("_.id = '{}'".format(id_municipio)).first()
                
                # Algumas cidades não possuem unidades gestoras
                try:
                    result = [ug.__node__['nome'] for ug in mun.unidades_gestoras]
                    return result
                except:
                    return None
            else:
                result = UnidadeGestora.match(db).where("_.nome_esfera_jurisdicionado = 'Municipal'")
            
            nodes = [n.__node__ for n in result]
            return nodes
