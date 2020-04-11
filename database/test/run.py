import os

PREFIX = "python"
TEST_FILES = [
    'test_candidato.py',
    'test_unidade_gestora.py',
    'test_socio.py',
    'test_empresa.py'
]

if __name__ == "__main__":
    for file in TEST_FILES:
        os.system(PREFIX + " " + file)