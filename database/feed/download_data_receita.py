import gdown

EMPRESAS_URL = 'https://drive.google.com/uc?id=1c_gwLqaVQzRmY2IYCMyPDDCoC8OtTuiW'
OUTPUT_FILE_EMPRESAS = '../../dados/empresa.csv.gz'


gdown.download(EMPRESAS_URL, output=OUTPUT_FILE_EMPRESAS)