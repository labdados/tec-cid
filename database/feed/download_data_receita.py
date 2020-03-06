import gdown

SOCIOS_URL = 'https://drive.google.com/uc?id=19DeL9HbOebNXRFZ_bmmZu1uAogdY8ZGI'
OUTPUT_FILE_SOCI0S = '../../dados/socio.csv.gz'

EMPRESAS_URL = 'https://drive.google.com/uc?id=1c_gwLqaVQzRmY2IYCMyPDDCoC8OtTuiW'
OUTPUT_FILE_EMPRESAS = '../../dados/empresa.csv.gz'


gdown.download(EMPRESAS_URL, output=OUTPUT_FILE_EMPRESAS)
gdown.download(SOCIOS_URL, output=OUTPUT_FILE_SOCI0S)