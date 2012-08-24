#!/usr/bin/env python
# encoding=utf-8
# maintainer: Fad


import peewee

from datetime import datetime


DB_FILE = "zerin.db"
VERSION = "0.0.1b"
dbh = peewee.SqliteDatabase(DB_FILE)


class BaseModel(peewee.Model):

    class Meta:
        database = dbh

    @classmethod
    def all(cls):
        return list(cls.select())


class Owner(BaseModel):
    """
    """

    username = peewee.CharField(max_length=30, verbose_name="Nom d'utilisateur",
                                unique=True)
    password = peewee.CharField(max_length=150)
    password_zerin = peewee.IntegerField()

    def __unicode__(self):
        return u"%(name)s" % {"name": self.username}

    def full_mane(self):
        return u"%(name)s " % {"name": self.self.username}


class GroupContact(BaseModel):
    """ Groupe des clients"""
    name = peewee.CharField(max_length=30, verbose_name=u"Nom")

    def __unicode__(self):
        return u"%(name)s" % {"name": self.name}


class PhoneNumber(BaseModel):
    """ Numero des clients"""
    Number = peewee.IntegerField(verbose_name=u"Numero de téléphone")

    def __unicode__(self):
        return u"%(number)s" % {u"number": self.number}

    def full_name(self):
        return [contact for contact in Contact.filter(phone=self)]


class Contact(BaseModel):
    """ Contacte des clients
    """

    name = peewee.CharField(max_length=30, verbose_name=(u"Nom"), unique=True)
    phone = peewee.ForeignKeyField(PhoneNumber, verbose_name=u"Telephone")
    group = peewee.ForeignKeyField(GroupContact, verbose_name=u"Groupes")

    def __unicode__(self):
        return u"%(name)s" % {"name": self.name}

    def full_mane(self):
        return u"%(name)s %(group)s %(phone)s" % {"name": self.self.name,
                                                  "group": self.group,
                                                  "phone" : self.phone}


class Reports(BaseModel):
    """ """

    O = "o"
    M = "m"
    OPERATEUR = ((O, "Orange"), (M, "Malitel"))

    contact = peewee.ForeignKeyField(Contact)
    operateur = peewee.CharField(choices=OPERATEUR, default=O)
    clients = peewee.ForeignKeyField(Contact)
    amount = peewee.IntegerField(default=0)
    reporting_d = peewee.DateTimeField(default=datetime.now())

    def __unicode__(self):
        return (u"%(amount)s --> %(clients)s le %(operateur)s %(reporting_d)s") \
               % {'operateur': self.operateur, \
                  'reporting_d': self.reporting_d.strftime('%x %Hh:%Mmm'), \
                  'clients': self.clients, 'amount': self.amount}
