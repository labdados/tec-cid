from download_data_sancoes_utils import DownloadSancao
import csv

DOWNLOAD_DATA_SANCOES = '../../dados/download_data_sancoes.csv'

URL_INDEX = 0
OUTPUT_FILE_INDEX = 1
MAX_DAYS_INDEX = 2

if __name__ == '__main__':
    with open(DOWNLOAD_DATA_SANCOES, 'r') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        next(csv_data)

        for download in csv_data:
            sancao = DownloadSancao(download[URL_INDEX], download[OUTPUT_FILE_INDEX], int(download[MAX_DAYS_INDEX]))
            sancao.download_from_url()