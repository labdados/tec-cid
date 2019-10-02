from py2neo.ogm import GraphObject, Property, RelatedTo

class UnidadeGestora(GraphObject):
    cd_ugestora = Property()
    nome = Property()
    municipio = Property()
    jurisdicionado_id = Property()
    nome_tipo_jurisdicionado = Property()
    nome_tipo_administracao_jurisdicionado = Property()
    nome_esfera_jurisdicionado = Property()

    realizou = RelatedTo("Licitacao")
    pertence_a = RelatedTo("Municipio")

    def __iter__(self):
        return self.__node__