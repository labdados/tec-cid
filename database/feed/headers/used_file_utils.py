from headers.used_file import UsedFile

from headers.file_utils import FileUtils
from headers.json_utils import JsonUtils

from headers.exceptions.invalid_used_file_exception import InvalidUsedFileException
from headers.exceptions.invalid_attribute_exception import InvalidAttributeException


class UsedFileUtils:
    """
    Classe utilitária para a classe  @see `UsedFile`
    """
    FILES_WITH_ATTRIBUTES_JSON = '/data/files_with_attributes.json'

    @staticmethod
    def initialize_used_files() -> dict:
        files_with_attributes = {"files": []}
        used_files = JsonUtils.get_used_files()

        for key, files in used_files.items():
            for file in files:
                used_file = UsedFile(file_name=file, header=[], used_attributes=[])
                files_with_attributes.get('files').append(used_file.__dict__)

        return files_with_attributes

    @staticmethod
    def create_files_with_attributes_json() -> None:
        try:
            final_path = FileUtils.get_full_path(UsedFileUtils.FILES_WITH_ATTRIBUTES_JSON)
            FileUtils.file_exists(final_path)
        
        except FileNotFoundError:
            files_with_attributes = UsedFileUtils.initialize_used_files()
            json_file = JsonUtils.dict_to_json(files_with_attributes)
            JsonUtils.save_json(json_file, UsedFileUtils.FILES_WITH_ATTRIBUTES_JSON)

    @staticmethod
    def validate_attribute(used_file, attribute_name:str):
        try:
            getattr(used_file, attribute_name)
        except AttributeError:
            raise InvalidAttributeException(f'O atributo "{attribute_name}" não pertence a classe UsedFile!')

    @staticmethod
    def get_used_files_list_from_key_name(key_name:str) -> list:
        """
        Método que retorna uma lista de arquivos que são usados nos arquivos *.cypher a partir de uma chave.
        Valores possíveis: "tce", "tse", "receita_federal", "sancoes"
        """
        all_used_files = JsonUtils.get_used_files()
        result = JsonUtils.get_dict_by_key_from_dict_list(key_name, all_used_files)

        if result:
            return result

        else:
            raise Exception(f'[ERROR] The key must be "tce", "tse", "receita_federal" or "sancoes"')

    @staticmethod
    def update_used_file(csv_name: str, attribute_name:str, new_attribute_value: list) -> None:
        """
        Método para atualizar o header ou os atributos utilizados no objeto do tipo `UsedFile` 
        no arquivo `files_with_attributes.json`
        """
        JsonUtils.assert_is_array(new_attribute_value)

        files_with_attributes = JsonUtils.get_dict_from_json_file(UsedFileUtils.FILES_WITH_ATTRIBUTES_JSON)
        used_files = files_with_attributes.get('files')

        for index, file in enumerate(used_files):
            used_file = UsedFile(file.get('file_name'), file.get('header'), file.get('used_attributes'))
            UsedFileUtils.validate_attribute(used_file, attribute_name)

            if (used_file.file_name == csv_name):
                setattr(used_file, attribute_name, new_attribute_value)
                used_files[index] = used_file.__dict__

                files_with_attributes['files'] = used_files
                files_with_attributes = JsonUtils.dict_to_json(files_with_attributes)

                JsonUtils.save_json(files_with_attributes, UsedFileUtils.FILES_WITH_ATTRIBUTES_JSON)
                return

        raise InvalidUsedFileException(csv_name)

    @staticmethod
    def get_used_file_from_files_with_attributes(file_name:str) -> dict:
        files_with_attributes = JsonUtils.get_dict_from_json_file(UsedFileUtils.FILES_WITH_ATTRIBUTES_JSON)
        files_with_attributes = files_with_attributes.get('files')
        
        for file in files_with_attributes:
            if (file.get('file_name') == file_name): return file

        raise Exception(f'O CSV "{file_name}" não está apto para ser analisado!')