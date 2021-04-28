class InvalidAttributeException(Exception):

    def __init__(self, message):
        self.message = message

        super().__init__(f"[EXCEPTION]: {self.message}")