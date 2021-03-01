class UsedFile:
    """
    Classe para representar um nome de arquivo CSV, qual é seu antigo e novo header e quais
    atributos deles são utilizados para carregar no banco de dados
    """

    def __init__(self, file_name:str, header:list, used_attributes:list):
        self.file_name = file_name
        self.header = header
        self.used_attributes = used_attributes

    @staticmethod
    def is_valid_attribute(self, attribute:str):
        return hasattr(self, attribute)