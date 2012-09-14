#!/usr/bin/env python

import sys

from flask import Flask

app = Flask('zerin_server')

from views.addressbook import (addressbook_main, addressbook_grouplist,
                               addressbook_contactlist, addressbook_contact,
                               addressbook_transfer,
                               addressbook_add_contact_to_group,
                               addressbook_add_group,
                               addressbook_delete_group)
from views.transfer import transfer_main, transfer_test, transfer_info

app.route('/addressbook')(addressbook_main)
app.route('/addressbook/group_list')(addressbook_grouplist)
app.route('/addressbook/contact/<contact_id>')(addressbook_contact)
app.route('/addressbook/contact_for/<group_id>')(addressbook_contactlist)
app.route('/addressbook/transfer_for/<contact_id>')(addressbook_transfer)
app.route('/addressbook/add_contact/<contact_id>/to_group/<group_id>')(
                                              addressbook_add_contact_to_group)
app.route('/addressbook/add_group', methods=['POST'])(addressbook_add_group)
app.route('/addressbook/delete_group/<group_id>')(addressbook_delete_group)
app.route('/')(transfer_main)
app.route('/test')(transfer_test)
app.route('/info', methods=['POST'])(transfer_info)


if __name__ == '__main__':
    try:
        http_port = int(sys.argv[1])
    except:
        http_port = 5000
    app.run(debug=True, port=http_port)
