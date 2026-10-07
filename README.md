# 🎫 Sistema de Controle de Chamados

API REST desenvolvida em **Python** com **FastAPI** e **SQLite** para gerenciamento de chamados de suporte.

O projeto foi desenvolvido como parte dos meus estudos em **desenvolvimento backend**, com foco em APIs, banco de dados, organização de código e operações CRUD.

## 🚀 Funcionalidades

* ✅ Criar chamados
* 📋 Listar todos os chamados
* 🔎 Consultar chamado por ID
* 🔄 Alterar status do chamado
* 🗑️ Excluir chamado
* ❌ Retornar HTTP 404 quando o chamado não existe

## 🛠️ Tecnologias

* **Python**
* **FastAPI**
* **SQLite**
* **Pydantic**
* **Uvicorn**
* **Swagger / OpenAPI**

## 📁 Estrutura do projeto

```text
sistema-de-controle-de-chamados/
│
├── main.py
├── banco.py
├── services.py
├── schemas.py
├── banco.db
└── README.md
```

### `main.py`

Responsável pelas rotas e pela comunicação com a API.

### `services.py`

Contém a lógica da aplicação e faz a ligação entre as rotas e o banco de dados.

### `banco.py`

Responsável pelas operações com o SQLite, como:

* criação da tabela
* inserção
* consulta
* alteração
* exclusão

### `schemas.py`

Contém os modelos Pydantic utilizados para validar os dados recebidos e retornados pela API.

## 🔄 Endpoints

| Método   | Endpoint                        | Função                  |
| -------- | ------------------------------- | ----------------------- |
| `GET`    | `/chamados`                     | Lista todos os chamados |
| `POST`   | `/chamados`                     | Cria um novo chamado    |
| `GET`    | `/chamados/{id_chamado}`        | Consulta um chamado     |
| `PUT`    | `/chamados/{id_chamado}/status` | Altera o status         |
| `DELETE` | `/chamados/{id_chamado}`        | Exclui um chamado       |

## 📌 Status disponíveis

Os chamados podem possuir os seguintes status:

* `Aberto`
* `Em andamento`
* `Concluído`

## ▶️ Como executar

Clone o repositório e entre na pasta do projeto:

```bash
cd sistema-de-controle-de-chamados
```

Instale as dependências:

```bash
pip install fastapi uvicorn
```

Execute a API:

```bash
python -m uvicorn main:app --reload
```

A API estará disponível em:

```text
http://127.0.0.1:8000
```

## 📚 Documentação

O FastAPI disponibiliza automaticamente a documentação interativa através do Swagger.

Acesse:

```text
http://127.0.0.1:8000/docs
```

Por lá é possível testar todos os endpoints da API diretamente pelo navegador.

## 🎯 Objetivo do projeto

O objetivo deste projeto foi colocar em prática conceitos de desenvolvimento backend, principalmente:

* criação de APIs REST
* operações CRUD
* integração com banco de dados
* validação de dados
* organização por responsabilidades
* tratamento de erros HTTP
* utilização do Swagger para testes

Este projeto faz parte da minha jornada de estudos em **desenvolvimento backend com Python**.
