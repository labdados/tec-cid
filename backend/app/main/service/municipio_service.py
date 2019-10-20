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
        
        return nodes
    
    def get_gestoes(self, id_municipio, ano):
        query = "MATCH p=(c:Candidato)-[r:GOVERNA]->(m:Municipio) \
            WHERE m.id = '{id}' AND {ano} >= c.ano_eleicao + 1 AND \
            {ano} <= c.ano_eleicao + 4 \
            RETURN c.id AS id_candidato, \
            c.ano_eleicao + 1 AS ano_inicio_mandato, \
            c.ano_eleicao + 4 AS ano_fim_mandato".format(id = id_municipio, ano = ano)
        result = db.run(query).data()
        
        return result

    def get_municipio(self, id):
        result = Municipio.match(db).where(id = id)
        nodes = [n.__node__ for n in result]
        return nodes

