class InvalidHeaderException(Exception):

    def __init__(self, file_name):
        self.file_name = file_name

        super().__init__(f"[EXCEPTION]: O arquivo '{self.file_name}' não possui header e está vazio!")