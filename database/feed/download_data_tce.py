from etl_utils import download_file

LICITACOES_URL = 'https://dados.tce.pb.gov.br/TCE-PB-Portal-Gestor-Licitacoes_Propostas.txt.gz'
OUTPUT_FILE_LICITACOES = '../../dados/TCE-PB-Portal-Gestor-Licitacoes_Propostas.txt.gz'

EMPENHOS_URL = "https://dados.tce.pb.gov.br/TCE-PB-SAGRES-Empenhos_Esfera_Municipal.txt.gz"
OUTPUT_FILE_EMPENHOS = '../../dados/TCE-PB-SAGRES-Empenhos_Esfera_Municipal.txt.gz'

PAGAMENTOS_URL = 'https://dados.tce.pb.gov.br/TCE-PB-SAGRES-Pagamentos_Esfera_Municipal.txt.gz'
OUTPUT_FILE_PAGAMENTOS = '../../dados/TCE-PB-SAGRES-Pagamentos_Esfera_Municipal.txt.gz'


if __name__ == '__main__':
    download_file(LICITACOES_URL, OUTPUT_FILE_LICITACOES)
    download_file(EMPENHOS_URL, OUTPUT_FILE_EMPENHOS)
    # download_file(PAGAMENTOS_URL, OUTPUT_FILE_PAGAMENTOS)