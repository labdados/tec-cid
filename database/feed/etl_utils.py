import os
import requests
from py2neo import Graph
from tqdm import tqdm

OK_STATUS = 200

def download_file(url, output_file=None, chunk_size=8192, progress=True):
    if not output_file:
        output_file = url.split('/')[-1]
    elif os.path.isdir(output_file):
        output_file = os.path.join(output_file, url.split('/')[-1])
    
    with open(output_file, 'wb') as ouput:
        response = requests.get(url, stream=True)
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

def query_from_file(neo4j:Graph, cypher_file):
    with open(cypher_file) as f:
        query = f.read().rstrip("\n")
        print(query)
        return neo4j.evaluate(query)

def is_url_status_ok(url):
    return requests.get(url).status_code == OK_STATUS