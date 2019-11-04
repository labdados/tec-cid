from etl_utils import download_file

PAGAMENTOS_URL = 'https://dados.tce.pb.gov.br/TCE-PB-SAGRES-Pagamentos_Esfera_Municipal.txt.gz'
OUTPUT_FILE = '../../dados/TCE-PB-SAGRES-Pagamentos_Esfera_Municipal.txt.gz'

if __name__ == '__main__':
    download_file(PAGAMENTOS_URL, OUTPUT_FILE)