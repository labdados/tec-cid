import os
import csv

import headers.cypher_utils

from headers.file_utils import FileUtils
from headers.used_file_utils import UsedFileUtils

class HeaderUtils:

    PREFIX = '/../../../dados'

    @staticmethod
    def get_header(file_name:str) -> list:
        if (FileUtils.file_exists(file_name)):
            with open(file_name, 'r') as csv_file:
                reader = csv.reader(csv_file)
                header = next(reader)
                delimiter = FileUtils.detect_csv_delimiter(str(header))

            with open(file_name, 'r') as csv_file:
                reader = csv.reader(csv_file, delimiter=delimiter)
                return next(reader)
        else:
            return None

    @staticmethod
    def fill_header_and_used_attributes(key_name:str) -> None:
        """
        Método que preenche o header e quais atributos dos *.csv são utilizados,
        a partir de umas das chaves presentes no arquivo `used_files.json`
        """
        UsedFileUtils.create_files_with_attributes_json()
        file_names = UsedFileUtils.get_used_files_list_from_key_name(key_name)
        csv_with_used_attributes = headers.cypher_utils.CypherUtils.get_used_attributes_from_cypher_files(key_name)

        if file_names:
            for file_name in file_names:
                prefix = FileUtils.get_full_path(HeaderUtils.PREFIX)
                prefix += '/'
                header = HeaderUtils.get_header(prefix + file_name)

                used_attributes = [aux.get('used_attributes') for aux in csv_with_used_attributes if aux.get('csv_name') == file_name]
                used_attributes = used_attributes[0]

                UsedFileUtils.update_used_file(file_name, 'header', header)
                UsedFileUtils.update_used_file(file_name, 'used_attributes', used_attributes)