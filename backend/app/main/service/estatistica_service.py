from ..model.licitacao import Licitacao
from app.main import db

PARTICIPANTE_GROUP = "participante"
MUNICIPIO_GROUP = "municipio"

class EstatisticaService:

    def get_estatistica_licitacoes(self, id_municipio, data_inicio, data_fim, pagina, itens,
                                   agrupar_por, ordenar_por, ordem):
        
        q_match = ("MATCH (p:Participante)-[f:FEZ_PROPOSTA_EM]->(l:Licitacao)<-"
                   "[REALIZOU]-(u:UnidadeGestora)-[:PERTENCE_A]->(m:Municipio)")
        
        conditions = ["l.valor_licitado IS NOT NULL", "f.situacao = 'Vencedora'"]

        if id_municipio:
            conditions.append("m.id = '{}'".format(id_municipio))

        if data_inicio:
            conditions.append("l.data_homologacao >= date('{}')".format(data_inicio))

        if data_fim:
            conditions.append("l.data_homologacao <= date('{}')".format(data_fim))

        group_by_l = [g.strip().lower() for g in agrupar_por.split(',')]
        return_l = []

        if PARTICIPANTE_GROUP in group_by_l:
            return_l.append("p.cpf_cnpj AS cpf_cnpj_participante, "
                            "p.nome AS nome_participante")

        if MUNICIPIO_GROUP in group_by_l:
            return_l.append("m.id AS id_municipio, "
                            "m.nome AS nome_municipio")

        return_l.append("COUNT(DISTINCT l) AS n_licitacoes, "
                        "COUNT(DISTINCT p) AS n_participantes, "
                        "SUM(l.valor_licitado) AS valor_licitacoes, "
                        "SUM(f.valor) AS valor_propostas_vencedoras")
        
        if not ordenar_por:
            ordenar_por = "valor_licitacoes"

        if ordem.upper() in ["DESC", "ASC"]:
            ordenar_por += " {}".format(ordem)
        else:
            ordenar_por += " DESC"

        skip = itens * (pagina - 1)

        query = (q_match + 
                 " WHERE {}".format(" AND ".join(conditions)) +
                 " RETURN {}".format(", ".join(return_l)) +
                 " ORDER BY {}".format(ordenar_por) +
                 " SKIP {} LIMIT {}".format(skip, itens))

        result = db.run(query).data()
        return(result)
