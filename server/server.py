#!/usr/bin/env python
# encoding: utf-8
import json
import random
import requests
from PIL import Image
from flask import Flask, request

WORKER_COUNT = 3
RETRIES = 10
worker_list = [i for i in range(WORKER_COUNT)]

app = Flask(__name__)
@app.route('/')
def index():
    return json.dumps({})

@app.route('/recognize', methods=['POST'])
def distribute_task():
    # distribute task to empty worker or reject it.
    for _retry in range(RETRIES):
        random.shuffle(worker_list)
        i = worker_list[0] + 1
        try:
            # Ensure the machine is available
            r = requests.get("http://worker-" + str(i) + ":3000/", timeout=1000)
            if r.status_code != 200:
                continue

            # Send the task
            print("Send request to ", "http://worker-" + str(i) + ":3000/recognize")
            r = requests.post("http://worker-" + str(i) + ":3000/recognize", files=request.files, timeout=10000)
            if r.status_code == 200:
                return r.json()
        except:
            continue
    return "Too many requests", 429
        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
