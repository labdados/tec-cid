import json

class ZippedFilesUtils:
    """
    Classe para obter nome do diretório que foi compactado, o nome do arquivo que será lido
    do diretório compactado, o nome do arquivo após a extração e o ano do arquivo
    """
    ZIPPED_FILES = '../../dados/zipped_files.json'
    
    @staticmethod
    def get_zipped_files() -> list:
        with open(ZippedFilesUtils.ZIPPED_FILES, 'r') as json_file:
            data = json.load(json_file)
            return data

    @staticmethod
    def get_zipped_files_from_key(key_name:str) -> dict:
        zipped_files = ZippedFilesUtils.get_zipped_files()
        result = zipped_files.get(key_name)

        if result:
            return result

        raise Exception(f'[ERROR] The key must be "candidatos", "receita_candidatos" or "sancoes"')

    @staticmethod
    def get_zipped_files_from_year(key_name:str, year:int) -> dict:
        zipped_files = ZippedFilesUtils.get_zipped_files_from_key(key_name)
        result = next((dictionary for dictionary in zipped_files if dictionary['year'] == year), None)

        if result:
            return result

        raise Exception(f'[ERROR] The year {year} is not valid!')