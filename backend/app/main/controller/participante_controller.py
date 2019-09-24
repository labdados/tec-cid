from ..service.participante_service import ParticipanteService
from flask_restplus import Resource, Namespace
from flask import Flask, json, request, jsonify

participante_service = ParticipanteService()

api = Namespace('Participante', description='Operações relacionadas aos participantes')

def gerando_response(results, x_total_count):
   response = Flask.response_class(response=results, headers={
         "X-Total-Count": x_total_count
      }, mimetype="application/json")
   
   return response

@api.route("")
@api.doc(params={'pagina': 'Página que será acessada'})
@api.doc(params={'limite': 'Quantos resultados serão retornados'})
class Participante(Resource):
   def get(self):
      ''' 
      Retorna os participantes
      '''

      codParticipante = request.args.get("codPart", '', str)
      pagina = request.args.get("pagina", 1, int)
      limite = request.args.get("limite", 20, int)

      participantes = participante_service.get_participantes(pagina, limite)
      results = json.dumps({"dados": participantes})
      total = participante_service.count_part

      response = gerando_response(results, total)

      return response

@api.route("/<string:id>")
@api.doc(params={'id': 'CPF/CNPJ do participante'})
class ParticipanteEspecifico(Resource):
   def get(self, id):
      '''
      Retorna um participante específico
      '''
      participante = participante_service.get_participante_por_codigo(id)
      return jsonify({"dados": participante})