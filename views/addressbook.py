# encoding=utf8

import json

from flask import render_template

from models import Group, ContactGroup, PhoneNumber, Contact, Transfer

ALL_CONTACTS = -1

SUCCESS = u'success'
INFO = u'info'
WARNING = u'warning'
ERROR = u'error'

def dict_return(data, level, message, message_html=None):
    data.update({'return': level,
                 'return_text': message})
    if message_html:
        data.update({'return_html': message_html})


def addressbook_main():
    return render_template('addressbook.html')


def addressbook_grouplist():
    data = {'groups': [group.to_dict()
                       for group in Group.filter().order_by("name")]}
    return json.dumps(data)


def addressbook_contact(contact_id):
    data = {'contact': Contact.get(id=int(contact_id)).to_dict(True)}
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


def addressbook_transfer(contact_id):
    numbers = PhoneNumber.filter(contact=Contact.get(id=int(contact_id)))
    data = {'transfers': [tr.to_dict() for tr in Transfer.filter(number__in=numbers)]}
    return json.dumps(data)
 

def addressbook_add_contact_to_group(group_id, contact_id):
    contact = Contact.get(id=int(contact_id))
    group = Group.get(id=int(group_id))

    data = {'contact': contact.to_dict(),
            'group': group.to_dict()}

    subst = {'contact': contact.display_name(),
             'group': group.display_name()}

    if ContactGroup.filter(contact=contact, group=group).count():
        dict_return(data, INFO, 
                    u"%(contact)s fait déjà parti du groupe %(group)s." % subst,
                    message_html=u"<strong>%(contact)s</strong> fait déjà "
                                 u"parti du groupe "
                                 u"<strong>%(group)s</strong>." % subst)
    else:
        cg = ContactGroup(contact=contact, group=group)
        try:
            cg.save()
            dict_return(data, SUCCESS, 
                        u"%(contact)s a été ajouté au groupe %(group)s." % subst,
                        message_html=u"<strong>%(contact)s</strong> a été "
                                     u"ajouté au groupe "
                                     u"<strong>%(group)s</strong>." % subst)
        except Exception as e:
            subst.update({'err': e.message})
            dict_return(data, ERROR, 
                    u"Impossible d'ajouter %(contact)s au groupe "
                    u"%(group)s: %(err)r" % subst,
                    message_html=u"Impossible d'ajouter <strong>%(contact)s</strong> au "
                                 u"groupe <strong>%(group)s</strong>:<br />"
                                 u"<em>%(err)r</em>" % subst)

    return json.dumps(data)    
