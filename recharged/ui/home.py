#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: Fadiga

from PySide import QtGui
from datetime import datetime
from common import ZWidget, ZPageTitle, ZTableWidget
from database import Transfer, AddressBook, PhoneNumber


class HomeViewWidget(ZWidget):
    """ Shows the home page  """

    def __init__(self, parent=0, *args, **kwargs):
        super(HomeViewWidget, self).__init__(parent=parent,
                                                        *args, **kwargs)

        self.table = OperationTableWidget(parent=self)
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.table)

        self.parent = parent
        self.parentWidget().setWindowTitle(u"Bienvenu sur Zerin")
        self.title = ZPageTitle(u"Tranfer credit")
        self.order_number = QtGui.QLineEdit()

        # form transfer
        self.number = QtGui.QLineEdit()
        self.amount = QtGui.QLineEdit()
        self.number.setValidator(QtGui.QIntValidator())
        self.amount.setValidator(QtGui.QIntValidator())
        butt = QtGui.QPushButton((u"OK"))
        butt.clicked.connect(self.add_operation)


        formbox = QtGui.QGridLayout()
        formbox.addWidget(QtGui.QLabel((u'Number')), 0, 0)
        formbox.addWidget(QtGui.QLabel((u'Amount')), 0, 1)
        formbox.addWidget(self.number, 1, 0, 1, 2)
        formbox.addWidget(self.amount, 1, 1, 1, 2)
        formbox.addWidget(butt, 1, 2, 1, 2)

        vbox = QtGui.QVBoxLayout()
        formbox.setSizeConstraint(QtGui.QLayout.SetFixedSize)

        vbox.addWidget(self.title)

        vbox.addLayout(formbox)
        formbox.addWidget(butt)

        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def add_operation(self):
        ''' add operation '''

        number = self.number.text()
        for adressbook in AddressBook.all():
            number = self.number.text()
            contact = None
            if adressbook.phone.number == int(self.number.text()):
                contact = adressbook.phone
                number = None
                break

        date_ = datetime.now()

        transfer = Transfer(amount=self.amount.text(), contact=contact, date=date_, number=number)

        transfer.save()
        self.table.refresh_()


class OperationTableWidget(ZTableWidget):

    def __init__(self, parent, *args, **kwargs):

        ZTableWidget.__init__(self, parent=parent, *args, **kwargs)
        self.header = [(u'Amount'), (u'Contact'), \
                       (u'Date')]

        self.set_data_for()
        self.refresh(True)

    def refresh_(self):
        self._reset()
        self.set_data_for()
        self.refresh(True)

    def set_data_for(self):
        self._data = [(operation.amount, operation.sender(),\
                      operation.date.strftime(u'%d-%m-%Y')) \
                      for operation in Transfer.select()]

