import os
import datetime

PREFIX = "python3"
TEST_FILES = [
    'test_candidato.py',
    'test_unidade_gestora.py',
    'test_socio.py',
    'test_participante.py',
    'test_empresa.py'
]

def get_time():
    now = datetime.datetime.now()
    hours = now.hour
    minutes = now.minute
    seconds = now.second

    return '{}h:{}m:{}s'.format(hours, minutes, seconds)


if __name__ == "__main__":
    start_time = '[START TIME]: ' + get_time()

    for file in TEST_FILES:
        os.system(PREFIX + " " + file)
    
    finish_time = '[FINISH TIME]: ' + get_time()

    print(start_time)
    print(finish_time)