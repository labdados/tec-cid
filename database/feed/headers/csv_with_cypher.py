class CsvWithCypher:
    """
    Classe para representar o nome do CSV junto com um array de arquivos *.cypher do tipo
    `cypher_file.CypherFile.

    {
        "csv_name": "empenhos.csv",
        "cypher_array": [
            {
                "file_name": "rel_gerou_teste.cypher",
                "used_attributes": [
                    {
                        "used_attribute": "cd_teste",
                        "line_numbers": [
                            5
                        ]
                    }
            },
            {
                ...
            }
        }
    }
    """
    def __init__(self, csv_name:str, cypher_array:list):
        self.csv_name = csv_name
        self.cypher_array = cypher_array