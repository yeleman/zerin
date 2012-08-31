#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: Fadiga

from PySide import QtGui, QtCore
from datetime import datetime
from common import ZWidget, ZPageTitle, ZTableWidget, Button, ZBoxTitle
from database import Transfer, Contact


class HomeViewWidget(ZWidget):
    """ Shows the home page  """

    def __init__(self, parent=0, *args, **kwargs):
        super(HomeViewWidget, self).__init__(parent=parent,
                                                        *args, **kwargs)

        self.table = OperationTableWidget(parent=self)
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.table)

        splitter = QtGui.QSplitter(QtCore.Qt.Horizontal)

        splitter_left = QtGui.QSplitter(QtCore.Qt.Vertical)
        splitter_right = QtGui.QSplitter(QtCore.Qt.Vertical)

        splitter_left.addWidget(ZBoxTitle(u"Les groups"))
        splitter_left.addWidget(self.table)

        splitter.addWidget(splitter_left)
        splitter.addWidget(splitter_right)

        hbox.addWidget(splitter)

        self.parent = parent
        self.parentWidget().setWindowTitle(u"Bienvenu sur Zerin")
        self.title = ZPageTitle(u"Tranfert credit")
        self.order_number = QtGui.QLineEdit()

        # form transfer
        self.number = QtGui.QLineEdit()
        self.number.setInputMask("D9.99.99.99")
        self.number.setAlignment(QtCore.Qt.AlignCenter)
        self.number.setFont(QtGui.QFont("Arial", 18))
        self.number.setText(u"70.00.00.00")


        self.amount = QtGui.QLineEdit()
        self.amount.setValidator(QtGui.QIntValidator())
        butt = Button(u"OK")
        butt.clicked.connect(self.add_operation)


        formbox = QtGui.QGridLayout()
        formbox.addWidget(QtGui.QLabel((u'Numero')), 0, 0)
        formbox.addWidget(QtGui.QLabel((u'Montant')), 0, 1)
        formbox.addWidget(self.number, 1, 0)
        formbox.addWidget(self.amount, 1, 1)
        formbox.addWidget(butt, 1, 2)

        vbox = QtGui.QVBoxLayout()
        formbox.setSizeConstraint(QtGui.QLayout.SetFixedSize)

        vbox.addWidget(self.title)

        vbox.addLayout(formbox)
        formbox.addWidget(butt)

        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def add_operation(self):
        ''' add operation '''

        number = self.number.text().replace('.', '')

        contact = self.search_contact(number)
        if contact and contact.phone.operator.slug == 'orange':
            self.send_orange(contact, number)
            number = None
        elif contact and contact.phone.operator.slug == 'malitel':
            self.send_malitel(contact, number)
            number = None

        if number:
            slug =self.verification_number(number)

        if number and slug == 'orange':
            self.send_orange(contact, number)
        elif number and slug == 'malitel':
            self.send_malitel(contact, number)




    def verification_number(self, number):
        slug = ""
        if number.startswith('7'):
            slug = 'orange'
        if number.startswith('6'):
            slug = 'malitel'
        return slug

    def search_contact(self, number):

        try:
            contact = Contact.filter(phone__number=number).get()
        except:
            contact = None

        return contact


    def send_orange(self, contact, number):

        self.transfer_credit(contact, number)
        return u"function Orange"

    def send_malitel(self, contact, number):
        """  """
        self.transfer_credit(contact, number)
        return u"function Malitel"


    def transfer_credit(self, contact, number):
        """ transfer amount credit"""
        date_send = datetime.now()
        transfer = Transfer(amount=self.amount.text(), contact=contact,
                            date=date_send, number=number)

        transfer.save()
        self.number.setText(u"70.00.00.00")
        self.amount.clear()
        self.table.refresh_()
        return True

class OperationTableWidget(ZTableWidget):

    def __init__(self, parent, *args, **kwargs):

        ZTableWidget.__init__(self, parent=parent, *args, **kwargs)
        self.header = [(u'Contact'), (u'Montant'), \
                       (u'Heure')]

        self.set_data_for()
        self.refresh(True)

    def refresh_(self):
        self._reset()
        self.set_data_for()
        self.refresh(True)

    def set_data_for(self):
        self._data = [(operation.amount, operation.full_name(),\
                      operation.date.strftime(u'%d-%m-%Y')) \
                      for operation in Transfer.select()]

