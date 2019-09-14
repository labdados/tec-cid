from py2neo.ogm import GraphObject, Property

class Candidato(GraphObject):
    cpf = Property("CPF")
    nome = Property("Nome")
    num_candidato = Property("NumCandidato")
    sigla_partido = Property("SiglaPartido")

    def __iter__(self):
        return self.__node__