#from participante_service import Participante_Service as participante_service
from ..service.participante_service import Participante_Service
from flask_restplus import Resource, Namespace
from flask import Flask, json, request

participante_service = Participante_Service()

api = Namespace('Participante', description='Operações relacionadas aos participantes')

def gerando_response(results, x_total_count):
   #print(results)
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

      participantes =  json.dumps(participante_service.get_participantes(pagina, limite))
      total = dao.count_part

      response = gerando_response(participantes, total)

      return response



@api.route("/participantes/<string:id>")
@api.doc(params={'id': 'CPF/CNPJ do participante'})
class ParticipanteEspecifico(Resource):
   def get(self, id):
      '''
      Retorna um participante específico
      '''
      return jsonify(participante_service.get_participante_por_codigo(id))