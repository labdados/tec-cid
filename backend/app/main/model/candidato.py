from py2neo.ogm import GraphObject, Property, RelatedTo

class Candidato(GraphObject):
    cpf = Property()
    cd_eleicao = Property()
    ano_eleicao = Property()
    uf = Property()
    municipio = Property()
    nome = Property()
    nome_urna = Property()
    numero = Property()
    sigla_partido = Property()
    coligacao = Property()
    cargo = Property()
    situacao = Property()
    genero = Property()
    grau_instrucao = Property()
    raca = Property()
    ocupacao = Property()

    filiado_a = RelatedTo("Partido")
    governa = RelatedTo("Municipio")

    def __iter__(self):
        return self.__node__