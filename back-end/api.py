from flask import Flask, jsonify, request, Blueprint, url_for, json
from banco import Dao
from flask_cors import CORS
from flask_restplus import Api, Resource, apidoc

api_url_prefix = "/tec-cid/api"
app = Flask(__name__)

class MyCustomApi(Api):
    def _register_apidoc(self, app: Flask) -> None:
        conf = app.extensions.setdefault('restplus', {})
        custom_apidoc = apidoc.Apidoc('restplus_doc', 'flask_restplus.apidoc',
                                      template_folder='templates', static_folder='static',
                                      static_url_path=api_url_prefix)

        @custom_apidoc.add_app_template_global
        def swagger_static(filename: str) -> str:
            return url_for('restplus_doc.static', filename=filename)

        if not conf.get('apidoc_registered', False):
            app.register_blueprint(custom_apidoc)
        conf['apidoc_registered'] = True

blueprint = Blueprint('api', __name__, url_prefix=api_url_prefix)
api = MyCustomApi(blueprint, doc='/docs')
app.register_blueprint(blueprint)

CORS(app, resources=r"/tec-cid/api/*", headers="Content-Type")

dao = Dao()   
   

@api.route("/licitacoes")
@api.doc(params={
   "codUni": "Código da unidade gestora",
   "tipoLic": "Código do tipo da licitação",
   "dataInicio": "Data de início de um intervalo de tempo, no formato `AAAA-MM-DD`.",
   "dataFim": "Data de término de um intervalo de tempo, no formato `AAAA-MM-DD`.",
   "limite": "Quantos resultados serão retornados",
   "pagina": "Página que será acessada",
   "ordenarPor": "Nome do campo pelo qual a lista deve ser ordenada.",
   "ordem": "O sentido da ordenação: `ASC` para A a Z ou 0 a 9, e `DESC` para Z a A ou 9 a 0."
})
class Licitacao(Resource):
   def get(self):
      ''' 
      Retorna as licitações baseadas nos filtros que foram passados
      '''
      data_inicio = request.args.get("dataInicio", '', str)
      data_fim = request.args.get("dataFim", '', str)
      cod_uni = request.args.get("codUni", '', str)
      tipo_lic = request.args.get("tipoLic", '', str)
      pagina = request.args.get("pagina", 1, int)
      limite = request.args.get("limite", 20, int)
      ordenar_por = request.args.get("ordenarPor", "Data", str)
      ordem = request.args.get("ordem", '', str)
      licitacoes = dao.get_licitacoes(cod_uni, tipo_lic, data_inicio, data_fim,
                                      pagina, limite, ordenar_por, ordem)
      
      licitacoes =  json.dumps({"dados": licitacoes})
      total = dao.count_lic

      response = gera_response(licitacoes, total)

      return response

def gera_response(results, x_total_count):
   response = app.response_class(response=results, headers={
         "X-Total-Count": x_total_count
      }, mimetype="application/json")
   
   return response

@api.route("/licitacoes/<string:id>/propostas")
@api.doc(params={'id': 'id da licitação'})
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

      results = json.dumps(dao.procura_propostas(codUnidadeGestora, codLicitacao, codTipoLicitacao, pagina, limite))

      response = gera_response(results, dao.count_props)

      return response


@api.route("/licitacoes/<string:id>")
@api.doc(params={'id': 'id da licitação'})
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

      participantes =  json.dumps(dao.get_participantes(pagina, limite))
      total = dao.count_part

      response = gera_response(participantes, total)

      return response



@api.route("/participantes/<string:id>")
@api.doc(params={'id': 'CPF/CNPJ do participante'})
class ParticipanteEspecifico(Resource):
   def get(self, id):
      '''
      Retorna um participante específico
      '''
      return jsonify(dao.get_participante_por_codigo(id))

@api.route("/unidades-gestoras")
class UnidadesGest(Resource):
   def get(self):
      '''
      Retorna uma lista com os nomes e os códigos das unidades gestoras
      '''
      return jsonify(dao.get_unidades_e_codigos())

app.run(host = '0.0.0.0', debug=True)
