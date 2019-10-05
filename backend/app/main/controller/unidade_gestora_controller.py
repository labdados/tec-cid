from ..service.unidade_gestora_service import UnidadeGestoraService
from flask_restplus import Resource, Namespace
from flask import jsonify, request

unidades = UnidadeGestoraService()

api = Namespace('Unidade Gestora', description='Operações relacionadas as unidades gestoras')

@api.route("")
@api.doc(params={"nomeMunicipio": "Unidades gestoras deste munícipio específico"})
class UnidadesGestoraList(Resource):
   def get(self):
      '''
      Retorna uma lista com os nomes e os códigos das unidades gestoras
      '''
      nome_municipio = request.args.get("nomeMunicipio", "", str)
      result = unidades.get_unidades_gestoras(nome_municipio)
      return jsonify({"dados": result})
   