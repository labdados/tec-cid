import os
import headers.json_utils

from csv import Sniffer

class FileUtils:

    @staticmethod
    def __is_file(file_name:str) -> bool: 
        return os.path.isfile(file_name)

    @staticmethod
    def file_exists(file_name:str) -> bool:
        if (os.path.exists(file_name) and FileUtils.__is_file(file_name)):
            return True
        os.path.exists(file_name)
        raise FileNotFoundError(f'The file {file_name} not exists!')

    @staticmethod
    def get_all_files_from_path(path_name:str) -> list:
        all_files = os.listdir(path_name)
        only_files = []

        for file in all_files:
            if (os.path.isfile(path_name + file)):
                only_files.append(file)

        return only_files

    @staticmethod
    def read_file(file_name: str) -> list:
        file_array = []
        
        if (FileUtils.file_exists(file_name)):
            with open(file_name, 'r') as file:
                for line in file:
                    final_line = line.replace('\n', '').replace('\t', '').strip()
                    file_array.append(final_line)

        return file_array

    @staticmethod
    def get_used_files_list_from_key_name(key_name:str) -> list:
        """
        Método que retorna uma lista de arquivos que são usados nos arquivos *.cypher a partir de uma chave.
        Valores possíveis: "tce", "tse", "receita_federal", "sancoes"
        """
        all_used_files = headers.json_utils.JsonUtils.get_used_files()
        result = headers.json_utils.JsonUtils.get_dict_by_key_from_dict_list(key_name, all_used_files)

        if result:
            return result

        else:
            raise Exception(f'[ERROR] The key must be "tce", "tse", "receita_federal" or "sancoes"')

    @staticmethod
    def get_full_path(file_path:str) -> str:
        absolute_path = os.path.dirname(os.path.abspath(__file__))
        return absolute_path + file_path

    @staticmethod
    def detect_csv_delimiter(str_array:str) -> str:
        sniffer = Sniffer()
        dialect = sniffer.sniff(str_array)

        return dialect.delimiter