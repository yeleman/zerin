#!/usr/bin/env python
# encoding=utf-8
# Autor: Fadiga

from model import  (ContactGroup, Operator, PhoneNumber, Contact, Transfer,
                    Settings)


def setup(drop_tables=False):
    """ create tables if not exist """

    did_create = False

    for model in [ContactGroup, Operator, PhoneNumber, Contact, Transfer,
                    Settings]:
        if drop_tables:
            model.drop_table()
        if not model.table_exists():
            model.create_table()
            did_create = True
