from py2neo.ogm import GraphObject, Property, RelatedFrom, RelatedTo

class Licitacao(GraphObject):
    cd_ugestora = Property("CodUnidadeGest")
    nu_licitacao = Property("CodLicitacao")
    tp_licitacao = Property("CodTipoLicitacao")
    de_tipolicitacao = TipoLicitacao = Property("TipoLicitacao")
    tp_objeto = Property("CodObj")
    dt_homologacao = Property("Data")
    de_tipoobjeto = Property("NomeObg")
    de_obs = Property("Obs")
    vl_licitacao = Property("Valor")
    
    propostas = RelatedFrom("Participante", "FEZ_PROPOSTA_EM")
    unidade_gestora = RelatedFrom("UnidadeGestora", "REALIZOU")
    
    def __iter__(self):
        return self.__node__


class Participante(GraphObject):
    chave_participante = Property("ChaveParticipante")
    nome_participante = Property("NomeParticipante")

    licitacoes_que_participou = RelatedTo("Licitacao", "FEZ_PROPOSTA_EM")

    def __iter__(self):
        return self.__node__