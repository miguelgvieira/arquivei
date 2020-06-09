Projeto feito para o processo seletivo da empresa Arquivei.

## Como usar
Para subir o projeto, apenas é necessário rodar o comando:

```shell
docker-compose up --build
```

Ele irá subir dois dockers, um para o banco de dados(MysSql), e outro uma instância python, onde irá instalar todas as dependências necessárias, e expor a porta 5000.

## Endpoints

Três Endpoints foram criados nesse projeto:

    POST - /api/v1/nfe/arquivei

Endpoint que irá bater na api da arquivei disponibilizada para o projeto. Pegará todas as Nota Fiscais Eletrônicas do endpoint, e salvará access_key e valor total no banco de dados.

    GET - /api/v1/nfe/

Endpoint para retornar todas as notas fiscais salvas no banco de dados

    GET - /api/v1/nfe/access_key/<access_key>

Endpoint que retorna uma única nota fiscal, com a "access_key" igual à fornecida na uri.