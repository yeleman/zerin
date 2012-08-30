#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: Fadiga

from PySide import QtGui

from common import ZWidget, ZPageTitle, ZTableWidget


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
        self.title = ZPageTitle(u"Tranfert credit")
        self.order_number = QtGui.QLineEdit()

        # form transfer
        self.number = QtGui.QLineEdit()
        self.amount = QtGui.QLineEdit()
        self.amount.setValidator(QtGui.QIntValidator())
        butt = QtGui.QPushButton((u"OK"))
        butt.clicked.connect(self.add_operation)


        formbox = QtGui.QGridLayout()
        formbox.addWidget(QtGui.QLabel((u'number')), 0, 0)
        formbox.addWidget(QtGui.QLabel((u'Montant')), 0, 1)
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

        date_ = datetime(int(2012), int(1), int(21))
        contact = AddressBook.all()[0]

        transfer = Transfer(amount='1000', contact=contact, date=date_, number="")
        transfer.save()
        self.table.refresh(True)


class OperationTableWidget(ZTableWidget):

    def __init__(self, parent, *args, **kwargs):

        ZTableWidget.__init__(self, parent=parent, *args, **kwargs)
        self.header = [(u'Motant'), (u'Contact'), \
                       (u'Date'), (u'number')]

        self.set_data_for()
        self.refresh(True)

    def set_data_for(self):
        self._data = [(operation.amount, operation.contact,\
                      operation.date.strftime(u'%d-%m-%Y'),\
                      operation.number) \
                      for operation in Transfer.select()]

