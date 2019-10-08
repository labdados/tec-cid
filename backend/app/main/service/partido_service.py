from ..model.models import Partido
from app.main import db

class PartidoService:
  
  def get_partidos(self, pagina, limite):
    skip = limite * (pagina - 1)
    result = Partido.match(db).order_by("_.sigla").skip(skip).limit(limite)
    nodes = [n.__node__ for n in result]
    return nodes
