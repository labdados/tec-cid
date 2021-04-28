class UsedAttribute:
    """
    Classe para representar um atributo que está sendo utilizado
    com quais linhas ele é utilizado
    
    @see `cypher_file.CypherFile`
    """

    def __init__(self, attribute_name:str, line_numbers=list):
        self.attribute_name = attribute_name
        self.line_numbers = line_numbers