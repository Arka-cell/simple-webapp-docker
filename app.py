import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def main():
    # Retrieve all environment variables as a dictionary
    env_vars = dict(os.environ)
    return jsonify(env_vars)

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001)
