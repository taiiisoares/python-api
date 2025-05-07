from flask import Flask, jsonify, request

app = Flask (__name__)

livros = [
    {
        'id': 1,
        'título': 'Harry Potter e a Pedra Filosofal: 1',
        'autor': 'J.K Rowling'
    },
    {
        'id': 2,
        'título': 'O Senhor dos Anéis: A Sociedade do Anel',
        'autor': 'J.R.R. Tolkien'
    },
    {
        'id': 3,
        'título': '1984',
        'autor': 'George Orwell'
    },
    {
        'id': 4,
        'título': 'O Hobbit',
        'autor': 'J.R.R. Tolkien'
    },
    {
        'id': 5,
        'título': 'Dom Casmurro',
        'autor': 'Machado de Assis'
    },
    {
        'id': 6,
        'título': 'A Revolução dos Bichos',
        'autor': 'George Orwell'
    }
]


# Criar
@app.route('/livros',methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

# Consultar(todos)
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

# Consultar(id)
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
        
# Editar
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

# Excluir
@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)

app.run(port=5000,host='localhost',debug=True)