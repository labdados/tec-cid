#from unidades_gestoras_service import Unidades_Gestoras_Service
from ..service.unidades_gestoras_service import Unidade_Gestora_Service
from flask_restplus import Namespace, Resource
from flask import jsonify

unidades = Unidade_Gestora_Service()

api = Namespace('Unidade Gestora', description='Operações relacionadas as unidades gestoras')

@api.route("")
class UnidadesGest(Resource):
   def get(self):
      '''
      Retorna uma lista com os nomes e os códigos das unidades gestoras
      '''
      return jsonify(unidades.get_unidades_e_codigos())