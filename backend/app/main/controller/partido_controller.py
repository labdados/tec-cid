from ..service.partido_service import PartidoService
from flask_restx import Resource, Namespace
from flask import request, jsonify

partidos = PartidoService()

api = Namespace('Partido', 'Operações relacionadas a partidos políticos')

@api.route("")
@api.doc(params={'pagina': 'Página que será acessada'})
@api.doc(params={'limite': 'Quantos resultados serão retornados'})
class PartidoList(Resource):
   def get(self):
      '''
      Retorna os partidos
      '''
      pagina = request.args.get("pagina", 1, int)
      limite = request.args.get("limite", 20, int)
      result = partidos.get_partidos(pagina, limite)
      return jsonify({"dados": result})