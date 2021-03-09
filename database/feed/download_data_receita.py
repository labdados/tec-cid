from etl_utils import download_file
from download_utils import DownloadUtils

PREFIX = '../../dados/'
KEY = 'receita_federal'


if __name__ == "__main__":
    download_file_names = DownloadUtils.get_download_file_names_from_key(key_name=KEY)

    for key, value in download_file_names.items():
        download_file(url=value['url'], output_file=PREFIX + value['output_file'])