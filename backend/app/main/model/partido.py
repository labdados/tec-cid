from py2neo.ogm import GraphObject, Property

class Partido(GraphObject):
    num_partido = Property("NumeroPartido")
    siglaPartido = Property("SiglaPartido")

    def __iter__(self):
        return self.__node__