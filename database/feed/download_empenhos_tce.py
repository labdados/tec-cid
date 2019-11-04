from etl_utils import download_file

EMPENHOS_URL = "https://dados.tce.pb.gov.br/TCE-PB-SAGRES-Empenhos_Esfera_Municipal.txt.gz"
OUTPUT_FILE = '../../dados/TCE-PB-SAGRES-Empenhos_Esfera_Municipal.txt.gz'

if __name__ == '__main__':
    download_file(EMPENHOS_URL, OUTPUT_FILE)