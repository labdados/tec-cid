# tec-cid

Sistema do projeto Tecnologia Cidadã - PROBEX 2019

## Como rodar a API REST e o banco de dados Neo4j

### Pré-requesitos

- Docker

### Passo a passo

1. Clonar este repositório:

```
git clone https://github.com/labdados/tec-cid.git
```

2. No diretório `tec-cid`, criar um `.env` com base no `.env.example`:

```
cd tec-cid
cp .env.example .env
```

3. Executar banco de dados neo4j e servidor da API REST, configurados no docker-compose.yml:
```
docker-compose up
```

4. Fazer download dos dados do TCE-PB e TSE, e alimentar o banco de dados neo4j:

```
cd database/feed
./extract_data_tce-pb.sh
./extract_data_tse.sh
./feed_docker_neo4j.sh
```

5. Verificar se tudo ocorreu como esperado acessando a [API](http://localhost:5000/tec-cid/api/docs) e o [browser do neo4j](http://localhost:7474/browser), usando as credenciais especificadas no `.env`
