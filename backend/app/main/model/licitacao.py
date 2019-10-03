from py2neo.ogm import GraphObject, Property, RelatedFrom

class Licitacao(GraphObject):
    cd_ugestora = Property()
    cd_modalidade = Property()
    numero_licitacao = Property()
    modalidade = Property()
    objeto = Property()
    valor_estimado = Property()
    valor_licitado = Property()
    data_homologacao = Property()
    ano_homologacao = Property()
    situacao_fracassada = Property()
    nome_estagio_processual = Property()
    nome_setor_atual = Property()
    url = Property()
    
    propostas = RelatedFrom("Participante", "FEZ_PROPOSTA_EM")
    unidades_gestoras = RelatedFrom("UnidadeGestora", "REALIZOU")
    
    def __iter__(self):
        return self.__node__