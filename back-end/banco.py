from py2neo import Graph

class Dao:
    def __init__(self):
        self.graph = Graph("bolt://localhost:7687", auth=("neo4j", "tcctcc"))
        self.num_pag_licitacoes = 0
        self.num_pag_participantes = 0


    def get_licitacoes(self, num_resultados):
        result = self.graph.run('match (lic:Licitacao) return lic ORDER BY lic.Data SKIP {num_pag} limit {num}',num_pag = self.num_pag_licitacoes, num=num_resultados)
        self.num_pag_licitacoes += 1
        nodes = [n for n in result]
        return nodes

    def get_participantes(self, num_resultados):
        result = self.graph.run('match (part:Participante) return part ORDER BY part.NomeParticipante SKIP {num_pag} limit {num}', num_pag=self.num_pag_participantes, num=num_resultados)
        self.num_pag_participantes += 1
        nodes = [n for n in result]
        return nodes

    def get_licitacao_nomeunidadegestora(self, nome):
        result = self.graph.run('match (lic:Licitacao{NomeUnidadeGest:$nome}) return lic', nome=nome)
        nodes = [n for n in result]
        return nodes

    def get_licitacao_por_ano(self, ano):
        result = self.graph.run('match (lic:Licitacao) WHERE lic.Data CONTAINS {ano} return lic', ano=str(ano))
        nodes = [n for n in result]
        return nodes

    # Busca participante pelo cpf ou cnpj
    def get_participante_por_codigo(self, codigo):
        result = self.graph.run("match (part:Participante{ChaveParticipante:$codigo}) return part", codigo=codigo)
        nodes = [n for n in result]
        return nodes

