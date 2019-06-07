from flask import Flask, jsonify, request
from banco import Dao
from flask_cors import CORS
from flask_restplus import Api, Resource


app = Flask(__name__)
api = Api(app=app, doc='/docs')

CORS(app, resources=r"/api/*", headers="Content-Type")

dao = Dao()

@api.route("/api/licitacao")
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
      ano = request.args.get("ano", None, str)
      codUni = request.args.get("codUni", None, str)
      tipoLic = request.args.get("tipoLic", None, str)
      pagina = request.args.get("pagina", 1, int)
      limite = request.args.get("limite", 20, int)
      return jsonify(dao.get_licitacoes(ano, tipoLic, codUni, pagina, limite))


@api.route("/api/participante")
@api.doc(params={'codPart': 'Código do participante que está sendo buscado'})
@api.doc(params={'pagina': 'Página que será acessada'})
@api.doc(params={'limite': 'Quantos resultados serão retornados'})
class Participante(Resource):
   def get(self):
      ''' 
      Retorna os participantes
      '''

      codParticipante = request.args.get("codPart", None, str)
      pagina = request.args.get("pagina", 1, int)
      limite = request.args.get("limite", 20, int)
      return jsonify(dao.get_participantes(codParticipante, pagina, limite))


@app.route('/api')
def olar():
   dao.gerando_query_participante("35422468000159", 1, 10)
   return "inicio"
   

app.run(debug=True)