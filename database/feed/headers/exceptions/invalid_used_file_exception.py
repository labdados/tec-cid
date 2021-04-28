class InvalidUsedFileException(Exception):

    def __init__(self, file_name):
        self.file_name = file_name

        super().__init__(f"[EXCEPTION]: O arquivo '{self.file_name}' não pode ser utilizado para ser analisado!")