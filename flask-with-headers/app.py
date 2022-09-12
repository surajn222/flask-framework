from flask import Flask, render_template, request, jsonify
from requests import get
import os
import json

app = Flask(__name__, template_folder='templates')

@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>')
def hello_world(u_path):
    print(request.headers)
    dict_request_headers = request.headers
    print(json.dumps(dict_request_headers, indent=2, default=str))
    return jsonify(**dict_request_headers)

    #return json.dumps(dict_request_headers, indent=2, default=str)
    #return get(f'http://www.google.com').content
    #return 'Test'

@app.route('/list/')
def list_api_key():
    print(request.headers)
    dict_request_headers = request.headers
    print(json.dumps(dict_request_headers, indent=2, default=str))
    return jsonify(**dict_request_headers)


@app.route('/')
def hello():
    return redirect(url_for('foo'))

if __name__ == '__main__':
  app.run(debug=True)