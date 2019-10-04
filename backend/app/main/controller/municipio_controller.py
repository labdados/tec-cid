from ..service.municipio_service import MunicipioService
from flask_restplus import Resource, Namespace
from flask import request, jsonify

municipios = MunicipioService()

api = Namespace('Munícipio', 'Operações relacionadas aos municípios')

@api.route("")
@api.doc(params={'pagina': 'Página que será acessada'})
@api.doc(params={'limite': 'Quantos resultados serão retornados'})
class Municipios(Resource):
   def get(self):
      '''
      Retorna os municipios
      '''
      pagina = request.args.get("pagina", 1, int)
      limite = request.args.get("limite", 20, int)
      result = municipios.get_municipios(pagina, limite)
      return jsonify({"dados": result})

@api.route("/<string:id>")
@api.doc(params={'id': 'ID do municipio'})
class Municipio(Resource):
   def get(self, id):
      '''
      Retorna um municipio específico
      '''
      municipio = municipios.get_municipio(id)
      return jsonify({"dados": municipio})