from flask import Flask, jsonify, render_template, request
from py2neo import Graph
from banco import Dao
from flask_cors import CORS
from paginacao import Paginacao

app = Flask(__name__)

CORS(app, resources=r"/api/*", headers="Content-Type")

tipo_licitacao = "lic"
tipo_participante = "part"

dao = Dao()
pag = Paginacao(dao)


@app.route('/api')
def olar():
    return "inicio"

###########  Rotas para as licitações  ###############

@app.route('/api/licitacoes/', defaults={'page': 1, 'limite': 10})
@app.route("/api/licitacoes/pagina/<int:page>/limite/<int:limite>", methods=["GET"])
def show_licitacoes(page, limite):
   #page = request.args.get("page", 1)
   #limite = request.args.get("limite", 10)
   return jsonify(pag.get_licitacoes(page, limite, tipo_licitacao))

###########  Rotas para os participantes  ###############

@app.route('/api/participantes/', defaults={'page': 1, 'limite': 10})
@app.route("/api/participantes/pagina/<int:page>/limite/<int:limite>", methods=["GET"])
def show_participantes(page, limite):
   return jsonify(pag.get_participantes(page, limite, tipo_participante))

###########  Rotas para as buscas  ###############

@app.route("/api/licitacoes/unidadeGestora/<string:unidade>", methods=["GET"])
def procura_licitacoes_de_unidade_gestora(unidade):
   return jsonify(dao.get_licitacao_nomeunidadegestora(unidade))

@app.route("/api/licitacoes/ano/<int:ano>", methods=["GET"])
def procura_licitacoes_por_ano(ano):
   return jsonify(dao.get_licitacao_por_ano(ano))

@app.route("/api/participante/codigo/<string:codigo>", methods=["GET"])
def procura_participante_por_codigo(codigo):
   return jsonify(dao.get_participante_por_codigo(codigo))


app.run(debug=True)