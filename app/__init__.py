# -*- coding: utf-8 -*-
"""
@author: italo.lins
"""

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "ok",
        "mensagem": "Backend Flask running"
    })

@app.route('/hello')
def hello():
    return "Hello, world!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
