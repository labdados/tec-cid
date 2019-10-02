# Back-end do projeto Tecnologia Cidadã

## Pré-requisitos

- Docker
- Python 3.6+

## Rodando o banco de dados (Neo4j) e a API REST (Flask)

No diretório raíz do projeto (`tec-cid/`):

```
docker-compose up
```

## Alimentando o banco

Entre no diretório de feed do BD:

```
cd database/feed
```

Garanta que as dependências estão instaladas:

```
pip3 install -r requirements.txt
```

Rode os scripts para fazer download dos dados do TCE-PB e TSE:

```
python3 download_data_tce.py
python3 download_data_tse.py
```

Em seguida, roda os scripts para extrair, transformar e criar os arquivos CSV de entrada:

```
python3 extract_transform_data_tce.py
python3 extract_transform_data_tse.py
```

Por fim, rode os scripts para carregar os dados no BD.
```
python3 load_data_tce.py
python3 load_data_tse.py
```

OBS: Você pode rodar esta mesma sequência de alimentação do BD para atualizar o mesmo apenas com dados novos, sem precisar apagar os dados atuais.