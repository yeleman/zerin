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
    """ Group of contacts"""

    name = peewee.CharField(max_length=30, verbose_name=u"Nom")

    def __unicode__(self):
        return u"%(name)s" % {"name": self.name}


class Operator(BaseModel):
    """ Operators """
    id_ = peewee.CharField(max_length=30, verbose_name=u"ID")
    name = peewee.CharField(max_length=30, verbose_name=u"Nom")

    def __unicode__(self):
        return u"%(name)s/%(id_)s" % {"name": self.name, "id_": self.id_}


class PhoneNumber(BaseModel):
    """ Contact number """

    number = peewee.IntegerField(verbose_name=u"Numero de téléphone")
    operator = peewee.ForeignKeyField(Operator, verbose_name=u"Operateur")

    def __unicode__(self):
        return u"%(number)s" % {u"number": self.number}


class AddressBook(BaseModel):
    """ Address book """

    name = peewee.CharField(max_length=30, verbose_name=(u"Nom"), unique=True)
    phone = peewee.ForeignKeyField(PhoneNumber, verbose_name=u"Telephone")
    group = peewee.ForeignKeyField(GroupContact, verbose_name=u"Groupes")

    def __unicode__(self):
        return u"%(name)s" % {"name": self.name}


class Transfer(BaseModel):
    """ Ensemble des  transferts effectués """

    amount = peewee.IntegerField(verbose_name=u"Montant")
    contact = peewee.ForeignKeyField(AddressBook, verbose_name=u"Telephone",
                                     blank=True, null=True)
    date = peewee.DateTimeField(verbose_name=u"Date")
    number = peewee.IntegerField(verbose_name=u"Telephone",
                                     blank=True, null=True)

    def __unicode__(self):
        return u"%(amount)s/%(contact)s" % {"contact": self.contact,
                                             "amount": self.amount}

    def sender(self):
        """ choix du destinateur """
        pass


class Settings(BaseModel):
    password = peewee.CharField(max_length=30, verbose_name=(u"Nom"))
    password_orange = peewee.CharField(max_length=30,
                                       verbose_name=(u"Mot de passe Orange"))
    password_malitel = peewee.CharField(max_length=30,
                                       verbose_name=(u"Mot de passe Malitel"))
