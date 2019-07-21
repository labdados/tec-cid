from py2neo import Graph
from models import Licitacao, Participante, UnidadeGestora
import config as cfg

class Dao:
    def __init__(self):
        self.graph = Graph(host=cfg.NEO4J_CFG["host"] , http_port=cfg.NEO4J_CFG["http_port"], https_port=cfg.NEO4J_CFG["https_port"] , bolt_port=cfg.NEO4J_CFG["bolt_port"], user=cfg.NEO4J_CFG["user"], password=cfg.NEO4J_CFG["passwd"])
        self.count_lic = 0
        self.count_part = 0
        self.count_props = 0


    def get_count(self, query):
        result = self.graph.run(query).data()     
        dic = result[0]
        count = dic['COUNT(*)']
        return count

    def get_licitacoes(self, ano, tipo, unidade, pagina, itens):
        skip = itens * (pagina - 1)
        
        filtros = {}
        conditions = []

        if ano:
            conditions.append("_.Data ENDS WITH '{}'".format(ano))

        if tipo:
            conditions.append("_.CodTipoLicitacao = '{}'".format(tipo))

        if unidade:
            conditions.append("_.CodUnidadeGest = '{}'".format(unidade))

        self.count_lic = len(Licitacao.match(self.graph).where(*conditions))

        result = Licitacao.match(self.graph).where(*conditions).order_by("_.Data").skip(skip).limit(itens)
        
        nodes = []
        for lic in result:
            node = lic.__node__
            node["id"] = "{}-{}-{}".format(lic.cd_ugestora, lic.nu_licitacao, lic.tp_licitacao)
            nodes.append(node)

        nodes.append(self.secao_de_links(pagina, itens, ano, tipo, unidade))
        return(nodes)


    def get_unidades_e_codigos(self):
        result = UnidadeGestora.match(self.graph)
        nodes = [n.__node__ for n in result]
        return nodes
    

    def get_licitacao_especifica(self, codUnidadeGestora, codTipoLicitacao, codLicitacao):
        result = self.graph.run("MATCH (l:Licitacao) WHERE l.CodUnidadeGest='{}' AND l.CodTipoLicitacao='{}' AND l.CodLicitacao='{}' RETURN l ".format(codUnidadeGestora, codTipoLicitacao, codLicitacao))
        nodes = [n for n in result]
        return nodes


    def procurando_propostas(self, codUnidadeGestora, codLicitacao, codTipoLicitacao, pagina, limite):
        skip = limite * (pagina - 1)

        query = "MATCH p=()-[r:FEZ_PROPOSTA_EM]->() WHERE r.CodUnidadeGest='{}' and r.CodTipoLicitacao='{}' and r.CodLicitacao='{}' ".format(codUnidadeGestora, codTipoLicitacao, codLicitacao)

        self.count_props = self.get_count(query+"RETURN COUNT(*)")

        result = self.graph.run(query + " RETURN r SKIP {} LIMIT {}".format(skip, limite))
        nodes = [n for n in result]
        return nodes


    def get_participantes(self, pagina, itens):
        skip = itens * (pagina - 1)
        result = Participante.match(self.graph).order_by("_.NomeParticipante").skip(skip).limit(itens)

        self.count_part = len(Participante.match(self.graph))

        nodes = [n.__node__ for n in result]
        nodes.append(self.secao_de_links_participantes(pagina, itens))
        return nodes

    # Busca participante pelo cpf ou cnpj
    def get_participante_por_codigo(self, codigo):
        result = Participante.match(self.graph).where("_.ChaveParticipante = '{}'".format(codigo))
        nodes = [n.__node__ for n in result]
        return nodes          

