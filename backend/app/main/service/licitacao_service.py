from ..model.licitacao import Licitacao
from app.main.__init_ import db

class LicitacaoService:
    
    def __init__(self):
    	self.count_lic = 0
    	self.count_props = 0

    def get_licitacoes(self, unidade, tipo, data_inicio, data_fim, pagina, itens, ordenar_por, ordem):
        skip = itens * (pagina - 1)
        
        filtros = {}
        conditions = ["_.Valor IS NOT NULL"]

        if tipo:
            conditions.append("_.CodTipoLicitacao = '{}'".format(tipo))

        if unidade:
            conditions.append("_.CodUnidadeGest = '{}'".format(unidade))

        if data_inicio:
            conditions.append("_.Data >= date('{}')".format(data_inicio))

        if data_fim:
            conditions.append("_.Data <= date('{}')".format(data_fim))

        if not ordenar_por:
            ordenar_por = "_.Data"
        else:
            ordenar_por = "_." + ordenar_por

        if ordem.upper() in ["DESC", "ASC"]:
            ordenar_por += " {}".format(ordem)

        self.count_lic = len(Licitacao.match(db).where(*conditions))
        result = Licitacao.match(db).where(*conditions).order_by(ordenar_por).skip(skip).limit(itens)
        nodes = []
        for lic in result:
            node = lic.__node__
            node["id"] = "{}-{}-{}".format(lic.cd_ugestora, lic.nu_licitacao, lic.tp_licitacao)
            node["Data"] = node["Data"].__str__()
            nodes.append(node)

        return(nodes)

    def get_licitacao_especifica(self, codUnidadeGestora, codTipoLicitacao, codLicitacao):
        result = db.run("MATCH (l:Licitacao) WHERE l.CodUnidadeGest='{}' AND l.CodTipoLicitacao='{}' AND l.CodLicitacao='{}' RETURN l ".format(codUnidadeGestora, codTipoLicitacao, codLicitacao)).data()
        nodes = []
        for lic in result:
            node = lic["l"]
            node["id"] = "{}-{}-{}".format(codUnidadeGestora, codLicitacao, codTipoLicitacao)
            node["Data"] = node["Data"].__str__()
            nodes.append(node)
        return nodes

    def get_propostas(self, codUnidadeGestora, codLicitacao, codTipoLicitacao, pagina, limite):
        skip = limite * (pagina - 1)

        query = "MATCH (p:Participante)<-[r:RECEBEU_PROPOSTA_DE]-(l:Licitacao) \
            WHERE l.CodUnidadeGest='{}' and l.CodTipoLicitacao='{}' and l.CodLicitacao='{}'".format(codUnidadeGestora, codTipoLicitacao, codLicitacao)

        self.count_props = self.get_count(query+"RETURN COUNT(*)")

        result = db.run(query + " RETURN p.NomeParticipante as NomeParticipante, p.ChaveParticipante as ChaveParticipante, \
                                          r.CodUnidadeGest as CodUnidadeGest, r.CodLicitacao as CodLicitacao, \
                                          r.CodTipoLicitacao as CodTipoLicitacao, r.QuantidadeOferdada as QuantidadeOferdada, \
                                          r.ValorOfertado as ValorOfertado \
                                          SKIP {} LIMIT {}".format(skip, limite)).data()
        return result