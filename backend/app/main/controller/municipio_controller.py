from ..service.municipio_service import MunicipioService
from flask_restplus import Resource, Namespace
from flask import request, jsonify

municipios = MunicipioService()

api = Namespace('Munícipio', 'Operações relacionadas aos municípios')

@api.route("")
@api.doc(params={
   "pagina": "Página que será acessada",
   "limite": "Quantos resultados serão retornados",
   "atributos": "Atributos do município que serão retornados, separados por\
      virgula. Se não for informado, todos serão retornados.\
      Valores válidos: `id, nome, mesoregiao, microregiao,\
      codigo_ibge, codigo_siaf, link_ibge, link_wikipedia, esfera`"
})
class MunicipioList(Resource):
   def get(self):
      '''
      Retorna os municipios
      '''
      pagina = request.args.get("pagina", 1, int)
      limite = request.args.get("limite", 20, int)
      atributos = request.args.get("atributos", '', str)
      result = municipios.get_municipios(pagina, limite, atributos)
      return jsonify({"dados": result})
