import csv
import gzip
import io

EMPRESA_INPUT_GZIP = '../../dados/empresa.csv.gz'

def extract_empresa(input_gz):
    with io.TextIOWrapper(gzip.GzipFile(input_gz)) as csv_file:
        for line in csv_file:
            yield line

def transform_empresa(line, row):
    if (row != 1):
        for fields in csv.reader([line], delimiter=","):
            if (len(fields[31]) == 10):
                pass
            
            else:
                assert fields[31] == ''

if __name__ == '__main__':
    row = 1
    for line in extract_empresa(EMPRESA_INPUT_GZIP):
        transform_empresa(line, row)
        row += 1