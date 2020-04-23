import os
import datetime

PREFIX = "python3"
BLANK_SPACE = " "

DOWNLOAD_FILES = [
    'download_data_tce.py',
    'download_data_tse.py',
    'download_data_receita.py'
]

EXTRACT_FILES = [
    'extract_transform_data_tce.py',
    'extract_transform_data_tse.py',
    'extract_transform_data_empresas.py',
    'extract_transform_data_socios.py'
]

LOAD_FILES = [
    'load_data_tce.py',
    'load_data_tse.py',
    'load_data_receita.py'
]

def get_time():
    now = datetime.datetime.now()
    hours = now.hour
    minutes = now.minute
    seconds = now.second

    return '{}h:{}m:{}s'.format(hours, minutes, seconds)

def download_files(download_files):
    for file in download_files:
        os.system(PREFIX + BLANK_SPACE + file)

def extract_files(extract_files):
    for file in extract_files:
        os.system(PREFIX + BLANK_SPACE + file)

def load_data(load_files):
    for file in load_files:
        os.system(PREFIX + BLANK_SPACE + file)


if __name__ == "__main__":
    try:
        start_time = '[START TIME]: ' + get_time()

        os.system("pip3 install -r requirements.txt")

        download_files(DOWNLOAD_FILES)
        extract_files(EXTRACT_FILES)
        # load_data(LOAD_FILES)

    except Exception as error:
        print(error)

    finally:
        finish_time = '[FINISH TIME]: ' + get_time()

        print(start_time)
        print(finish_time)