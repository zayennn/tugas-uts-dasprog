from flask import Flask, request, render_template, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "db_todo_list"

mysql = MySQL(app)

@app.route('/')
def index():
    return "Halaman Index"

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        status = request.form['status']

        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO todo (name, status) VALUES (%s, %s)",
            (name, status)
        )
        mysql.connection.commit()
        cursor.close()

        return redirect(url_for('create'))

    return render_template('create.html')

if __name__ == "__main__":
    app.run(debug=True)

