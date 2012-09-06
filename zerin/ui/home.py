#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: Fadiga

from PySide import QtGui, QtCore
from datetime import datetime
from common import ZWidget, ZPageTitle, ZTableWidget, Button, ZBoxTitle
from database import Transfer, PhoneNumber, Operator


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

        phonenumber = self.verification_number(number)

        if phonenumber.operator.slug == 'orange':
            self.send_orange(phonenumber)
        elif phonenumber.operator.slug == 'malitel':
            self.send_malitel(phonenumber)

    def verification_number(self, number):
        """ Check number """
        try:
            return PhoneNumber.get(number=number)
        except:
            phonenumber = PhoneNumber()
            phonenumber.number = number
            if number.startswith('7'):
                phonenumber.operator = Operator.get(slug='orange')
            elif number.startswith('6'):
                phonenumber.operator = Operator.get(slug='malitel')
            phonenumber.contact = None
            phonenumber.save()

            return phonenumber

    def send_orange(self, number):
        """ Transfer credit Orange """

        self.transfer_credit(number)
        return u"function Orange"

    def send_malitel(self, number):
        """ Transfer credit Malitel """
        self.transfer_credit(number)
        return u"function Malitel"

    def transfer_credit(self, number):
        """ transfer amount credit"""
        date_send = datetime.now()
        amount =  self.amount.text()
        if amount:
            transfer = Transfer(amount=self.amount.text(), number=number,
                                date=date_send)

            transfer.save()

            self.number.setText(u"70.00.00.00")
            self.amount.clear()
            self.table.refresh_()
        else:
            print 'donner le montant'


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
        self._data = [(operation.number.full_name(), operation.amount,
                      operation.date.strftime(u'%d-%m-%Y')) \
                      for operation in Transfer.select().order_by('date')]

