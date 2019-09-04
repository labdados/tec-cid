from py2neo.ogm import GraphObject, Property, RelatedFrom, RelatedTo

class Licitacao(GraphObject):
    cd_ugestora = Property("CodUnidadeGest")
    nu_licitacao = Property("CodLicitacao")
    tp_licitacao = Property("CodTipoLicitacao")
    de_tipolicitacao = Property("TipoLicitacao")
    tp_objeto = Property("CodObj")
    dt_homologacao = Property("Data")
    de_tipoobjeto = Property("NomeObg")
    de_obs = Property("Obs")
    vl_licitacao = Property("Valor")
    
    propostas = RelatedFrom("Participante", "FEZ_PROPOSTA_EM")
    unidade_gestora = RelatedFrom("UnidadeGestora", "REALIZOU")
    
    def __iter__(self):
        return self.__node__

class Licitacao2(GraphObject):
    __primarykey__ = "uuid"
    
    uuid = Property("uuid")
    cd_ugestora = Property("cd_ugestora")
    de_Obs = Property("de_Obs")
    de_TipoLicitacao = Property("de_TipoLicitacao")
    de_TipoObjeto = Property("de_TipoObjeto")
    de_ugestora = Property("de_ugestora")
    dt_Homologacao = Property("dt_Homologacao")
    nu_Licitacao = Property("nu_Licitacao")
    tp_Licitacao = Property("tp_Licitacao")
    tp_Objeto = Property("tp_Objeto")
    vl_Licitacao = Property("vl_Licitacao")
    
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


class UnidadeGestora(GraphObject):
    cod_unidade_gestora = Property("CodUnidadeGest")
    nome_unidade_gestora = Property("NomeUnidadeGest")

    realizou = RelatedTo("Licitacao", "REALIZOU")

    def __iter__(self):
        return self.__node__


class Candidato(GraphObject):
    cpf = Property("CPF")
    nome = Property("Nome")
    num_candidato = Property("NumCandidato")
    sigla_partido = Property("SiglaPartido")

    def __iter__(self):
        return self.__node__


class Partido(GraphObject):
    num_partido = Property("NumeroPartido")
    siglaPartido = Property("SiglaPartido")

    def __iter__(self):
        return self.__node__


class Municipio(GraphObject):
    cod_sagres = Property("codigo_sagres")
    municipio_importacao = Property("municipioImportacao")

    def __iter__(self):
        return self.__node__
