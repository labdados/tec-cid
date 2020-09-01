from gdrive_utils import download_file, get_dictionary
import datetime

DOWNLOAD_RECEITA_CSV = '../../dados/download_receita.csv'


def get_time():
    now = datetime.datetime.now()
    hours = now.hour
    minutes = now.minute
    seconds = now.second
    return '{}h:{}m:{}s'.format(hours, minutes, seconds)


if __name__ == '__main__':
    files = get_dictionary(DOWNLOAD_RECEITA_CSV)
    path = '../../dados/'

    for id, name in files.items():
        try:
            final_path = path + name

            print(f'[{get_time()}] Starting download: {name}')
            download_file(id, final_path)
            print(f'[{get_time()}] Finished download: {name}\n\n')

        except Exception as e:
            print(e)