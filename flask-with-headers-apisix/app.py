from flask import Flask, render_template, request, jsonify
from requests import get
import os
import json
from argparse import ArgumentParser
from etcd_client import *
app = Flask(__name__, template_folder='templates')

@app.route('/keys/insert/', methods = ["POST"])
def list_api_key():
    dict_request_headers = request.get_data()
    print(type((dict_request_headers)))
    raw_data = dict_request_headers.decode("utf-8")
    json_raw_data = json.loads(raw_data)
    access_key = json_raw_data["access_key"]
    backend_url = json_raw_data["backend_url"]
    # Call etcd
    client = connect(app.config['etcd_host'], app.config['etcd_port'])
    success = insert_keys(client, access_key, backend_url)
    # print(json.dumps(dict_request_headers, indent=2, default=str))
    return str([access_key, backend_url]) + ": " + str(success)

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--etcd_host', '-etcd_host')
    parser.add_argument('--etcd_port', '-etcd_port')
    parser.add_argument('--host', '-host')
    args = parser.parse_args()
    etcd_host = args.etcd_host
    etcd_port = args.etcd_port
    host = args.host
    app.config['etcd_host'] = etcd_host
    app.config['etcd_port'] = etcd_port
    app.run(debug=True, host='0.0.0.0')