from py2neo import Graph
import config as cfg 

class Dao:
    def __init__(self):
        self.graph = Graph(cfg.NEO4J_CFG["host"], auth=(cfg.NEO4J_CFG["user"], cfg.NEO4J_CFG["passwd"]))

    def get_licitacoes(self, ano, tipo, unidade, page, num_resultados):

        query = self.gerando_query_licitacao(ano, tipo, unidade, page, num_resultados)
        result = self.graph.run(query)
        nodes = [n for n in result]

        for n in nodes:
            n[0]['id'] = "{}-{}-{}".format(n[1], n[2], n[3])

        return nodes

    def get_participantes(self, pagina, limite):
        skip = limite * (pagina - 1)
        result = self.graph.run("MATCH (part:Participante) RETURN part ORDER BY part.NomeParticipante SKIP {} LIMIT {}".format(skip, limite))
        nodes = [n for n in result]
        return nodes

    # Busca participante pelo cpf ou cnpj
    def get_participante_por_codigo(self, codigo):
        result = self.graph.run("MATCH (part:Participante{ChaveParticipante:$codigo}) return part", codigo=codigo)
        nodes = [n for n in result]
        return nodes
          
    # Gera a query baseada nos filtros que foram passados
    def gerando_query_licitacao(self, ano, tipo, unidade, pagina, limite):
        skip = limite * (pagina - 1)

        last = False
        query = "MATCH (lic:Licitacao) "

        if ano != '':
            query += "WHERE lic.Data CONTAINS '{}' ".format(ano)
            last = True

        if unidade != '' and last == True:
            query += "AND lic.CodUnidadeGest = '{}' ".format(unidade)
            last = True
        elif unidade != '' and last == False:
            query += "WHERE lic.CodUnidadeGest = '{}' ".format(unidade)
            last = True

        if tipo != '' and last == True:
            query += "AND lic.CodTipoLicitacao = '{}' ".format(tipo)
        elif tipo != '' and last == False:
            query += "WHERE lic.CodTipoLicitacao = '{}' ".format(tipo)
        
        query += "RETURN lic, lic.CodUnidadeGest, lic.CodTipoLicitacao, lic.CodLicitacao ORDER BY lic.Data SKIP {} LIMIT {}".format(skip, limite)


        return query
    
    def procurando_propostas(self, codUnidadeGestora, codTipoLicitacao, codLicitacao, pagina, limite):
        skip = limite * (pagina - 1)
        result = self.graph.run("MATCH p=()-[r:FEZ_PROPOSTA_EM]->() WHERE r.CodUnidadeGest='{}' and r.CodTipoLicitacao='{}' and r.CodLicitacao='{}'  RETURN r SKIP {} LIMIT {}".format(codUnidadeGestora, codTipoLicitacao, codLicitacao, skip, limite))
        nodes = [n for n in result]
        return nodes

    def get_licitacao_especifica(self, codUnidadeGestora, codTipoLicitacao, codLicitacao):
        result = self.graph.run("MATCH (l:Licitacao) WHERE l.CodUnidadeGest='{}' AND l.CodTipoLicitacao='{}' AND l.CodLicitacao='{}' RETURN l ".format(codUnidadeGestora, codTipoLicitacao, codLicitacao))
        nodes = [n for n in result]
        return nodes
