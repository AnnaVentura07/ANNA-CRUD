import sqlite3

def init_db():
    conn = sqlite3.connect('inventario_jogos.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jogos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            plataforma TEXT NOT NULL,
            ano_lancamento INTEGER
        )
    ''')
    conn.commit()
    conn.close()
    print("Banco 'inventario_jogos.db' inicializado com sucesso!")

if __name__ == '__main__':
    init_db()