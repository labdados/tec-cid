import json

class DownloadUtils:
    """
    Classe utilitária para obter a URL e OUTPUT_FILE
    dos arquivos de download que serão usados na ETL
    """
    __DOWNLOAD_FILE_NAMES = '../../dados/download_file_names.json'

    @staticmethod
    def get_all_download_file_names() -> list:
        with open(DownloadUtils.__DOWNLOAD_FILE_NAMES) as json_file:
            return json.load(json_file)

    @staticmethod
    def get_download_file_names_from_key(key_name:str) -> dict:
        file_names = DownloadUtils.get_all_download_file_names()
        result = file_names.get(key_name)

        if result:
            return result

        raise Exception(f'The key must be "tce", "tse", "receita_federal" or "sancoes"')