#!/usr/bin/env python

import json

from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def index():
    return open('test.html', 'r').read()


@app.route('/test')
def test():
    data = {'sent': [
        {'number': '73 12 08 96', 'name': 'reg', 'status': 'sent'},
        {'number': '65 73 10 76', 'name': 'fad', 'status': 'delivered'},
        {'number': '65 73 10 76', 'name': 'Alou DOlo', 'status': 'delivered'},
    ]}
    return json.dumps(data)

@app.route('/info', methods=['POST'])
def info(*args, **kwargs):
    from pprint import pprint as pp ; pp(request.form)
    

    name = request.form.get('name')
    id_ = request.form.get('id')

    users = {
        'fad': {'name': u"Ibrahima Fadiga", 'age': 2},
        'reg': {'name': u"Renaud Gaudin", 'age': 3},
    }
    return json.dumps(users.get(name))


if __name__ == '__main__':
    app.run(debug=True)