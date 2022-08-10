import logging
from logging.config import dictConfig
from datetime import date, timedelta

from log_utils.log_utils import LogUtils
from etl_utils import download_file, is_url_status_ok

from exceptions.valid_url_not_found_exception import ValidUrlNotFoundException
from exceptions.invalid_download_days_limit_exception import InvalidDownloadDaysLimitException
class DownloadSancao:

    def __init__(self, base_url, output_zip_file, max_days_from_today):
        self.base_url = base_url
        self.output_zip_file = output_zip_file
        self.max_days_from_today = max_days_from_today
        dictConfig(LogUtils.get_updated_dict_config())

    def __str__(self):
        return f'BASE_URL={self.base_url}, OUTPUT_ZIP_FILE={self.output_zip_file}, MAX_DAYS_FROM_TODAY={self.max_days_from_today}'

    def get_date(self):
        day = date.today()
        return day.strftime("%Y%m%d")

    def is_invalid_download_days_limit(self, days_before_today:int, max_days_from_today:int) -> bool:
        '''
        Função que retorna se a quantidade de dias a partir de hoje a ser utilizada na URL para download
        já atingiu o limite máximo de dias, que para ser um limite válido não pode ser maior que a quantidade
        máxima de dias a partir de hoje

        return False: days_before_today <= max_days_from_today
        return True: days_before_today > max_days_from_today
        '''
        return days_before_today > max_days_from_today

    def download_from_url(self):
        final_url = self.base_url + self.get_date()
        valid_url = is_url_status_ok(final_url)
        days_before_today = 0
        
        while not (is_url_status_ok(final_url) or self.is_invalid_download_days_limit(days_before_today, self.max_days_from_today)):
            day = date.today() - timedelta(days=days_before_today)
            final_url = self.base_url + day.strftime("%Y%m%d")
            valid_url = is_url_status_ok(final_url)
            days_before_today += 1
        
        if (not valid_url):
            raise ValidUrlNotFoundException(f'Nenhuma URL válida com resposta 200 OK foi encontrada a partir do objeto: {str(self)}')

        if (self.is_invalid_download_days_limit(days_before_today, self.max_days_from_today)):
            raise InvalidDownloadDaysLimitException('O limite máximo de dias para a tentativa download foi atingido: '
                f'total de tentativas {days_before_today} é maior que total máximo permitido {self.max_days_from_today}')

        logging.info(f'Tentando realizar download com a URL {final_url}')
        download_file(final_url, self.output_zip_file)