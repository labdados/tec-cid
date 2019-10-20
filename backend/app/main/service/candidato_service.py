from ..model.models import Candidato
from app.main import db

class CandidatoService:

    def get_candidatos(self, pagina, limite):
        skip = limite * (pagina - 1)
        result = Candidato.match(db).order_by("_.nome").skip(skip).limit(limite)
        nodes = [n.__node__ for n in result]
        return nodes
    
    def get_candidato_por_id(self, id):
        result = Candidato.match(db).where(id = id)
        nodes = [n.__node__ for n in result]
        return nodes