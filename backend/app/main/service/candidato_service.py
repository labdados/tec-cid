from ..model.candidato import Candidato
from app.main import db

class CandidatoService:

    def get_candidatos(self, pagina, limite):
        skip = limite * (pagina - 1)
        result = Candidato.match(db).order_by("_.Nome").skip(skip).limit(limite)
        nodes = [n.__node__ for n in result]
        return nodes

