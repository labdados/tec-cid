from py2neo import Graph
from models import Licitacao, Participante, UnidadeGestora
import config as cfg

class Dao:
    def __init__(self):
        self.graph = Graph(host=cfg.NEO4J_CFG["host"] , http_port=cfg.NEO4J_CFG["http_port"], https_port=cfg.NEO4J_CFG["https_port"] , bolt_port=cfg.NEO4J_CFG["bolt_port"], user=cfg.NEO4J_CFG["user"], password=cfg.NEO4J_CFG["passwd"])
        self.count_lic = self.get_count("Licitacao")
        self.count_part = self.get_count("Participante")


    def get_count(self, tipo):
        result = self.graph.run("MATCH (l:{}) RETURN count(*)".format(tipo)).data()
        dic = result[0]
        count = dic['count(*)']
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

        result = Licitacao.match(self.graph).where(*conditions).order_by("_.Data").skip(skip).limit(itens)
        
        nodes = []
        for lic in result:
            node = lic.__node__
            node["id"] = "{}-{}-{}".format(lic.cd_ugestora, lic.nu_licitacao, lic.tp_licitacao)
            nodes.append(node)

        nodes.append(self.secao_de_links(pagina, itens, ano, tipo, unidade))
        return(nodes)

    def secao_de_links_participantes(self, pagina, limite):
        url = "http://localhost:5000/tec-cid/api/participantes"

        last = int(self.count_part / limite)
        prox = pagina + 1

        links = {"links": [
            {
                "rel": "self",
                "href": url + "?pagina={page}&limite={limite}".format(page = pagina, limite = limite)
            },
            {
                "rel": "next",
                "href": url + "?pagina={page}".format(page=prox)
            },
            {
                "rel": "first",
                "href": url
            },
            {
                "rel": "last",
                "href": url + "?pagina={page}".format(page=last)
            },
        ]}
        return links


    def secao_de_links(self, pagina, limite, ano="", tipo="", unidade=""):
        #url = "http://labdados.dcx.ufpb.br/tec-cid/api/licitacoes"
        url = "http://localhost:5000/tec-cid/api/licitacoes"

        last = int(self.count_lic / limite)
        prox = pagina + 1

        links = {"links": [
            {
                "rel": "self",
                "href": url + "&limite={limite}&pagina={pagina}&ano={ano}&tipoLic={tipoLic}&codUni={codUni}".format(limite = limite, pagina = pagina, ano = ano, tipoLic = tipo, codUni = unidade)
            },
            {
                "rel": "next",
                "href": url + "?pagina={page}".format(page = prox)
            },
            {
                "rel": "first",
                "href": url
            },
            {
                "rel": "last",
                "href": url + "?pagina={pagina}".format(pagina = last)
            }
        ]}

        return links

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
        nodes.append(self.secao_de_links_participantes(pagina, itens))
        return nodes

    # Busca participante pelo cpf ou cnpj
    def get_participante_por_codigo(self, codigo):
        result = Participante.match(self.graph).where("_.ChaveParticipante = '{}'".format(codigo))
        nodes = [n.__node__ for n in result]
        return nodes          

