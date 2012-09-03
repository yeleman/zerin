#!/usr/bin/env python
# encoding=utf-8
# Autor: Fadiga

from models import  (Group, Operator, PhoneNumber, Contact, ContactGroup, Transfer,
                    Settings)


def setup(drop_tables=False):
    """ create tables if not exist """

    did_create = False

    for models in [Group, Operator, Contact, PhoneNumber, ContactGroup, Transfer,
                    Settings]:
        if drop_tables:
            models.drop_table()
        if not models.table_exists():
            models.create_table()
            did_create = True
