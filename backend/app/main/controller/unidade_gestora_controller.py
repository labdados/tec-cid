from ..service.unidade_gestora_service import UnidadeGestoraService
from flask_restplus import Resource, Namespace
from flask import jsonify

unidades = UnidadeGestoraService()

api = Namespace('Unidade Gestora', description='Operações relacionadas as unidades gestoras')

@api.route("")
class UnidadesGestoraList(Resource):
   def get(self):
      '''
      Retorna uma lista com os nomes e os códigos das unidades gestoras
      '''
      result = unidades.get_unidades_gestoras()
      return jsonify({"dados": result})