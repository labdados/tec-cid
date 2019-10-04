from ..model.municipio import Municipio
from app.main import db
from flask import json, jsonify

IMAGE_ATTRIBUTES = ['bandeira', 'brasao']

class MunicipioService:

    def get_municipios(self, pagina, limite, campos):
        skip = limite * (pagina - 1)
        
        fields = campos.split(",") if campos else ''
        
        result = Municipio.match(db).order_by("_.nome").skip(skip).limit(limite)
        nodes = []
        for obj in result:
            node = obj.__node__
            # remove image attributes
            for k in IMAGE_ATTRIBUTES:
                node.pop(k, None)
            # filter selected fields
            node = {k: node[k] for k in fields if k in node} if fields else node
            if node:
                nodes.append(node)

        return nodes