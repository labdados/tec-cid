from ..service.municipio_service import MunicipioService
from flask_restx import Resource, Namespace
from flask import request, jsonify
from datetime import datetime

municipios = MunicipioService()

api = Namespace('Munícipio', 'Operações relacionadas aos municípios')

@api.route("")
@api.doc(params={
   "pagina": "Página que será acessada",
   "limite": "Quantos resultados serão retornados",
   "atributos": "Atributos do município que serão retornados, separados por\
      virgula. Se não for informado, todos serão retornados.\
      Valores válidos: `id, nome, mesoregiao, microregiao,\
      codigo_ibge, codigo_siaf, link_ibge, link_wikipedia, esfera`"
})
class MunicipioList(Resource):
   def get(self):
      '''
      Retorna os municipios
      '''
      pagina = request.args.get("pagina", 1, int)
      limite = request.args.get("limite", 20, int)
      atributos = request.args.get("atributos", '', str)
      result = municipios.get_municipios(pagina, limite, atributos)
      return jsonify({"dados":result})

@api.route("/<string:id>/gestoes")
@api.doc(params={
   "id": "Identificador do município. Pode ser obtido do endpoint '/municipios'",
   "ano": "Filtra a gestão que estava governando o município naquele ano específico"
})
class GestaoList(Resource):
   def get(self, id):
      ano_atual = int(datetime.now().year) # ano default é o atual
      ano = request.args.get("ano", ano_atual, int)
      result = municipios.get_gestoes(id, ano)
      return jsonify({"dados": result})
      

@api.route("/<string:id>")
@api.doc(params={'id': 'ID do município'})
class Municipio(Resource):
   def get(self, id):
      '''
      Retorna um municipio específico
      '''
      municipio = municipios.get_municipio(id)
      return jsonify({"dados": municipio})

