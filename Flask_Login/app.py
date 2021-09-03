from flask import Flask, render_template, request, redirect

app = Flask(__name__)

lUsuario = []
lPlaca = []
lRevisiones = []

@app.route('/')
def index():
    return render_template("index.html", lUs = lUsuario, lPl = lPlaca, lRe = lRevisiones)

@app.route('/registro')
def registro():
    return render_template("registro.html")

@app.route("/guardar", methods=['post'])
def guardar():
    usuario = request.form["usuario"]
    placa = request.form["placa"]
    revisiones = request.form ["revisiones"]

    lUsuario.append(usuario)

    return redirect("/")

@app.route("/login", methods=['post'])
def login():
    us = request.form['Usuario']
    lPlaca.append(placa)
    lRevisiones.append(revisiones)
    pl = request.form['Placa']

    if (us in lUsuario):
        pos = lUsuario.index(us)
        if(lPlaca[pos] == pl):
            return redirect("/inicio/" + str(pos))

@app.route("/inicio/<int:pos>")
def inicio(pos):
    render_template("inicio.html", usuario = lUsuario[pos], placa = lPlaca[pos])

if __name__ == '__main__':
    app.run(port=3000, debug=True)