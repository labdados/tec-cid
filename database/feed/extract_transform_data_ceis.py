import csv
import io
import zipfile as zf
import gzip

CEIS_INPUT_ZIP = '../../dados/ceis.zip'
CEIS_OUTPUT_CSV = '../../dados/ceis.csv'

FILENAME_INDEX = 0
HEADER_SIZE = 22

def get_zip_file_name(zip_file):
    zip_file = zf.ZipFile(zip_file)
    return zip_file.namelist()[FILENAME_INDEX]

def extract_ceis(zip_file, file_to_decompress):
    zip_file = zf.ZipFile(zip_file)
    with io.TextIOWrapper(zip_file.open(file_to_decompress), encoding="latin1") as text_file:
        for line in text_file:
            yield line
    
def transform_ceis(line):
    for fields in csv.reader([line], delimiter=";"):
        assert len(fields) ==  HEADER_SIZE
        return fields

if __name__ == '__main__':
    ceis_zip_file_name = get_zip_file_name(CEIS_INPUT_ZIP)

    with open(CEIS_OUTPUT_CSV, 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=";", quoting=csv.QUOTE_NONNUMERIC)
        
        for line in extract_ceis(CEIS_INPUT_ZIP, ceis_zip_file_name):
            row = transform_ceis(line)
            writer.writerow(row)