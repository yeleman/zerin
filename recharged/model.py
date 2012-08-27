#!/usr/bin/env python
# encoding=utf-8
# maintainer: Fad


import peewee

DB_FILE = "zerin.db"
dbh = peewee.SqliteDatabase(DB_FILE)


class BaseModel(peewee.Model):

    class Meta:
        database = dbh

    @classmethod
    def all(cls):
        return list(cls.select())


class GroupContact(BaseModel):
    """ Groupe des clients"""

    name = peewee.CharField(max_length=30, verbose_name=u"Nom")

    def __unicode__(self):
        return u"%(name)s" % {"name": self.name}


class PhoneNumber(BaseModel):
    """ Numero des clients """

    number = peewee.IntegerField(verbose_name=u"Numero de téléphone")

    def __unicode__(self):
        return u"%(number)s" % {u"number": self.number}


class Contact(BaseModel):
    """ Contacte des clients """

    name = peewee.CharField(max_length=30, verbose_name=(u"Nom"), unique=True)
    phone = peewee.ForeignKeyField(PhoneNumber, verbose_name=u"Telephone")
    group = peewee.ForeignKeyField(GroupContact, verbose_name=u"Groupes")

    def __unicode__(self):
        return u"%(name)s" % {"name": self.name}
