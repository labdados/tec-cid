from ..service.candidato_service import CandidatoService
from flask_restplus import Resource, Namespace
from flask import request, jsonify

candidato = CandidatoService()

api = Namespace('Candidato', 'Operações relacionadas aos candidatos de partidos políticos')

@api.route("")
@api.doc(params={'pagina': 'Página que será acessada'})
@api.doc(params={'limite': 'Quantos resultados serão retornados'})
class Candidatos(Resource):
   def get(self):
      '''
      Retorna os candidatos
      '''
      pagina = request.args.get("pagina", 1, int)
      limite = request.args.get("limite", 20, int)
      candidatos = candidato.get_candidatos(pagina, limite)
      return jsonify({"dados": candidatos})