import headers.header_utils

from headers.cypher_file import CypherFile
from headers.used_attribute import UsedAttribute
from headers.csv_with_cypher import CsvWithCypher

from headers.file_utils import FileUtils
from headers.search_utils import SearchUtils

from re import findall

class CypherUtils:

    __SOURCE_PATH_CYPHER = '../../database/feed/cypher/'
    __SOURCE_PATH_CSV = '../../dados/'
    __UNSED_FILES = ['pagamentos.csv', 'socios_doadores_com_nomes_distintos.csv']
    __ATTRIBUTE_INDEX = 7
    __SIZE_ARRAY_LOADS_CSV = 8

    @staticmethod
    def get_source_path():
        return CypherUtils.__SOURCE_PATH_CYPHER

    @staticmethod
    def __get_all_cypher_files(path_name: str) -> list:
        all_files = FileUtils.get_all_files_from_path(path_name)
        cypher_files = []

        for file in all_files:
            if ('.cypher' in file):
                cypher_files.append(file)

        return cypher_files

    @staticmethod
    def __get_cypher_line_if_loads_csv(file_name: str) -> str:
        FileUtils.file_exists(file_name)

        with open(file_name, 'r') as cypher_file:
            for line in cypher_file.readlines():
                if ('file:///' in line):
                    return line.replace('\n', '')

        return None

    @staticmethod
    def get_cypher_file_if_loads_csv(file_name: str) -> list:
        """
        Método que retorna um array com as linhas de um arquivo *.cypher
        caso ele carregue um CSV
        """
        FileUtils.file_exists(file_name)
        file_loads_csv = CypherUtils.__get_cypher_line_if_loads_csv(file_name)

        if (file_loads_csv):
            return FileUtils.read_file(file_name)

        else:
            return None

    @staticmethod
    def __get_cypher_load_attribute(file_name: str) -> str:
        cypher_line = CypherUtils.__get_cypher_line_if_loads_csv(file_name)

        if (cypher_line):
            # Removendo espaços laterais e / ou consecutivos
            cypher_line = ' '.join(cypher_line.split(' '))
            cypher_line = cypher_line.split(' ')

            if len(cypher_line) != CypherUtils.__SIZE_ARRAY_LOADS_CSV:
                raise Exception(f"O tamanho do array da linha que carrega o CSV não tem tamanho {CypherUtils.__SIZE_ARRAY_LOADS_CSV}")

            return cypher_line[CypherUtils.__ATTRIBUTE_INDEX]

        return None

    @staticmethod
    def __get_csv_file_name_from_cypher_file(file_name: str) -> str:
        cypher_line = CypherUtils.__get_cypher_line_if_loads_csv(file_name)

        if (cypher_line):
            # Returns only the file name if contains *csv
            return findall(r'\w*.csv', cypher_line)[0]

        return None

    @staticmethod
    def get_dict_with_csv_and_cypher_file() -> dict:
        """
        Método que retorna um dicionário, onde chave é o nome do arquivo CSV
        e o conteúdo é um array de arquivos *.cypher onde aquele CSV é utilizado.
        Exemplo: {'doacoes_candidatos.csv': ['nodes_doador.cypher', 'rel_doacoes_candidatos.cypher']}
        """
        csv_with_cypher = {}
        cypher_files = CypherUtils.__get_all_cypher_files(CypherUtils.__SOURCE_PATH_CYPHER)

        for cypher_file in cypher_files:
            cypher_file = CypherUtils.__SOURCE_PATH_CYPHER + cypher_file

            cypher_line = CypherUtils.__get_cypher_line_if_loads_csv(cypher_file)
            cypher_attribute = CypherUtils.__get_cypher_load_attribute(cypher_file)
            csv_file = CypherUtils.__get_csv_file_name_from_cypher_file(cypher_file)

            if (cypher_line and cypher_attribute and (csv_file not in CypherUtils.__UNSED_FILES)):
                if (csv_file not in csv_with_cypher):
                    csv_with_cypher[csv_file] = []  # Inicializando o array de arquivos *.cypher

                csv_with_cypher[csv_file].append(cypher_file.replace(CypherUtils.__SOURCE_PATH_CYPHER, ''))

        return csv_with_cypher

    @staticmethod
    def get_csv_file_names_with_header(csv_file_names:list) -> dict:
        """
        Método que retorna um dicionário, onde a chave é o nome do CSV
        e o valor é seu header a partir de uma lista de nomes de CSV
        """
        result = {}

        for file_name in csv_file_names:
            header = headers.header_utils.HeaderUtils.get_header(CypherUtils.__SOURCE_PATH_CSV + file_name)
            result[file_name] = header

        return result

    @staticmethod
    def get_csv_with_cypher_files(csv_files:list) -> dict:
        """
        Método que retorna um JSON que contém o nome do csv, o nome do arquivo cypher onde o CSV
        é utilizado, quais o atributos utilizados e em quais linhas eles ocorrem,
        a partir de uma lista de CSV's
        """
        csv_with_cypher_file = CypherUtils.get_dict_with_csv_and_cypher_file()

        final_json = {"csv_with_cypher": []}
        for csv_key in csv_files:
            cypher_files = csv_with_cypher_file.get(csv_key)
            csv_with_cypher = CsvWithCypher(csv_name=csv_key, cypher_array=[])

            for cypher_file in cypher_files:
                file = FileUtils.read_file(CypherUtils.get_source_path() + cypher_file)
                cypher_object = CypherFile(file_name=cypher_file, used_attributes=[])

                used_attributes = SearchUtils.get_used_attributes_from_cypher_file(file)
                for attribute in used_attributes:
                    line_numbers = [number+1 for number, line in enumerate(file) if ('line.' + attribute) in line]

                    if (line_numbers):
                        attribute = attribute.replace('`', '')
                        used_attribute = UsedAttribute(attribute_name=attribute, line_numbers=line_numbers)
                        cypher_object.used_attributes.append(used_attribute)

                csv_with_cypher.cypher_array.append(cypher_object)

            final_json['csv_with_cypher'].append(csv_with_cypher)

        return final_json

    @staticmethod
    def get_used_attributes_from_cypher_files(csv_key_name:str) -> list:
        """
        Método que retorna uma lista que contém o nome do CSV e quais atributos são utilizados
        nos arquivos *.cypher, a partir de uma das chaves (tce, tse, receita_federal, sancoes)
        que estão no arquivo `used_files.json`
        """
        csv_files = FileUtils.get_used_files_list_from_key_name(csv_key_name)
        csv_with_cypher_files = CypherUtils.get_csv_with_cypher_files(csv_files)
        csv_with_cypher_files = csv_with_cypher_files.get('csv_with_cypher')

        csv_with_attributes = []

        for csv_with_cypher_file in csv_with_cypher_files:
            csv_name = csv_with_cypher_file.csv_name
            cypher_array = csv_with_cypher_file.cypher_array

            dict_tmp = {'csv_name': csv_name, 'used_attributes': set()}

            for cypher_file in cypher_array:
                for used_attribute in cypher_file.used_attributes:
                    dict_tmp['used_attributes'].add(used_attribute.attribute_name)

            dict_tmp['used_attributes'] = [attribute for attribute in dict_tmp['used_attributes']]
            csv_with_attributes.append(dict_tmp)
            
        return csv_with_attributes

    @staticmethod
    def get_missed_attributes_from_cypher_file(csv_files:list, missed_attributes:list) -> list:
        """
        Método que retorna uma lista com os atributos que estão faltando no header, com o nome do CSV, qual o nome
        do arquivo cypher e em quais linhas eles são utilizados. Exemplo:
        
        get_missed_attributes_from_cypher_file([licitacoes_propostas.csv, empenho.csv], ['cd_ugestora'])
        [
            {
                'csv_name': 'licitacoes_propostas.csv', 
                'cypher_array': [
                    {
                        'file_name': 'rel_licitacoes_propostas.cypher', 
                        'used_attributes': [
                            {
                                'attribute_name': 'cd_ugestora', 
                                'line_numbers': [4, 14, 18]
                            }
                        ]
                    }
                ]
            }
        ]
        """
        csv_with_cypher_files = CypherUtils.get_csv_with_cypher_files(csv_files)
        csv_with_cypher_files = csv_with_cypher_files.get('csv_with_cypher')

        missed_files_with_attributes = []

        for csv_with_cypher_file in csv_with_cypher_files:
            csv_with_cypher = CsvWithCypher(csv_name=csv_with_cypher_file.csv_name, cypher_array=[])
            cypher_array = csv_with_cypher_file.cypher_array

            for cypher_file in cypher_array:
                temp_cypher_file = CypherFile(file_name=cypher_file.file_name, used_attributes=[])

                for used_attribute in cypher_file.used_attributes:
                    if (used_attribute.attribute_name in missed_attributes):
                        temp_cypher_file.used_attributes.append(used_attribute)

                if (temp_cypher_file.used_attributes != []):
                    csv_with_cypher.cypher_array.append(temp_cypher_file)
                
            if (csv_with_cypher.cypher_array != []):
                missed_files_with_attributes.append(csv_with_cypher)
    
        return missed_files_with_attributes