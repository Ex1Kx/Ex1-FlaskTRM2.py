from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQLdb
app = Flask(__name__)
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "app_motos"
mysql = "MySQL(app)"

@app.route("/")
def index():
    return render_template("index.html")

app.route("/register", methods=["get", "post"])
def register():
    cur =mysql.connection.cursor()
    cur.execute("select * from id_tip")
    tipo = cur.fetchall()

    cur = mysql.connection.cursor()
    cur.execute("select * from id_moto")
    moto = cur.fetchall()
    cur.close()

    if request.method == "GET":
        render_template("register.html", tipo = tipo, moto = moto)
else:

if __name__ == "__main__":
    app.run(debug=True)