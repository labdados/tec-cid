from etl_utils import download_file, is_url_status_ok
from datetime import date, timedelta


class DownloadSancao:
    url = ''
    output_zip_file = ''
    max_days_from_today = 0

    def __init__(self, url, output_zip_file, max_days_from_today):
        self.url = url
        self.output_zip_file = output_zip_file
        self.max_days_from_today = max_days_from_today


    def get_date(self):
        day = date.today()
        return day.strftime("%Y%m%d")

    def download_from_url(self):
        final_url = self.url + self.get_date()
        valid_url = is_url_status_ok(final_url)

        days_before_today = 0
        while not (is_url_status_ok(final_url) or days_before_today > self.max_days_from_today):
            day = date.today() - timedelta(days=days_before_today)
            final_url = self.url + day.strftime("%Y%m%d")
            valid_url = is_url_status_ok(final_url)
            days_before_today += 1

        assert valid_url == True
        print(final_url)
        download_file(final_url, self.output_zip_file)