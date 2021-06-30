import os
import subprocess
import sys
import traceback
import datetime

import logging
from logging.config import dictConfig

from log_utils.log_utils import LogUtils
from headers.header_analyser import HeaderAnalyser
from headers.used_file_utils import UsedFileUtils
from headers.header_utils import HeaderUtils

PREFIX = "python3"
BLANK_SPACE = " "

DOWNLOAD_FILES = [
    'download_data_tce.py',
    'download_data_tse.py',
    'download_data_receita.py',
    'download_data_sancoes.py'
]

EXTRACT_TRANSFORM_TCE       =    'extract_transform_data_tce.py'
EXTRACT_TRANSFORM_TSE       =    'extract_transform_data_tse.py'
EXTRACT_TRANSFORM_EMPRESAS  =    'extract_transform_data_empresas.py'
EXTRACT_TRANSFORM_SOCIOS    =    'extract_transform_data_socios.py'
EXTRACT_TRANSFORM_SANCOES   =    'extract_transform_data_sancoes.py'

LOAD_DATA_TCE               =    'load_data_tce.py'
LOAD_DATA_TSE               =    'load_data_tse.py'
LOAD_DATA_RECEITA           =    'load_data_receita.py'
LOAD_DATA_SANCOES           =    'load_data_sancoes.py'


def download_files(download_files):
    for file in download_files:
        logging.info(f'Executando arquivo de download {file}')
        subprocess.run([PREFIX, file], check=True)

def extract_file(extract_file):
    logging.info(f'Executando arquivo de extração {extract_file}')
    subprocess.run([PREFIX, extract_file], check=True)

def load_data(load_file):
    logging.info(f'Executando arquivo de carregamento {load_file}')
    subprocess.run([PREFIX, load_file], check=True)

def get_time():
    now = datetime.datetime.now()
    hours = now.hour
    minutes = now.minute
    seconds = now.second

    return '{}h:{}m:{}s'.format(hours, minutes, seconds)


if __name__ == "__main__":
    try:
        global_start_time = '[GLOBAL START TIME]: ' + get_time()
        LogUtils.update_override_log_filename(override_filename=True)
        LogUtils.update_override_log_filename(override_filename=False)

        dictConfig(LogUtils.get_updated_dict_config())

        subprocess.run(['pip3', 'install', '-r', 'requirements.txt'], check=True)
        download_files(DOWNLOAD_FILES)

        extract_file(EXTRACT_TRANSFORM_TCE)
        extract_file(EXTRACT_TRANSFORM_TSE)

        HeaderUtils.fill_header_and_used_attributes(key_name='tce')
        HeaderUtils.fill_header_and_used_attributes(key_name='tse')

        tce = UsedFileUtils.get_used_files_list_from_key_name(key_name='tce')
        tse = UsedFileUtils.get_used_files_list_from_key_name(key_name='tse')
        HeaderAnalyser.analyze(key_name=None, file_names=tce + tse)

        HeaderAnalyser.analyze(key_name='tce')
        HeaderAnalyser.analyze(key_name='tse')

        load_data(LOAD_DATA_TCE)
        load_data(LOAD_DATA_TSE)

        extract_file(EXTRACT_TRANSFORM_EMPRESAS)
        extract_file(EXTRACT_TRANSFORM_SOCIOS)

        HeaderUtils.fill_header_and_used_attributes(key_name='receita_federal')
        HeaderAnalyser.analyze(key_name='receita_federal')

        load_data(LOAD_DATA_RECEITA)

        extract_file(EXTRACT_TRANSFORM_SANCOES)
        
        HeaderUtils.fill_header_and_used_attributes(key_name='sancoes')
        HeaderAnalyser.analyze(key_name='sancoes')

        load_data(LOAD_DATA_SANCOES)

    except AssertionError:
        _, _, tb = sys.exc_info()
        logging.critical(tb)
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        logging.critical(f'Ocorreu um erro de asserção na linha {line} no trecho "{text}" do arquivo {filename}')
        exit(1)

    except KeyboardInterrupt:
        logging.critical(traceback.format_exc())
        exit(1)

    except Exception as error:
        logging.critical(traceback.format_exc())
        exit(1)

    except:
        logging.critical(traceback.format_exc())
        exit(1)

    finally:
        LogUtils.update_override_log_filename(override_filename=True)
        global_finish_time = '[GLOBAL FINISH TIME]: ' + get_time()
        logging.info(global_start_time)
        logging.info(global_finish_time)