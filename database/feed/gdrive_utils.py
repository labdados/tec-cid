import requests
import csv 

ID_INDEX = 0 # ID do arquivo no Google Drive
FILE_NAME_INDEX = 1
BASE_URL = "https://docs.google.com/uc?export=download"


def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, path_to_download):
    CHUNK_SIZE = 32768

    with open(path_to_download, 'wb') as file:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:
                file.write(chunk)

def download_file(id, path_to_download):
    session = requests.Session()
    response = session.get(BASE_URL, params = {'id': id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {'id': id, 'confirm': token}
        response = session.get(BASE_URL, params = params, stream=True)

    save_response_content(response, path_to_download)

def get_dictionary(csv_file):
    with open(csv_file, 'r') as file:
        csv_data = csv.reader(file, delimiter=",")
        next(csv_data) # Skip title line
        dictionary = {}
        for row in csv_data:
            dictionary[row[ID_INDEX]] = row[FILE_NAME_INDEX]

    return dictionary