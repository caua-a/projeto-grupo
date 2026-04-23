
from database.conexao import Conexao

def select(id=None):
    conexao, cursor = Conexao.conectar()
    
    if id:
        cursor.execute("SELECT codigo, produto, descricao, preco, destaque, foto FROM produtos WHERE codigo = %s", (id,))
        item = cursor.fetchone()
        conexao.close()
        return item
    else:
        cursor.execute('SELECT codigo, produto, descricao, preco, destaque, foto FROM produtos WHERE disponibilidade = 1')
        itens = cursor.fetchall()
        conexao.close()
        return itens