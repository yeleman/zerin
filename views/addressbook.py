
import json

from flask import render_template

from models import Group, ContactGroup

ALL_CONTACTS = -1


def addressbook_main():
    return render_template('addressbook.html')


def addressbook_grouplist():
    data = {'groups': [group.to_dict() 
                       for group in Group.filter().order_by("name")]}
    return json.dumps(data)


def addressbook_contactlist(group_id):
    try:
        group_id = int(group_id)
    except:
        group_id = ALL_CONTACTS

    if group_id == ALL_CONTACTS:
        qs = ContactGroup.filter().group_by('contact')
        group_dict = {'id': -1, 'name': u"Tous"}
    else:
        qs = ContactGroup.filter(group__id=group_id)
        group_dict = Group.get(id=group_id).to_dict()
    data = {'contacts': [contact_group.contact.to_dict() 
                         for contact_group in qs],
            'group': group_dict}
    return json.dumps(data)
