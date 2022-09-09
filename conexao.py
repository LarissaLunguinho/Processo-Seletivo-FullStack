import sqlite3 as lite

con = lite.connect('crud.db')

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE tarefa(id INTEGER PRIMARY KEY AUTOINCREMENT, titulo VARCHAR, descricao VARCHAR, ativo TINYINT, dt_alteracao TIMESTAMP(10), dt_cadastro TIMESTAMP(10))")