from logging import currentframe
from os import path, makedirs
from pathlib import Path
from json import load, dumps
from datetime import date
from calendar import timegm
from time import gmtime


class LogUtils:

    __LOGS_DIRECTORY = '../logs/'
    __DICT_CONFIG_JSON = path.dirname(path.realpath('dict_config.json')) + '/log_utils/dict_config.json'

    @staticmethod
    def get_absolute_path(relative_path:str) -> str:
        '''
        Método que retorna o caminho absoluto a partir do caminho relativo do parâmetro.
        Exemplo: relative_path='../logs/mm-YYYY',
        get_absolute_path(relative_path) -> '/home/user/tec-cid/database/feed/logs/mm-YYYY'
        '''
        path = Path(relative_path).resolve()
        return str(path)

    @staticmethod
    def generate_directory(current_dir_name:str) -> None:
        '''
        Método para gerar um diretório a partir do nome passado como parâmetro
        '''
        final_dir_name = path.join(LogUtils.__LOGS_DIRECTORY, current_dir_name)
        makedirs(name=final_dir_name, exist_ok=True)

    @staticmethod
    def get_relative_directory_name() -> str:
        '''
        Método que retorna o caminho relativo com o nome do diretório que deverá ser utilizado
        para salvar os logs, que contém mês e ano no formato mm-YYYY
        '''
        current_dir_name = date.today().strftime('%m-%Y')
        LogUtils.generate_directory(current_dir_name)
        
        return path.join(LogUtils.__LOGS_DIRECTORY, current_dir_name)

    @staticmethod
    def get_epoch_timestamp():
        '''
        Método para retornar o timestamp da época atual em segundos.
        Exemplo: timegm(tm_year=2021, tm_mon=5, tm_mday=25, tm_hour=21, tm_min=1, tm_sec=57) -> 1621976517
        '''
        return str(timegm(gmtime()))

    @staticmethod
    def generate_log_filename() -> str:
        '''
        Método que gera o nome do arquivo de log, com o dia, mês e ano no formato
        dd-mm-yyyy_etl.log. Exemplo: 06-08-2020_etl.log
        '''
        current_epoch = LogUtils.get_epoch_timestamp()
        log_filename =  f'etl_{current_epoch}.log'

        return log_filename

    @staticmethod
    def get_path_log_file():
        '''
        Método para retornar o caminho absoluto do arquivo de log que deverá ser utilizado.
        Exemplo: home/user/tec-cid/database/feed/logs/08-2020/06-08-2020_etl.log
        '''
        relative_dir_name = LogUtils.get_relative_directory_name()
        absolute_path = LogUtils.get_absolute_path(relative_dir_name)
        file_name = LogUtils.generate_log_filename()

        final_log_path = path.join(absolute_path, file_name)

        return final_log_path

    @staticmethod
    def get_dict_config() -> dict:
        '''Método que obtém o dicionário de configuração que está no arquivo JSON LogUtils.__DICT_CONFIG_JSON'''
        with open(LogUtils.__DICT_CONFIG_JSON, 'r') as dict_file:
            return load(dict_file)

    @staticmethod
    def update_override_log_filename(override_filename:bool) -> None:
        '''
        Método para atualizar o atributo override_filename para
        sobrescrever ou não o nome do arquivo de log que fica em handlers.file_handler.filename
        no LogUtils.__DICT_CONFIG_JSON
        '''
        dict_config = LogUtils.get_dict_config()
        dict_config['override_log_filename'] = override_filename
        dict_config_json = dumps(dict_config, ensure_ascii=False, indent=4)

        with open(LogUtils.__DICT_CONFIG_JSON, 'w') as json_file:
            json_file.write(dict_config_json)

    @staticmethod
    def update_dict_config_filename() -> dict:
        '''Método que atualiza o nome do arquivo de log no dicionário de configuração (LogUtils.__DICT_CONFIG_JSON)'''
        dict_config = LogUtils.get_dict_config()

        if (dict_config['override_log_filename']):
            log_filename = LogUtils.get_path_log_file()
            dict_config['handlers']['file_handler']['filename'] = log_filename

        return dict_config

    @staticmethod
    def get_updated_dict_config() -> dict:
        '''Método que retorna o dicionário de configuração atualizado com o nome do arquivo de log que deverá ser utilizado'''
        dict_config = LogUtils.update_dict_config_filename()
        dict_config_json = dumps(dict_config, ensure_ascii=False, indent=4)

        with open(LogUtils.__DICT_CONFIG_JSON, 'w') as json_file:
            json_file.write(dict_config_json)

        return dict_config