import json
import headers.file_utils

class JsonUtils:
    """
    Classe com funções úteis para manipulação e utilização de JSON para a detecção da alteração de headers nos arquivos
    """
    __USED_FILES_PATH = '/data/used_files.json'

    @staticmethod
    def get_used_files():
        return JsonUtils.get_dict_from_json_file(JsonUtils.__USED_FILES_PATH)

    @staticmethod
    def get_dict_from_json_object(json_object:object) -> dict:
        return json.loads(json_object)

    @staticmethod
    def get_dict_from_json_file(json_file_path:str, full_path=True) -> dict:
        if (full_path):
            final_path = headers.file_utils.FileUtils.get_full_path(json_file_path)
        else:
            final_path = json_file_path
            
        with open(final_path, 'r') as json_file:
            data = json.load(json_file)
            return data

    @staticmethod
    def dict_to_json(dict_name:dict) -> json:
        try:
            return json.dumps(dict_name, ensure_ascii=False, indent=4)

        except Exception as e:
            raise Exception(f"Erro ao converter o dicionário {dict_name.__dict__} em um JSON: {e.__cause__}")

    @staticmethod
    def save_json(json_object:dict, json_name:str) -> None:
        final_path = headers.file_utils.FileUtils.get_full_path(json_name)
        try:
            with open(final_path, 'w', encoding='utf-8') as json_file:
                json_file.write(json_object)
        
        except Exception as e:
            raise Exception(f"Erro ao salvar o JSON {json_name} a partir do objeto {json_object.__dict__}: {e.__cause__}")

    @staticmethod
    def get_dict_by_key_from_dict_list(dict_key:str, dict_list:dict) -> list:
        """
        Método que procura a partir de uma chave em uma lista de dicionários e retorna uma lista
        de elementos daquela chave.
        Exemplo: dict_list = {'key1': [1,2,3], 'key2': [0,1,2]}
            get_dict_by_key_from_dict_list('key1', dict_list) returns [1,2,3]
            get_dict_by_key_from_dict_list('key2', dict_list) returns [0,1,2]
            get_dict_by_key_from_dict_list('key3', dict_list) returns None
        """
        return dict_list.get(dict_key)

    @staticmethod
    def get_dict_by_key_value_from_dict_array(dict_key:str, value:str, dict_list:list) -> dict:
        """
        Método que procura um dicionário a partir de uma chave:valor em um array de dicionários,
        e retorna apenas a primeira ocorrência.
        Exemplo: dict_array = [{'name': 'dict_a'}, {'name': 'dict_b'}, {'name': 'dict_a'}]
            get_dict_by_key_value_from_dict_array('name', 'dict_a', dict_array) returns  {'name': 'dict_a'}
            get_dict_by_key_value_from_dict_array('name', 'dict_b', dict_array) returns {'name': 'dict_b'}
            get_dict_by_key_value_from_dict_array('name', 'dict_ab', dict_array) returns None
        """
        return next((dictionary for dictionary in dict_list if dictionary[dict_key] == value), None)

    @staticmethod
    def dict_already_exists(dict_key:str, value:str, dict_list:list) -> bool:
        """
        Método que retorna se um dicionário já existe na lista de dicionários de arquivos
        """
        exists = JsonUtils.get_dict_by_key_value_from_dict_array(dict_key, value, dict_list)
        return True if exists else False

    @staticmethod
    def assert_is_array(array:list):
        if not (type(array) == list):
            raise TypeError(f"A variável do tipo {type(array)} deve ser uma lista!")