#!/usr/bin/env python

import sys

from flask import Flask

app = Flask('zerin_server')

from views.addressbook import addressbook_main, addressbook_grouplist, addressbook_contactlist
from views.transfer import transfer_main, transfer_test, transfer_info

app.route('/addressbook')(addressbook_main)
app.route('/addressbook/group_list')(addressbook_grouplist)
app.route('/addressbook/contact_for/<group_id>')(addressbook_contactlist)
app.route('/')(transfer_main)
app.route('/test')(transfer_test)
app.route('/info', methods=['POST'])(transfer_info)


if __name__ == '__main__':
    try:
        http_port = int(sys.argv[1])
    except:
        http_port = 5000
    app.run(debug=True, port=http_port)