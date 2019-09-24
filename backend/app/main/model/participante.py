from py2neo.ogm import GraphObject, Property, RelatedTo

class Participante(GraphObject):
    chave_participante = Property("ChaveParticipante")
    nome_participante = Property("NomeParticipante")

    licitacoes_que_participou = RelatedTo("Licitacao", "FEZ_PROPOSTA_EM")

    def __iter__(self):
        return self.__node__