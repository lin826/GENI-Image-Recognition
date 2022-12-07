#!/usr/bin/env python
# encoding: utf-8
import os
import json
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/')
def index():
    return json.dumps({})

@app.route('/recognize', methods=['POST'])
def distribute_task():
    # TODO: distribute task to empty worker or reject it.
    return requests.post("worke-1:5000/recognize", files=request.files, timeout=10000)

if __name__ == '__main__':
    app.run()
