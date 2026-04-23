from flask import Flask, render_template
from model.produtos import select

app = Flask(__name__)

@app.route('/')
def pag_principal():
    itens = select(id=None) 
    return render_template('index.html', itens=itens)

@app.route('/pagina2/<int:id>')
def pag_2(id):
    item_especifico = select(id)
    return render_template('pagina2.html', item=item_especifico)

if __name__ == '__main__':
    app.run(debug=True)