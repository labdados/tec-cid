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