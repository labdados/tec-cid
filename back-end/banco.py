from py2neo import Graph
from models import Licitacao, Participante, UnidadeGestora
from settings import *

class Dao:
    def __init__(self):
        self.graph = Graph(host=NEO4J_CFG["host"] , port=NEO4J_CFG["port"],
                           user=NEO4J_CFG["user"], password=NEO4J_CFG["passwd"])

    def get_licitacoes(self, ano, tipo, unidade, pagina, itens, ordenar_por, ordem):
        skip = itens * (pagina - 1)
        
        filtros = {}
        conditions = ["_.Valor IS NOT NULL"]

        if ano:
            conditions.append("_.Data ENDS WITH '{}'".format(ano))

        if tipo:
            conditions.append("_.CodTipoLicitacao = '{}'".format(tipo))

        if unidade:
            conditions.append("_.CodUnidadeGest = '{}'".format(unidade))

        if not ordenar_por:
            ordenar_por = "_.Data"
        else:
            ordenar_por = "_." + ordenar_por

        if ordem.upper() in ["DESC", "ASC"]:
            ordenar_por += " {}".format(ordem)

        result = Licitacao.match(self.graph).where(*conditions).order_by(ordenar_por).skip(skip).limit(itens)
        nodes = []
        for lic in result:
            node = lic.__node__
            node["id"] = "{}-{}-{}".format(lic.cd_ugestora, lic.nu_licitacao, lic.tp_licitacao)
            node["Data"] = node["Data"].__str__()
            nodes.append(node)
        
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

