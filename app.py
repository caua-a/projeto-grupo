from flask import Flask, render_template
from model.produtos import select

app = Flask(__name__)

@app.route('/')
def pag_principal():
    return render_template('index.html')

@app.route('/pagina2')
def pag_2():
    itens = select()
    return render_template('pagina2.html', itens=itens)





if __name__ == '__main__':
    app.run(debug=True)
