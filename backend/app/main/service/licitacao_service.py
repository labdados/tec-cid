from ..model.models import Licitacao
from ..model.models import UnidadeGestora
from app.main import db
from .municipio_service import MunicipioService

class LicitacaoService:

    def __init__(self):
    	self.count_lic = 0
    	self.count_props = 0

    def get_count(self, query):
        result = db.run(query).data()     
        dic = result[0]
        count = dic['COUNT(*)']
        return count

    def get_licitacoes(self, unidade, tipo, data_inicio, data_fim, pagina, itens, ordenar_por, ordem, id_municipio):
        q_match = ("MATCH (lic:Licitacao)<-[REALIZOU]-(ug:UnidadeGestora)-[:PERTENCE_A]->(mun:Municipio)")
        return_l = ["lic", "ug.nome AS nome_ug"]
        conditions = ["lic.valor_licitado IS NOT NULL"]

        if id_municipio:
            conditions.append("mun.id = '{}'".format(id_municipio))
        
        if tipo:
            conditions.append("lic.cd_tipo_licitacao = '{}'".format(tipo))

        if unidade:
            conditions.append("lic.cd_ugestora = '{}'".format(unidade))

        if data_inicio:
            conditions.append("lic.data_homologacao >= date('{}')".format(data_inicio))

        if data_fim:
            conditions.append("lic.data_homologacao <= date('{}')".format(data_fim))

        if not ordenar_por:
            ordenar_por = "lic.data_homologacao"
        else:
            ordenar_por = "lic." + ordenar_por

        if ordem.upper() in ["DESC", "ASC"]:
            ordenar_por += " {}".format(ordem)

        skip = itens * (pagina - 1)

        query = (q_match + 
                 " WHERE {}".format(" AND ".join(conditions)))

        count_query = query + " RETURN COUNT(lic) AS count_lic"
        self.count_lic = db.run(count_query).evaluate()

        query += (" RETURN {}".format(", ".join(return_l)) +
                  " ORDER BY {}".format(ordenar_por) +
                  " SKIP {} LIMIT {}".format(skip, itens))

        print(query)
        
        results = db.run(query).data()
        nodes = []
        for res in results:
            node = {**res["lic"], 'nome_unidade_gestora': res["nome_ug"]}
            node["id"] = "{}-{}-{}".format(node["cd_ugestora"], node["cd_tipo_licitacao"],
                                           node["numero_licitacao"])
            nodes.append(node)
        return nodes

    def get_licitacao(self, codUnidadeGestora, codTipoLicitacao, codLicitacao):
        result = Licitacao.match(db).where(cd_ugestora = codUnidadeGestora,
                                           cd_tipo_licitacao = codTipoLicitacao,
                                           numero_licitacao = codLicitacao)
        
        unidade_gestora = UnidadeGestora.match(db).where(cd_ugestora = codUnidadeGestora)
        nome_unidade_gest = ''
        for uni in unidade_gestora:
            node = uni.__node__
            nome_unidade_gest = node['nome']

        #result = db.run("MATCH (l:Licitacao) WHERE l.cd_ugestora='{}' AND l.cd_modalidade='{}' AND l.numero_licitacao='{}' RETURN l ".format(codUnidadeGestora, codTipoLicitacao, codLicitacao)).data()
        nodes = []
        for lic in result:
            node = lic.__node__
            node["id"] = "{}-{}-{}".format(codUnidadeGestora, codLicitacao, codTipoLicitacao)
            node["data_homologacao"] = node["data_homologacao"].__str__()
            node["nome_unidade_gestora"] = nome_unidade_gest
            nodes.append(node)
        return nodes

    def get_propostas(self, codUnidadeGestora, codTipoLicitacao, codLicitacao, pagina, limite):
        skip = limite * (pagina - 1)

        query = "MATCH (p:Participante)-[r:FEZ_PROPOSTA_EM]->(l:Licitacao) \
                WHERE l.cd_ugestora='{}' and l.cd_tipo_licitacao='{}' and l.numero_licitacao='{}'".format(codUnidadeGestora, codTipoLicitacao, codLicitacao)

        self.count_props = self.get_count(query + "RETURN COUNT(*)")

        result = db.run(query + " RETURN p.nome as nome_participante, p.cpf_cnpj as cpf_cnpj_participante, \
                                 l.cd_ugestora as cd_ugestora, l.numero_licitacao as numero_licitacao, \
                                 l.cd_tipo_licitacao as cd_tipo_licitacao_licitacao, r.valor as valor_proposta, \
                                 r.situacao as situacao_proposta \
                                 SKIP {} LIMIT {}".format(skip, limite)).data()
        return result