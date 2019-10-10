from ..model.municipio import Municipio
from app.main import db
from flask import json, jsonify

class MunicipioService:

    def get_municipios(self, pagina, limite, campos):
        skip = limite * (pagina - 1)
        
        args = ''
        if campos:
            args = campos.split(",")
            
        filtros = []
        
        if args:
            # Formatando os campos de filtro estilo cypher
            for i in range(0, len(args)): 
                # Caso seja o último campo é preciso tirar a vírgula
                if i == len(args) - 1:
                    filtros.append("m.{} as {} ".format(args[i], args[i]))
                else:
                    filtros.append("m.{} as {}, ".format(args[i], args[i]))

            res = " ".join(filtros)
            query = "MATCH (m:Municipio) RETURN {} SKIP {} LIMIT {}".format(res, skip, limite)
            result = db.run(query).data()
        else:
            resultado = Municipio.match(db).order_by("_.nome").skip(skip).limit(limite)
            result = [n.__node__ for n in resultado]
        
        return result
    
    def get_gestoes(self, id_municipio, ano):
        query = ''
        if ano:
            print("tem ano")
            query = "MATCH p=(c:Candidato)-[r:GOVERNA]->(m:Municipio) WHERE m.id = '{id}' AND {ano} >= c.ano_eleicao + 1 AND {ano} <= c.ano_eleicao + 4 RETURN c.cpf AS id_candidato, c.ano_eleicao AS ano_inicio_mandato, c.ano_eleicao + 4 AS ano_fim_mandato".format(id = id_municipio, ano = ano)
        else:
            print("sem ano")
            query = "MATCH p=(c:Candidato)-[r:GOVERNA]->(m:Municipio) where m.id = '{}' RETURN c.cpf AS id_candidato, c.ano_eleicao + 1 AS ano_inicio_mandato, c.ano_eleicao + 4 AS ano_fim_mandato ORDER BY ano_inicio_mandato DESC LIMIT 1".format(id_municipio)
        
        return db.run(query).data()