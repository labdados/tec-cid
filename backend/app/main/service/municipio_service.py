from ..model.municipio import Municipio
from app.main.__init_ import db

class MunicipioService:

    def get_municipios(self, pagina, limite):
        skip = limite * (pagina - 1)
        result = Municipio.match(db).skip(skip).limit(limite)
        nodes = [n.__node__ for n in result]
        return nodes