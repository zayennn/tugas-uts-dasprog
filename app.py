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
def index():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    cursor.close()

    return render_template('index.html', tasks=tasks)

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
    if request.method == "POST":
        cur = mysql.connection.cursor()
        name = request.form['name']
        status = request.form['status']
        cur.execute(
            "UPDATE tasks SET name=%s, status=%s WHERE id=%s",
            (name, status, id)
        )
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tasks WHERE id=%s", (id,))
    task = cur.fetchone()
    cur.close()
    return render_template('edit.html', task=task)

# ardel
from flask import Flask, request, redirect, url_for, render_template
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
def index():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    cursor.close()

    return render_template('index.html', tasks=tasks)

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
    if request.method == "POST":
        cur = mysql.connection.cursor()
        name = request.form['name']
        status = request.form['status']
        cur.execute(
            "UPDATE tasks SET name=%s, status=%s WHERE id=%s",
            (name, status, id)
        )
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tasks WHERE id=%s", (id,))
    task = cur.fetchone()
    cur.close()
    return render_template('edit.html', task=task)

# ardel
@app.route('/delete/<int:id>', methods=["GET", "POST"])
def delete(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM tasks WHERE id=%s", (id,))
    mysql.connection.commit()
    cur.close()

    return redirect(url_for('index'))
