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


class Group(BaseModel):
    """ Group of contacts """

    name = peewee.CharField(max_length=30, verbose_name=u"Nom")

    def __unicode__(self):
        return u"%(name)s" % {"name": self.name}


class Operator(BaseModel):
    """ Operators """

    slug = peewee.CharField(max_length=30, verbose_name=u"Code")
    name = peewee.CharField(max_length=30, verbose_name=u"Nom")

    def __unicode__(self):
        return u"%(name)s" % {"name": self.name}


class PhoneNumber(BaseModel):
    """ Contact number """

    number = peewee.IntegerField(verbose_name=u"Numero de téléphone")
    operator = peewee.ForeignKeyField(Operator, verbose_name=u"Opérateur",
                                      related_name='operators')

    def __unicode__(self):
        return u"%(number)s" % {u"number": self.number}


class Contact(BaseModel):
    """ Contact address book """

    name = peewee.CharField(max_length=100, verbose_name=(u"Nom"), unique=True)
    number = peewee.ForeignKeyField(PhoneNumber, verbose_name=u"Téléphone",
                                   related_name='numbers')

    def __unicode__(self):
        return u"%(name)s" % {"name": self.name}


class ContactGroup(BaseModel):
    """ Contact with group """

    contact = peewee.ForeignKeyField(Contact, verbose_name=u"Contact",
                                   related_name='contacts')
    group = peewee.ForeignKeyField(Group, verbose_name=u"Groupe",
                                   related_name='groups')


class Transfer(BaseModel):
    """ Ensemble des  transferts effectués """

    amount = peewee.IntegerField(verbose_name=u"Montant")
    number = peewee.ForeignKeyField(PhoneNumber, verbose_name=u"Téléphone",
                                   related_name='numbers')
    date = peewee.DateTimeField(verbose_name=u"Date")

    def __unicode__(self):
        return u"%(amount)s/%(number)s" % {"number": self.number,
                                             "amount": self.amount}

class Settings(BaseModel):
    password = peewee.CharField(max_length=30, verbose_name=(u"Nom"))
    password_orange = peewee.CharField(max_length=30,
                                       verbose_name=(u"Mot de passe Orange"))
    password_malitel = peewee.CharField(max_length=30,
                                       verbose_name=(u"Mot de passe Malitel"))
