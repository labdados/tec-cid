from ..model.models import Municipio
from app.main import db
from flask import json, jsonify

IMAGE_ATTRIBUTES = ["bandeira", "brasao"]

class MunicipioService:

    def get_municipios(self, pagina, limite, atributos):
        skip = limite * (pagina - 1)
        atr_l = atributos.lower().replace(' ', '').split(',') if atributos else ''
        
        result = Municipio.match(db).order_by('_.nome').skip(skip).limit(limite)
        nodes = []
        for obj in result:
            node = obj.__node__
            # remove image attributes
            for k in IMAGE_ATTRIBUTES:
                node.pop(k, None)
            # filter selected fields
            node = {k: node[k] for k in atr_l if k in node} if atr_l else node
            if node:
                nodes.append(node)

        result = Municipio.match(db).order_by("_.nome").skip(skip).limit(limite)
        nodes = [n.__node__ for n in result]
        return nodes
    
    def get_municipio(self, id):
        result = Municipio.match(db).where(id = id)
        nodes = [n.__node__ for n in result]
        return nodes
