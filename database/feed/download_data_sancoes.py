from download_data_sancoes_utils import DownloadSancao
from download_utils import DownloadUtils

PREFIX = '../../dados/'
KEY = 'sancoes'

if __name__ == '__main__':
    download_file_names = DownloadUtils.get_download_file_names_from_key(key_name=KEY)

    for key, value in download_file_names.items():
        sancao = DownloadSancao(value['url'], PREFIX + value['output_file'], value['max_days_from_today'])
        print(f'A iniciar download do arquivo {value["output_file"]}...')
        sancao.download_from_url()