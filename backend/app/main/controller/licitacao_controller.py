from ..service.licitacao_service import LicitacaoService
from flask_restplus import Namespace, Resource
from flask import Flask, json, request, jsonify

api = Namespace('Licitação', description='Operações relacionadas a licitações')

lic_service = LicitacaoService()

def gerando_response(results, x_total_count):
   response = Flask.response_class(response=results, headers={
         "X-Total-Count": x_total_count
      }, mimetype="application/json")
   
   return response

@api.route("")
@api.doc(params={
   "codUni": "Código da unidade gestora",
   "tipoLic": "Código do tipo da licitação",
   "dataInicio": "Data de início de um intervalo de tempo, no formato `AAAA-MM-DD`.",
   "dataFim": "Data de término de um intervalo de tempo, no formato `AAAA-MM-DD`.",
   "limite": "Quantos resultados serão retornados",
   "pagina": "Página que será acessada",
   "ordenarPor": "Nome do campo pelo qual a lista deve ser ordenada.",
   "ordem": "O sentido da ordenação: `ASC` para A a Z ou 0 a 9, e `DESC` para Z a A ou 9 a 0.",
   "nomeMunicipio": "Nome do município a quem pertence as licitações"
})
class LicitacaoList(Resource):
   def get(self):
      ''' 
      Retorna as licitações baseadas nos filtros que foram passados
      '''
      data_inicio = request.args.get("dataInicio", '', str)
      data_fim = request.args.get("dataFim", '', str)
      cod_uni = request.args.get("codUni", '', str)
      tipo_lic = request.args.get("tipoLic", '', str)
      pagina = request.args.get("pagina", 1, int)
      limite = request.args.get("limite", 20, int)
      ordenar_por = request.args.get("ordenarPor", "Data", str)
      ordem = request.args.get("ordem", '', str)
      nome_municipio = request.args.get("nomeMunicipio", '', str)
      licitacoes = lic_service.get_licitacoes(cod_uni, tipo_lic, data_inicio, data_fim,
                                      pagina, limite, ordenar_por, ordem, nome_municipio)
      
      licitacoes =  json.dumps({"dados": licitacoes})
      total = lic_service.count_lic

      response = gerando_response(licitacoes, total)

      return response

@api.route("/<string:id>")
@api.doc(params={'id': 'id da licitação'})
class Licitacao(Resource):
   def get(self, id):
      '''
      Retorna uma licitação específica
      '''
      data = id.split("-")
      codUnidadeGestora = data[0]
      codTipoLicitacao = data[1]
      codLicitacao = data[2]
      licitacao = lic_service.get_licitacao(codUnidadeGestora, codTipoLicitacao, codLicitacao)
      licitacao = json.dumps({"dados": licitacao})
      response = gerando_response(licitacao, 1)
      return response

@api.route("/<string:id>/propostas")
@api.doc(params={'id': 'id da licitação'})
@api.doc(params={'pagina': 'Página que será acessada'})
@api.doc(params={'limite': 'Quantos resultados serão retornados'})
class PropostaList(Resource):
   def get(self, id):
      '''
      Retorna as propostas que um participante fez em uma determinada licitação
      '''

      data = id.split("-")
      codUnidadeGestora = data[0]
      codTipoLicitacao = data[1]
      codLicitacao = data[2]

      pagina = request.args.get("pagina", 1, int)
      limite = request.args.get("limite", 20, int)

      propostas = lic_service.get_propostas(codUnidadeGestora, codTipoLicitacao, codLicitacao, pagina, limite)
      results = json.dumps({"dados": propostas})

      response = gerando_response(results, lic_service.count_props)

      return response