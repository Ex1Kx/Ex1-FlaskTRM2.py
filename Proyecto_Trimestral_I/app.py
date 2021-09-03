from flask import Flask, render_template, request, redirect, url_for, flash, session, escape
import pandas as pd
from flask_mysqldb import MySQL,MySQLdb

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'inventorysystemdb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

app = Flask(__name__)


@app.route('/')
def login():
    return render_template("index.html")


@app.route('/home', methods=['POST'])
def home():
    return render_template('index.html')


@app.route('/log', methods=['POST'])
def log():

        try:
            username_form = request.form['username']
            password_form = request.form['password']
            if username_form == "" and password_form == "":
                flash('Porfavor llena todos los campos')
            else:

                if request.method == 'POST':
                        mydb = mysql.connect(user='root', password='root', host='localhost', database='inventorysystemdb')
                        mycursor = mydb.cursor()

                        if 'username' in session:
                            return redirect(url_for('index'))
                        if request.method == 'POST':
                            mycursor.execute("SELECT COUNT(1) FROM logincredentials WHERE UserName = %s;", [username_form])
                            if mycursor.fetchone()[0]:
                                mycursor.execute("SELECT Password FROM logincredentials WHERE Password = %s;", [password_form])
                                for row in mycursor.fetchall():
                                    if password_form == row[0]:
                                        session['username'] = request.form['username']
                                        mydb.commit()
                                        mycursor.close()
                                        flash('Logeo exitoso')
                                        return render_template('index.html')
                                    else:
                                        flash('El usuario o contraseña son incorrectos')
                                        return redirect(url_for('login'))
                                else:
                                    flash('El usuario o contraseña son incorrectos')
                                    return redirect(url_for('login'))
                            else:
                                flash('El usuario o contraseña son incorrectos')
                                return redirect(url_for('login'))
        except Exception as e:
                    print(e)
                    return render_template('login.html')


@app.route('/logout', methods=['GET'])
def logout():
    if request.method == 'GET':
        session.clear()
        return render_template('login.html')


@app.route('/insert', methods=['POST'])
def insert():

        try:
            prodname = request.form['addname']
            prodprice = request.form['addprice']
            prodquant = request.form['addquantity']

            if prodname == "":
                return render_template('index.html')
            elif prodprice == "":
                return render_template('index.html')
            elif prodquant == "":
                return render_template('index.html')
            else:

               if request.method == 'POST':
                    mydb = mysql.connect(user='root', password='root', host='localhost', database="inventorysystemdb")
                    mycursor = mydb.cursor()
                    if request.method == 'POST':
                         mycursor.execute("SELECT COUNT(1) FROM billInventory WHERE product_name = %s;", [prodname])
                         if mycursor.fetchone()[0]:
                            flash(prodname + ' ya esta en la lista')
                            return render_template('index.html')
                         else:
                            mycursor.execute("INSERT INTO billInventory(product_name, price ,quantity) Values(%s,%s,%s)", (prodname, prodprice, prodquant))
                            mydb.commit()
                            mycursor.close()
                            mydb.close()
                            flash(prodname + ', ' + prodprice + ', ' + prodquant + ', Se ha guardado satisfactoriamente!')
                            return render_template('index.html')
                    else:
                        return render_template('index.html')
        except Exception as e:
            flash(e)
            return render_template('index.html')


@app.route('/searchall', methods=['POST'])
def searchall():
    try:
        if request.method == 'POST':
            mydb = mysql.connect(user='root', password='root', host='localhost', database='inventorysystemdb')
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM billInventory")
            #cambiar linea anterior por si acaso
            data = mycursor.fetchall()
            return render_template('index.html', products=data)
    except Exception as e:
        flash(e)
        return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():

    try:
        prodname = request.form['searchprod']
        if prodname == "":
            flash('Porfavor llena el campo de busqueda ')
            return render_template('index.html')
        else:
            if request.method == 'POST':
                mydb = mysql.connect(user='root', password='root', host='localhost', database='inventorysystemdb')
                mycursor = mydb.cursor()
                if request.method == 'POST':
                    mycursor.execute("SELECT COUNT(1) FROM billInventory WHERE product_name = %s;", [prodname])
                    #1
                    if mycursor.fetchone()[0]:
                        mycursor.execute("SELECT * FROM billInventory WHERE product_name = %s;", [prodname])
                        #2
                        prod = mycursor.fetchall()
                        flash(prodname + ' Encontrado!')
                        return render_template('index.html', prodnames=prod)
                    else:
                        flash('No hay productos como ese.. ' + prodname)
                    return render_template('index.html')
                else:
                    flash('No hay productos como ese.. ' + prodname)
                    return render_template('index.html')
            else:
                return render_template('index.html')

    except Exception as e:
        flash(e)
        return render_template('index.html')


@app.route('/delete', methods=['POST'])
def delete():
    try:
        namee = request.form['prodsname']
        if namee == "":
            return render_template('index.html')
        else:
            if request.method == 'POST':
                mydb = mysql.connect(user='root', password='root', host='localhost', database='inventorysystemdb')
                mycursor = mydb.cursor()
                if request.method == 'POST':
                    mycursor.execute("SELECT COUNT(1) FROM billInventory WHERE product_name = %s;", [namee])
                    #3
                    if mycursor.fetchone()[0]:
                        mycursor.execute("DELETE FROM billInventory WHERE product_name = %s;", [namee])
                        #4
                        mydb.commit()
                        mycursor.close()
                        mydb.close()
                        flash('Borrado satisfactoriamente!')
                        return render_template('index.html')
                    else:
                        flash('El producto ' + request.form['prodsname'] + ' no esta en la lista')
        return render_template('index.html')
    except Exception as e:
        flash(e)
        return render_template('index.html')


@app.route('/update', methods=['POST'])
def update():
    try:
       name_prod = request.form['namess']
       price = request.form['pricee']
       quantt= request.form['quantityy']
       if name_prod == "":
            return render_template('index.html')
       elif price == "":
            return render_template('index.html')
       elif quantt == "":
            return render_template('index.html')
       else:
           if request.method == 'POST':
               mydb = mysql.connect(user='root', password='root', host='localhost', database='inventorysystemdb')
               mycursor = mydb.cursor()
               if request.method == 'POST':
                   mycursor.execute("SELECT COUNT(1) FROM billInventory WHERE product_name = %s;", [name_prod])
                   if mycursor.fetchone()[0]:
                       mycursor.execute("SELECT * FROM billInventory WHERE product_name = %s;", [name_prod])
                       produ = mycursor.fetchall()
                       flash(name_prod + ' Encontrado!')
                       for row in produ:
                           b = row[3]
                           if int(b)+int(quantt) < 0:
                               flash('Cantidad insuficiente')
                               return render_template('index.html')
                           else:
                               sum = int(b) + int(quantt)
                               mycursor.execute("UPDATE billInventory SET price='" + price + "' , quantity='" + str(sum) + "' WHERE product_name='" + name_prod + "'")
                               mydb.commit()
                               mycursor.close()
                               mydb.close()
                               flash('Actualizado satisfactoriamente')
                               return render_template('index.html')
                   else:
                        flash('No hay un producto como ese... ' + name_prod)
                   return render_template('index.html')
    except Exception as e:
        flash(e)
        return render_template('index.html')

app.secret_key = "zs40)58t5x3(0huyx(@2=u$@s!!l^6pb%hp29rpo_2n5%&s+kay"
if __name__ == "__main__":
    app.run(port=460, debug=True)

