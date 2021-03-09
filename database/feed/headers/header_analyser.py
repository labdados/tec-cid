from headers.used_file import UsedFile

from headers.used_file_utils import UsedFileUtils
from headers.file_utils import FileUtils
from headers.json_utils import JsonUtils
from headers.header_utils import HeaderUtils
from headers.cypher_utils import CypherUtils

from headers.exceptions.missing_attributes_exception import MissingAttributesException

class HeaderAnalyser:
   
    PREFIX = '/../../../dados'

    @staticmethod
    def get_formatted_message(list_of_missed_attributes_from_cypher_file:list):
        message = ""

        if (list_of_missed_attributes_from_cypher_file != []):
            for values in list_of_missed_attributes_from_cypher_file:
                for result in values:
                    cypher_array = result.cypher_array
                    message += f'CSV utilizado: {result.csv_name}\n'

                    for cypher in cypher_array:
                        used_attributes = cypher.used_attributes
                        message += f'Arquivo Cypher: {cypher.file_name}\n'

                        for attribute in used_attributes:
                            message += f'Atributo: {attribute.attribute_name}, linha(s): {attribute.line_numbers}\n'

                        message += ('-' * 100)
                        message += '\n'

                    message += '\n'

        return message

    @staticmethod
    def analyze(key_name:str, file_names=None) -> None:
        """
        Método que analisa se existe algum atributo que foi removido ou atualizado
        e retorna uma exceção com o nome do atributo, em qual arquivo cypher ele se encontra
        e em quais linhas 
        """
        results = []

        if (not file_names):
            file_names = UsedFileUtils.get_used_files_list_from_key_name(key_name)

        used_files_with_attributes = JsonUtils.get_dict_from_json_file(UsedFileUtils.FILES_WITH_ATTRIBUTES_JSON)
        used_files_with_attributes = used_files_with_attributes['files']

        for file_name in file_names:
            file = JsonUtils.get_dict_by_key_value_from_dict_array(
                dict_key='file_name', 
                value=file_name, 
                dict_list=used_files_with_attributes
            )

            header = {value for value in file['header']}
            used_attributes = {value for value in file['used_attributes']}

            if (used_attributes.issubset(header)):
                print(f'[INFO]: Todos os atributos que são utilizados do arquivo {file_name} estão presentes no seu header!')

            else:
                missing_attributes = used_attributes - header
                missing_attributes_array = [value for value in missing_attributes]

                result = CypherUtils.get_missed_attributes_from_cypher_file([file_name], missing_attributes_array)
                results.append(result)

        if (results != []):
            message = HeaderAnalyser.get_formatted_message(results)
            raise MissingAttributesException(message)