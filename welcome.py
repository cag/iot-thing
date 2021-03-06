# Copyright 2015 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from flask import Flask, jsonify, request

app = Flask(__name__)
latest_data = {}

@app.route('/')
def home():
    return app.send_static_file('index.html')

FIELDS = ["temp", "humidity", "accelX", "accelY", "accelZ", "magnX", "magnY", "magnZ",]
@app.route('/send-data')
def receive_data():
    for f in FIELDS:
        if f in request.args:
            latest_data[f] = request.args[f]
    # return jsonify(response)
    return ('', 204)

@app.route('/data')
def fdsafdsa():
    return jsonify(latest_data)

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))
