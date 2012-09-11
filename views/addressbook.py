
from flask import render_template


def addressbook_main():

    users = {
        'fad': {'name': u"Ibrahima Fadiga", 'age': 2},
        'reg': {'name': u"Renaud Gaudin", 'age': 3},
    }
    return render_template('addressbook.html', users=users)