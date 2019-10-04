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
    
    def get_gestoes(self, id_municipio, ano_inicio_mandato):
        query_ano_inicio, query_ano_fim, query_id_mun = ''
        
        if ano_inicio_mandato:
            query_ano_inicio = "WHERE c.ano_eleicao > {}".format(ano_inicio_mandato)
        if ano_fim_mandato:
            query_ano_fim = "AND c.ano_eleicao + 4 <= {}".format(ano_fim_mandato)
       if id_municipio:
            query_id_mun = "AND m.id = '{}'".format(id_municipio)
        
        query = "MATCH p=(c:Candidato)-[r:GOVERNA]->(m:Municipio) WHERE m.id = {} AND c.ano_eleicao > {} AND c.ano_eleicao + 4 <= {} RETURN m.id AS id_municipio, c.cpf AS cpf_candidato, c.ano_eleicao AS ano_inicio_mandato, c.ano_eleicao + 4 AS ano_fim_mandato"