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
      return jsonify({"dados":result})

@api.route("/<string:idMunicipio>/gestoes")
@api.doc(params={
   "idMunicipio": "Id do município",
   "ano": "Ano do início do mandato"
})
class Gestoes(Resource):
   def get(self, idMunicipio):
      ano = request.args.get("ano", None, int)
      result = municipios.get_gestoes(idMunicipio, ano)
      return jsonify({"dados": result})
      

@api.route("/<string:id>")
@api.doc(params={'id': 'ID do municipio'})
class Municipio(Resource):
   def get(self, id):
      '''
      Retorna um municipio específico
      '''
      municipio = municipios.get_municipio(id)
      return jsonify({"dados": municipio})

