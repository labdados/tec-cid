from ..service.licitacao_service import Licitacao_Service
from flask_restplus import Namespace, Resource
from flask import Flask, json, request, jsonify

api = Namespace('Licitação', description='Operações relacionadas a licitações')

lic_service = Licitacao_Service()

def gerando_response(results, x_total_count):
   print(results)
   response = Flask.response_class(response=results, headers={
         "X-Total-Count": x_total_count
      }, mimetype="application/json")
   
   return response


@api.route("")
@api.doc(params={"ano": "Ano das licitações"})
@api.doc(params={"codUni": "Código da unidade gestora"})
@api.doc(params={"tipoLic": "Código do tipo da licitação"})
@api.doc(params={'pagina': 'Página que será acessada'})
@api.doc(params={'limite': 'Quantos resultados serão retornados'})
class Licitacao(Resource):
   def get(self):
      ''' 
      Retorna as licitações baseadas nos filtros que foram passados
      '''
      ano = request.args.get("ano", '', str)
      codUni = request.args.get("codUni", '', str)
      tipoLic = request.args.get("tipoLic", '', str)
      pagina = request.args.get("pagina", 1, int)
      limite = request.args.get("limite", 20, int)
      #print(dao.count_lic)
     
      licitacoes =  json.dumps(lic_service.get_licitacoes(ano, tipoLic, codUni, pagina, limite))
      total = lic_service.count_lic

      response = gerando_response(licitacoes, total)

      return response

@api.route("/licitacoes/<string:id>/propostas")
@api.doc(params={'id': 'id da licitação'})
@api.doc(params={'pagina': 'Página que será acessada'})
@api.doc(params={'limite': 'Quantos resultados serão retornados'})
class Propostas(Resource):
   def get(self, id):
      '''
      Retorna as propostas que um participante fez em uma determinada licitação
      '''

      data = id.split("-")
      codUnidadeGestora = data[0]
      codLicitacao = data[1]
      codTipoLicitacao = data[2]

      pagina = request.args.get("pagina", 1, int)
      limite = request.args.get("limite", 20, int)

      results = json.dumps(lic_service.procurando_propostas(codUnidadeGestora, codLicitacao, codTipoLicitacao, pagina, limite))

      response = gerando_response(results, lic_service.count_props)

      return response


@api.route("/licitacoes/<string:id>")
@api.doc(params={'id': 'id da licitação'})
class LicitacaoEspecifica(Resource):
   def get(self, id):
      '''
      Retorna uma licitação específica
      '''
      data = id.split("-")
      codUnidadeGestora = data[0]
      codLicitacao = data[1]
      codTipoLicitacao = data[2]

      return jsonify(lic_service.get_licitacao_especifica(codUnidadeGestora, codTipoLicitacao, codLicitacao))