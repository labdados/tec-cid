from ..service.unidade_gestora_service import UnidadeGestoraService
from flask_restx import Resource, Namespace
from flask import jsonify, request

unidades = UnidadeGestoraService()

api = Namespace('Unidade Gestora', description='Operações relacionadas as unidades gestoras')

@api.route("")
@api.doc(params={"nomeMunicipio": "Unidades gestoras deste munícipio específico",
                 "idMunicipio": "ID do municipio"})
class UnidadesGestoraList(Resource):
   def get(self):
      '''
      Retorna uma lista com os nomes e os códigos das unidades gestoras
      '''
      nome_municipio = request.args.get("nomeMunicipio", "", str)
      id_municipio = request.args.get("idMunicipio", "", str)
      result = unidades.get_unidades_gestoras(nome_municipio, id_municipio)
      return jsonify({"dados": result})
   