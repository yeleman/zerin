#!/usr/bin/env python
# encoding=utf-8
# Autor: Fadiga

from model import  PhoneNumber, GroupContact, Contact


def setup(drop_tables=False):
    """ create tables if not exist """

    did_create = False

    for model in [GroupContact, PhoneNumber, Contact]:
        if drop_tables:
            model.drop_table()
        if not model.table_exists():
            model.create_table()
            did_create = True
