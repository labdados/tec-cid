from ..model.municipio import Municipio
from app.main import db

class MunicipioService:

    def get_municipios(self, pagina, limite):
        skip = limite * (pagina - 1)
        result = Municipio.match(db).order_by("_.nome").skip(skip).limit(limite)
        nodes = [n.__node__ for n in result]
        return nodes
    
    def get_municipio(self, id):
        result = Municipio.match(db).where(id = id)
        nodes = [n.__node__ for n in result]
        return nodes