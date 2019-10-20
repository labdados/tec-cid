from ..service.candidato_service import CandidatoService
from flask_restplus import Resource, Namespace
from flask import request, jsonify

candidato_service = CandidatoService()

api = Namespace('Candidato', 'Operações relacionadas aos candidatos de partidos políticos')

@api.route("")
@api.doc(params={'pagina': 'Página que será acessada'})
@api.doc(params={'limite': 'Quantos resultados serão retornados'})
class CandidatoList(Resource):
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
       def get(self, id):
         '''
         Retorna um candidato específico 
         '''
         candidato = candidato_service.get_candidato_por_id(id)
         return jsonify({"dados": candidato})

@api.route("<string:id>/doacoes")
@api.doc(params={"id": "ID do candidato"})
class DoacoesList(Resource):
   def get(self, id):
      '''
      Retorna as doações que determinado candidato recebeu 
      '''
      doacoes = candidato_service.get_doacoes(id)
      return jsonify({"dados": doacoes})