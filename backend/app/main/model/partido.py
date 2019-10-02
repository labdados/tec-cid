from py2neo.ogm import GraphObject, Property, RelatedFrom

class Partido(GraphObject):
    nome = Property()
    numero = Property()
    sigla = Property()

    candidatos = RelatedFrom("Candidato", "FILIADO_A")

    def __iter__(self):
        return self.__node__