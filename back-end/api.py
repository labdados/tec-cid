from flask import Flask, jsonify, render_template
from py2neo import Graph
from banco import Dao
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources=r"/api/*", headers="Content-Type")

dao = Dao()

@app.route('/api')
def olar():
    return "inicio"

@app.route('/api/licitacoes')
def get_json_licitacoes():
   result = dao.get_licitacoes(10)
   return jsonify(result)

@app.route('/api/participantes')
def get_json_participantes():
   result = dao.get_participantes(10)
   return jsonify(result)

app.run(debug=True)