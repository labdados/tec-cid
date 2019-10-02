from py2neo.ogm import GraphObject, Property, RelatedTo

class Participante(GraphObject):
    cpf_cnpj = Property()
    nome = Property()

    fez_proposta_em = RelatedTo("Licitacao")

    def __iter__(self):
        return self.__node__