from py2neo.ogm import GraphObject, Property

class Municipio(GraphObject):
    cod_sagres = Property("codigo_sagres")
    municipio_importacao = Property("municipioImportacao")

    def __iter__(self):
        return self.__node__