from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL,MySQLdb
import pandas as pd
import xlrd

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'facturacion'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/logout', methods=["GET", "POST"])
def logout():
    session.clear()
    return render_template("home.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        name = request.form['name']
        base = request.form['base']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO cajero (name, base) VALUES (%s,%s)",(name,base))
        mysql.connection.commit()
        session['name'] = request.form['name']
        session['base'] = request.form['base']
        return redirect(url_for('home'))


@app.route('/billing', methods=["GET", "POST"])
def billing():
    if request.method == 'GET':
        return render_template("billing.html")
    else:
        codigo = request.form['codigo']
        cantidad = request.form['cantidad']
        pago = request.form ['pago']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO facturas (codigo, cantidad, pago) VALUES (%s,%s,%s)",(codigo,cantidad, pago))
        mysql.connection.commit()
        return redirect(url_for('home'))

filePath = "excel/productos.xlsx"
openFile = xlrd.open_workbook(filePath)
sheet = openFile.sheet_by_name("Hoja1")
print("Filas", sheet.nrows)
if __name__ == '__main__':
    app.secret_key = "op)nl7$z#-&#nde5#$&-^r%(ip1wi#a50c5=y-adofq#(7z!2v"
    app.run(port=4000, debug=True)