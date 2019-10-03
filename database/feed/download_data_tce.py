from etl_utils import download_file

LICITACOES_URL = 'https://dados.tce.pb.gov.br/TCE-PB-Portal-Gestor-Licitacoes_Propostas.txt.gz'
OUTPUT_FILE = '../../dados/TCE-PB-Portal-Gestor-Licitacoes_Propostas.txt.gz'

if __name__ == '__main__':
    download_file(LICITACOES_URL, OUTPUT_FILE)