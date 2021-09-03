from flask import Flask, render_template, request

app = Flask(__name__)

listaPropietario = []
listaMascotas = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/guardar", methods=["POST"])
def guardar():

    nPropietario = request.form["nombre"]
    nMascota = request.form["mascota"]
    listaPropietario.append(nPropietario)
    listaMascotas.append(nMascota)
    return render_template('index.html',listaM = listaMascotas, listaP = listaPropietario)

@app.route("/buscar", methods=["POST"])
def buscar():
    nPropietario = request.form["bPropietario"]


    if(nPropietario in listaPropietario):
        pos = listaPropietario.index(nPropietario)
        
        return render_template("index.html", vPro = listaPropietario[pos], vMasco = listaMascotas[pos])
    else:
        return render_template("index.html")



if  __name__=='__main__':
    app.run(port=10000, debug=True)