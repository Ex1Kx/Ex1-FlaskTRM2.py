from flask import Flask, render_template, request

app = Flask(__name__)

lUsuario = []
lPlaca = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/guardar", methods=["POST"])
def guardar():

    nUsuario = request.form["usuario"]
    nPlaca = request.form["placa"]
    lUsuario.append(nUsuario)
    lPlaca.append(nPlaca)
    return render_template('index.html',listaP = lPlaca, listaU = lUsuario)

@app.route("/buscar", methods=["POST"])
def buscar():
    nUsuario = request.form["bUsuario"]


    if(nUsuario in lUsuario):
        pos = lUsuario.index(nUsuario)
        
        return render_template("index.html", vUs = lUsuario[pos], vPl = lPlaca[pos])
    else:
        return render_template("index.html")



if  __name__=='__main__':
    app.run(port=10000, debug=True)