from ..model.models import Licitacao
from app.main import db

class LicitacaoService:

    def __init__(self):
    	self.count_lic = 0
    	self.count_props = 0

    def get_count(self, query):
        result = db.run(query).data()     
        dic = result[0]
        count = dic['COUNT(*)']
        return count

    def get_licitacoes(self, unidade, tipo, data_inicio, data_fim, pagina, itens, ordenar_por, ordem):
        skip = itens * (pagina - 1)
        
        filtros = {}
        conditions = ["_.valor_licitado IS NOT NULL"]

        if tipo:
            conditions.append("_.cd_modalidade = '{}'".format(tipo))

        if unidade:
            conditions.append("_.cd_ugestora = '{}'".format(unidade))

        if data_inicio:
            conditions.append("_.data_homologacao >= date('{}')".format(data_inicio))

        if data_fim:
            conditions.append("_.data_homologacao <= date('{}')".format(data_fim))

        if not ordenar_por:
            ordenar_por = "_.data_homologacao"
        else:
            ordenar_por = "_." + ordenar_por

        if ordem.upper() in ["DESC", "ASC"]:
            ordenar_por += " {}".format(ordem)

        #self.count_lic = len(Licitacao.match(db).where(*conditions))
        match_query = Licitacao.match(db).where(*conditions)
        self.count_lic = match_query.__len__()
        result = match_query.order_by(ordenar_por).skip(skip).limit(itens)
        nodes = []
        for lic in result:
            node = lic.__node__
            node["id"] = "{}-{}-{}".format(lic.cd_ugestora, lic.cd_modalidade, lic.numero_licitacao)
            node["data_homologacao"] = node["data_homologacao"].__str__()
            nodes.append(node)

        return(nodes)

    def get_licitacao(self, codUnidadeGestora, codTipoLicitacao, codLicitacao):
        result = Licitacao.match(db).where(cd_ugestora = codUnidadeGestora,
                                           cd_modalidade = codTipoLicitacao,
                                           numero_licitacao = codLicitacao)

        #result = db.run("MATCH (l:Licitacao) WHERE l.cd_ugestora='{}' AND l.cd_modalidade='{}' AND l.numero_licitacao='{}' RETURN l ".format(codUnidadeGestora, codTipoLicitacao, codLicitacao)).data()
        nodes = []
        for lic in result:
            node = lic.__node__
            node["id"] = "{}-{}-{}".format(codUnidadeGestora, codLicitacao, codTipoLicitacao)
            node["data_homologacao"] = node["data_homologacao"].__str__()
            nodes.append(node)
        return nodes

    def get_propostas(self, codUnidadeGestora, codTipoLicitacao, codLicitacao, pagina, limite):
        skip = limite * (pagina - 1)

        query = "MATCH (p:Participante)-[r:FEZ_PROPOSTA_EM]->(l:Licitacao) \
                WHERE l.cd_ugestora='{}' and l.cd_modalidade='{}' and l.numero_licitacao='{}'".format(codUnidadeGestora, codTipoLicitacao, codLicitacao)

        self.count_props = self.get_count(query + "RETURN COUNT(*)")

        result = db.run(query + " RETURN p.nome as nome_participante, p.cpf_cnpj as cpf_cnpj_participante, \
                                 l.cd_ugestora as cd_ugestora, l.numero_licitacao as numero_licitacao, \
                                 l.cd_modalidade as cd_modalidade_licitacao, r.valor as valor_proposta, \
                                 r.situacao as situacao_proposta \
                                 SKIP {} LIMIT {}".format(skip, limite)).data()
        return result