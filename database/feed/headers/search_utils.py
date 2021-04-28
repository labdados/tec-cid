from re import finditer
from re import search
from re import match

import json

class SearchUtils:
    __UNUSED_ATTRIBUTES = ['line.Nome do doador']
    APOSTROPHE = '`'

    @staticmethod
    def text_is_used(text, unused_attributes):
        for attribute in SearchUtils.__UNUSED_ATTRIBUTES:
            if (attribute == text):
                return False

        return True

    @staticmethod
    def text_is_present(full_text, text):
        is_used = SearchUtils.text_is_used(text, SearchUtils.__UNUSED_ATTRIBUTES)
        if (is_used):
            return text in full_text

        return None

    @staticmethod
    def get_matched_indexes_from_line(line:str) -> list:
        results = []
        for match in finditer('line', line):
            results.append([match.start(), match.end()])

        return results

    @staticmethod
    def get_used_attributes_from_cypher_file(file_array:list) -> list:
        """
        Método para obter os atributos utilizados no arquivo cypher
        que devem começar com 'line.*'
        """
        all_attributes = []

        for line in file_array:
            if (SearchUtils.text_is_present(line, 'line.')):
                results = []

                for match in finditer('line.', line):
                    results.append([match.start(), match.end()])

                # Pegando todos os atributos que começam com "line." e separando por pipe(|) para depois retornar os atributos daquela linha
                attributes = ''
                if results:
                    for result in results:
                        end = result[1]

                        has_apostrophe = False
                        if (line[end] == SearchUtils.APOSTROPHE):
                            has_apostrophe = True

                        total_apostrophes = 0
                        for char in line[end:]:
                            if (has_apostrophe and total_apostrophes < 2):
                                if (char == SearchUtils.APOSTROPHE):
                                    total_apostrophes += 1

                                attributes += char

                            elif (not char.isalpha() and (char == '_') or char.isalpha()):
                                attributes += char

                            elif (has_apostrophe or not char.isalpha()):
                                attributes += '|'
                                break

                    attributes = attributes.split('|')

                    # Removendo valores vazios ('')
                    final_attributes = [value for value in attributes if value]
                    all_attributes += final_attributes

        all_attributes = set(all_attributes)

        return list(all_attributes)