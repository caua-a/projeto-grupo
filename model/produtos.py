import mysql.connector
from database.conexao import Conexao

def select():
    conexao, cursor = Conexao.conectar()
    cursor.execute('select * from produtos')
    itens = cursor.fetchall()
    conexao.close()
    return itens
