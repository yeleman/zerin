
import json

from flask import render_template, request


def transfer_main():
    dic = {}
    return render_template('test.html', dic=dic)


def transfer_test():
    data = {'sent': [
        {'number': '73 12 08 96', 'name': 'reg', 'status': 'sent'},
        {'number': '65 73 10 76', 'name': 'fad', 'status': 'delivered'},
        {'number': '65 73 10 76', 'name': 'Alou DOlo', 'status': 'delivered'},
    ]}
    return json.dumps(data)


def transfer_info(*args, **kwargs):
    from pprint import pprint as pp ; pp(request.form)

    name = request.form.get('name')
    id_ = request.form.get('id')

    users = {
        'fad': {'name': u"Ibrahima Fadiga", 'age': 2},
        'reg': {'name': u"Renaud Gaudin", 'age': 3},
    }
    return json.dumps(users.get(name))