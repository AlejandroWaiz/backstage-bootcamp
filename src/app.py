import socket
from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route('/api/v1/details')
def details():
    actualTime = datetime.datetime.now()
    hostname = socket.gethostname()
    return jsonify({"Message": "Hello", "Time": actualTime, "Host": hostname})

@app.route('/api/v1/healthz')
def health():
    return jsonify({"Status": "ok"}), 200

if __name__ == '__main__':

    app.run(host="0.0.0.0")