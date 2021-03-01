class CypherFile:
    """
    Classe para representar o nome do arquivo cypher e uma lista de atributos do tipo
    `used_attribute.UsedAttribute` que são utilizados e as linhas onde ocorrem no arquivo cypher
    """
    def __init__(self, file_name:str, used_attributes:list):
        self.file_name = file_name
        self.used_attributes = used_attributes