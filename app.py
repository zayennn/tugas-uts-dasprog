from flask import Flask, request, redirect, url_for,render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

# setup database
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "db_todo_list"

mysql = MySQL(app)

# khansa
@app.route('/')
def index() :
    return render_template('index.html')

# maya
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        status = request.form['status']

        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO tasks (name, status) VALUES (%s, %s)",
            (name, status)
        )
        mysql.connection.commit()
        cursor.close()

        return redirect(url_for('index'))

    return render_template('create.html')

# kemal
@app.route('/edit/<int:id>', methods=["GET", "POST"])
def edit(id):
    cur = mysql.connection.cursor()

    if request.method == "POST":
        nama = request.form['nama']
        status = request.form['status']
        cur.execute(
            "UPDATE tasks SET nama_task=%s WHERE id=%s",
            (nama, status, id)
        )
        mysql.connection.commit()
        return redirect(url_for('index'))

    cur.execute("SELECT * FROM tasks WHERE id=%s", (id,))
    task = cur.fetchone()
    return render_template('edit.html', task=task)

# ardel
@app.route('/delete/<int:id>', methods=["GET", "POST"])
def delete(id):
    pass
# jangantinggalinaku