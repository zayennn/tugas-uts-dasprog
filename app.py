from flask import Flask

app = Flask(__name__)

@app.route('/')
def index() :
    return "salaam'aleykum dunyaa!"

if __name__ == "__main__" :
    app.run(debug=True)