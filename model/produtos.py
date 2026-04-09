
from database.conexao import Conexao

def select():
    conexao, cursor = Conexao.conectar()
    cursor.execute('select * from produtos')
    itens = cursor.fetchall()
    conexao.close()
    return itens

def ativoo(codigo, status):
        conexao,cursor= Conexao.conectar()
        status = int(status)
        status_atual = 0 if status == 1 else 1
        # if status_atual == 1:
        #     status = 0
        cursor.execute("update musica set ativo = %s where codigo = %s",(status_atual,codigo))
        conexao.commit()
        conexao.close()

        



def ativoo(codigo, status):
        conexao,cursor= Conexao.conectarconectar()
        status = int(status)
        status_atual = 0 if status == 1 else 1
        # if status_atual == 1:
        #     status = 0
        cursor.execute("update musica set ativo = %s where codigo = %s",(status_atual,codigo))
        conexao.commit()
        conexao.close()