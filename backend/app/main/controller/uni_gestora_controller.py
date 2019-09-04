from ..service.unidades_gestoras_service import Unidade_Gestora_Service
from flask_restplus import Resource, Namespace
from flask import jsonify

unidades = Unidade_Gestora_Service()

api = Namespace('Unidade Gestora', description='Operações relacionadas as unidades gestoras')

@api.route("")
class UnidadesGest(Resource):
   def get(self):
      '''
      Retorna uma lista com os nomes e os códigos das unidades gestoras
      '''
      result = unidades.get_unidades_e_codigos()
      return jsonify({"dados": result})