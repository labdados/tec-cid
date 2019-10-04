from ..service.estatistica_service import EstatisticaService
from flask_restplus import Namespace, Resource
from flask import Flask, json, request, jsonify

api = Namespace('Licitação', description='Operações relacionadas a licitações')

estat_service = EstatisticaService()

@api.route("licitacoes")
@api.doc(params={
   "codUni": "Código da unidade gestora",
   "tipoLic": "Código do tipo da licitação",
   "dataInicio": "Data de início de um intervalo de tempo, no formato `AAAA-MM-DD`.",
   "dataFim": "Data de término de um intervalo de tempo, no formato `AAAA-MM-DD`.",
   "limite": "Quantos resultados serão retornados",
   "pagina": "Página que será acessada",
   "ordenarPor": "Nome do campo pelo qual a lista deve ser ordenada.",
   "ordem": "O sentido da ordenação: `ASC` para A a Z ou 0 a 9, e `DESC` para Z a A ou 9 a 0."
})
class EstatisticaLicitacoes(Resource):
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
      agrupar_por = request.args.get("agruparPor", '', str)
      ordenar_por = request.args.get("ordenarPor", 'Data', str)
      ordem = request.args.get("ordem", '', str)
      res = estat_service.get_estatistica_licitacoes(cod_uni, tipo_lic, data_inicio, data_fim,
                                                     pagina, limite, agrupar_por, ordenar_por, ordem)
      return json.dumps({"dados": res})

