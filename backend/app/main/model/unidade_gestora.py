from py2neo.ogm import GraphObject, Property, RelatedTo


class UnidadeGestora(GraphObject):
    cod_unidade_gestora = Property("CodUnidadeGest")
    nome_unidade_gestora = Property("NomeUnidadeGest")

    realizou = RelatedTo("Licitacao", "REALIZOU")

    def __iter__(self):
        return self.__node__