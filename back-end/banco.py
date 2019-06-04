from py2neo import Graph
import config as cfg 

class Dao:
    def __init__(self):
        self.graph = Graph(cfg.NEO4J_CFG["host"], auth=(cfg.NEO4J_CFG["user"], cfg.NEO4J_CFG["passwd"]))

    def get_licitacoes(self, page, num_resultados):
        skip = num_resultados * (page - 1)
        result = self.graph.run('MATCH (lic:Licitacao) RETURN lic ORDER BY lic.Data SKIP {skip} LIMIT {num}', skip=skip, num=num_resultados)
        nodes = [n for n in result]
        return nodes

    def get_participantes(self, page, num_resultados):
        skip = num_resultados * (page - 1)
        result = self.graph.run('MATCH (part:Participante) return part ORDER BY part.NomeParticipante SKIP {skip} limit {num}', skip=skip, num=num_resultados)
        nodes = [n for n in result]
        return nodes

    def get_licitacao_nomeunidadegestora(self, nome):
        print("a")
        result = self.graph.run('MATCH (lic:Licitacao{NomeUnidadeGest:$nome}) return lic', nome=nome)
        nodes = [n for n in result]
        print("tamanho do resultado: ", len(nodes))
        return nodes

    def get_licitacao_por_ano(self, ano, page, limite):
        skip = limite * (page - 1)
        result = self.graph.run('MATCH (lic:Licitacao) WHERE lic.Data CONTAINS {ano} RETURN lic ORDER BY lic.Data SKIP {skip} LIMIT {limit}', ano=str(ano), skip=skip, limit=limite)
        nodes = [n for n in result]
        print("tamanho do resultado: ", len(nodes))
        return nodes

    # Busca participante pelo cpf ou cnpj
    def get_participante_por_codigo(self, codigo):
        result = self.graph.run("MATCH (part:Participante{ChaveParticipante:$codigo}) return part", codigo=codigo)
        nodes = [n for n in result]
        return nodes

