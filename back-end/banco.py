from py2neo import Graph
from models import Licitacao, Participante, UnidadeGestora
import config as cfg

class Dao:
    def __init__(self):
        #self.graph = Graph(host='neodb', http_port=7474, https_port= 7473, bolt_port=7687, user='neo4j', password='tcctcc')
        self.graph = Graph(host=cfg.NEO4J_CFG["host"] , http_port=cfg.NEO4J_CFG["http_port"], https_port=cfg.NEO4J_CFG["https_port"] , bolt_port=cfg.NEO4J_CFG["bolt_port"], user=cfg.NEO4J_CFG["user"], password=cfg.NEO4J_CFG["passwd"])       

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

        result = Licitacao.match(self.graph).where(*conditions).order_by("_.Data").skip(skip).limit(itens)
        
        nodes = []
        for lic in result:
            node = lic.__node__
            node["id"] = "{}-{}-{}".format(lic.cd_ugestora, lic.nu_licitacao, lic.tp_licitacao)
            nodes.append(node)
        
        return(nodes)


    def get_unidades_e_codigos(self):
        result = UnidadeGestora.match(self.graph)
        nodes = []
            
        for uni in result:
            node = uni.__node__
            if uni.nome_unidade_gestora != None:
                nodes.append(node)

        return nodes
    
    def get_licitacao_especifica(self, codUnidadeGestora, codTipoLicitacao, codLicitacao):
        result = self.graph.run("MATCH (l:Licitacao) WHERE l.CodUnidadeGest='{}' AND l.CodTipoLicitacao='{}' AND l.CodLicitacao='{}' RETURN l ".format(codUnidadeGestora, codTipoLicitacao, codLicitacao))
        nodes = [n for n in result]
        return nodes


    def procurando_propostas(self, codUnidadeGestora, codLicitacao, codTipoLicitacao, pagina, limite):
        skip = limite * (pagina - 1)

        result = self.graph.run("MATCH p=()-[r:FEZ_PROPOSTA_EM]->() WHERE r.CodUnidadeGest='{}' and r.CodTipoLicitacao='{}' and r.CodLicitacao='{}'  RETURN r SKIP {} LIMIT {}".format(codUnidadeGestora, codTipoLicitacao, codLicitacao, skip, limite))
        nodes = [n for n in result]
        return nodes


    def get_participantes(self, pagina, itens):
        skip = itens * (pagina - 1)
        result = Participante.match(self.graph).order_by("_.NomeParticipante").skip(skip).limit(itens)
        nodes = [n.__node__ for n in result]
        return nodes


    # Busca participante pelo cpf ou cnpj
    def get_participante_por_codigo(self, codigo):
        result = Participante.match(self.graph).where("_.ChaveParticipante = '{}'".format(codigo))
        nodes = [n.__node__ for n in result]
        return nodes