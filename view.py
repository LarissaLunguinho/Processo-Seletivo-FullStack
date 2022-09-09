import sqlite3 as lite

con = lite.connect('crud.db')

def inserir_info(i):
    with con:
        cur = con.cursor()
        query ="INSERT INTO tarefa (titulo, descricao, ativo, dt_cadastro, dt_alteracao) VALUES (?, ?, ?, ?, ?)"
        cur.execute(query, i)

def mostrar_info():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM tarefa"
        cur.execute(query)
        informacao = cur.fetchall()
        
        for i in informacao:
            lista.append(i)
    return lista

def atualizar_info(i):  
    with con:
        cur = con.cursor()
        query = "UPDATE tarefa SET titulo=?, descricao=?, ativo=?, dt_cadastro=?, dt_alteracao=? WHERE id=?"
        cur.execute(query,i)

def deletar_info(i):    
    with con:
        cur = con.cursor()
        query="DELETE FROM tarefa WHERE id=?"
        cur.execute(query,i)