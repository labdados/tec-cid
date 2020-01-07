from flask_restplus import fields

class ModelFactory:
    def __init__(self, api):
        self.api = api
        
    def candidato_swagger(self):
        return self.api.model('Candidato', {
            'ano_eleicao': fields.Integer,
            'cargo': fields.String,
            'cd_eleicao': fields.String,
            'coligacao': fields.String,
            'cpf': fields.String,
            'genero': fields.String,
            'grau_instrucao': fields.String,
            'id': fields.String,
            'municipio': fields.String,
            'nome': fields.String,
            'nome_urna': fields.String,
            'numero': fields.String,
            'ocupacao': fields.String,
            'raca': fields.String,
            'sigla_partido': fields.String,
            'situacao': fields.String,
            'uf': fields.String,
            'tipo_eleicao': fields.String,
        })
        
    def doacoes_swagger(self):
        return self.api.model('Doações', {
            'cpf_cnpj_doador': fields.String,
            'descricao_receita': fields.String,
            'fonte_recurso': fields.String,
            'nome_doador': fields.String,
            'tipo_receita': fields.String,
            'valor_receita': fields.Float,
        })
        
    def licitacoes_swagger(self):
        return self.api.model('Licitação', {
            "ano_homologacao": fields.Integer,
            "cd_modalidade": fields.String,
            "cd_ugestora": fields.String,
            "data_homologacao": fields.String,
            "id": fields.String,
            "modalidade": fields.String,
            "nome_estagio_processual": fields.String,
            "nome_setor_atual": fields.String,
            "nome_unidade_gestora": fields.String,
            "numero_licitacao": fields.String,
            "objeto": fields.String,
            "situacao_fracassada": fields.String,
            "url": fields.String,
            "valor_licitado": fields.Float,
        })
        
    def propostas_swagger(self):
        return self.api.model('Propostas', {
            'cd_modalidade_licitacao': fields.String,
            'cd_ugestora': fields.String,
            'cpf_cnpj_participante': fields.String,
            'nome_participante': fields.String,
            'numero_licitacao': fields.String,
            'situacao_proposta': fields.String,
            'valor_proposta': fields.Float,
        })
        
    