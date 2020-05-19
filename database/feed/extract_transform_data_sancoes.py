import csv
import io
import zipfile as zf
import gzip

CEIS_INPUT_ZIP = '../../dados/ceis.zip'
CEIS_OUTPUT_CSV = '../../dados/ceis.csv'
HEADER_SIZE_CEIS = 22

CEPIM_INPUT_ZIP = '../../dados/cepim.zip'
CEPIM_OUTPUT_CSV = '../../dados/cepim.csv'
HEADER_SIZE_CEPIM = 5

CNEP_INPUT_ZIP = '../../dados/cnep.zip'
CNEP_OUTPUT_CSV = '../../dados/cnep.csv'
HEADER_SIZE_CNEP = 21

FILENAME_INDEX = 0
HEADER_SIZE = 22

def get_zip_file_name(zip_file):
    zip_file = zf.ZipFile(zip_file)
    return zip_file.namelist()[FILENAME_INDEX]

def extract_sancoes(zip_file, file_to_decompress):
    zip_file = zf.ZipFile(zip_file)
    with io.TextIOWrapper(zip_file.open(file_to_decompress), encoding="latin1") as text_file:
        for line in text_file:
            yield line
    
def transform_sancoes(line, header_size):
    for fields in csv.reader([line], delimiter=";"):
        assert len(fields) ==  header_size
        return fields

if __name__ == '__main__':
    ceis_zip_file_name = get_zip_file_name(CEIS_INPUT_ZIP)
    cepim_zip_file_name = get_zip_file_name(CEPIM_INPUT_ZIP)
    cnep_zip_file_name = get_zip_file_name(CNEP_INPUT_ZIP)
    

    with open(CEIS_OUTPUT_CSV, 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=";", quoting=csv.QUOTE_NONNUMERIC)
        for line in extract_sancoes(CEIS_INPUT_ZIP, ceis_zip_file_name):
            row = transform_sancoes(line, HEADER_SIZE_CEIS)
            writer.writerow(row)


    with open(CEPIM_OUTPUT_CSV, 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=";", quoting=csv.QUOTE_NONNUMERIC)
        for line in extract_sancoes(CEPIM_INPUT_ZIP, cepim_zip_file_name):
            row = transform_sancoes(line, HEADER_SIZE_CEPIM)
            writer.writerow(row)

    with open(CNEP_OUTPUT_CSV, 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=";", quoting=csv.QUOTE_NONNUMERIC)
        for line in extract_sancoes(CNEP_INPUT_ZIP, cnep_zip_file_name):
            row = transform_sancoes(line, HEADER_SIZE_CNEP)
            writer.writerow(row)
