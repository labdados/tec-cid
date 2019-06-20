from flask import Flask, jsonify, request, Blueprint
from banco import Dao
from flask_cors import CORS
from flask_restplus import Api, Resource

app = Flask(__name__)

blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint, doc='/docs')

app.register_blueprint(blueprint)

CORS(app, resources=r"/api/*", headers="Content-Type")

dao = Dao()

@api.route("/licitacoes")
@api.doc(params={"ano": "Ano das licitações"})
@api.doc(params={"codUni": "Código da unidade gestora"})
@api.doc(params={"tipoLic": "Código do tipo da licitação"})
@api.doc(params={'pagina': 'Página que será acessada'})
@api.doc(params={'limite': 'Quantos resultados serão retornados'})
class Licitacao(Resource):
   def get(self):
      ''' 
      Retorna as licitações baseadas nos filtros que foram passados
      '''
      ano = request.args.get("ano", '', str)
      codUni = request.args.get("codUni", '', str)
      tipoLic = request.args.get("tipoLic", '', str)
      pagina = request.args.get("pagina", 1, int)
      limite = request.args.get("limite", 20, int)
      return jsonify(dao.get_licitacoes(ano, tipoLic, codUni, pagina, limite))


@api.route("/licitacoes/<string:id>/propostas")
@api.doc(params={'pagina': 'Página que será acessada'})
@api.doc(params={'limite': 'Quantos resultados serão retornados'})
class Propostas(Resource):
   def get(self, id):
      '''
      Retorna as propostas que um participante fez em uma determinada licitação
      '''

      data = id.split("-")
      codUnidadeGestora = data[0]
      codLicitacao = data[1]
      codTipoLicitacao = data[2]

      pagina = request.args.get("pagina", 1, int)
      limite = request.args.get("limite", 20, int)

      return jsonify(dao.procurando_propostas(codUnidadeGestora, codLicitacao, codTipoLicitacao, pagina, limite))

@api.route("/licitacoes/<string:id>")
class LicitacaoEspecifica(Resource):
   def get(self, id):
      '''
      Retorna uma licitação específica
      '''
      data = id.split("-")
      codUnidadeGestora = data[0]
      codLicitacao = data[1]
      codTipoLicitacao = data[2]

      return jsonify(dao.get_licitacao_especifica(codUnidadeGestora, codTipoLicitacao, codLicitacao))


@api.route("/participantes")
@api.doc(params={'pagina': 'Página que será acessada'})
@api.doc(params={'limite': 'Quantos resultados serão retornados'})
class Participante(Resource):
   def get(self):
      ''' 
      Retorna os participantes
      '''

      codParticipante = request.args.get("codPart", '', str)
      pagina = request.args.get("pagina", 1, int)
      limite = request.args.get("limite", 20, int)
      return jsonify(dao.get_participantes(pagina, limite))

@api.route("/participantes/<string:id>")
@api.doc(params={'id': 'CPF/CNPJ do participante'})
class ParticipanteEspecifico(Resource):
   def get(self, id):
      '''
      Retorna um participante específico
      '''
      return jsonify(dao.get_participante_por_codigo(id))

@api.route("/unidades_gestoras")
class UnidadesGest(Resource):
   def get(self):
      '''
      Retorna uma lista com os nomes e os códigos das unidades gestoras
      '''
      return jsonify(dao.get_unidades_e_codigos())

app.run(host = '0.0.0.0', debug=True)