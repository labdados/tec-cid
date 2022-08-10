class MissingAttributesException(Exception):

    def __init__(self, formatted_message:str):
        self.message = f"Os seguintes atributos que são utilizados foram removidos ou alterados:\n\n"
        super().__init__(self.message + formatted_message)