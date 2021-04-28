import os
import subprocess
import requests
from py2neo import Graph
from tqdm import tqdm

MAX_RETRIES = 2
OK_STATUS = 200
COMPLETED_DOWNLOAD = 100

def download_file(url, output_file=None, chunk_size=8192, progress=True, total_retries=0):
    if not output_file:
        output_file = url.split('/')[-1]
    elif os.path.isdir(output_file):
        output_file = os.path.join(output_file, url.split('/')[-1])
    
    file_size = 0
    try:
        with open(output_file, 'wb') as ouput:
            response = requests.get(url, stream=True, headers={'Accept-Encoding': None})
            file_size = int(response.headers.get('content-length', 0))
            if progress:
                pbar = tqdm(total=file_size, unit='B', unit_scale=True, desc=output_file)
            for chunk in response.iter_content(chunk_size):
                if chunk:  # filter out keep-alive new chunks
                    ouput.write(chunk)
                    if progress:
                        pbar.update(chunk_size)
            if progress:
                pbar.close()

    finally:
        final_size = os.stat(output_file).st_size

        if (file_size != 0):
            result_percentage = (final_size/file_size) * 100
        
        else:
            result_percentage = 0

        retry_download(total_retries, result_percentage, url, output_file)

def retry_download(total_retries, result_percentage, url, output_file):
    if (result_percentage != COMPLETED_DOWNLOAD and total_retries < MAX_RETRIES):
        total_retries += 1
        print(f'\n[INFO] O arquivo {output_file} da URL {url} foi baixado apenas {result_percentage:.2f}% de 100%')
        print(f'[INFO] Realizando retentativa de download {total_retries}x de {MAX_RETRIES}x')
        download_file(url=url,output_file=output_file, total_retries=total_retries)

    elif (result_percentage == COMPLETED_DOWNLOAD):
        print(f'\n[INFO] O arquivo {output_file} da URL {url} foi baixado {result_percentage:.2f}%')
        return

    raise Exception(f'[EXCEPTION] Após {MAX_RETRIES} retentativas de download do arquivo {output_file} '
        + f'a partir da URL {url}, o download ficou apenas com {result_percentage:.2f}%')

def query_from_file(neo4j:Graph, cypher_file):
    with open(cypher_file) as f:
        query = f.read().rstrip("\n")
        print(query)
        return neo4j.evaluate(query)

def is_url_status_ok(url):
    return requests.get(url).status_code == OK_STATUS
