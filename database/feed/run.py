import os
import datetime
import traceback


PREFIX = "python3"
BLANK_SPACE = " "

DOWNLOAD_FILES = [
    'download_data_tce.py',
    'download_data_tse.py',
    'download_data_receita.py'
]

EXTRACT_TRANSFORM_TCE       =    'extract_transform_data_tce.py'
EXTRACT_TRANSFORM_TSE       =    'extract_transform_data_tse.py'   
EXTRACT_TRANSFORM_EMPRESAS  =    'extract_transform_data_empresas.py'   
EXTRACT_TRANSFORM_SOCIOS    =    'extract_transform_data_socios.py'  

LOAD_DATA_TCE               =    'load_data_tce.py'
LOAD_DATA_TSE               =    'load_data_tse.py'
LOAD_DATA_RECEITA           =    'load_data_receita.py'


def download_files(download_files):
    for file in download_files:
        os.system(PREFIX + BLANK_SPACE + file)

def extract_file(extract_file):
    os.system(PREFIX + BLANK_SPACE + extract_file)

def load_data(load_file):
    os.system(PREFIX + BLANK_SPACE + load_file)

def get_time():
    now = datetime.datetime.now()
    hours = now.hour
    minutes = now.minute
    seconds = now.second

    return '{}h:{}m:{}s'.format(hours, minutes, seconds)


if __name__ == "__main__":

    try:
        start_time = '[START TIME]: ' + get_time()

        os.system("pip3 install -r requirements.txt")

        download_files(DOWNLOAD_FILES)

        extract_file(EXTRACT_TRANSFORM_TCE)
        extract_file(EXTRACT_TRANSFORM_TSE)

        load_data(LOAD_DATA_TCE)
        load_data(LOAD_DATA_TSE)

        extract_file(EXTRACT_TRANSFORM_EMPRESAS)
        extract_file(EXTRACT_TRANSFORM_SOCIOS)

        load_data(LOAD_DATA_RECEITA)

    except Exception as error:
        print(error)
        print(traceback.format_exc())

    finally:
        finish_time = '[FINISH TIME]: ' + get_time()

        print(start_time)
        print(finish_time)