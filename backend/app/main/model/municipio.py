from py2neo.ogm import GraphObject, Property, RelatedFrom

class Municipio(GraphObject):
    id = Property()
    uf = Property()
    nome = Property()
    mesoregiao = Property()
    microregiao = Property()
    codigo_ibge = Property()
    codigo_siaf = Property()
    link_ibge = Property()
    bandeira = Property()
    brasao = Property()
    link_wikipedia = Property()
    esfera = Property()
    cancelled = Property()

    prefeitos = RelatedFrom("Candidato", "GOVERNA")
    unidades_gestoras = RelatedFrom("UnidadeGestora", "PERTENCE_A")

    def __iter__(self):
        return self.__node__