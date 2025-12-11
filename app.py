from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# setup database
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "db_todo_list"

mysql = MySQL(app)

@app.route('/')
def index() :
    return "salaam'aleykum dunyaa!"

if __name__ == "__main__" :
    app.run(debug=True)