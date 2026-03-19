from flask import Flask, jsonify
from main import gen_build

app = Flask(__name__)

@app.route("/get_data")
def get_data():
    try:
        return jsonify(gen_build())
    except Exception as e:
        return jsonify({"error ": str(e)}), 500