# tec-cid

Sistema do projeto Tecnologia Cidadã - PROBEX 2019

## Como rodar a API REST e o banco de dados Neo4j

### Pré-requisitos

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

4. Fazer download dos dados do TCE-PB, TSE e Receita Federal; extrair e transformar para criar CSVs no formato adequado e carregar o banco de dados neo4j. Carregue antes o `.env` para obter as credenciais do Neo4j, para que os scripts de load funcionem.

```
. .env
cd database/feed
pip3 install -r requirements.txt
python3 download_data_tce.py
python3 download_data_tse.py
python3 download_data_receita.py
python3 extract_transform_data_tce.py
python3 extract_transform_data_tse.py
python3 extract_transform_data_receita.py
python3 load_data_tce.py
python3 load_data_tse.py
python3 load_data_receita.py
```

Outra opção, caso as credenciais do neo4j não sejam carregadas do `.env`, é passar as credenciais direto nos scripts de load:

```
python3 load_data_tce.py <neo4j-user> <neo4j-password>
python3 load_data_tse.py <neo4j-user> <neo4j-password>
```

5. Verificar se tudo ocorreu como esperado acessando a [API](http://localhost:5000/tec-cid/api/docs) e o [browser do Neo4j](http://localhost:7474/browser), usando as credenciais especificadas no `.env`

## Como rodar o frontend em Angular

### Pré-requisitos

- npm

### Passo a passo (Para o ambiente de desenvolvimento)

O ambiente de desenvolvimento é aquele em que o programador usa para construir o software. Muitas das vezes é sua máquina local.

1. Clonar este repositório:

```
git clone https://github.com/labdados/tec-cid.git
```

2. No diretório `tec-cid/frontend/tec-cid`, rodar o comando `npm install`:

3. Iniciar o servidor angular com o comando `ng serve`

4. Acessar o browser no seguinte endereço `http://localhost:4200`

### Passo a passo (Para o ambiente de produção)

O ambiente de produçã é aquele em que o usuário final do sistema terá acesso. Nesse caso, um sevidor web por exemplo.
Para simular um ambiente de produção é só seguir os seguintes passos:

1. Clonar este repositório:

```
git clone https://github.com/labdados/tec-cid.git
```

2. No diretório `tec-cid/frontend/tec-cid`, rodar o comando `npm install`:

3. Buildar o sistema rodando o seguinte comando `ng build --prod` onde o `--prod` significa que o build será de produção. Isso criará um diretório chamado `/dist`

4. Dentro do diretório `/dist` rode o seguinte comando `npm init` para inicializar um arquivo `package.json`. Acesse o arquivo `package.json`, na parte de `scripts` adicione a seguinte linha `"start": "node index.js"` 

5. Feito isto, é hora de configurar o nosso servidor, para isso usaremos o express que é um framework Node.js. Criaremos dentro do diretório `/dist` um arquivo `index.js`. Utilize o exemplo `index.js.exemple`.

6. Agora só resta levantar o servidor. No diretório `/dist` rode o comando `npm start` e acesse o `http://localhost:3000`
