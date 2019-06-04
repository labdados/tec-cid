from flask import Flask, jsonify, request
from banco import Dao
from flask_cors import CORS
from flask_restplus import Api, Resource


app = Flask(__name__)
api = Api(app=app, doc='/docs')

CORS(app, resources=r"/api/*", headers="Content-Type")

dao = Dao()

@api.route("/api/licitacao")
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

@api.route("/api/licitacao/")
@api.doc(params={'ano': 'Ano das licitações'})
@api.doc(params={'pagina': 'Pagina que sera acessada'})
@api.doc(params={'limite': 'Quantos resultados serão retornados'})
class Licitacao_por_ano(Resource):
   def get(self):
      '''
      Retorna as licitações de determinado ano
      '''
      ano = request.args.get("ano", 2003, int)
      pagina = request.args.get("pagina", 1, int)
      limite = request.args.get("limite", 20, int)
      return jsonify(dao.get_licitacao_por_ano(ano, pagina, limite))

@api.route("/api/licitacao/unidade_gestora")
@api.doc(params={'unidade': 'Unidade gestora'})
class Licitacao_por_unidade_gestora(Resource):
   def get(self):
      '''
      Retorna as licitações de uma unidade gestora
      '''
      unidade = request.args.get('unidade', 'Câmara Municipal de Rio Tinto', str)
      return jsonify(dao.get_licitacao_nomeunidadegestora(unidade))

@api.route("/api/participante")
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


@api.route("/api/participante/codigo")
@api.doc(params={"cod": "CPF ou CNPJ do participante"})
class Participante_por_codigo(Resource):
   def get(self):
      '''
      Retorna o participante que tem determinado CPF/CNPJ
      '''
      codigo = request.args.get("cod", '35422468000159', str)
      return jsonify(dao.get_participante_por_codigo(codigo))
   

@app.route('/api')
def olar():
    return "inicio"

app.run(debug=True)