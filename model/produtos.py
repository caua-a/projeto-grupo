
from database.conexao import Conexao

def select(id = False):
        conexao, cursor = Conexao.conectar()
        if id:
                cursor.execute("SELECT codigo, produto, descricao, preco, destaque, foto from produtos where disponibilidade = 1")
        else:
                cursor.execute("SELECT codigo, produto, descricao, preco, destaque, foto, disponibilidade from produtos;")
                
        itens = cursor.fetchall()
        conexao.close()
        return itens
