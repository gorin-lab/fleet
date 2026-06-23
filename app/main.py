import json
from flask import Flask, render_template, request, jsonify
import logging
import os


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return jsonify({'result':'OK'}), 200

@app.route('/health', methods=['GET'])
def health():
    return "Hello, world!"


if __name__ == '__main__':  

    app.run(host='0.0.0.0', port=8080, threaded=True)

