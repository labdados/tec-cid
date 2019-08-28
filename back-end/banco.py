from py2neo import Graph
from models import Licitacao, Participante, UnidadeGestora
from settings import *

class Dao:
    def __init__(self):
        self.graph = Graph(host=NEO4J_CFG["host"] , port=NEO4J_CFG["port"],
                           user=NEO4J_CFG["user"], password=NEO4J_CFG["passwd"])
        self.count_lic = 0
        self.count_part = 0
        self.count_props = 0

    def get_count(self, query):
        result = self.graph.run(query).data()     
        dic = result[0]
        count = dic['COUNT(*)']
        return count

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

        self.count_lic = len(Licitacao.match(self.graph).where(*conditions))
        result = Licitacao.match(self.graph).where(*conditions).order_by(ordenar_por).skip(skip).limit(itens)
        nodes = []
        for lic in result:
            node = lic.__node__
            node["id"] = "{}-{}-{}".format(lic.cd_ugestora, lic.nu_licitacao, lic.tp_licitacao)
            node["Data"] = node["Data"].__str__()
            nodes.append(node)

        #nodes.append(self.secao_de_links(pagina, itens, ano, tipo, unidade))
        return(nodes)

    
    def get_unidades_e_codigos(self):
        result = UnidadeGestora.match(self.graph)
        nodes = [n.__node__ for n in result]
        return nodes
    

    def get_licitacao_especifica(self, codUnidadeGestora, codTipoLicitacao, codLicitacao):
        result = self.graph.run("MATCH (l:Licitacao) WHERE l.CodUnidadeGest='{}' AND l.CodTipoLicitacao='{}' AND l.CodLicitacao='{}' RETURN l ".format(codUnidadeGestora, codTipoLicitacao, codLicitacao)).data()
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
        #query = "MATCH p=()-[r:FEZ_PROPOSTA_EM]->() WHERE r.CodUnidadeGest='{}' and r.CodTipoLicitacao='{}' and r.CodLicitacao='{}' ".format(codUnidadeGestora, codTipoLicitacao, codLicitacao)

        self.count_props = self.get_count(query+"RETURN COUNT(*)")

        result = self.graph.run(query + " RETURN p.NomeParticipante as NomeParticipante, p.ChaveParticipante as ChaveParticipante, \
                                          r.CodUnidadeGest as CodUnidadeGest, r.CodLicitacao as CodLicitacao, \
                                          r.CodTipoLicitacao as CodTipoLicitacao, r.QuantidadeOferdada as QuantidadeOferdada, \
                                          r.ValorOfertado as ValorOfertado \
                                          SKIP {} LIMIT {}".format(skip, limite)).data()
        #nodes = [n for n in result]
        return result


    def get_participantes(self, pagina, itens):
        skip = itens * (pagina - 1)
        result = Participante.match(self.graph).order_by("_.NomeParticipante").skip(skip).limit(itens)

        self.count_part = len(Participante.match(self.graph))

        nodes = [n.__node__ for n in result]
        #nodes.append(self.secao_de_links_participantes(pagina, itens))
        return nodes

    # Busca participante pelo cpf ou cnpj
    def get_participante_por_codigo(self, codigo):
        result = Participante.match(self.graph).where("_.ChaveParticipante = '{}'".format(codigo))
        nodes = [n.__node__ for n in result]
        return nodes          

