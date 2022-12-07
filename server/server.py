#!/usr/bin/env python
# encoding: utf-8
import json
import requests
from flask import Flask, request

WORKER_COUNT = 3

app = Flask(__name__)
@app.route('/')
def index():
    return json.dumps({})

@app.route('/recognize', methods=['POST'])
def distribute_task():
    # distribute task to empty worker or reject it.
    for i in range(WORKER_COUNT):
        try:
            r = requests.post("http://worker-" + i + ":5000/recognize", files=request.files, timeout=10000)
            if r.status_code == 200:
                return r.json()
        except:
            continue
    return "Too many requests", 429
        

if __name__ == '__main__':
    app.run()
