import sqlite3

def conectar_banco():
    return sqlite3.connect('banco.db')

def criar_tabela():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS chamados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT NOT NULL,
            categoria TEXT NOT NULL,
            status TEXT NOT NULL
        )
    ''')
    conexao.commit()
    conexao.close()

def inserir_chamado(nome, descricao, categoria, status):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO chamados (nome, descricao, categoria, status)
        VALUES (?, ?, ?, ?)
    ''', (nome, descricao, categoria, status))
    id_chamado = cursor.lastrowid

    conexao.commit()
    conexao.close()

    return id_chamado

def listar_chamados():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM chamados')
    chamados = cursor.fetchall()
    conexao.close()
    return chamados

def buscar_chamado_por_id(id_chamado):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM chamados WHERE id = ?', (id_chamado,))
    chamado = cursor.fetchone()
    conexao.close()
    return chamado

def alterar_status(id_chamado, novo_status):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('UPDATE chamados SET status = ? WHERE id = ?', (novo_status, id_chamado))
    conexao.commit()
    conexao.close()

def deletar_chamado(id_chamado):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM chamados WHERE id = ?', (id_chamado,))
    conexao.commit()
    conexao.close()

criar_tabela()