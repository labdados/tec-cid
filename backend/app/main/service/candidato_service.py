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
    
    def get_doacoes(self, id_candidato):
        query = "MATCH path=(part:Participante)-[r:DOOU_PARA]->(cand:Candidato) \
        WHERE cand.id = '{id}' \
        RETURN part.cpf_cnpj as cpf_cnpj_doador, part.nome as nome_doador, \
        r.valor_receita as valor_receita, r.tipo_receita as tipo_receita, \
        r.fonte_recurso as fonte_recurso, r.descricao_receita as descricao_receita".format(id = id_candidato)
        result = db.run(query).data()
        return result