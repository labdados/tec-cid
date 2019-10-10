from ..model.models import UnidadeGestora, Municipio
from app.main import db
from ..model.models import Municipio

class UnidadeGestoraService:

    def get_unidades_gestoras(self, nome_municipio, id_municipio):
        try:
            nodes = []
            if id_municipio:
                municipio = Municipio.match(db).where("_.id = '{}'".format(id_municipio)).first()
                for ug in municipio.unidades_gestoras:
                    db.pull(ug) # Precisa dar pull para obter objeto relacionado
                    nodes.append(ug.__node__)
            elif nome_municipio:
                result = UnidadeGestora.match(db).where("_.municipio = '{}'".format(nome_municipio.upper()))
                nodes = [n.__node__ for n in result]
            else:
                result = UnidadeGestora.match(db).where("_.nome_esfera_jurisdicionado = 'Municipal'")
                nodes = [n.__node__ for n in result]
            
            return nodes
        except Exception as e: # Algumas cidades não possuem unidades gestoras
            print(e)
            return None
