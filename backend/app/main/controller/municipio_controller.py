from ..service.municipio_service import Municipio_Service
from flask_restplus import Resource, Namespace
from flask import request, jsonify

municipios = Municipio_Service()

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
      municipios = dao.get_municipios(pagina, limite)
      return jsonify({"dados": municipios})