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
@app.route('/create', methods=["GET", "POST"])
def create():
    return "ini halaman create"

# kemal
@app.route('/edit/<int:id>', methods=["GET", "POST"])
def edit(id):
    return "ini halaman edit"

# ardel
@app.route('/delete/<int:id>', methods=["GET", "POST"])
def delete(id):
    pass