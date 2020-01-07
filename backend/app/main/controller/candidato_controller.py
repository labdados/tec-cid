from ..service.candidato_service import CandidatoService
from flask_restplus import Resource, Namespace, fields
from flask import request, jsonify
from ..model.api_models import ModelFactory

candidato_service = CandidatoService()

api = Namespace('Candidato', 'Operações relacionadas aos candidatos de partidos políticos')

swagger_doc = ModelFactory(api)

@api.route("")
@api.doc(params={'pagina': 'Página que será acessada'})
@api.doc(params={'limite': 'Quantos resultados serão retornados'})
class CandidatoList(Resource):
   @api.marshal_with(swagger_doc.candidato_swagger(), as_list=True, description='Retorna uma lista de candidatos')
   def get(self):
      '''
      Retorna os candidatos
      '''
      pagina = request.args.get("pagina", 1, int)
      limite = request.args.get("limite", 20, int)
      candidatos = candidato_service.get_candidatos(pagina, limite)
      return jsonify({"dados": candidatos})
   
@api.route("/<string:id>")
@api.doc(params={"id": "ID do candidato"})
class Candidato(Resource):
       @api.marshal_with(swagger_doc.candidato_swagger())
       def get(self, id):
         '''
         Retorna um candidato específico 
         '''
         candidato = candidato_service.get_candidato(id)
         return jsonify({"dados": candidato})

@api.route("/<string:id>/doacoes")
@api.doc(params={"id": "ID do candidato"})
class DoacoesList(Resource):
   @api.marshal_with(swagger_doc.doacoes_swagger(), as_list=True)
   def get(self, id):
      '''
      Retorna as doações que determinado candidato recebeu 
      '''
      doacoes = candidato_service.get_doacoes(id)
      return jsonify({"dados": doacoes})