
from flask import Flask, render_template, session, redirect, url_for, request
from model.produtos import select

app = Flask(__name__)
app.secret_key = 'chave_secreta_para_cookies' # Necessário para usar sessions

@app.route('/')
def pag_principal():
    itens = select(id=None) 
    # Inicializa o carrinho se ele não existir
    if 'carrinho' not in session:
        session['carrinho'] = []
    return render_template('index.html', itens=itens, carrinho=session['carrinho'])

@app.route('/adicionar/<int:id>')
def adicionar_ao_carrinho(id):
    item_especifico = select(id)
    
    if 'carrinho' not in session:
        session['carrinho'] = []
    
    # dicionario dos itens
    item_carrinho = {
        'id': item_especifico['codigo'],
        'nome': item_especifico['produto'],
        'preco': item_especifico['preco'],
        'foto': item_especifico['foto']
    }
    
    # adicionando
    carrinho_atual = session['carrinho']
    carrinho_atual.append(item_carrinho)
    session['carrinho'] = carrinho_atual
    
    return redirect(url_for('pag_principal', abrir_carrinho='true'))

@app.route('/carrinho')

# Rota para limpar o carrinho (opcional)
@app.route('/limpar')
def limpar_carrinho():
    session.pop('carrinho', None)
    return redirect(url_for('pag_principal'))

@app.route('/remover/<int:indice>')
def remover_item(indice):
    carrinho = session.get('carrinho', [])
    
    # Verifica se o índice existe na lista antes de tentar remover
    if 0 <= indice < len(carrinho):
        carrinho.pop(indice)  # Remove o item na posição específica
        session['carrinho'] = carrinho
        session.modified = True # Avisa o Flask que a sessão mudou
        
    return redirect(url_for('pag_principal', abrir_carrinho='true'))

@app.route('/pagina2/<int:id>')
def pag_2(id):
    item_especifico = select(id)
    return render_template('pagina2.html', item=item_especifico)



if __name__ == '__main__':
    app.run(debug=True)