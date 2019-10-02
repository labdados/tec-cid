from etl_utils import download_file

OUTPUT_DIR = '../../dados/'
PRESTACAO_CONTAS_URL = 'http://agencia.tse.jus.br/estatistica/sead/odsele/prestacao_contas/prestacao_contas_2016.zip'
CANDIDATOS_URL = 'http://agencia.tse.jus.br/estatistica/sead/odsele/consulta_cand/consulta_cand_2016.zip'

if __name__ == '__main__':
    download_file(PRESTACAO_CONTAS_URL, OUTPUT_DIR)
    download_file(CANDIDATOS_URL, OUTPUT_DIR)