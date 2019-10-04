from ..service.municipio_service import MunicipioService
from flask_restplus import Resource, Namespace
from flask import request, jsonify

municipios = MunicipioService()

api = Namespace('Munícipio', 'Operações relacionadas aos municípios')

@api.route("")
@api.doc(params={"pagina": "Página que será acessada",
                 "limite": "Quantos resultados serão retornados",
                 "campos": "Dados do município que serão retornados, separados por virgula"})
class MunicipioList(Resource):
   def get(self):
      '''
      Retorna os municipios
      '''
      pagina = request.args.get("pagina", 1, int)
      limite = request.args.get("limite", 20, int)
      campos = request.args.get("campos", '', str)
      result = municipios.get_municipios(pagina, limite, campos)
      return jsonify({"dados":result})

@api.route("/<string:id>/gestoes")
@api.doc(params={
   "idMunicipio": "Id do município",
   "anoInicioMandato": "Ano do início do mandato",
   "anoFimMandato": "Ano do fim do mandato"
})
class Gestoes(Resource):
       def get(self):
              


@api.route("/<string:id>/gestoes/<string:ano>")
@api.doc(params={
   "id": "Id do munícipio",
   "ano": "Ano do mandato"
})