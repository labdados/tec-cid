import csv
import io
import zipfile as zf
import gzip

from zipped_file_utils import ZippedFilesUtils

PREFIX = '../../dados/'
FILENAME_INDEX = 0

def get_zip_file_name(zip_file):
    zip_file = zf.ZipFile(zip_file)
    return zip_file.namelist()[FILENAME_INDEX]

def extract_sancoes(zip_file, file_to_decompress):
    zip_file = zf.ZipFile(zip_file)
    with io.TextIOWrapper(zip_file.open(file_to_decompress), encoding="latin1") as text_file:
        for line in text_file:
            yield line
    
def transform_sancoes(line):
    for fields in csv.reader([line], delimiter=";"):
        return fields

if __name__ == '__main__':
    zipped_files = ZippedFilesUtils.get_zipped_files_from_key('sancoes')

    for zipped_file in zipped_files:
        final_path = PREFIX + zipped_file.get('output_csv')
        with open(final_path, 'w') as csv_file:
            writer = csv.writer(csv_file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
            for line in extract_sancoes(PREFIX + zipped_file.get('input_zip'),  get_zip_file_name(PREFIX + zipped_file.get('input_zip'))):
                row = transform_sancoes(line)
                writer.writerow(row)