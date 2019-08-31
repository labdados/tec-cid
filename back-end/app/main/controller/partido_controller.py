from ..service.partido_service import Partido_Service
from flask_restplus import Resource, Namespace
from flask import request, jsonify

partidos = Partido_Service()

api = Namespace('Partido', 'Operações relacionadas a partidos políticos')

@api.route("")
@api.doc(params={'pagina': 'Página que será acessada'})
@api.doc(params={'limite': 'Quantos resultados serão retornados'})
class Partidos(Resource):
   def get(self):
      '''
      Retorna os partidos
      '''
      pagina = request.args.get("pagina", 1, int)
      limite = request.args.get("limite", 20, int)
      partidos = partidos.get_partidos(pagina, limite)
      return jsonify({"dados": partidos})