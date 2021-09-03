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

app.route("/registro", methods = ['get', 'post'] )
def registro():

    cur =mysql.connection.cursor()
    cur.execute("SELECT * FROM user")
    placa = cur.fetchall()

    cur.close()
    if request.method == 'get':
        return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)