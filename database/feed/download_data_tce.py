from etl_utils import download_file
from download_utils import DownloadUtils

PREFIX = '../../dados/'
KEY = 'tce'
UNSED_KEYS = ['pagamentos']

if __name__ == '__main__':
    download_file_names = DownloadUtils.get_download_file_names_from_key(key_name=KEY)

    for key, value in download_file_names.items():
        if (key not in UNSED_KEYS):
            download_file(url=value['url'], output_file=PREFIX + value['output_file'])