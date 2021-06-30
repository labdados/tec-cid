import logging
from logging.config import dictConfig

from log_utils.log_utils import LogUtils
from download_data_sancoes_utils import DownloadSancao
from download_utils import DownloadUtils

PREFIX = '../../dados/'
KEY = 'sancoes'

if __name__ == '__main__':
    dictConfig(LogUtils.get_updated_dict_config())
    download_file_names = DownloadUtils.get_download_file_names_from_key(key_name=KEY)

    for key, value in download_file_names.items():
        sancao = DownloadSancao(value['url'], PREFIX + value['output_file'], value['max_days_from_today'])
        logging.info(f'A iniciar download do arquivo {value["output_file"]}')
        sancao.download_from_url()