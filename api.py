from flask import Flask
from main import gen_build

app = Flask(__name__)

@app.route("/get_data")
def get_data():
    return gen_build()