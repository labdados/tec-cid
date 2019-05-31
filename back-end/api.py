from flask import Flask, jsonify, request
from banco import Dao
from flask_cors import CORS
from flask_restplus import Api, Resource


app = Flask(__name__)
api = Api(app=app)

CORS(app, resources=r"/api/*", headers="Content-Type")

dao = Dao()

@api.route("/api/licitacao/")
@api.doc(params={'pagina': 'Pagina que sera acessada'})
@api.doc(params={'limite': 'Quantos resultados serão retornados'})
class Licitacao(Resource):
   def get(self):
      ''' 
      Retorna as licitações
      '''
      pagina = request.args.get("pagina", 1, int)
      limite = request.args.get("limite", 20, int)
      return jsonify(dao.get_licitacoes(pagina, limite))


@api.route("/api/participante/")
@api.doc(params={'pagina': 'Pagina que sera acessada'})
@api.doc(params={'limite': 'Quantos resultados serão retornados'})
class Participante(Resource):
   def get(self):
      ''' 
      Retorna os participantes
      '''
      pagina = int(request.args.get("pagina", 1, int))
      limite = int(request.args.get("limite", 20, int))
      return jsonify(dao.get_participantes(pagina, limite))
   

@app.route('/api')
def olar():
    return "inicio"

app.run(debug=True)