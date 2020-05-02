from etl_utils import download_file, is_url_status_ok
from datetime import date, timedelta

OK_STATUS = 200
URL = 'http://www.portaltransparencia.gov.br/download-de-dados/ceis/'
OUTPUT_FILE_CEIS = '../../dados/ceis.zip'

def get_date():
    day = date.today()
    return day.strftime("%Y%m%d")

if __name__ == '__main__':
    final_url = URL + get_date()
    valid_url = is_url_status_ok(final_url)

    days_before_today = 0
    while not is_url_status_ok(final_url) or days_before_today > 10:
        day = date.today() - timedelta(days=days_before_today)
        final_url = URL + day.strftime("%Y%m%d")
        valid_url = is_url_status_ok(final_url)
        days_before_today += 1

    assert valid_url == True
    print(final_url)
    download_file(final_url, OUTPUT_FILE_CEIS)