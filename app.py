from flask import Flask, render_template
from model.produtos import select

app = Flask(__name__)

@app.route('/')
def pag_principal():
    itens = select()
    return render_template('index.html', itens=itens)

@app.route('/pagina2/<id>')
def pag_2():
    itens = select(id)
    return render_template('pagina2.html', itens=itens)





if __name__ == '__main__':
    app.run(debug=True)
