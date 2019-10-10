from ..service.estatistica_service import EstatisticaService
from flask_restplus import Namespace, Resource
from flask import Flask, json, request, jsonify

api = Namespace('Estatística', description='Estatísticas agregadas de licitações.')

estatistica_svc = EstatisticaService()

@api.route("/licitacoes")
@api.doc(params={
   "idMunicipio": "Identificador do município",
   "dataInicio": "Data de início de um intervalo de tempo, no formato `AAAA-MM-DD`.",
   "dataFim": "Data de término de um intervalo de tempo, no formato `AAAA-MM-DD`.",
   "pagina": "Página que será acessada",
   "limite": "Quantos resultados serão retornados",
   "agruparPor": "Nome dos campos para os quais as estatísticas serão agrupadas. \
                  Valores válidos (separados por vírgula): `municipio`, `participante`",
   "ordenarPor": "Nome do campo pelo qual a lista deve ser ordenada. \
                  Valores válidos: `valor_total_propostas` (default), `n_licitacoes`,\
                                    `nome_participante`, `nome_municipio`",
   "ordem": "O sentido da ordenação: `ASC` para A a Z ou 0 a 9, e `DESC` para Z a A ou 9 a 0."
})
class EstatisticaLicitacoes(Resource):
   def get(self):
      ''' 
      Retorna as licitações baseadas nos filtros que foram passados
      '''
      data_inicio = request.args.get("dataInicio", '', str)
      data_fim = request.args.get("dataFim", '', str)
      id_municipio = request.args.get("idMunicipio", '', str)
      pagina = request.args.get("pagina", 1, int)
      limite = request.args.get("limite", 20, int)
      agrupar_por = request.args.get("agruparPor", '', str)
      ordenar_por = request.args.get("ordenarPor", '', str)
      ordem = request.args.get("ordem", '', str)
      res = estatistica_svc.get_estatistica_licitacoes(id_municipio, data_inicio, data_fim, pagina,
                                                       limite, agrupar_por, ordenar_por, ordem)
      return jsonify({"dados": res})

