from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def executar_query(query, params=(), fetchone=False, fetchall=False, commit=False):
    conn = sqlite3.connect('inventario_jogos.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    resultado = None
    
    try:
        cursor.execute(query, params)
        if commit:
            conn.commit()
        if fetchone:
            resultado = cursor.fetchone()
        elif fetchall:
            resultado = cursor.fetchall()
    finally:
        conn.close()
    return resultado

def criar_tabela():
    # Adicionado campo preco REAL aqui
    executar_query('''
        CREATE TABLE IF NOT EXISTS jogos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            plataforma TEXT NOT NULL,
            ano_lancamento INTEGER,
            preco REAL
        )
    ''', commit=True)

@app.route('/jogos', methods=['GET'])
@app.route('/jogos/<int:id>', methods=['GET'])
def gerenciar_jogos(id=None):
    if id:
        jogo = executar_query("SELECT * FROM jogos WHERE id = ?", (id,), fetchone=True)
        if jogo:
            return jsonify(dict(jogo)), 200
        return jsonify({"erro": "Jogo não encontrado"}), 404

    dados = executar_query("SELECT * FROM jogos", fetchall=True)
    return jsonify([dict(item) for item in dados]), 200

@app.route('/jogos', methods=['POST'])
def criar_jogo():
    dados = request.get_json()
    titulo = dados.get('titulo')
    plataforma = dados.get('plataforma')
    ano = dados.get('ano_lancamento')
    preco = dados.get('preco') # Novo campo capturado

    if not titulo or not plataforma:
        return jsonify({"erro": "Título e Plataforma são obrigatórios"}), 400

    # Adicionado preco no INSERT
    executar_query(
        "INSERT INTO jogos (titulo, plataforma, ano_lancamento, preco) VALUES (?, ?, ?, ?)",
        (titulo, plataforma, ano, preco),
        commit=True
    )
    return jsonify({"mensagem": "Jogo registrado com sucesso!"}), 201

@app.route('/jogos/<int:id>', methods=['PUT'])
def atualizar_jogo(id):
    dados = request.get_json()
    
    existe = executar_query("SELECT id FROM jogos WHERE id = ?", (id,), fetchone=True)
    if not existe:
        return jsonify({"erro": "Jogo não encontrado"}), 404


    executar_query(
        "UPDATE jogos SET titulo = ?, plataforma = ?, ano_lancamento = ?, preco = ? WHERE id = ?",
        (dados.get('titulo'), dados.get('plataforma'), dados.get('ano_lancamento'), dados.get('preco'), id),
        commit=True
    )
    return '', 204

@app.route('/jogos/<int:id>', methods=['DELETE'])
def deletar_jogo(id):
    jogo = executar_query("SELECT id FROM jogos WHERE id = ?", (id,), fetchone=True)
    
    if not jogo:
        return jsonify({"erro": "Jogo não encontrado"}), 404

    executar_query("DELETE FROM jogos WHERE id = ?", (id,), commit=True)
    return jsonify({"mensagem": "Jogo removido do inventário!"}), 200

if __name__ == '__main__':
    criar_tabela()
    app.run(debug=True)
