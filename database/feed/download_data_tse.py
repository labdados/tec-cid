import logging

from logging.config import dictConfig
from log_utils.log_utils import LogUtils

from etl_utils import download_file
from download_utils import DownloadUtils

INDEX_VALUES = 0
PREFIX = '../../dados/'
KEY = 'tse'

dictConfig(LogUtils.get_updated_dict_config())

headers = {
    'authority': 'cdn.tse.jus.br',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'dnt': '1',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-platform': '"Linux"',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'Accept-Encoding': None
}

if __name__ == '__main__':
    download_file_names = DownloadUtils.get_download_file_names_from_key(key_name=KEY)

    for download_file_name in download_file_names:
        for key, files in download_file_name.items():
            for file in files:
                logging.info(f"Iniciando download do arquivo {file['output_file']} a partir da URL {file['url']}")
                download_file(url=file['url'], output_file=PREFIX + file['output_file'], headers=headers)