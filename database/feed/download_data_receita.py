from etl_utils import download_file

URL_PREFIX = 'https://data.brasil.io/dataset/socios-brasil/'

SOCIOS_URL = URL_PREFIX + 'socio.csv.gz'
OUTPUT_FILE_SOCI0S = '../../dados/socio.csv.gz'

EMPRESAS_URL = URL_PREFIX + 'empresa.csv.gz'
OUTPUT_FILE_EMPRESAS = '../../dados/empresa.csv.gz'


if __name__ == "__main__":
    download_file(url=SOCIOS_URL, output_file=OUTPUT_FILE_SOCI0S)
    download_file(url=EMPRESAS_URL, output_file=OUTPUT_FILE_EMPRESAS)