from .main.controller.licitacao_controller import api as licitacao_namespace
from .main.controller.participante_controller import api as participante_namespace
from .main.controller.unidade_gestora_controller import api as unidades_namespace
from .main.controller.candidato_controller import api as candidatos_namespace
from .main.controller.partido_controller import api as partidos_namespace
from .main.controller.municipio_controller import api as municipios_namespace
from .main.controller.estatistica_controller import api as estatistica_namespace

from flask import Flask, Blueprint, url_for
from flask_restx import Api, Resource, apidoc

api_url_prefix = "/tec-cid/api"

class MyCustomApi(Api):

    def _register_apidoc(self, app: Flask) -> None:
        conf = app.extensions.setdefault('restplus', {})
        custom_apidoc = apidoc.Apidoc('restplus_doc', 'flask_restx.apidoc',
        template_folder='templates', static_folder='static',
        static_url_path=api_url_prefix)

        @custom_apidoc.add_app_template_global
        def swagger_static(filename: str) -> str:
            return url_for('restplus_doc.static', filename=filename)

        if not conf.get('apidoc_registered', False):
            app.register_blueprint(custom_apidoc)
        conf['apidoc_registered'] = True

blueprint = Blueprint('api', __name__, url_prefix=api_url_prefix)
api = MyCustomApi(blueprint, doc='/docs')

api.add_namespace(licitacao_namespace, path="/licitacoes")
api.add_namespace(participante_namespace, path="/participantes")
api.add_namespace(unidades_namespace, path="/unidades-gestoras")
api.add_namespace(candidatos_namespace, path="/candidatos")
api.add_namespace(partidos_namespace, path="/partidos")
api.add_namespace(municipios_namespace, path="/municipios")
api.add_namespace(estatistica_namespace, path="/estatisticas")
