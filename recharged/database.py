#!/usr/bin/env python
# encoding=utf-8
# Autor: Fadiga

from model import (Owner, PhoneNumber, GroupContact, Contact, Reports)


def setup(drop_tables=False):
    """ create tables if not exist """

    did_create = False

    for model in [GroupContact, PhoneNumber, Owner, Contact, Reports]:
        if drop_tables:
            model.drop_table()
        if not model.table_exists():
            model.create_table()
            did_create = True
