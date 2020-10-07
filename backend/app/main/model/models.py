from py2neo.ogm import GraphObject, Property, RelatedTo, RelatedFrom

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

class Licitacao(GraphObject):
    cd_ugestora = Property()
    cd_tipo_licitacao = Property()
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


class Candidato(GraphObject):
    cpf = Property()
    cd_eleicao = Property()
    tipo_eleicao = Property()
    ano_eleicao = Property()
    uf = Property()
    municipio = Property()
    unidade_estadual = Property()
    nome = Property()
    nome_urna = Property()
    numero = Property()
    sigla_partido = Property()
    coligacao = Property()
    cargo = Property()
    situacao = Property()
    data_nascimento = Property()
    titulo_eleitoral = Property()
    genero = Property()
    grau_instrucao = Property()
    raca = Property()
    ocupacao = Property()

    filiado_a = RelatedTo("Partido")
    governa = RelatedTo("Municipio")

    def __iter__(self):
        return self.__node__
    
class Participante(GraphObject):
    cpf_cnpj = Property()
    nome = Property()

    fez_proposta_em = RelatedTo("Licitacao")

    def __iter__(self):
        return self.__node__

class Partido(GraphObject):
    nome = Property()
    numero = Property()
    sigla = Property()

    candidatos = RelatedFrom("Candidato", "FILIADO_A")

    def __iter__(self):
        return self.__node__
