from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "app_motos"
mysql = "MySQL(app)"
Usuario = []
Placa = []
Revisiones = []

@app.route('/')
def index():
    return render_template('index.html', Usuario = Usuario, Placa = Placa, Revisiones = Revisiones)

@app.route('/register')
def register():
    cursor= mysql.connection.cursor()
    cursor.execute("select * from register;")
    datos = cursor.fetchall()
    return render_template("registro.html", datos=datos)

@app.route('/guardar', methods=['POST'])
def guardar():
    usuario = request.form["usuario"]
    placa = request.form["placa"]
    revisiones = request.form["revisiones"]

    Usuario.append(usuario)
    Placa.append(placa)
    Revisiones.append(revisiones)

    return redirect("/")
@app.route("/login", methods=['POST'])
def login():
    us = request.form['usuario']
    pl = request.form['placa']

    if (us in Usuario):
        pos = Usuario.index(us)

        if(Placa[pos] == pl):
            return redirect("/inicio/" + str(pos))
        else:
            return render_template("index.html", error = "Error en el inicio de sesion")

@app.route("/inicio/<int:pos>")
def inicio(pos):
    return render_template("inicio.html", usuario = Usuario[pos], placa = Placa[pos], revisiones = Revisiones[pos])
if __name__=='__main__':
    app.run(port=3000, debug=True)