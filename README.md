# tec-cid
Sistema do projeto Tecnologia Cidadã - PROBEX 2019


## Como executar a API e o Banco do projeto localmente:

### Pré-requesitos
Docker

### Passo a passo

1º Clonar o repositório do [tec-cid](https://github.com/labdados/tec-cid.git).

2º No diretório /tec-cid criar um .env com os seguintes dados:
```bash

NEO4J_HOST=neo4j
NEO4J_PORT=7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=password
NEO4J_AUTH=neo4j/password
NEO4J_DIR_IMPORT=/import

NEO4J_dbms_memory_heap_initial__size=1G
NEO4J_dbms_memory_heap_max__size=4G
NEO4J_dbms_connectors_default__listen__address=0.0.0.0

```
3º No diretório ``` /tec-cid ``` rodar o ```docker-compose up```

4º Após isso é necessário popular o banco, para isso vá para o diretório ```database/feed``` e rode o script ```feed_docker_neo4j.sh``` (Caso haja erro de permissão, dar um ```chmod -R 777```).

5º Verificar se tudo ocorreu como esperado acessando a [API](http://localhost:5000/tec-cid/api/docs) e o [Banco](http://localhost:7474/browser).
