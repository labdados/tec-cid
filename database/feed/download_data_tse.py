from etl_utils import download_file
from download_utils import DownloadUtils

INDEX_VALUES = 0
PREFIX = '../../dados/'
KEY = 'tse'

if __name__ == '__main__':
    download_file_names = DownloadUtils.get_download_file_names_from_key(key_name=KEY)

    for download_file_name in download_file_names:
        for key, files in download_file_name.items():
            for file in files:
                download_file(url=file['url'], output_file=PREFIX + file['output_file'])