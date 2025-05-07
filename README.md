API de Livros
=============

📚 Esta é uma API simples desenvolvida em Python com Flask, que permite realizar operações básicas (CRUD) em um catálogo de livros.

Objetivo
--------
Criar uma API REST que permita:
- Consultar todos os livros
- Consultar um livro específico por ID
- Adicionar um novo livro
- Editar um livro existente
- Excluir um livro

Tecnologias utilizadas
----------------------
- Python
- Flask

URL Base
--------
http://localhost

Endpoints
---------
Consultar todos os livros:
  GET /livros

Consultar livro por ID:
  GET /livros/<int:id>

Adicionar novo livro:
  POST /livros

Editar livro existente:
  PUT /livros/<int:id>

Excluir livro:
  DELETE /livros/<int:id>

Recursos disponíveis
--------------------
Livros:
  Cada livro possui:
    - id: Identificador único (int)
    - título: Título do livro (string)
    - autor: Nome do autor (string)

Exemplo de dados (JSON)
-----------------------
{
  "id": 1,
  "título": "Harry Potter e a Pedra Filosofal: 1",
  "autor": "J.K Rowling"
}

Executando o projeto
---------------------
1. Instale o Flask:
   pip install flask

2. Execute a aplicação:
   python nome_do_arquivo.py

3. Acesse no navegador ou via Postman:
   http://localhost:5000/livros

Contato
-------
Feito com 💻 por Tainá
